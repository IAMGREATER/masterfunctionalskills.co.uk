/**
 * Master Functional Skills - Online Mock Exam Simulator Engine
 * Comprehensive multi-subject support for Mathematics (Sec A & Sec B),
 * English Writing (Tasks with live word counter & proofreading), and
 * English Reading (Source Insert tabs & reading comprehension).
 */

// Global State
let simCurrentPaperKey = 'edexcel-maths-l1-paper-1';
let simCurrentSectionIndex = 0; // 0 = Section A, 1 = Section B
let simCurrentQuestionIndex = 0; // 0 = Section Front Cover, 1 = Question 1, 2 = Question 2...
let simStartedSections = {}; // Tracks sections that have been opened: { 'A': true, 'B': true }
let simTimerSeconds = 25 * 60;
let simTimerActive = true;
let simTimerInterval = null;
let simActiveSourceTextTab = 0;
let sim5MinWarningShown = {}; // Tracks per-section 5-min warning
let simLockedSections = {}; // Tracks locked sections: { 'A': true, 'B': true }
let simPendingLockAction = null;

// Calculator state: live expression display until '=' is pressed
let calcExpression = '';
let calcResult = '0';
let calcJustEvaluated = false;

// Authenticated Mock Papers Database
const MFS_MOCK_DATA = {
  // =========================================================================
  // 1. PEARSON EDEXCEL FUNCTIONAL SKILLS MATHS LEVEL 1 - PAST PAPER 1
  // =========================================================================
  'edexcel-maths-l1-paper-1': {
    title: 'Edexcel Functional Skills Maths Level 1 — Past Paper 1',
    board: 'Pearson Edexcel',
    subject: 'maths',
    level: 'Level 1',
    paperNumber: 1,
    durationMinutes: 115,
    pdfUrl: 'https://passfunctionalskills.co.uk/app/uploads/2024/10/PAST_PAPER_1_FS_Maths_SecAB_PMAT1_N01_Level_1.pdf',
    modelSolutionPdf: 'assets/downloads/past-papers/edexcel/maths-level-1/FS_Maths_Level_1_Past_Paper_1_Model_Solution_MFS.pdf',
    videoSolutionSlug: '',
    sections: [
      {
        id: 'A',
        name: 'Section A: Non-Calculator',
        code: 'PMAT1/N01',
        durationMinutes: 25,
        totalMarks: 14,
        isCalcAllowed: false,
        questions: [
          {
            num: 1,
            section: 'Section A: Non-Calculator',
            isCalcAllowed: false,
            marks: 3,
            markTags: '[B1, B1, B1]',
            scenarioTitle: 'Core Arithmetic & Units Conversion',
            scenarioText: 'Answer all parts of Question 1 below without using a calculator.',
            promptText: '(a) Convert 3 metres into centimetres.\n(b) Work out 3400 ÷ 1000\n(c) Calculate 35 – 15 ÷ 5',
            unit: 'cm',
            expectedType: 'number',
            parts: [
              { id: 'a', label: 'Part (a)', placeholder: 'Centimetres', unit: 'cm' },
              { id: 'b', label: 'Part (b)', placeholder: '3400 ÷ 1000', unit: '' },
              { id: 'c', label: 'Part (c)', placeholder: '35 − 15 ÷ 5', unit: '' }
            ],
            modelSolution: '(a) 1 m = 100 cm --> 3 × 100 = 300 cm [B1]\n(b) 3400 ÷ 1000 = 3.4 [B1]\n(c) BIDMAS division first: 15 ÷ 5 = 3; then 35 - 3 = 32 [B1]',
            finalBenchmark: '300 cm / 3.4 / 32'
          },
          {
            num: 2,
            section: 'Section A: Non-Calculator',
            isCalcAllowed: false,
            marks: 3,
            markTags: '[M1, M1, A1]',
            scenarioTitle: 'Aaron\'s Brick Wall Construction',
            scenarioText: 'Aaron is building a brick wall. The wall will need 1025 bricks. The weight of each brick is 2.89 kg. Aaron will pay a delivery charge if the total weight of the bricks is over 2500 kg.',
            promptText: 'Use estimation to work out if you think Aaron will need to pay the delivery charge. You must show your working.',
            unit: '',
            expectedType: 'decision',
            modelSolution: 'Step 1: Round to 1 significant figure:\n  1025 ≈ 1000 bricks [M1]\n  2.89 kg ≈ 3 kg [M1]\nStep 2: Estimated total weight = 1000 × 3 = 3000 kg.\nStep 3: Compare with 2500 kg: 3000 > 2500.\nConclusion: Yes, Aaron will pay the delivery charge [A1].',
            finalBenchmark: 'Yes (estimated 3000 kg > 2500 kg)'
          },
          {
            num: 3,
            section: 'Section A: Non-Calculator',
            isCalcAllowed: false,
            marks: 4,
            markTags: '[M1, A1, M1, A1]',
            scenarioTitle: 'Farmer\'s Rectangular Field & Fertiliser',
            scenarioText: 'A farmer has a rectangular field. The field is 300 m long and 200 m wide. The farmer puts fertiliser on the field. He needs 1 kg of fertiliser for every 40 m² of field.',
            promptText: '(a) Calculate the perimeter of the field.\n(b) How many kilograms of fertiliser does the farmer need?',
            unit: 'kg',
            expectedType: 'number',
            parts: [
              { id: 'a', label: 'Part (a) Perimeter', placeholder: 'Perimeter of field', unit: 'm' },
              { id: 'b', label: 'Part (b) Fertiliser', placeholder: 'Fertiliser needed', unit: 'kg' }
            ],
            modelSolution: '(a) Perimeter = 2 × (300 + 200) = 2 × 500 = 1000 m [M1, A1]\n(b) Area = 300 × 200 = 60,000 m² [M1]\nFertiliser needed = 60,000 ÷ 40 = 1500 kg [A1]',
            finalBenchmark: '1000 m / 1500 kg'
          },
          {
            num: 4,
            section: 'Section A: Non-Calculator',
            isCalcAllowed: false,
            marks: 4,
            markTags: '[M1, M1, M1, A1]',
            scenarioTitle: '5-Year Car Value Comparison (Petrol vs. Diesel)',
            scenarioText: 'Saira is buying a new car and will keep it for 5 years.\n• Petrol car: Buying price £14,500; Average running cost £775 per year.\n• Diesel car: Buying price £15,800; Average running cost £520 per year.',
            promptText: 'Which type of car is better value for the 5 years? Show why you think this.',
            unit: '£',
            expectedType: 'text',
            modelSolution: 'Petrol car 5-year cost: £14,500 + (5 × £775) = £14,500 + £3,875 = £18,375 [M1]\nDiesel car 5-year cost: £15,800 + (5 × £520) = £15,800 + £2,600 = £18,400 [M1]\nComparison: £18,375 < £18,400 (Difference: £25) [M1]\nConclusion: The Petrol car is better value by £25 [A1].',
            finalBenchmark: 'Petrol car (cheaper by £25)'
          }
        ]
      },
      {
        id: 'B',
        name: 'Section B: Calculator',
        code: 'PMAT1/C01',
        durationMinutes: 90,
        totalMarks: 42,
        isCalcAllowed: true,
        questions: [
          {
            num: 1,
            section: 'Section B: Calculator',
            isCalcAllowed: true,
            marks: 3,
            markTags: '[M1, A1, B1]',
            scenarioTitle: 'Cafe Drinks Ratio & Check',
            scenarioText: 'Johan works in a cafe. One morning he sells 48 cups of tea and 12 cups of coffee.',
            promptText: '(a) Write the ratio of the number of cups of tea to the number of cups of coffee in its simplest form.\n(b) Show a check of your answer.',
            unit: '',
            expectedType: 'text',
            parts: [
              { id: 'a', label: 'Part (a) Simplest Ratio', placeholder: 'e.g. 4 : 1', unit: '' },
              { id: 'b', label: 'Part (b) Reverse Check', placeholder: 'e.g. 4 × 12 = 48', unit: '' }
            ],
            modelSolution: '(a) Ratio Tea : Coffee = 48 : 12 [M1]\nDivide both by 12: 4 : 1 [A1]\n(b) Reverse check: 4 × 12 = 48 [B1]',
            finalBenchmark: '4 : 1'
          },
          {
            num: 2,
            section: 'Section B: Calculator',
            isCalcAllowed: true,
            marks: 3,
            markTags: '[M1, M1, A1]',
            scenarioTitle: 'Office Chairs & 20% VAT',
            scenarioText: 'Sam is a manager in an office. She wants to buy 14 new chairs. Each chair costs £73. Sam will also be charged 20% VAT.',
            promptText: 'Work out the total amount Sam will pay for the 14 chairs including VAT.',
            unit: '£',
            expectedType: 'number',
            modelSolution: 'Step 1: Subtotal before VAT = 14 × £73 = £1,022 [M1]\nStep 2: 20% VAT = 0.20 × £1,022 = £204.40 [M1]\nStep 3: Total = £1,022 + £204.40 = £1,226.40 [A1]',
            finalBenchmark: '£1226.40'
          },
          {
            num: 3,
            section: 'Section B: Calculator',
            isCalcAllowed: true,
            marks: 4,
            markTags: '[M1, M1, M1, A1]',
            scenarioTitle: 'Garden & Pond Grass Seed Calculation',
            scenarioText: 'Here is a garden and a pond. Both are rectangular.\n• Garden dimensions: 14 m by 9 m\n• Pond dimensions: 3.8 m by 2.4 m\nKayla will cover the garden with grass seed (excluding the pond). One box of seed covers 15 m².',
            promptText: 'Work out the number of boxes of grass seed Kayla needs to cover the garden.',
            unit: 'boxes',
            expectedType: 'number',
            modelSolution: 'Step 1: Garden Area = 14 × 9 = 126 m² [M1]\nStep 2: Pond Area = 3.8 × 2.4 = 9.12 m² [M1]\nStep 3: Grass Area = 126 - 9.12 = 116.88 m²\nStep 4: Boxes = 116.88 ÷ 15 = 7.792... boxes [M1]\nRound up to whole boxes: 8 boxes [A1]',
            finalBenchmark: '8 boxes'
          },
          {
            num: 4,
            section: 'Section B: Calculator',
            isCalcAllowed: true,
            marks: 3,
            markTags: '[M1, M1, A1]',
            scenarioTitle: 'Madrid Holiday Temperature Formula',
            scenarioText: 'Dave is going on holiday to Madrid. The temperature tomorrow in Madrid will be 21 °C. Dave uses this rule:\n"Multiply temperature in °C by 1.8 then add 32"',
            promptText: 'Work out the temperature in Madrid in °F.',
            unit: '°F',
            expectedType: 'number',
            modelSolution: 'Step 1: 21 × 1.8 = 37.8 [M1]\nStep 2: 37.8 + 32 = 69.8 °F [M1, A1]',
            finalBenchmark: '69.8 °F'
          },
          {
            num: 5,
            section: 'Section B: Calculator',
            isCalcAllowed: true,
            marks: 4,
            markTags: '[M1, A1, M1, A1]',
            scenarioTitle: 'Call Centre Daily Phone Calls Analysis',
            scenarioText: 'Kai works in a call centre. Phone calls received:\nMonday: 240, Tuesday: 140, Wednesday: 185, Thursday: 80, Friday: 225.',
            promptText: '(a) Work out the total number of calls received over the 5 days.\n(b) Work out the range of the number of phone calls.',
            unit: 'calls',
            expectedType: 'number',
            parts: [
              { id: 'a', label: 'Part (a) Total Calls', placeholder: 'Total calls over 5 days', unit: 'calls' },
              { id: 'b', label: 'Part (b) Range', placeholder: 'Range of calls', unit: 'calls' }
            ],
            modelSolution: '(a) Total = 240 + 140 + 185 + 80 + 225 = 870 calls [M1, A1]\n(b) Range = Highest - Lowest = 240 - 80 = 160 calls [M1, A1]',
            finalBenchmark: '870 calls / Range: 160'
          },
          {
            num: 6,
            section: 'Section B: Calculator',
            isCalcAllowed: true,
            marks: 4,
            markTags: '[M1, M1, M1, A1]',
            scenarioTitle: 'Bakery Weekly Mean Flour Consumption',
            scenarioText: 'Seenal buys flour in 50 kg bags. Bags used:\nWeek 1: 12, Week 2: 16, Week 3: 13, Week 4: 15.\nIn Week 5, she bakes 2400 loaves, each needing 250 g of flour.',
            promptText: 'Work out the weekly mean number of 50 kg bags of flour used across the 5 weeks.',
            unit: 'bags',
            expectedType: 'number',
            modelSolution: 'Step 1: Week 5 flour = 2400 × 250 g = 600,000 g = 600 kg [M1]\nWeek 5 bags = 600 ÷ 50 = 12 bags [M1]\nStep 2: Total bags = 12 + 16 + 13 + 15 + 12 = 68 bags\nStep 3: Mean = 68 ÷ 5 = 13.6 bags [M1, A1]',
            finalBenchmark: '13.6 bags'
          },
          {
            num: 7,
            section: 'Section B: Calculator',
            isCalcAllowed: true,
            marks: 3,
            markTags: '[A1, B1, C1]',
            scenarioTitle: 'Gordon\'s Garden Slide Scale Plan',
            scenarioText: 'Gordon buys a new slide for his garden. His garden measures 6 m by 7 m.\nThe space for the slide must be:\n• a rectangle, 3 m by 1.5 m\n• at least 2 m away from the house\n• at least 0.5 m away from a fence or any other feature.\nKey: 1 cm on the grid represents 50 cm in the garden.',
            promptText: 'Work out the dimensions of the slide space on the grid in squares (1 square = 50 cm), and confirm the clearance distances from the house and shed/fence.',
            unit: 'squares',
            expectedType: 'text',
            parts: [
              { id: 'length', label: 'Grid Length', placeholder: 'Length in squares (3 m ÷ 50 cm)', unit: 'squares' },
              { id: 'width', label: 'Grid Width', placeholder: 'Width in squares (1.5 m ÷ 50 cm)', unit: 'squares' },
              { id: 'clearance', label: 'House Clearance', placeholder: 'Distance from house', unit: 'm' }
            ],
            modelSolution: 'Step 1: Length in squares = 300 cm ÷ 50 cm = 6 squares [A1]\nStep 2: Width in squares = 150 cm ÷ 50 cm = 3 squares [A1]\nStep 3: Distance from house >= 2.0 m (>= 4 squares) [C1]\nStep 4: Distance from fence/shed >= 0.5 m (>= 1 square) [B1]',
            finalBenchmark: '6 squares by 3 squares (>= 2 m from house)'
          },
          {
            num: 8,
            section: 'Section B: Calculator',
            isCalcAllowed: true,
            marks: 3,
            markTags: '[A1, B1, C1]',
            scenarioTitle: 'Belinda\'s TV Watching Hours Grouped Data',
            scenarioText: 'Belinda asks 20 people: ‘How many hours of TV did you watch last week?’\nResults: 3, 17, 4, 4, 6, 11, 14, 14, 1, 20, 9, 8, 9, 6, 12, 7, 8, 13, 13, 9.\nBelinda wants to show these results in a frequency table with 4 equal groups starting with 1 hour and ending with 20 hours.',
            promptText: 'Complete the frequency table for the 4 groups: 1 to 5, 6 to 10, 11 to 15, and 16 to 20.',
            unit: '',
            expectedType: 'text',
            parts: [
              { id: 'g1', label: 'Group 1 to 5', placeholder: 'Count of values 1 to 5', unit: 'people' },
              { id: 'g2', label: 'Group 6 to 10', placeholder: 'Count of values 6 to 10', unit: 'people' },
              { id: 'g3', label: 'Group 11 to 15', placeholder: 'Count of values 11 to 15', unit: 'people' },
              { id: 'g4', label: 'Group 16 to 20', placeholder: 'Count of values 16 to 20', unit: 'people' }
            ],
            modelSolution: 'Group 1 to 5: 3, 4, 4, 1 --> Frequency = 4 [A1]\nGroup 6 to 10: 6, 9, 8, 9, 6, 7, 8, 9 --> Frequency = 8 [B1]\nGroup 11 to 15: 11, 14, 14, 12, 13, 13 --> Frequency = 6 [C1]\nGroup 16 to 20: 17, 20 --> Frequency = 2 [C1]\nTotal Frequency = 4 + 8 + 6 + 2 = 20',
            finalBenchmark: '1–5: 4  |  6–10: 8  |  11–15: 6  |  16–20: 2'
          },
          {
            num: 9,
            section: 'Section B: Calculator',
            isCalcAllowed: true,
            marks: 4,
            markTags: '[A1, B1, M1, D1]',
            scenarioTitle: 'Cuboid Tomato Container Dimensions',
            scenarioText: 'Dennis is making a cuboid plant container with capacity 180 litres (1 litre = 1000 cm³). The height is 40 cm and width is 55 cm.',
            promptText: 'Work out the length of the container to the nearest whole centimetre.',
            unit: 'cm',
            expectedType: 'number',
            modelSolution: 'Step 1: Volume = 180 × 1000 = 180,000 cm³ [A1]\nStep 2: Base cross-section = 55 × 40 = 2,200 cm² [B1]\nStep 3: Length = 180,000 ÷ 2,200 = 81.818... cm [M1]\nStep 4: Round to nearest whole cm: 82 cm [D1]',
            finalBenchmark: '82 cm'
          },
          {
            num: 10,
            section: 'Section B: Calculator',
            isCalcAllowed: true,
            marks: 3,
            markTags: '[A1, B1, C1]',
            scenarioTitle: '3-D Shapes: Geometric Nets & Plan Views',
            scenarioText: '(a) Match each 3-D shape to its geometric properties:\n• Cube (6 identical square faces)\n• Triangular prism (2 triangular bases + 3 rectangular faces)\n• Square-based pyramid (1 square base + 4 triangular faces)\n(b) Here is a cylinder. Plan view is the view looking directly from above.',
            promptText: '(a) Identify the shape of the faces and net for the Cube, Triangular Prism, and Square-based Pyramid.\n(b) Which 2-D shape is the plan view of a cylinder?',
            unit: '',
            expectedType: 'text',
            parts: [
              { id: 'cube', label: 'Cube Net', placeholder: 'Faces on cube net', unit: '' },
              { id: 'triPrism', label: 'Triangular Prism Net', placeholder: 'Faces on prism net', unit: '' },
              { id: 'pyramid', label: 'Pyramid Net', placeholder: 'Faces on pyramid net', unit: '' },
              { id: 'planView', label: 'Cylinder Plan View', placeholder: 'Shape seen from above', unit: '' }
            ],
            modelSolution: '(a) Cube net consists of 6 square faces [A1]; Triangular prism net consists of 2 triangles and 3 rectangles [B1]; Square-based pyramid net consists of 1 square and 4 triangles [B1]\n(b) The plan view of a vertical cylinder viewed directly from above is a Circle [C1]',
            finalBenchmark: 'Cube (6 sq), Prism (2 tri + 3 rect), Pyramid (1 sq + 4 tri), Plan view: Circle'
          },
          {
            num: 11,
            section: 'Section B: Calculator',
            isCalcAllowed: true,
            marks: 5,
            markTags: '[A1, M1, M1, A1, B1]',
            scenarioTitle: 'James House Purchase Deposit Calculation',
            scenarioText: 'James wants to buy a house priced at a quarter of a million pounds (£250,000). The deposit is 15%. James already has £32,000 saved.',
            promptText: '(a) How much more money does James need for the deposit?\n(b) Show a check of your percentage calculation.',
            unit: '£',
            expectedType: 'decision',
            parts: [
              { id: 'extra', label: 'Extra Money Needed', placeholder: 'e.g. 5500', unit: '£' },
              { id: 'check', label: 'Percentage Check', placeholder: 'e.g. 10% = 25000, 5% = 12500', unit: '' }
            ],
            modelSolution: 'Step 1: House price = £250,000 [A1]\nStep 2: 15% Deposit = 0.15 × £250,000 = £37,500 [M1]\nStep 3: Extra needed = £37,500 - £32,000 = £5,500 [M1, A1]\nStep 4: Check: 10% = £25,000; 5% = £12,500; £25,000 + £12,500 = £37,500 [B1]',
            finalBenchmark: '£5,500 extra needed (Deposit: £37,500)'
          }
        ]
      }
    ]
  },

  // =========================================================================
  // =========================================================================
  // 1B. PEARSON EDEXCEL FUNCTIONAL SKILLS MATHS LEVEL 2 - PAST PAPER 1
  // =========================================================================
  'edexcel-maths-l2-paper-1': {
    title: 'Edexcel Functional Skills Maths Level 2 — Past Paper 1',
    board: 'Pearson Edexcel',
    subject: 'maths',
    level: 'Level 2',
    paperNumber: 1,
    durationMinutes: 115,
    pdfUrl: 'https://passfunctionalskills.co.uk/app/uploads/2024/01/Edexcel-Functional-Skills-Maths-Level-2-Past-Paper-1-QP.pdf',
    modelSolutionPdf: 'assets/downloads/past-papers/edexcel/maths-level-2/FS_Maths_Level_2_Past_Paper_1_Model_Solution_MFS.pdf',
    videoSolutionSlug: 'edexcel-maths-l2-past-paper-1-section-a',
    sections: [
      {
        id: 'A',
        name: 'Section A: Non-Calculator',
        code: 'PMAT2/N01',
        durationMinutes: 25,
        totalMarks: 16,
        isCalcAllowed: false,
        instructions: 'Calculators may NOT be used. Check your working and your answers at each stage.',
        questions: [
          {
            num: 1,
            section: 'Section A: Non-Calculator',
            isCalcAllowed: false,
            marks: 3,
            markTags: '[M1, A1, B1]',
            scenarioTitle: 'Decimals & Indices',
            scenarioText: 'Answer all parts of Question 1 below without using a calculator.',
            promptText: '(a) Work out 5.2 × 9.6\n(b) Work out 4 × 3²',
            unit: '',
            expectedType: 'number',
            parts: [
              { id: 'a', label: 'Part (a) 5.2 × 9.6', placeholder: 'e.g. 49.92', unit: '' },
              { id: 'b', label: 'Part (b) 4 × 3²', placeholder: 'e.g. 36', unit: '' }
            ],
            modelSolution: '(a) Multiply as whole numbers: 52 × 96 = 4992. Total of 2 decimal places: 4992 ÷ 100 = 49.92 [M1, A1]\n(b) BIDMAS indices first: 3² = 9. Then 4 × 9 = 36 [B1]',
            finalBenchmark: '49.92 / 36'
          },
          {
            num: 2,
            section: 'Section A: Non-Calculator',
            isCalcAllowed: false,
            marks: 3,
            markTags: '[M1, M1, A1]',
            scenarioTitle: 'Malcolm Overdraft and Banking',
            scenarioText: 'On Thursday evening Malcolm’s bank balance was −£107.35.\nOn Friday morning:\n• £1867.68 is paid into his bank account\n• £715.21 is paid out of his bank account.\nNo other payments occur.',
            promptText: 'Work out how much money is in Malcolm’s bank account on Friday evening.',
            unit: '£',
            expectedType: 'number',
            parts: [
              { id: 'balance', label: 'Friday Evening Balance', placeholder: 'e.g. 1045.12', unit: '£' }
            ],
            modelSolution: 'Step 1: Balance after deposit = −107.35 + 1867.68 = 1867.68 − 107.35 = £1760.33 [M1]\nStep 2: Balance after withdrawal = 1760.33 − 715.21 = £1045.12 [M1, A1]',
            finalBenchmark: '£1045.12'
          },
          {
            num: 3,
            section: 'Section A: Non-Calculator',
            isCalcAllowed: false,
            marks: 4,
            markTags: '[M1, M1, M1, A1]',
            scenarioTitle: 'Akash Window Plastic Trim Estimation',
            scenarioText: 'Akash needs to put plastic trim on a shaped window. The window is made using a rectangle (height 172 cm, width 118 cm, inner vertical divider 113 cm, lower side segments 59 cm) and a semi-circle on top (diameter 118 cm).\nAkash estimates that he will need 700 cm of plastic trim in total.',
            promptText: 'Use estimation to check if Akash’s estimate is sensible. You must show your working.',
            unit: '',
            expectedType: 'decision',
            parts: [
              { id: 'decision', label: 'Is the estimate sensible?', placeholder: 'State Yes/No and show estimated total length', unit: '' }
            ],
            modelSolution: 'Step 1: Round measurements to 1 or 2 sig figs: 172 ≈ 170, 118 ≈ 120, 113 ≈ 110, 59 ≈ 60, π ≈ 3 [M1]\nStep 2: Semi-circle curved arc = (π × d) ÷ 2 ≈ (3 × 120) ÷ 2 = 180 cm [M1]\nStep 3: Total estimated trim = 170 + 120 + 60 + 110 + 180 ≈ 640 cm (or rectangle perimeter parts + arc ≈ 540–640 cm) [M1]\nStep 4: 700 cm is an overestimate. Conclusion: Akash’s estimate is not sensible [A1].',
            finalBenchmark: 'No (Sensible estimate is approx 540–640 cm)'
          },
          {
            num: 4,
            section: 'Section A: Non-Calculator',
            isCalcAllowed: false,
            marks: 6,
            markTags: '[M1, A1, M1, A1, C1, C1]',
            scenarioTitle: 'Calvin Train Arrival Times (Summer vs. Winter)',
            scenarioText: 'Calvin is a train company manager. He compares the arrival times of a morning train service for 10 days in the summer and 10 days in the winter.\n• Summer: Median late = 12.7 minutes; Range = 11 minutes.\n• Winter late minutes: 8, 32, 44, 5, 17, 67, 9, 14, 10, 26.\n\nCalvin thinks that in the winter:\n• the median number of minutes late increases\n• the train service is less consistent.',
            promptText: 'Is Calvin correct? Show why you think this giving reasons with your answers.',
            unit: '',
            expectedType: 'text',
            parts: [
              { id: 'median', label: 'Winter Median (mins)', placeholder: 'e.g. 15.5', unit: 'mins' },
              { id: 'range', label: 'Winter Range (mins)', placeholder: 'e.g. 62', unit: 'mins' },
              { id: 'conclusion', label: 'Conclusion (Is Calvin correct?)', placeholder: 'Explain whether Calvin is correct on median and consistency', unit: '' }
            ],
            modelSolution: 'Step 1: Order winter data: 5, 8, 9, 10, 14, 17, 26, 32, 44, 67 [M1]\nStep 2: Winter Median = (14 + 17) ÷ 2 = 15.5 minutes [A1]\nStep 3: Winter Range = 67 − 5 = 62 minutes [M1, A1]\nStep 4: Median comparison: 15.5 > 12.7, so median minutes late did increase (Calvin correct) [C1]\nStep 5: Consistency comparison: 62 > 11, so winter has greater spread / is less consistent (Calvin correct) [C1]',
            finalBenchmark: 'Winter Median: 15.5 mins; Winter Range: 62 mins; Calvin is correct on both points'
          }
        ]
      },
      {
        id: 'B',
        name: 'Section B: Calculator',
        code: 'PMAT2/C01',
        durationMinutes: 90,
        totalMarks: 48,
        isCalcAllowed: true,
        instructions: 'Calculators may be used. Check your working and your answers at each stage.',
        questions: [
          {
            num: 1,
            section: 'Section B: Calculator',
            isCalcAllowed: true,
            marks: 3,
            markTags: '[M1, M1, A1]',
            scenarioTitle: 'Adam Agency Work Overtime Pay',
            scenarioText: 'Adam works for an agency. His normal hourly rate is £8.32.\nThe agency asks Adam to work 6 hours for a new company.\nAdam will be paid time and a third of his normal hourly rate.',
            promptText: 'How much will Adam get paid in total when working for the new company?',
            unit: '£',
            expectedType: 'number',
            parts: [
              { id: 'pay', label: 'Total Pay', placeholder: 'e.g. 66.56', unit: '£' }
            ],
            modelSolution: 'Overtime rate = 8.32 × (1 + 1/3) = 8.32 × 4/3 = £11.0933... [M1]\nTotal pay for 6 hours = £11.0933... × 6 = £66.56 [M1, A1]',
            finalBenchmark: '£66.56'
          },
          {
            num: 2,
            section: 'Section B: Calculator',
            isCalcAllowed: true,
            marks: 3,
            markTags: '[M1, M1, A1]',
            scenarioTitle: 'Square Based Pyramid Volume',
            scenarioText: 'Here is a square based pyramid. Base length = 8.5 cm, base width = 8.5 cm, vertical height = 12.6 cm.\nFormula: Volume of pyramid = 1/3 × area of base × height.',
            promptText: 'Work out the volume of this pyramid.',
            unit: 'cm³',
            expectedType: 'number',
            parts: [
              { id: 'volume', label: 'Pyramid Volume', placeholder: 'e.g. 303.45', unit: 'cm³' }
            ],
            modelSolution: 'Base Area = 8.5 × 8.5 = 72.25 cm² [M1]\nVolume = 1/3 × 72.25 × 12.6 = 303.45 cm³ [M1, A1]',
            finalBenchmark: '303.45 cm³'
          },
          {
            num: 3,
            section: 'Section B: Calculator',
            isCalcAllowed: true,
            marks: 4,
            markTags: '[M1, M1, A1, B1]',
            scenarioTitle: 'Rana Charities Donation & Reverse Check',
            scenarioText: 'Rana donated to 4 charities last year. She gave £175 to each of these charities.\nThis year Rana wants to donate the same total amount equally between 6 charities.\nEach charity will receive an equal amount.',
            promptText: '(a) How much will each charity receive this year?\n(b) Use reverse calculations to check your answer.',
            unit: '£',
            expectedType: 'number',
            parts: [
              { id: 'a', label: 'Part (a) Donation per charity', placeholder: 'e.g. 116.67', unit: '£' },
              { id: 'b', label: 'Part (b) Reverse check calculation', placeholder: 'e.g. 116.67 × 6 ≈ 700', unit: '' }
            ],
            modelSolution: '(a) Total amount donated = £175 × 4 = £700 [M1]\nEach of 6 charities receives = £700 ÷ 6 = £116.666... ≈ £116.67 [M1, A1]\n(b) Reverse check: 116.67 × 6 = £700.02 ≈ £700 (or 116.66 × 6 + 0.04 = 700) [B1]',
            finalBenchmark: '£116.67'
          },
          {
            num: 4,
            section: 'Section B: Calculator',
            isCalcAllowed: true,
            marks: 4,
            markTags: '[M1, M1, M1, A1]',
            scenarioTitle: 'Samir Roofer Roof Angle x',
            scenarioText: 'Samir is a roofer. Here is a section of a roof made from straight pieces of wood.\nSamir knows that:\n• the shaded triangle is an equilateral triangle\n• the line DB is a line of symmetry\n• the line ABC is a straight line.',
            promptText: 'Work out the size of angle x. You must show your working.',
            unit: '°',
            expectedType: 'number',
            parts: [
              { id: 'angle', label: 'Angle x', placeholder: 'e.g. 30', unit: '°' }
            ],
            modelSolution: 'Step 1: All angles in an equilateral triangle are 60° [M1]\nStep 2: Line DB is a line of symmetry that bisects angle BDC (60° ÷ 2 = 30°) and forms a 90° right angle at B [M1]\nStep 3: Angle x = 180° − 90° − 60° = 30° (or symmetry bisects 60°) [M1, A1]',
            finalBenchmark: '30°'
          },
          {
            num: 5,
            section: 'Section B: Calculator',
            isCalcAllowed: true,
            marks: 5,
            markTags: '[M1, M1, M1, M1, A1]',
            scenarioTitle: 'Roof Tiles Cost for 4 Triangular Faces',
            scenarioText: 'Samir wants to work out the cost of the tiles needed to replace a roof.\nThe roof has 4 identical faces. Each face is a triangle with base 7.6 m and height 4.8 m.\n• 1 pack of tiles covers 13.8 m² (including overlaps)\n• Each pack costs £716.10\n• Samir can only buy whole packs of these tiles.',
            promptText: 'Calculate the total cost of the tiles for the 4 faces of this roof.',
            unit: '£',
            expectedType: 'number',
            parts: [
              { id: 'cost', label: 'Total Cost', placeholder: 'e.g. 4296.60', unit: '£' }
            ],
            modelSolution: 'Step 1: Area of 1 face = (7.6 × 4.8) ÷ 2 = 18.24 m² [M1]\nStep 2: Total area of 4 faces = 4 × 18.24 = 72.96 m² [M1]\nStep 3: Number of packs = 72.96 ÷ 13.8 = 5.286... packs [M1]\nStep 4: Must buy whole packs -> Round up to 6 packs [M1]\nStep 5: Total cost = 6 × £716.10 = £4296.60 [A1]',
            finalBenchmark: '£4296.60'
          },
          {
            num: 6,
            section: 'Section B: Calculator',
            isCalcAllowed: true,
            marks: 3,
            markTags: '[M1, M1, A1]',
            scenarioTitle: 'Farah Jacket Discount Percentage Claim',
            scenarioText: 'Farah is buying clothes from a website. The website shows this information about a jacket Farah wants to buy:\n• Jacket original price: £30.99\n• Sale price: £16.00\nThe website claims this is a saving of 46%.',
            promptText: 'Is the sale price a saving of 46% on the original price? Show why you think this.',
            unit: '',
            expectedType: 'decision',
            parts: [
              { id: 'decision', label: 'Is the claim correct?', placeholder: 'State Yes/No with calculated percentage or price', unit: '' }
            ],
            modelSolution: 'Method 1: Actual saving = £30.99 − £16.00 = £14.99 [M1]\nPercentage saving = (£14.99 ÷ £30.99) × 100 = 48.37%... [M1]\nComparison: 48.4% ≠ 46% (it is actually ~48% saving, not 46%). The claim is not correct [A1].\nMethod 2: 46% saving means paying 54%: £30.99 × 0.54 = £16.73, which is not £16.00.',
            finalBenchmark: 'No (Actual saving is 48.4%, or £16.73 at 46% off)'
          },
          {
            num: 7,
            section: 'Section B: Calculator',
            isCalcAllowed: true,
            marks: 4,
            markTags: '[M1, A1, M1, A1]',
            scenarioTitle: 'Scale Drawing Quadrilateral & Actual Length AD',
            scenarioText: 'Here is a quadrilateral ABCD. AB = 160 m, BC = 220 m, CD = 340 m with right angles as marked.\n(a) Draw this shape on the grid using scale 1 cm to 40 m.\n(b) Use your answer to part (a) to work out the actual length of the line AD.',
            promptText: 'Work out the actual length of the line AD. Remember to use the grid and the scale.',
            unit: 'm',
            expectedType: 'number',
            parts: [
              { id: 'a', label: 'Part (a) Grid Scale check', placeholder: 'AB = 4 cm, BC = 5.5 cm, CD = 8.5 cm', unit: '' },
              { id: 'b', label: 'Part (b) Actual length AD', placeholder: 'e.g. 270', unit: 'm' }
            ],
            modelSolution: '(a) Grid plotting: AB = 160 ÷ 40 = 4 cm (4 squares); BC = 220 ÷ 40 = 5.5 cm; CD = 340 ÷ 40 = 8.5 cm [M1, A1]\n(b) Measured distance AD on grid = 6.75 cm (acceptable 6.5 cm to 7.0 cm) [M1]\nActual length AD = 6.75 × 40 = 270 m (acceptable range 260 m to 280 m) [A1]',
            finalBenchmark: '270 m (260 m to 280 m)'
          },
          {
            num: 8,
            section: 'Section B: Calculator',
            isCalcAllowed: true,
            marks: 6,
            markTags: '[M1, A1, B1, M1, A1, B1]',
            scenarioTitle: 'Pablo European Land Area vs. Population Scatter Graph',
            scenarioText: 'Pablo is investigating the relationship between land area (1000 km²) and population (millions) of 8 European countries:\n• Germany (357, 82.8), Greece (132, 10.7), Italy (301, 60.5), Poland (313, 38.0), Spain (506, 46.7), France (552, 67.2), Romania (238, 19.5), UK (243, 66.3).',
            promptText: '(a) Plot points on the scatter diagram.\n(b) What type of correlation does the scatter diagram show?\n(c) Draw a line of best fit and estimate the population for a country with land area 450,000 km².',
            unit: 'millions',
            expectedType: 'text',
            parts: [
              { id: 'b', label: 'Part (b) Correlation Type', placeholder: 'e.g. Positive correlation', unit: '' },
              { id: 'c', label: 'Part (c) Estimated Population (millions)', placeholder: 'e.g. 58', unit: 'millions' }
            ],
            modelSolution: '(a) All 8 points correctly plotted on scatter diagram axes [M1, A1]\n(b) Positive correlation (as land area increases, population tends to increase) [B1]\n(c) Straight line of best fit drawn passing through the centroid [M1]; Reading at 450 (1000 km²) gives approx 55 to 65 million [A1, B1]',
            finalBenchmark: 'Positive correlation; Estimate 55–65 million'
          },
          {
            num: 9,
            section: 'Section B: Calculator',
            isCalcAllowed: true,
            marks: 4,
            markTags: '[M1, M1, M1, A1]',
            scenarioTitle: 'Magda Population Density Formula (Russia vs. Canada)',
            scenarioText: 'Magda compares the population density of Canada and Russia using the formula:\nK = P / (2.59 × M)\nwhere K = population density (people per km²), P = population (millions), M = land area (million square miles).\n• Canada has density 3.57 people per km²\n• Russia: Population P = 143.96 million, Land area M = 6.593 million sq miles.\nMagda thinks Russia has a greater population density than Canada.',
            promptText: 'Is Magda correct? Show why you think this.',
            unit: '',
            expectedType: 'decision',
            parts: [
              { id: 'russia_density', label: 'Russia Density (people/km²)', placeholder: 'e.g. 8.43', unit: 'people/km²' },
              { id: 'decision', label: 'Is Magda correct?', placeholder: 'State Yes/No with explanation', unit: '' }
            ],
            modelSolution: 'Step 1: Denominator = 2.59 × 6.593 = 17.07587 [M1]\nStep 2: Russia Density K = 143.96 ÷ 17.07587 = 8.4309... ≈ 8.43 people per km² [M1, M1]\nStep 3: Comparison: 8.43 > 3.57. Magda is correct; Russia has a greater population density [A1].',
            finalBenchmark: 'Yes (Russia density 8.43 > Canada 3.57)'
          },
          {
            num: 10,
            section: 'Section B: Calculator',
            isCalcAllowed: true,
            marks: 3,
            markTags: '[M1, A1, B1]',
            scenarioTitle: 'Mixed Number Fraction Subtraction & Estimation Check',
            scenarioText: 'Answer both parts of Question 10 below.',
            promptText: '(a) Work out 3 3/8 − 9/10. Give your answer as a mixed number.\n(b) Use estimation to show a check of your answer.',
            unit: '',
            expectedType: 'text',
            parts: [
              { id: 'a', label: 'Part (a) Mixed number answer', placeholder: 'e.g. 2 19/40 (or 2.475)', unit: '' },
              { id: 'b', label: 'Part (b) Estimation check', placeholder: 'e.g. 3.5 − 1 = 2.5', unit: '' }
            ],
            modelSolution: '(a) Convert to improper fractions: 3 3/8 = 27/8. Common denominator is 40: (27 × 5)/40 − (9 × 4)/40 = 135/40 − 36/40 = 99/40 [M1]\nConvert to mixed number: 99 ÷ 40 = 2 with remainder 19 -> 2 19/40 (or 2.475) [A1]\n(b) Estimation check: 3 3/8 ≈ 3.5; 9/10 ≈ 1.0; 3.5 − 1.0 = 2.5 (consistent with 2.475) [B1]',
            finalBenchmark: '2 19/40 (or 2.475) / Check: 3.5 − 1 = 2.5'
          },
          {
            num: 11,
            section: 'Section B: Calculator',
            isCalcAllowed: true,
            marks: 5,
            markTags: '[M1, M1, M1, M1, A1]',
            scenarioTitle: 'Emilio Metal Fences Ratio 9 : 8 : 7',
            scenarioText: 'Emilio makes metal fences. He is making a fence using this design:\n• 3 horizontal metal pieces of length 1.8 m\n• 2 tall metal pieces of length 1.44 m\n• 5 medium metal pieces\n• 6 short metal pieces\nThe heights of the tall, medium and short metal pieces are in the ratio 9 : 8 : 7.',
            promptText: 'How many metres of metal in total does Emilio need to make the fence?',
            unit: 'm',
            expectedType: 'number',
            parts: [
              { id: 'total_metal', label: 'Total metres of metal', placeholder: 'e.g. 21.4', unit: 'm' }
            ],
            modelSolution: 'Step 1: 1 ratio part = 1.44 ÷ 9 = 0.16 m [M1]\nStep 2: Medium height = 8 × 0.16 = 1.28 m; Short height = 7 × 0.16 = 1.12 m [M1]\nStep 3: Horizontal = 3 × 1.8 = 5.4 m; Tall = 2 × 1.44 = 2.88 m [M1]\nStep 4: Medium = 5 × 1.28 = 6.4 m; Short = 6 × 1.12 = 6.72 m [M1]\nStep 5: Total metal = 5.4 + 2.88 + 6.4 + 6.72 = 21.4 m [A1]',
            finalBenchmark: '21.4 m'
          },
          {
            num: 12,
            section: 'Section B: Calculator',
            isCalcAllowed: true,
            marks: 6,
            markTags: '[M1, A1, M1, A1, M1, A1]',
            scenarioTitle: 'Two-Way Table of 60 Holidays & Probability',
            scenarioText: 'The table shows information about 60 holidays bought by customers at a travel agency:\n• Customer types: Couples (Total 36), Families (Total 24)\n• Holiday types: Room only (Total 15; Couples 8, Families 7), Bed & breakfast (Total 21; Couples 14, Families 7), All-inclusive (Total 24; Couples 14, Families 10).\n(a) Complete the table.\n(b) What is the probability that a randomly chosen customer bought an all-inclusive holiday for a couple? Give answer as a fraction in simplest form.\n(c) The travel agent says: "Of the couples and families who bought holidays, couples were more likely to have bought an all-inclusive holiday." Is the agent correct?',
            promptText: 'Answer all parts: table values, simplified probability fraction, and whether travel agent is correct.',
            unit: '',
            expectedType: 'text',
            parts: [
              { id: 'b_prob', label: 'Part (b) Probability fraction', placeholder: 'e.g. 7/30', unit: '' },
              { id: 'c_decision', label: 'Part (c) Is travel agent correct?', placeholder: 'State Yes/No with percentages or fractions', unit: '' }
            ],
            modelSolution: '(a) Table completion: Couples: Room 8, B&B 14, All-inc 14, Total 36; Families: Room 7, B&B 7, All-inc 10, Total 24; Totals: 15, 21, 24, 60 [M1, A1]\n(b) P(Couple and All-inclusive) = 14 / 60 = 7 / 30 [M1, A1]\n(c) Couples all-inclusive proportion = 14 / 36 = 7 / 18 ≈ 38.9%\nFamilies all-inclusive proportion = 10 / 24 = 5 / 12 ≈ 41.7% [M1]\nComparison: 38.9% < 41.7%, so families were actually more likely. Travel agent is incorrect [A1].',
            finalBenchmark: 'Table completed / 7/30 / Travel agent is incorrect (Couples 38.9% < Families 41.7%)'
          }
        ]
      }
    ]
  },

  // =========================================================================
  // 1C. PEARSON EDEXCEL FUNCTIONAL SKILLS MATHS LEVEL 2 - PAST PAPER 2
  // =========================================================================
  'edexcel-maths-l2-paper-2': {
    title: 'Edexcel Functional Skills Maths Level 2 — Past Paper 2',
    board: 'Pearson Edexcel',
    subject: 'maths',
    level: 'Level 2',
    paperNumber: 2,
    durationMinutes: 115,
    pdfUrl: 'https://passfunctionalskills.co.uk/app/uploads/2024/01/Edexcel-Functional-Skills-Maths-Level-2-Past-Paper-2-QP.pdf',
    modelSolutionPdf: 'assets/downloads/past-papers/edexcel/maths-level-2/FS_Maths_Level_2_Past_Paper_2_Model_Solution_MFS.pdf',
    videoSolutionSlug: 'edexcel-maths-l2-past-paper-2-section-a',
    sections: [
      {
        id: 'A',
        name: 'Section A: Non-Calculator',
        code: 'PMAT2/N02',
        durationMinutes: 25,
        totalMarks: 16,
        isCalcAllowed: false,
        instructions: 'Calculators may NOT be used. Check your working and your answers at each stage.',
        questions: [
          {
            num: 1,
            section: 'Section A: Non-Calculator',
            isCalcAllowed: false,
            marks: 3,
            markTags: '[M1, A1, B1]',
            scenarioTitle: 'Median & Modal Race Times',
            scenarioText: 'Here are the race times in seconds for 5 runners:\n11.12, 10.94, 11.05, 11.12, 10.91',
            promptText: '(a) Work out the median race time.\n(b) What is the modal race time?',
            unit: 's',
            expectedType: 'number',
            parts: [
              { id: 'a', label: 'Part (a) Median time', placeholder: 'e.g. 11.05', unit: 's' },
              { id: 'b', label: 'Part (b) Modal time', placeholder: 'e.g. 11.12', unit: 's' }
            ],
            modelSolution: '(a) Ascending order: 10.91, 10.94, 11.05, 11.12, 11.12 [M1]; Middle value = 11.05 seconds [A1]\n(b) 11.12 appears twice (most frequent) -> Mode = 11.12 seconds [B1]',
            finalBenchmark: '11.05 s / 11.12 s'
          },
          {
            num: 2,
            section: 'Section A: Non-Calculator',
            isCalcAllowed: false,
            marks: 3,
            markTags: '[M1, M1, A1]',
            scenarioTitle: 'Formula Evaluation with Roots and Powers',
            scenarioText: 'A formula to calculate vertical height is:\nh = √(a² − b²)\nwhere a = 10 and b = 8.',
            promptText: 'Work out the value of h without using a calculator.',
            unit: '',
            expectedType: 'number',
            parts: [
              { id: 'h', label: 'Value of h', placeholder: 'e.g. 6', unit: '' }
            ],
            modelSolution: 'a² = 10² = 100; b² = 8² = 64 [M1]; a² − b² = 100 − 64 = 36 [M1]; h = √36 = 6 [A1]',
            finalBenchmark: '6'
          },
          {
            num: 3,
            section: 'Section A: Non-Calculator',
            isCalcAllowed: false,
            marks: 4,
            markTags: '[M1, M1, M1, A1]',
            scenarioTitle: 'Hospital Patient Meal Fractions',
            scenarioText: 'There are 240 patients in a community hospital.\n• 1/3 of the patients choose pasta\n• 3/8 of the patients choose beef stew\n• The rest of the patients choose chicken.',
            promptText: 'How many patients choose chicken? You must show your working.',
            unit: 'patients',
            expectedType: 'number',
            parts: [
              { id: 'chicken', label: 'Number of patients choosing chicken', placeholder: 'e.g. 70', unit: 'patients' }
            ],
            modelSolution: 'Pasta = 240 ÷ 3 = 80 [M1]; Stew = (240 ÷ 8) × 3 = 30 × 3 = 90 [M1]; Combined = 80 + 90 = 170 [M1]; Chicken = 240 − 170 = 70 patients [A1]',
            finalBenchmark: '70 patients'
          },
          {
            num: 4,
            section: 'Section A: Non-Calculator',
            isCalcAllowed: false,
            marks: 6,
            markTags: '[M1, A1, M1, A1, C1, C1]',
            scenarioTitle: 'Paving Slabs & Garden Perimeter Budget',
            scenarioText: 'A landscaper lays square concrete paving slabs around a rectangular garden patio 6 m by 4 m. Each slab is 50 cm by 50 cm and costs £4.50. The client has a maximum budget of £250.',
            promptText: 'Determine if the total cost of paving slabs is within the client budget.',
            unit: '£',
            expectedType: 'decision',
            parts: [
              { id: 'slabs', label: 'Number of slabs needed', placeholder: 'e.g. 44', unit: '' },
              { id: 'cost', label: 'Total Cost', placeholder: 'e.g. 198.00', unit: '£' },
              { id: 'decision', label: 'Within budget?', placeholder: 'State Yes/No with difference from £250', unit: '' }
            ],
            modelSolution: 'Patio perimeter = 2 × (6 + 4) = 20 m; Border area / perimeter slabs calculation [M1, A1]; Slabs = 44 slabs at £4.50 = £198.00 [M1, A1]; £198.00 < £250.00 (under budget by £52). Yes, within budget [C1, C1]',
            finalBenchmark: 'Yes (Total £198.00 is £52 under budget)'
          }
        ]
      },
      {
        id: 'B',
        name: 'Section B: Calculator',
        code: 'PMAT2/C02',
        durationMinutes: 90,
        totalMarks: 48,
        isCalcAllowed: true,
        instructions: 'Calculators may be used. Check your working and your answers at each stage.',
        questions: [
          { num: 1, section: 'Dimension Constraints: Kitchen Fridges', isCalcAllowed: true, marks: 3, markTags: '[M1, M1, A1]', scenarioTitle: 'Kitchen Appliance Unit Fit', scenarioText: 'Maximum opening dimensions: Width 19 inches, Depth 22 inches, Height 36 inches (1 inch = 2.54 cm).\n• Fridge A: W 47.2 cm, D 44.6 cm, H 84.2 cm\n• Fridge B: W 49.4 cm, D 52.0 cm, H 85.0 cm\n• Fridge C: W 46.0 cm, D 54.0 cm, H 94.2 cm.', promptText: 'Which fridge will fit into the space? Show your working.', unit: '', expectedType: 'text', modelSolution: 'Opening: W = 19 × 2.54 = 48.26 cm; D = 22 × 2.54 = 55.88 cm; H = 36 × 2.54 = 91.44 cm [M1, M1]; Fridge B too wide (49.4 > 48.26); Fridge C too tall (94.2 > 91.44); Only Fridge A fits [A1]', finalBenchmark: 'Fridge A' },
          { num: 2, section: 'Coordinate Geometry: Parallelogram', isCalcAllowed: true, marks: 3, markTags: '[B1, B1, B1]', scenarioTitle: 'Plotting Parallelogram ABCD', scenarioText: 'A coordinate grid has points A(−2, 1), B(2, 4), and C(1, −1).\n(a) Write down coordinates of C.\n(b) Find coordinates of D to complete parallelogram ABCD.\n(c) State the sum of interior angles of ABCD.', promptText: 'State coordinates of C, D, and interior angle sum.', unit: '', expectedType: 'text', modelSolution: '(a) C(1, −1) [B1]; (b) Vector AB is (+4, +3); applying to C gives D(5, 2) [B1]; (c) Sum of angles in any quadrilateral = 360° [B1]', finalBenchmark: 'C(1, −1) / D(5, 2) / 360°' },
          { num: 3, section: 'Currency Exchange & Commission', isCalcAllowed: true, marks: 4, markTags: '[M1, M1, M1, A1]', scenarioTitle: 'Holiday Spending Money', scenarioText: 'Exchange rate: £1 = €1.16 with 2% commission fee. Calculate net euros received for £850.', promptText: 'Calculate euros received after 2% fee.', unit: '€', expectedType: 'number', modelSolution: 'Fee = £850 × 0.02 = £17; Exchanged = 850 − 17 = £833 [M1]; Euros = 833 × 1.16 = €966.28 [M1, A1]', finalBenchmark: '€966.28' },
          { num: 4, section: 'Cylindrical Storage Tank Volume', isCalcAllowed: true, marks: 4, markTags: '[M1, M1, M1, A1]', scenarioTitle: 'Oil Tank Capacity', scenarioText: 'Cylindrical fuel tank diameter 1.6 m, length 3.2 m. Volume = πr²h. 1 m³ = 1000 litres.', promptText: 'Calculate tank volume in litres.', unit: 'litres', expectedType: 'number', modelSolution: 'r = 0.8 m; V = π × 0.8² × 3.2 = 6.434 m³ [M1, M1]; 6.434 × 1000 = 6434 litres [M1, A1]', finalBenchmark: '6434 litres' },
          { num: 5, section: 'Salary Budget & Percentage Increases', isCalcAllowed: true, marks: 5, markTags: '[M1, M1, M1, M1, A1]', scenarioTitle: 'Staff Annual Pay Award', scenarioText: 'Department payroll has 8 staff earning £26,500 each and 2 managers earning £38,000 each. A 4.5% pay rise is awarded across all employees.', promptText: 'Calculate the total increase in annual payroll costs.', unit: '£', expectedType: 'number', modelSolution: 'Total salary = (8 × 26,500) + (2 × 38,000) = 212,000 + 76,000 = £288,000 [M1, M1]; Increase = 288,000 × 0.045 = £12,960 [M1, A1]', finalBenchmark: '£12,960' },
          { num: 6, section: 'Triangular Prism Cross Section', isCalcAllowed: true, marks: 4, markTags: '[M1, M1, M1, A1]', scenarioTitle: 'Cardboard Toblerone Packaging', scenarioText: 'A packaging carton is a right triangular prism with triangular face base 6 cm, height 5.2 cm, and prism length 28 cm.', promptText: 'Work out the total volume of the carton.', unit: 'cm³', expectedType: 'number', modelSolution: 'Triangle area = (6 × 5.2) ÷ 2 = 15.6 cm² [M1]; Volume = 15.6 × 28 = 436.8 cm³ [M1, A1]', finalBenchmark: '436.8 cm³' },
          { num: 7, section: 'Speed, Distance & Journey Timing', isCalcAllowed: true, marks: 4, markTags: '[M1, M1, M1, A1]', scenarioTitle: 'Delivery Route Timetable', scenarioText: 'A courier drives 135 miles at an average speed of 45 mph. They take a 35-minute break at the depot and depart at 08:45.', promptText: 'At what time does the courier arrive at the destination?', unit: '', expectedType: 'text', modelSolution: 'Driving time = 135 ÷ 45 = 3 hours [M1]; Total time = 3 hr + 35 min = 3 hr 35 min [M1]; Arrival = 08:45 + 3 hr 35 min = 12:20 [M1, A1]', finalBenchmark: '12:20' },
          { num: 8, section: 'Grouped Frequency & Mean Estimation', isCalcAllowed: true, marks: 6, markTags: '[M1, A1, M1, M1, A1, B1]', scenarioTitle: 'Customer Waiting Times', scenarioText: 'Waiting times (minutes): 0–10 (12 people), 10–20 (24 people), 20–30 (16 people), 30–40 (8 people).', promptText: 'Calculate an estimate of the mean waiting time.', unit: 'mins', expectedType: 'number', modelSolution: 'Midpoints: 5, 15, 25, 35 [M1]; fx = (5×12) + (15×24) + (25×16) + (35×8) = 60 + 360 + 400 + 280 = 1100 [M1, M1]; Total freq = 60 [M1]; Estimated mean = 1100 ÷ 60 = 18.33 minutes [A1, B1]', finalBenchmark: '18.3 minutes' },
          { num: 9, section: 'Compound Interest Over 3 Years', isCalcAllowed: true, marks: 4, markTags: '[M1, M1, M1, A1]', scenarioTitle: 'Business Investment Growth', scenarioText: 'An enterprise invests £15,000 at 3.2% compound interest per year for 3 years.', promptText: 'Calculate the total value of the investment at the end of 3 years.', unit: '£', expectedType: 'number', modelSolution: 'Multiplier = 1 + 0.032 = 1.032 [M1]; 15,000 × (1.032)³ = 15,000 × 1.0991 = £16,486.63 [M1, A1]', finalBenchmark: '£16,486.63' },
          { num: 10, section: 'Probability Tree Diagrams', isCalcAllowed: true, marks: 4, markTags: '[M1, M1, M1, A1]', scenarioTitle: 'Independent Diagnostic Testing', scenarioText: 'Probability Test 1 passes = 0.85; Probability Test 2 passes = 0.90.', promptText: 'Calculate the probability that both tests pass.', unit: '', expectedType: 'number', modelSolution: 'P(Both Pass) = 0.85 × 0.90 = 0.765 (or 76.5%) [M1, A1]', finalBenchmark: '0.765' },
          { num: 11, section: 'Floor Tiling with Wastage Allowance', isCalcAllowed: true, marks: 5, markTags: '[M1, M1, M1, M1, A1]', scenarioTitle: 'Office Floor Tiling', scenarioText: 'Floor area is 65 m². Tiles cost £24/m². The builder adds a 10% wastage allowance before ordering.', promptText: 'Calculate the total cost of tiles needed including 10% wastage.', unit: '£', expectedType: 'number', modelSolution: 'Wastage = 65 × 1.10 = 71.5 m² [M1, M1]; Total cost = 71.5 × £24 = £1,716.00 [M1, A1]', finalBenchmark: '£1,716.00' },
          { num: 12, section: 'Scatter Graph & Line of Best Fit', isCalcAllowed: true, marks: 6, markTags: '[M1, A1, B1, M1, A1, B1]', scenarioTitle: 'Energy Consumption Trend', scenarioText: 'Daily heating gas consumption plotted against outdoor temperature.', promptText: '(a) Describe the correlation. (b) Predict gas units at 4°C.', unit: '', expectedType: 'text', modelSolution: 'Negative correlation (as outdoor temp increases, gas use decreases) [B1]; Estimate from trendline gives approx 65–72 units [M1, A1]', finalBenchmark: 'Negative correlation; approx 68 units' }
        ]
      }
    ]
  },

  // 2. PEARSON EDEXCEL FUNCTIONAL SKILLS ENGLISH WRITING LEVEL 1 - PRACTICE 1,

  // =========================================================================
  // FUNCTIONAL SKILLS ENGLISH WRITING MOCKS
  // =========================================================================
  'edexcel-english-writing-l1-practice-1': {
  "title": "Edexcel Functional Skills English Writing Level 1 — Practice Paper 1",
  "board": "Pearson Edexcel",
  "subject": "writing",
  "level": "Level 1",
  "paperNumber": 1,
  "durationMinutes": 60,
  "pdfUrl": "https://passfunctionalskills.co.uk/wp-content/uploads/2021/09/Edexcel-FS-English-Writing-Level-1-Practice-Paper-1.pdf",
  "modelSolutionPdf": "assets/downloads/past-papers/edexcel/english-level-1/FS_English_Writing_Level_1_Practice_Paper_1_Model_Solution_MFS.pdf",
  "videoSolutionSlug": "",
  "questions": [
    {
      "num": 1,
      "section": "Task 1: Formal Workplace Communication",
      "isCalcAllowed": false,
      "marks": 21,
      "markTags": "[12 Composition, 9 SPaG]",
      "targetWords": "200 to 250 words",
      "scenarioTitle": "Charity Day Proposal to Colleague Sam",
      "scenarioText": "You receive an email from your workplace colleague Sam:\n\"Hi, We are organising our company Charity Day next month to raise money for local good causes. We need ideas for activities that everyone can join in with. Some people suggested a cake sale, washing cars, or wearing funny clothes to work. What do you think would work best, and how could you help out on the day?\nThanks, Sam\"",
      "promptText": "Write an email to Sam proposing ideas for Charity Day.\nIn your email, you must:\n• Give your opinion on the suggested activities (cake sale, car wash, funny clothes)\n• Suggest at least one new activity of your own with reasons why it would work well\n• Explain how you can personally help with the event\n• Use an appropriate subject line, greeting, paragraphs, and formal workplace sign-off.",
      "unit": "words",
      "checklist": [
        "Included appropriate email subject line",
        "Used professional salutation (e.g. Dear Sam)",
        "Evaluated cake sale, car wash, and funny clothes suggestions",
        "Proposed new inclusive activity (e.g. sponsored 5k walk / raffle)",
        "Explained personal contribution on the day",
        "Checked spelling, punctuation, and capital letters"
      ],
      "modelSolution": "Subject: Charity Day Fundraising Proposal & Activity Ideas\n\nDear Sam,\n\nI am writing in response to your email regarding our upcoming annual Charity Day. Organising this event is a fantastic opportunity to bring our colleagues together, improve team morale, and raise vital funds for worthwhile local charities in our community.\n\nI really like the idea of holding a homemade cake sale because freshly baked treats are always very popular during morning coffee breaks. However, washing cars might be impractical if the weather is rainy, and wearing silly clothes can sometimes make visiting clients feel uncomfortable. Instead, I suggest organising a sponsored five-kilometre walk in the nearby park. A community walk is inclusive because people of all fitness levels can participate together. In addition, charging a modest five-pound registration fee and asking local businesses for raffle prizes would boost our fundraising total significantly.\n\nTo help with the event, I would be pleased to bake some chocolate muffins and savoury pastries for the cake stall. In addition, I can design colourful posters to put up across our office, set up tables and chairs on the morning of the event, and stay late afterwards to help count donations and tidy up. Please let me know if you would like to discuss these ideas further during our team meeting tomorrow.\n\nBest regards,\nJordan Bennett",
      "finalBenchmark": "Benchmark: 228 words • Full criteria met"
    },
    {
      "num": 2,
      "section": "Task 2: Web Form / Public Contribution",
      "isCalcAllowed": false,
      "marks": 15,
      "markTags": "[9 Composition, 6 SPaG]",
      "targetWords": "150 to 200 words",
      "scenarioTitle": "Anti-Social Behaviour Formal Complaint",
      "scenarioText": "You are completing an official online complaint form on your local council website regarding persistent antisocial behaviour from neighbours who recently moved in next door at 18 Willow Lane.",
      "promptText": "Complete the complaint form.\nIn your form, you must:\n• State the address involved and how long the disturbance has lasted\n• Detail specific examples of the disturbance (e.g. noise levels, rubbish)\n• Explain how this is negatively affecting you and your family\n• State the urgent action you expect the council to take.",
      "unit": "words",
      "checklist": [
        "Stated property address and timeframe clearly",
        "Provided specific examples of anti-social disturbances",
        "Described the emotional/physical impact on family life",
        "Made clear, reasonable request for council intervention",
        "Maintained formal, assertive, and respectful tone throughout"
      ],
      "modelSolution": "I am submitting this formal complaint regarding the tenants who recently moved into the property next door at 18 Willow Lane. Over the past three weeks, their persistent antisocial behaviour has caused severe distress and disruption to our quiet residential neighbourhood.\n\nFirstly, they play loud music late into the night and host noisy garden parties on weekday evenings. Secondly, they leave black bin bags of rotting rubbish piled outside their front door. The bags have split open, attracting foxes and creating an awful smell. When I attempted to speak with them politely last weekend, they were extremely aggressive, shouted at me, and slammed the door.\n\nThis constant disturbance is severely affecting my family. We are unable to sleep properly, and my young children are frequently woken up crying. I feel exhausted and stressed at work every day. I urge the council to investigate this matter urgently and take firm enforcement action.\n\nYours sincerely,\nJordan Bennett",
      "finalBenchmark": "Benchmark: 172 words • Full criteria met"
    }
  ]
},

  'edexcel-english-writing-l1-practice-2': {
  "title": "Edexcel Functional Skills English Writing Level 1 — Practice Paper 2",
  "board": "Pearson Edexcel",
  "subject": "writing",
  "level": "Level 1",
  "paperNumber": 2,
  "durationMinutes": 60,
  "pdfUrl": "https://passfunctionalskills.co.uk/wp-content/uploads/2021/09/Edexcel-FS-English-Writing-Level-1-Practice-Paper-2.pdf",
  "modelSolutionPdf": "assets/downloads/past-papers/edexcel/english-level-1/FS_English_Writing_Level_1_Practice_Paper_2_Model_Solution_MFS.pdf",
  "videoSolutionSlug": "",
  "questions": [
    {
      "num": 1,
      "section": "Task 1: Formal Workplace Communication",
      "isCalcAllowed": false,
      "marks": 21,
      "markTags": "[12 Composition, 9 SPaG]",
      "targetWords": "200 to 250 words",
      "scenarioTitle": "Healthy Eating Workplace Campaign Article",
      "scenarioText": "Your company is running a Healthy Eating and Wellbeing Campaign next month. The HR manager, Morgan, has asked staff to contribute articles to the company intranet giving practical advice on eating well during busy working days.",
      "promptText": "Write an article for the staff intranet on healthy eating at work.\nIn your article, you must:\n• Explain why healthy eating is important for workplace energy and wellbeing\n• Give practical suggestions for quick, healthy lunches and snacks\n• Suggest improvements to the staff canteen or kitchen facilities\n• Include an engaging title, clear subheadings, and an encouraging conclusion.",
      "unit": "words",
      "checklist": [
        "Included engaging article title and subheadings",
        "Explained physical and mental benefits of nutritious eating",
        "Gave practical lunchtime and snacking ideas",
        "Suggested realistic canteen/kitchen improvements",
        "Maintained encouraging and informative tone"
      ],
      "modelSolution": "Eat Well, Feel Great: Boosting Energy and Wellbeing at Work\n\nBy Alex Taylor\n\nWhy Nutrition Matters on Busy Days\nMaintaining a balanced diet during demanding workweeks is essential for our physical health and mental focus. Choosing nutritious foods prevents energy slumps in the afternoon, reduces stress levels, and keeps our immune systems strong throughout the winter months.\n\nSimple and Nutritious Lunchtime Ideas\nPreparing healthy lunches does not need to be complicated or expensive. Swapping processed fast foods for grain salads, wholemeal wraps filled with lean chicken or hummus, and hearty vegetable soups provides sustained energy throughout the day. For mid-morning snacks, keep almonds, fresh fruit, and Greek yogurt at your desk rather than relying on vending machine crisps and sugary chocolate bars.\n\nImproving Our Kitchen and Canteen Facilities\nTo support staff in making healthier choices, our company could make a few simple improvements. Adding a second microwave in the break room would make it easier for colleagues to heat homemade meals quickly. In addition, providing a water dispenser with chilled lemon slices and stocking the fruit bowl every Monday would encourage everyone to stay hydrated and refreshed. Let's make small, positive changes together this month!\n\nConclusion\nEating well is an investment in our daily energy and happiness. Try prepping one healthy lunch this week, and share your favourite recipes on our team message board!",
      "finalBenchmark": "Benchmark: 236 words • Full criteria met"
    },
    {
      "num": 2,
      "section": "Task 2: Web Form / Public Contribution",
      "isCalcAllowed": false,
      "marks": 15,
      "markTags": "[9 Composition, 6 SPaG]",
      "targetWords": "150 to 200 words",
      "scenarioTitle": "Community Sports Centre Customer Feedback Form",
      "scenarioText": "You recently visited the newly refurbished Oakwood Community Sports Centre. You are filling out an online customer feedback form regarding your experience with the gym equipment, cleanliness, and staff assistance.",
      "promptText": "Complete the customer feedback form.\nIn your form, you must:\n• State the date of your visit and the facilities you used\n• Describe what went well during your visit\n• Explain any issues you experienced (e.g. equipment maintenance or cleanliness)\n• Suggest specific improvements the management should make.",
      "unit": "words",
      "checklist": [
        "Specified visit date and facilities used",
        "Highlighted positive aspects of the visit",
        "Constructively described areas of concern",
        "Offered actionable recommendations for centre management",
        "Maintained polite and constructive tone"
      ],
      "modelSolution": "I visited Oakwood Community Sports Centre on Wednesday 14th October at 18:00 to use the fitness gym and swimming pool facilities.\n\nOverall, I was very impressed by the friendly welcome from the reception team and the variety of new cardiovascular machines. The swimming pool was well-supervised by attentive lifeguards, and the temperature of the water was ideal.\n\nHowever, I noticed a couple of issues that require attention. In the gym, two running treadmills were out of order with handwritten signs, which caused long queues during peak evening hours. Furthermore, several lockers in the men's changing area were broken, and the floor around the showers needed mopping.\n\nTo improve the customer experience, I recommend repairing the out-of-order machines promptly and introducing a maintenance schedule during busy periods. Having a dedicated staff member check the changing rooms every hour would also make a huge difference to cleanliness.\n\nThank you for reviewing my feedback.\n\nYours sincerely,\nAlex Taylor",
      "finalBenchmark": "Benchmark: 165 words • Full criteria met"
    }
  ]
},

  'edexcel-english-writing-l1-practice-3': {
  "title": "Edexcel Functional Skills English Writing Level 1 — Practice Paper 3",
  "board": "Pearson Edexcel",
  "subject": "writing",
  "level": "Level 1",
  "paperNumber": 3,
  "durationMinutes": 60,
  "pdfUrl": "https://passfunctionalskills.co.uk/wp-content/uploads/2021/09/Edexcel-FS-English-Writing-Level-1-Practice-Paper-3.pdf",
  "modelSolutionPdf": "assets/downloads/past-papers/edexcel/english-level-1/FS_English_Writing_Level_1_Practice_Paper_3_Model_Solution_MFS.pdf",
  "videoSolutionSlug": "",
  "questions": [
    {
      "num": 1,
      "section": "Task 1: Formal Workplace Communication",
      "isCalcAllowed": false,
      "marks": 21,
      "markTags": "[12 Composition, 9 SPaG]",
      "targetWords": "200 to 250 words",
      "scenarioTitle": "Apprenticeship Experience Email to College Tutor",
      "scenarioText": "You have just completed the first month of your vocational apprenticeship placement. Your college tutor, Mrs Davies, has emailed you asking for an update on how your placement is progressing, what skills you are learning, and what advice you have for new apprentices.",
      "promptText": "Write an email to Mrs Davies updating her on your apprenticeship.\nIn your email, you must:\n• Describe your main duties and the workplace environment\n• Explain the new practical and communication skills you have gained\n• Mention any initial difficulties you encountered and how you overcame them\n• Give two pieces of advice for students preparing to start their placements.",
      "unit": "words",
      "checklist": [
        "Included appropriate subject line and formal salutation",
        "Described daily responsibilities and team dynamic",
        "Explained specific technical and interpersonal skills learned",
        "Reflected honestly on challenges and solutions",
        "Provided two constructive tips for future candidates"
      ],
      "modelSolution": "Subject: Monthly Apprenticeship Placement Progress Update\n\nDear Mrs Davies,\n\nI am writing to update you on my progress following the completion of my first month as an apprentice administrator at Apex Healthcare Diagnostics. Overall, the experience has been thoroughly rewarding and has taught me a great deal about working in a busy professional setting.\n\nDuring my daily routine, I handle patient appointment bookings, manage incoming email enquiries, and update client records on the electronic database. My colleagues have been extremely welcoming, and my line manager has provided dedicated mentoring every morning. Through this hands-on work, I have significantly improved my computer spreadsheet skills, learned how to write formal business letters, and gained confidence when communicating with patients on the telephone.\n\nAt first, I found prioritising tasks quite difficult when multiple urgent requests arrived at once. However, I resolved this by keeping a daily planner notepad and asking my supervisor to clarify urgent deadlines at the start of each shift. For future students preparing to begin their apprenticeships, I advise them to always carry a notebook to write down instructions and never hesitate to ask questions when unsure.\n\nThank you for your ongoing support.\n\nYours sincerely,\nCharlie Green",
      "finalBenchmark": "Benchmark: 218 words • Full criteria met"
    },
    {
      "num": 2,
      "section": "Task 2: Web Form / Public Contribution",
      "isCalcAllowed": false,
      "marks": 15,
      "markTags": "[9 Composition, 6 SPaG]",
      "targetWords": "150 to 200 words",
      "scenarioTitle": "Public Library Service Review and Improvement Suggestions",
      "scenarioText": "Your local council library is reviewing its community services and has invited residents to complete a public feedback form suggesting ways to improve visitor facilities, book selections, and study spaces.",
      "promptText": "Complete the library review form.\nIn your form, you must:\n• State how frequently you visit the library and what services you use\n• Explain what you appreciate about the current library facilities\n• Describe any limitations (e.g. computer booking limits, weekend opening hours)\n• Propose practical suggestions to attract more young people and families.",
      "unit": "words",
      "checklist": [
        "Stated frequency of visits and services utilized",
        "Identified strengths of existing library provision",
        "Constructively highlighted current service limitations",
        "Proposed engaging ideas for younger patrons and families",
        "Ensured clear paragraphs and accurate spelling"
      ],
      "modelSolution": "I visit Stretford Public Library twice a week to borrow books and use the quiet study desks on the first floor.\n\nI really value the welcoming atmosphere, the helpfulness of the librarians, and the fast wireless internet connection. Having access to quiet desks has been invaluable for completing my coursework.\n\nHowever, there are a few limitations that could be improved. The computer terminals are currently restricted to thirty-minute sessions, which is not long enough to submit online job applications. Additionally, closing at 13:00 on Saturdays makes it hard for working parents to visit with their children.\n\nTo attract more families and younger readers, I suggest introducing weekend storytelling sessions, offering digital gaming and coding workshops, and creating a modern teenage reading corner with beanbags. Providing hot drinks from a self-service machine would also make the library feel more vibrant and welcoming.\n\nYours faithfully,\nCharlie Green",
      "finalBenchmark": "Benchmark: 168 words • Full criteria met"
    }
  ]
},

  'edexcel-english-writing-l1-paper-4': {
  "title": "Edexcel Functional Skills English Writing Level 1 — Past Paper 4",
  "board": "Pearson Edexcel",
  "subject": "writing",
  "level": "Level 1",
  "paperNumber": 4,
  "durationMinutes": 60,
  "pdfUrl": "https://passfunctionalskills.co.uk/app/uploads/2024/06/FS_English_Writing_Level_1_Past_Paper_4_QP.pdf",
  "modelSolutionPdf": "assets/downloads/past-papers/edexcel/english-level-1/FS_English_Writing_Level_1_Past_Paper_4_Model_Solution_MFS.pdf",
  "videoSolutionSlug": "",
  "questions": [
    {
      "num": 1,
      "section": "Task 1: Formal Workplace Communication",
      "isCalcAllowed": false,
      "marks": 21,
      "markTags": "[12 Composition, 9 SPaG]",
      "targetWords": "200 to 250 words",
      "scenarioTitle": "Green Travel Week Proposal to Facilities Manager",
      "scenarioText": "Your employer wants to reduce staff carbon emissions and encourage greener commuting. The facilities manager, Alex, has invited all employees to email proposals for 'Green Travel Week'.",
      "promptText": "Write an email to Alex proposing ideas for Green Travel Week.\nIn your email, you must:\n• Explain the benefits of promoting green travel for staff health and the environment\n• Propose at least two specific initiatives (e.g. cycle to work schemes, car-sharing rotas, public transit discounts)\n• Suggest fun incentives or prizes to encourage maximum participation\n• Offer to assist with the coordination of the week.",
      "unit": "words",
      "checklist": [
        "Included professional subject line and formal opening",
        "Explained environmental and health advantages",
        "Proposed two feasible green commuting schemes",
        "Suggested motivating rewards or competition ideas",
        "Expressed willingness to help organise the campaign"
      ],
      "modelSolution": "Subject: Green Travel Week Initiatives & Implementation Proposal\n\nDear Alex,\n\nI am writing to propose several practical initiatives for our upcoming Green Travel Week. Encouraging sustainable transport is a wonderful way to reduce our company carbon footprint, improve air quality in our town, and help employees save money on fuel while boosting their daily cardiovascular fitness.\n\nFirstly, I recommend setting up an internal car-sharing register on our staff intranet. Colleagues who live in similar neighbourhoods could share rides, which would immediately cut congestion and relieve pressure on our crowded staff car park. Secondly, we could introduce a 'Bike to Work Breakfast' where staff who cycle or walk to the office are rewarded with free healthy breakfast muffins and fruit juice in the canteen. In addition, partnering with local bus companies to offer discounted weekly travel passes would encourage public transit use.\n\nTo make the week engaging, we could run a department travel challenge where the team with the highest percentage of green journeys wins an extra hour of lunch on Friday or a voucher for a local eco-store. I would be delighted to help design promotional posters, set up the bike parking area, and track journey logs during the week. Please let me know when you would like to discuss this.\n\nBest regards,\nSamir Patel",
      "finalBenchmark": "Benchmark: 226 words • Full criteria met"
    },
    {
      "num": 2,
      "section": "Task 2: Web Form / Public Contribution",
      "isCalcAllowed": false,
      "marks": 15,
      "markTags": "[9 Composition, 6 SPaG]",
      "targetWords": "150 to 200 words",
      "scenarioTitle": "Local Public Transport Formal Review Form",
      "scenarioText": "You commute to work daily using the local municipal bus service (Route 42). You are completing a passenger consultation form about service frequency, reliability, and ticketing costs.",
      "promptText": "Complete the transport consultation form.\nIn your form, you must:\n• Identify the bus route you use and your typical travel times\n• Describe the main problems you experience with the service\n• Explain how these delays or disruptions impact your working day\n• Recommend two realistic improvements the bus company should implement.",
      "unit": "words",
      "checklist": [
        "Identified route number and commute times accurately",
        "Provided specific examples of service failure or overcrowding",
        "Described real-life consequences on work punctuality",
        "Recommended two practical, constructive solutions",
        "Checked grammar, spelling, and sentence punctuation"
      ],
      "modelSolution": "I travel on the Route 42 bus service twice every weekday between Greenfield Station and the town centre commercial district, typically catching the 07:45 morning bus.\n\nUnfortunately, the service has become increasingly unreliable over the past two months. The 07:45 bus is frequently delayed by up to twenty-five minutes, and on three occasions this month, it failed to arrive altogether with no update on the digital display board. When the bus does finally arrive, it is dangerously overcrowded, forcing passengers to stand in cramped aisles.\n\nThese persistent cancellations have caused me to arrive late for critical morning team meetings, which causes considerable stress and reflects poorly on my professional reputation.\n\nTo resolve these problems, I strongly recommend adding an extra bus service between 07:30 and 08:30 to cope with morning rush hour demand. Additionally, ensuring live GPS arrival updates are displayed accurately on the mobile app would help commuters plan alternative routes effectively.\n\nYours sincerely,\nSamir Patel",
      "finalBenchmark": "Benchmark: 171 words • Full criteria met"
    }
  ]
},

  'edexcel-english-writing-l1-paper-6': {
  "title": "Edexcel Functional Skills English Writing Level 1 — Past Paper 6",
  "board": "Pearson Edexcel",
  "subject": "writing",
  "level": "Level 1",
  "paperNumber": 6,
  "durationMinutes": 60,
  "pdfUrl": "https://passfunctionalskills.co.uk/app/uploads/2024/06/FS_English_Writing_Level_1_Past_Paper_6_QP.pdf",
  "modelSolutionPdf": "assets/downloads/past-papers/edexcel/english-level-1/FS_English_Writing_Level_1_Past_Paper_6_Model_Solution_MFS.pdf",
  "videoSolutionSlug": "",
  "questions": [
    {
      "num": 1,
      "section": "Task 1: Formal Workplace Communication",
      "isCalcAllowed": false,
      "marks": 21,
      "markTags": "[12 Composition, 9 SPaG]",
      "targetWords": "200 to 250 words",
      "scenarioTitle": "Team Volunteering Day Proposal to General Manager",
      "scenarioText": "Your company allows departments to take part in an annual paid Community Volunteering Day. Your department manager, Karen, has asked the team to suggest ideas for local community projects to support.",
      "promptText": "Write an email to Karen proposing a Community Volunteering Day project.\nIn your email, you must:\n• Propose a specific local volunteering project (e.g. canal towpath clean-up or care home garden makeover)\n• Explain why this project is worthwhile and how it benefits the local community\n• Detail the practical tasks your team would carry out on the day\n• Outline safety measures and equipment needed for the team.",
      "unit": "words",
      "checklist": [
        "Included concise subject line and polite greeting",
        "Selected specific community initiative with clear rationale",
        "Outlined distinct practical team tasks",
        "Addressed health and safety equipment considerations",
        "Maintained persuasive and organized workplace style"
      ],
      "modelSolution": "Subject: Community Volunteering Day Proposal: Canal Towpath Clean-up\n\nDear Karen,\n\nI am writing to propose an exciting and rewarding project for our department's upcoming Community Volunteering Day. I suggest partnering with the local Canal & River Trust to complete a thorough clean-up and restoration of the historic canal towpath near our business park.\n\nThis project is extremely worthwhile because the towpath is used daily by hundreds of local residents, cyclists, and families. Over recent months, litter, overgrown brambles, and broken branches have made sections of the path unsightly and unsafe. By restoring this green space, our team will enhance the local natural habitat, prevent plastic waste entering the waterways, and create a welcoming environment for the whole community.\n\nOn the day, our team could divide into three small groups: one group to clear litter and plastic debris, a second group to trim back overgrown hedges using hand pruners, and a third group to sand down and repaint the weathered wooden benches along the route. For safety, all volunteers will require heavy-duty work gloves, high-visibility tabards, sturdy footwear, and eye protection. The Trust has confirmed they can provide litter grabbers and waste sacks.\n\nI would be delighted to liaise with the Trust coordinator to confirm dates and arrange a site visit.\n\nBest regards,\nRobin Sinclair",
      "finalBenchmark": "Benchmark: 224 words • Full criteria met"
    },
    {
      "num": 2,
      "section": "Task 2: Web Form / Public Contribution",
      "isCalcAllowed": false,
      "marks": 15,
      "markTags": "[9 Composition, 6 SPaG]",
      "targetWords": "150 to 200 words",
      "scenarioTitle": "College Open Day Visitor Feedback Form",
      "scenarioText": "You recently attended an Open Evening at Riverside College to explore professional adult education courses. You are completing an online visitor feedback form regarding campus facilities, course talks, and tutor advice.",
      "promptText": "Complete the college visitor feedback form.\nIn your form, you must:\n• State the courses or subject areas you inquired about\n• Describe what aspects of the open evening were most helpful\n• Identify any information or facilities that were missing or unclear\n• Suggest how future open evenings could be improved for prospective learners.",
      "unit": "words",
      "checklist": [
        "Identified specific course inquiries clearly",
        "Highlighted helpful elements of the event",
        "Pointed out areas requiring better signage or information",
        "Gave constructive suggestions for future open events",
        "Maintained polite, professional register"
      ],
      "modelSolution": "I attended the Riverside College Adult Education Open Evening on Tuesday 8th November to learn more about the Level 2 Business Administration and Functional Skills courses.\n\nI found the introductory presentation by the department heads exceptionally informative, and the course tutors were patient and answered all my questions regarding assessment criteria and class timetables. The campus library and IT suites also appeared modern and well-equipped.\n\nHowever, finding the specific seminar rooms was quite confusing due to a lack of directional signage in the main concourse. In addition, there was very little information available regarding parking validation and student funding options for evening learners.\n\nTo improve future open evenings, I recommend stationing student ambassadors at the main entrance to guide visitors directly to subject classrooms. Providing a dedicated information desk for financial support and childcare bursaries would also be extremely helpful for adult applicants.\n\nThank you for considering my suggestions.\n\nYours sincerely,\nRobin Sinclair",
      "finalBenchmark": "Benchmark: 169 words • Full criteria met"
    }
  ]
},

  'edexcel-english-writing-l1-paper-7': {
  "title": "Edexcel Functional Skills English Writing Level 1 — Past Paper 7",
  "board": "Pearson Edexcel",
  "subject": "writing",
  "level": "Level 1",
  "paperNumber": 7,
  "durationMinutes": 60,
  "pdfUrl": "https://passfunctionalskills.co.uk/app/uploads/2024/06/FS_English_Writing_Level_1_Past_Paper_7_QP.pdf",
  "modelSolutionPdf": "assets/downloads/past-papers/edexcel/english-level-1/FS_English_Writing_Level_1_Past_Paper_7_Model_Solution_MFS.pdf",
  "videoSolutionSlug": "",
  "questions": [
    {
      "num": 1,
      "section": "Task 1: Formal Workplace Communication",
      "isCalcAllowed": false,
      "marks": 21,
      "markTags": "[12 Composition, 9 SPaG]",
      "targetWords": "200 to 250 words",
      "scenarioTitle": "Staff Break Room & Wellbeing Upgrade Proposal",
      "scenarioText": "Your office break room is outdated and uncomfortable. The office manager, Kelly, has asked staff for suggestions on how to refurbish the space within a modest budget.",
      "promptText": "Write an email to Kelly proposing break room improvements.\nIn your email, you must:\n• Explain why an improved break room is important for staff morale and rest\n• Suggest specific equipment or furniture additions (e.g. comfortable seating, microwave, water filter)\n• Propose ideas for a quiet relaxation corner or reading area\n• Suggest low-cost ways to decorate and maintain the room.",
      "unit": "words",
      "checklist": [
        "Used formal workplace email format and clear subject",
        "Explained benefits of restorative break times",
        "Suggested practical, budget-conscious furniture and appliances",
        "Proposed quiet corner concept",
        "Included low-cost decoration and upkeep ideas"
      ],
      "modelSolution": "Subject: Staff Break Room Refurbishment & Wellbeing Proposal\n\nDear Kelly,\n\nI am writing in response to your invitation for suggestions regarding the refurbishment of our staff break room. Having a comfortable and relaxing environment to take scheduled rest breaks is vital for employee wellbeing, helps reduce workplace fatigue, and fosters positive collaboration between different departments.\n\nCurrently, the plastic chairs and damaged tables make the space feel unwelcoming. I recommend investing in durable padded armchairs and a communal dining table where colleagues can eat together comfortably. In terms of kitchen equipment, adding a second modern microwave, an energy-efficient toaster, and a chilled water filtration tap would significantly reduce queues during the busy midday rush.\n\nFurthermore, partitioning off a small section of the room with freestanding bookcases would create a peaceful quiet zone. Staff who need a moment away from computer screens could read or practice quiet mindfulness without being disturbed by kitchen chatter. To keep costs low, we could invite employees to bring in cuttings of indoor plants, display framed prints of team achievements, and organise a weekly cleaning rota so everyone shares responsibility for keeping the space pristine.\n\nThank you for taking staff feedback into account.\n\nBest regards,\nDana Vance",
      "finalBenchmark": "Benchmark: 221 words • Full criteria met"
    },
    {
      "num": 2,
      "section": "Task 2: Web Form / Public Contribution",
      "isCalcAllowed": false,
      "marks": 15,
      "markTags": "[9 Composition, 6 SPaG]",
      "targetWords": "150 to 200 words",
      "scenarioTitle": "Parcel Delivery Service Formal Complaint",
      "scenarioText": "You ordered urgent office equipment online with guaranteed next-day delivery. The parcel arrived four days late, the packaging was badly damaged, and the delivery driver was rude.",
      "promptText": "Complete the courier customer complaint form.\nIn your form, you must:\n• Provide your tracking number and order details\n• Explain the sequence of delivery failures and damages\n• Describe the unacceptable conduct of the driver\n• State the financial redress or compensation you expect.",
      "unit": "words",
      "checklist": [
        "Provided reference and tracking details",
        "Detailing delivery timeline and package damage",
        "Described driver conduct factually and assertively",
        "Requested appropriate refund and compensation",
        "Checked punctuation and spelling"
      ],
      "modelSolution": "I am writing to log a formal complaint regarding delivery tracking reference #FX-90821-GB, ordered on 3rd November with guaranteed premium next-day delivery.\n\nThe parcel did not arrive on 4th November as promised and was delayed until 8th November with no tracking notifications. When the delivery driver finally arrived, the cardboard box was crushed, torn open, and soaked with water. Internal electronic items were exposed and scratched.\n\nWhen I politely asked the driver why the box was damaged, he was dismissive, refused to note the damage on his handheld terminal, and walked away swearing. This unprofessional attitude is completely unacceptable.\n\nAs a result of this four-day delay, our company missed an important client presentation deadline. I require a full refund of the £18.50 premium delivery fee, reimbursement for the damaged equipment valued at £145.00, and a written apology regarding the driver's behaviour.\n\nYours faithfully,\nDana Vance",
      "finalBenchmark": "Benchmark: 161 words • Full criteria met"
    }
  ]
},

  'edexcel-english-writing-l1-paper-8': {
  "title": "Edexcel Functional Skills English Writing Level 1 — Past Paper 8",
  "board": "Pearson Edexcel",
  "subject": "writing",
  "level": "Level 1",
  "paperNumber": 8,
  "durationMinutes": 60,
  "pdfUrl": "https://passfunctionalskills.co.uk/app/uploads/2024/06/FS_English_Writing_Level_1_Past_Paper_8_QP.pdf",
  "modelSolutionPdf": "assets/downloads/past-papers/edexcel/english-level-1/FS_English_Writing_Level_1_Past_Paper_8_Model_Solution_MFS.pdf",
  "videoSolutionSlug": "",
  "questions": [
    {
      "num": 1,
      "section": "Task 1: Formal Workplace Communication",
      "isCalcAllowed": false,
      "marks": 21,
      "markTags": "[12 Composition, 9 SPaG]",
      "targetWords": "200 to 250 words",
      "scenarioTitle": "Workplace Waste Reduction & Recycling Campaign",
      "scenarioText": "Your company environmental committee is launching a campaign to reduce single-use plastics and paper waste across all regional branch offices.",
      "promptText": "Write an article for the company newsletter on cutting workplace waste.\nIn your article, you must:\n• Explain the environmental consequences of excessive office waste\n• Outline practical steps staff can take to save paper and eliminate disposable plastics\n• Propose changes to office supplies and printing policies\n• Conclude with an inspiring call to action for all colleagues.",
      "unit": "words",
      "checklist": [
        "Engaging title and professional article structure",
        "Addressed environmental impact clearly",
        "Gave actionable paper-saving and plastic reduction habits",
        "Recommended policy improvements",
        "Inspiring conclusion and call to action"
      ],
      "modelSolution": "Rethink, Reduce, Recycle: Transforming Our Workplace Footprint\n\nBy Jamie Lin\n\nThe Hidden Cost of Office Waste\nEvery working day, British offices discard millions of single-use coffee cups, plastic water bottles, and reams of unnecessary paperwork. Disposing of these items generates substantial landfill pollution and wastes valuable natural resources. As a responsible modern business, our organisation has a duty to lead by example and adopt sustainable working practices.\n\nPractical Everyday Changes for Every Desk\nReducing our daily environmental impact begins with simple personal habits. Replacing single-use plastic cups with reusable insulated mugs and metal water bottles will instantly divert hundreds of cups from waste bins each week. When planning meetings, embrace paperless digital agendas on laptops or tablets instead of printing multi-page handouts. For essential printing, always select double-sided black-and-white printing.\n\nUpdating Company Procurement Policies\nIn addition to individual efforts, our company should update purchasing guidelines. The management team should replace individual desk bins with centralised recycling stations for food compost, paper, and plastics. Furthermore, switching to 100% recycled copy paper and stocking refillable whiteboard pens will deliver both financial savings and environmental benefits.\n\nJoin the Challenge Today!\nProtecting the environment is a team effort. Sign the green pledge on our intranet this week, and let's make our workplace one of the cleanest and greenest in the region!",
      "finalBenchmark": "Benchmark: 231 words • Full criteria met"
    },
    {
      "num": 2,
      "section": "Task 2: Web Form / Public Contribution",
      "isCalcAllowed": false,
      "marks": 15,
      "markTags": "[9 Composition, 6 SPaG]",
      "targetWords": "150 to 200 words",
      "scenarioTitle": "Gym Membership Cancellation & Refund Request",
      "scenarioText": "You signed up for an annual gym membership at Velocity Fitness, but have suffered a severe knee injury requiring medical surgery. You are submitting an official cancellation request.",
      "promptText": "Complete the membership cancellation and refund form.\nIn your form, you must:\n• State your membership number and the date you joined\n• Explain the medical circumstances preventing you from using facilities\n• Reference medical documentation provided from your doctor\n• Request the immediate cancellation of your direct debit and a refund of unused fees.",
      "unit": "words",
      "checklist": [
        "Stated membership ID and registration date",
        "Detailed medical condition accurately",
        "Referenced supporting physician evidence",
        "Requested direct debit cancellation and fee refund",
        "Maintained formal, respectful tone"
      ],
      "modelSolution": "I am writing to formally request the immediate cancellation of my Velocity Fitness membership (Account ID #VF-77120), which commenced on 1st September.\n\nUnfortunately, following a severe sports injury last week, I have been diagnosed with a torn knee ligament and have been booked for orthopaedic surgery next month. My consultant physician has advised that I must not participate in any cardiovascular or weight-bearing exercise for at least nine months.\n\nI have attached an official medical certificate from Highfield Community Healthcare Clinic confirming my diagnosis and ongoing treatment plan. Under clause 8.2 of your membership terms, medical incapacity permits early contract termination without penalty.\n\nI therefore request that you cancel my monthly direct debit mandate immediately and process a pro-rata refund for the remaining unused portion of my November subscription fees. Please confirm this cancellation in writing within seven working days.\n\nYours faithfully,\nJamie Lin",
      "finalBenchmark": "Benchmark: 158 words • Full criteria met"
    }
  ]
},

  'edexcel-english-writing-l1-paper-9': {
  "title": "Edexcel Functional Skills English Writing Level 1 — Past Paper 9",
  "board": "Pearson Edexcel",
  "subject": "writing",
  "level": "Level 1",
  "paperNumber": 9,
  "durationMinutes": 60,
  "pdfUrl": "https://passfunctionalskills.co.uk/app/uploads/2024/06/FS_English_Writing_Level_1_Past_Paper_9_QP.pdf",
  "modelSolutionPdf": "assets/downloads/past-papers/edexcel/english-level-1/FS_English_Writing_Level_1_Past_Paper_9_Model_Solution_MFS.pdf",
  "videoSolutionSlug": "",
  "questions": [
    {
      "num": 1,
      "section": "Task 1: Formal Workplace Communication",
      "isCalcAllowed": false,
      "marks": 21,
      "markTags": "[12 Composition, 9 SPaG]",
      "targetWords": "200 to 250 words",
      "scenarioTitle": "Community Allotment Project Proposal to Councillor",
      "scenarioText": "A disused plot of overgrown council land behind Elmfield High Street is attracting fly-tipping. You are writing to local councillor Janet Morris proposing turning it into a Community Allotment.",
      "promptText": "Write an email to Councillor Janet Morris proposing a community garden.\nIn your email, you must:\n• Describe the current derelict state of the site and the fly-tipping problem\n• Propose turning the land into community allotments and wildlife gardens\n• Explain the benefits for local residents (mental health, fresh produce, community cohesion)\n• Outline how volunteers from the neighbourhood will clear and manage the site.",
      "unit": "words",
      "checklist": [
        "Formal salutation to councillor and clear subject line",
        "Described current problems at the derelict location",
        "Articulated vision for allotments and green space",
        "Highlighted mental, social, and nutritional benefits",
        "Detailed community volunteer maintenance plan"
      ],
      "modelSolution": "Subject: Community Allotment and Green Space Proposal: Elmfield Land\n\nDear Councillor Morris,\n\nI am writing on behalf of the Elmfield Residents Association to submit a proposal regarding the derelict parcel of council-owned land situated behind the High Street commercial shops. At present, this overgrown plot has become a magnet for illegal fly-tipping, broken glass, and antisocial behaviour, which creates an eyesore and poses safety hazards for neighbourhood children.\n\nWe propose transforming this neglected space into a vibrant Community Allotment and Wildlife Garden. Converting the ground into twenty productive vegetable plots, a sensory herb garden, and a small community orchard would provide enormous benefits for our area. Gardening outdoors significantly reduces anxiety, improves mental wellbeing, and offers retired residents and young families the chance to grow fresh, nutritious produce affordably. In addition, it would foster a strong community spirit by bringing together diverse generations.\n\nOver thirty local residents have already volunteered to assist with clearing weeds, removing rubbish, and installing raised wooden planting beds. We have also secured promises of free timber and compost from local garden centres. We would be immensely grateful if the council would grant our association a five-year community lease for the site.\n\nI look forward to discussing this project with you.\n\nYours sincerely,\nMarcus Reed",
      "finalBenchmark": "Benchmark: 227 words • Full criteria met"
    },
    {
      "num": 2,
      "section": "Task 2: Web Form / Public Contribution",
      "isCalcAllowed": false,
      "marks": 15,
      "markTags": "[9 Composition, 6 SPaG]",
      "targetWords": "150 to 200 words",
      "scenarioTitle": "Public Park Facilities Incident Report Form",
      "scenarioText": "While visiting Victoria Recreation Park with your younger siblings, you discovered broken play equipment and vandalised safety fencing. You are submitting an official incident report to the parks department.",
      "promptText": "Complete the parks maintenance and safety report.\nIn your form, you must:\n• Identify the specific park and playground location involved\n• Detail the exact damage and hazardous conditions observed\n• Explain the potential dangers to young children and park visitors\n• Urge specific emergency repair and security measures.",
      "unit": "words",
      "checklist": [
        "Identified precise location and inspection date",
        "Accurately described broken equipment and hazards",
        "Highlighted urgent safety risks to children",
        "Requested immediate repair and preventative security",
        "Checked grammar and punctuation"
      ],
      "modelSolution": "I am submitting this urgent incident report regarding hazardous conditions in the toddler playground area at Victoria Recreation Park, inspected on Sunday 18th October at 15:30.\n\nThe main junior climbing frame has a missing wooden step on the access ladder, leaving exposed rusted bolts protruding at child height. Furthermore, the safety barrier surrounding the swings has been vandalised, with jagged metal fencing left hanging into the bark pit. Several broken glass bottles were also scattered under the slide.\n\nThese conditions pose an immediate danger of severe lacerations and fall injuries to young children playing in the park. My six-year-old brother narrowly avoided cutting his hand on the exposed bolts.\n\nI urge the parks department to cordon off the damaged climbing frame immediately with safety tape, remove the hazardous glass, and complete urgent repairs before the coming weekend. Installing nighttime security cameras would also help deter future vandalism.\n\nYours faithfully,\nMarcus Reed",
      "finalBenchmark": "Benchmark: 167 words • Full criteria met"
    }
  ]
},

  'edexcel-english-writing-l1-paper-10': {
  "title": "Edexcel Functional Skills English Writing Level 1 — Past Paper 10",
  "board": "Pearson Edexcel",
  "subject": "writing",
  "level": "Level 1",
  "paperNumber": 10,
  "durationMinutes": 60,
  "pdfUrl": "https://passfunctionalskills.co.uk/app/uploads/2024/06/FS_English_Writing_Level_1_Past_Paper_10_QP.pdf",
  "modelSolutionPdf": "assets/downloads/past-papers/edexcel/english-level-1/FS_English_Writing_Level_1_Past_Paper_10_Model_Solution_MFS.pdf",
  "videoSolutionSlug": "",
  "questions": [
    {
      "num": 1,
      "section": "Task 1: Formal Workplace Communication",
      "isCalcAllowed": false,
      "marks": 21,
      "markTags": "[12 Composition, 9 SPaG]",
      "targetWords": "200 to 250 words",
      "scenarioTitle": "Work Experience Placement Evaluation Email to Supervisor",
      "scenarioText": "You have completed a two-week administrative work experience placement with a regional distribution company. Your supervisor, Helen, has requested an email evaluating your placement and career development.",
      "promptText": "Write an email to Helen evaluating your placement.\nIn your email, you must:\n• Thank Helen and the team for their guidance and mentorship\n• Summarise the key administrative projects you worked on\n• Explain how the experience improved your professional confidence and skills\n• Outline your future career plans and employment aspirations.",
      "unit": "words",
      "checklist": [
        "Polite greeting and professional expression of gratitude",
        "Summarised daily administrative contributions",
        "Reflected on personal growth and workplace skills",
        "Articulated future educational/career goals",
        "Accurate spelling, punctuation, and grammar"
      ],
      "modelSolution": "Subject: Work Experience Placement Reflection & Evaluation\n\nDear Helen,\n\nI am writing to express my sincere gratitude to you and the entire logistics team for supporting me throughout my two-week administrative work placement at Meridian Distribution. The guidance and encouragement you provided made my placement an incredibly valuable learning journey.\n\nDuring my two weeks with the company, I gained hands-on experience in a variety of vital office operations. I assisted with processing electronic delivery manifests, logged customer delivery queries into the database, and formatted weekly driver schedules. Shadowing the customer service coordinators was particularly fascinating, as it demonstrated how effective communication and calm problem-solving resolve complex logistics delays.\n\nThis placement has substantially boosted my professional confidence. I have mastered advanced spreadsheet functions, learned how to draft formal business correspondence, and become comfortable communicating with commercial suppliers over the phone. Most importantly, working in your busy office has reinforced my ambition to pursue a career in supply chain management. Following the completion of my Functional Skills qualifications, I intend to apply for a Level 3 Business Administration Apprenticeship.\n\nThank you once again for your mentorship and time.\n\nBest regards,\nLeah Miller",
      "finalBenchmark": "Benchmark: 216 words • Full criteria met"
    },
    {
      "num": 2,
      "section": "Task 2: Web Form / Public Contribution",
      "isCalcAllowed": false,
      "marks": 15,
      "markTags": "[9 Composition, 6 SPaG]",
      "targetWords": "150 to 200 words",
      "scenarioTitle": "Vocational Training Course Evaluation Form",
      "scenarioText": "You recently completed an intensive customer service training course. You are filling in a post-course evaluation form reviewing the tutors, course materials, and workshop activities.",
      "promptText": "Complete the course evaluation form.\nIn your form, you must:\n• State the title of the training course and dates attended\n• Describe what aspects of the training were most effective\n• Identify any topics that needed more practical practice\n• Suggest improvements for future cohorts of trainees.",
      "unit": "words",
      "checklist": [
        "Stated course title and training dates",
        "Highlighted effective instructional methods and materials",
        "Constructively identified areas needing more attention",
        "Recommended practical improvements for future sessions",
        "Maintained formal, constructive tone"
      ],
      "modelSolution": "I attended the three-day Professional Customer Service Excellence Workshop from 21st to 23rd October at the Central Training Academy.\n\nThe lead tutor was engaging and used real-world case studies that made the theoretical concepts memorable. The role-playing exercises on de-escalating customer complaints were particularly effective, as they provided immediate constructive feedback on our body language and tone of voice.\n\nHowever, I felt that the module on handling written email complaints was slightly rushed. We were only allocated thirty minutes to draft responses, which did not leave enough time to explore complex billing disputes in depth.\n\nFor future cohorts, I recommend extending the course by half a day to allow for additional practical writing exercises. Providing trainees with a printed reference booklet of standard response templates would also be an invaluable resource to consult in the workplace.\n\nThank you for delivering an excellent training programme.\n\nYours sincerely,\nLeah Miller",
      "finalBenchmark": "Benchmark: 167 words • Full criteria met"
    }
  ]
},

  'edexcel-english-writing-l2-practice-1': {
  "title": "Edexcel Functional Skills English Writing Level 2 — Practice Paper 1",
  "board": "Pearson Edexcel",
  "subject": "writing",
  "level": "Level 2",
  "paperNumber": 1,
  "durationMinutes": 60,
  "pdfUrl": "https://passfunctionalskills.co.uk/wp-content/uploads/2021/09/Edexcel-FS-English-Writing-Level-2-Practice-Paper-1.pdf",
  "modelSolutionPdf": "assets/downloads/past-papers/edexcel/english-level-2/FS_English_Writing_Level_2_Practice_Paper_1_Model_Solution_MFS.pdf",
  "videoSolutionSlug": "",
  "questions": [
    {
      "num": 1,
      "section": "Task 1: Formal Workplace Communication",
      "isCalcAllowed": false,
      "marks": 21,
      "markTags": "[12 Composition, 9 SPaG]",
      "targetWords": "250 to 300 words",
      "scenarioTitle": "Flexible & Hybrid Working Policy Proposal to Senior Management",
      "scenarioText": "Your organisation is reviewing its post-pandemic workplace policies. The Senior Leadership Team has invited employees to submit formal proposals evaluating whether a permanent hybrid working model (combining remote and office-based work) should be adopted.",
      "promptText": "Write a formal proposal to the Senior Leadership Team on hybrid working.\nIn your proposal, you must:\n• Analyse the advantages and potential drawbacks of hybrid working for both staff and the organisation\n• Propose clear guidelines regarding core in-office collaboration days and remote performance metrics\n• Address concerns about team cohesion, data confidentiality, and onboarding junior employees\n• Conclude with a persuasive recommendation on why adopting this policy will future-proof the business.",
      "unit": "words",
      "checklist": [
        "Structured with formal proposal headings and professional executive tone",
        "Thoroughly analysed benefits and challenges for both stakeholders",
        "Formulated specific policy guidelines and measurable criteria",
        "Addressed data security, team culture, and apprentice mentoring",
        "Delivered clear, evidence-based conclusion"
      ],
      "modelSolution": "Proposal for Permanent Adoption of a Structured Hybrid Working Model\n\nTo: The Senior Leadership Team\nFrom: Alex Morgan, Senior Project Coordinator\nDate: 12th November\n\n1. Executive Summary\nThis proposal outlines the strategic advantages of transitioning our organisation to a formal hybrid working model. By combining the flexibility of remote working with focused in-person office collaboration, our company can optimize productivity, enhance employee wellbeing, and reduce facility overheads while maintaining operational excellence.\n\n2. Analysis of Benefits and Strategic Considerations\nThe implementation of hybrid working during recent trials yielded measurable benefits. Commuting time was eliminated on remote days, leading to a reported 24% increase in deep-focus productivity and reduced staff turnover. Furthermore, downsizing physical desk requirements presents long-term estate cost reductions.\n\nConversely, senior leaders have raised legitimate concerns regarding team cohesion, client data security, and the pastoral development of apprentices. Without clear frameworks, isolated remote working can lead to fragmented communication and diminished institutional culture.\n\n3. Proposed Operational Guidelines\nTo balance autonomy with accountability, I recommend the following policies:\n• Structured Collaboration: Teams attend the central office on two mandatory 'core collaboration days' (Tuesdays and Thursdays) dedicated to brainstorming, client presentations, and one-to-one mentoring.\n• Output-Driven Metrics: Performance evaluation must transition from physical hours at desks to demonstrable milestones, task completion rates, and client satisfaction scores.\n• Security and Mentorship Protocols: Implement mandatory multi-factor authentication on all company hardware, and pair every junior trainee with an on-site buddy for dedicated daily support.\n\n4. Recommendation\nAdopting a modern hybrid working policy will establish our firm as an employer of choice, expanding our recruitment pool across the country. I strongly urge the executive board to ratify this framework for the coming financial year.",
      "finalBenchmark": "Benchmark: 284 words • Full criteria met"
    },
    {
      "num": 2,
      "section": "Task 2: Web Form / Public Contribution",
      "isCalcAllowed": false,
      "marks": 15,
      "markTags": "[9 Composition, 6 SPaG]",
      "targetWords": "200 to 250 words",
      "scenarioTitle": "Council Environmental Consultation Formal Submission",
      "scenarioText": "Your municipal council has launched a statutory public consultation on introducing a Clean Air Zone, expanding cycle superhighways, and increasing parking charges in the historic town centre.",
      "promptText": "Write a formal submission to the Council Planning and Environmental Committee.\nIn your contribution, you must:\n• Evaluate the environmental and public health arguments for restricting town centre traffic\n• Discuss the potential economic impact on independent retailers and vulnerable residents\n• Propose balanced compromises (e.g. electric delivery hubs, park-and-ride shuttle subsidies)\n• Conclude with clear recommendations for the committee.",
      "unit": "words",
      "checklist": [
        "Formal committee submission format with reference numbers",
        "Balanced environmental and commercial evaluation",
        "Addressed accessibility for mobility-impaired residents",
        "Formulated pragmatic commercial compromises",
        "Maintained sophisticated, authoritative register"
      ],
      "modelSolution": "Formal Submission: Town Centre Clean Air Zone and Sustainable Transit Consultation\nReference: ENV-CONS-2026/04\n\nI am submitting this formal response to the Council Planning and Environmental Committee regarding the proposed Clean Air Zone and traffic management framework for the historic town centre.\n\nThe health imperative driving this proposal is indisputable. Particulate emissions and nitrogen dioxide levels along the high street currently exceed statutory limits, directly exacerbating asthma and respiratory illnesses among vulnerable residents. Investing in segregated cycle infrastructure and reducing vehicle congestion will undoubtedly create a safer, quieter, and more sustainable public realm.\n\nHowever, the committee must carefully consider the acute economic vulnerabilities facing independent high-street retailers. Introducing substantial parking levies without providing viable transit alternatives risks deterring suburban shoppers, who may simply redirect their custom to out-of-town retail parks with free parking. Furthermore, elderly residents and those with restricted mobility rely on vehicle access to reach essential pharmacies and banking services.\n\nTo reconcile these competing priorities, I urge the committee to adopt a phased compromise:\n1. Provide complimentary zero-emission park-and-ride electric shuttles running every ten minutes from peripheral car parks.\n2. Establish dedicated loading-bay access for commercial couriers before 09:30 and after 17:00.\n3. Grant complete parking fee exemptions for blue-badge holders and healthcare workers.\n\nBy implementing these safeguards, the council can deliver ambitious environmental targets while safeguarding town centre commerce.\n\nYours faithfully,\nAlex Morgan",
      "finalBenchmark": "Benchmark: 238 words • Full criteria met"
    }
  ]
},

  'edexcel-english-writing-l2-practice-2': {
  "title": "Edexcel Functional Skills English Writing Level 2 — Practice Paper 2",
  "board": "Pearson Edexcel",
  "subject": "writing",
  "level": "Level 2",
  "paperNumber": 2,
  "durationMinutes": 60,
  "pdfUrl": "https://passfunctionalskills.co.uk/wp-content/uploads/2021/09/Edexcel-FS-English-Writing-Level-2-Practice-Paper-2.pdf",
  "modelSolutionPdf": "assets/downloads/past-papers/edexcel/english-level-2/FS_English_Writing_Level_2_Practice_Paper_2_Model_Solution_MFS.pdf",
  "videoSolutionSlug": "",
  "questions": [
    {
      "num": 1,
      "section": "Task 1: Formal Workplace Communication",
      "isCalcAllowed": false,
      "marks": 21,
      "markTags": "[12 Composition, 9 SPaG]",
      "targetWords": "250 to 300 words",
      "scenarioTitle": "Workplace Mental Health & Peer Support Scheme Proposal",
      "scenarioText": "Workplace stress and burnout have emerged as key factors contributing to employee sickness absences. You are submitting a formal proposal to the Director of Human Resources recommending the launch of an accredited Mental Health First Aider programme.",
      "promptText": "Write a formal proposal to the HR Director recommending a peer support initiative.\nIn your proposal, you must:\n• Contextualise the impact of unmanaged stress on employee retention and organisational productivity\n• Outline the structure of the proposed Mental Health First Aider network across departments\n• Detail training requirements, confidentiality boundaries, and professional escalation routes\n• Present an actionable implementation timeline with clear success indicators.",
      "unit": "words",
      "checklist": [
        "Professional proposal structure with numbered sections",
        "Articulated organizational and human cost of stress",
        "Structured confidential peer-support architecture",
        "Defined clear ethical and medical escalation boundaries",
        "Included realistic timeline and evaluation metrics"
      ],
      "modelSolution": "Proposal for Implementing an Accredited Workplace Mental Health First Aid Network\n\nTo: Director of Human Resources\nFrom: Cameron Diaz, Operations Supervisor\nDate: 18th November\n\n1. Organizational Context & Business Case\nIn today's fast-paced corporate environment, psychological wellbeing is inextricably linked to organizational resilience. Internal data reveals that stress-related absences accounted for 38% of our firm's lost working days last year, incurring substantial agency staffing costs and diminishing team morale. Establishing proactive peer-support mechanisms is therefore both an ethical imperative and a prudent business strategy.\n\n2. Structure of the Peer Support Network\nI propose establishing a certified network of Mental Health First Aiders (MHFAs) across all regional facilities. Volunteers from diverse seniority levels will be trained to identify early signs of anxiety, depression, and burnout. Rather than acting as clinical therapists, MHFAs will serve as approachable, non-judgemental points of contact, offering active listening and guiding colleagues toward professional support resources.\n\n3. Safeguarding, Training, and Escalation Protocols\nTo protect both peer supporters and employees, rigorous protocols must be instituted:\n• Accredited Instruction: Candidates will complete the standard two-day MHFA England qualification, funded through corporate development budgets.\n• Strict Confidentiality Boundaries: Discussions remain strictly confidential, except where there is an identified risk of self-harm or harm to others.\n• Escalation Pathways: Clear referral pathways will connect staff directly to our Employee Assistance Programme (EAP) and clinical occupational therapy partners.\n\n4. Implementation Timeline and Metrics\nSubject to executive approval, volunteer recruitment will commence in January, followed by training in February and a company-wide launch in March. Success will be evaluated through anonymous quarterly wellbeing surveys and sickness absence monitoring.\n\nI welcome the opportunity to present this vital initiative at the next executive board meeting.",
      "finalBenchmark": "Benchmark: 288 words • Full criteria met"
    },
    {
      "num": 2,
      "section": "Task 2: Web Form / Public Contribution",
      "isCalcAllowed": false,
      "marks": 15,
      "markTags": "[9 Composition, 6 SPaG]",
      "targetWords": "200 to 250 words",
      "scenarioTitle": "Public Transport Regional Disruption Formal Compensation Claim",
      "scenarioText": "You were travelling to an important professional conference when your regional express train was cancelled without warning, stranding hundreds of passengers for three hours in freezing conditions without replacement transport.",
      "promptText": "Write a formal letter of complaint and compensation claim to the Customer Operations Director.\nIn your letter, you must:\n• Provide your booking reference, travel date, and ticket cost details\n• Detail the chronological failures of communication and passenger welfare during the incident\n• Explain the consequential professional losses resulting from your missed conference presentation\n• Demand a full ticket refund, reimbursement of consequential travel expenses, and policy reforms.",
      "unit": "words",
      "checklist": [
        "Formal business letter format with passenger credentials",
        "Chronological exposition of service and duty-of-care failures",
        "Clearly articulated professional and financial repercussions",
        "Specific demand for refunds and consequential cost redress",
        "Firm, dignified, and legally grounded tone"
      ],
      "modelSolution": "Cameron Diaz\n42 St. Andrews Crescent\nBristol, BS8 4ND\n\n19th November\n\nCustomer Operations Director\nGreat Western Rail Services\nMilford House, Swindon\n\nDear Director,\n\nFormal Complaint & Consequential Loss Claim — Booking Ref: GWR-891044-T\n\nI am writing to register an official complaint and claim for consequential financial losses regarding the severe disruption experienced on Friday 13th November on the 07:15 service from Bristol Parkway to London Paddington.\n\nAfter boarding, passengers were informed that the train was cancelled due to an engine defect. Shockingly, staff instructed all passengers to disembark onto an unheated, exposed platform in sub-zero temperatures. For the subsequent three hours, station departure boards displayed conflicting notices, no rail-replacement coaches were dispatched, and station staff abandoned the customer assistance desk, leaving passengers without water, hot beverages, or guidance.\n\nAs a direct consequence of this unacceptable service collapse, I was unable to attend the National Medical Logistics Summit, where I was scheduled to deliver the morning keynote address. In addition to severe reputational damage, our company forfeited a non-refundable £450 conference registration fee and incurred £180 in emergency taxi fares attempting to reach an alternative rail junction.\n\nUnder the National Rail Conditions of Travel and Consumer Rights legislation, I demand:\n1. A 100% refund of my £132.50 first-class return fare under the Delay Repay scheme.\n2. Full reimbursement of the £180 emergency taxi expense (receipt enclosed).\n3. A written explanation of the operational failures that left vulnerable passengers without welfare assistance.\n\nI anticipate your formal response and payment settlement within fourteen days.\n\nYours faithfully,\nCameron Diaz",
      "finalBenchmark": "Benchmark: 247 words • Full criteria met"
    }
  ]
},

  'edexcel-english-writing-l2-paper-10': {
  "title": "Edexcel Functional Skills English Writing Level 2 — Past Paper 10",
  "board": "Pearson Edexcel",
  "subject": "writing",
  "level": "Level 2",
  "paperNumber": 10,
  "durationMinutes": 60,
  "pdfUrl": "https://passfunctionalskills.co.uk/app/uploads/2024/06/FS_English_Writing_Level_2_Past_Paper_10_QP.pdf",
  "modelSolutionPdf": "assets/downloads/past-papers/edexcel/english-level-2/FS_English_Writing_Level_2_Past_Paper_10_Model_Solution_MFS.pdf",
  "videoSolutionSlug": "",
  "questions": [
    {
      "num": 1,
      "section": "Task 1: Formal Workplace Communication",
      "isCalcAllowed": false,
      "marks": 21,
      "markTags": "[12 Composition, 9 SPaG]",
      "targetWords": "250 to 300 words",
      "scenarioTitle": "Community Hub Redevelopment Funding Application Article",
      "scenarioText": "The National Lottery Community Fund has announced a major grant scheme for redeveloping derelict historic buildings into multifunctional community learning hubs. You are writing an in-depth funding bid feature for the community partnership.",
      "promptText": "Write an article for the regional funding committee advocating for the project.\nIn your article, you must:\n• Present the historical context of the Old Town Hall and its current state of disrepair\n• Detail the architectural vision for the new learning hub (digital IT classrooms, youth spaces, maker-space)\n• Explain the socio-economic benefits for local employment, adult literacy, and social inclusion\n• Provide clear justification for why this grant will deliver sustainable community value.",
      "unit": "words",
      "checklist": [
        "Persuasive feature journalism structure with compelling headline",
        "Synthesised heritage preservation with modern community utility",
        "Detailed vocational, educational, and digital inclusion benefits",
        "Demonstrated long-term sustainability and financial viability",
        "Flawless Level 2 vocabulary, register, and syntax"
      ],
      "modelSolution": "Revitalising Our Heritage: Transforming the Old Town Hall into a Beacon of Opportunity\n\nBy Taylor Bailey\n\nA Landmark at the Crossroads of History and Neglect\nFor more than a century, the Old Town Hall stood as the civic heart of our town—a symbol of industrial pride and architectural elegance. Today, however, behind its grand Victorian façade lies a building in poignant decline. Roof leaks, boarded-up windows, and decaying plasterwork threaten to destroy a vital cultural asset. Yet beneath the dust lies an extraordinary opportunity to breathe new life into our community through the National Lottery Community Fund.\n\nA Forward-Looking Vision: The Beacon Community Hub\nOur redevelopment plan does not merely seek to preserve bricks and mortar; it reimagines the space as a 21st-century multipurpose hub for lifelong learning and innovation. The ground floor will house an accessible digital library equipped with high-speed fibre broadband and 3D printing maker-spaces. The upper floors will provide modern seminar classrooms dedicated to adult numeracy, digital literacy, and English language qualifications, alongside collaborative co-working desks for local micro-entrepreneurs.\n\nUnlocking Socio-Economic Potential and Social Inclusion\nThis project addresses urgent local disparities. In our borough, youth unemployment remains 6% above the national average, and thousands of adult workers lack basic digital certifications. By partnering with local vocational colleges and charities, the Beacon Hub will deliver accredited training programmes, CV workshops, and after-school coding clubs. Furthermore, an affordable community café run by vocational catering apprentices will generate self-sustaining revenue while combating social isolation among elderly residents.\n\nA Transformative Investment for Generations to Come\nInvesting in the Old Town Hall is an investment in human dignity and collective ambition. We urge the National Lottery Committee to partner with us in restoring our proud past to power a brighter future.",
      "finalBenchmark": "Benchmark: 292 words • Full criteria met"
    },
    {
      "num": 2,
      "section": "Task 2: Web Form / Public Contribution",
      "isCalcAllowed": false,
      "marks": 15,
      "markTags": "[9 Composition, 6 SPaG]",
      "targetWords": "200 to 250 words",
      "scenarioTitle": "Commercial Services Quality Charter & Consumer Audit Report",
      "scenarioText": "Your regional consumer advocacy group has conducted an audit into delivery reliability, hidden fees, and customer service responsiveness across regional parcel logistics firms.",
      "promptText": "Write an executive summary report for the Consumer Standards Authority.\nIn your report, you must:\n• State the scope of the consumer audit and methodology employed\n• Highlight key findings regarding late deliveries, customer communication, and damaged goods\n• Contrast high-performing commercial practices with persistent systemic failures\n• Recommend mandatory regulatory standards to protect online consumers.",
      "unit": "words",
      "checklist": [
        "Formal executive reporting structure with clear findings",
        "Statistical and qualitative audit analysis",
        "Balanced comparison of exemplary vs defective commercial practices",
        "Actionable regulatory recommendations for consumer enforcement",
        "Rigorous formal register and precise technical vocabulary"
      ],
      "modelSolution": "Executive Summary Report: Regional E-Commerce Logistics and Consumer Standards Audit\nPublished by the Regional Consumer Advocacy Group\nDate: 24th November\n\n1. Purpose and Methodology\nThis report investigates consumer satisfaction and operational reliability across five major logistics carriers operating within our regional district over a six-month evaluation period. The study synthesised 2,400 verified consumer complaints, conducted 150 covert test deliveries, and analysed parcel tracking latency across peak promotional sales periods.\n\n2. Primary Findings\nThe audit revealed widespread deficiencies in service delivery and post-purchase customer dispute resolution:\n• Unacceptable Delay Rates: 28% of guaranteed express shipments failed to arrive within advertised delivery windows, with tracking statuses frequently falsified as 'customer not home'.\n• Cargo Damage & Inadequate Redress: Over 14% of parcels showed external crushing or moisture penetration, with automated chatbot systems systematically frustrating consumer refund claims.\n• Systemic Communication Collapse: In 65% of disputed cases, customers were unable to speak with a human agent, leading to prolonged commercial deadlock.\n\n3. Best Practice vs Systemic Failure\nWhile two leading couriers demonstrated exemplary performance through live GPS driver maps, photographic delivery verification, and immediate human mediation, the remaining budget operators consistently offloaded liability onto independent sub-contractors without oversight.\n\n4. Recommendations for Statutory Enforcement\nTo restore public confidence, we recommend that the Consumer Standards Authority introduce:\n1. Mandatory automatic compensation for parcels delayed beyond 48 hours.\n2. Statutory requirements for carriers to provide live human customer service channels during business hours.\n3. Independent dispute arbitration funded by courier registration levies.\n\nYours faithfully,\nTaylor Bailey, Lead Regulatory Auditor",
      "finalBenchmark": "Benchmark: 248 words • Full criteria met"
    }
  ]
},

  // =========================================================================
  // FUNCTIONAL SKILLS ENGLISH READING MOCKS
  // =========================================================================
  'edexcel-english-reading-l1-paper-10': {
  "title": "Edexcel Functional Skills English Reading Level 1 — Past Paper 10",
  "board": "Pearson Edexcel",
  "subject": "reading",
  "level": "Level 1",
  "paperNumber": 10,
  "durationMinutes": 60,
  "pdfUrl": "https://passfunctionalskills.co.uk/app/uploads/2024/06/FS_English_Reading_Level_1_Past_Paper_10_QP.pdf",
  "modelSolutionPdf": "assets/downloads/past-papers/edexcel/english-level-1/FS_English_Reading_Level_1_Past_Paper_10_Model_Solution_MFS.pdf",
  "videoSolutionSlug": "",
  "sourceTexts": [
    {
      "id": "text-a",
      "label": "Text A: Email",
      "title": "Email: Good news from Sam",
      "content": "From: Sam\nTo: Ali\nSubject: Good news\n\nHey Ali,\n\nGood news – I’ve passed my Level 2 in Business Administration. The even better news is I’ve got a job in the finance team at the hospital.\n\nI’m thrilled but also a bit nervous so I’m looking for advice. It’s going to be totally different from what I’m doing now – this new job looks more challenging, but the salary is much better.\n\nThere’s no uniform – so I’ll have to think about what I’m going to wear. What tips do you have for starting this job – especially what to do on the first day?\n\nCheers,\nSam"
    },
    {
      "id": "text-b",
      "label": "Text B: Webpage",
      "title": "Careers Advice: First day in a new job",
      "content": "First day in a new job\n\nBe prepared\nCongratulations – you’ve got a new job. Now you need to prepare for the first day. Re-read the job description so you’re clear about what’s expected of you. Have another look at the company website to update yourself on the latest information and check the dress code. Work out your route there and think about transport. Collect the documents you need to take with you, like proof of your address.\n\nGet off to the right start\nIt’s essential to be punctual on your first day – take care over your appearance and have a suitable workbag. Introduce yourself to people you meet and make sure you smile and look enthusiastic – this will impress everyone straightaway. Take a folder to keep any material you’re given.\n\nLearn names and roles\nAim to learn the names of people, especially those you’re going to be working with – it’s helpful to find out people’s roles and responsibilities too. You’ll be given lots of information on the first day so have something with you to note down the things you need to remember.\n\nBecome involved\nIt can be difficult on the first day to know what to do, but if there’s an opportunity, offer to help out with a task or sit in on a meeting – and ask plenty of questions. You could also make cups of tea (take your own mug) – this will demonstrate you’re willing and eager to be part of the team.\n\nKnow your workplace\nMake sure you get to know the layout of the building – the location of the toilets, the staff restroom and the fire exits. It’s useful to know where your line manager is based and how to get to the canteen – you may be given a work buddy to help you. The first day is exhausting – but everything will become more familiar and easier as the weeks go by.\n\nGood luck!"
    },
    {
      "id": "text-c",
      "label": "Text C: Forum",
      "title": "Careers Advice Web Forum Discussion",
      "content": "Chas:\nDo you remember your first day in your first job? I was totally freaked out – I felt sick with nerves. My grandad said: ‘Just keep smiling’. That advice helped. It’s important to get ready before your first day, like deciding how to travel to your new workplace.\n\nLilli:\nYes, starting a new job is incredibly challenging – you don’t know anyone, everything is unfamiliar – and sometimes there isn’t enough to do. Try to bond with a fellow worker on the first day – later on, they can advise you about things like holiday entitlement.\n\nSeth:\nIt’s tough for sure, Lilli. Writing everything down really helped me on my first day. There’s useful advice online, including reminders to get your paperwork sorted beforehand. After you’ve been there for a few weeks, find out about sick leave.\n\nLilli:\nIt’s sensible to check what to wear before you start. My last job, I turned up in a dress and discovered everyone else in jeans – awkward! My tip for the first day is keep your phone off.\n\nChas:\nI asked about promotion opportunities on the first day in my current job – I was worried it was out of line, but my manager praised my ambition. Now I’ve been in the job a while, I’m planning to request time off to study."
    }
  ],
  "questions": [
    {
      "num": 1,
      "section": "Questions on Text A",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text A: Location & Organisational Feature",
      "scenarioText": "Refer to Text A (Email from Sam) in the Source Booklet.",
      "promptText": "(a) According to Text A, where is Sam’s new job?\n(b) Which organisational feature helped you find this information?",
      "expectedType": "text",
      "parts": [
        {
          "id": "a",
          "label": "Part (a) Location",
          "placeholder": "Where is Sam’s new job?",
          "unit": ""
        },
        {
          "id": "b",
          "label": "Part (b) Feature",
          "placeholder": "Organisational feature identified",
          "unit": ""
        }
      ],
      "modelSolution": "(a) In the finance team at the hospital [1 mark]\n(b) Email body / first paragraph / subject line [1 mark]",
      "finalBenchmark": "At the hospital (finance team) / Email text"
    },
    {
      "num": 2,
      "section": "Questions on Text A",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text A: Vocabulary & Synonyms",
      "scenarioText": "In Text A, Sam writes: ‘especially what to do’.\nYou may use a dictionary to answer this question.",
      "promptText": "Give one word or phrase to replace ‘especially’ that keeps the meaning of this quotation the same.",
      "expectedType": "text",
      "modelSolution": "Accept: particularly / specifically / in particular / mostly [1 mark]",
      "finalBenchmark": "particularly / specifically"
    },
    {
      "num": 3,
      "section": "Questions on Text A",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text A: Emotion & Attitude Retrieval",
      "scenarioText": "Refer to Text A (Email from Sam).",
      "promptText": "According to Text A, identify two different feelings Sam has about starting the new job.",
      "expectedType": "text",
      "modelSolution": "1. Thrilled (excited) [1 mark]\n2. Nervous (anxious / apprehensive) [1 mark]",
      "finalBenchmark": "1. Thrilled  2. Nervous"
    },
    {
      "num": 4,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Purpose of Text",
      "scenarioText": "Refer to Text B (Careers Advice Webpage).",
      "promptText": "What is the main purpose of Text B?",
      "expectedType": "multiple-choice",
      "options": [
        "A: To advertise job vacancies at a company",
        "B: To give practical guidance on preparing for and surviving your first day at work",
        "C: To explain health and safety laws in office workplaces",
        "D: To review different types of work bags and mugs"
      ],
      "modelSolution": "Correct Answer: B (To give practical guidance on preparing for and surviving your first day at work) [1 mark]",
      "finalBenchmark": "Option B"
    },
    {
      "num": 5,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Information Retrieval (Items)",
      "scenarioText": "Refer to Text B.",
      "promptText": "According to Text B, give two practical items or documents you should collect or take with you on your first day.",
      "expectedType": "text",
      "modelSolution": "Any two from: Proof of address / Suitable workbag / Folder (for keeping material) / Notepad or pen (something to note things down) / Own mug [1 mark each, max 2]",
      "finalBenchmark": "Proof of address / folder / workbag / notepad"
    },
    {
      "num": 6,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Interpersonal Skills & First Impression",
      "scenarioText": "Refer to Text B under the heading ‘Get off to the right start’.",
      "promptText": "What two things should you do when meeting new people to impress everyone straightaway?",
      "expectedType": "text",
      "modelSolution": "1. Introduce yourself [1 mark]\n2. Smile and look enthusiastic [1 mark]",
      "finalBenchmark": "Introduce yourself / Smile and look enthusiastic"
    },
    {
      "num": 7,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Workplace Layout & Facilities",
      "scenarioText": "Refer to Text B under the heading ‘Know your workplace’.",
      "promptText": "Name two facilities or locations in the building layout you should get to know.",
      "expectedType": "text",
      "modelSolution": "Any two from: Toilets / Staff restroom / Fire exits / Where line manager is based / Canteen [1 mark each, max 2]",
      "finalBenchmark": "Toilets / Fire exits / Canteen"
    },
    {
      "num": 8,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Identifying Subheadings",
      "scenarioText": "Refer to Text B.",
      "promptText": "Which sub-heading in Text B contains advice on offering to help with tasks and making cups of tea?",
      "expectedType": "text",
      "modelSolution": "Become involved [1 mark]",
      "finalBenchmark": "Become involved"
    },
    {
      "num": 9,
      "section": "Questions on Text C",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Grandad's Advice",
      "scenarioText": "Refer to Text C (Forum comments).",
      "promptText": "In Text C, what advice from Chas's grandad helped him with his nerves on his first day?",
      "expectedType": "text",
      "modelSolution": "‘Just keep smiling’ [1 mark]",
      "finalBenchmark": "Just keep smiling"
    },
    {
      "num": 10,
      "section": "Questions on Text C",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Telephone Etiquette",
      "scenarioText": "Refer to Lilli's comments in Text C.",
      "promptText": "What specific tip does Lilli give for your first day regarding your mobile phone?",
      "expectedType": "text",
      "modelSolution": "Keep your phone off [1 mark]",
      "finalBenchmark": "Keep your phone off"
    },
    {
      "num": 11,
      "section": "Synthesis: Text B & Text C",
      "isCalcAllowed": false,
      "marks": 3,
      "markTags": "[3 marks]",
      "scenarioTitle": "Comparing Advice across Texts B and C",
      "scenarioText": "Both Text B and Text C give advice about starting a new job.",
      "promptText": "Identify one similarity in the advice given in both Text B and Text C, and one difference in the specific tips mentioned.",
      "expectedType": "text",
      "modelSolution": "Similarity: Both recommend getting paperwork/documents organized before the first day, and checking travel arrangements/transport route [1-2 marks].\nDifference: Text B recommends offering to make cups of tea to show willingness; Text C advises keeping your phone switched off or asking about study leave [1 mark].",
      "finalBenchmark": "Similarity: Paperwork / Route; Difference: Tea / Phone etiquette"
    },
    {
      "num": 12,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Organisational Feature",
      "scenarioText": "Refer to Text B.",
      "promptText": "What organisational feature is used in Text B to divide the article into clear thematic sections?",
      "expectedType": "text",
      "modelSolution": "Subheadings (or Headings / bold titles) [1 mark]",
      "finalBenchmark": "Subheadings"
    },
    {
      "num": 13,
      "section": "Questions on Text C",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Seth's Advice on Sick Leave",
      "scenarioText": "Refer to Seth's comments in Text C.",
      "promptText": "According to Seth, when should you find out about sick leave?",
      "expectedType": "text",
      "modelSolution": "After you’ve been there for a few weeks [1 mark]",
      "finalBenchmark": "After a few weeks"
    },
    {
      "num": 14,
      "section": "Cross-Text Evaluation",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text Format Comparison",
      "scenarioText": "Consider Text A, Text B, and Text C.",
      "promptText": "Which text is written in an informal conversational style featuring multiple different contributors?",
      "expectedType": "multiple-choice",
      "options": [
        "A: Text A",
        "B: Text B",
        "C: Text C",
        "D: None of the texts"
      ],
      "modelSolution": "Correct Answer: C (Text C is an online forum featuring comments from Chas, Lilli, and Seth) [1 mark]",
      "finalBenchmark": "Option C"
    },
    {
      "num": 15,
      "section": "Synthesis: All Texts",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Clothing & Dress Code Advice",
      "scenarioText": "Refer to all three texts regarding workplace clothing and dress code.",
      "promptText": "Identify two pieces of advice given across the texts about what to wear or how to prepare your clothing for a new job.",
      "expectedType": "text",
      "modelSolution": "1. Check the dress code / company website beforehand (Text B) [1 mark]\n2. Take care over your appearance / check what others wear so you don't turn up over/under-dressed (Text B / Text C) [1 mark]",
      "finalBenchmark": "Check dress code / Take care over appearance"
    }
  ]
},

  'edexcel-english-reading-l1-paper-9': {
  "title": "Edexcel Functional Skills English Reading Level 1 — Past Paper 9",
  "board": "Pearson Edexcel",
  "subject": "reading",
  "level": "Level 1",
  "paperNumber": 9,
  "durationMinutes": 60,
  "pdfUrl": "https://passfunctionalskills.co.uk/app/uploads/2024/06/FS_English_Reading_Level_1_Past_Paper_9_QP.pdf",
  "modelSolutionPdf": "assets/downloads/past-papers/edexcel/english-level-1/FS_English_Reading_Level_1_Past_Paper_9_Model_Solution_MFS.pdf",
  "videoSolutionSlug": "",
  "sourceTexts": [
    {
      "id": "text-a",
      "label": "Text A: Newsletter",
      "title": "Community Allotments Initiative Newsletter",
      "content": "From: Jo Harrison, Allotment Project Leader\nTo: All Greenview Community Members\nSubject: New Allotment Plots Now Available!\n\nDear Neighbours,\n\nI am delighted to announce that phase one of the Greenview Community Allotments is officially open! After six months of hard work by local volunteers, twenty raised vegetable beds and a community toolshed are ready for planting.\n\nGrowing your own food is not only cost-effective during rising grocery prices, but it is also fantastic for physical exercise and mental relaxation. Being outdoors in the fresh air helps melt away the stresses of the working week.\n\nPlots cost £35 per year, which includes water access, communal tool usage, and organic compost. We will be holding a free 'Starting Your Plot' induction morning this Saturday at 10:00.\n\nPlease email me by Thursday if you would like to secure a bed.\n\nBest regards,\nJo Harrison"
    },
    {
      "id": "text-b",
      "label": "Text B: Guide",
      "title": "Beginner's Guide to Allotment Gardening",
      "content": "Beginner's Guide to Allotment Gardening\n\nPlanning Your Plot\nBefore you start digging, take time to observe your plot. Note which areas receive full sunlight and which are shaded by fences. Group vegetables with similar water and nutrient needs together to make watering manageable.\n\nSoil Preparation\nHealthy soil is the foundation of abundant crops. Dig in plenty of well-rotted organic matter or homemade compost in early spring. Avoid walking on damp soil, as this compresses the earth and damages delicate root structures.\n\nEssential Tools\nYou do not need to spend a fortune on equipment. The essential starter kit includes:\n• A sturdy stainless steel spade and fork\n• A hand trowel for delicate weeding and planting\n• A 10-litre watering can with a rose sprinkler attachment\n• Durable leather gardening gloves to protect against thorns\n\nPest Control and Companions\nRather than using chemical sprays, protect your crops organically. Planting marigolds alongside tomatoes deters whiteflies, while beer traps and copper tape protect tender lettuce seedlings from slugs. Always cover brassicas with fine netting to stop butterflies laying caterpillars.\n\nCommunity Etiquette\nKeep shared pathways clear of hoses and tools at all times. Share surplus vegetables with neighbours, and keep your weeds under control so seeds do not blow onto adjoining plots."
    },
    {
      "id": "text-c",
      "label": "Text C: Forum",
      "title": "Allotment Growers Community Forum",
      "content": "Ravi:\nI took on my first allotment plot two years ago and it was the best lifestyle decision I ever made. Initially, the weeds were waist-high and I felt like giving up after the first weekend. My tip is: tackle just one square metre at a time and cover the rest with cardboard to suffocate weeds.\n\nMaya:\nTotally agree, Ravi! It’s all about patience. Last summer we harvested so many runner beans and courgettes that we supplied our whole street. The community spirit down at the plots is wonderful—there’s always someone willing to lend a wheelbarrow or advise on blight.\n\nDave:\nMy warning for beginners is: don’t over-sow seed packets! I planted three packets of lettuce at once and ended up with eighty lettuces ready on the same day. Sow a few seeds every fortnight for a continuous fresh harvest."
    }
  ],
  "questions": [
    {
      "num": 1,
      "section": "Questions on Text A",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text A: Key Information Retrieval",
      "scenarioText": "Refer to Text A.",
      "promptText": "(a) According to Text A, what is the main objective of allotment gardening?\n(b) Which organisational feature helped you locate this answer?",
      "expectedType": "text",
      "parts": [
        {
          "id": "a",
          "label": "Part (a) Objective",
          "placeholder": "Main objective",
          "unit": ""
        },
        {
          "id": "b",
          "label": "Part (b) Feature",
          "placeholder": "Organisational feature",
          "unit": ""
        }
      ],
      "modelSolution": "(a) Opening community allotment plots and encouraging residents to grow food affordably [1 mark]\n(b) Heading / Opening paragraph / Bold text [1 mark]",
      "finalBenchmark": "Opening plots / fresh food"
    },
    {
      "num": 2,
      "section": "Questions on Text A",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text A: Vocabulary in Context",
      "scenarioText": "Refer to Text A.\nYou may use a dictionary to answer this question.",
      "promptText": "Give one word or phrase from Text A that means 'cost-effective' in this context.",
      "expectedType": "text",
      "modelSolution": "Accept: affordable / economical / budget-friendly [1 mark]",
      "finalBenchmark": "vital / essential"
    },
    {
      "num": 3,
      "section": "Questions on Text A",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text A: Detail Retrieval",
      "scenarioText": "Refer to Text A.",
      "promptText": "Identify two benefits of allotment gardening mentioned in Text A.",
      "expectedType": "text",
      "modelSolution": "1. Physical exercise and mental relaxation in fresh air [1 mark]\n2. Affordable fresh vegetables and communal compost access [1 mark]",
      "finalBenchmark": "Two distinct benefits from Text A"
    },
    {
      "num": 4,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Main Purpose",
      "scenarioText": "Refer to Text B.",
      "promptText": "What is the main purpose of Text B?",
      "expectedType": "multiple-choice",
      "options": [
        "A: To provide practical guidance and rules regarding allotment gardening",
        "B: To criticise previous council management decisions",
        "C: To advertise commercial equipment for sale",
        "D: To recruit paid staff members"
      ],
      "modelSolution": "Correct Answer: Option A (To provide practical guidance and rules) [1 mark]",
      "finalBenchmark": "Option A"
    },
    {
      "num": 5,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Guidance Steps",
      "scenarioText": "Refer to Text B.",
      "promptText": "Identify two practical steps or items recommended for beginners.",
      "expectedType": "text",
      "modelSolution": "1. Review safety instructions and plan tasks in advance [1 mark]\n2. Use appropriate protective equipment and tools [1 mark]",
      "finalBenchmark": "Two practical steps from Text B"
    },
    {
      "num": 6,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Health and Safety",
      "scenarioText": "Refer to Text B under the safety guidelines.",
      "promptText": "What two safety precautions should participants take according to the text?",
      "expectedType": "text",
      "modelSolution": "1. Wear sturdy footwear and protective gloves [1 mark]\n2. Keep hydration available and take scheduled rest breaks [1 mark]",
      "finalBenchmark": "Footwear/gloves and hydration/breaks"
    },
    {
      "num": 7,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Collaboration Advice",
      "scenarioText": "Refer to Text B.",
      "promptText": "Name two ways participants are encouraged to support their peers or neighbours.",
      "expectedType": "text",
      "modelSolution": "1. Share tools and equipment considerately [1 mark]\n2. Offer assistance to newcomers and communicate regularly [1 mark]",
      "finalBenchmark": "Sharing tools / assisting newcomers"
    },
    {
      "num": 8,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Organisational Structure",
      "scenarioText": "Refer to Text B.",
      "promptText": "Which sub-heading in Text B contains advice on equipment upkeep and storage?",
      "expectedType": "text",
      "modelSolution": "Tools and Maintenance (or Equipment Care) [1 mark]",
      "finalBenchmark": "Subheading identified"
    },
    {
      "num": 9,
      "section": "Questions on Text C",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Participant Experience",
      "scenarioText": "Refer to Text C.",
      "promptText": "What was the main initial challenge described by the first contributor?",
      "expectedType": "text",
      "modelSolution": "Feeling overwhelmed by the initial workload or lack of time [1 mark]",
      "finalBenchmark": "Initial challenge stated"
    },
    {
      "num": 10,
      "section": "Questions on Text C",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Practical Tips",
      "scenarioText": "Refer to Text C.",
      "promptText": "Identify one specific practical tip recommended by a forum contributor.",
      "expectedType": "text",
      "modelSolution": "Keep a written log or schedule tasks into small manageable blocks [1 mark]",
      "finalBenchmark": "Practical tip stated"
    },
    {
      "num": 11,
      "section": "Synthesis: Text B & Text C",
      "isCalcAllowed": false,
      "marks": 3,
      "markTags": "[3 marks]",
      "scenarioTitle": "Comparative Synthesis",
      "scenarioText": "Both Text B and Text C give advice on allotment gardening.",
      "promptText": "Identify one similarity and one difference in the recommendations given across Text B and Text C.",
      "expectedType": "text",
      "modelSolution": "Similarity: Both emphasize preparation, patience, and asking experienced peers for advice [1-2 marks].\nDifference: Text B focuses on formal rules and safety compliance, whereas Text C shares personal anecdotes and informal coping strategies [1 mark].",
      "finalBenchmark": "Valid similarity and difference"
    },
    {
      "num": 12,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Presentation Features",
      "scenarioText": "Refer to Text B.",
      "promptText": "Explain how bullet points are used in Text B to make information accessible to readers.",
      "expectedType": "text",
      "modelSolution": "Bullet points break complex lists into short, digestible points that are easy to scan [1 mark]",
      "finalBenchmark": "Digestible list format / easy to scan"
    },
    {
      "num": 13,
      "section": "Questions on Text C",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Fact vs Opinion",
      "scenarioText": "Refer to Text C.",
      "promptText": "Identify one opinion expressed by a contributor in Text C.",
      "expectedType": "text",
      "modelSolution": "Personal viewpoint stating that taking part was the 'best decision ever made' or 'more fun than expected' [1 mark]",
      "finalBenchmark": "Opinion identified"
    },
    {
      "num": 14,
      "section": "Cross-Text Evaluation",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text Format Comparison",
      "scenarioText": "Refer to all three texts.",
      "promptText": "Which text is an official informational guide designed for public reference?",
      "expectedType": "multiple-choice",
      "options": [
        "A: Text A",
        "B: Text B",
        "C: Text C",
        "D: None of the texts"
      ],
      "modelSolution": "Correct Answer: Option B (Text B is an official informational guide/webpage) [1 mark]",
      "finalBenchmark": "Option B"
    },
    {
      "num": 15,
      "section": "Synthesis: All Texts",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Overarching Theme Synthesis",
      "scenarioText": "Refer to all three texts.",
      "promptText": "Give two reasons why community collaboration is vital for long-term success.",
      "expectedType": "text",
      "modelSolution": "1. Shared effort reduces individual burnout and keeps projects sustainable [1 mark]\n2. Diverse knowledge and peer support help members overcome challenges quickly [1 mark]",
      "finalBenchmark": "Two reasons for collaboration"
    }
  ]
},

  'edexcel-english-reading-l1-paper-8': {
  "title": "Edexcel Functional Skills English Reading Level 1 — Past Paper 8",
  "board": "Pearson Edexcel",
  "subject": "reading",
  "level": "Level 1",
  "paperNumber": 8,
  "durationMinutes": 60,
  "pdfUrl": "https://passfunctionalskills.co.uk/app/uploads/2024/06/FS_English_Reading_Level_1_Past_Paper_8_QP.pdf",
  "modelSolutionPdf": "assets/downloads/past-papers/edexcel/english-level-1/FS_English_Writing_Level_1_Past_Paper_8_Model_Solution_MFS.pdf",
  "videoSolutionSlug": "",
  "sourceTexts": [
    {
      "id": "text-a",
      "label": "Text A: Email",
      "title": "Cycle to Work Scheme Launch Memo",
      "content": "From: David Evans, Facilities Coordinator\nTo: All Staff\nSubject: New Cycle to Work Scheme & Secure Bike Parking\n\nDear Colleagues,\n\nWe are thrilled to announce the launch of our government-backed Cycle to Work scheme, starting next Monday. This initiative allows all permanent employees to purchase a commuter bike and safety accessories tax-free through payroll deduction, saving up to 32% on retail prices.\n\nCycling to work reduces traffic congestion, improves cardiovascular fitness, and saves money on expensive petrol and parking fees.\n\nWe have installed 40 secure, covered bicycle racks near Entrance B, monitored by 24-hour CCTV. In addition, refurbished staff shower facilities and personal lockers are now open on the ground floor.\n\nSign up via the staff intranet before 30th November to qualify for the autumn cycle voucher.\n\nWarm regards,\nDavid Evans"
    },
    {
      "id": "text-b",
      "label": "Text B: Guide",
      "title": "Safe Commuting: Essential Cycling Tips",
      "content": "Safe Commuting: Essential Cycling Tips\n\nRoad Safety & Visibility\nBeing seen by drivers is the single most important safety rule for urban cyclists. Always wear a bright, high-visibility vest or reflective jacket, especially during dawn, dusk, and rainy weather. Legally, your bicycle must be fitted with a working white front light, a red rear light, and amber pedal reflectors when cycling in the dark.\n\nHelmet & Gear Maintenance\nInspect your bicycle helmet before every ride. If a helmet suffers any impact or crack, replace it immediately. Choose breathable, waterproof outerwear to stay comfortable in changing British weather.\n\nThe Quick M-Check\nBefore setting off, perform the five-minute 'M-Check':\n• Tyres: Check pressure and ensure there are no sharp stones embedded in the rubber.\n• Brakes: Squeeze levers firmly; the bike should not roll forward when pushed.\n• Chain: Ensure the chain is clean, lubricated, and does not squeak.\n• Handlebars: Check that the handlebars are aligned straight and tightly secured.\n\nRoute Planning\nAvoid busy dual carriageways where possible. Use dedicated off-road cycle paths and quiet residential backstreets to make your commute relaxing and low-stress."
    },
    {
      "id": "text-c",
      "label": "Text C: Forum",
      "title": "Cycle Commuters Discussion Board",
      "content": "Liam:\nSwapping my train commute for a 6-mile bike ride has completely transformed my mornings. I no longer arrive at work stressed about train cancellations, and I've lost a stone in four months without dieting. My top tip: invest in waterproof pannier bags rather than wearing a heavy backpack, which makes your back sweat.\n\nChloe:\nI was terrified of cycling on main roads at first, but downloading a route-planning app helped me find a peaceful canal route that only adds five minutes to my journey. Having clean showers at work makes a massive difference too!\n\nMark:\nAlways carry a puncture repair kit, a mini hand pump, and a spare inner tube. Getting a flat tyre three miles from the office on a rainy Tuesday morning is miserable if you aren't prepared!"
    }
  ],
  "questions": [
    {
      "num": 1,
      "section": "Questions on Text A",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text A: Key Information Retrieval",
      "scenarioText": "Refer to Text A.",
      "promptText": "(a) According to Text A, what is the main objective of cycle commuting?\n(b) Which organisational feature helped you locate this answer?",
      "expectedType": "text",
      "parts": [
        {
          "id": "a",
          "label": "Part (a) Objective",
          "placeholder": "Main objective",
          "unit": ""
        },
        {
          "id": "b",
          "label": "Part (b) Feature",
          "placeholder": "Organisational feature",
          "unit": ""
        }
      ],
      "modelSolution": "(a) Encouraging employees to cycle to work tax-free and providing secure facilities [1 mark]\n(b) Heading / Opening paragraph / Bold text [1 mark]",
      "finalBenchmark": "Tax-free cycling / secure parking"
    },
    {
      "num": 2,
      "section": "Questions on Text A",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text A: Vocabulary in Context",
      "scenarioText": "Refer to Text A.\nYou may use a dictionary to answer this question.",
      "promptText": "Give one word or phrase from Text A that means 'essential' in this context.",
      "expectedType": "text",
      "modelSolution": "Accept: crucial / vital / necessary / mandatory [1 mark]",
      "finalBenchmark": "vital / essential"
    },
    {
      "num": 3,
      "section": "Questions on Text A",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text A: Detail Retrieval",
      "scenarioText": "Refer to Text A.",
      "promptText": "Identify two benefits of cycle commuting mentioned in Text A.",
      "expectedType": "text",
      "modelSolution": "1. Saves money on fuel and parking while improving cardiovascular fitness [1 mark]\n2. Reduces traffic congestion and offers secure CCTV parking [1 mark]",
      "finalBenchmark": "Two distinct benefits from Text A"
    },
    {
      "num": 4,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Main Purpose",
      "scenarioText": "Refer to Text B.",
      "promptText": "What is the main purpose of Text B?",
      "expectedType": "multiple-choice",
      "options": [
        "A: To provide practical guidance and rules regarding cycle commuting",
        "B: To criticise previous council management decisions",
        "C: To advertise commercial equipment for sale",
        "D: To recruit paid staff members"
      ],
      "modelSolution": "Correct Answer: Option A (To provide practical guidance and rules) [1 mark]",
      "finalBenchmark": "Option A"
    },
    {
      "num": 5,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Guidance Steps",
      "scenarioText": "Refer to Text B.",
      "promptText": "Identify two practical steps or items recommended for beginners.",
      "expectedType": "text",
      "modelSolution": "1. Review safety instructions and plan tasks in advance [1 mark]\n2. Use appropriate protective equipment and tools [1 mark]",
      "finalBenchmark": "Two practical steps from Text B"
    },
    {
      "num": 6,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Health and Safety",
      "scenarioText": "Refer to Text B under the safety guidelines.",
      "promptText": "What two safety precautions should participants take according to the text?",
      "expectedType": "text",
      "modelSolution": "1. Wear sturdy footwear and protective gloves [1 mark]\n2. Keep hydration available and take scheduled rest breaks [1 mark]",
      "finalBenchmark": "Footwear/gloves and hydration/breaks"
    },
    {
      "num": 7,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Collaboration Advice",
      "scenarioText": "Refer to Text B.",
      "promptText": "Name two ways participants are encouraged to support their peers or neighbours.",
      "expectedType": "text",
      "modelSolution": "1. Share tools and equipment considerately [1 mark]\n2. Offer assistance to newcomers and communicate regularly [1 mark]",
      "finalBenchmark": "Sharing tools / assisting newcomers"
    },
    {
      "num": 8,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Organisational Structure",
      "scenarioText": "Refer to Text B.",
      "promptText": "Which sub-heading in Text B contains advice on equipment upkeep and storage?",
      "expectedType": "text",
      "modelSolution": "Tools and Maintenance (or Equipment Care) [1 mark]",
      "finalBenchmark": "Subheading identified"
    },
    {
      "num": 9,
      "section": "Questions on Text C",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Participant Experience",
      "scenarioText": "Refer to Text C.",
      "promptText": "What was the main initial challenge described by the first contributor?",
      "expectedType": "text",
      "modelSolution": "Feeling overwhelmed by the initial workload or lack of time [1 mark]",
      "finalBenchmark": "Initial challenge stated"
    },
    {
      "num": 10,
      "section": "Questions on Text C",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Practical Tips",
      "scenarioText": "Refer to Text C.",
      "promptText": "Identify one specific practical tip recommended by a forum contributor.",
      "expectedType": "text",
      "modelSolution": "Keep a written log or schedule tasks into small manageable blocks [1 mark]",
      "finalBenchmark": "Practical tip stated"
    },
    {
      "num": 11,
      "section": "Synthesis: Text B & Text C",
      "isCalcAllowed": false,
      "marks": 3,
      "markTags": "[3 marks]",
      "scenarioTitle": "Comparative Synthesis",
      "scenarioText": "Both Text B and Text C give advice on cycle commuting.",
      "promptText": "Identify one similarity and one difference in the recommendations given across Text B and Text C.",
      "expectedType": "text",
      "modelSolution": "Similarity: Both emphasize preparation, patience, and asking experienced peers for advice [1-2 marks].\nDifference: Text B focuses on formal rules and safety compliance, whereas Text C shares personal anecdotes and informal coping strategies [1 mark].",
      "finalBenchmark": "Valid similarity and difference"
    },
    {
      "num": 12,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Presentation Features",
      "scenarioText": "Refer to Text B.",
      "promptText": "Explain how bullet points are used in Text B to make information accessible to readers.",
      "expectedType": "text",
      "modelSolution": "Bullet points break complex lists into short, digestible points that are easy to scan [1 mark]",
      "finalBenchmark": "Digestible list format / easy to scan"
    },
    {
      "num": 13,
      "section": "Questions on Text C",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Fact vs Opinion",
      "scenarioText": "Refer to Text C.",
      "promptText": "Identify one opinion expressed by a contributor in Text C.",
      "expectedType": "text",
      "modelSolution": "Personal viewpoint stating that taking part was the 'best decision ever made' or 'more fun than expected' [1 mark]",
      "finalBenchmark": "Opinion identified"
    },
    {
      "num": 14,
      "section": "Cross-Text Evaluation",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text Format Comparison",
      "scenarioText": "Refer to all three texts.",
      "promptText": "Which text is an official informational guide designed for public reference?",
      "expectedType": "multiple-choice",
      "options": [
        "A: Text A",
        "B: Text B",
        "C: Text C",
        "D: None of the texts"
      ],
      "modelSolution": "Correct Answer: Option B (Text B is an official informational guide/webpage) [1 mark]",
      "finalBenchmark": "Option B"
    },
    {
      "num": 15,
      "section": "Synthesis: All Texts",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Overarching Theme Synthesis",
      "scenarioText": "Refer to all three texts.",
      "promptText": "Give two reasons why community collaboration is vital for long-term success.",
      "expectedType": "text",
      "modelSolution": "1. Shared effort reduces individual burnout and keeps projects sustainable [1 mark]\n2. Diverse knowledge and peer support help members overcome challenges quickly [1 mark]",
      "finalBenchmark": "Two reasons for collaboration"
    }
  ]
},

  'edexcel-english-reading-l1-paper-7': {
  "title": "Edexcel Functional Skills English Reading Level 1 — Past Paper 7",
  "board": "Pearson Edexcel",
  "subject": "reading",
  "level": "Level 1",
  "paperNumber": 7,
  "durationMinutes": 60,
  "pdfUrl": "https://passfunctionalskills.co.uk/app/uploads/2024/06/FS_English_Reading_Level_1_PAPER-7_QP.pdf",
  "modelSolutionPdf": "assets/downloads/past-papers/edexcel/english-level-1/FS_English_Reading_Level_1_PAPER-7_Model_Solution_MFS.pdf",
  "videoSolutionSlug": "",
  "sourceTexts": [
    {
      "id": "text-a",
      "label": "Text A: Overview",
      "title": "Text A: Staff Wellbeing Memo",
      "content": "From: Project Coordinator\nTo: Community Members\nSubject: Update on Staff Wellbeing and Healthy Work Habits\n\nDear Friends,\n\nWe are pleased to introduce our comprehensive initiative focusing on wellbeing habits. Over the past six months, feedback from local residents and staff has highlighted the immense value of accessible resources, supportive guidance, and dedicated community spaces.\n\nParticipating in this programme provides meaningful benefits for health, skills development, and daily wellbeing. We invite everyone to get involved and share ideas during our weekly drop-in sessions.\n\nBest regards,\nCoordination Team"
    },
    {
      "id": "text-b",
      "label": "Text B: Guidance",
      "title": "Text B: Ergonomics & Mindfulness Guide",
      "content": "Guidance and Best Practice: Staff Wellbeing and Healthy Work Habits\n\nGetting Started\nBefore taking action, familiarise yourself with available facilities and guidelines. Set achievable goals and discuss expectations with experienced coordinators.\n\nEssential Principles\n• Plan activities in advance and allocate sufficient preparation time.\n• Use designated safety equipment and adhere to standard operational procedures.\n• Maintain clear communication with peers and group leaders.\n• Record progress and celebrate milestones regularly.\n\nOngoing Maintenance and Review\nRegularly evaluate your routines and seek feedback. Sustainable habits develop gradually through consistency and mutual support."
    },
    {
      "id": "text-c",
      "label": "Text C: Discussion",
      "title": "Text C: Employee Feedback Forum",
      "content": "Community Discussion Forum\n\nParticipant 1:\nGetting involved in wellbeing habits was one of the most rewarding steps I've taken. The initial learning curve felt steep, but breaking goals into small steps made all the difference.\n\nParticipant 2:\nThe camaraderie and supportive atmosphere keep me motivated every single week. Having knowledgeable coordinators ready to answer questions makes the journey enjoyable.\n\nParticipant 3:\nMy advice to anyone starting out is to stay patient and avoid rushing. Consistency always beats intensity!"
    }
  ],
  "questions": [
    {
      "num": 1,
      "section": "Questions on Text A",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text A: Key Information Retrieval",
      "scenarioText": "Refer to Text A.",
      "promptText": "(a) According to Text A, what is the main objective of wellbeing habits?\n(b) Which organisational feature helped you locate this answer?",
      "expectedType": "text",
      "parts": [
        {
          "id": "a",
          "label": "Part (a) Objective",
          "placeholder": "Main objective",
          "unit": ""
        },
        {
          "id": "b",
          "label": "Part (b) Feature",
          "placeholder": "Organisational feature",
          "unit": ""
        }
      ],
      "modelSolution": "(a) Promoting wellbeing habits and supporting community members with accessible resources [1 mark]\n(b) Heading / Opening paragraph / Bold text [1 mark]",
      "finalBenchmark": "Accessible resources / community support"
    },
    {
      "num": 2,
      "section": "Questions on Text A",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text A: Vocabulary in Context",
      "scenarioText": "Refer to Text A.\nYou may use a dictionary to answer this question.",
      "promptText": "Give one word or phrase from Text A that means 'comprehensive' in this context.",
      "expectedType": "text",
      "modelSolution": "Accept: thorough / complete / wide-ranging [1 mark]",
      "finalBenchmark": "vital / essential"
    },
    {
      "num": 3,
      "section": "Questions on Text A",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text A: Detail Retrieval",
      "scenarioText": "Refer to Text A.",
      "promptText": "Identify two benefits of wellbeing habits mentioned in Text A.",
      "expectedType": "text",
      "modelSolution": "1. Meaningful benefits for health and skills development [1 mark]\n2. Supportive peer environment and weekly drop-in advice [1 mark]",
      "finalBenchmark": "Two distinct benefits from Text A"
    },
    {
      "num": 4,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Main Purpose",
      "scenarioText": "Refer to Text B.",
      "promptText": "What is the main purpose of Text B?",
      "expectedType": "multiple-choice",
      "options": [
        "A: To provide practical guidance and rules regarding wellbeing habits",
        "B: To criticise previous council management decisions",
        "C: To advertise commercial equipment for sale",
        "D: To recruit paid staff members"
      ],
      "modelSolution": "Correct Answer: Option A (To provide practical guidance and rules) [1 mark]",
      "finalBenchmark": "Option A"
    },
    {
      "num": 5,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Guidance Steps",
      "scenarioText": "Refer to Text B.",
      "promptText": "Identify two practical steps or items recommended for beginners.",
      "expectedType": "text",
      "modelSolution": "1. Review safety instructions and plan tasks in advance [1 mark]\n2. Use appropriate protective equipment and tools [1 mark]",
      "finalBenchmark": "Two practical steps from Text B"
    },
    {
      "num": 6,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Health and Safety",
      "scenarioText": "Refer to Text B under the safety guidelines.",
      "promptText": "What two safety precautions should participants take according to the text?",
      "expectedType": "text",
      "modelSolution": "1. Wear sturdy footwear and protective gloves [1 mark]\n2. Keep hydration available and take scheduled rest breaks [1 mark]",
      "finalBenchmark": "Footwear/gloves and hydration/breaks"
    },
    {
      "num": 7,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Collaboration Advice",
      "scenarioText": "Refer to Text B.",
      "promptText": "Name two ways participants are encouraged to support their peers or neighbours.",
      "expectedType": "text",
      "modelSolution": "1. Share tools and equipment considerately [1 mark]\n2. Offer assistance to newcomers and communicate regularly [1 mark]",
      "finalBenchmark": "Sharing tools / assisting newcomers"
    },
    {
      "num": 8,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Organisational Structure",
      "scenarioText": "Refer to Text B.",
      "promptText": "Which sub-heading in Text B contains advice on equipment upkeep and storage?",
      "expectedType": "text",
      "modelSolution": "Tools and Maintenance (or Equipment Care) [1 mark]",
      "finalBenchmark": "Subheading identified"
    },
    {
      "num": 9,
      "section": "Questions on Text C",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Participant Experience",
      "scenarioText": "Refer to Text C.",
      "promptText": "What was the main initial challenge described by the first contributor?",
      "expectedType": "text",
      "modelSolution": "Feeling overwhelmed by the initial workload or lack of time [1 mark]",
      "finalBenchmark": "Initial challenge stated"
    },
    {
      "num": 10,
      "section": "Questions on Text C",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Practical Tips",
      "scenarioText": "Refer to Text C.",
      "promptText": "Identify one specific practical tip recommended by a forum contributor.",
      "expectedType": "text",
      "modelSolution": "Keep a written log or schedule tasks into small manageable blocks [1 mark]",
      "finalBenchmark": "Practical tip stated"
    },
    {
      "num": 11,
      "section": "Synthesis: Text B & Text C",
      "isCalcAllowed": false,
      "marks": 3,
      "markTags": "[3 marks]",
      "scenarioTitle": "Comparative Synthesis",
      "scenarioText": "Both Text B and Text C give advice on wellbeing habits.",
      "promptText": "Identify one similarity and one difference in the recommendations given across Text B and Text C.",
      "expectedType": "text",
      "modelSolution": "Similarity: Both emphasize preparation, patience, and asking experienced peers for advice [1-2 marks].\nDifference: Text B focuses on formal rules and safety compliance, whereas Text C shares personal anecdotes and informal coping strategies [1 mark].",
      "finalBenchmark": "Valid similarity and difference"
    },
    {
      "num": 12,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Presentation Features",
      "scenarioText": "Refer to Text B.",
      "promptText": "Explain how bullet points are used in Text B to make information accessible to readers.",
      "expectedType": "text",
      "modelSolution": "Bullet points break complex lists into short, digestible points that are easy to scan [1 mark]",
      "finalBenchmark": "Digestible list format / easy to scan"
    },
    {
      "num": 13,
      "section": "Questions on Text C",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Fact vs Opinion",
      "scenarioText": "Refer to Text C.",
      "promptText": "Identify one opinion expressed by a contributor in Text C.",
      "expectedType": "text",
      "modelSolution": "Personal viewpoint stating that taking part was the 'best decision ever made' or 'more fun than expected' [1 mark]",
      "finalBenchmark": "Opinion identified"
    },
    {
      "num": 14,
      "section": "Cross-Text Evaluation",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text Format Comparison",
      "scenarioText": "Refer to all three texts.",
      "promptText": "Which text is an official informational guide designed for public reference?",
      "expectedType": "multiple-choice",
      "options": [
        "A: Text A",
        "B: Text B",
        "C: Text C",
        "D: None of the texts"
      ],
      "modelSolution": "Correct Answer: Option B (Text B is an official informational guide/webpage) [1 mark]",
      "finalBenchmark": "Option B"
    },
    {
      "num": 15,
      "section": "Synthesis: All Texts",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Overarching Theme Synthesis",
      "scenarioText": "Refer to all three texts.",
      "promptText": "Give two reasons why community collaboration is vital for long-term success.",
      "expectedType": "text",
      "modelSolution": "1. Shared effort reduces individual burnout and keeps projects sustainable [1 mark]\n2. Diverse knowledge and peer support help members overcome challenges quickly [1 mark]",
      "finalBenchmark": "Two reasons for collaboration"
    }
  ]
},

  'edexcel-english-reading-l1-paper-6': {
  "title": "Edexcel Functional Skills English Reading Level 1 — Past Paper 6",
  "board": "Pearson Edexcel",
  "subject": "reading",
  "level": "Level 1",
  "paperNumber": 6,
  "durationMinutes": 60,
  "pdfUrl": "https://passfunctionalskills.co.uk/app/uploads/2024/06/FS_English_Reading_Level_1_PAPER-6_QP.pdf",
  "modelSolutionPdf": "assets/downloads/past-papers/edexcel/english-level-1/FS_English_Reading_Level_1_PAPER-6_Model_Solution_MFS.pdf",
  "videoSolutionSlug": "",
  "sourceTexts": [
    {
      "id": "text-a",
      "label": "Text A: Overview",
      "title": "Text A: Volunteering Project Launch",
      "content": "From: Project Coordinator\nTo: Community Members\nSubject: Update on Community Environmental Volunteering\n\nDear Friends,\n\nWe are pleased to introduce our comprehensive initiative focusing on canal and nature conservation. Over the past six months, feedback from local residents and staff has highlighted the immense value of accessible resources, supportive guidance, and dedicated community spaces.\n\nParticipating in this programme provides meaningful benefits for health, skills development, and daily wellbeing. We invite everyone to get involved and share ideas during our weekly drop-in sessions.\n\nBest regards,\nCoordination Team"
    },
    {
      "id": "text-b",
      "label": "Text B: Guidance",
      "title": "Text B: Safety & Environmental Guidelines",
      "content": "Guidance and Best Practice: Community Environmental Volunteering\n\nGetting Started\nBefore taking action, familiarise yourself with available facilities and guidelines. Set achievable goals and discuss expectations with experienced coordinators.\n\nEssential Principles\n• Plan activities in advance and allocate sufficient preparation time.\n• Use designated safety equipment and adhere to standard operational procedures.\n• Maintain clear communication with peers and group leaders.\n• Record progress and celebrate milestones regularly.\n\nOngoing Maintenance and Review\nRegularly evaluate your routines and seek feedback. Sustainable habits develop gradually through consistency and mutual support."
    },
    {
      "id": "text-c",
      "label": "Text C: Discussion",
      "title": "Text C: Volunteers Experience Board",
      "content": "Community Discussion Forum\n\nParticipant 1:\nGetting involved in canal and nature conservation was one of the most rewarding steps I've taken. The initial learning curve felt steep, but breaking goals into small steps made all the difference.\n\nParticipant 2:\nThe camaraderie and supportive atmosphere keep me motivated every single week. Having knowledgeable coordinators ready to answer questions makes the journey enjoyable.\n\nParticipant 3:\nMy advice to anyone starting out is to stay patient and avoid rushing. Consistency always beats intensity!"
    }
  ],
  "questions": [
    {
      "num": 1,
      "section": "Questions on Text A",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text A: Key Information Retrieval",
      "scenarioText": "Refer to Text A.",
      "promptText": "(a) According to Text A, what is the main objective of canal and nature conservation?\n(b) Which organisational feature helped you locate this answer?",
      "expectedType": "text",
      "parts": [
        {
          "id": "a",
          "label": "Part (a) Objective",
          "placeholder": "Main objective",
          "unit": ""
        },
        {
          "id": "b",
          "label": "Part (b) Feature",
          "placeholder": "Organisational feature",
          "unit": ""
        }
      ],
      "modelSolution": "(a) Promoting canal and nature conservation and supporting community members with accessible resources [1 mark]\n(b) Heading / Opening paragraph / Bold text [1 mark]",
      "finalBenchmark": "Accessible resources / community support"
    },
    {
      "num": 2,
      "section": "Questions on Text A",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text A: Vocabulary in Context",
      "scenarioText": "Refer to Text A.\nYou may use a dictionary to answer this question.",
      "promptText": "Give one word or phrase from Text A that means 'comprehensive' in this context.",
      "expectedType": "text",
      "modelSolution": "Accept: thorough / complete / wide-ranging [1 mark]",
      "finalBenchmark": "vital / essential"
    },
    {
      "num": 3,
      "section": "Questions on Text A",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text A: Detail Retrieval",
      "scenarioText": "Refer to Text A.",
      "promptText": "Identify two benefits of canal and nature conservation mentioned in Text A.",
      "expectedType": "text",
      "modelSolution": "1. Meaningful benefits for health and skills development [1 mark]\n2. Supportive peer environment and weekly drop-in advice [1 mark]",
      "finalBenchmark": "Two distinct benefits from Text A"
    },
    {
      "num": 4,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Main Purpose",
      "scenarioText": "Refer to Text B.",
      "promptText": "What is the main purpose of Text B?",
      "expectedType": "multiple-choice",
      "options": [
        "A: To provide practical guidance and rules regarding canal and nature conservation",
        "B: To criticise previous council management decisions",
        "C: To advertise commercial equipment for sale",
        "D: To recruit paid staff members"
      ],
      "modelSolution": "Correct Answer: Option A (To provide practical guidance and rules) [1 mark]",
      "finalBenchmark": "Option A"
    },
    {
      "num": 5,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Guidance Steps",
      "scenarioText": "Refer to Text B.",
      "promptText": "Identify two practical steps or items recommended for beginners.",
      "expectedType": "text",
      "modelSolution": "1. Review safety instructions and plan tasks in advance [1 mark]\n2. Use appropriate protective equipment and tools [1 mark]",
      "finalBenchmark": "Two practical steps from Text B"
    },
    {
      "num": 6,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Health and Safety",
      "scenarioText": "Refer to Text B under the safety guidelines.",
      "promptText": "What two safety precautions should participants take according to the text?",
      "expectedType": "text",
      "modelSolution": "1. Wear sturdy footwear and protective gloves [1 mark]\n2. Keep hydration available and take scheduled rest breaks [1 mark]",
      "finalBenchmark": "Footwear/gloves and hydration/breaks"
    },
    {
      "num": 7,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Collaboration Advice",
      "scenarioText": "Refer to Text B.",
      "promptText": "Name two ways participants are encouraged to support their peers or neighbours.",
      "expectedType": "text",
      "modelSolution": "1. Share tools and equipment considerately [1 mark]\n2. Offer assistance to newcomers and communicate regularly [1 mark]",
      "finalBenchmark": "Sharing tools / assisting newcomers"
    },
    {
      "num": 8,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Organisational Structure",
      "scenarioText": "Refer to Text B.",
      "promptText": "Which sub-heading in Text B contains advice on equipment upkeep and storage?",
      "expectedType": "text",
      "modelSolution": "Tools and Maintenance (or Equipment Care) [1 mark]",
      "finalBenchmark": "Subheading identified"
    },
    {
      "num": 9,
      "section": "Questions on Text C",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Participant Experience",
      "scenarioText": "Refer to Text C.",
      "promptText": "What was the main initial challenge described by the first contributor?",
      "expectedType": "text",
      "modelSolution": "Feeling overwhelmed by the initial workload or lack of time [1 mark]",
      "finalBenchmark": "Initial challenge stated"
    },
    {
      "num": 10,
      "section": "Questions on Text C",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Practical Tips",
      "scenarioText": "Refer to Text C.",
      "promptText": "Identify one specific practical tip recommended by a forum contributor.",
      "expectedType": "text",
      "modelSolution": "Keep a written log or schedule tasks into small manageable blocks [1 mark]",
      "finalBenchmark": "Practical tip stated"
    },
    {
      "num": 11,
      "section": "Synthesis: Text B & Text C",
      "isCalcAllowed": false,
      "marks": 3,
      "markTags": "[3 marks]",
      "scenarioTitle": "Comparative Synthesis",
      "scenarioText": "Both Text B and Text C give advice on canal and nature conservation.",
      "promptText": "Identify one similarity and one difference in the recommendations given across Text B and Text C.",
      "expectedType": "text",
      "modelSolution": "Similarity: Both emphasize preparation, patience, and asking experienced peers for advice [1-2 marks].\nDifference: Text B focuses on formal rules and safety compliance, whereas Text C shares personal anecdotes and informal coping strategies [1 mark].",
      "finalBenchmark": "Valid similarity and difference"
    },
    {
      "num": 12,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Presentation Features",
      "scenarioText": "Refer to Text B.",
      "promptText": "Explain how bullet points are used in Text B to make information accessible to readers.",
      "expectedType": "text",
      "modelSolution": "Bullet points break complex lists into short, digestible points that are easy to scan [1 mark]",
      "finalBenchmark": "Digestible list format / easy to scan"
    },
    {
      "num": 13,
      "section": "Questions on Text C",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Fact vs Opinion",
      "scenarioText": "Refer to Text C.",
      "promptText": "Identify one opinion expressed by a contributor in Text C.",
      "expectedType": "text",
      "modelSolution": "Personal viewpoint stating that taking part was the 'best decision ever made' or 'more fun than expected' [1 mark]",
      "finalBenchmark": "Opinion identified"
    },
    {
      "num": 14,
      "section": "Cross-Text Evaluation",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text Format Comparison",
      "scenarioText": "Refer to all three texts.",
      "promptText": "Which text is an official informational guide designed for public reference?",
      "expectedType": "multiple-choice",
      "options": [
        "A: Text A",
        "B: Text B",
        "C: Text C",
        "D: None of the texts"
      ],
      "modelSolution": "Correct Answer: Option B (Text B is an official informational guide/webpage) [1 mark]",
      "finalBenchmark": "Option B"
    },
    {
      "num": 15,
      "section": "Synthesis: All Texts",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Overarching Theme Synthesis",
      "scenarioText": "Refer to all three texts.",
      "promptText": "Give two reasons why community collaboration is vital for long-term success.",
      "expectedType": "text",
      "modelSolution": "1. Shared effort reduces individual burnout and keeps projects sustainable [1 mark]\n2. Diverse knowledge and peer support help members overcome challenges quickly [1 mark]",
      "finalBenchmark": "Two reasons for collaboration"
    }
  ]
},

  'edexcel-english-reading-l1-paper-4': {
  "title": "Edexcel Functional Skills English Reading Level 1 — Past Paper 4",
  "board": "Pearson Edexcel",
  "subject": "reading",
  "level": "Level 1",
  "paperNumber": 4,
  "durationMinutes": 60,
  "pdfUrl": "https://passfunctionalskills.co.uk/app/uploads/2024/06/FS_English_Reading_Level_1_PAPER-4_QP.pdf",
  "modelSolutionPdf": "assets/downloads/past-papers/edexcel/english-level-1/FS_English_Reading_Level_1_PAPER-4_Model_Solution_MFS.pdf",
  "videoSolutionSlug": "",
  "sourceTexts": [
    {
      "id": "text-a",
      "label": "Text A: Overview",
      "title": "Text A: Transit Network Announcement",
      "content": "From: Project Coordinator\nTo: Community Members\nSubject: Update on Green Public Transport & Transit\n\nDear Friends,\n\nWe are pleased to introduce our comprehensive initiative focusing on public transport commuting. Over the past six months, feedback from local residents and staff has highlighted the immense value of accessible resources, supportive guidance, and dedicated community spaces.\n\nParticipating in this programme provides meaningful benefits for health, skills development, and daily wellbeing. We invite everyone to get involved and share ideas during our weekly drop-in sessions.\n\nBest regards,\nCoordination Team"
    },
    {
      "id": "text-b",
      "label": "Text B: Guidance",
      "title": "Text B: Bus & Train Passenger Guide",
      "content": "Guidance and Best Practice: Green Public Transport & Transit\n\nGetting Started\nBefore taking action, familiarise yourself with available facilities and guidelines. Set achievable goals and discuss expectations with experienced coordinators.\n\nEssential Principles\n• Plan activities in advance and allocate sufficient preparation time.\n• Use designated safety equipment and adhere to standard operational procedures.\n• Maintain clear communication with peers and group leaders.\n• Record progress and celebrate milestones regularly.\n\nOngoing Maintenance and Review\nRegularly evaluate your routines and seek feedback. Sustainable habits develop gradually through consistency and mutual support."
    },
    {
      "id": "text-c",
      "label": "Text C: Discussion",
      "title": "Text C: Commuter Opinions Forum",
      "content": "Community Discussion Forum\n\nParticipant 1:\nGetting involved in public transport commuting was one of the most rewarding steps I've taken. The initial learning curve felt steep, but breaking goals into small steps made all the difference.\n\nParticipant 2:\nThe camaraderie and supportive atmosphere keep me motivated every single week. Having knowledgeable coordinators ready to answer questions makes the journey enjoyable.\n\nParticipant 3:\nMy advice to anyone starting out is to stay patient and avoid rushing. Consistency always beats intensity!"
    }
  ],
  "questions": [
    {
      "num": 1,
      "section": "Questions on Text A",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text A: Key Information Retrieval",
      "scenarioText": "Refer to Text A.",
      "promptText": "(a) According to Text A, what is the main objective of public transport commuting?\n(b) Which organisational feature helped you locate this answer?",
      "expectedType": "text",
      "parts": [
        {
          "id": "a",
          "label": "Part (a) Objective",
          "placeholder": "Main objective",
          "unit": ""
        },
        {
          "id": "b",
          "label": "Part (b) Feature",
          "placeholder": "Organisational feature",
          "unit": ""
        }
      ],
      "modelSolution": "(a) Promoting public transport commuting and supporting community members with accessible resources [1 mark]\n(b) Heading / Opening paragraph / Bold text [1 mark]",
      "finalBenchmark": "Accessible resources / community support"
    },
    {
      "num": 2,
      "section": "Questions on Text A",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text A: Vocabulary in Context",
      "scenarioText": "Refer to Text A.\nYou may use a dictionary to answer this question.",
      "promptText": "Give one word or phrase from Text A that means 'comprehensive' in this context.",
      "expectedType": "text",
      "modelSolution": "Accept: thorough / complete / wide-ranging [1 mark]",
      "finalBenchmark": "vital / essential"
    },
    {
      "num": 3,
      "section": "Questions on Text A",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text A: Detail Retrieval",
      "scenarioText": "Refer to Text A.",
      "promptText": "Identify two benefits of public transport commuting mentioned in Text A.",
      "expectedType": "text",
      "modelSolution": "1. Meaningful benefits for health and skills development [1 mark]\n2. Supportive peer environment and weekly drop-in advice [1 mark]",
      "finalBenchmark": "Two distinct benefits from Text A"
    },
    {
      "num": 4,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Main Purpose",
      "scenarioText": "Refer to Text B.",
      "promptText": "What is the main purpose of Text B?",
      "expectedType": "multiple-choice",
      "options": [
        "A: To provide practical guidance and rules regarding public transport commuting",
        "B: To criticise previous council management decisions",
        "C: To advertise commercial equipment for sale",
        "D: To recruit paid staff members"
      ],
      "modelSolution": "Correct Answer: Option A (To provide practical guidance and rules) [1 mark]",
      "finalBenchmark": "Option A"
    },
    {
      "num": 5,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Guidance Steps",
      "scenarioText": "Refer to Text B.",
      "promptText": "Identify two practical steps or items recommended for beginners.",
      "expectedType": "text",
      "modelSolution": "1. Review safety instructions and plan tasks in advance [1 mark]\n2. Use appropriate protective equipment and tools [1 mark]",
      "finalBenchmark": "Two practical steps from Text B"
    },
    {
      "num": 6,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Health and Safety",
      "scenarioText": "Refer to Text B under the safety guidelines.",
      "promptText": "What two safety precautions should participants take according to the text?",
      "expectedType": "text",
      "modelSolution": "1. Wear sturdy footwear and protective gloves [1 mark]\n2. Keep hydration available and take scheduled rest breaks [1 mark]",
      "finalBenchmark": "Footwear/gloves and hydration/breaks"
    },
    {
      "num": 7,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Collaboration Advice",
      "scenarioText": "Refer to Text B.",
      "promptText": "Name two ways participants are encouraged to support their peers or neighbours.",
      "expectedType": "text",
      "modelSolution": "1. Share tools and equipment considerately [1 mark]\n2. Offer assistance to newcomers and communicate regularly [1 mark]",
      "finalBenchmark": "Sharing tools / assisting newcomers"
    },
    {
      "num": 8,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Organisational Structure",
      "scenarioText": "Refer to Text B.",
      "promptText": "Which sub-heading in Text B contains advice on equipment upkeep and storage?",
      "expectedType": "text",
      "modelSolution": "Tools and Maintenance (or Equipment Care) [1 mark]",
      "finalBenchmark": "Subheading identified"
    },
    {
      "num": 9,
      "section": "Questions on Text C",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Participant Experience",
      "scenarioText": "Refer to Text C.",
      "promptText": "What was the main initial challenge described by the first contributor?",
      "expectedType": "text",
      "modelSolution": "Feeling overwhelmed by the initial workload or lack of time [1 mark]",
      "finalBenchmark": "Initial challenge stated"
    },
    {
      "num": 10,
      "section": "Questions on Text C",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Practical Tips",
      "scenarioText": "Refer to Text C.",
      "promptText": "Identify one specific practical tip recommended by a forum contributor.",
      "expectedType": "text",
      "modelSolution": "Keep a written log or schedule tasks into small manageable blocks [1 mark]",
      "finalBenchmark": "Practical tip stated"
    },
    {
      "num": 11,
      "section": "Synthesis: Text B & Text C",
      "isCalcAllowed": false,
      "marks": 3,
      "markTags": "[3 marks]",
      "scenarioTitle": "Comparative Synthesis",
      "scenarioText": "Both Text B and Text C give advice on public transport commuting.",
      "promptText": "Identify one similarity and one difference in the recommendations given across Text B and Text C.",
      "expectedType": "text",
      "modelSolution": "Similarity: Both emphasize preparation, patience, and asking experienced peers for advice [1-2 marks].\nDifference: Text B focuses on formal rules and safety compliance, whereas Text C shares personal anecdotes and informal coping strategies [1 mark].",
      "finalBenchmark": "Valid similarity and difference"
    },
    {
      "num": 12,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Presentation Features",
      "scenarioText": "Refer to Text B.",
      "promptText": "Explain how bullet points are used in Text B to make information accessible to readers.",
      "expectedType": "text",
      "modelSolution": "Bullet points break complex lists into short, digestible points that are easy to scan [1 mark]",
      "finalBenchmark": "Digestible list format / easy to scan"
    },
    {
      "num": 13,
      "section": "Questions on Text C",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Fact vs Opinion",
      "scenarioText": "Refer to Text C.",
      "promptText": "Identify one opinion expressed by a contributor in Text C.",
      "expectedType": "text",
      "modelSolution": "Personal viewpoint stating that taking part was the 'best decision ever made' or 'more fun than expected' [1 mark]",
      "finalBenchmark": "Opinion identified"
    },
    {
      "num": 14,
      "section": "Cross-Text Evaluation",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text Format Comparison",
      "scenarioText": "Refer to all three texts.",
      "promptText": "Which text is an official informational guide designed for public reference?",
      "expectedType": "multiple-choice",
      "options": [
        "A: Text A",
        "B: Text B",
        "C: Text C",
        "D: None of the texts"
      ],
      "modelSolution": "Correct Answer: Option B (Text B is an official informational guide/webpage) [1 mark]",
      "finalBenchmark": "Option B"
    },
    {
      "num": 15,
      "section": "Synthesis: All Texts",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Overarching Theme Synthesis",
      "scenarioText": "Refer to all three texts.",
      "promptText": "Give two reasons why community collaboration is vital for long-term success.",
      "expectedType": "text",
      "modelSolution": "1. Shared effort reduces individual burnout and keeps projects sustainable [1 mark]\n2. Diverse knowledge and peer support help members overcome challenges quickly [1 mark]",
      "finalBenchmark": "Two reasons for collaboration"
    }
  ]
},

  'edexcel-english-reading-l1-practice-1': {
  "title": "Edexcel Functional Skills English Reading Level 1 — Practice Paper 1",
  "board": "Pearson Edexcel",
  "subject": "reading",
  "level": "Level 1",
  "paperNumber": 1,
  "durationMinutes": 60,
  "pdfUrl": "https://passfunctionalskills.co.uk/app/uploads/2024/06/FS_English_Reading_Level_1_PRACTICE-1_QP.pdf",
  "modelSolutionPdf": "assets/downloads/past-papers/edexcel/english-level-1/FS_English_Reading_Level_1_PRACTICE-1_Model_Solution_MFS.pdf",
  "videoSolutionSlug": "",
  "sourceTexts": [
    {
      "id": "text-a",
      "label": "Text A: Overview",
      "title": "Text A: Volunteer Network Email",
      "content": "From: Project Coordinator\nTo: Community Members\nSubject: Update on Community Volunteering & Mentoring\n\nDear Friends,\n\nWe are pleased to introduce our comprehensive initiative focusing on community volunteering. Over the past six months, feedback from local residents and staff has highlighted the immense value of accessible resources, supportive guidance, and dedicated community spaces.\n\nParticipating in this programme provides meaningful benefits for health, skills development, and daily wellbeing. We invite everyone to get involved and share ideas during our weekly drop-in sessions.\n\nBest regards,\nCoordination Team"
    },
    {
      "id": "text-b",
      "label": "Text B: Guidance",
      "title": "Text B: Volunteer Handbook & Induction",
      "content": "Guidance and Best Practice: Community Volunteering & Mentoring\n\nGetting Started\nBefore taking action, familiarise yourself with available facilities and guidelines. Set achievable goals and discuss expectations with experienced coordinators.\n\nEssential Principles\n• Plan activities in advance and allocate sufficient preparation time.\n• Use designated safety equipment and adhere to standard operational procedures.\n• Maintain clear communication with peers and group leaders.\n• Record progress and celebrate milestones regularly.\n\nOngoing Maintenance and Review\nRegularly evaluate your routines and seek feedback. Sustainable habits develop gradually through consistency and mutual support."
    },
    {
      "id": "text-c",
      "label": "Text C: Discussion",
      "title": "Text C: Volunteers Experience Forum",
      "content": "Community Discussion Forum\n\nParticipant 1:\nGetting involved in community volunteering was one of the most rewarding steps I've taken. The initial learning curve felt steep, but breaking goals into small steps made all the difference.\n\nParticipant 2:\nThe camaraderie and supportive atmosphere keep me motivated every single week. Having knowledgeable coordinators ready to answer questions makes the journey enjoyable.\n\nParticipant 3:\nMy advice to anyone starting out is to stay patient and avoid rushing. Consistency always beats intensity!"
    }
  ],
  "questions": [
    {
      "num": 1,
      "section": "Questions on Text A",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text A: Key Information Retrieval",
      "scenarioText": "Refer to Text A.",
      "promptText": "(a) According to Text A, what is the main objective of community volunteering?\n(b) Which organisational feature helped you locate this answer?",
      "expectedType": "text",
      "parts": [
        {
          "id": "a",
          "label": "Part (a) Objective",
          "placeholder": "Main objective",
          "unit": ""
        },
        {
          "id": "b",
          "label": "Part (b) Feature",
          "placeholder": "Organisational feature",
          "unit": ""
        }
      ],
      "modelSolution": "(a) Promoting community volunteering and supporting community members with accessible resources [1 mark]\n(b) Heading / Opening paragraph / Bold text [1 mark]",
      "finalBenchmark": "Accessible resources / community support"
    },
    {
      "num": 2,
      "section": "Questions on Text A",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text A: Vocabulary in Context",
      "scenarioText": "Refer to Text A.\nYou may use a dictionary to answer this question.",
      "promptText": "Give one word or phrase from Text A that means 'comprehensive' in this context.",
      "expectedType": "text",
      "modelSolution": "Accept: thorough / complete / wide-ranging [1 mark]",
      "finalBenchmark": "vital / essential"
    },
    {
      "num": 3,
      "section": "Questions on Text A",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text A: Detail Retrieval",
      "scenarioText": "Refer to Text A.",
      "promptText": "Identify two benefits of community volunteering mentioned in Text A.",
      "expectedType": "text",
      "modelSolution": "1. Meaningful benefits for health and skills development [1 mark]\n2. Supportive peer environment and weekly drop-in advice [1 mark]",
      "finalBenchmark": "Two distinct benefits from Text A"
    },
    {
      "num": 4,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Main Purpose",
      "scenarioText": "Refer to Text B.",
      "promptText": "What is the main purpose of Text B?",
      "expectedType": "multiple-choice",
      "options": [
        "A: To provide practical guidance and rules regarding community volunteering",
        "B: To criticise previous council management decisions",
        "C: To advertise commercial equipment for sale",
        "D: To recruit paid staff members"
      ],
      "modelSolution": "Correct Answer: Option A (To provide practical guidance and rules) [1 mark]",
      "finalBenchmark": "Option A"
    },
    {
      "num": 5,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Guidance Steps",
      "scenarioText": "Refer to Text B.",
      "promptText": "Identify two practical steps or items recommended for beginners.",
      "expectedType": "text",
      "modelSolution": "1. Review safety instructions and plan tasks in advance [1 mark]\n2. Use appropriate protective equipment and tools [1 mark]",
      "finalBenchmark": "Two practical steps from Text B"
    },
    {
      "num": 6,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Health and Safety",
      "scenarioText": "Refer to Text B under the safety guidelines.",
      "promptText": "What two safety precautions should participants take according to the text?",
      "expectedType": "text",
      "modelSolution": "1. Wear sturdy footwear and protective gloves [1 mark]\n2. Keep hydration available and take scheduled rest breaks [1 mark]",
      "finalBenchmark": "Footwear/gloves and hydration/breaks"
    },
    {
      "num": 7,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Collaboration Advice",
      "scenarioText": "Refer to Text B.",
      "promptText": "Name two ways participants are encouraged to support their peers or neighbours.",
      "expectedType": "text",
      "modelSolution": "1. Share tools and equipment considerately [1 mark]\n2. Offer assistance to newcomers and communicate regularly [1 mark]",
      "finalBenchmark": "Sharing tools / assisting newcomers"
    },
    {
      "num": 8,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Organisational Structure",
      "scenarioText": "Refer to Text B.",
      "promptText": "Which sub-heading in Text B contains advice on equipment upkeep and storage?",
      "expectedType": "text",
      "modelSolution": "Tools and Maintenance (or Equipment Care) [1 mark]",
      "finalBenchmark": "Subheading identified"
    },
    {
      "num": 9,
      "section": "Questions on Text C",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Participant Experience",
      "scenarioText": "Refer to Text C.",
      "promptText": "What was the main initial challenge described by the first contributor?",
      "expectedType": "text",
      "modelSolution": "Feeling overwhelmed by the initial workload or lack of time [1 mark]",
      "finalBenchmark": "Initial challenge stated"
    },
    {
      "num": 10,
      "section": "Questions on Text C",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Practical Tips",
      "scenarioText": "Refer to Text C.",
      "promptText": "Identify one specific practical tip recommended by a forum contributor.",
      "expectedType": "text",
      "modelSolution": "Keep a written log or schedule tasks into small manageable blocks [1 mark]",
      "finalBenchmark": "Practical tip stated"
    },
    {
      "num": 11,
      "section": "Synthesis: Text B & Text C",
      "isCalcAllowed": false,
      "marks": 3,
      "markTags": "[3 marks]",
      "scenarioTitle": "Comparative Synthesis",
      "scenarioText": "Both Text B and Text C give advice on community volunteering.",
      "promptText": "Identify one similarity and one difference in the recommendations given across Text B and Text C.",
      "expectedType": "text",
      "modelSolution": "Similarity: Both emphasize preparation, patience, and asking experienced peers for advice [1-2 marks].\nDifference: Text B focuses on formal rules and safety compliance, whereas Text C shares personal anecdotes and informal coping strategies [1 mark].",
      "finalBenchmark": "Valid similarity and difference"
    },
    {
      "num": 12,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Presentation Features",
      "scenarioText": "Refer to Text B.",
      "promptText": "Explain how bullet points are used in Text B to make information accessible to readers.",
      "expectedType": "text",
      "modelSolution": "Bullet points break complex lists into short, digestible points that are easy to scan [1 mark]",
      "finalBenchmark": "Digestible list format / easy to scan"
    },
    {
      "num": 13,
      "section": "Questions on Text C",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Fact vs Opinion",
      "scenarioText": "Refer to Text C.",
      "promptText": "Identify one opinion expressed by a contributor in Text C.",
      "expectedType": "text",
      "modelSolution": "Personal viewpoint stating that taking part was the 'best decision ever made' or 'more fun than expected' [1 mark]",
      "finalBenchmark": "Opinion identified"
    },
    {
      "num": 14,
      "section": "Cross-Text Evaluation",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text Format Comparison",
      "scenarioText": "Refer to all three texts.",
      "promptText": "Which text is an official informational guide designed for public reference?",
      "expectedType": "multiple-choice",
      "options": [
        "A: Text A",
        "B: Text B",
        "C: Text C",
        "D: None of the texts"
      ],
      "modelSolution": "Correct Answer: Option B (Text B is an official informational guide/webpage) [1 mark]",
      "finalBenchmark": "Option B"
    },
    {
      "num": 15,
      "section": "Synthesis: All Texts",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Overarching Theme Synthesis",
      "scenarioText": "Refer to all three texts.",
      "promptText": "Give two reasons why community collaboration is vital for long-term success.",
      "expectedType": "text",
      "modelSolution": "1. Shared effort reduces individual burnout and keeps projects sustainable [1 mark]\n2. Diverse knowledge and peer support help members overcome challenges quickly [1 mark]",
      "finalBenchmark": "Two reasons for collaboration"
    }
  ]
},

  'edexcel-english-reading-l1-practice-2': {
  "title": "Edexcel Functional Skills English Reading Level 1 — Practice Paper 2",
  "board": "Pearson Edexcel",
  "subject": "reading",
  "level": "Level 1",
  "paperNumber": 2,
  "durationMinutes": 60,
  "pdfUrl": "https://passfunctionalskills.co.uk/app/uploads/2024/06/FS_English_Reading_Level_1_PRACTICE-2_QP.pdf",
  "modelSolutionPdf": "assets/downloads/past-papers/edexcel/english-level-1/FS_English_Reading_Level_1_PRACTICE-2_Model_Solution_MFS.pdf",
  "videoSolutionSlug": "",
  "sourceTexts": [
    {
      "id": "text-a",
      "label": "Text A: Overview",
      "title": "Text A: Active Workday Memo",
      "content": "From: Project Coordinator\nTo: Community Members\nSubject: Update on Active Health & Posture in the Workplace\n\nDear Friends,\n\nWe are pleased to introduce our comprehensive initiative focusing on workplace posture & movement. Over the past six months, feedback from local residents and staff has highlighted the immense value of accessible resources, supportive guidance, and dedicated community spaces.\n\nParticipating in this programme provides meaningful benefits for health, skills development, and daily wellbeing. We invite everyone to get involved and share ideas during our weekly drop-in sessions.\n\nBest regards,\nCoordination Team"
    },
    {
      "id": "text-b",
      "label": "Text B: Guidance",
      "title": "Text B: Office Ergonomics Guide",
      "content": "Guidance and Best Practice: Active Health & Posture in the Workplace\n\nGetting Started\nBefore taking action, familiarise yourself with available facilities and guidelines. Set achievable goals and discuss expectations with experienced coordinators.\n\nEssential Principles\n• Plan activities in advance and allocate sufficient preparation time.\n• Use designated safety equipment and adhere to standard operational procedures.\n• Maintain clear communication with peers and group leaders.\n• Record progress and celebrate milestones regularly.\n\nOngoing Maintenance and Review\nRegularly evaluate your routines and seek feedback. Sustainable habits develop gradually through consistency and mutual support."
    },
    {
      "id": "text-c",
      "label": "Text C: Discussion",
      "title": "Text C: Staff Wellness Forum",
      "content": "Community Discussion Forum\n\nParticipant 1:\nGetting involved in workplace posture & movement was one of the most rewarding steps I've taken. The initial learning curve felt steep, but breaking goals into small steps made all the difference.\n\nParticipant 2:\nThe camaraderie and supportive atmosphere keep me motivated every single week. Having knowledgeable coordinators ready to answer questions makes the journey enjoyable.\n\nParticipant 3:\nMy advice to anyone starting out is to stay patient and avoid rushing. Consistency always beats intensity!"
    }
  ],
  "questions": [
    {
      "num": 1,
      "section": "Questions on Text A",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text A: Key Information Retrieval",
      "scenarioText": "Refer to Text A.",
      "promptText": "(a) According to Text A, what is the main objective of workplace posture & movement?\n(b) Which organisational feature helped you locate this answer?",
      "expectedType": "text",
      "parts": [
        {
          "id": "a",
          "label": "Part (a) Objective",
          "placeholder": "Main objective",
          "unit": ""
        },
        {
          "id": "b",
          "label": "Part (b) Feature",
          "placeholder": "Organisational feature",
          "unit": ""
        }
      ],
      "modelSolution": "(a) Promoting workplace posture & movement and supporting community members with accessible resources [1 mark]\n(b) Heading / Opening paragraph / Bold text [1 mark]",
      "finalBenchmark": "Accessible resources / community support"
    },
    {
      "num": 2,
      "section": "Questions on Text A",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text A: Vocabulary in Context",
      "scenarioText": "Refer to Text A.\nYou may use a dictionary to answer this question.",
      "promptText": "Give one word or phrase from Text A that means 'comprehensive' in this context.",
      "expectedType": "text",
      "modelSolution": "Accept: thorough / complete / wide-ranging [1 mark]",
      "finalBenchmark": "vital / essential"
    },
    {
      "num": 3,
      "section": "Questions on Text A",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text A: Detail Retrieval",
      "scenarioText": "Refer to Text A.",
      "promptText": "Identify two benefits of workplace posture & movement mentioned in Text A.",
      "expectedType": "text",
      "modelSolution": "1. Meaningful benefits for health and skills development [1 mark]\n2. Supportive peer environment and weekly drop-in advice [1 mark]",
      "finalBenchmark": "Two distinct benefits from Text A"
    },
    {
      "num": 4,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Main Purpose",
      "scenarioText": "Refer to Text B.",
      "promptText": "What is the main purpose of Text B?",
      "expectedType": "multiple-choice",
      "options": [
        "A: To provide practical guidance and rules regarding workplace posture & movement",
        "B: To criticise previous council management decisions",
        "C: To advertise commercial equipment for sale",
        "D: To recruit paid staff members"
      ],
      "modelSolution": "Correct Answer: Option A (To provide practical guidance and rules) [1 mark]",
      "finalBenchmark": "Option A"
    },
    {
      "num": 5,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Guidance Steps",
      "scenarioText": "Refer to Text B.",
      "promptText": "Identify two practical steps or items recommended for beginners.",
      "expectedType": "text",
      "modelSolution": "1. Review safety instructions and plan tasks in advance [1 mark]\n2. Use appropriate protective equipment and tools [1 mark]",
      "finalBenchmark": "Two practical steps from Text B"
    },
    {
      "num": 6,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Health and Safety",
      "scenarioText": "Refer to Text B under the safety guidelines.",
      "promptText": "What two safety precautions should participants take according to the text?",
      "expectedType": "text",
      "modelSolution": "1. Wear sturdy footwear and protective gloves [1 mark]\n2. Keep hydration available and take scheduled rest breaks [1 mark]",
      "finalBenchmark": "Footwear/gloves and hydration/breaks"
    },
    {
      "num": 7,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Collaboration Advice",
      "scenarioText": "Refer to Text B.",
      "promptText": "Name two ways participants are encouraged to support their peers or neighbours.",
      "expectedType": "text",
      "modelSolution": "1. Share tools and equipment considerately [1 mark]\n2. Offer assistance to newcomers and communicate regularly [1 mark]",
      "finalBenchmark": "Sharing tools / assisting newcomers"
    },
    {
      "num": 8,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Organisational Structure",
      "scenarioText": "Refer to Text B.",
      "promptText": "Which sub-heading in Text B contains advice on equipment upkeep and storage?",
      "expectedType": "text",
      "modelSolution": "Tools and Maintenance (or Equipment Care) [1 mark]",
      "finalBenchmark": "Subheading identified"
    },
    {
      "num": 9,
      "section": "Questions on Text C",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Participant Experience",
      "scenarioText": "Refer to Text C.",
      "promptText": "What was the main initial challenge described by the first contributor?",
      "expectedType": "text",
      "modelSolution": "Feeling overwhelmed by the initial workload or lack of time [1 mark]",
      "finalBenchmark": "Initial challenge stated"
    },
    {
      "num": 10,
      "section": "Questions on Text C",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Practical Tips",
      "scenarioText": "Refer to Text C.",
      "promptText": "Identify one specific practical tip recommended by a forum contributor.",
      "expectedType": "text",
      "modelSolution": "Keep a written log or schedule tasks into small manageable blocks [1 mark]",
      "finalBenchmark": "Practical tip stated"
    },
    {
      "num": 11,
      "section": "Synthesis: Text B & Text C",
      "isCalcAllowed": false,
      "marks": 3,
      "markTags": "[3 marks]",
      "scenarioTitle": "Comparative Synthesis",
      "scenarioText": "Both Text B and Text C give advice on workplace posture & movement.",
      "promptText": "Identify one similarity and one difference in the recommendations given across Text B and Text C.",
      "expectedType": "text",
      "modelSolution": "Similarity: Both emphasize preparation, patience, and asking experienced peers for advice [1-2 marks].\nDifference: Text B focuses on formal rules and safety compliance, whereas Text C shares personal anecdotes and informal coping strategies [1 mark].",
      "finalBenchmark": "Valid similarity and difference"
    },
    {
      "num": 12,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Presentation Features",
      "scenarioText": "Refer to Text B.",
      "promptText": "Explain how bullet points are used in Text B to make information accessible to readers.",
      "expectedType": "text",
      "modelSolution": "Bullet points break complex lists into short, digestible points that are easy to scan [1 mark]",
      "finalBenchmark": "Digestible list format / easy to scan"
    },
    {
      "num": 13,
      "section": "Questions on Text C",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Fact vs Opinion",
      "scenarioText": "Refer to Text C.",
      "promptText": "Identify one opinion expressed by a contributor in Text C.",
      "expectedType": "text",
      "modelSolution": "Personal viewpoint stating that taking part was the 'best decision ever made' or 'more fun than expected' [1 mark]",
      "finalBenchmark": "Opinion identified"
    },
    {
      "num": 14,
      "section": "Cross-Text Evaluation",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text Format Comparison",
      "scenarioText": "Refer to all three texts.",
      "promptText": "Which text is an official informational guide designed for public reference?",
      "expectedType": "multiple-choice",
      "options": [
        "A: Text A",
        "B: Text B",
        "C: Text C",
        "D: None of the texts"
      ],
      "modelSolution": "Correct Answer: Option B (Text B is an official informational guide/webpage) [1 mark]",
      "finalBenchmark": "Option B"
    },
    {
      "num": 15,
      "section": "Synthesis: All Texts",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Overarching Theme Synthesis",
      "scenarioText": "Refer to all three texts.",
      "promptText": "Give two reasons why community collaboration is vital for long-term success.",
      "expectedType": "text",
      "modelSolution": "1. Shared effort reduces individual burnout and keeps projects sustainable [1 mark]\n2. Diverse knowledge and peer support help members overcome challenges quickly [1 mark]",
      "finalBenchmark": "Two reasons for collaboration"
    }
  ]
},

  'edexcel-english-reading-l1-practice-3': {
  "title": "Edexcel Functional Skills English Reading Level 1 — Practice Paper 3",
  "board": "Pearson Edexcel",
  "subject": "reading",
  "level": "Level 1",
  "paperNumber": 3,
  "durationMinutes": 60,
  "pdfUrl": "https://passfunctionalskills.co.uk/app/uploads/2024/06/FS_English_Reading_Level_1_PRACTICE-3_QP.pdf",
  "modelSolutionPdf": "assets/downloads/past-papers/edexcel/english-level-1/FS_English_Reading_Level_1_PRACTICE-3_Model_Solution_MFS.pdf",
  "videoSolutionSlug": "",
  "sourceTexts": [
    {
      "id": "text-a",
      "label": "Text A: Overview",
      "title": "Text A: Library Upgrade Notice",
      "content": "From: Project Coordinator\nTo: Community Members\nSubject: Update on Digital Libraries & Community Literacy\n\nDear Friends,\n\nWe are pleased to introduce our comprehensive initiative focusing on digital library services. Over the past six months, feedback from local residents and staff has highlighted the immense value of accessible resources, supportive guidance, and dedicated community spaces.\n\nParticipating in this programme provides meaningful benefits for health, skills development, and daily wellbeing. We invite everyone to get involved and share ideas during our weekly drop-in sessions.\n\nBest regards,\nCoordination Team"
    },
    {
      "id": "text-b",
      "label": "Text B: Guidance",
      "title": "Text B: Community Resources Factsheet",
      "content": "Guidance and Best Practice: Digital Libraries & Community Literacy\n\nGetting Started\nBefore taking action, familiarise yourself with available facilities and guidelines. Set achievable goals and discuss expectations with experienced coordinators.\n\nEssential Principles\n• Plan activities in advance and allocate sufficient preparation time.\n• Use designated safety equipment and adhere to standard operational procedures.\n• Maintain clear communication with peers and group leaders.\n• Record progress and celebrate milestones regularly.\n\nOngoing Maintenance and Review\nRegularly evaluate your routines and seek feedback. Sustainable habits develop gradually through consistency and mutual support."
    },
    {
      "id": "text-c",
      "label": "Text C: Discussion",
      "title": "Text C: Library Users Discussion",
      "content": "Community Discussion Forum\n\nParticipant 1:\nGetting involved in digital library services was one of the most rewarding steps I've taken. The initial learning curve felt steep, but breaking goals into small steps made all the difference.\n\nParticipant 2:\nThe camaraderie and supportive atmosphere keep me motivated every single week. Having knowledgeable coordinators ready to answer questions makes the journey enjoyable.\n\nParticipant 3:\nMy advice to anyone starting out is to stay patient and avoid rushing. Consistency always beats intensity!"
    }
  ],
  "questions": [
    {
      "num": 1,
      "section": "Questions on Text A",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text A: Key Information Retrieval",
      "scenarioText": "Refer to Text A.",
      "promptText": "(a) According to Text A, what is the main objective of digital library services?\n(b) Which organisational feature helped you locate this answer?",
      "expectedType": "text",
      "parts": [
        {
          "id": "a",
          "label": "Part (a) Objective",
          "placeholder": "Main objective",
          "unit": ""
        },
        {
          "id": "b",
          "label": "Part (b) Feature",
          "placeholder": "Organisational feature",
          "unit": ""
        }
      ],
      "modelSolution": "(a) Promoting digital library services and supporting community members with accessible resources [1 mark]\n(b) Heading / Opening paragraph / Bold text [1 mark]",
      "finalBenchmark": "Accessible resources / community support"
    },
    {
      "num": 2,
      "section": "Questions on Text A",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text A: Vocabulary in Context",
      "scenarioText": "Refer to Text A.\nYou may use a dictionary to answer this question.",
      "promptText": "Give one word or phrase from Text A that means 'comprehensive' in this context.",
      "expectedType": "text",
      "modelSolution": "Accept: thorough / complete / wide-ranging [1 mark]",
      "finalBenchmark": "vital / essential"
    },
    {
      "num": 3,
      "section": "Questions on Text A",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text A: Detail Retrieval",
      "scenarioText": "Refer to Text A.",
      "promptText": "Identify two benefits of digital library services mentioned in Text A.",
      "expectedType": "text",
      "modelSolution": "1. Meaningful benefits for health and skills development [1 mark]\n2. Supportive peer environment and weekly drop-in advice [1 mark]",
      "finalBenchmark": "Two distinct benefits from Text A"
    },
    {
      "num": 4,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Main Purpose",
      "scenarioText": "Refer to Text B.",
      "promptText": "What is the main purpose of Text B?",
      "expectedType": "multiple-choice",
      "options": [
        "A: To provide practical guidance and rules regarding digital library services",
        "B: To criticise previous council management decisions",
        "C: To advertise commercial equipment for sale",
        "D: To recruit paid staff members"
      ],
      "modelSolution": "Correct Answer: Option A (To provide practical guidance and rules) [1 mark]",
      "finalBenchmark": "Option A"
    },
    {
      "num": 5,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Guidance Steps",
      "scenarioText": "Refer to Text B.",
      "promptText": "Identify two practical steps or items recommended for beginners.",
      "expectedType": "text",
      "modelSolution": "1. Review safety instructions and plan tasks in advance [1 mark]\n2. Use appropriate protective equipment and tools [1 mark]",
      "finalBenchmark": "Two practical steps from Text B"
    },
    {
      "num": 6,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Health and Safety",
      "scenarioText": "Refer to Text B under the safety guidelines.",
      "promptText": "What two safety precautions should participants take according to the text?",
      "expectedType": "text",
      "modelSolution": "1. Wear sturdy footwear and protective gloves [1 mark]\n2. Keep hydration available and take scheduled rest breaks [1 mark]",
      "finalBenchmark": "Footwear/gloves and hydration/breaks"
    },
    {
      "num": 7,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Collaboration Advice",
      "scenarioText": "Refer to Text B.",
      "promptText": "Name two ways participants are encouraged to support their peers or neighbours.",
      "expectedType": "text",
      "modelSolution": "1. Share tools and equipment considerately [1 mark]\n2. Offer assistance to newcomers and communicate regularly [1 mark]",
      "finalBenchmark": "Sharing tools / assisting newcomers"
    },
    {
      "num": 8,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Organisational Structure",
      "scenarioText": "Refer to Text B.",
      "promptText": "Which sub-heading in Text B contains advice on equipment upkeep and storage?",
      "expectedType": "text",
      "modelSolution": "Tools and Maintenance (or Equipment Care) [1 mark]",
      "finalBenchmark": "Subheading identified"
    },
    {
      "num": 9,
      "section": "Questions on Text C",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Participant Experience",
      "scenarioText": "Refer to Text C.",
      "promptText": "What was the main initial challenge described by the first contributor?",
      "expectedType": "text",
      "modelSolution": "Feeling overwhelmed by the initial workload or lack of time [1 mark]",
      "finalBenchmark": "Initial challenge stated"
    },
    {
      "num": 10,
      "section": "Questions on Text C",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Practical Tips",
      "scenarioText": "Refer to Text C.",
      "promptText": "Identify one specific practical tip recommended by a forum contributor.",
      "expectedType": "text",
      "modelSolution": "Keep a written log or schedule tasks into small manageable blocks [1 mark]",
      "finalBenchmark": "Practical tip stated"
    },
    {
      "num": 11,
      "section": "Synthesis: Text B & Text C",
      "isCalcAllowed": false,
      "marks": 3,
      "markTags": "[3 marks]",
      "scenarioTitle": "Comparative Synthesis",
      "scenarioText": "Both Text B and Text C give advice on digital library services.",
      "promptText": "Identify one similarity and one difference in the recommendations given across Text B and Text C.",
      "expectedType": "text",
      "modelSolution": "Similarity: Both emphasize preparation, patience, and asking experienced peers for advice [1-2 marks].\nDifference: Text B focuses on formal rules and safety compliance, whereas Text C shares personal anecdotes and informal coping strategies [1 mark].",
      "finalBenchmark": "Valid similarity and difference"
    },
    {
      "num": 12,
      "section": "Questions on Text B",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Presentation Features",
      "scenarioText": "Refer to Text B.",
      "promptText": "Explain how bullet points are used in Text B to make information accessible to readers.",
      "expectedType": "text",
      "modelSolution": "Bullet points break complex lists into short, digestible points that are easy to scan [1 mark]",
      "finalBenchmark": "Digestible list format / easy to scan"
    },
    {
      "num": 13,
      "section": "Questions on Text C",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Fact vs Opinion",
      "scenarioText": "Refer to Text C.",
      "promptText": "Identify one opinion expressed by a contributor in Text C.",
      "expectedType": "text",
      "modelSolution": "Personal viewpoint stating that taking part was the 'best decision ever made' or 'more fun than expected' [1 mark]",
      "finalBenchmark": "Opinion identified"
    },
    {
      "num": 14,
      "section": "Cross-Text Evaluation",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text Format Comparison",
      "scenarioText": "Refer to all three texts.",
      "promptText": "Which text is an official informational guide designed for public reference?",
      "expectedType": "multiple-choice",
      "options": [
        "A: Text A",
        "B: Text B",
        "C: Text C",
        "D: None of the texts"
      ],
      "modelSolution": "Correct Answer: Option B (Text B is an official informational guide/webpage) [1 mark]",
      "finalBenchmark": "Option B"
    },
    {
      "num": 15,
      "section": "Synthesis: All Texts",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Overarching Theme Synthesis",
      "scenarioText": "Refer to all three texts.",
      "promptText": "Give two reasons why community collaboration is vital for long-term success.",
      "expectedType": "text",
      "modelSolution": "1. Shared effort reduces individual burnout and keeps projects sustainable [1 mark]\n2. Diverse knowledge and peer support help members overcome challenges quickly [1 mark]",
      "finalBenchmark": "Two reasons for collaboration"
    }
  ]
},

  'edexcel-english-reading-l2-practice-1': {
  "title": "Edexcel Functional Skills English Reading Level 2 — Practice Paper 1",
  "board": "Pearson Edexcel",
  "subject": "reading",
  "level": "Level 2",
  "paperNumber": 1,
  "durationMinutes": 75,
  "pdfUrl": "https://passfunctionalskills.co.uk/wp-content/uploads/2021/09/Edexcel-FS-English-Reading-Level-2-Practice-Paper-1.pdf",
  "modelSolutionPdf": "assets/downloads/past-papers/edexcel/english-level-2/FS_English_Reading_Level_2_Practice_Paper_1_Model_Solution_MFS.pdf",
  "videoSolutionSlug": "",
  "sourceTexts": [
    {
      "id": "text-a",
      "label": "Text A: Report",
      "title": "Technical Evaluation: Decentralised Renewable Microgrids",
      "content": "Decentralised Renewable Energy: Operational Performance Analysis\nPublished by the Sustainable Energy Infrastructure Commission\n\n1. Overview and Core Findings\nThe rapid decentralisation of regional electrical networks represents the most profound structural shift in British energy distribution since nationalisation. Community microgrids—localised networks that integrate photovoltaic generation, wind turbines, and industrial battery energy storage systems (BESS)—can operate either synchronously with the national grid or autonomously in 'islanded' mode.\n\nDuring the twelve-month test deployment across South Gloucestershire, the pilot microgrid demonstrated an average 41% reduction in peak-hour transmission losses. Furthermore, commercial facilities within the network experienced zero unscheduled outages, compared to an average of 3.8 hours of grid interruption across the wider regional network.\n\n2. Strategic Infrastructure Imperatives\nHowever, technical success is contingent upon critical baseline capabilities. Smart bi-directional inverters, algorithmic demand-response automation, and hardened cybersecurity firewalls are mandatory to prevent voltage instability. Without standardized interface protocols, integrating disparate domestic battery assets will remain cost-prohibitive for municipal authorities."
    },
    {
      "id": "text-b",
      "label": "Text B: Feature",
      "title": "The Clean Transit Horizon: Urban EV Infrastructure",
      "content": "The Clean Transit Horizon: Revolutionising Urban Energy Infrastructure\nBy Dr Marcus Vance, Senior Research Fellow in Transport Logistics\n\nThe electrification of regional transit systems is universally recognised as a cornerstone of the national net-zero roadmap. Replacing diesel bus fleets and commercial delivery vans with battery-electric alternatives promises to eradicate toxic particulate emissions and drastically reduce urban carbon footprints.\n\nYet beneath this optimistic narrative lies an uncomfortable engineering reality: our legacy electrical distribution grids were never designed to support millions of simultaneous rapid-charging transactions. Innovation cannot succeed in an institutional vacuum. If a regional bus depot attempts to charge eighty double-decker electric buses at 18:00 without localized grid reinforcement, local substations face catastrophic thermal overload.\n\nTo avert systemic grid failure, urban planners must adopt integrated multi-modal microgrids. Installing multi-megawatt commercial battery storage at transit hubs enables operators to trickle-charge storage banks during low-cost overnight wholesale hours, discharging stored green energy directly into vehicle fleets during daytime peak demand. This synergistic approach transforms transit depots from potential grid liabilities into dynamic network assets."
    },
    {
      "id": "text-c",
      "label": "Text C: Editorial",
      "title": "Energy Transition: Public Accountability and True Costs",
      "content": "The Green Energy Paradigm: Who Really Bears the Financial Burden?\nEditorial by Clara Henderson, Chief Economic Columnist\n\nLet us dispense with the rose-tinted corporate brochures. While green technology advocates wax lyrical about utopian zero-carbon microgrids, working-class households are grappling with soaring standing charges on their energy bills to subsidise infrastructure they can neither access nor afford.\n\nIt is reckless and disingenuous to present the rapid overhaul of regional energy grids as a painless technical upgrade. Behind the slick rhetoric of 'algorithmic demand response' lies the prospect of dynamic surge-pricing, penalising families who cannot afford to shift their cooking or heating to off-peak midnight hours.\n\nFurthermore, concentrating public subsidies into wealthy suburban solar pilot projects while neglecting social housing insulation reinforces environmental inequality. If clean energy transitions are to command democratic legitimacy, policymakers must guarantee that funding models are progressive, transparent, and safeguarded against predatory commercial profiteering."
    }
  ],
  "questions": [
    {
      "num": 1,
      "section": "Text A: Factual Retrieval & Synthesis",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text A: Key Findings",
      "scenarioText": "Refer to Text A.",
      "promptText": "Identify two primary factual conclusions reported in Text A regarding renewable energy microgrids and transit infrastructure.",
      "expectedType": "text",
      "parts": [
        {
          "id": "a",
          "label": "Part (a) Finding 1",
          "placeholder": "First factual conclusion",
          "unit": ""
        },
        {
          "id": "b",
          "label": "Part (b) Finding 2",
          "placeholder": "Second factual conclusion",
          "unit": ""
        }
      ],
      "modelSolution": "1. Demonstrated statistical efficiency gains and cost reductions [1 mark]\n2. Identified critical infrastructure requirements needed for scaling [1 mark]",
      "finalBenchmark": "Two valid findings identified"
    },
    {
      "num": 2,
      "section": "Text A: Vocabulary & Subtlety",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text A: Contextual Semantics",
      "scenarioText": "Refer to paragraph 2 of Text A.",
      "promptText": "Explain the meaning of the technical term as used in the context of the report.",
      "expectedType": "text",
      "modelSolution": "Accurate definition reflecting contextual meaning and domain-specific usage [1 mark]",
      "finalBenchmark": "Contextual meaning explained"
    },
    {
      "num": 3,
      "section": "Text A: Fact vs Opinion",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text A: Analytical Differentiation",
      "scenarioText": "Refer to Text A.",
      "promptText": "Identify one verifiable empirical fact and one subjective opinion expressed in Text A.",
      "expectedType": "text",
      "modelSolution": "Fact: Measurable statistical datum or cited study [1 mark]\nOpinion: Subjective qualitative judgment or forecast [1 mark]",
      "finalBenchmark": "One fact and one opinion identified"
    },
    {
      "num": 4,
      "section": "Text B: Primary Purpose & Stance",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Purpose & Register",
      "scenarioText": "Refer to Text B.",
      "promptText": "What is the overarching rhetorical purpose of Text B?",
      "expectedType": "multiple-choice",
      "options": [
        "A: To evaluate the operational viability and challenges of renewable energy microgrids and transit infrastructure",
        "B: To dismiss alternative methodologies as unviable",
        "C: To promote commercial procurement contracts exclusively",
        "D: To entertain general readers with satirical anecdotes"
      ],
      "modelSolution": "Correct Answer: Option A (To evaluate operational viability and challenges) [1 mark]",
      "finalBenchmark": "Option A"
    },
    {
      "num": 5,
      "section": "Text B: Rhetorical & Linguistic Devices",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Persuasive Techniques",
      "scenarioText": "Refer to Text B.",
      "promptText": "Identify two linguistic or stylistic techniques the author uses to engage the target audience.",
      "expectedType": "text",
      "modelSolution": "Any two from: Rhetorical questions / Emotive vocabulary / Triadic phrasing (rule of three) / Expert testimony / Contrastive juxtaposition [1 mark each, max 2]",
      "finalBenchmark": "Two valid linguistic techniques"
    },
    {
      "num": 6,
      "section": "Text B: Implied Meaning",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[2 marks]",
      "scenarioTitle": "Text B: Inference & Nuance",
      "scenarioText": "In Text B, the author notes: 'Innovation cannot succeed in an institutional vacuum.'",
      "promptText": "Explain what the author implies by this statement.",
      "expectedType": "text",
      "modelSolution": "Implies that technical innovation requires supportive regulatory frameworks, political backing, and collaborative infrastructure to be successful [2 marks]",
      "finalBenchmark": "Requires institutional/regulatory support"
    },
    {
      "num": 7,
      "section": "Text B: Organisational Cohesion",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Textual Architecture",
      "scenarioText": "Refer to Text B.",
      "promptText": "Explain how the author employs structural features to present a balanced argument.",
      "expectedType": "text",
      "modelSolution": "Uses comparative subheadings, analytical data tables, and transitional conjunctions to weigh advantages against risks [1-2 marks]",
      "finalBenchmark": "Comparative headings and balanced data"
    },
    {
      "num": 8,
      "section": "Text C: Tone & Register",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Tone Analysis",
      "scenarioText": "Refer to the opening paragraph of Text C.",
      "promptText": "Which adjective best characterises the tone of the writer in Text C?",
      "expectedType": "multiple-choice",
      "options": [
        "A: Critically urgent and provocative",
        "B: Indifferent and unconcerned",
        "C: Light-hearted and humorous",
        "D: Solemnly apologetic"
      ],
      "modelSolution": "Correct Answer: Option A (Critically urgent and provocative) [1 mark]",
      "finalBenchmark": "Option A"
    },
    {
      "num": 9,
      "section": "Text C: Evaluating Bias",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[2 marks]",
      "scenarioTitle": "Text C: Bias & Subjectivity",
      "scenarioText": "Refer to Text C.",
      "promptText": "Identify evidence of potential authorial bias in Text C, explaining how emotive language is used to sway opinion.",
      "expectedType": "text",
      "modelSolution": "Identifies loaded/pejorative adjectives ('reckless', 'short-sighted') used to discredit opposing views without acknowledging counter-evidence [2 marks]",
      "finalBenchmark": "Loaded emotive language cited with analysis"
    },
    {
      "num": 10,
      "section": "Text C: Stakeholder Perspectives",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text C: Contrasting Claims",
      "scenarioText": "Refer to Text C.",
      "promptText": "Identify two distinct stakeholder concerns highlighted by the contributors.",
      "expectedType": "text",
      "modelSolution": "1. Disproportionate financial burden on low-income consumers [1 mark]\n2. Long-term reliability and cybersecurity vulnerabilities [1 mark]",
      "finalBenchmark": "Two stakeholder concerns"
    },
    {
      "num": 11,
      "section": "Synthesis: Text B & Text C",
      "isCalcAllowed": false,
      "marks": 3,
      "markTags": "[3 marks]",
      "scenarioTitle": "Cross-Text Synthesis",
      "scenarioText": "Both Text B and Text C address the transition toward renewable energy microgrids and transit infrastructure.",
      "promptText": "Compare how Text B and Text C approach the question of economic cost and feasibility.",
      "expectedType": "text",
      "modelSolution": "Text B argues that initial capital investment yields substantial long-term net savings through efficiency gains [1 mark]. In contrast, Text C highlights the immediate fiscal strain on local budgets and questions whether return on investment is guaranteed [1 mark]. Both agree that targeted subsidies are required to mitigate hardship [1 mark].",
      "finalBenchmark": "Detailed comparative analysis across both texts"
    },
    {
      "num": 12,
      "section": "Cross-Text Analysis",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Evidence Evaluation",
      "scenarioText": "Refer to Text A and Text B.",
      "promptText": "How does the evidence presented in Text A support the recommendations outlined in Text B?",
      "expectedType": "text",
      "modelSolution": "Empirical data and pilot performance figures in Text A substantiate the feasibility claims and practical guidelines asserted in Text B [1-2 marks]",
      "finalBenchmark": "Empirical validation link established"
    },
    {
      "num": 13,
      "section": "Synthesis: All Texts",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Implicit Assumptions",
      "scenarioText": "Consider the perspectives across all three texts.",
      "promptText": "What underlying assumption is shared by the authors of all three texts?",
      "expectedType": "multiple-choice",
      "options": [
        "A: That continuing with the status quo regarding renewable energy microgrids and transit infrastructure is unsustainable",
        "B: That technological change should be halted immediately",
        "C: That central government should fund 100% of all community expenditure",
        "D: That international regulations do not apply to municipal bodies"
      ],
      "modelSolution": "Correct Answer: Option A (Status quo is unsustainable) [1 mark]",
      "finalBenchmark": "Option A"
    },
    {
      "num": 14,
      "section": "Critical Analysis",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[2 marks]",
      "scenarioTitle": "Audience & Register Alignment",
      "scenarioText": "Compare the writing style and target readership of Text A and Text C.",
      "promptText": "Explain how the register and format of each text are tailored to its intended audience.",
      "expectedType": "text",
      "modelSolution": "Text A employs formal, objective academic prose suited for policymakers and analysts [1 mark]. Text C utilises impassioned, direct rhetorical discourse designed to mobilize public civic action [1 mark].",
      "finalBenchmark": "Formal policy vs public civic rhetoric"
    },
    {
      "num": 15,
      "section": "Synthesis: Concluding Synthesis",
      "isCalcAllowed": false,
      "marks": 3,
      "markTags": "[3 marks]",
      "scenarioTitle": "Strategic Recommendations",
      "scenarioText": "Synthesising insights from all three texts.",
      "promptText": "Outline three critical recommendations for leaders seeking to implement renewable energy microgrids and transit infrastructure effectively.",
      "expectedType": "text",
      "modelSolution": "1. Prioritise robust physical and digital infrastructure planning [1 mark]\n2. Implement transparent, accessible communication to address public scepticism [1 mark]\n3. Establish inclusive financial safety nets for disadvantaged communities [1 mark]",
      "finalBenchmark": "Three strategic recommendations synthesised"
    }
  ]
},

  'edexcel-english-reading-l2-practice-2': {
  "title": "Edexcel Functional Skills English Reading Level 2 — Practice Paper 2",
  "board": "Pearson Edexcel",
  "subject": "reading",
  "level": "Level 2",
  "paperNumber": 2,
  "durationMinutes": 75,
  "pdfUrl": "https://passfunctionalskills.co.uk/app/uploads/2024/06/FS_English_Reading_Level_2_PRACTICE-2_QP.pdf",
  "modelSolutionPdf": "assets/downloads/past-papers/edexcel/english-level-2/FS_English_Reading_Level_2_PRACTICE-2_Model_Solution_MFS.pdf",
  "videoSolutionSlug": "",
  "sourceTexts": [
    {
      "id": "text-a",
      "label": "Text A: Report",
      "title": "Technical Whitepaper: Strategic Developments in Workplace Mental Health And Ergonomics",
      "content": "Comprehensive Strategic Assessment: Workplace Mental Health And Ergonomics\nPublished by the Regional Innovation Research Council\n\n1. Executive Summary & Quantitative Evidence\nThis technical evaluation synthesises performance data, fiscal impacts, and operational outcomes associated with adopting workplace mental health and ergonomics. Over a multi-site empirical trial, organisations demonstrated measurable improvements in productivity and service delivery, with reported efficiency gains averaging 29%.\n\n2. Implementation Frameworks & Systemic Challenges\nTransitioning to new paradigms requires careful change management, robust data governance, and comprehensive workforce training. Leaders must balance digital innovation with equitable accessibility to ensure all user demographics benefit equally."
    },
    {
      "id": "text-b",
      "label": "Text B: Feature",
      "title": "The Evolution of Modern Practice: Implementing Workplace Mental Health And Ergonomics",
      "content": "Critical Analysis: Overcoming Operational Inertia in Workplace Mental Health And Ergonomics\nBy Senior Research Analysts\n\nModern organisations face an imperative to modernise legacy workflows. However, technological and procedural innovation cannot succeed in an institutional vacuum. Strategic alignment between senior leadership, frontline teams, and regulatory bodies is essential.\n\nBy establishing cross-functional working groups and iterative feedback mechanisms, institutions can proactively address emerging bottlenecks while maintaining high service standards."
    },
    {
      "id": "text-c",
      "label": "Text C: Editorial",
      "title": "Perspectives & Public Accountability: Scrutinising Workplace Mental Health And Ergonomics",
      "content": "Public Interest Editorial: Scrutinising the Human Dimensions of Workplace Mental Health And Ergonomics\nBy Lead Investigative Commentators\n\nAs institutional adoption of workplace mental health and ergonomics accelerates, public scrutiny must remain vigilant. Technological and policy transitions often risk marginalising vulnerable service users unless strict ethical standards and oversight frameworks are enforced.\n\nWe urge policymakers to ensure public funding models remain transparent, accessible, and grounded in community dignity."
    }
  ],
  "questions": [
    {
      "num": 1,
      "section": "Text A: Factual Retrieval & Synthesis",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text A: Key Findings",
      "scenarioText": "Refer to Text A.",
      "promptText": "Identify two primary factual conclusions reported in Text A regarding workplace mental health and ergonomics.",
      "expectedType": "text",
      "parts": [
        {
          "id": "a",
          "label": "Part (a) Finding 1",
          "placeholder": "First factual conclusion",
          "unit": ""
        },
        {
          "id": "b",
          "label": "Part (b) Finding 2",
          "placeholder": "Second factual conclusion",
          "unit": ""
        }
      ],
      "modelSolution": "1. Demonstrated statistical efficiency gains and cost reductions [1 mark]\n2. Identified critical infrastructure requirements needed for scaling [1 mark]",
      "finalBenchmark": "Two valid findings identified"
    },
    {
      "num": 2,
      "section": "Text A: Vocabulary & Subtlety",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text A: Contextual Semantics",
      "scenarioText": "Refer to paragraph 2 of Text A.",
      "promptText": "Explain the meaning of the technical term as used in the context of the report.",
      "expectedType": "text",
      "modelSolution": "Accurate definition reflecting contextual meaning and domain-specific usage [1 mark]",
      "finalBenchmark": "Contextual meaning explained"
    },
    {
      "num": 3,
      "section": "Text A: Fact vs Opinion",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text A: Analytical Differentiation",
      "scenarioText": "Refer to Text A.",
      "promptText": "Identify one verifiable empirical fact and one subjective opinion expressed in Text A.",
      "expectedType": "text",
      "modelSolution": "Fact: Measurable statistical datum or cited study [1 mark]\nOpinion: Subjective qualitative judgment or forecast [1 mark]",
      "finalBenchmark": "One fact and one opinion identified"
    },
    {
      "num": 4,
      "section": "Text B: Primary Purpose & Stance",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Purpose & Register",
      "scenarioText": "Refer to Text B.",
      "promptText": "What is the overarching rhetorical purpose of Text B?",
      "expectedType": "multiple-choice",
      "options": [
        "A: To evaluate the operational viability and challenges of workplace mental health and ergonomics",
        "B: To dismiss alternative methodologies as unviable",
        "C: To promote commercial procurement contracts exclusively",
        "D: To entertain general readers with satirical anecdotes"
      ],
      "modelSolution": "Correct Answer: Option A (To evaluate operational viability and challenges) [1 mark]",
      "finalBenchmark": "Option A"
    },
    {
      "num": 5,
      "section": "Text B: Rhetorical & Linguistic Devices",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Persuasive Techniques",
      "scenarioText": "Refer to Text B.",
      "promptText": "Identify two linguistic or stylistic techniques the author uses to engage the target audience.",
      "expectedType": "text",
      "modelSolution": "Any two from: Rhetorical questions / Emotive vocabulary / Triadic phrasing (rule of three) / Expert testimony / Contrastive juxtaposition [1 mark each, max 2]",
      "finalBenchmark": "Two valid linguistic techniques"
    },
    {
      "num": 6,
      "section": "Text B: Implied Meaning",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[2 marks]",
      "scenarioTitle": "Text B: Inference & Nuance",
      "scenarioText": "In Text B, the author notes: 'Innovation cannot succeed in an institutional vacuum.'",
      "promptText": "Explain what the author implies by this statement.",
      "expectedType": "text",
      "modelSolution": "Implies that technical innovation requires supportive regulatory frameworks, political backing, and collaborative infrastructure to be successful [2 marks]",
      "finalBenchmark": "Requires institutional/regulatory support"
    },
    {
      "num": 7,
      "section": "Text B: Organisational Cohesion",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Textual Architecture",
      "scenarioText": "Refer to Text B.",
      "promptText": "Explain how the author employs structural features to present a balanced argument.",
      "expectedType": "text",
      "modelSolution": "Uses comparative subheadings, analytical data tables, and transitional conjunctions to weigh advantages against risks [1-2 marks]",
      "finalBenchmark": "Comparative headings and balanced data"
    },
    {
      "num": 8,
      "section": "Text C: Tone & Register",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Tone Analysis",
      "scenarioText": "Refer to the opening paragraph of Text C.",
      "promptText": "Which adjective best characterises the tone of the writer in Text C?",
      "expectedType": "multiple-choice",
      "options": [
        "A: Critically urgent and provocative",
        "B: Indifferent and unconcerned",
        "C: Light-hearted and humorous",
        "D: Solemnly apologetic"
      ],
      "modelSolution": "Correct Answer: Option A (Critically urgent and provocative) [1 mark]",
      "finalBenchmark": "Option A"
    },
    {
      "num": 9,
      "section": "Text C: Evaluating Bias",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[2 marks]",
      "scenarioTitle": "Text C: Bias & Subjectivity",
      "scenarioText": "Refer to Text C.",
      "promptText": "Identify evidence of potential authorial bias in Text C, explaining how emotive language is used to sway opinion.",
      "expectedType": "text",
      "modelSolution": "Identifies loaded/pejorative adjectives ('reckless', 'short-sighted') used to discredit opposing views without acknowledging counter-evidence [2 marks]",
      "finalBenchmark": "Loaded emotive language cited with analysis"
    },
    {
      "num": 10,
      "section": "Text C: Stakeholder Perspectives",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text C: Contrasting Claims",
      "scenarioText": "Refer to Text C.",
      "promptText": "Identify two distinct stakeholder concerns highlighted by the contributors.",
      "expectedType": "text",
      "modelSolution": "1. Disproportionate financial burden on low-income consumers [1 mark]\n2. Long-term reliability and cybersecurity vulnerabilities [1 mark]",
      "finalBenchmark": "Two stakeholder concerns"
    },
    {
      "num": 11,
      "section": "Synthesis: Text B & Text C",
      "isCalcAllowed": false,
      "marks": 3,
      "markTags": "[3 marks]",
      "scenarioTitle": "Cross-Text Synthesis",
      "scenarioText": "Both Text B and Text C address the transition toward workplace mental health and ergonomics.",
      "promptText": "Compare how Text B and Text C approach the question of economic cost and feasibility.",
      "expectedType": "text",
      "modelSolution": "Text B argues that initial capital investment yields substantial long-term net savings through efficiency gains [1 mark]. In contrast, Text C highlights the immediate fiscal strain on local budgets and questions whether return on investment is guaranteed [1 mark]. Both agree that targeted subsidies are required to mitigate hardship [1 mark].",
      "finalBenchmark": "Detailed comparative analysis across both texts"
    },
    {
      "num": 12,
      "section": "Cross-Text Analysis",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Evidence Evaluation",
      "scenarioText": "Refer to Text A and Text B.",
      "promptText": "How does the evidence presented in Text A support the recommendations outlined in Text B?",
      "expectedType": "text",
      "modelSolution": "Empirical data and pilot performance figures in Text A substantiate the feasibility claims and practical guidelines asserted in Text B [1-2 marks]",
      "finalBenchmark": "Empirical validation link established"
    },
    {
      "num": 13,
      "section": "Synthesis: All Texts",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Implicit Assumptions",
      "scenarioText": "Consider the perspectives across all three texts.",
      "promptText": "What underlying assumption is shared by the authors of all three texts?",
      "expectedType": "multiple-choice",
      "options": [
        "A: That continuing with the status quo regarding workplace mental health and ergonomics is unsustainable",
        "B: That technological change should be halted immediately",
        "C: That central government should fund 100% of all community expenditure",
        "D: That international regulations do not apply to municipal bodies"
      ],
      "modelSolution": "Correct Answer: Option A (Status quo is unsustainable) [1 mark]",
      "finalBenchmark": "Option A"
    },
    {
      "num": 14,
      "section": "Critical Analysis",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[2 marks]",
      "scenarioTitle": "Audience & Register Alignment",
      "scenarioText": "Compare the writing style and target readership of Text A and Text C.",
      "promptText": "Explain how the register and format of each text are tailored to its intended audience.",
      "expectedType": "text",
      "modelSolution": "Text A employs formal, objective academic prose suited for policymakers and analysts [1 mark]. Text C utilises impassioned, direct rhetorical discourse designed to mobilize public civic action [1 mark].",
      "finalBenchmark": "Formal policy vs public civic rhetoric"
    },
    {
      "num": 15,
      "section": "Synthesis: Concluding Synthesis",
      "isCalcAllowed": false,
      "marks": 3,
      "markTags": "[3 marks]",
      "scenarioTitle": "Strategic Recommendations",
      "scenarioText": "Synthesising insights from all three texts.",
      "promptText": "Outline three critical recommendations for leaders seeking to implement workplace mental health and ergonomics effectively.",
      "expectedType": "text",
      "modelSolution": "1. Prioritise robust physical and digital infrastructure planning [1 mark]\n2. Implement transparent, accessible communication to address public scepticism [1 mark]\n3. Establish inclusive financial safety nets for disadvantaged communities [1 mark]",
      "finalBenchmark": "Three strategic recommendations synthesised"
    }
  ]
},

  'edexcel-english-reading-l2-practice-3': {
  "title": "Edexcel Functional Skills English Reading Level 2 — Practice Paper 3",
  "board": "Pearson Edexcel",
  "subject": "reading",
  "level": "Level 2",
  "paperNumber": 3,
  "durationMinutes": 75,
  "pdfUrl": "https://passfunctionalskills.co.uk/app/uploads/2024/06/FS_English_Reading_Level_2_PRACTICE-3_QP.pdf",
  "modelSolutionPdf": "assets/downloads/past-papers/edexcel/english-level-2/FS_English_Reading_Level_2_PRACTICE-3_Model_Solution_MFS.pdf",
  "videoSolutionSlug": "",
  "sourceTexts": [
    {
      "id": "text-a",
      "label": "Text A: Report",
      "title": "Technical Whitepaper: Strategic Developments in Artificial Intelligence In Public Services",
      "content": "Comprehensive Strategic Assessment: Artificial Intelligence In Public Services\nPublished by the Regional Innovation Research Council\n\n1. Executive Summary & Quantitative Evidence\nThis technical evaluation synthesises performance data, fiscal impacts, and operational outcomes associated with adopting artificial intelligence in public services. Over a multi-site empirical trial, organisations demonstrated measurable improvements in productivity and service delivery, with reported efficiency gains averaging 29%.\n\n2. Implementation Frameworks & Systemic Challenges\nTransitioning to new paradigms requires careful change management, robust data governance, and comprehensive workforce training. Leaders must balance digital innovation with equitable accessibility to ensure all user demographics benefit equally."
    },
    {
      "id": "text-b",
      "label": "Text B: Feature",
      "title": "The Evolution of Modern Practice: Implementing Artificial Intelligence In Public Services",
      "content": "Critical Analysis: Overcoming Operational Inertia in Artificial Intelligence In Public Services\nBy Senior Research Analysts\n\nModern organisations face an imperative to modernise legacy workflows. However, technological and procedural innovation cannot succeed in an institutional vacuum. Strategic alignment between senior leadership, frontline teams, and regulatory bodies is essential.\n\nBy establishing cross-functional working groups and iterative feedback mechanisms, institutions can proactively address emerging bottlenecks while maintaining high service standards."
    },
    {
      "id": "text-c",
      "label": "Text C: Editorial",
      "title": "Perspectives & Public Accountability: Scrutinising Artificial Intelligence In Public Services",
      "content": "Public Interest Editorial: Scrutinising the Human Dimensions of Artificial Intelligence In Public Services\nBy Lead Investigative Commentators\n\nAs institutional adoption of artificial intelligence in public services accelerates, public scrutiny must remain vigilant. Technological and policy transitions often risk marginalising vulnerable service users unless strict ethical standards and oversight frameworks are enforced.\n\nWe urge policymakers to ensure public funding models remain transparent, accessible, and grounded in community dignity."
    }
  ],
  "questions": [
    {
      "num": 1,
      "section": "Text A: Factual Retrieval & Synthesis",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text A: Key Findings",
      "scenarioText": "Refer to Text A.",
      "promptText": "Identify two primary factual conclusions reported in Text A regarding artificial intelligence in public services.",
      "expectedType": "text",
      "parts": [
        {
          "id": "a",
          "label": "Part (a) Finding 1",
          "placeholder": "First factual conclusion",
          "unit": ""
        },
        {
          "id": "b",
          "label": "Part (b) Finding 2",
          "placeholder": "Second factual conclusion",
          "unit": ""
        }
      ],
      "modelSolution": "1. Demonstrated statistical efficiency gains and cost reductions [1 mark]\n2. Identified critical infrastructure requirements needed for scaling [1 mark]",
      "finalBenchmark": "Two valid findings identified"
    },
    {
      "num": 2,
      "section": "Text A: Vocabulary & Subtlety",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text A: Contextual Semantics",
      "scenarioText": "Refer to paragraph 2 of Text A.",
      "promptText": "Explain the meaning of the technical term as used in the context of the report.",
      "expectedType": "text",
      "modelSolution": "Accurate definition reflecting contextual meaning and domain-specific usage [1 mark]",
      "finalBenchmark": "Contextual meaning explained"
    },
    {
      "num": 3,
      "section": "Text A: Fact vs Opinion",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text A: Analytical Differentiation",
      "scenarioText": "Refer to Text A.",
      "promptText": "Identify one verifiable empirical fact and one subjective opinion expressed in Text A.",
      "expectedType": "text",
      "modelSolution": "Fact: Measurable statistical datum or cited study [1 mark]\nOpinion: Subjective qualitative judgment or forecast [1 mark]",
      "finalBenchmark": "One fact and one opinion identified"
    },
    {
      "num": 4,
      "section": "Text B: Primary Purpose & Stance",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Purpose & Register",
      "scenarioText": "Refer to Text B.",
      "promptText": "What is the overarching rhetorical purpose of Text B?",
      "expectedType": "multiple-choice",
      "options": [
        "A: To evaluate the operational viability and challenges of artificial intelligence in public services",
        "B: To dismiss alternative methodologies as unviable",
        "C: To promote commercial procurement contracts exclusively",
        "D: To entertain general readers with satirical anecdotes"
      ],
      "modelSolution": "Correct Answer: Option A (To evaluate operational viability and challenges) [1 mark]",
      "finalBenchmark": "Option A"
    },
    {
      "num": 5,
      "section": "Text B: Rhetorical & Linguistic Devices",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Persuasive Techniques",
      "scenarioText": "Refer to Text B.",
      "promptText": "Identify two linguistic or stylistic techniques the author uses to engage the target audience.",
      "expectedType": "text",
      "modelSolution": "Any two from: Rhetorical questions / Emotive vocabulary / Triadic phrasing (rule of three) / Expert testimony / Contrastive juxtaposition [1 mark each, max 2]",
      "finalBenchmark": "Two valid linguistic techniques"
    },
    {
      "num": 6,
      "section": "Text B: Implied Meaning",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[2 marks]",
      "scenarioTitle": "Text B: Inference & Nuance",
      "scenarioText": "In Text B, the author notes: 'Innovation cannot succeed in an institutional vacuum.'",
      "promptText": "Explain what the author implies by this statement.",
      "expectedType": "text",
      "modelSolution": "Implies that technical innovation requires supportive regulatory frameworks, political backing, and collaborative infrastructure to be successful [2 marks]",
      "finalBenchmark": "Requires institutional/regulatory support"
    },
    {
      "num": 7,
      "section": "Text B: Organisational Cohesion",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Textual Architecture",
      "scenarioText": "Refer to Text B.",
      "promptText": "Explain how the author employs structural features to present a balanced argument.",
      "expectedType": "text",
      "modelSolution": "Uses comparative subheadings, analytical data tables, and transitional conjunctions to weigh advantages against risks [1-2 marks]",
      "finalBenchmark": "Comparative headings and balanced data"
    },
    {
      "num": 8,
      "section": "Text C: Tone & Register",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Tone Analysis",
      "scenarioText": "Refer to the opening paragraph of Text C.",
      "promptText": "Which adjective best characterises the tone of the writer in Text C?",
      "expectedType": "multiple-choice",
      "options": [
        "A: Critically urgent and provocative",
        "B: Indifferent and unconcerned",
        "C: Light-hearted and humorous",
        "D: Solemnly apologetic"
      ],
      "modelSolution": "Correct Answer: Option A (Critically urgent and provocative) [1 mark]",
      "finalBenchmark": "Option A"
    },
    {
      "num": 9,
      "section": "Text C: Evaluating Bias",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[2 marks]",
      "scenarioTitle": "Text C: Bias & Subjectivity",
      "scenarioText": "Refer to Text C.",
      "promptText": "Identify evidence of potential authorial bias in Text C, explaining how emotive language is used to sway opinion.",
      "expectedType": "text",
      "modelSolution": "Identifies loaded/pejorative adjectives ('reckless', 'short-sighted') used to discredit opposing views without acknowledging counter-evidence [2 marks]",
      "finalBenchmark": "Loaded emotive language cited with analysis"
    },
    {
      "num": 10,
      "section": "Text C: Stakeholder Perspectives",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text C: Contrasting Claims",
      "scenarioText": "Refer to Text C.",
      "promptText": "Identify two distinct stakeholder concerns highlighted by the contributors.",
      "expectedType": "text",
      "modelSolution": "1. Disproportionate financial burden on low-income consumers [1 mark]\n2. Long-term reliability and cybersecurity vulnerabilities [1 mark]",
      "finalBenchmark": "Two stakeholder concerns"
    },
    {
      "num": 11,
      "section": "Synthesis: Text B & Text C",
      "isCalcAllowed": false,
      "marks": 3,
      "markTags": "[3 marks]",
      "scenarioTitle": "Cross-Text Synthesis",
      "scenarioText": "Both Text B and Text C address the transition toward artificial intelligence in public services.",
      "promptText": "Compare how Text B and Text C approach the question of economic cost and feasibility.",
      "expectedType": "text",
      "modelSolution": "Text B argues that initial capital investment yields substantial long-term net savings through efficiency gains [1 mark]. In contrast, Text C highlights the immediate fiscal strain on local budgets and questions whether return on investment is guaranteed [1 mark]. Both agree that targeted subsidies are required to mitigate hardship [1 mark].",
      "finalBenchmark": "Detailed comparative analysis across both texts"
    },
    {
      "num": 12,
      "section": "Cross-Text Analysis",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Evidence Evaluation",
      "scenarioText": "Refer to Text A and Text B.",
      "promptText": "How does the evidence presented in Text A support the recommendations outlined in Text B?",
      "expectedType": "text",
      "modelSolution": "Empirical data and pilot performance figures in Text A substantiate the feasibility claims and practical guidelines asserted in Text B [1-2 marks]",
      "finalBenchmark": "Empirical validation link established"
    },
    {
      "num": 13,
      "section": "Synthesis: All Texts",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Implicit Assumptions",
      "scenarioText": "Consider the perspectives across all three texts.",
      "promptText": "What underlying assumption is shared by the authors of all three texts?",
      "expectedType": "multiple-choice",
      "options": [
        "A: That continuing with the status quo regarding artificial intelligence in public services is unsustainable",
        "B: That technological change should be halted immediately",
        "C: That central government should fund 100% of all community expenditure",
        "D: That international regulations do not apply to municipal bodies"
      ],
      "modelSolution": "Correct Answer: Option A (Status quo is unsustainable) [1 mark]",
      "finalBenchmark": "Option A"
    },
    {
      "num": 14,
      "section": "Critical Analysis",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[2 marks]",
      "scenarioTitle": "Audience & Register Alignment",
      "scenarioText": "Compare the writing style and target readership of Text A and Text C.",
      "promptText": "Explain how the register and format of each text are tailored to its intended audience.",
      "expectedType": "text",
      "modelSolution": "Text A employs formal, objective academic prose suited for policymakers and analysts [1 mark]. Text C utilises impassioned, direct rhetorical discourse designed to mobilize public civic action [1 mark].",
      "finalBenchmark": "Formal policy vs public civic rhetoric"
    },
    {
      "num": 15,
      "section": "Synthesis: Concluding Synthesis",
      "isCalcAllowed": false,
      "marks": 3,
      "markTags": "[3 marks]",
      "scenarioTitle": "Strategic Recommendations",
      "scenarioText": "Synthesising insights from all three texts.",
      "promptText": "Outline three critical recommendations for leaders seeking to implement artificial intelligence in public services effectively.",
      "expectedType": "text",
      "modelSolution": "1. Prioritise robust physical and digital infrastructure planning [1 mark]\n2. Implement transparent, accessible communication to address public scepticism [1 mark]\n3. Establish inclusive financial safety nets for disadvantaged communities [1 mark]",
      "finalBenchmark": "Three strategic recommendations synthesised"
    }
  ]
},

  'edexcel-english-reading-l2-paper-10': {
  "title": "Edexcel Functional Skills English Reading Level 2 — Past Paper 10",
  "board": "Pearson Edexcel",
  "subject": "reading",
  "level": "Level 2",
  "paperNumber": 10,
  "durationMinutes": 75,
  "pdfUrl": "https://passfunctionalskills.co.uk/app/uploads/2024/06/FS_English_Reading_Level_2_PAPER-10_QP.pdf",
  "modelSolutionPdf": "assets/downloads/past-papers/edexcel/english-level-2/FS_English_Reading_Level_2_PAPER-10_Model_Solution_MFS.pdf",
  "videoSolutionSlug": "",
  "sourceTexts": [
    {
      "id": "text-a",
      "label": "Text A: Report",
      "title": "Technical Whitepaper: Strategic Developments in Digital Healthcare Transformation And Remote Monitoring",
      "content": "Comprehensive Strategic Assessment: Digital Healthcare Transformation And Remote Monitoring\nPublished by the Regional Innovation Research Council\n\n1. Executive Summary & Quantitative Evidence\nThis technical evaluation synthesises performance data, fiscal impacts, and operational outcomes associated with adopting digital healthcare transformation and remote monitoring. Over a multi-site empirical trial, organisations demonstrated measurable improvements in productivity and service delivery, with reported efficiency gains averaging 29%.\n\n2. Implementation Frameworks & Systemic Challenges\nTransitioning to new paradigms requires careful change management, robust data governance, and comprehensive workforce training. Leaders must balance digital innovation with equitable accessibility to ensure all user demographics benefit equally."
    },
    {
      "id": "text-b",
      "label": "Text B: Feature",
      "title": "The Evolution of Modern Practice: Implementing Digital Healthcare Transformation And Remote Monitoring",
      "content": "Critical Analysis: Overcoming Operational Inertia in Digital Healthcare Transformation And Remote Monitoring\nBy Senior Research Analysts\n\nModern organisations face an imperative to modernise legacy workflows. However, technological and procedural innovation cannot succeed in an institutional vacuum. Strategic alignment between senior leadership, frontline teams, and regulatory bodies is essential.\n\nBy establishing cross-functional working groups and iterative feedback mechanisms, institutions can proactively address emerging bottlenecks while maintaining high service standards."
    },
    {
      "id": "text-c",
      "label": "Text C: Editorial",
      "title": "Perspectives & Public Accountability: Scrutinising Digital Healthcare Transformation And Remote Monitoring",
      "content": "Public Interest Editorial: Scrutinising the Human Dimensions of Digital Healthcare Transformation And Remote Monitoring\nBy Lead Investigative Commentators\n\nAs institutional adoption of digital healthcare transformation and remote monitoring accelerates, public scrutiny must remain vigilant. Technological and policy transitions often risk marginalising vulnerable service users unless strict ethical standards and oversight frameworks are enforced.\n\nWe urge policymakers to ensure public funding models remain transparent, accessible, and grounded in community dignity."
    }
  ],
  "questions": [
    {
      "num": 1,
      "section": "Text A: Factual Retrieval & Synthesis",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text A: Key Findings",
      "scenarioText": "Refer to Text A.",
      "promptText": "Identify two primary factual conclusions reported in Text A regarding digital healthcare transformation and remote monitoring.",
      "expectedType": "text",
      "parts": [
        {
          "id": "a",
          "label": "Part (a) Finding 1",
          "placeholder": "First factual conclusion",
          "unit": ""
        },
        {
          "id": "b",
          "label": "Part (b) Finding 2",
          "placeholder": "Second factual conclusion",
          "unit": ""
        }
      ],
      "modelSolution": "1. Demonstrated statistical efficiency gains and cost reductions [1 mark]\n2. Identified critical infrastructure requirements needed for scaling [1 mark]",
      "finalBenchmark": "Two valid findings identified"
    },
    {
      "num": 2,
      "section": "Text A: Vocabulary & Subtlety",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text A: Contextual Semantics",
      "scenarioText": "Refer to paragraph 2 of Text A.",
      "promptText": "Explain the meaning of the technical term as used in the context of the report.",
      "expectedType": "text",
      "modelSolution": "Accurate definition reflecting contextual meaning and domain-specific usage [1 mark]",
      "finalBenchmark": "Contextual meaning explained"
    },
    {
      "num": 3,
      "section": "Text A: Fact vs Opinion",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text A: Analytical Differentiation",
      "scenarioText": "Refer to Text A.",
      "promptText": "Identify one verifiable empirical fact and one subjective opinion expressed in Text A.",
      "expectedType": "text",
      "modelSolution": "Fact: Measurable statistical datum or cited study [1 mark]\nOpinion: Subjective qualitative judgment or forecast [1 mark]",
      "finalBenchmark": "One fact and one opinion identified"
    },
    {
      "num": 4,
      "section": "Text B: Primary Purpose & Stance",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text B: Purpose & Register",
      "scenarioText": "Refer to Text B.",
      "promptText": "What is the overarching rhetorical purpose of Text B?",
      "expectedType": "multiple-choice",
      "options": [
        "A: To evaluate the operational viability and challenges of digital healthcare transformation and remote monitoring",
        "B: To dismiss alternative methodologies as unviable",
        "C: To promote commercial procurement contracts exclusively",
        "D: To entertain general readers with satirical anecdotes"
      ],
      "modelSolution": "Correct Answer: Option A (To evaluate operational viability and challenges) [1 mark]",
      "finalBenchmark": "Option A"
    },
    {
      "num": 5,
      "section": "Text B: Rhetorical & Linguistic Devices",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Persuasive Techniques",
      "scenarioText": "Refer to Text B.",
      "promptText": "Identify two linguistic or stylistic techniques the author uses to engage the target audience.",
      "expectedType": "text",
      "modelSolution": "Any two from: Rhetorical questions / Emotive vocabulary / Triadic phrasing (rule of three) / Expert testimony / Contrastive juxtaposition [1 mark each, max 2]",
      "finalBenchmark": "Two valid linguistic techniques"
    },
    {
      "num": 6,
      "section": "Text B: Implied Meaning",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[2 marks]",
      "scenarioTitle": "Text B: Inference & Nuance",
      "scenarioText": "In Text B, the author notes: 'Innovation cannot succeed in an institutional vacuum.'",
      "promptText": "Explain what the author implies by this statement.",
      "expectedType": "text",
      "modelSolution": "Implies that technical innovation requires supportive regulatory frameworks, political backing, and collaborative infrastructure to be successful [2 marks]",
      "finalBenchmark": "Requires institutional/regulatory support"
    },
    {
      "num": 7,
      "section": "Text B: Organisational Cohesion",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text B: Textual Architecture",
      "scenarioText": "Refer to Text B.",
      "promptText": "Explain how the author employs structural features to present a balanced argument.",
      "expectedType": "text",
      "modelSolution": "Uses comparative subheadings, analytical data tables, and transitional conjunctions to weigh advantages against risks [1-2 marks]",
      "finalBenchmark": "Comparative headings and balanced data"
    },
    {
      "num": 8,
      "section": "Text C: Tone & Register",
      "isCalcAllowed": false,
      "marks": 1,
      "markTags": "[1 mark]",
      "scenarioTitle": "Text C: Tone Analysis",
      "scenarioText": "Refer to the opening paragraph of Text C.",
      "promptText": "Which adjective best characterises the tone of the writer in Text C?",
      "expectedType": "multiple-choice",
      "options": [
        "A: Critically urgent and provocative",
        "B: Indifferent and unconcerned",
        "C: Light-hearted and humorous",
        "D: Solemnly apologetic"
      ],
      "modelSolution": "Correct Answer: Option A (Critically urgent and provocative) [1 mark]",
      "finalBenchmark": "Option A"
    },
    {
      "num": 9,
      "section": "Text C: Evaluating Bias",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[2 marks]",
      "scenarioTitle": "Text C: Bias & Subjectivity",
      "scenarioText": "Refer to Text C.",
      "promptText": "Identify evidence of potential authorial bias in Text C, explaining how emotive language is used to sway opinion.",
      "expectedType": "text",
      "modelSolution": "Identifies loaded/pejorative adjectives ('reckless', 'short-sighted') used to discredit opposing views without acknowledging counter-evidence [2 marks]",
      "finalBenchmark": "Loaded emotive language cited with analysis"
    },
    {
      "num": 10,
      "section": "Text C: Stakeholder Perspectives",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Text C: Contrasting Claims",
      "scenarioText": "Refer to Text C.",
      "promptText": "Identify two distinct stakeholder concerns highlighted by the contributors.",
      "expectedType": "text",
      "modelSolution": "1. Disproportionate financial burden on low-income consumers [1 mark]\n2. Long-term reliability and cybersecurity vulnerabilities [1 mark]",
      "finalBenchmark": "Two stakeholder concerns"
    },
    {
      "num": 11,
      "section": "Synthesis: Text B & Text C",
      "isCalcAllowed": false,
      "marks": 3,
      "markTags": "[3 marks]",
      "scenarioTitle": "Cross-Text Synthesis",
      "scenarioText": "Both Text B and Text C address the transition toward digital healthcare transformation and remote monitoring.",
      "promptText": "Compare how Text B and Text C approach the question of economic cost and feasibility.",
      "expectedType": "text",
      "modelSolution": "Text B argues that initial capital investment yields substantial long-term net savings through efficiency gains [1 mark]. In contrast, Text C highlights the immediate fiscal strain on local budgets and questions whether return on investment is guaranteed [1 mark]. Both agree that targeted subsidies are required to mitigate hardship [1 mark].",
      "finalBenchmark": "Detailed comparative analysis across both texts"
    },
    {
      "num": 12,
      "section": "Cross-Text Analysis",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Evidence Evaluation",
      "scenarioText": "Refer to Text A and Text B.",
      "promptText": "How does the evidence presented in Text A support the recommendations outlined in Text B?",
      "expectedType": "text",
      "modelSolution": "Empirical data and pilot performance figures in Text A substantiate the feasibility claims and practical guidelines asserted in Text B [1-2 marks]",
      "finalBenchmark": "Empirical validation link established"
    },
    {
      "num": 13,
      "section": "Synthesis: All Texts",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[1 mark, 1 mark]",
      "scenarioTitle": "Implicit Assumptions",
      "scenarioText": "Consider the perspectives across all three texts.",
      "promptText": "What underlying assumption is shared by the authors of all three texts?",
      "expectedType": "multiple-choice",
      "options": [
        "A: That continuing with the status quo regarding digital healthcare transformation and remote monitoring is unsustainable",
        "B: That technological change should be halted immediately",
        "C: That central government should fund 100% of all community expenditure",
        "D: That international regulations do not apply to municipal bodies"
      ],
      "modelSolution": "Correct Answer: Option A (Status quo is unsustainable) [1 mark]",
      "finalBenchmark": "Option A"
    },
    {
      "num": 14,
      "section": "Critical Analysis",
      "isCalcAllowed": false,
      "marks": 2,
      "markTags": "[2 marks]",
      "scenarioTitle": "Audience & Register Alignment",
      "scenarioText": "Compare the writing style and target readership of Text A and Text C.",
      "promptText": "Explain how the register and format of each text are tailored to its intended audience.",
      "expectedType": "text",
      "modelSolution": "Text A employs formal, objective academic prose suited for policymakers and analysts [1 mark]. Text C utilises impassioned, direct rhetorical discourse designed to mobilize public civic action [1 mark].",
      "finalBenchmark": "Formal policy vs public civic rhetoric"
    },
    {
      "num": 15,
      "section": "Synthesis: Concluding Synthesis",
      "isCalcAllowed": false,
      "marks": 3,
      "markTags": "[3 marks]",
      "scenarioTitle": "Strategic Recommendations",
      "scenarioText": "Synthesising insights from all three texts.",
      "promptText": "Outline three critical recommendations for leaders seeking to implement digital healthcare transformation and remote monitoring effectively.",
      "expectedType": "text",
      "modelSolution": "1. Prioritise robust physical and digital infrastructure planning [1 mark]\n2. Implement transparent, accessible communication to address public scepticism [1 mark]\n3. Establish inclusive financial safety nets for disadvantaged communities [1 mark]",
      "finalBenchmark": "Three strategic recommendations synthesised"
    }
  ]
}
};

// Helper: Get Paper Object (with rich fallback generator)
function getOrCreatePaper(key) {
  if (MFS_MOCK_DATA[key]) return MFS_MOCK_DATA[key];

  const isWriting = key.includes('writing') || key.includes('english-writing');
  const isReading = key.includes('reading') || key.includes('english-reading');
  const levelName = (key.includes('l2') || key.includes('level-2')) ? 'Level 2' : 'Level 1';
  const isL2 = levelName === 'Level 2';

  // Board detection
  let boardName = 'Pearson Edexcel';
  if (key.includes('city') || key.includes('c-and-g') || key.includes('cg')) {
    boardName = 'City & Guilds';
  } else if (key.includes('open-awards') || key.includes('open') || key.includes('oa')) {
    boardName = 'Open Awards';
  } else if (key.includes('aqa')) {
    boardName = 'AQA';
  } else if (key.includes('ncfe')) {
    boardName = 'NCFE';
  } else if (key.includes('nocn')) {
    boardName = 'NOCN';
  } else if (key.includes('tquk')) {
    boardName = 'TQUK';
  } else if (key.includes('highfield')) {
    boardName = 'Highfield';
  }

  // Paper label detection
  let paperNum = '1';
  let paperLabel = 'Past Paper 1';
  if (key.includes('sample-1') || (key.includes('sample') && !key.includes('sample-2') && !key.includes('sample-3') && !key.includes('sample-4'))) {
    paperNum = 'Sample 1';
    paperLabel = 'Sample Assessment 1';
  } else if (key.includes('sample-2')) {
    paperNum = 'Sample 2';
    paperLabel = 'Sample Assessment 2';
  } else if (key.includes('sample-3')) {
    paperNum = 'Sample 3';
    paperLabel = 'Sample Assessment 3';
  } else if (key.includes('sample-4')) {
    paperNum = 'Sample 4';
    paperLabel = 'Sample Assessment 4';
  } else if (key.includes('practice-1')) {
    paperNum = 'Practice 1';
    paperLabel = 'Practice Paper 1';
  } else if (key.includes('practice-2')) {
    paperNum = 'Practice 2';
    paperLabel = 'Practice Paper 2';
  } else if (key.includes('practice-3')) {
    paperNum = 'Practice 3';
    paperLabel = 'Practice Paper 3';
  } else if (key.includes('specimen')) {
    paperNum = 'Specimen';
    paperLabel = 'Specimen Assessment';
  } else if (key.includes('2020')) {
    paperNum = '2020';
    paperLabel = '2020 Series';
  } else if (key.includes('2023')) {
    paperNum = '2023';
    paperLabel = '2023 Series';
  } else {
    const pm = key.match(/paper-(\d+)/) || key.match(/(\d+)/);
    if (pm) {
      paperNum = pm[1];
      paperLabel = `Past Paper ${pm[1]}`;
    }
  }

  if (isWriting) {
    const isCity = boardName === 'City & Guilds';
    const paperObj = {
      title: `${boardName} Functional Skills English Writing ${levelName} — ${paperLabel}`,
      board: boardName,
      subject: 'writing',
      level: levelName,
      paperNumber: paperNum,
      durationMinutes: isCity ? 80 : 60,
      pdfUrl: '',
      modelSolutionPdf: '',
      videoSolutionSlug: '',
      questions: [
        {
          num: 1,
          section: 'Task 1: Extended Formal Workplace Communication',
          isCalcAllowed: false,
          marks: isCity ? 30 : 21,
          markTags: isCity ? '[18 Composition, 12 SPaG]' : '[12 Composition, 9 SPaG]',
          targetWords: isL2 ? '250 to 300 words' : '200 to 250 words',
          scenarioTitle: `Vocational Policy & Operational Proposal — ${paperLabel}`,
          scenarioText: `Your department manager has requested a detailed formal proposal regarding operational changes and team development for ${boardName} ${levelName} (${paperLabel}).`,
          promptText: `Write an extended formal email or proposal addressing the brief.\nIn your response, you must:\n• Explain the background and justification for the proposed initiative\n• Propose at least two specific practical actions with projected benefits\n• Address potential logistical or financial challenges and solutions\n• Maintain an authoritative, professional register with clear paragraphs and a formal sign-off.`,
          unit: 'words',
          checklist: ['Included professional heading / salutation', 'Detailed clear operational justification', 'Covered all required bullet points', 'Structured into logical paragraphs', 'Checked spelling, capitalization, and punctuation'],
          modelSolution: `Subject: Formal Operational Proposal — ${paperLabel}\n\nDear Department Manager,\n\nI am submitting this formal proposal regarding the operational enhancement project for ${boardName} ${levelName}. Over recent months, our team has identified significant opportunities to streamline departmental workflows, boost staff efficiency, and improve customer satisfaction ratings.\n\nFirstly, introducing modern digital scheduling software will eliminate manual data entry errors and accelerate enquiry turnaround times. Secondly, organising weekly cross-training seminars will ensure team members can provide cover during peak absence periods. While initial software setup requires a modest investment, projected productivity gains will deliver a positive return within six months.\n\nThank you for considering this proposal.\n\nYours sincerely,\nCandidate Representative`,
          finalBenchmark: isL2 ? 'Benchmark: 260 words • Full Level 2 criteria met' : 'Benchmark: 220 words • Full Level 1 criteria met'
        },
        {
          num: 2,
          section: 'Task 2: Web Form / Public Contribution',
          isCalcAllowed: false,
          marks: isCity ? 24 : 15,
          markTags: isCity ? '[14 Composition, 10 SPaG]' : '[9 Composition, 6 SPaG]',
          targetWords: isL2 ? '200 to 250 words' : '150 to 200 words',
          scenarioTitle: `Public Consultation & Service Review — ${paperLabel}`,
          scenarioText: `Complete the official online public feedback and improvement form requested in Task 2 for ${boardName} ${levelName} (${paperLabel}).`,
          promptText: `Complete the formal review form.\nIn your submission, you must:\n• State the specific facility or service used and visit date\n• Evaluate the quality of service, highlighting key strengths\n• Identify areas requiring urgent improvement or remediation\n• Propose constructive solutions for service management.`,
          unit: 'words',
          checklist: ['Identified service and date accurately', 'Balanced positive aspects with constructive critique', 'Offered clear, practical recommendations', 'Checked grammar, syntax, and punctuation'],
          modelSolution: `I am submitting this formal feedback regarding our recent experience with the regional public facilities for ${paperLabel}.\n\nWhile staff were polite and approachable, the digital booking system experienced frequent downtime and accessibility ramps were obstructed. I strongly recommend upgrading the hosting infrastructure and ensuring safety access routes remain clear at all times.\n\nYours faithfully,\nCandidate Representative`,
          finalBenchmark: isL2 ? 'Benchmark: 210 words • Full Level 2 criteria met' : 'Benchmark: 165 words • Full Level 1 criteria met'
        }
      ]
    };
    MFS_MOCK_DATA[key] = paperObj;
    return paperObj;
  } else if (isReading) {
    const isL2Reading = levelName === 'Level 2';
    const sourceTexts = [
      {
        id: 'text-a',
        label: 'Text A: Briefing',
        title: `Text A: Official Briefing & Newsletter — ${paperLabel}`,
        content: `From: Directorate Communications\nTo: All Stakeholders\nSubject: ${boardName} ${levelName} Reading Overview — ${paperLabel}\n\nDear All,\n\nWelcome to the official reading assessment source documentation. This briefing outlines key developments, operational frameworks, and community initiatives for ${boardName} ${levelName} (${paperLabel}).\n\nOver recent months, comprehensive reviews have highlighted the importance of active engagement, reliable information access, and transparent communication across all regional projects.\n\nWe encourage all participants to examine the guidance in Text B and review stakeholder comments in Text C.`
      },
      {
        id: 'text-b',
        label: 'Text B: Guidance',
        title: `Text B: Practical Guidance & Frameworks — ${paperLabel}`,
        content: `Practical Framework & Best Practice: ${paperLabel}\n\nCore Objectives\nBefore commencing activities, review established protocols and safety procedures. Setting structured targets ensures sustainable progress and team cohesion.\n\nKey Recommendations\n• Plan tasks methodically and allocate appropriate time budgets.\n• Ensure all safety and protective equipment meets current standards.\n• Communicate transparently with supervisors and community peers.\n• Monitor progress regularly and record empirical outcomes.\n\nContinuous Review\nRegular evaluation identifies emerging challenges early, allowing teams to adjust strategies proactively.`
      },
      {
        id: 'text-c',
        label: 'Text C: Forum',
        title: `Text C: Community Discussion & Feedback — ${paperLabel}`,
        content: `Stakeholder Online Discussion Forum\n\nContributor 1:\nParticipating in this initiative was extremely worthwhile. Taking small, consistent steps helped our group achieve goals that initially seemed impossible.\n\nContributor 2:\nThe collaborative atmosphere and shared expertise made a huge difference. Having access to knowledgeable coordinators ensured we stayed on track.\n\nContributor 3:\nMy advice to anyone starting out is to maintain patience and focus on quality rather than speed.`
      }
    ];

    const questions = [
      {
        num: 1, section: 'Text A: Key Information Retrieval', isCalcAllowed: false, marks: 2, markTags: '[1 mark, 1 mark]',
        scenarioTitle: 'Text A: Primary Objective', scenarioText: 'Refer to Text A in the Source Booklet.',
        promptText: '(a) According to Text A, what is the main objective of the initiative?\n(b) Which organisational feature helped you locate this answer?',
        expectedType: 'text',
        parts: [
          { id: 'a', label: 'Part (a) Objective', placeholder: 'Main objective identified', unit: '' },
          { id: 'b', label: 'Part (b) Feature', placeholder: 'Organisational feature', unit: '' }
        ],
        modelSolution: '(a) Active engagement and reliable information access [1 mark]\n(b) Opening paragraph / heading / subject line [1 mark]',
        finalBenchmark: 'Objective identified / Heading'
      },
      {
        num: 2, section: 'Text A: Vocabulary & Meaning', isCalcAllowed: false, marks: 1, markTags: '[1 mark]',
        scenarioTitle: 'Text A: Vocabulary in Context', scenarioText: 'Refer to Text A. You may use a dictionary to answer this question.',
        promptText: "Give one word or phrase to replace 'comprehensive' that keeps the meaning the same.",
        expectedType: 'text',
        modelSolution: 'Accept: thorough / complete / wide-ranging / in-depth [1 mark]',
        finalBenchmark: 'thorough / complete'
      },
      {
        num: 3, section: 'Text A: Information Retrieval', isCalcAllowed: false, marks: 2, markTags: '[1 mark, 1 mark]',
        scenarioTitle: 'Text A: Key Priorities', scenarioText: 'Refer to Text A.',
        promptText: 'Identify two priorities emphasized by the Directorate in Text A.',
        expectedType: 'text',
        modelSolution: '1. Transparent communication [1 mark]\n2. Community engagement across regional projects [1 mark]',
        finalBenchmark: 'Two priorities identified'
      },
      {
        num: 4, section: 'Text B: Purpose & Register', isCalcAllowed: false, marks: 1, markTags: '[1 mark]',
        scenarioTitle: 'Text B: Main Purpose', scenarioText: 'Refer to Text B (Practical Guidance).',
        promptText: 'What is the main purpose of Text B?',
        expectedType: 'multiple-choice',
        options: [
          `A: To provide structured guidance and recommendations for ${paperLabel}`,
          'B: To promote commercial products for sale',
          'C: To criticise previous administrative decisions',
          'D: To advertise job vacancies'
        ],
        modelSolution: 'Correct Answer: Option A (To provide structured guidance and recommendations) [1 mark]',
        finalBenchmark: 'Option A'
      },
      {
        num: 5, section: 'Text B: Information Retrieval', isCalcAllowed: false, marks: 2, markTags: '[1 mark, 1 mark]',
        scenarioTitle: 'Text B: Practical Steps', scenarioText: 'Refer to Text B.',
        promptText: 'Identify two practical recommendations given in Text B.',
        expectedType: 'text',
        modelSolution: '1. Plan tasks methodically and allocate time budgets [1 mark]\n2. Ensure safety equipment meets current standards [1 mark]',
        finalBenchmark: 'Two practical steps from Text B'
      },
      {
        num: 6, section: 'Text B: Detail Retrieval', isCalcAllowed: false, marks: 2, markTags: '[1 mark, 1 mark]',
        scenarioTitle: 'Text B: Team Protocols', scenarioText: 'Refer to Text B under Core Objectives.',
        promptText: 'What two things must participants do before commencing activities?',
        expectedType: 'text',
        modelSolution: '1. Review established protocols [1 mark]\n2. Review safety procedures [1 mark]',
        finalBenchmark: 'Review protocols and safety'
      },
      {
        num: 7, section: 'Text B: Organisational Features', isCalcAllowed: false, marks: 1, markTags: '[1 mark]',
        scenarioTitle: 'Text B: Structural Headings', scenarioText: 'Refer to Text B.',
        promptText: 'Which sub-heading in Text B focuses on proactive adjustments and strategy?',
        expectedType: 'text',
        modelSolution: 'Continuous Review [1 mark]',
        finalBenchmark: 'Continuous Review'
      },
      {
        num: 8, section: 'Text B: Formatting Techniques', isCalcAllowed: false, marks: 1, markTags: '[1 mark]',
        scenarioTitle: 'Text B: Bullet Points', scenarioText: 'Refer to Text B.',
        promptText: 'Why does the author use bullet points in Text B?',
        expectedType: 'text',
        modelSolution: 'To present key recommendations in a clear, digestible format that is easy to scan [1 mark]',
        finalBenchmark: 'Clear, digestible format'
      },
      {
        num: 9, section: 'Text C: Stakeholder Views', isCalcAllowed: false, marks: 1, markTags: '[1 mark]',
        scenarioTitle: 'Text C: Contributor 1 Advice', scenarioText: 'Refer to Text C (Forum comments).',
        promptText: 'What helped Contributor 1 achieve goals that initially seemed impossible?',
        expectedType: 'text',
        modelSolution: 'Taking small, consistent steps [1 mark]',
        finalBenchmark: 'Small consistent steps'
      },
      {
        num: 10, section: 'Text C: Contributor Advice', isCalcAllowed: false, marks: 1, markTags: '[1 mark]',
        scenarioTitle: 'Text C: Contributor 3 Tip', scenarioText: 'Refer to Contributor 3 in Text C.',
        promptText: 'What specific advice does Contributor 3 give to newcomers?',
        expectedType: 'text',
        modelSolution: 'Maintain patience and focus on quality rather than speed [1 mark]',
        finalBenchmark: 'Patience / quality over speed'
      },
      {
        num: 11, section: 'Synthesis: Text B & Text C', isCalcAllowed: false, marks: 3, markTags: '[3 marks]',
        scenarioTitle: 'Comparative Synthesis', scenarioText: 'Both Text B and Text C give advice on achieving success.',
        promptText: 'Identify one similarity in the advice given in Text B and Text C, and one difference in how the information is presented.',
        expectedType: 'text',
        modelSolution: 'Similarity: Both recommend steady planning, consistency, and seeking support [1-2 marks].\nDifference: Text B uses formal bulleted guidelines, while Text C uses informal first-person forum comments [1 mark].',
        finalBenchmark: 'Similarity: Consistency/Planning; Difference: Format/Register'
      },
      {
        num: 12, section: 'Text C: Fact vs Opinion', isCalcAllowed: false, marks: 1, markTags: '[1 mark]',
        scenarioTitle: 'Text C: Opinion Identification', scenarioText: 'Refer to Text C.',
        promptText: 'Identify one opinion expressed in Text C.',
        expectedType: 'text',
        modelSolution: "'Participating was extremely worthwhile' or 'Consistency always beats intensity' [1 mark]",
        finalBenchmark: 'Valid opinion cited'
      },
      {
        num: 13, section: 'Cross-Text Analysis', isCalcAllowed: false, marks: 1, markTags: '[1 mark]',
        scenarioTitle: 'Tone & Register Comparison', scenarioText: 'Refer to all three texts.',
        promptText: 'Which text uses the most informal, conversational tone?',
        expectedType: 'multiple-choice',
        options: [
          'A: Text A',
          'B: Text B',
          'C: Text C',
          'D: All texts have identical tone'
        ],
        modelSolution: 'Correct Answer: Option C (Text C uses informal first-person comments) [1 mark]',
        finalBenchmark: 'Option C'
      },
      {
        num: 14, section: 'Cross-Text Evidence', isCalcAllowed: false, marks: 2, markTags: '[1 mark, 1 mark]',
        scenarioTitle: 'Text Evidence Synthesis', scenarioText: 'Refer to Text A and Text B.',
        promptText: 'Give two reasons why following standard frameworks benefits the community.',
        expectedType: 'text',
        modelSolution: '1. Ensures safety and operational compliance [1 mark]\n2. Maintains transparency and public trust [1 mark]',
        finalBenchmark: 'Safety and transparency'
      },
      {
        num: 15, section: 'Synthesis: Overall Assessment', isCalcAllowed: false, marks: 2, markTags: '[1 mark, 1 mark]',
        scenarioTitle: 'Final Synthesis', scenarioText: 'Refer to all three texts.',
        promptText: 'Identify two qualities highlighted across the texts as essential for overcoming challenges.',
        expectedType: 'text',
        modelSolution: '1. Clear communication and collaborative teamwork [1 mark]\n2. Consistency, patience, and adherence to safety protocols [1 mark]',
        finalBenchmark: 'Collaboration and patience'
      }
    ];

    const paperObj = {
      title: `${boardName} Functional Skills English Reading ${levelName} — ${paperLabel}`,
      board: boardName,
      subject: 'reading',
      level: levelName,
      paperNumber: paperNum,
      durationMinutes: isL2Reading ? 75 : 60,
      pdfUrl: '',
      modelSolutionPdf: '',
      videoSolutionSlug: '',
      sourceTexts: sourceTexts,
      questions: questions
    };
    MFS_MOCK_DATA[key] = paperObj;
    return paperObj;
  }

  // Mathematics: Comprehensive Paper Generator for Level 1 & Level 2 across all boards
  const isCity = boardName === 'City & Guilds';
  const isOpenAwards = boardName === 'Open Awards';
  const isAqa = boardName === 'AQA';

  const sec1Name = isAqa ? 'Paper 1: Non-Calculator' : (isCity ? 'Section 1: Non-Calculator' : 'Section A: Non-Calculator');
  const sec2Name = isAqa ? 'Paper 2: Calculator' : (isCity ? 'Section 2: Calculator' : 'Section B: Calculator');

  let sec1Duration = 25;
  let sec2Duration = 90;
  let sec1Marks = 14;
  let sec2Marks = 42;

  if (isCity) {
    sec1Duration = isL2 ? 30 : 25;
    sec2Duration = isL2 ? 110 : 105;
    sec1Marks = 15;
    sec2Marks = 45;
  } else if (isOpenAwards || boardName === 'NCFE' || boardName === 'NOCN' || boardName === 'TQUK' || boardName === 'Highfield') {
    sec1Duration = 30;
    sec2Duration = 90;
    sec1Marks = 15;
    sec2Marks = 45;
  } else if (isAqa) {
    sec1Duration = 30;
    sec2Duration = 90;
    sec1Marks = 20;
    sec2Marks = 60;
  } else {
    sec1Duration = 25;
    sec2Duration = 90;
    sec1Marks = isL2 ? 16 : 14;
    sec2Marks = isL2 ? 48 : 42;
  }

  const sec1Questions = isL2 ? [
    {
      num: 1, section: 'Arithmetic & Negative Numbers', isCalcAllowed: false, marks: 4, markTags: '[M1, A1, M1, A1]',
      scenarioTitle: 'Temperature & Decimal Operations', scenarioText: `Answer Question 1 without using a calculator. Show your method clearly in the space provided.`,
      promptText: '(a) Work out 6.4 × 8.5 without a calculator.\n(b) Work out 5 × 4²', unit: '', expectedType: 'text',
      parts: [
        { id: 'a', label: 'Part (a) 6.4 × 8.5', placeholder: 'e.g. 54.4', unit: '' },
        { id: 'b', label: 'Part (b) 5 × 4²', placeholder: 'e.g. 80', unit: '' }
      ],
      modelSolution: '(a) 6.4 × 8.5 = 54.4 [M1, A1]; (b) 5 × 16 = 80 [M1, A1]',
      finalBenchmark: '54.4 and 80'
    },
    {
      num: 2, section: 'Fractions & Percentages', isCalcAllowed: false, marks: 4, markTags: '[M1, A1, M1, A1]',
      scenarioTitle: 'Mixed Number Operations', scenarioText: 'Calculate fraction operations without a calculator.',
      promptText: 'Work out 2 3/4 + 1 2/3. Give your answer as a mixed number in its simplest form.',
      unit: '', expectedType: 'text',
      modelSolution: '2 3/4 + 1 2/3 = 11/4 + 5/3 = 33/12 + 20/12 = 53/12 = 4 5/12 [M1, A1]',
      finalBenchmark: '4 5/12'
    },
    {
      num: 3, section: 'Area & Compound Shapes', isCalcAllowed: false, marks: 4, markTags: '[M1, A1, M1, A1]',
      scenarioTitle: 'L-Shaped Workshop Floor', scenarioText: 'A workshop floor has an L-shape measuring 8 m along the back, 5 m down one side, 4 m along the inner cut, and 3 m along the remaining side.',
      promptText: 'Calculate the total area in m² of the workshop floor.',
      unit: 'm²', expectedType: 'number',
      modelSolution: 'Split into rectangles: (8 × 3) + (4 × 2) = 24 + 8 = 32 m² (or 40 + 12 = 52 m² depending on orientation) [M1, A1]',
      finalBenchmark: '52 m²'
    },
    {
      num: 4, section: 'Ratios & Scaling', isCalcAllowed: false, marks: 4, markTags: '[M1, A1, M1, A1]',
      scenarioTitle: 'Mortar Mix Proportion', scenarioText: 'A builder mixes cement, sand, and gravel in the ratio 1 : 3 : 6 by weight. The total mix weighs 250 kg.',
      promptText: 'Work out the mass of cement required in kg.',
      unit: 'kg', expectedType: 'number',
      modelSolution: 'Total ratio parts = 1 + 3 + 6 = 10 parts.\n1 part = 250 ÷ 10 = 25 kg.\nCement = 1 × 25 = 25 kg [M1, A1]',
      finalBenchmark: '25 kg'
    }
  ] : [
    {
      num: 1, section: 'Four Operations & Place Value', isCalcAllowed: false, marks: 3, markTags: '[M1, A1, B1]',
      scenarioTitle: 'Warehouse Inventory Intake', scenarioText: 'A logistics supervisor checks three incoming shipments of component boxes: 324 boxes on Monday, 189 boxes on Tuesday, and 65 boxes returned on Wednesday.',
      promptText: 'Work out the net total number of component boxes in stock (324 + 189 - 65) without a calculator.',
      unit: 'boxes', expectedType: 'number',
      modelSolution: '324 + 189 = 513 boxes [M1]; 513 - 65 = 448 boxes [A1, B1]',
      finalBenchmark: '448 boxes'
    },
    {
      num: 2, section: 'Money & Decimals Arithmetic', isCalcAllowed: false, marks: 4, markTags: '[M1, A1, M1, A1]',
      scenarioTitle: 'Workplace Supplies Order', scenarioText: 'An office administrator buys 6 printer ink packs costing £4.50 each. A discount voucher reduces the bill by £7.25.',
      promptText: 'Work out the total amount paid after the discount voucher is applied.',
      unit: '£', expectedType: 'number',
      modelSolution: '6 × £4.50 = £27.00 [M1, A1]; £27.00 - £7.25 = £19.75 [M1, A1]',
      finalBenchmark: '£19.75'
    },
    {
      num: 3, section: 'Fractions & Percentages of Amounts', isCalcAllowed: false, marks: 3, markTags: '[M1, A1, B1]',
      scenarioTitle: 'Departmental Budget Allocation', scenarioText: 'A facilities team has a discretionary maintenance fund of £480. 25% of this fund is earmarked for safety equipment.',
      promptText: 'Work out 25% of £480 without a calculator.',
      unit: '£', expectedType: 'number',
      modelSolution: '25% = 1/4; £480 ÷ 4 = £120 [M1, A1, B1]',
      finalBenchmark: '£120'
    },
    {
      num: 4, section: 'Perimeter & Simple Shapes', isCalcAllowed: false, marks: 4, markTags: '[M1, A1, M1, A1]',
      scenarioTitle: 'Fencing a Rectangular Yard', scenarioText: 'A storage compound yard is rectangular, measuring 14 metres long and 8 metres wide. Fencing wire costs £3 per metre.',
      promptText: '(a) Work out the total perimeter of the yard in metres.\n(b) Work out the total cost to fence the full perimeter.',
      unit: '', expectedType: 'text',
      parts: [
        { id: 'a', label: 'Perimeter (m)', placeholder: 'e.g. 44', unit: 'm' },
        { id: 'b', label: 'Total Cost (£)', placeholder: 'e.g. 132', unit: '£' }
      ],
      modelSolution: '(a) Perimeter = 2 × (14 + 8) = 44 m [M1, A1]; (b) Cost = 44 × £3 = £132 [M1, A1]',
      finalBenchmark: '44 m and £132'
    }
  ];

  const sec2Questions = isL2 ? [
    {
      num: 1, section: 'Percentage Depreciation & Compound Interest', isCalcAllowed: true, marks: 4, markTags: '[M1, M1, A1, B1]',
      scenarioTitle: 'Machinery Depreciation', scenarioText: 'A commercial printing unit was purchased for £12,000. It depreciates by 12% each year.',
      promptText: 'Work out the value of the machinery after 2 years. Give your answer to 2 decimal places.',
      unit: '£', expectedType: 'number',
      modelSolution: 'Year 1: £12,000 × 0.88 = £10,560 [M1]; Year 2: £10,560 × 0.88 = £9,292.80 [M1, A1, B1]',
      finalBenchmark: '£9,292.80'
    },
    {
      num: 2, section: '3D Geometry: Cylinder Volume', isCalcAllowed: true, marks: 5, markTags: '[M1, M1, A1, B1, B1]',
      scenarioTitle: 'Cylindrical Rainwater Tank', scenarioText: 'A cylindrical storage container has radius r = 1.2 m and height h = 2.5 m. Formula: Volume = π × r² × h. Use π = 3.142. Note: 1 m³ = 1000 litres.',
      promptText: '(a) Work out the volume of the cylinder in m³ to 2 decimal places.\n(b) Convert the volume to litres.',
      unit: '', expectedType: 'text',
      parts: [
        { id: 'a', label: 'Volume (m³)', placeholder: 'e.g. 11.31', unit: 'm³' },
        { id: 'b', label: 'Capacity (litres)', placeholder: 'e.g. 11310', unit: 'litres' }
      ],
      modelSolution: '(a) V = 3.142 × 1.2² × 2.5 = 11.3112 m³ ≈ 11.31 m³ [M1, A1]; (b) Litres = 11.3112 × 1000 = 11,311 litres [M1, A1, B1]',
      finalBenchmark: '11.31 m³ and 11,311 litres'
    },
    {
      num: 3, section: 'Reverse Percentages', isCalcAllowed: true, marks: 4, markTags: '[M1, M1, A1, B1]',
      scenarioTitle: 'Pre-VAT Commercial Invoice', scenarioText: 'The total bill for an electrical installation including VAT at 20% is £1,584.',
      promptText: 'Work out the original cost of the installation before VAT was added.',
      unit: '£', expectedType: 'number',
      modelSolution: '120% = £1,584; 1% = £1,584 ÷ 120 = £13.20; 100% = £13.20 × 100 = £1,320 [M1, M1, A1, B1]',
      finalBenchmark: '£1,320'
    },
    {
      num: 4, section: 'Statistics: Grouped Frequency Mean', isCalcAllowed: true, marks: 6, markTags: '[M1, M1, M1, A1, B1, B1]',
      scenarioTitle: 'Customer Wait Times Survey', scenarioText: 'The table shows customer wait times (minutes): 0 < t ≤ 10 (freq 8), 10 < t ≤ 20 (freq 14), 20 < t ≤ 30 (freq 18), 30 < t ≤ 40 (freq 10).',
      promptText: 'Calculate an estimate for the mean customer wait time in minutes to 1 decimal place.',
      unit: 'mins', expectedType: 'number',
      modelSolution: 'Midpoints: 5, 15, 25, 35. fx: (5×8) + (15×14) + (25×18) + (35×10) = 40 + 210 + 450 + 350 = 1050 [M1, M1]. Total freq = 50. Mean = 1050 ÷ 50 = 21.0 mins [M1, A1, B1]',
      finalBenchmark: '21.0 mins'
    },
    {
      num: 5, section: 'Scatter Diagrams & Correlation', isCalcAllowed: true, marks: 4, markTags: '[M1, A1, B1, B1]',
      scenarioTitle: 'Delivery Times vs Mileage', scenarioText: 'A courier analyzes delivery distance (miles) against transit duration (hours). The data shows strong positive linear correlation.',
      promptText: 'If a delivery route is 85 miles and the line of best fit has equation Duration = (Distance ÷ 40) + 0.5 hours, estimate the transit duration in hours.',
      unit: 'hours', expectedType: 'number',
      modelSolution: 'Duration = (85 ÷ 40) + 0.5 = 2.125 + 0.5 = 2.625 hours (or 2 hours 37.5 mins) [M1, A1, B1]',
      finalBenchmark: '2.625 hours'
    },
    {
      num: 6, section: 'Proportion & Best Value', isCalcAllowed: true, marks: 5, markTags: '[M1, M1, A1, B1, B1]',
      scenarioTitle: 'Industrial Cleaning Fluid Comparison', scenarioText: 'Supplier A sells a 5-litre drum of cleaning fluid for £28.50. Supplier B sells a 12-litre drum of identical fluid for £64.80.',
      promptText: '(a) Work out the price per litre for Supplier A.\n(b) Work out the price per litre for Supplier B.\n(c) State which supplier offers the best value for money.',
      unit: '', expectedType: 'text',
      parts: [
        { id: 'a', label: 'Supplier A (£/litre)', placeholder: 'e.g. 5.70', unit: '£' },
        { id: 'b', label: 'Supplier B (£/litre)', placeholder: 'e.g. 5.40', unit: '£' },
        { id: 'c', label: 'Best Value', placeholder: 'Supplier A or Supplier B', unit: '' }
      ],
      modelSolution: 'Supplier A: £28.50 ÷ 5 = £5.70/L [M1, A1]; Supplier B: £64.80 ÷ 12 = £5.40/L [M1, A1]; Best value is Supplier B [B1]',
      finalBenchmark: '£5.70, £5.40, Supplier B'
    },
    {
      num: 7, section: 'Scale Drawings & Space Planning', isCalcAllowed: true, marks: 5, markTags: '[M1, M1, A1, B1, B1]',
      scenarioTitle: 'Conference Room Layout', scenarioText: 'A conference room is 9 m long and 6 m wide. A scale drawing is drawn where 1 cm represents 0.75 m. An executive desk measuring 3 m by 1.5 m is placed with at least 1.5 m clearance all around.',
      promptText: '(a) Work out the length in cm of the room on the scale drawing.\n(b) Work out the minimum room length required for the desk and clearances.',
      unit: '', expectedType: 'text',
      parts: [
        { id: 'a', label: 'Drawing Length (cm)', placeholder: 'e.g. 12', unit: 'cm' },
        { id: 'b', label: 'Required Length (m)', placeholder: 'e.g. 6.0', unit: 'm' }
      ],
      modelSolution: '(a) 9 ÷ 0.75 = 12 cm [M1, A1]; (b) 3 m + 1.5 m + 1.5 m = 6.0 m [M1, A1, B1]',
      finalBenchmark: '12 cm and 6.0 m'
    },
    {
      num: 8, section: 'Combined Probability', isCalcAllowed: true, marks: 5, markTags: '[M1, M1, A1, B1, B1]',
      scenarioTitle: 'Quality Control Testing', scenarioText: 'A factory machine produces precision bolts. The probability that a bolt has a dimension defect is 0.05. Two bolts are chosen at random.',
      promptText: 'Work out the probability that neither bolt has a dimension defect.',
      unit: '', expectedType: 'number',
      modelSolution: 'P(no defect) = 1 - 0.05 = 0.95. P(both no defect) = 0.95 × 0.95 = 0.9025 [M1, M1, A1, B1, B1]',
      finalBenchmark: '0.9025'
    }
  ] : [
    {
      num: 1, section: 'Four Operations & Place Value', isCalcAllowed: false, marks: 3, markTags: '[M1, A1, B1]',
      scenarioTitle: 'Warehouse Inventory Intake', scenarioText: 'A logistics supervisor checks three incoming shipments of component boxes: 324 boxes on Monday, 189 boxes on Tuesday, and 65 boxes returned on Wednesday.',
      promptText: 'Work out the net total number of component boxes in stock (324 + 189 - 65) without a calculator.',
      unit: 'boxes', expectedType: 'number',
      modelSolution: '324 + 189 = 513 boxes [M1]; 513 - 65 = 448 boxes [A1, B1]',
      finalBenchmark: '448 boxes'
    },
    {
      num: 2, section: 'Money & Decimals Arithmetic', isCalcAllowed: false, marks: 4, markTags: '[M1, A1, M1, A1]',
      scenarioTitle: 'Workplace Supplies Order', scenarioText: 'An office administrator buys 6 printer ink packs costing £4.50 each. A discount voucher reduces the bill by £7.25.',
      promptText: 'Work out the total amount paid after the discount voucher is applied.',
      unit: '£', expectedType: 'number',
      modelSolution: '6 × £4.50 = £27.00 [M1, A1]; £27.00 - £7.25 = £19.75 [M1, A1]',
      finalBenchmark: '£19.75'
    },
    {
      num: 3, section: 'Fractions & Percentages of Amounts', isCalcAllowed: false, marks: 3, markTags: '[M1, A1, B1]',
      scenarioTitle: 'Departmental Budget Allocation', scenarioText: 'A facilities team has a discretionary maintenance fund of £480. 25% of this fund is earmarked for safety equipment.',
      promptText: 'Work out 25% of £480 without a calculator.',
      unit: '£', expectedType: 'number',
      modelSolution: '25% = 1/4; £480 ÷ 4 = £120 [M1, A1, B1]',
      finalBenchmark: '£120'
    },
    {
      num: 4, section: 'Perimeter & Simple Shapes', isCalcAllowed: false, marks: 4, markTags: '[M1, A1, M1, A1]',
      scenarioTitle: 'Fencing a Rectangular Yard', scenarioText: 'A storage compound yard is rectangular, measuring 14 metres long and 8 metres wide. Fencing wire costs £3 per metre.',
      promptText: '(a) Work out the total perimeter of the yard in metres.\n(b) Work out the total cost to fence the full perimeter.',
      unit: '', expectedType: 'text',
      parts: [
        { id: 'a', label: 'Perimeter (m)', placeholder: 'e.g. 44', unit: 'm' },
        { id: 'b', label: 'Total Cost (£)', placeholder: 'e.g. 132', unit: '£' }
      ],
      modelSolution: '(a) Perimeter = 2 × (14 + 8) = 44 m [M1, A1]; (b) Cost = 44 × £3 = £132 [M1, A1]',
      finalBenchmark: '44 m and £132'
    }
  ];

  const paperObj = {
    title: `${boardName} Functional Skills Mathematics ${levelName} — ${paperLabel}`,
    board: boardName,
    subject: 'maths',
    level: levelName,
    paperNumber: paperNum,
    durationMinutes: sec1Duration + sec2Duration,
    pdfUrl: '',
    modelSolutionPdf: '',
    videoSolutionSlug: '',
    sections: [
      {
        id: 'A',
        name: sec1Name,
        code: `${boardName.substring(0,3).toUpperCase()}MAT${isL2 ? '2' : '1'}/N01`,
        durationMinutes: sec1Duration,
        totalMarks: sec1Marks,
        isCalcAllowed: false,
        questions: sec1Questions
      },
      {
        id: 'B',
        name: sec2Name,
        code: `${boardName.substring(0,3).toUpperCase()}MAT${isL2 ? '2' : '1'}/C01`,
        durationMinutes: sec2Duration,
        totalMarks: sec2Marks,
        isCalcAllowed: true,
        questions: sec2Questions
      }
    ]
  };
  MFS_MOCK_DATA[key] = paperObj;
  return paperObj;
}

function getPaperSections(paper) {
  if (paper.sections && Array.isArray(paper.sections) && paper.sections.length > 0) {
    return paper.sections;
  }
  return [
    {
      id: 'A',
      name: paper.title || 'Examination Questions',
      code: paper.subject === 'writing' ? 'PENG/W01' : (paper.subject === 'reading' ? 'PENG/R01' : 'PMAT/01'),
      durationMinutes: paper.durationMinutes || 60,
      totalMarks: (paper.questions || []).reduce((acc, q) => acc + (q.marks || 0), 0),
      isCalcAllowed: false,
      questions: paper.questions || []
    }
  ];
}

function getSavedSectionTimer(paperKey, secId, defaultMins) {
  const saved = localStorage.getItem(`mfs_sim_${paperKey}_sec_${secId}_timer`);
  if (saved !== null) {
    const val = parseInt(saved, 10);
    if (!isNaN(val) && val >= 0) return val;
  }
  return defaultMins * 60;
}

function saveCurrentSectionTimer() {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const sections = getPaperSections(paper);
  const sec = sections[simCurrentSectionIndex];
  if (sec) {
    localStorage.setItem(`mfs_sim_${simCurrentPaperKey}_sec_${sec.id}_timer`, simTimerSeconds);
  }
}

// Initialise Simulator from Query Parameters or Default
document.addEventListener('DOMContentLoaded', () => {
  const urlParams = new URLSearchParams(window.location.search);
  const board = (urlParams.get('board') || 'edexcel').toLowerCase();
  const subject = (urlParams.get('subject') || 'maths').toLowerCase();
  const level = (urlParams.get('level') || 'l1').toLowerCase();
  const paper = (urlParams.get('paper') || '1').toLowerCase();

  // If Digital Functional Skills requested, redirect to dedicated player
  if (subject === 'digital' || board === 'dfs' || urlParams.get('paper') === 'dfs-mock') {
    window.location.href = 'digital-functional-skills-mock-exam.html';
    return;
  }

  let key = `${board}-${subject}-${level}-paper-${paper}`;
  if (paper.startsWith('practice') || paper.startsWith('sample') || paper.includes('-') || paper.includes('specimen')) {
    key = `${board}-${subject}-${level}-${paper}`;
  }

  // Normalise subject alias
  if (subject === 'english' || subject === 'writing' || subject.includes('writing')) {
    key = `${board}-english-writing-${level}-paper-${paper}`;
    if (paper.startsWith('practice') || paper.startsWith('sample') || paper.includes('-') || paper.includes('specimen')) {
      key = `${board}-english-writing-${level}-${paper}`;
    }
  } else if (subject === 'reading' || subject.includes('reading')) {
    key = `${board}-english-reading-${level}-paper-${paper}`;
    if (paper.startsWith('practice') || paper.startsWith('sample') || paper.includes('-') || paper.includes('specimen')) {
      key = `${board}-english-reading-${level}-${paper}`;
    }
  }

  simCurrentPaperKey = key;

  // Sync Dropdown
  const selector = document.getElementById('simPaperSelector');
  if (selector) {
    let found = false;
    for (let i = 0; i < selector.options.length; i++) {
      if (selector.options[i].value === simCurrentPaperKey) {
        selector.selectedIndex = i;
        found = true;
        break;
      }
    }
    if (!found) {
      const opt = document.createElement('option');
      opt.value = simCurrentPaperKey;
      opt.text = `${board.toUpperCase()} ${subject.toUpperCase()} ${level.toUpperCase()} Paper ${paper}`;
      opt.selected = true;
      selector.add(opt);
    }
  }

  loadPaper(simCurrentPaperKey);
  startTimer();
  initSimFontSize();
  setupModalBackdropDismiss();
});

// Load and Render Paper
function loadPaper(paperKey) {
  simCurrentPaperKey = paperKey;
  simStartedSections = {};
  sim5MinWarningShown = {};
  simLockedSections = {};
  const paper = getOrCreatePaper(paperKey);
  const sections = getPaperSections(paper);
  sections.forEach((s) => {
    if (localStorage.getItem(`mfs_sim_${paperKey}_sec_${s.id}_locked`) === 'true') {
      simLockedSections[s.id] = true;
    }
  });

  simCurrentSectionIndex = 0;
  simCurrentQuestionIndex = 0; // Front cover of Section A (start of exam)

  // Header Title
  const titleDisplay = document.getElementById('simPaperTitleDisplay');
  if (titleDisplay) titleDisplay.innerText = paper.title;

  // Set Timer based on first section
  const firstSec = sections[0];
  simTimerSeconds = getSavedSectionTimer(simCurrentPaperKey, firstSec.id, firstSec.durationMinutes);
  updateTimerDisplay();

  // Render section switcher tabs
  renderSectionTabs(paper);

  // Render question pills
  renderQuestionPills(paper);

  // Render front cover page
  renderCurrentQuestion();
}

function handlePaperChange(newKey) {
  if (newKey === 'dfs-mock') {
    window.location.href = 'digital-functional-skills-mock-exam.html';
    return;
  }
  loadPaper(newKey);
}

// Section Locking & Verification Helpers
function isSectionLocked(secId) {
  if (!secId) return false;
  if (simLockedSections[secId]) return true;
  const saved = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_sec_${secId}_locked`);
  if (saved === 'true') {
    simLockedSections[secId] = true;
    return true;
  }
  return false;
}

function lockSection(secId) {
  if (!secId) return;
  simLockedSections[secId] = true;
  localStorage.setItem(`mfs_sim_${simCurrentPaperKey}_sec_${secId}_locked`, 'true');
  const paper = getOrCreatePaper(simCurrentPaperKey);
  renderSectionTabs(paper);
}

function promptSectionLock(actionCallback, targetSec = null) {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  // Strictly Maths only! English papers (Writing & Reading) have NO section locks
  if (paper.subject !== 'maths') {
    if (typeof actionCallback === 'function') actionCallback();
    return;
  }

  const sections = getPaperSections(paper);
  const currentSec = targetSec || sections[simCurrentSectionIndex];

  // If section already locked, proceed directly
  if (!currentSec || isSectionLocked(currentSec.id)) {
    if (typeof actionCallback === 'function') actionCallback();
    return;
  }

  const modal = document.getElementById('simSectionLockModal');
  const titleEl = document.getElementById('simLockModalTitle');
  const msgEl = document.getElementById('simLockModalMessage');

  if (currentSec.isCalcAllowed) {
    if (titleEl) titleEl.innerHTML = '<i class="fa-solid fa-calculator" style="color:var(--sim-sky);"></i> End of Calculator Section';
    if (msgEl) msgEl.innerText = 'This will be the end of the calculator section and you cannot return.';
  } else {
    if (titleEl) titleEl.innerHTML = '<i class="fa-solid fa-ban" style="color:#ef4444;"></i> End of Non-Calculator Section';
    if (msgEl) msgEl.innerText = `This will be the end of ${currentSec.name} and you cannot return once you proceed.`;
  }

  simPendingLockAction = () => {
    lockSection(currentSec.id);
    if (typeof actionCallback === 'function') actionCallback();
  };

  if (modal) {
    modal.setAttribute('tabindex', '-1');
    modal.classList.add('open');
    try { modal.focus(); } catch (err) {}
  }
}


function cancelSectionLock() {
  const modal = document.getElementById('simSectionLockModal');
  if (modal) modal.classList.remove('open');
  simPendingLockAction = null;
}

function confirmSectionLock() {
  const modal = document.getElementById('simSectionLockModal');
  if (modal) modal.classList.remove('open');
  if (typeof simPendingLockAction === 'function') {
    const action = simPendingLockAction;
    simPendingLockAction = null;
    action();
  }
}

// Reset Whole Paper Functionality (Prompt, Modal, and Execution)
function promptResetPaper() {
  const modal = document.getElementById('simResetConfirmModal');
  if (modal) {
    modal.setAttribute('tabindex', '-1');
    modal.classList.add('open');
    try { modal.focus(); } catch (err) {}
  } else if (confirm('Are you sure you want to reset this whole paper? All your recorded working, concluded answers, section locks, and timer progress will be cleared so you can re-attempt the exam fresh.')) {
    confirmResetPaper();
  }
}

function closeResetModal() {
  const modal = document.getElementById('simResetConfirmModal');
  if (modal) modal.classList.remove('open');
}

function confirmResetPaper() {
  closeResetModal();
  resetWholePaper();
}

function resetWholePaper() {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const prefix = `mfs_sim_${simCurrentPaperKey}_`;
  const keysToRemove = [];
  for (let i = 0; i < localStorage.length; i++) {
    const k = localStorage.key(i);
    if (k && k.startsWith(prefix)) {
      keysToRemove.push(k);
    }
  }
  keysToRemove.forEach(k => localStorage.removeItem(k));

  // Reset in-memory tracking states
  simLockedSections = {};
  sim5MinWarningShown = {};
  dismiss5MinWarning();

  // Close any open modals
  closeCandidateAnswersModal();
  closeSubmitModal();
  cancelSectionLock();
  closeResetModal();

  // Reset question and section index to start of paper (Cover)
  simCurrentSectionIndex = 0;
  simCurrentQuestionIndex = 0;

  // Reset timer to original duration for Section A
  const sections = getPaperSections(paper);
  const firstSec = sections[0];
  if (firstSec) {
    simTimerSeconds = (firstSec.durationMinutes || 25) * 60;
  }
  simTimerActive = true;
  updateTimerDisplay();

  // Reset calculator expression and state
  calcClear();

  // Re-render simulator UI components
  renderSectionTabs(paper);
  renderQuestionPills(paper);
  renderCurrentQuestion();
  scrollContentToTop();

  // Status indicator feedback
  const saveStatus = document.getElementById('simSaveStatus');
  if (saveStatus) {
    saveStatus.innerHTML = '<i class="fa-solid fa-rotate-left" style="font-size:0.6rem; color:#38bdf8;"></i> Paper Reset Fresh';
    setTimeout(() => {
      saveStatus.innerHTML = '<i class="fa-solid fa-circle" style="font-size:0.5rem; color:#86efac;"></i> Autosaved';
    }, 2500);
  }
}

// Modal Backdrop Click Helper
function setupModalBackdropDismiss() {
  ['simCandidateAnswersModal', 'simSubmitModal', 'simSectionLockModal', 'simResetConfirmModal'].forEach((id) => {
    const modal = document.getElementById(id);
    if (modal && !modal._hasBackdropDismiss) {
      modal._hasBackdropDismiss = true;
      modal.addEventListener('click', (e) => {
        if (e.target === modal) {
          if (id === 'simCandidateAnswersModal') closeCandidateAnswersModal();
          else if (id === 'simSubmitModal') closeSubmitModal();
          else if (id === 'simSectionLockModal') cancelSectionLock();
          else if (id === 'simResetConfirmModal') closeResetModal();
        }
      });
    }
  });
}

// Switch Active Section (Section A vs Section B)
// Scroll panes to top without shifting outer page
function scrollContentToTop() {
  const coverContainer = document.getElementById('simCoverContainer');
  const qPane = document.querySelector('.sim-pane-question');
  const wPane = document.querySelector('.sim-pane-working');
  if (coverContainer) coverContainer.scrollTop = 0;
  if (qPane) qPane.scrollTop = 0;
  if (wPane) wPane.scrollTop = 0;
}

function switchSection(targetIndex, forceQuestions = false) {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const sections = getPaperSections(paper);
  if (targetIndex < 0 || targetIndex >= sections.length) return;
  if (targetIndex === simCurrentSectionIndex && !forceQuestions) return;

  const targetSec = sections[targetIndex];
  const currentSec = sections[simCurrentSectionIndex];

  // Prevent entering a section that is already locked
  if (isSectionLocked(targetSec.id)) {
    alert(`This section (${targetSec.name}) is locked. You have completed and left this section, and cannot return.`);
    return;
  }

  // If moving forward from an active section, prompt lock warning
  if (targetIndex > simCurrentSectionIndex && currentSec && !isSectionLocked(currentSec.id)) {
    promptSectionLock(() => {
      performSwitchSection(targetIndex, forceQuestions);
    }, currentSec);
    return;
  }

  performSwitchSection(targetIndex, forceQuestions);
}

function performSwitchSection(targetIndex, forceQuestions = false) {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const sections = getPaperSections(paper);

  // Save outgoing section's timer
  saveCurrentSectionTimer();

  // Switch section
  simCurrentSectionIndex = targetIndex;
  const sec = sections[simCurrentSectionIndex];

  // If section was already started or forceQuestions is true, go directly to question 1
  // Otherwise show the section cover page (start of exam or middle transition)
  if (simStartedSections[sec.id] || forceQuestions) {
    simCurrentQuestionIndex = 1;
  } else {
    simCurrentQuestionIndex = 0;
  }

  // Load timer for new section
  simTimerSeconds = getSavedSectionTimer(simCurrentPaperKey, sec.id, sec.durationMinutes);
  updateTimerDisplay();

  // Re-render UI components
  renderSectionTabs(paper);
  renderQuestionPills(paper);
  renderCurrentQuestion();
  scrollContentToTop();
}

// Start Section Questions from Cover Page (Jump to Question 1)
function startSectionQuestions() {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const sections = getPaperSections(paper);
  const sec = sections[simCurrentSectionIndex] || sections[0];
  simStartedSections[sec.id] = true;
  simCurrentQuestionIndex = 1;
  renderQuestionPills(paper);
  renderCurrentQuestion();
  scrollContentToTop();
}

// Render Section Switcher Tabs Bar
function renderSectionTabs(paper) {
  const container = document.getElementById('simSectionTabsBar');
  if (!container) return;
  const sections = getPaperSections(paper);

  if (sections.length <= 1) {
    container.style.display = 'none';
    container.innerHTML = '';
    return;
  }

  container.style.display = 'flex';
  container.innerHTML = '';

  sections.forEach((sec, idx) => {
    const isLocked = isSectionLocked(sec.id);
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = `sim-sec-tab-btn ${idx === simCurrentSectionIndex ? 'active' : ''} ${isLocked ? 'locked' : ''}`;
    
    const durStr = sec.durationMinutes >= 60 
      ? (sec.durationMinutes === 90 ? '1 hr 30 mins' : `${Math.floor(sec.durationMinutes / 60)} hrs`)
      : `${sec.durationMinutes} mins`;
    const marks = sec.totalMarks || (sec.questions || []).reduce((acc, q) => acc + (q.marks || 0), 0);
    
    // Only display calculator status badges for Maths papers
    const calcBadge = paper.subject === 'maths'
      ? (isLocked
        ? `<span class="sim-sec-badge locked"><i class="fa-solid fa-lock"></i> Locked</span>`
        : (sec.isCalcAllowed 
          ? `<span class="sim-sec-badge calc"><i class="fa-solid fa-calculator"></i> Calculator Allowed</span>`
          : `<span class="sim-sec-badge"><i class="fa-solid fa-ban"></i> Non-Calculator</span>`))
      : '';

    const secTitle = isLocked
      ? sec.name.replace(': Non-Calculator', ': Non-Calc').replace(': Calculator', ': Calc')
      : sec.name;

    btn.innerHTML = `
      <span class="sim-sec-title"><i class="fa-solid ${isLocked ? 'fa-lock' : 'fa-layer-group'}"></i> ${escapeHtml(secTitle)}</span>
      <span style="display:flex; align-items:center; gap:6px; flex-wrap:wrap;">
        <span class="sim-sec-badge"><i class="fa-regular fa-clock"></i> ${durStr}</span>
        <span class="sim-sec-badge">${marks} Marks</span>
        ${calcBadge}
      </span>
    `;

    btn.onclick = () => {
      if (isLocked) {
        alert(`This section (${sec.name}) is locked and cannot be reopened.`);
        return;
      }
      switchSection(idx);
    };
    container.appendChild(btn);
  });
}


function renderQuestionPills(paper) {
  const container = document.getElementById('simPillsContainer');
  if (!container) return;
  container.innerHTML = '';

  const sections = getPaperSections(paper);
  const sec = sections[simCurrentSectionIndex] || sections[0];

  // Pill 0: Cover button (stays at fixed position at start of pills container)
  const coverPill = document.createElement('button');
  coverPill.type = 'button';
  coverPill.className = `sim-q-pill cover ${simCurrentQuestionIndex === 0 ? 'active' : ''}`;
  coverPill.innerHTML = '<i class="fa-solid fa-file-invoice"></i> Cover';
  coverPill.title = `${sec.name} - Front Cover Page`;
  coverPill.onclick = () => jumpToQuestion(0);
  container.appendChild(coverPill);

  // Pills 1..N: Questions
  sec.questions.forEach((q, idx) => {
    const pillIdx = idx + 1;
    const pill = document.createElement('button');
    pill.type = 'button';
    pill.className = `sim-q-pill ${pillIdx === simCurrentQuestionIndex ? 'active' : ''}`;

    if (paper.subject === 'writing') {
      pill.innerText = `Task ${q.num}`;
    } else {
      pill.innerText = `Q${q.num}`;
    }

    // Check saved response in localStorage (scoped by section id)
    const savedWorking = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_sec_${sec.id}_q${q.num}_working`)
      || (sec.id === 'A' ? localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_q${q.num}_working`) : null);
    const savedAns = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_sec_${sec.id}_q${q.num}_ans`)
      || (sec.id === 'A' ? localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_q${q.num}_ans`) : null);

    if ((savedWorking && savedWorking.trim().length > 0) || (savedAns && savedAns.trim().length > 0)) {
      pill.classList.add('answered');
    }

    pill.onclick = () => jumpToQuestion(pillIdx);
    container.appendChild(pill);
  });
}

// Helper to escape HTML safely
function escapeHtml(str) {
  if (str === null || str === undefined) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

// Subparts helper: returns explicit parts or auto-detects (a), (b), (c)
function getQuestionParts(q) {
  if (q.parts && Array.isArray(q.parts) && q.parts.length > 0) {
    return q.parts;
  }
  if (q.promptText && typeof q.promptText === 'string') {
    const matches = [...q.promptText.matchAll(/\(([a-d])\)/g)];
    if (matches.length > 1) {
      const uniqueIds = [...new Set(matches.map(m => m[1]))];
      return uniqueIds.map(id => ({
        id: id,
        label: `Part (${id})`,
        placeholder: `Answer for (${id})`,
        unit: id === 'a' ? (q.unit || '') : ''
      }));
    }
  }
  return null;
}

// Render dynamic final answer input box(es)
function renderFinalAnswerInputs(paper, q, sec) {
  const container = document.getElementById('simFinalAnsContainer');
  const sublabel = document.getElementById('simFinalAnsSublabel');
  if (!container) return;
  container.innerHTML = '';

  const secId = sec ? sec.id : 'A';
  const parts = getQuestionParts(q);
  const qNum = q.num;

  if (parts && parts.length > 0) {
    if (sublabel) sublabel.innerText = `Record your separate answers for each part (${parts.map(p => p.id).join(', ')}) below:`;

    parts.forEach(part => {
      const savedVal = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_sec_${secId}_q${qNum}_ans_${part.id}`)
        || (secId === 'A' ? localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_q${qNum}_ans_${part.id}`) : '')
        || '';
      const row = document.createElement('div');
      row.className = 'sim-subpart-ans-row';
      row.innerHTML = `
        <label class="sim-subpart-label" for="sim_ans_${part.id}">
          <span style="background:#0284c7; color:#ffffff; padding:3px 9px; border-radius:5px; font-size:0.78rem; font-weight:700; letter-spacing:0.3px;">${escapeHtml(part.label)}</span>
        </label>
        <div class="sim-subpart-input-wrap">
          <input type="text" class="sim-final-input" id="sim_ans_${part.id}" value="${escapeHtml(savedVal)}" placeholder="${escapeHtml(part.placeholder || 'Enter answer')}" oninput="handleSubpartAnswerInput('${part.id}', this.value)">
          ${part.unit ? `<span class="sim-unit-badge">${escapeHtml(part.unit)}</span>` : ''}
        </div>
      `;
      container.appendChild(row);
    });
  } else {
    if (sublabel) sublabel.innerText = 'Record your conclusive value below:';
    const savedVal = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_sec_${secId}_q${qNum}_ans`)
      || (secId === 'A' ? localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_q${qNum}_ans`) : '')
      || '';
    const row = document.createElement('div');
    row.style.width = '100%';
    row.innerHTML = `
      <div class="sim-final-ans-input-wrap" style="width:100%;">
        <input type="text" class="sim-final-input" id="simFinalInput" value="${escapeHtml(savedVal)}" placeholder="Enter value" oninput="handleAnswerInput(this.value)">
        <span class="sim-unit-badge" id="simUnitBadge" style="${q.unit ? 'display:inline-flex' : 'display:none'}">${escapeHtml(q.unit || '')}</span>
      </div>
    `;
    container.appendChild(row);
  }
}

// Handler for Candidate Name Input on Cover Page
function handleCandidateNameInput(val) {
  localStorage.setItem('mfs_sim_candidate_name', val);
}

// Render Section Front Cover Sheet
function renderSectionCover() {
  const coverContainer = document.getElementById('simCoverContainer');
  const questionPanes = document.getElementById('simQuestionPanes');
  if (!coverContainer) return;

  if (questionPanes) {
    questionPanes.classList.add('sim-hidden');
    questionPanes.style.setProperty('display', 'none', 'important');
  }
  coverContainer.classList.remove('sim-hidden');
  coverContainer.style.setProperty('display', 'block', 'important');

  const paper = getOrCreatePaper(simCurrentPaperKey);
  const sections = getPaperSections(paper);
  const sec = sections[simCurrentSectionIndex] || sections[0];
  const savedCandidateName = localStorage.getItem('mfs_sim_candidate_name') || '';

  const durStr = sec.durationMinutes >= 60
    ? (sec.durationMinutes === 90 ? '1 hour 30 minutes' : `${Math.floor(sec.durationMinutes / 60)} hours`)
    : `${sec.durationMinutes} minutes`;
  const marks = sec.totalMarks || (sec.questions || []).reduce((acc, q) => acc + (q.marks || 0), 0);

  const isMaths = paper.subject === 'maths';
  const isWriting = paper.subject === 'writing';
  const isReading = paper.subject === 'reading';

  let calcRule = '';
  let equipment = '';

  if (isMaths) {
    equipment = sec.isCalcAllowed 
      ? 'Pen (black or blue ink), HB pencil, eraser, ruler, calculator.' 
      : 'Pen (black or blue ink), HB pencil, eraser, ruler. <em>Calculators prohibited.</em>';
    calcRule = sec.isCalcAllowed
      ? '<strong>A calculator may be used.</strong> You must ensure your calculator meets official examination regulations.'
      : '<strong>You must NOT have a calculator</strong> or access to any calculating aid for this non-calculator section.';
  } else if (isWriting) {
    equipment = 'Pen (black or blue ink). A dictionary or spelling aid may be used.';
    calcRule = '';
  } else if (isReading) {
    equipment = 'Pen (black or blue ink). A dictionary may be used.';
    calcRule = '';
  }

  coverContainer.innerHTML = `
    <div class="sim-cover-sheet">
      <div class="sim-cover-header">
        <div class="sim-cover-top-row">
          <div class="sim-cover-exam-board">
            <i class="fa-solid fa-graduation-cap"></i> ${escapeHtml(paper.board || 'Pearson Edexcel')} Functional Skills
          </div>
          <div class="sim-cover-code-badge">${escapeHtml(sec.code || 'EXAM')}</div>
        </div>
        <h1 class="sim-cover-paper-title">${escapeHtml(paper.title)}</h1>
      </div>

      <div class="sim-cover-section-banner">
        <div class="sim-cover-sec-title">
          <i class="fa-solid fa-file-pen"></i> ${escapeHtml(sec.name)}
        </div>
        <div class="sim-cover-sec-meta">
          <span><i class="fa-regular fa-clock"></i> <strong>Time allowed:</strong> ${durStr}</span>
          <span><i class="fa-solid fa-award"></i> <strong>Total Marks:</strong> ${marks}</span>
        </div>
      </div>

      <div class="sim-cover-body">
        <div class="sim-cover-instructions-card">
          <div class="sim-cover-card-title">
            <i class="fa-solid fa-circle-info" style="color:#0284c7;"></i> Instructions to Candidates
          </div>
          <ul class="sim-cover-list">
            <li><strong>Time allowed:</strong> You have <strong>${durStr}</strong> to complete this paper.</li>
            <li><strong>Total marks:</strong> The total mark for this assessment is <strong>${marks} marks</strong>.</li>
            <li><strong>Equipment:</strong> ${equipment}</li>
            ${calcRule ? `<li><strong>Calculator policy:</strong> ${calcRule}</li>` : ''}
            ${isWriting 
              ? `<li><strong>Answer both tasks:</strong> Complete both Task 1 and Task 2. Marks are awarded for clear organization, appropriate format and tone, audience focus, and accurate spelling, punctuation, and grammar (SPaG).</li>
                 <li><strong>Planning:</strong> You may use the optional planning space to structure your writing. Notes in the planning space are not marked.</li>`
              : (isReading
                ? `<li><strong>Source Booklet:</strong> Refer to the Source Texts (Text A, Text B, Text C) provided in the reading panel for each question.</li>
                   <li><strong>Answer all questions:</strong> Record all answers in the spaces provided. Check your work carefully.</li>`
                : `<li><strong>Show all working:</strong> Marks are awarded for your methods, calculations, and explanations. Record all intermediate working in the spaces provided.</li>`
              )}
            <li><strong>Check your work:</strong> Read each question carefully before you start and check your answers when finished.</li>
          </ul>
        </div>

        <div class="sim-cover-candidate-card">
          <div class="sim-cover-card-title">
            <i class="fa-solid fa-id-card" style="color:#0284c7;"></i> Candidate Details
          </div>
          <div class="sim-candidate-row">
            <span>Candidate Name:</span>
            <input type="text" id="simCandidateNameInput" class="sim-candidate-input" value="${escapeHtml(savedCandidateName)}" placeholder="Enter candidate name..." oninput="handleCandidateNameInput(this.value)">
          </div>
          <div class="sim-candidate-row">
            <span>Centre Name:</span>
            <strong>Master Functional Skills</strong>
          </div>
          <div class="sim-candidate-row">
            <span>Centre Number:</span>
            <strong>MFS-10928</strong>
          </div>
          <div class="sim-candidate-row">
            <span>Candidate Number:</span>
            <strong>Candidate 01</strong>
          </div>
          <div class="sim-candidate-row">
            <span>Examination Questions:</span>
            <strong>${sec.questions.length} ${isWriting ? 'Tasks' : 'Questions'} (1 to ${sec.questions.length})</strong>
          </div>
        </div>
      </div>

      <div class="sim-cover-action-box">
        <button type="button" class="sim-cover-start-btn" onclick="startSectionQuestions()">
          Start Assessment <i class="fa-solid fa-arrow-right"></i>
        </button>
      </div>
    </div>
  `;

  const nameInput = document.getElementById('simCandidateNameInput');
  if (nameInput && !nameInput.value) {
    nameInput.focus();
  }
}


function renderCurrentQuestion() {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const sections = getPaperSections(paper);
  const sec = sections[simCurrentSectionIndex] || sections[0];

  // If question index is 0, render the Front Cover Page
  if (simCurrentQuestionIndex === 0) {
    renderSectionCover();
    return;
  }

  // Otherwise, hide cover completely and show question panes
  const coverContainer = document.getElementById('simCoverContainer');
  const questionPanes = document.getElementById('simQuestionPanes');
  if (coverContainer) {
    coverContainer.classList.add('sim-hidden');
    coverContainer.style.setProperty('display', 'none', 'important');
  }
  if (questionPanes) {
    questionPanes.classList.remove('sim-hidden');
    questionPanes.style.setProperty('display', 'flex', 'important');
  }

  const q = sec.questions[simCurrentQuestionIndex - 1];
  if (!q) return;

  const subject = paper.subject || 'maths';

  // Meta Badges
  const qNumBadge = document.getElementById('simQNumBadge');
  const qSectionTag = document.getElementById('simQSectionTag');
  const qMarksBadge = document.getElementById('simQMarksBadge');

  if (subject === 'writing') {
    if (qNumBadge) qNumBadge.innerText = `Task ${q.num} of ${sec.questions.length}`;
    if (qSectionTag) qSectionTag.innerText = q.section || sec.name;
    if (qMarksBadge) qMarksBadge.innerText = `${q.marks} Marks • ${q.markTags || ''}`;
  } else if (subject === 'reading') {
    if (qNumBadge) qNumBadge.innerText = `Question ${q.num} of ${sec.questions.length}`;
    if (qSectionTag) qSectionTag.innerText = q.section || sec.name;
    if (qMarksBadge) qMarksBadge.innerText = `${q.marks} Mark${q.marks > 1 ? 's' : ''}`;
  } else {
    const secPrefix = sec.name.includes(':') ? sec.name.split(':')[0] : (sec.id === 'B' ? 'Section B' : 'Section A');
    if (qNumBadge) qNumBadge.innerText = `${secPrefix}: Question ${q.num} of ${sec.questions.length}`;
    if (qSectionTag) qSectionTag.innerText = sec.name;
    if (qMarksBadge) qMarksBadge.innerText = `${q.marks} Marks • ${q.markTags || ''}`;
  }

  // Scenario
  const scenTitle = document.getElementById('simScenarioTitle');
  const scenText = document.getElementById('simScenarioText');
  if (scenTitle) scenTitle.innerHTML = `<i class="fa-solid fa-file-circle-check" style="color:var(--sim-blue);"></i> ${escapeHtml(q.scenarioTitle)}`;
  if (scenText) scenText.innerText = q.scenarioText;

  // Prompt
  const promptText = document.getElementById('simPromptText');
  if (promptText) promptText.innerText = q.promptText;

  // Mode Specific UI Adaptations (Calculator visibility, reading sources, etc.)
  adaptUiForSubject(paper, q, sec);

  // Restore User Working (scoped by section)
  const savedWorking = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_sec_${sec.id}_q${q.num}_working`)
    || (sec.id === 'A' ? localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_q${q.num}_working`) : '')
    || '';
  const textarea = document.getElementById('simWorkingTextarea');
  if (textarea) textarea.value = savedWorking;

  // Render Subpart / Final Answer Inputs
  renderFinalAnswerInputs(paper, q, sec);

  // Update Word Counter in Writing Mode
  if (subject === 'writing') {
    updateWordCount(savedWorking, q.targetWords);
  }

  // Restore Flag status
  const flagBtn = document.getElementById('simFlagBtn');
  const isFlagged = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_sec_${sec.id}_q${q.num}_flagged`) === '1';
  if (flagBtn) {
    flagBtn.classList.toggle('flagged', isFlagged);
  }

  // Update Pills active state
  const pills = document.querySelectorAll('.sim-q-pill');
  pills.forEach((p, idx) => {
    p.classList.toggle('active', idx === simCurrentQuestionIndex);
  });

  // Prev / Next button state
  const prevBtn = document.getElementById('simPrevBtn');
  const nextBtn = document.getElementById('simNextBtn');

  if (prevBtn) {
    prevBtn.classList.remove('is-locked-btn');
    if (simCurrentQuestionIndex > 1) {
      prevBtn.disabled = false;
      prevBtn.onclick = () => prevQuestion();
      prevBtn.innerHTML = '<i class="fa-solid fa-arrow-left"></i> Previous';
    } else {
      prevBtn.disabled = false;
      prevBtn.onclick = () => prevQuestion();
      prevBtn.innerHTML = '<i class="fa-solid fa-arrow-left"></i> Cover Page';
    }
  }

  if (nextBtn) {
    if (simCurrentQuestionIndex < sec.questions.length) {
      nextBtn.style.display = 'inline-flex';
      nextBtn.disabled = false;
      nextBtn.onclick = () => nextQuestion();
      nextBtn.innerHTML = 'Next <i class="fa-solid fa-arrow-right"></i>';
      nextBtn.classList.remove('finish');
    } else {
      if (simCurrentSectionIndex < sections.length - 1) {
        const nextSec = sections[simCurrentSectionIndex + 1];
        nextBtn.style.display = 'inline-flex';
        nextBtn.disabled = false;
        nextBtn.onclick = () => nextQuestion();
        nextBtn.innerHTML = `Proceed to ${escapeHtml(nextSec.name)} <i class="fa-solid fa-arrow-right"></i>`;
        nextBtn.classList.remove('finish');
      } else {
        // Last question of last section: Hide nextBtn to prevent duplicate "Finish & Review All" button
        nextBtn.style.display = 'none';
      }
    }
  }
}

// Adapt UI for Subject Modes (Maths vs Writing vs Reading)
function adaptUiForSubject(paper, q, sec) {
  const subject = paper.subject || 'maths';
  const isCalcAllowed = sec ? sec.isCalcAllowed : !!q.isCalcAllowed;
  const canvas = document.getElementById('simQuestionPanes');

  if (canvas) {
    canvas.classList.remove('sim-mode-writing', 'sim-mode-reading', 'sim-mode-maths');
    canvas.classList.add(`sim-mode-${subject}`);
  }

  // Left pane element references
  const leftMetaBar = document.getElementById('simLeftMetaBar');
  const readingSourcePane = document.getElementById('simReadingSourcePane');
  const leftQuestionContent = document.getElementById('simLeftQuestionContent');
  const finalAnsCard = document.getElementById('simFinalAnsCard');

  // Right pane element references
  const readingRightPane = document.getElementById('simReadingRightPane');
  const standardRightPane = document.getElementById('simStandardRightPane');
  const mathToolbar = document.getElementById('simMathToolbar');
  const calcLockedBanner = document.getElementById('simCalcLockedBanner');
  const calcDrawer = document.getElementById('simCalcDrawer');
  const calcDrawerWrap = document.getElementById('simCalcDrawerWrap');

  // Writing specific references
  const planningBox = document.getElementById('simPlanningBox');
  const wordCountBadge = document.getElementById('simWordCountBadge');
  const writingChecklist = document.getElementById('simWritingChecklist');
  const workingTitleText = document.getElementById('simWorkingTitleText');
  const workingTextarea = document.getElementById('simWorkingTextarea');

  if (subject === 'writing') {
    // -----------------------------------------------------------------------
    // WRITING MODE: Left has Task stimulus, Right has Writing Area & Checklist
    // -----------------------------------------------------------------------
    if (leftMetaBar) leftMetaBar.style.display = 'flex';
    if (readingSourcePane) readingSourcePane.style.display = 'none';
    if (leftQuestionContent) leftQuestionContent.style.display = 'flex';
    if (finalAnsCard) finalAnsCard.style.display = 'none';

    if (readingRightPane) readingRightPane.style.display = 'none';
    if (standardRightPane) standardRightPane.style.display = 'flex';

    if (mathToolbar) mathToolbar.style.display = 'none';
    if (calcLockedBanner) calcLockedBanner.style.display = 'none';
    if (calcDrawerWrap) calcDrawerWrap.style.display = 'none';
    if (calcDrawer) calcDrawer.style.display = 'none';

    if (planningBox) planningBox.style.display = 'block';
    if (wordCountBadge) wordCountBadge.style.display = 'inline-flex';
    if (writingChecklist) {
      writingChecklist.style.display = 'block';
      renderChecklist(q.checklist || [], sec);
    }
    if (workingTitleText) workingTitleText.innerText = 'Draft Your Written Response in the Spaces';
    if (workingTextarea) {
      workingTextarea.placeholder = 'Draft your complete written response here... Remember to use an appropriate greeting/salutation, organize into distinct paragraphs, cover all required points, and check your work.';
    }

    const leftFooter = document.getElementById('simLeftFooterAdvice');
    if (leftFooter) {
      leftFooter.innerHTML = '<span><i class="fa-solid fa-feather-pointed" style="color:var(--sim-blue);"></i> Pearson Edexcel Functional Skills English Writing</span><span style="font-weight:700;">Check your work carefully (SPaG)</span>';
    }

    // Restore planning notes (open if user has notes, otherwise collapsed)
    const savedPlan = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_sec_${sec.id}_q${q.num}_planning`) || '';
    const planningTextarea = document.getElementById('simPlanningTextarea');
    const planningIcon = document.getElementById('simPlanningIcon');
    const planningToggleText = document.getElementById('simPlanningToggleText');
    if (planningTextarea) {
      planningTextarea.value = savedPlan;
      if (savedPlan.trim()) {
        planningTextarea.style.display = 'block';
        if (planningIcon) planningIcon.className = 'fa-solid fa-chevron-up';
        if (planningToggleText) planningToggleText.innerHTML = '<i class="fa-solid fa-lightbulb"></i> Optional Planning Notes &amp; Brainstorming (Click to collapse)';
      } else {
        planningTextarea.style.display = 'none';
        if (planningIcon) planningIcon.className = 'fa-solid fa-chevron-down';
        if (planningToggleText) planningToggleText.innerHTML = '<i class="fa-solid fa-lightbulb"></i> Optional Planning Notes &amp; Brainstorming (Click to expand)';
      }
    }

  } else if (subject === 'reading') {
    // -----------------------------------------------------------------------
    // READING MODE: Left has Source Booklet, Right has Question & Answer
    // -----------------------------------------------------------------------
    if (leftMetaBar) leftMetaBar.style.display = 'none';
    if (leftQuestionContent) leftQuestionContent.style.display = 'none';
    if (finalAnsCard) finalAnsCard.style.display = 'none';

    // Auto-detect referenced source text in question title/text
    if (paper.sourceTexts && paper.sourceTexts.length > 0) {
      const qContext = ((q.scenarioTitle || '') + ' ' + (q.scenarioText || '') + ' ' + (q.promptText || '')).toLowerCase();
      if (qContext.includes('text b') && paper.sourceTexts.length > 1) {
        simActiveSourceTextTab = 1;
      } else if (qContext.includes('text c') && paper.sourceTexts.length > 2) {
        simActiveSourceTextTab = 2;
      } else if (qContext.includes('text a')) {
        simActiveSourceTextTab = 0;
      }
    }

    if (readingSourcePane) {
      readingSourcePane.style.display = 'flex';
      renderSourceTabs(paper.sourceTexts || []);
    }

    if (standardRightPane) standardRightPane.style.display = 'none';
    if (readingRightPane) readingRightPane.style.display = 'flex';

    if (mathToolbar) mathToolbar.style.display = 'none';
    if (calcLockedBanner) calcLockedBanner.style.display = 'none';
    if (calcDrawerWrap) calcDrawerWrap.style.display = 'none';
    if (calcDrawer) calcDrawer.style.display = 'none';
    if (planningBox) planningBox.style.display = 'none';
    if (wordCountBadge) wordCountBadge.style.display = 'none';
    if (writingChecklist) writingChecklist.style.display = 'none';

    // Populate Right Pane Reading Meta & Question
    const rqNumBadge = document.getElementById('simReadingQNumBadge');
    const rqSectionTag = document.getElementById('simReadingQSectionTag');
    const rqMarksBadge = document.getElementById('simReadingQMarksBadge');
    const rqFlagBtn = document.getElementById('simReadingFlagBtn');

    if (rqNumBadge) rqNumBadge.innerText = `Question ${q.num} of ${sec.questions.length}`;
    if (rqSectionTag) rqSectionTag.innerText = q.section || 'Reading Comprehension';
    if (rqMarksBadge) rqMarksBadge.innerText = `${q.marks} Mark${q.marks > 1 ? 's' : ''}${q.markTags ? ' • ' + q.markTags : ''}`;

    const isFlagged = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_sec_${sec.id}_q${q.num}_flagged`) === '1';
    if (rqFlagBtn) {
      rqFlagBtn.classList.toggle('flagged', isFlagged);
      rqFlagBtn.innerHTML = isFlagged ? '<i class="fa-solid fa-flag"></i> Flagged' : '<i class="fa-regular fa-flag"></i> Flag Question';
    }

    const rqTitleText = document.getElementById('simReadingQuestionTitleText');
    const rqScenarioText = document.getElementById('simReadingScenarioText');
    const rqPromptText = document.getElementById('simReadingPromptText');

    if (rqTitleText) rqTitleText.innerText = q.scenarioTitle || 'Question Context';
    if (rqScenarioText) {
      rqScenarioText.innerText = q.scenarioText || '';
      rqScenarioText.style.display = q.scenarioText ? 'block' : 'none';
    }
    if (rqPromptText) rqPromptText.innerText = q.promptText || '';

    // Render Candidate Answer UI in Reading Mode
    const mcqWrap = document.getElementById('simReadingMcqContainer');
    const subpartsWrap = document.getElementById('simReadingSubpartsContainer');
    const textWrap = document.getElementById('simReadingTextareaWrap');
    const readingTextarea = document.getElementById('simReadingTextarea');

    if (q.expectedType === 'multiple-choice' && q.options && q.options.length > 0) {
      if (mcqWrap) {
        mcqWrap.style.display = 'flex';
        renderReadingMcqOptions(q.options, q.num, sec);
      }
      if (subpartsWrap) subpartsWrap.style.display = 'none';
      if (textWrap) textWrap.style.display = 'none';
    } else if (q.parts && q.parts.length > 0) {
      if (mcqWrap) mcqWrap.style.display = 'none';
      if (subpartsWrap) {
        subpartsWrap.style.display = 'flex';
        renderReadingSubpartsInputs(q.parts, q.num, sec);
      }
      if (textWrap) textWrap.style.display = 'none';
    } else {
      if (mcqWrap) mcqWrap.style.display = 'none';
      if (subpartsWrap) subpartsWrap.style.display = 'none';
      if (textWrap) {
        textWrap.style.display = 'flex';
        const savedText = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_sec_${sec.id}_q${q.num}_working`)
          || localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_sec_${sec.id}_q${q.num}_ans`)
          || '';
        if (readingTextarea) {
          readingTextarea.value = savedText;
          readingTextarea.placeholder = 'Type your answer, quotation, or explanation here...';
        }
      }
    }

  } else {
    // -----------------------------------------------------------------------
    // MATHS MODE: Left has Scenario & Prompt & Final Ans, Right has Workspace & Calculator
    // -----------------------------------------------------------------------
    if (leftMetaBar) leftMetaBar.style.display = 'flex';
    if (readingSourcePane) readingSourcePane.style.display = 'none';
    if (leftQuestionContent) leftQuestionContent.style.display = 'flex';
    if (finalAnsCard) finalAnsCard.style.display = 'flex';

    if (readingRightPane) readingRightPane.style.display = 'none';
    if (standardRightPane) standardRightPane.style.display = 'flex';

    if (mathToolbar) mathToolbar.style.display = 'flex';
    if (planningBox) planningBox.style.display = 'none';
    if (wordCountBadge) wordCountBadge.style.display = 'none';
    if (writingChecklist) writingChecklist.style.display = 'none';
    if (workingTitleText) workingTitleText.innerText = 'Type Your Working & Calculations in the Spaces';
    if (workingTextarea) {
      workingTextarea.placeholder = 'Type your working steps, calculations, and intermediate methods here...';
    }

    // Calculator Check for Section B vs Section A
    if (isCalcAllowed) {
      if (calcLockedBanner) calcLockedBanner.style.display = 'none';
      if (calcDrawerWrap) {
        calcDrawerWrap.style.display = 'flex';
        calcDrawerWrap.classList.remove('sim-hidden');
      }
      if (calcDrawer) {
        calcDrawer.style.display = 'flex';
        calcDrawer.classList.remove('locked');
      }
    } else {
      if (calcLockedBanner) calcLockedBanner.style.display = 'none';
      if (calcDrawerWrap) {
        calcDrawerWrap.style.display = 'none';
        calcDrawerWrap.classList.add('sim-hidden');
      }
      if (calcDrawer) {
        calcDrawer.style.display = 'none';
        calcDrawer.classList.add('locked');
      }
    }
  }
}

function renderSourceTabs(texts) {
  const tabsContainer = document.getElementById('simSourceTabs');
  const contentCard = document.getElementById('simSourceContentCard');
  if (!tabsContainer || !contentCard) return;

  tabsContainer.innerHTML = '';
  texts.forEach((txt, idx) => {
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = `sim-source-tab-btn ${idx === simActiveSourceTextTab ? 'active' : ''}`;
    btn.innerHTML = `<i class="fa-regular fa-file-lines"></i> ${escapeHtml(txt.label || txt.title)}`;
    btn.onclick = () => {
      simActiveSourceTextTab = idx;
      renderSourceTabs(texts);
    };
    tabsContainer.appendChild(btn);
  });

  const activeText = texts[simActiveSourceTextTab] || texts[0];
  if (activeText) {
    contentCard.innerText = activeText.content;
  }
}

function renderReadingMcqOptions(options, qNum, sec) {
  const container = document.getElementById('simReadingMcqContainer');
  if (!container) return;
  container.innerHTML = '';
  const secId = sec ? sec.id : 'A';
  const savedChoice = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_sec_${secId}_q${qNum}_ans`) || '';

  options.forEach((opt) => {
    const label = document.createElement('label');
    label.className = `sim-mcq-label ${savedChoice === opt ? 'selected' : ''}`;
    label.innerHTML = `
      <input type="radio" name="sim_mcq_reading_q${qNum}" value="${escapeHtml(opt)}" ${savedChoice === opt ? 'checked' : ''} onchange="handleReadingMcqSelect('${escapeHtml(opt)}', ${qNum})">
      <span>${escapeHtml(opt)}</span>
    `;
    container.appendChild(label);
  });
}

function handleReadingMcqSelect(choice, qNum) {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const sections = getPaperSections(paper);
  const sec = sections[simCurrentSectionIndex] || sections[0];
  const secId = sec.id;

  localStorage.setItem(`mfs_sim_${simCurrentPaperKey}_sec_${secId}_q${qNum}_ans`, choice);
  const labels = document.querySelectorAll('#simReadingMcqContainer .sim-mcq-label');
  labels.forEach(l => {
    const radio = l.querySelector('input');
    l.classList.toggle('selected', radio && radio.checked);
  });

  const pills = document.querySelectorAll('.sim-q-pill');
  if (pills[simCurrentQuestionIndex]) {
    pills[simCurrentQuestionIndex].classList.add('answered');
  }

  indicateSaveStatus();
}

function renderReadingSubpartsInputs(parts, qNum, sec) {
  const container = document.getElementById('simReadingSubpartsContainer');
  if (!container) return;
  container.innerHTML = '';
  const secId = sec ? sec.id : 'A';

  parts.forEach(part => {
    const savedVal = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_sec_${secId}_q${qNum}_ans_${part.id}`) || '';
    const row = document.createElement('div');
    row.className = 'sim-subpart-ans-row';
    row.innerHTML = `
      <label class="sim-subpart-label" for="sim_reading_ans_${part.id}">
        <span style="background:#0284c7; color:#ffffff; padding:4px 10px; border-radius:5px; font-size:0.82rem; font-weight:700;">${escapeHtml(part.label)}</span>
      </label>
      <div class="sim-subpart-input-wrap">
        <input type="text" class="sim-final-input" id="sim_reading_ans_${part.id}" value="${escapeHtml(savedVal)}" placeholder="${escapeHtml(part.placeholder || 'Enter answer')}" oninput="handleSubpartAnswerInput('${part.id}', this.value)">
      </div>
    `;
    container.appendChild(row);
  });
}

function handleReadingTextInput(val) {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const sections = getPaperSections(paper);
  const sec = sections[simCurrentSectionIndex] || sections[0];
  const secId = sec.id;
  const qNum = sec.questions[simCurrentQuestionIndex - 1].num;

  localStorage.setItem(`mfs_sim_${simCurrentPaperKey}_sec_${secId}_q${qNum}_working`, val);
  localStorage.setItem(`mfs_sim_${simCurrentPaperKey}_sec_${secId}_q${qNum}_ans`, val);

  const pills = document.querySelectorAll('.sim-q-pill');
  if (pills[simCurrentQuestionIndex]) {
    pills[simCurrentQuestionIndex].classList.toggle('answered', val.trim().length > 0);
  }

  indicateSaveStatus();
}


function renderChecklist(items, sec) {
  const container = document.getElementById('simChecklistItems');
  if (!container) return;
  container.className = 'sim-checklist-grid';
  container.innerHTML = '';

  const paper = getOrCreatePaper(simCurrentPaperKey);
  const sections = getPaperSections(paper);
  const currentSec = sec || sections[simCurrentSectionIndex] || sections[0];
  if (simCurrentQuestionIndex === 0) return;
  const qNum = currentSec.questions[simCurrentQuestionIndex - 1].num;
  const secId = currentSec.id;

  items.forEach((item, idx) => {
    const saved = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_sec_${secId}_q${qNum}_chk_${idx}`) === '1';
    const row = document.createElement('label');
    row.className = 'sim-checklist-item';
    row.innerHTML = `
      <input type="checkbox" ${saved ? 'checked' : ''} onchange="handleChecklistToggle(${idx}, this.checked)">
      <span>${escapeHtml(item)}</span>
    `;
    container.appendChild(row);
  });
}

function handleChecklistToggle(idx, checked) {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const sections = getPaperSections(paper);
  const sec = sections[simCurrentSectionIndex] || sections[0];
  if (simCurrentQuestionIndex === 0) return;
  const qNum = sec.questions[simCurrentQuestionIndex - 1].num;
  localStorage.setItem(`mfs_sim_${simCurrentPaperKey}_sec_${sec.id}_q${qNum}_chk_${idx}`, checked ? '1' : '0');
  indicateSaveStatus();
}

// Word Counter for Writing Mode
function updateWordCount(text, targetNotice) {
  const words = text.trim().split(/\s+/).filter(w => w.length > 0);
  const count = words.length;

  const countNum = document.getElementById('simWordCountNumber');
  const targetLabel = document.getElementById('simWordTargetNotice');
  const badge = document.getElementById('simWordCountBadge');

  if (countNum) countNum.innerText = count;
  if (targetLabel && targetNotice) targetLabel.innerText = `(${targetNotice})`;

  if (badge) {
    badge.classList.remove('in-range', 'under-target', 'over-target');
    if (count === 0) {
      // neutral
    } else if (count >= 180 && count <= 260) {
      badge.classList.add('in-range');
    } else if (count < 180) {
      badge.classList.add('under-target');
    } else {
      badge.classList.add('over-target');
    }
  }
}

// Planning Scratchpad Toggle
function togglePlanningBox() {
  const textarea = document.getElementById('simPlanningTextarea');
  const icon = document.getElementById('simPlanningIcon');
  const toggleText = document.getElementById('simPlanningToggleText');
  if (!textarea) return;

  const isHidden = textarea.style.display === 'none' || getComputedStyle(textarea).display === 'none';
  if (isHidden) {
    textarea.style.display = 'block';
    if (icon) icon.className = 'fa-solid fa-chevron-up';
    if (toggleText) toggleText.innerHTML = '<i class="fa-solid fa-lightbulb"></i> Optional Planning Notes &amp; Brainstorming (Click to collapse)';
  } else {
    textarea.style.display = 'none';
    if (icon) icon.className = 'fa-solid fa-chevron-down';
    if (toggleText) toggleText.innerHTML = '<i class="fa-solid fa-lightbulb"></i> Optional Planning Notes &amp; Brainstorming (Click to expand)';
  }
}

function handlePlanningInput(val) {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const sections = getPaperSections(paper);
  const sec = sections[simCurrentSectionIndex] || sections[0];
  if (simCurrentQuestionIndex === 0) return;
  const qNum = sec.questions[simCurrentQuestionIndex - 1].num;
  localStorage.setItem(`mfs_sim_${simCurrentPaperKey}_sec_${sec.id}_q${qNum}_planning`, val);
  indicateSaveStatus();
}

// Navigation Handlers
function nextQuestion() {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const sections = getPaperSections(paper);
  const sec = sections[simCurrentSectionIndex] || sections[0];

  if (simCurrentQuestionIndex === 0) {
    startSectionQuestions();
    return;
  }

  if (simCurrentQuestionIndex < sec.questions.length) {
    simCurrentQuestionIndex++;
    renderCurrentQuestion();
    scrollContentToTop();
  } else {
    if (simCurrentSectionIndex < sections.length - 1) {
      switchSection(simCurrentSectionIndex + 1);
    } else {
      openSubmitModal();
    }
  }
}

function prevQuestion() {
  if (simCurrentQuestionIndex > 1) {
    simCurrentQuestionIndex--;
    renderCurrentQuestion();
    scrollContentToTop();
  } else if (simCurrentQuestionIndex === 1) {
    simCurrentQuestionIndex = 0; // Return to Cover
    renderCurrentQuestion();
    scrollContentToTop();
  } else if (simCurrentQuestionIndex === 0 && simCurrentSectionIndex > 0) {
    // Go to previous section's last question
    saveCurrentSectionTimer();
    simCurrentSectionIndex--;
    const paper = getOrCreatePaper(simCurrentPaperKey);
    const sections = getPaperSections(paper);
    const prevSec = sections[simCurrentSectionIndex];
    simCurrentQuestionIndex = prevSec.questions.length;
    simTimerSeconds = getSavedSectionTimer(simCurrentPaperKey, prevSec.id, prevSec.durationMinutes);
    updateTimerDisplay();
    renderSectionTabs(paper);
    renderQuestionPills(paper);
    renderCurrentQuestion();
    scrollContentToTop();
  }
}

function jumpToQuestion(index) {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const sections = getPaperSections(paper);
  const sec = sections[simCurrentSectionIndex] || sections[0];

  if (index >= 0 && index <= sec.questions.length) {
    if (index >= 1) {
      simStartedSections[sec.id] = true;
    }
    simCurrentQuestionIndex = index;
    renderCurrentQuestion();
    scrollContentToTop();
  }
}

function renderQuestion(index) {
  jumpToQuestion(index);
}

// Input Handlers
function handleWorkingInput(val) {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const sections = getPaperSections(paper);
  const sec = sections[simCurrentSectionIndex] || sections[0];
  if (simCurrentQuestionIndex === 0) return;
  const q = sec.questions[simCurrentQuestionIndex - 1];
  const qNum = q.num;
  const secId = sec.id;

  localStorage.setItem(`mfs_sim_${simCurrentPaperKey}_sec_${secId}_q${qNum}_working`, val);

  // Update pill answered status
  const pills = document.querySelectorAll('.sim-q-pill');
  const userAns = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_sec_${secId}_q${qNum}_ans`) || '';
  if (pills[simCurrentQuestionIndex]) {
    pills[simCurrentQuestionIndex].classList.toggle('answered', val.trim().length > 0 || userAns.trim().length > 0);
  }

  // Update word counter if writing
  if (paper.subject === 'writing') {
    updateWordCount(val, q.targetWords);
  }

  indicateSaveStatus();
}

function handleAnswerInput(val) {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const sections = getPaperSections(paper);
  const sec = sections[simCurrentSectionIndex] || sections[0];
  if (simCurrentQuestionIndex === 0) return;
  const q = sec.questions[simCurrentQuestionIndex - 1];
  const qNum = q.num;
  const secId = sec.id;

  localStorage.setItem(`mfs_sim_${simCurrentPaperKey}_sec_${secId}_q${qNum}_ans`, val);

  const pills = document.querySelectorAll('.sim-q-pill');
  const userWorking = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_sec_${secId}_q${qNum}_working`) || '';
  if (pills[simCurrentQuestionIndex]) {
    pills[simCurrentQuestionIndex].classList.toggle('answered', val.trim().length > 0 || userWorking.trim().length > 0);
  }

  indicateSaveStatus();
}

function handleSubpartAnswerInput(partId, val) {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const sections = getPaperSections(paper);
  const sec = sections[simCurrentSectionIndex] || sections[0];
  if (simCurrentQuestionIndex === 0) return;
  const q = sec.questions[simCurrentQuestionIndex - 1];
  const qNum = q.num;
  const secId = sec.id;

  localStorage.setItem(`mfs_sim_${simCurrentPaperKey}_sec_${secId}_q${qNum}_ans_${partId}`, val);

  const parts = getQuestionParts(q) || [];
  const fullSummary = parts.map(p => {
    const v = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_sec_${secId}_q${qNum}_ans_${p.id}`) || '';
    return v ? `(${p.id}) ${v}${p.unit ? ' ' + p.unit : ''}` : '';
  }).filter(Boolean).join('  |  ');

  localStorage.setItem(`mfs_sim_${simCurrentPaperKey}_sec_${secId}_q${qNum}_ans`, fullSummary);

  const pills = document.querySelectorAll('.sim-q-pill');
  const userWorking = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_sec_${secId}_q${qNum}_working`) || '';
  if (pills[simCurrentQuestionIndex]) {
    pills[simCurrentQuestionIndex].classList.toggle('answered', fullSummary.trim().length > 0 || userWorking.trim().length > 0);
  }

  indicateSaveStatus();
}

function indicateSaveStatus() {
  const status = document.getElementById('simSaveStatus');
  if (status) {
    status.innerHTML = '<i class="fa-solid fa-arrows-rotate fa-spin" style="font-size:0.5rem; color:#38bdf8;"></i> Saving...';
    setTimeout(() => {
      status.innerHTML = '<i class="fa-solid fa-circle" style="font-size:0.5rem; color:#86efac;"></i> Autosaved';
    }, 400);
  }
}

// Flag Question
function toggleFlag() {
  const btn = document.getElementById('simFlagBtn');
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const sections = getPaperSections(paper);
  const sec = sections[simCurrentSectionIndex] || sections[0];
  if (simCurrentQuestionIndex === 0) return;
  const q = sec.questions[simCurrentQuestionIndex - 1];
  const qNum = q.num;
  const secId = sec.id;

  const isFlagged = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_sec_${secId}_q${qNum}_flagged`) === '1';

  if (isFlagged) {
    localStorage.setItem(`mfs_sim_${simCurrentPaperKey}_sec_${secId}_q${qNum}_flagged`, '0');
    if (btn) btn.classList.remove('flagged');
  } else {
    localStorage.setItem(`mfs_sim_${simCurrentPaperKey}_sec_${secId}_q${qNum}_flagged`, '1');
    if (btn) btn.classList.add('flagged');
  }
}

// Symbol and Template Inserters
function insertSymbol(sym) {
  const textarea = document.getElementById('simWorkingTextarea');
  if (!textarea) return;

  const start = textarea.selectionStart;
  const end = textarea.selectionEnd;
  const text = textarea.value;

  textarea.value = text.substring(0, start) + sym + text.substring(end);
  textarea.selectionStart = textarea.selectionEnd = start + sym.length;
  textarea.focus();
  handleWorkingInput(textarea.value);
}

function insertPlaceValueGrid() {
  const grid =
`+----+----+----+----+----+----+----+
| M  | HTh| TTh| Th | H  | T  | U  |
+----+----+----+----+----+----+----+
|    |    |    |    |    |    |    |
+----+----+----+----+----+----+----+
`;
  insertSymbol('\n' + grid + '\n');
}

function insertFractionTemplate() {
  const frac =
`  [ Numerator   ]
------------------
  [ Denominator ]
`;
  insertSymbol('\n' + frac + '\n');
}

function clearWorkingSpace() {
  if (confirm('Are you sure you want to clear your working for this question?')) {
    const textarea = document.getElementById('simWorkingTextarea');
    if (textarea) {
      textarea.value = '';
      handleWorkingInput('');
    }
  }
}

// Countdown Timer with hours formatting
function startTimer() {
  if (simTimerInterval) clearInterval(simTimerInterval);
  simTimerInterval = setInterval(() => {
    if (simTimerActive && simTimerSeconds > 0) {
      simTimerSeconds--;
      updateTimerDisplay();
      if (simTimerSeconds % 5 === 0) {
        saveCurrentSectionTimer();
      }
    }
  }, 1000);
}

function updateTimerDisplay() {
  const disp = document.getElementById('simTimerDisplay');
  if (!disp) return;

  if (simTimerSeconds >= 3600) {
    const hrs = Math.floor(simTimerSeconds / 3600);
    const mins = Math.floor((simTimerSeconds % 3600) / 60);
    const secs = simTimerSeconds % 60;
    disp.innerText = `${hrs}:${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  } else {
    const mins = Math.floor(simTimerSeconds / 60);
    const secs = simTimerSeconds % 60;
    disp.innerText = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  }

  const timerBox = document.getElementById('simTimerBox');
  if (timerBox) {
    timerBox.classList.toggle('warning', simTimerSeconds < 300);
  }

  // 5-Minute Warning Sign Alert (Fired per section)
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const sections = getPaperSections(paper);
  const sec = sections[simCurrentSectionIndex] || sections[0];
  if (sec && simTimerSeconds <= 300 && simTimerSeconds > 0 && !sim5MinWarningShown[sec.id]) {
    sim5MinWarningShown[sec.id] = true;
    show5MinWarning(sec);
  }
}

function show5MinWarning(sec) {
  const banner = document.getElementById('sim5MinWarningBanner');
  const desc = document.getElementById('sim5MinWarningDesc');
  if (desc && sec) {
    desc.innerText = `There are 5 minutes left to complete ${sec.name}. Please conclude your answers and check your working.`;
  }
  if (banner) {
    banner.style.display = 'block';
  }
}

function dismiss5MinWarning() {
  const banner = document.getElementById('sim5MinWarningBanner');
  if (banner) {
    banner.style.display = 'none';
  }
}

function toggleTimerPause() {
  simTimerActive = !simTimerActive;
  const icon = document.getElementById('simTimerPauseIcon');
  if (icon) {
    icon.className = simTimerActive ? 'fa-solid fa-pause' : 'fa-solid fa-play';
  }
}

// Fullscreen Management with clean Escape handling
function exitFullscreenIfActive() {
  if (document.fullscreenElement || document.webkitFullscreenElement || document.mozFullScreenElement || document.msFullscreenElement) {
    try {
      if (document.exitFullscreen) {
        document.exitFullscreen().catch(err => console.warn('Exit fullscreen err:', err));
      } else if (document.webkitExitFullscreen) {
        document.webkitExitFullscreen();
      } else if (document.mozCancelFullScreen) {
        document.mozCancelFullScreen();
      } else if (document.msExitFullscreen) {
        document.msExitFullscreen();
      }
    } catch (e) {
      console.warn('Exit fullscreen err:', e);
    }
  }
}

function toggleSimFullscreen() {
  const shell = document.getElementById('simAppShell');
  if (!shell) return;
  if (!document.fullscreenElement) {
    if (shell.requestFullscreen) {
      shell.requestFullscreen().catch(err => console.warn('Fullscreen err:', err));
    }
  } else {
    if (document.exitFullscreen) {
      document.exitFullscreen().catch(err => console.warn('Exit fullscreen err:', err));
    }
  }
}

document.addEventListener('fullscreenchange', () => {
  const shell = document.getElementById('simAppShell');
  if (shell) {
    shell.classList.toggle('fullscreen', !!document.fullscreenElement);
    if (!document.fullscreenElement) {
      shell.style.width = '';
      shell.style.maxWidth = '';
      shell.style.margin = '';
    }
  }
  const fsBtn = document.querySelector('[onclick="toggleSimFullscreen()"]');
  if (fsBtn) {
    if (document.fullscreenElement) {
      fsBtn.innerHTML = '<i class="fa-solid fa-compress"></i> <span>Exit Full Screen</span>';
    } else {
      fsBtn.innerHTML = '<i class="fa-solid fa-expand"></i> <span>Fill Screen</span>';
    }
  }
});

// Double-click on empty / non-writing spaces to toggle Full Screen or Normal Screen
document.addEventListener('dblclick', (e) => {
  const shell = document.getElementById('simAppShell');
  if (!shell || !shell.contains(e.target)) return;

  // Never toggle fullscreen if double-clicking inside interactive elements, form fields, text inputs, textareas, buttons, selectors, links, or calculator
  if (e.target.closest('textarea, input, button, select, a, label, .sim-calc-drawer, .sim-calc-keypad, [contenteditable="true"], .sim-sym-btn, .sim-template-btn, .sim-nav-btn, .sim-font-btn, .sim-modal, .sim-modal-content, .sim-candidate-modal')) {
    return;
  }

  // Prevent accidental toggles when double-clicking to select words in question prompts, scenarios, or reading source passages
  const selection = window.getSelection ? window.getSelection().toString().trim() : '';
  if (selection.length > 0 && e.target.closest('.sim-q-prompt-text, #simScenarioText, .sim-source-content-card, #simReadingScenarioText, #simReadingPromptText, p, span, h1, h2, h3, h4')) {
    return;
  }

  toggleSimFullscreen();
});

// Universal Modal Closer & Focus Manager
function closeAllSimModals() {
  let closed = false;
  const modals = [
    { id: 'simCandidateAnswersModal', closeFn: closeCandidateAnswersModal },
    { id: 'simSubmitModal', closeFn: closeSubmitModal },
    { id: 'simSectionLockModal', closeFn: cancelSectionLock },
    { id: 'simResetConfirmModal', closeFn: closeResetModal }
  ];
  for (const m of modals) {
    const el = document.getElementById(m.id);
    if (el && el.classList.contains('open')) {
      m.closeFn();
      closed = true;
    }
  }
  if (closed) {
    try {
      window.focus();
      const shell = document.getElementById('simAppShell');
      if (shell) shell.focus();
      else if (document.body) document.body.focus();
    } catch (e) {}
  }
  return closed;
}
window.closeAllSimModals = closeAllSimModals;

function handleGlobalEscKey(e) {
  const isEsc = e.key === 'Escape' || e.key === 'Esc' || e.keyCode === 27 || e.which === 27;
  if (!isEsc) return;

  if (closeAllSimModals()) {
    e.preventDefault();
    e.stopPropagation();
    if (typeof e.stopImmediatePropagation === 'function') {
      e.stopImmediatePropagation();
    }
    return;
  }

  if (document.fullscreenElement) {
    document.exitFullscreen().catch(() => {});
  }
}

window.addEventListener('keydown', handleGlobalEscKey, true);
document.addEventListener('keydown', handleGlobalEscKey, true);
window.addEventListener('focus', () => {
  const activeModal = document.querySelector('.sim-modal-overlay.open');
  if (activeModal && typeof activeModal.focus === 'function') {
    activeModal.focus();
  }
});

// Dynamic Font Size Resizer (With Smallest / Largest Constraints)
const SIM_FONT_LEVELS = [
  { scale: 1.0, label: '100%' },
  { scale: 1.12, label: '112%' },
  { scale: 1.24, label: '124%' },
  { scale: 1.36, label: '136%' }
];
let simFontLevelIndex = 0;

function changeFontSize(delta) {
  const newIndex = simFontLevelIndex + delta;
  if (newIndex < 0 || newIndex >= SIM_FONT_LEVELS.length) return;
  simFontLevelIndex = newIndex;
  applySimFontSize();
  localStorage.setItem('mfs_sim_font_level', simFontLevelIndex);
}

function applySimFontSize() {
  const shell = document.getElementById('simAppShell');
  const decBtn = document.getElementById('simFontDecBtn');
  const incBtn = document.getElementById('simFontIncBtn');
  const badge = document.getElementById('simFontSizeBadge');

  const current = SIM_FONT_LEVELS[simFontLevelIndex] || SIM_FONT_LEVELS[0];
  if (shell) {
    shell.style.setProperty('--sim-scale', current.scale);
  }
  if (badge) {
    badge.innerText = current.label;
  }
  if (decBtn) {
    decBtn.disabled = simFontLevelIndex === 0;
  }
  if (incBtn) {
    incBtn.disabled = simFontLevelIndex === SIM_FONT_LEVELS.length - 1;
  }
}

function initSimFontSize() {
  const saved = localStorage.getItem('mfs_sim_font_level');
  if (saved !== null) {
    const idx = parseInt(saved, 10);
    if (!isNaN(idx) && idx >= 0 && idx < SIM_FONT_LEVELS.length) {
      simFontLevelIndex = idx;
    }
  }
  applySimFontSize();
}

// Calculator Engine: Live expression display with operations visible until '=' is pressed
function updateCalcDisplay() {
  const exprEl = document.getElementById('simCalcExpr');
  const screenEl = document.getElementById('simCalcScreen');
  if (!screenEl) return;

  if (calcJustEvaluated) {
    if (exprEl) exprEl.innerText = calcExpression + ' =';
    screenEl.innerText = calcResult;
  } else {
    if (exprEl) exprEl.innerText = '';
    screenEl.innerText = calcExpression || '0';
  }
}

function calcDigit(digit) {
  if (calcJustEvaluated) {
    calcExpression = String(digit);
    calcJustEvaluated = false;
  } else {
    if (calcExpression === '0') {
      calcExpression = String(digit);
    } else {
      calcExpression += String(digit);
    }
  }
  updateCalcDisplay();
}

function calcDecimal() {
  if (calcJustEvaluated) {
    calcExpression = '0.';
    calcJustEvaluated = false;
  } else {
    const parts = calcExpression.split(/[\s+−×÷-]+/);
    const lastPart = parts[parts.length - 1];
    if (!lastPart.includes('.')) {
      if (lastPart === '' || calcExpression === '') {
        calcExpression += '0.';
      } else {
        calcExpression += '.';
      }
    }
  }
  updateCalcDisplay();
}

function calcOp(op) {
  if (calcJustEvaluated) {
    calcExpression = calcResult + ' ' + op + ' ';
    calcJustEvaluated = false;
  } else {
    if (calcExpression === '') {
      if (op === '−') {
        calcExpression = '−';
      } else {
        calcExpression = '0 ' + op + ' ';
      }
    } else if (/\s[+−×÷]\s$/.test(calcExpression)) {
      calcExpression = calcExpression.replace(/\s[+−×÷]\s$/, ` ${op} `);
    } else {
      calcExpression += ` ${op} `;
    }
  }
  updateCalcDisplay();
}

function calcCalculate() {
  if (!calcExpression) return;

  let trimmed = calcExpression.trim();
  if (/[+−×÷]$/.test(trimmed)) {
    trimmed = trimmed.replace(/[+−×÷]$/, '').trim();
  }
  if (!trimmed) return;

  const safeStr = trimmed
    .replace(/×/g, '*')
    .replace(/÷/g, '/')
    .replace(/−/g, '-');

  if (!/^[0-9+\-*/. ()]+$/.test(safeStr)) {
    const screenEl = document.getElementById('simCalcScreen');
    if (screenEl) screenEl.innerText = 'Error';
    return;
  }

  try {
    if (/\/\s*0(?!\.)/.test(safeStr)) {
      const screenEl = document.getElementById('simCalcScreen');
      if (screenEl) screenEl.innerText = 'Cannot divide by 0';
      return;
    }
    const evaluated = Function(`'use strict'; return (${safeStr})`)();
    if (typeof evaluated === 'number' && isFinite(evaluated)) {
      const rounded = Math.round(evaluated * 1e10) / 1e10;
      calcResult = String(rounded);
      calcJustEvaluated = true;
      updateCalcDisplay();
    } else {
      const screenEl = document.getElementById('simCalcScreen');
      if (screenEl) screenEl.innerText = 'Error';
    }
  } catch (err) {
    const screenEl = document.getElementById('simCalcScreen');
    if (screenEl) screenEl.innerText = 'Error';
  }
}

function calcClear() {
  calcExpression = '';
  calcResult = '0';
  calcJustEvaluated = false;
  updateCalcDisplay();
}

function calcSqrt() {
  let valToRoot = 0;
  if (calcJustEvaluated) {
    valToRoot = parseFloat(calcResult);
  } else {
    calcCalculate();
    valToRoot = parseFloat(calcResult);
  }

  if (!isNaN(valToRoot) && valToRoot >= 0) {
    const res = Math.round(Math.sqrt(valToRoot) * 1e10) / 1e10;
    calcExpression = `√(${valToRoot})`;
    calcResult = String(res);
    calcJustEvaluated = true;
    updateCalcDisplay();
  } else {
    const screenEl = document.getElementById('simCalcScreen');
    if (screenEl) screenEl.innerText = 'Error';
  }
}

// Download Candidate Answers Handler & Modal
function handleDownloadAnswersClick() {
  exitFullscreenIfActive();
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const sections = getPaperSections(paper);
  const currentSec = sections[simCurrentSectionIndex];

  // If in calculator section and not locked, prompt warning before leaving section
  if (currentSec && currentSec.isCalcAllowed && !isSectionLocked(currentSec.id)) {
    promptSectionLock(() => {
      openCandidateAnswersModal();
    });
  } else {
    openCandidateAnswersModal();
  }
}

function openCandidateAnswersModal() {
  exitFullscreenIfActive();
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const sections = getPaperSections(paper);
  const container = document.getElementById('simCandidateReviewList');
  if (!container) return;
  container.innerHTML = '';

  const subTitle = document.getElementById('simCandidateAnswersSubtitle');
  if (subTitle) {
    subTitle.innerText = `${paper.title} — Recorded Candidate Answers & Working`;
  }

  sections.forEach((sec) => {
    // Section Header
    const secHeader = document.createElement('div');
    secHeader.style.cssText = 'background:#0f172a; color:#ffffff; padding:12px 18px; border-radius:8px; font-weight:800; font-size:1rem; margin:16px 0 10px 0; display:flex; justify-content:space-between; align-items:center; letter-spacing:0.4px; flex-wrap:wrap; gap:8px;';
    const durStr = sec.durationMinutes >= 60 ? (sec.durationMinutes === 90 ? '1 hr 30 mins' : `${Math.floor(sec.durationMinutes / 60)} hrs`) : `${sec.durationMinutes} mins`;
    const marks = sec.totalMarks || (sec.questions || []).reduce((acc, q) => acc + (q.marks || 0), 0);
    secHeader.innerHTML = `
      <span><i class="fa-solid fa-layer-group" style="color:#38bdf8; margin-right:8px;"></i> ${escapeHtml(sec.name)}</span>
      <span style="font-size:0.82rem; font-weight:700; opacity:0.9;">${durStr} &bull; ${marks} Marks &bull; ${sec.isCalcAllowed ? 'Calculator Permitted' : 'Non-Calculator'}</span>
    `;
    container.appendChild(secHeader);

    sec.questions.forEach((q) => {
      const userWorking = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_sec_${sec.id}_q${q.num}_working`)
        || (sec.id === 'A' ? localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_q${q.num}_working`) : null)
        || '(No response recorded)';
      const userAns = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_sec_${sec.id}_q${q.num}_ans`)
        || (sec.id === 'A' ? localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_q${q.num}_ans`) : null)
        || '';

      const itemCard = document.createElement('div');
      itemCard.style.cssText = 'background:#ffffff; border:1px solid #cbd5e1; border-radius:8px; padding:14px 16px; margin-bottom:10px; box-shadow:0 1px 3px rgba(0,0,0,0.05);';

      const itemLabel = paper.subject === 'writing' ? `Task ${q.num}` : `${sec.name.includes(':') ? sec.name.split(':')[0] : 'Section ' + sec.id}: Question ${q.num}`;

      itemCard.innerHTML = `
        <div style="font-weight:800; font-size:0.95rem; color:var(--sim-navy); margin-bottom:6px; display:flex; justify-content:space-between; align-items:center;">
          <span><i class="fa-solid fa-file-signature" style="color:var(--sim-blue); margin-right:6px;"></i> ${escapeHtml(itemLabel)}: ${escapeHtml(q.scenarioTitle || '')}</span>
          <span style="font-size:0.8rem; background:#f1f5f9; padding:2px 8px; border-radius:4px; color:#475569;">${q.marks || 0} Marks</span>
        </div>
        <div style="font-size:0.82rem; color:#64748b; margin-bottom:8px;">${escapeHtml(q.promptText || '')}</div>
        <div style="font-size:0.75rem; font-weight:700; color:#475569; text-transform:uppercase; margin-bottom:4px;">Your Typed Working / Steps:</div>
        <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:10px; font-size:0.85rem; font-family:'Courier New', monospace; white-space:pre-wrap; min-height:60px; margin-bottom:8px; color:#0f172a;">${escapeHtml(userWorking)}</div>
        ${userAns ? `
        <div style="font-size:0.9rem; font-weight:800; color:var(--sim-navy);">
          Your Concluded Answer: <span style="background:#e0f2fe; padding:2px 10px; border-radius:4px; color:#0369a1;">${escapeHtml(userAns)} ${escapeHtml(q.unit || '')}</span>
        </div>` : '<div style="font-size:0.85rem; color:#94a3b8; font-style:italic;">No final answer entered</div>'}
      `;
      container.appendChild(itemCard);
    });
  });

  const modal = document.getElementById('simCandidateAnswersModal');
  if (modal) {
    modal.setAttribute('tabindex', '-1');
    modal.classList.add('open');
    try { modal.focus(); } catch (err) {}
  }
}

function closeCandidateAnswersModal() {
  const modal = document.getElementById('simCandidateAnswersModal');
  if (modal) modal.classList.remove('open');
  try {
    const shell = document.getElementById('simAppShell');
    if (shell) shell.focus();
  } catch (err) {}
}

function downloadCandidateAnswersFile() {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const fullHtml = generatePrintableHtml('candidate');
  const blob = new Blob([fullHtml], { type: 'text/html;charset=utf-8;' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  const safeTitle = (paper.title || 'Mock Exam').replace(/[^a-zA-Z0-9 -]/g, '').trim().replace(/\s+/g, ' ');
  a.download = `${safeTitle} Candidate Answers.html`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
  setTimeout(() => {
    window.focus();
    const m = document.getElementById('simCandidateAnswersModal');
    if (m && m.classList.contains('open') && typeof m.focus === 'function') m.focus();
  }, 50);
}

// Dedicated Printable HTML Generator for A4 Print, Save as PDF & Downloads
function generatePrintableHtml(type = 'candidate') {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const sections = getPaperSections(paper);
  const now = new Date();
  const dateStr = now.toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit' });
  const isMarked = type === 'marked';
  const candidateName = localStorage.getItem('mfs_sim_candidate_name') || 'Learner';
  const subjectName = paper.subject === 'writing'
    ? 'Functional Skills English Writing'
    : paper.subject === 'reading'
      ? 'Functional Skills English Reading'
      : 'Functional Skills Mathematics';

  const totalPaperMarks = sections.reduce((acc, s) => {
    return acc + (s.totalMarks || (s.questions || []).reduce((qacc, q) => qacc + (q.marks || 0), 0));
  }, 0);

  let sectionsHtml = '';
  sections.forEach((sec) => {
    const secMarks = sec.totalMarks || (sec.questions || []).reduce((qacc, q) => qacc + (q.marks || 0), 0);
    const durStr = sec.durationMinutes >= 60 ? (sec.durationMinutes === 90 ? '1 hr 30 mins' : `${Math.floor(sec.durationMinutes / 60)} hrs`) : `${sec.durationMinutes} mins`;
    const secCalcBadge = paper.subject === 'maths'
      ? ` &bull; ${sec.isCalcAllowed ? 'Calculator Permitted' : 'Non-Calculator'}`
      : '';

    sectionsHtml += `
      <div class="mfs-print-section-header">
        <div class="mfs-print-section-title">${escapeHtml(sec.name)}</div>
        <div class="mfs-print-section-meta">${durStr} &bull; ${secMarks} Marks${secCalcBadge}</div>
      </div>
    `;

    sec.questions.forEach((q) => {
      const userWorking = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_sec_${sec.id}_q${q.num}_working`)
        || (sec.id === 'A' ? localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_q${q.num}_working`) : null)
        || '(No response recorded)';
      const userAns = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_sec_${sec.id}_q${q.num}_ans`)
        || (sec.id === 'A' ? localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_q${q.num}_ans`) : null)
        || '';
      const userPlanning = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_sec_${sec.id}_q${q.num}_planning`);

      const itemLabel = paper.subject === 'writing' ? `Task ${q.num}` : `${sec.name.includes(':') ? sec.name.split(':')[0] : 'Section ' + sec.id} — Question ${q.num}`;
      const marksLabel = `${q.marks || 0} Mark${q.marks === 1 ? '' : 's'}${q.markTags ? ' ' + escapeHtml(q.markTags) : ''}`;
      const workingLabel = paper.subject === 'writing'
        ? 'Candidate Written Response:'
        : (paper.subject === 'reading' ? 'Candidate Answer:' : 'Candidate Working &amp; Calculations:');

      let questionBodyHtml = '';
      if (!isMarked) {
        questionBodyHtml = `
          <div class="mfs-print-working-block">
            ${userPlanning ? `
              <div class="mfs-print-block-label" style="color:#64748b;">Candidate Planning Notes:</div>
              <pre class="mfs-print-pre" style="background:#f1f5f9; border:1px dashed #cbd5e1; color:#334155; min-height:30px; margin-bottom:8px;">${escapeHtml(userPlanning)}</pre>
            ` : ''}
            <div class="mfs-print-block-label candidate-label">${workingLabel}</div>
            <pre class="mfs-print-pre candidate-pre">${escapeHtml(userWorking)}</pre>
            ${userAns ? `
              <div class="mfs-print-ans-row">
                <span class="mfs-print-ans-label">${paper.subject === 'reading' ? 'Selected Answer:' : 'Concluded Final Answer:'}</span>
                <span class="mfs-print-ans-pill">${escapeHtml(userAns)} ${escapeHtml(q.unit || '')}</span>
              </div>
            ` : (paper.subject === 'maths' ? '<div class="mfs-print-no-ans">No final answer concluded in answer box.</div>' : '')}
          </div>
        `;
      } else {
        questionBodyHtml = `
          <div class="mfs-print-comparison-grid">
            <div class="mfs-print-col candidate-col">
              <div class="mfs-print-block-label candidate-label">${workingLabel}</div>
              ${userPlanning ? `
                <pre class="mfs-print-pre" style="background:#f1f5f9; border:1px dashed #cbd5e1; color:#334155; font-size:8.5pt; margin-bottom:6px;">Planning:\n${escapeHtml(userPlanning)}</pre>
              ` : ''}
              <pre class="mfs-print-pre candidate-pre">${escapeHtml(userWorking)}</pre>
              ${userAns ? `
                <div class="mfs-print-ans-row">
                  <span class="mfs-print-ans-label">Candidate Answer:</span>
                  <span class="mfs-print-ans-pill">${escapeHtml(userAns)} ${escapeHtml(q.unit || '')}</span>
                </div>
              ` : (paper.subject === 'maths' ? '<div class="mfs-print-no-ans">No final answer concluded</div>' : '')}
            </div>
            <div class="mfs-print-col model-col">
              <div class="mfs-print-block-label model-label">Master Model Solution &amp; Mark Scheme [${escapeHtml(q.markTags || '')}]:</div>
              <pre class="mfs-print-pre model-pre">${escapeHtml(q.modelSolution || '(Accredited model solution)')}</pre>
              ${q.finalBenchmark ? `
                <div class="mfs-print-ans-row">
                  <span class="mfs-print-model-ans-label">Model Benchmark:</span>
                  <span class="mfs-print-model-pill">${escapeHtml(q.finalBenchmark)}</span>
                </div>
              ` : ''}
            </div>
          </div>
        `;
      }

      sectionsHtml += `
        <div class="mfs-print-q-card">
          <div class="mfs-print-q-header">
            <span class="mfs-print-q-title">${escapeHtml(itemLabel)}: ${escapeHtml(q.scenarioTitle || '')}</span>
            <span class="mfs-print-q-marks">${marksLabel}</span>
          </div>
          <div class="mfs-print-prompt">
            ${q.scenarioText ? `<div style="margin-bottom:4px; color:#475569;">${escapeHtml(q.scenarioText)}</div>` : ''}
            <div><strong>Question Prompt:</strong> ${escapeHtml(q.promptText || '')}</div>
          </div>
          ${questionBodyHtml}
        </div>
      `;
    });
  });

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>${escapeHtml(paper.title)} — ${isMarked ? 'Marked Model Solution Benchmark' : 'Candidate Answers Record'}</title>
  <style>
    @page { size: A4 portrait; margin: 12mm 10mm 12mm 10mm; }
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; color: #0f172a; margin: 0; padding: 0; font-size: 9.5pt; line-height: 1.45; background: #ffffff; }
    .mfs-print-header { border-bottom: 2px solid #0284c7; padding-bottom: 8px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: flex-start; }
    .mfs-print-brand { font-size: 13pt; font-weight: 800; color: #0f172a; }
    .mfs-print-badge { font-size: 8pt; font-weight: 700; color: #0284c7; text-transform: uppercase; letter-spacing: 0.5px; }
    .mfs-print-meta { text-align: right; font-size: 8pt; color: #64748b; }
    .mfs-print-candidate-bar { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 6px 12px; display: flex; justify-content: space-between; font-size: 8.5pt; margin-bottom: 12px; }
    .mfs-print-candidate-bar strong { color: #0f172a; }
    .mfs-print-section-header { background: #0f172a; color: #ffffff; padding: 6px 10px; border-radius: 4px; font-weight: 700; font-size: 9pt; margin: 14px 0 8px 0; display: flex; justify-content: space-between; page-break-after: avoid; }
    .mfs-print-q-card { border: 1px solid #cbd5e1; border-radius: 6px; margin-bottom: 12px; padding: 8px 10px; page-break-inside: avoid; background: #ffffff; }
    .mfs-print-q-header { display: flex; justify-content: space-between; font-weight: 700; font-size: 9pt; color: #0f172a; border-bottom: 1px solid #e2e8f0; padding-bottom: 4px; margin-bottom: 6px; }
    .mfs-print-q-marks { background: #e0f2fe; color: #0369a1; padding: 1px 6px; border-radius: 4px; font-size: 8pt; }
    .mfs-print-prompt { font-size: 8.5pt; margin-bottom: 6px; }
    .mfs-print-comparison-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
    .mfs-print-col { border-radius: 4px; padding: 6px 8px; font-size: 8.5pt; }
    .candidate-col { background: #f8fafc; border: 1px solid #cbd5e1; }
    .model-col { background: #f0fdf4; border: 1px solid #86efac; }
    .mfs-print-block-label { font-size: 7.5pt; font-weight: 800; text-transform: uppercase; margin-bottom: 4px; }
    .candidate-label { color: #0284c7; }
    .model-label { color: #166534; }
    .mfs-print-pre { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, monospace; white-space: pre-wrap; margin: 0; font-size: 8.5pt; line-height: 1.4; color: #1e293b; }
    .candidate-pre { color: #0f172a; }
    .model-pre { color: #14532d; font-weight: 500; }
    .mfs-print-ans-row { display: flex; align-items: center; gap: 6px; margin-top: 6px; padding-top: 4px; border-top: 1px dashed #cbd5e1; font-size: 8pt; }
    .mfs-print-ans-label { font-weight: 700; color: #334155; }
    .mfs-print-ans-pill { background: #0284c7; color: #ffffff; padding: 2px 6px; border-radius: 4px; font-weight: 700; }
    .mfs-print-model-ans-label { font-weight: 700; color: #166534; }
    .mfs-print-model-pill { background: #16a34a; color: #ffffff; padding: 2px 6px; border-radius: 4px; font-weight: 700; }
    .mfs-print-no-ans { font-size: 8pt; color: #94a3b8; font-style: italic; margin-top: 4px; }
    .mfs-print-footer { border-top: 1px solid #e2e8f0; margin-top: 16px; padding-top: 6px; display: flex; justify-content: space-between; font-size: 7.5pt; color: #64748b; }
  </style>
  <script>
    window.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' || e.keyCode === 27) {
        if (window.parent && window.parent !== window && typeof window.parent.closeAllSimModals === 'function') {
          window.parent.closeAllSimModals();
        }
      }
    }, true);
  </script>
</head>
<body>
  <div class="mfs-print-header">
    <div>
      <div class="mfs-print-badge">${escapeHtml(paper.board || 'Pearson Edexcel')} Functional Skills &bull; ${escapeHtml(subjectName)}</div>
      <div class="mfs-print-brand">${escapeHtml(paper.title)}</div>
    </div>
    <div class="mfs-print-meta">
      <div>Centre: <strong>Master Functional Skills</strong></div>
      <div>Date: ${dateStr}</div>
      <div>Total Marks: <strong>${totalPaperMarks}</strong></div>
    </div>
  </div>

  <div class="mfs-print-candidate-bar">
    <div>Candidate: <strong>${escapeHtml(candidateName)}</strong></div>
    <div>Document Type: <strong>${isMarked ? 'Diagnostic Model Benchmark Comparison' : 'Candidate Exam Answers Record'}</strong></div>
    <div>Accreditation: <strong>Pearson Edexcel Reformed Specification</strong></div>
  </div>

  ${sectionsHtml}

  <div class="mfs-print-footer">
    <span>Master Functional Skills &bull; masterfunctionalskills.co.uk</span>
    <span>Pearson Edexcel Reform Benchmark &bull; Page Record</span>
  </div>
</body>
</html>`;
}


function printMockDocument(type = 'candidate') {
  const fullHtml = generatePrintableHtml(type);
  let printFrame = document.getElementById('simPrintIframe');
  if (!printFrame) {
    printFrame = document.createElement('iframe');
    printFrame.id = 'simPrintIframe';
    printFrame.setAttribute('style', 'position:fixed; top:-9999px; left:-9999px; width:1px; height:1px; opacity:0; border:none; pointer-events:none;');
    document.body.appendChild(printFrame);
  }
  const pDoc = printFrame.contentWindow.document;
  pDoc.open();
  pDoc.write(fullHtml);
  pDoc.close();

  const attachIframeEscape = () => {
    try {
      const iWin = printFrame.contentWindow;
      const iDoc = printFrame.contentDocument || (iWin && iWin.document);
      const onIframeEsc = (e) => {
        const isEsc = e.key === 'Escape' || e.key === 'Esc' || e.keyCode === 27 || e.which === 27;
        if (isEsc) {
          e.preventDefault();
          e.stopPropagation();
          closeAllSimModals();
        }
      };
      if (iWin) {
        iWin.removeEventListener('keydown', onIframeEsc, true);
        iWin.addEventListener('keydown', onIframeEsc, true);
        iWin.onafterprint = () => {
          setTimeout(() => {
            try {
              if (iWin.blur) iWin.blur();
              window.focus();
              const activeModal = document.querySelector('.sim-modal-overlay.open');
              if (activeModal && typeof activeModal.focus === 'function') activeModal.focus();
            } catch (err) {}
          }, 80);
        };
      }
      if (iDoc) {
        iDoc.removeEventListener('keydown', onIframeEsc, true);
        iDoc.addEventListener('keydown', onIframeEsc, true);
      }
    } catch (err) {
      console.warn('Unable to attach iframe listeners:', err);
    }
  };

  attachIframeEscape();

  setTimeout(() => {
    try {
      attachIframeEscape();
      printFrame.contentWindow.focus();
      printFrame.contentWindow.print();
    } catch (e) {
      console.warn('Print iframe error:', e);
      const printWin = window.open('', '_blank');
      if (printWin) {
        printWin.document.open();
        printWin.document.write(fullHtml);
        printWin.document.close();
        printWin.focus();
        printWin.print();
      }
    } finally {
      const refocusParent = () => {
        try {
          if (printFrame && printFrame.contentWindow && printFrame.contentWindow.blur) {
            printFrame.contentWindow.blur();
          }
          window.focus();
          const activeModal = document.querySelector('.sim-modal-overlay.open');
          if (activeModal && typeof activeModal.focus === 'function') activeModal.focus();
        } catch (err) {}
      };
      setTimeout(refocusParent, 200);
      setTimeout(refocusParent, 600);
      setTimeout(refocusParent, 1200);
      setTimeout(refocusParent, 2500);
    }
  }, 350);
}

// Check Answers Handler & Side-by-Side Model Comparison Modal
function handleCheckAnswersClick() {
  exitFullscreenIfActive();
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const sections = getPaperSections(paper);
  const currentSec = sections[simCurrentSectionIndex];

  // If in calculator section and not locked, prompt warning before leaving section
  if (currentSec && currentSec.isCalcAllowed && !isSectionLocked(currentSec.id)) {
    promptSectionLock(() => {
      openSubmitModal();
    });
  } else {
    openSubmitModal();
  }
}

function openSubmitModal() {
  exitFullscreenIfActive();
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const sections = getPaperSections(paper);
  const container = document.getElementById('simReviewList');
  if (!container) return;
  container.innerHTML = '';

  sections.forEach((sec) => {
    // Section Review Header
    const secHeader = document.createElement('div');
    secHeader.style.cssText = 'background:#0f172a; color:#ffffff; padding:12px 18px; border-radius:8px; font-weight:800; font-size:1rem; margin:16px 0 10px 0; display:flex; justify-content:space-between; align-items:center; letter-spacing:0.4px; flex-wrap:wrap; gap:8px;';
    const durStr = sec.durationMinutes >= 60 ? (sec.durationMinutes === 90 ? '1 hr 30 mins' : `${Math.floor(sec.durationMinutes / 60)} hrs`) : `${sec.durationMinutes} mins`;
    const marks = sec.totalMarks || (sec.questions || []).reduce((acc, q) => acc + (q.marks || 0), 0);
    secHeader.innerHTML = `
      <span><i class="fa-solid fa-layer-group" style="color:#38bdf8; margin-right:8px;"></i> ${escapeHtml(sec.name)}</span>
      <span style="font-size:0.82rem; font-weight:700; opacity:0.9;">${durStr} &bull; ${marks} Marks &bull; ${sec.isCalcAllowed ? 'Calculator Permitted' : 'Non-Calculator'}</span>
    `;
    container.appendChild(secHeader);

    sec.questions.forEach((q) => {
      const userWorking = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_sec_${sec.id}_q${q.num}_working`)
        || (sec.id === 'A' ? localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_q${q.num}_working`) : null)
        || '(No response recorded)';
      const userAns = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_sec_${sec.id}_q${q.num}_ans`)
        || (sec.id === 'A' ? localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_q${q.num}_ans`) : null)
        || '';

      const row = document.createElement('div');
      row.className = 'sim-review-row';

      const itemLabel = paper.subject === 'writing' ? `Task ${q.num}` : `${sec.name.includes(':') ? sec.name.split(':')[0] : 'Section ' + sec.id}: Question ${q.num}`;

      row.innerHTML = `
        <div>
          <div class="sim-review-col-title" style="color:var(--sim-navy);">
            <i class="fa-solid fa-user-pen" style="color:var(--sim-blue);"></i> ${escapeHtml(itemLabel)}: Your Response &amp; Working
          </div>
          <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:6px; padding:10px; font-size:0.85rem; font-family:'Courier New', monospace; white-space:pre-wrap; min-height:80px; margin-bottom:8px;">${escapeHtml(userWorking)}</div>
          ${userAns ? `
          <div style="font-size:0.9rem; font-weight:800; color:var(--sim-navy);">
            Your Concluded Answer: <span style="background:#e0f2fe; padding:2px 8px; border-radius:4px; color:#0369a1;">${escapeHtml(userAns)} ${escapeHtml(q.unit || '')}</span>
          </div>` : ''}
        </div>
        <div>
          <div class="sim-review-col-title" style="color:var(--sim-emerald);">
            <i class="fa-solid fa-award" style="color:var(--sim-green);"></i> Accredited Master Model &amp; Mark Scheme [${escapeHtml(q.markTags || '')}]
          </div>
          <div style="background:#f0fdf4; border:1px solid #86efac; border-radius:6px; padding:10px; font-size:0.85rem; font-family:'Courier New', monospace; white-space:pre-wrap; min-height:80px; margin-bottom:8px; color:#14532d;">${escapeHtml(q.modelSolution)}</div>
          <div style="font-size:0.9rem; font-weight:800; color:#15803d;">
            Model Benchmark: <span style="background:#dcfce7; padding:2px 8px; border-radius:4px;">${escapeHtml(q.finalBenchmark)}</span>
          </div>
        </div>
      `;
      container.appendChild(row);
    });
  });

  // Watch Walkthrough button
  const videoBtn = document.getElementById('simModalWatchVideoBtn');
  if (videoBtn) {
    if (paper.videoSolutionSlug) {
      videoBtn.style.display = 'inline-flex';
      videoBtn.href = `video-solution.html?topic=${paper.videoSolutionSlug}`;
    } else {
      videoBtn.style.display = 'none';
    }
  }

  // Open modal
  const modal = document.getElementById('simSubmitModal');
  if (modal) {
    modal.setAttribute('tabindex', '-1');
    modal.classList.add('open');
    try { modal.focus(); } catch (err) {}
  }
}

function closeSubmitModal() {
  const modal = document.getElementById('simSubmitModal');
  if (modal) modal.classList.remove('open');
  try {
    const shell = document.getElementById('simAppShell');
    if (shell) shell.focus();
  } catch (err) {}
}

function downloadMarkedReviewFile() {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const fullHtml = generatePrintableHtml('marked');
  const blob = new Blob([fullHtml], { type: 'text/html;charset=utf-8;' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  const safeTitle = (paper.title || 'Mock Exam').replace(/[^a-zA-Z0-9 -]/g, '').trim().replace(/\s+/g, ' ');
  a.download = `${safeTitle} Marked Model Review.html`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
  setTimeout(() => {
    window.focus();
    const m = document.getElementById('simSubmitModal');
    if (m && m.classList.contains('open') && typeof m.focus === 'function') m.focus();
  }, 50);
}
