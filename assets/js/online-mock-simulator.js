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

// Calculator state
let calcCurrentVal = '0';
let calcMemory = 0;
let calcPendingOp = null;
let calcWaitingForOperand = false;

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

  // 2. PEARSON EDEXCEL FUNCTIONAL SKILLS ENGLISH WRITING LEVEL 1 - PRACTICE 1
  // =========================================================================
  'edexcel-english-writing-l1-practice-1': {
    title: 'Edexcel Functional Skills English Writing Level 1 — Practice Paper 1',
    board: 'Pearson Edexcel',
    subject: 'writing',
    level: 'Level 1',
    paperNumber: 1,
    durationMinutes: 60,
    pdfUrl: 'https://passfunctionalskills.co.uk/wp-content/uploads/2021/09/Edexcel-FS-English-Writing-Level-1-Practice-Paper-1.pdf',
    modelSolutionPdf: 'assets/downloads/past-papers/edexcel/english-level-1/FS_English_Writing_Level_1_Practice_Paper_1_Model_Solution_MFS.pdf',
    videoSolutionSlug: '',
    questions: [
      {
        num: 1,
        section: 'Task 1: Formal Workplace Email',
        isCalcAllowed: false,
        marks: 21,
        markTags: '[12 Composition, 9 SPaG]',
        targetWords: '200 to 250 words',
        scenarioTitle: 'Charity Day Proposal to Colleague Sam',
        scenarioText: 'You receive an email from your workplace colleague Sam:\n"Hi, We are organising our company Charity Day next month to raise money for local good causes. We need ideas for activities that everyone can join in with. Some people suggested a cake sale, washing cars, or wearing funny clothes to work. What do you think would work best, and how could you help out on the day?\nThanks, Sam"',
        promptText: 'Write an email to Sam proposing ideas for Charity Day.\nIn your email, you must:\n• Give your opinion on the suggested activities (cake sale, car wash, funny clothes)\n• Suggest at least one new activity of your own with reasons why it would work well\n• Explain how you can personally help with the event\n• Use an appropriate subject line, greeting, paragraphs, and formal workplace sign-off.',
        unit: 'words',
        checklist: [
          'Included appropriate email subject line',
          'Used professional salutation (e.g. Dear Sam)',
          'Evaluated cake sale, car wash, and funny clothes suggestions',
          'Proposed new inclusive activity (e.g. sponsored 5k walk / raffle)',
          'Explained personal contribution on the day',
          'Checked spelling, punctuation, and capital letters'
        ],
        modelSolution: 'Subject: Charity Day Fundraising Proposal & Activity Ideas\n\nDear Sam,\n\nI am writing in response to your email regarding our upcoming annual Charity Day. Organising this event is a fantastic opportunity to bring our colleagues together, improve team morale, and raise vital funds for worthwhile local charities in our community.\n\nI really like the idea of holding a homemade cake sale because freshly baked treats are always very popular during morning coffee breaks. However, washing cars might be impractical if the weather is rainy, and wearing silly clothes can sometimes make visiting clients feel uncomfortable. Instead, I suggest organising a sponsored five-kilometre walk in the nearby park. A community walk is inclusive because people of all fitness levels can participate together. In addition, charging a modest five-pound registration fee and asking local businesses for raffle prizes would boost our fundraising total significantly.\n\nTo help with the event, I would be pleased to bake some chocolate muffins and savoury pastries for the cake stall. In addition, I can design colourful posters to put up across our office, set up tables and chairs on the morning of the event, and stay late afterwards to help count donations and tidy up. Please let me know if you would like to discuss these ideas further during our team meeting tomorrow.\n\nBest regards,\nJordan Bennett',
        finalBenchmark: 'Benchmark: 228 words • Full criteria met'
      },
      {
        num: 2,
        section: 'Task 2: Council Web Complaint Form',
        isCalcAllowed: false,
        marks: 15,
        markTags: '[9 Composition, 6 SPaG]',
        targetWords: '150 to 200 words',
        scenarioTitle: 'Anti-Social Behaviour Formal Complaint',
        scenarioText: 'You are completing an official online complaint form on your local council website regarding persistent antisocial behaviour from neighbours who recently moved in next door at 18 Willow Lane.',
        promptText: 'Complete the complaint form.\nIn your form, you must:\n• State the address involved and how long the disturbance has lasted\n• Detail specific examples of the disturbance (e.g. noise levels, rubbish)\n• Explain how this is negatively affecting you and your family\n• State the urgent action you expect the council to take.',
        unit: 'words',
        checklist: [
          'Stated property address and timeframe clearly',
          'Provided specific examples of anti-social disturbances',
          'Described the emotional/physical impact on family life',
          'Made clear, reasonable request for council intervention',
          'Maintained formal, assertive, and respectful tone throughout'
        ],
        modelSolution: 'I am submitting this formal complaint regarding the tenants who recently moved into the property next door at 18 Willow Lane. Over the past three weeks, their persistent antisocial behaviour has caused severe distress and disruption to our quiet residential neighbourhood.\n\nFirstly, they play loud music late into the night and host noisy garden parties on weekday evenings. Secondly, they leave black bin bags of rotting rubbish piled outside their front door. The bags have split open, attracting foxes and creating an awful smell. When I attempted to speak with them politely last weekend, they were extremely aggressive, shouted at me, and slammed the door.\n\nThis constant disturbance is severely affecting my family. We are unable to sleep properly, and my young children are frequently woken up crying. I feel exhausted and stressed at work every day. I urge the council to investigate this matter urgently and take firm enforcement action.\n\nYours sincerely,\nJordan Bennett',
        finalBenchmark: 'Benchmark: 172 words • Full criteria met'
      }
    ]
  },

  // =========================================================================
  // 3. PEARSON EDEXCEL FUNCTIONAL SKILLS ENGLISH READING LEVEL 1 - PAST PAPER 10
  // =========================================================================
  'edexcel-english-reading-l1-paper-10': {
    title: 'Edexcel Functional Skills English Reading Level 1 — Past Paper 10',
    board: 'Pearson Edexcel',
    subject: 'reading',
    level: 'Level 1',
    paperNumber: 10,
    durationMinutes: 60,
    pdfUrl: 'https://passfunctionalskills.co.uk/app/uploads/2024/06/FS_English_Reading_Level_1_Past_Paper_10_QP.pdf',
    modelSolutionPdf: 'assets/downloads/past-papers/edexcel/english-level-1/FS_English_Reading_Level_1_Past_Paper_10_Model_Solution_MFS.pdf',
    videoSolutionSlug: '',
    sourceTexts: [
      {
        id: 'text-a',
        label: 'Text A: Email',
        title: 'Email: Good news from Sam',
        content: `From: Sam
To: Ali
Subject: Good news

Hey Ali,

Good news – I’ve passed my Level 2 in Business Administration. The even better news is I’ve got a job in the finance team at the hospital.

I’m thrilled but also a bit nervous so I’m looking for advice. It’s going to be totally different from what I’m doing now – this new job looks more challenging, but the salary is much better.

There’s no uniform – so I’ll have to think about what I’m going to wear. What tips do you have for starting this job – especially what to do on the first day?

Cheers,
Sam`
      },
      {
        id: 'text-b',
        label: 'Text B: Webpage',
        title: 'Careers Advice: First day in a new job',
        content: `First day in a new job

Be prepared
Congratulations – you’ve got a new job. Now you need to prepare for the first day. Re-read the job description so you’re clear about what’s expected of you. Have another look at the company website to update yourself on the latest information and check the dress code. Work out your route there and think about transport. Collect the documents you need to take with you, like proof of your address.

Get off to the right start
It’s essential to be punctual on your first day – take care over your appearance and have a suitable workbag. Introduce yourself to people you meet and make sure you smile and look enthusiastic – this will impress everyone straightaway. Take a folder to keep any material you’re given.

Learn names and roles
Aim to learn the names of people, especially those you’re going to be working with – it’s helpful to find out people’s roles and responsibilities too. You’ll be given lots of information on the first day so have something with you to note down the things you need to remember.

Become involved
It can be difficult on the first day to know what to do, but if there’s an opportunity, offer to help out with a task or sit in on a meeting – and ask plenty of questions. You could also make cups of tea (take your own mug) – this will demonstrate you’re willing and eager to be part of the team.

Know your workplace
Make sure you get to know the layout of the building – the location of the toilets, the staff restroom and the fire exits. It’s useful to know where your line manager is based and how to get to the canteen – you may be given a work buddy to help you. The first day is exhausting – but everything will become more familiar and easier as the weeks go by.

Good luck!`
      },
      {
        id: 'text-c',
        label: 'Text C: Forum',
        title: 'Careers Advice Web Forum Discussion',
        content: `Chas:
Do you remember your first day in your first job? I was totally freaked out – I felt sick with nerves. My grandad said: ‘Just keep smiling’. That advice helped. It’s important to get ready before your first day, like deciding how to travel to your new workplace.

Lilli:
Yes, starting a new job is incredibly challenging – you don’t know anyone, everything is unfamiliar – and sometimes there isn’t enough to do. Try to bond with a fellow worker on the first day – later on, they can advise you about things like holiday entitlement.

Seth:
It’s tough for sure, Lilli. Writing everything down really helped me on my first day. There’s useful advice online, including reminders to get your paperwork sorted beforehand. After you’ve been there for a few weeks, find out about sick leave.

Lilli:
It’s sensible to check what to wear before you start. My last job, I turned up in a dress and discovered everyone else in jeans – awkward! My tip for the first day is keep your phone off.

Chas:
I asked about promotion opportunities on the first day in my current job – I was worried it was out of line, but my manager praised my ambition. Now I’ve been in the job a while, I’m planning to request time off to study.`
      }
    ],
    questions: [
      {
        num: 1,
        section: 'Questions on Text A',
        isCalcAllowed: false,
        marks: 2,
        markTags: '[1 mark, 1 mark]',
        scenarioTitle: 'Text A: Location & Organisational Feature',
        scenarioText: 'Refer to Text A (Email from Sam) in the Source Booklet.',
        promptText: '(a) According to Text A, where is Sam’s new job?\n(b) Which organisational feature helped you find this information?',
        unit: '',
        expectedType: 'text',
        parts: [
          { id: 'a', label: 'Part (a) Location', placeholder: 'Where is Sam’s new job?', unit: '' },
          { id: 'b', label: 'Part (b) Feature', placeholder: 'Organisational feature identified', unit: '' }
        ],
        modelSolution: '(a) In the finance team at the hospital [1 mark]\n(b) Email body / first paragraph / subject line [1 mark]',
        finalBenchmark: 'At the hospital (finance team) / Email text'
      },
      {
        num: 2,
        section: 'Questions on Text A',
        isCalcAllowed: false,
        marks: 1,
        markTags: '[1 mark]',
        scenarioTitle: 'Text A: Vocabulary & Synonyms',
        scenarioText: 'In Text A, Sam writes: ‘especially what to do’.\nYou may use a dictionary to answer this question.',
        promptText: 'Give one word or phrase to replace ‘especially’ that keeps the meaning of this quotation the same.',
        unit: '',
        expectedType: 'text',
        modelSolution: 'Accept: particularly / specifically / in particular / mostly [1 mark]',
        finalBenchmark: 'particularly / specifically'
      },
      {
        num: 3,
        section: 'Questions on Text A',
        isCalcAllowed: false,
        marks: 2,
        markTags: '[1 mark, 1 mark]',
        scenarioTitle: 'Text A: Emotion & Attitude Retrieval',
        scenarioText: 'Refer to Text A (Email from Sam).',
        promptText: 'According to Text A, identify two different feelings Sam has about starting the new job.',
        unit: '',
        expectedType: 'text',
        modelSolution: '1. Thrilled (excited) [1 mark]\n2. Nervous (anxious / apprehensive) [1 mark]',
        finalBenchmark: '1. Thrilled  2. Nervous'
      },
      {
        num: 4,
        section: 'Questions on Text B',
        isCalcAllowed: false,
        marks: 1,
        markTags: '[1 mark]',
        scenarioTitle: 'Text B: Purpose of Text',
        scenarioText: 'Refer to Text B (Careers Advice Webpage).',
        promptText: 'What is the main purpose of Text B?',
        expectedType: 'multiple-choice',
        options: [
          'A: To advertise job vacancies at a company',
          'B: To give practical guidance on preparing for and surviving your first day at work',
          'C: To explain health and safety laws in office workplaces',
          'D: To review different types of work bags and mugs'
        ],
        modelSolution: 'Correct Answer: B (To give practical guidance on preparing for and surviving your first day at work) [1 mark]',
        finalBenchmark: 'Option B'
      },
      {
        num: 5,
        section: 'Questions on Text B',
        isCalcAllowed: false,
        marks: 2,
        markTags: '[1 mark, 1 mark]',
        scenarioTitle: 'Text B: Information Retrieval (Items)',
        scenarioText: 'Refer to Text B.',
        promptText: 'According to Text B, give two practical items or documents you should collect or take with you on your first day.',
        unit: '',
        expectedType: 'text',
        modelSolution: 'Any two from: Proof of address / Suitable workbag / Folder (for keeping material) / Notepad or pen (something to note things down) / Own mug [1 mark each, max 2]',
        finalBenchmark: 'Proof of address / folder / workbag / notepad'
      },
      {
        num: 6,
        section: 'Questions on Text B',
        isCalcAllowed: false,
        marks: 2,
        markTags: '[1 mark, 1 mark]',
        scenarioTitle: 'Text B: Interpersonal Skills & First Impression',
        scenarioText: 'Refer to Text B under the heading ‘Get off to the right start’.',
        promptText: 'What two things should you do when meeting new people to impress everyone straightaway?',
        unit: '',
        expectedType: 'text',
        modelSolution: '1. Introduce yourself [1 mark]\n2. Smile and look enthusiastic [1 mark]',
        finalBenchmark: 'Introduce yourself / Smile and look enthusiastic'
      },
      {
        num: 7,
        section: 'Questions on Text B',
        isCalcAllowed: false,
        marks: 2,
        markTags: '[1 mark, 1 mark]',
        scenarioTitle: 'Text B: Workplace Layout & Facilities',
        scenarioText: 'Refer to Text B under the heading ‘Know your workplace’.',
        promptText: 'Name two facilities or locations in the building layout you should get to know.',
        unit: '',
        expectedType: 'text',
        modelSolution: 'Any two from: Toilets / Staff restroom / Fire exits / Where line manager is based / Canteen [1 mark each, max 2]',
        finalBenchmark: 'Toilets / Fire exits / Canteen'
      },
      {
        num: 8,
        section: 'Questions on Text B',
        isCalcAllowed: false,
        marks: 1,
        markTags: '[1 mark]',
        scenarioTitle: 'Text B: Identifying Subheadings',
        scenarioText: 'Refer to Text B.',
        promptText: 'Which sub-heading in Text B contains advice on offering to help with tasks and making cups of tea?',
        unit: '',
        expectedType: 'text',
        modelSolution: 'Become involved [1 mark]',
        finalBenchmark: 'Become involved'
      },
      {
        num: 9,
        section: 'Questions on Text C',
        isCalcAllowed: false,
        marks: 1,
        markTags: '[1 mark]',
        scenarioTitle: 'Text C: Grandad\'s Advice',
        scenarioText: 'Refer to Text C (Forum comments).',
        promptText: 'In Text C, what advice from Chas\'s grandad helped him with his nerves on his first day?',
        unit: '',
        expectedType: 'text',
        modelSolution: '‘Just keep smiling’ [1 mark]',
        finalBenchmark: 'Just keep smiling'
      },
      {
        num: 10,
        section: 'Questions on Text C',
        isCalcAllowed: false,
        marks: 1,
        markTags: '[1 mark]',
        scenarioTitle: 'Text C: Telephone Etiquette',
        scenarioText: 'Refer to Lilli\'s comments in Text C.',
        promptText: 'What specific tip does Lilli give for your first day regarding your mobile phone?',
        unit: '',
        expectedType: 'text',
        modelSolution: 'Keep your phone off [1 mark]',
        finalBenchmark: 'Keep your phone off'
      },
      {
        num: 11,
        section: 'Synthesis: Text B & Text C',
        isCalcAllowed: false,
        marks: 3,
        markTags: '[3 marks]',
        scenarioTitle: 'Comparing Advice across Texts B and C',
        scenarioText: 'Both Text B and Text C give advice about starting a new job.',
        promptText: 'Identify one similarity in the advice given in both Text B and Text C, and one difference in the specific tips mentioned.',
        unit: '',
        expectedType: 'text',
        modelSolution: 'Similarity: Both recommend getting paperwork/documents organized before the first day, and checking travel arrangements/transport route [1-2 marks].\nDifference: Text B recommends offering to make cups of tea to show willingness; Text C advises keeping your phone switched off or asking about study leave [1 mark].',
        finalBenchmark: 'Similarity: Paperwork / Route; Difference: Tea / Phone etiquette'
      }
    ]
  }
};

// Helper: Get Paper Object (supports fallback generation)
function getOrCreatePaper(key) {
  if (MFS_MOCK_DATA[key]) return MFS_MOCK_DATA[key];

  // Dynamic fallback generator for any paper link from website
  const isWriting = key.includes('writing') || key.includes('english-writing');
  const isReading = key.includes('reading') || key.includes('english-reading');
  const isMaths = !isWriting && !isReading;

  const levelName = (key.includes('l2') || key.includes('level-2')) ? 'Level 2' : 'Level 1';
  const paperMatch = key.match(/paper-(\d+)/) || key.match(/practice-(\d+)/);
  const paperNum = paperMatch ? paperMatch[1] : (key.match(/([a-z0-9\-]+)$/) ? key.match(/([a-z0-9\-]+)$/)[1] : '1');
  const boardName = key.includes('aqa') ? 'AQA' : (key.includes('city') ? 'City & Guilds' : (key.includes('ncfe') ? 'NCFE' : (key.includes('tquk') ? 'TQUK' : (key.includes('nocn') ? 'NOCN' : 'Pearson Edexcel'))));

  if (isWriting) {
    return {
      title: `${boardName} Functional Skills English Writing ${levelName} — Paper ${paperNum}`,
      board: boardName,
      subject: 'writing',
      level: levelName,
      paperNumber: paperNum,
      durationMinutes: 60,
      questions: [
        {
          num: 1,
          section: 'Task 1: Formal Correspondence / Email',
          isCalcAllowed: false,
          marks: 21,
          markTags: '[12 Composition, 9 SPaG]',
          targetWords: '200 to 250 words',
          scenarioTitle: 'Vocational Workplace Writing Task 1',
          scenarioText: `Write an extended formal email or article based on the prompt requirements for Paper ${paperNum}.`,
          promptText: 'Address all bullet points, structure with clear paragraphs, and maintain a professional tone throughout.',
          unit: 'words',
          checklist: ['Addressed all prompt bullet points', 'Paragraphing used effectively', 'Formal/semi-formal tone maintained', 'SPaG checked carefully'],
          modelSolution: 'Examiner Model Criteria: Clear logical flow, appropriate register, complex sentence structures, accurate punctuation.',
          finalBenchmark: 'Target 200–250 words'
        },
        {
          num: 2,
          section: 'Task 2: Web Form / Report / Review',
          isCalcAllowed: false,
          marks: 15,
          markTags: '[9 Composition, 6 SPaG]',
          targetWords: '150 to 200 words',
          scenarioTitle: 'Public Form / Formal Letter Task 2',
          scenarioText: `Complete the formal web form or response requested in Task 2 for Paper ${paperNum}.`,
          promptText: 'Ensure your writing is detailed, persuasive, and accurately checked.',
          unit: 'words',
          checklist: ['Addressed required details', 'Appropriate tone for audience', 'Proofread for spelling and grammar'],
          modelSolution: 'Examiner Model Criteria: Cohesive argument, appropriate salutation and sign-off, varied vocabulary.',
          finalBenchmark: 'Target 150–200 words'
        }
      ]
    };
  } else if (isReading) {
    const isL2Reading = levelName === 'Level 2';
    return {
      title: `${boardName} Functional Skills English Reading ${levelName} — Paper ${paperNum}`,
      board: boardName,
      subject: 'reading',
      level: levelName,
      paperNumber: paperNum,
      durationMinutes: isL2Reading ? 75 : 60,
      sourceTexts: [
        { id: 'text-a', label: 'Text A', title: 'Text A: Informational Article', content: `Source Text A for ${boardName} English Reading ${levelName} Paper ${paperNum}.\nPlease consult the official Question Paper PDF for complete source articles.` },
        { id: 'text-b', label: 'Text B', title: 'Text B: Guidance Webpage', content: `Source Text B for ${boardName} English Reading ${levelName} Paper ${paperNum}.\nPlease consult the official Question Paper PDF for complete source articles.` },
        { id: 'text-c', label: 'Text C', title: 'Text C: Public Notice / Factsheet', content: `Source Text C for ${boardName} English Reading ${levelName} Paper ${paperNum}.\nPlease consult the official Question Paper PDF for complete source articles.` }
      ],
      questions: isL2Reading ? [
        { num: 1, section: 'Text A Analysis', marks: 2, promptText: 'Identify two reasons given in Text A regarding the primary issue.', expectedType: 'text', modelSolution: 'Consult mark scheme for accredited details.', finalBenchmark: '2 marks' },
        { num: 2, section: 'Text A Organisational Features', marks: 2, promptText: 'Explain how the author uses organisational features in Text A to present information clearly.', expectedType: 'text', modelSolution: 'Use of subheadings, bullet points, and bold text.', finalBenchmark: '2 marks' },
        { num: 3, section: 'Text B Vocabulary & Tone', marks: 2, promptText: 'Give the meaning of the key term as used in paragraph 3 of Text B.', expectedType: 'text', modelSolution: 'Vocabulary definition in context.', finalBenchmark: '2 marks' },
        { num: 4, section: 'Text B Bias & Fact vs Opinion', marks: 3, promptText: 'Identify one fact and two opinions expressed in Text B.', expectedType: 'text', modelSolution: 'Fact vs opinion differentiation.', finalBenchmark: '3 marks' },
        { num: 5, section: 'Text C Implication & Purpose', marks: 3, promptText: 'What is the main purpose of Text C? Support your answer with two textual examples.', expectedType: 'text', modelSolution: 'Purpose identification with textual evidence.', finalBenchmark: '3 marks' },
        { num: 6, section: 'Synthesis & Comparison', marks: 3, promptText: 'Compare the views presented in Text A and Text C regarding the proposed change.', expectedType: 'text', modelSolution: 'Comparison of perspectives across texts.', finalBenchmark: '3 marks' }
      ] : [
        { num: 1, section: 'Text A Retrieval', marks: 2, promptText: 'Identify two key facts provided in Text A.', expectedType: 'text', modelSolution: 'Factual retrieval from Text A.', finalBenchmark: '2 marks' },
        { num: 2, section: 'Text A Main Purpose', marks: 2, promptText: 'What is the main purpose of Text A?', expectedType: 'text', modelSolution: 'Informative / instructional purpose.', finalBenchmark: '2 marks' },
        { num: 3, section: 'Text B Information Search', marks: 2, promptText: 'According to Text B, what should a reader do first?', expectedType: 'text', modelSolution: 'Instructional retrieval from Text B.', finalBenchmark: '2 marks' },
        { num: 4, section: 'Text B & C Comparison', marks: 3, promptText: 'Identify one similarity and one difference in the advice given in Text B and Text C.', expectedType: 'text', modelSolution: 'Cross-text comparative synthesis.', finalBenchmark: '3 marks' }
      ]
    };
  }

  // Mathematics: Level 2 vs Level 1
  if (levelName === 'Level 2') {
    // Generate Level 2 Maths paper with Section A (25 min, 16 marks, 4 Qs) and Section B (90 min, 48 marks, 12 Qs)
    return {
      title: `${boardName} Functional Skills Mathematics Level 2 — Past Paper ${paperNum}`,
      board: boardName,
      subject: 'maths',
      level: 'Level 2',
      paperNumber: paperNum,
      durationMinutes: 115,
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
              scenarioTitle: 'Core Non-Calculator Decimals & Indices',
              scenarioText: `Question 1 for ${boardName} Level 2 Mathematics Paper ${paperNum}.`,
              promptText: '(a) Work out 6.4 × 8.5 without a calculator.\n(b) Work out 5 × 4²',
              expectedType: 'number',
              parts: [
                { id: 'a', label: 'Part (a) 6.4 × 8.5', placeholder: 'e.g. 54.4', unit: '' },
                { id: 'b', label: 'Part (b) 5 × 4²', placeholder: 'e.g. 80', unit: '' }
              ],
              modelSolution: '(a) 64 × 85 = 5440 -> 54.4 [M1, A1]\n(b) 4² = 16; 5 × 16 = 80 [B1]',
              finalBenchmark: '54.4 / 80'
            },
            {
              num: 2,
              section: 'Section A: Non-Calculator',
              isCalcAllowed: false,
              marks: 3,
              markTags: '[M1, M1, A1]',
              scenarioTitle: 'Negative Financial Balances & Budgeting',
              scenarioText: 'A commercial bank account starts with a negative balance of −£245.80. A client pays in £1,450.00 and an automatic invoice payment of £680.50 is deducted.',
              promptText: 'Calculate the final account balance at the end of the day.',
              unit: '£',
              expectedType: 'number',
              parts: [
                { id: 'balance', label: 'Closing Balance', placeholder: 'e.g. 523.70', unit: '£' }
              ],
              modelSolution: '−245.80 + 1450.00 = £1204.20 [M1]; 1204.20 − 680.50 = £523.70 [M1, A1]',
              finalBenchmark: '£523.70'
            },
            {
              num: 3,
              section: 'Section A: Non-Calculator',
              isCalcAllowed: false,
              marks: 4,
              markTags: '[M1, M1, M1, A1]',
              scenarioTitle: 'Compound Shape Perimeter & Estimation',
              scenarioText: 'A specialist workshop needs perimeter protective barrier edging around an L-shaped engineering bay measuring 18.6 m by 12.4 m.',
              promptText: 'Use rounding to 1 significant figure to estimate the total length of protective edging required.',
              unit: 'm',
              expectedType: 'number',
              parts: [
                { id: 'estimate', label: 'Estimated Perimeter', placeholder: 'e.g. 60', unit: 'm' }
              ],
              modelSolution: 'Round to 1 sig fig: 18.6 ≈ 20 m, 12.4 ≈ 10 m [M1]; Perimeter = 2 × (20 + 10) = 60 m [M1, A1]',
              finalBenchmark: '60 m'
            },
            {
              num: 4,
              section: 'Section A: Non-Calculator',
              isCalcAllowed: false,
              marks: 6,
              markTags: '[M1, A1, M1, A1, C1, C1]',
              scenarioTitle: 'Comparing Averages & Data Consistency',
              scenarioText: 'Compare delivery wait times across two logistics depots (Depot 1 median: 14.2 min, range: 18 min; Depot 2 raw dataset: 12, 15, 9, 28, 14, 11, 33, 16, 10, 22).',
              promptText: 'Calculate the median and range for Depot 2, then explain which depot has faster average deliveries and which is more consistent.',
              unit: '',
              expectedType: 'text',
              parts: [
                { id: 'median', label: 'Depot 2 Median', placeholder: 'e.g. 14.5', unit: 'mins' },
                { id: 'range', label: 'Depot 2 Range', placeholder: 'e.g. 24', unit: 'mins' },
                { id: 'conclusion', label: 'Comparison Conclusion', placeholder: 'Compare medians and consistency', unit: '' }
              ],
              modelSolution: 'Ordered: 9, 10, 11, 12, 14, 15, 16, 22, 28, 33 [M1]; Median = (14 + 15)/2 = 14.5 min [A1]; Range = 33 − 9 = 24 min [M1, A1]; Comparison: Depot 1 is faster (14.2 < 14.5) and more consistent (18 < 24) [C1, C1]',
              finalBenchmark: 'Depot 2 Median: 14.5 mins, Range: 24 mins'
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
            { num: 1, section: 'Rates of Pay & Overtime', isCalcAllowed: true, marks: 3, markTags: '[M1, M1, A1]', scenarioTitle: 'Overtime Earnings', scenarioText: 'Standard hourly wage is £11.40. Overtime is paid at time and a half for 8.5 hours.', promptText: 'Calculate total overtime pay.', unit: '£', expectedType: 'number', modelSolution: '11.40 × 1.5 = £17.10/hr; 17.10 × 8.5 = £145.35 [M1, A1]', finalBenchmark: '£145.35' },
            { num: 2, section: '3D Geometry: Volume of Cylinder', isCalcAllowed: true, marks: 3, markTags: '[M1, M1, A1]', scenarioTitle: 'Cylindrical Storage Tank', scenarioText: 'A cylindrical water tank has radius 1.2 m and height 2.5 m. Volume = πr²h.', promptText: 'Work out the volume of water the tank can hold. Use π = 3.142 or calculator π.', unit: 'm³', expectedType: 'number', modelSolution: 'V = π × 1.2² × 2.5 = π × 1.44 × 2.5 = 11.31 m³ [M1, A1]', finalBenchmark: '11.31 m³' },
            { num: 3, section: 'Reverse Calculations & Proportions', isCalcAllowed: true, marks: 4, markTags: '[M1, M1, A1, B1]', scenarioTitle: 'Batch Production Scaling', scenarioText: 'A catering recipe for 15 portions requires 450 g butter. Work out the butter needed for 36 portions, and show a reverse check.', promptText: '(a) Butter required for 36 portions. (b) Reverse check.', unit: 'g', expectedType: 'number', modelSolution: 'Per portion = 450 ÷ 15 = 30 g; 30 × 36 = 1080 g [M1, A1]; Check: 1080 ÷ 36 = 30 g [B1]', finalBenchmark: '1080 g' },
            { num: 4, section: 'Angle Properties & Triangles', isCalcAllowed: true, marks: 4, markTags: '[M1, M1, M1, A1]', scenarioTitle: 'Roof Truss Angles', scenarioText: 'An isosceles roof truss has an apex angle of 48°. Work out the size of the base angles.', promptText: 'Calculate the base angle of the isosceles truss.', unit: '°', expectedType: 'number', modelSolution: '(180 − 48) ÷ 2 = 132 ÷ 2 = 66° [M1, A1]', finalBenchmark: '66°' },
            { num: 5, section: 'Compound Area & Pack Costing', isCalcAllowed: true, marks: 5, markTags: '[M1, M1, M1, M1, A1]', scenarioTitle: 'Flooring Tiles & Whole Packs', scenarioText: 'A rectangular clinic lobby 8.4 m by 5.5 m needs tiles. Tiles come in boxes covering 2.4 m² at £38.50 per box. Only full boxes can be purchased.', promptText: 'Calculate the total cost of tiles needed.', unit: '£', expectedType: 'number', modelSolution: 'Area = 8.4 × 5.5 = 46.2 m²; Boxes = 46.2 ÷ 2.4 = 19.25 -> 20 boxes; Cost = 20 × £38.50 = £770.00 [M1, A1]', finalBenchmark: '£770.00' },
            { num: 6, section: 'Percentage Increase / Decrease', isCalcAllowed: true, marks: 3, markTags: '[M1, M1, A1]', scenarioTitle: 'Retail Discount Verification', scenarioText: 'A machinery item originally £420 is reduced to £315 in a clearance event. The store advertises "30% off".', promptText: 'Check if the advertised 30% discount is accurate. Show your working.', unit: '', expectedType: 'decision', modelSolution: 'Saving = 420 − 315 = £105; 105 ÷ 420 × 100 = 25%; Advertised 30% is incorrect (actual is 25%) [M1, A1]', finalBenchmark: 'No (Actual discount is 25%)' },
            { num: 7, section: 'Scale Plans & Bearings', isCalcAllowed: true, marks: 4, markTags: '[M1, A1, M1, A1]', scenarioTitle: 'Surveyor Scale Plan', scenarioText: 'On a plan drawn to scale 1 : 250, the distance between two survey points measures 14.8 cm.', promptText: 'Calculate the actual real-world distance between the two survey points in metres.', unit: 'm', expectedType: 'number', modelSolution: '14.8 × 250 = 3700 cm = 37.0 m [M1, A1]', finalBenchmark: '37 m' },
            { num: 8, section: 'Bivariate Data & Scatter Graphs', isCalcAllowed: true, marks: 6, markTags: '[M1, A1, B1, M1, A1, B1]', scenarioTitle: 'Scatter Graph Analysis', scenarioText: 'A study compares staff training hours against customer satisfaction ratings.', promptText: '(a) Identify the correlation. (b) Use a line of best fit to predict satisfaction for 35 hours of training.', unit: '', expectedType: 'text', modelSolution: 'Positive correlation; Estimate from trend line gives approx 82–88 rating [M1, A1]', finalBenchmark: 'Positive correlation; approx 85%' },
            { num: 9, section: 'Algebraic Formulas & Density', isCalcAllowed: true, marks: 4, markTags: '[M1, M1, M1, A1]', scenarioTitle: 'Material Density & Mass', scenarioText: 'Density = Mass ÷ Volume. A metal alloy casting has mass 14.85 kg and volume 0.0018 m³.', promptText: 'Calculate the density of the metal alloy in kg/m³.', unit: 'kg/m³', expectedType: 'number', modelSolution: 'Density = 14.85 ÷ 0.0018 = 8250 kg/m³ [M1, A1]', finalBenchmark: '8250 kg/m³' },
            { num: 10, section: 'Fraction Operations & Mixed Numbers', isCalcAllowed: true, marks: 3, markTags: '[M1, A1, B1]', scenarioTitle: 'Mixed Number Arithmetic', scenarioText: 'Work out 2 3/4 + 1 2/5 and give your answer as a mixed number in simplest form.', promptText: 'Calculate 2 3/4 + 1 2/5.', unit: '', expectedType: 'text', modelSolution: '2 3/4 = 11/4 = 55/20; 1 2/5 = 7/5 = 28/20; 55/20 + 28/20 = 83/20 = 4 3/20 [M1, A1]', finalBenchmark: '4 3/20' },
            { num: 11, section: 'Ratio in Three Parts', isCalcAllowed: true, marks: 5, markTags: '[M1, M1, M1, M1, A1]', scenarioTitle: 'Budget Sharing Ratio', scenarioText: 'A community grant of £84,000 is shared between Education, Healthcare, and Infrastructure in the ratio 3 : 5 : 4.', promptText: 'How much funding does Healthcare receive?', unit: '£', expectedType: 'number', modelSolution: 'Total parts = 3 + 5 + 4 = 12; 1 part = 84,000 ÷ 12 = £7,000; Healthcare = 5 × 7,000 = £35,000 [M1, A1]', finalBenchmark: '£35,000' },
            { num: 12, section: 'Two-Way Tables & Probability', isCalcAllowed: true, marks: 6, markTags: '[M1, A1, M1, A1, M1, A1]', scenarioTitle: 'Quality Inspection Contingency Table', scenarioText: 'A factory tests 120 components across two production lines. Complete the contingency table and calculate the conditional probability of selecting a pass from Line B.', promptText: 'Complete table and state simplified probability.', unit: '', expectedType: 'text', modelSolution: 'Table completion; P(Pass | Line B) = 48/60 = 4/5 [M1, A1]', finalBenchmark: '4/5 (or 0.8)' }
          ]
        }
      ]
    };
  }

  // Level 1 Maths Paper
  return MFS_MOCK_DATA['edexcel-maths-l1-paper-1'];
}

// Initialise Simulator from Query Parameters or Default
// Helper: Get Paper Sections (with fallback support)
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
  const board = urlParams.get('board') || 'edexcel';
  const subject = urlParams.get('subject') || 'maths';
  const level = urlParams.get('level') || 'l1';
  const paper = urlParams.get('paper') || '1';

  let key = `${board}-${subject}-${level}-paper-${paper}`;
  if (paper.startsWith('practice')) {
    key = `${board}-${subject}-${level}-${paper}`;
  }

  // Normalise subject alias
  if (subject === 'english' || subject === 'writing') {
    key = `${board}-english-writing-${level}-paper-${paper}`;
    if (paper.startsWith('practice')) key = `${board}-english-writing-${level}-${paper}`;
  } else if (subject === 'reading') {
    key = `${board}-english-reading-${level}-paper-${paper}`;
    if (paper.startsWith('practice')) key = `${board}-english-reading-${level}-${paper}`;
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
});

// Load and Render Paper
function loadPaper(paperKey) {
  simCurrentPaperKey = paperKey;
  simStartedSections = {};
  const paper = getOrCreatePaper(paperKey);
  const sections = getPaperSections(paper);
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
  loadPaper(newKey);
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
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = `sim-sec-tab-btn ${idx === simCurrentSectionIndex ? 'active' : ''}`;
    
    const durStr = sec.durationMinutes >= 60 
      ? (sec.durationMinutes === 90 ? '1 hr 30 mins' : `${Math.floor(sec.durationMinutes / 60)} hrs`)
      : `${sec.durationMinutes} mins`;
    const marks = sec.totalMarks || (sec.questions || []).reduce((acc, q) => acc + (q.marks || 0), 0);
    const calcBadge = sec.isCalcAllowed 
      ? `<span class="sim-sec-badge calc"><i class="fa-solid fa-calculator"></i> Calculator Allowed</span>`
      : `<span class="sim-sec-badge"><i class="fa-solid fa-ban"></i> Non-Calculator</span>`;

    btn.innerHTML = `
      <span class="sim-sec-title"><i class="fa-solid fa-layer-group"></i> ${escapeHtml(sec.name)}</span>
      <span style="display:flex; align-items:center; gap:6px; flex-wrap:wrap;">
        <span class="sim-sec-badge"><i class="fa-regular fa-clock"></i> ${durStr}</span>
        <span class="sim-sec-badge">${marks} Marks</span>
        ${calcBadge}
      </span>
    `;

    btn.onclick = () => switchSection(idx);
    container.appendChild(btn);
  });
}

// Render Navigation Pills (Fixed Position: Cover pill + Question Page pills)
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

  const calcRule = sec.isCalcAllowed
    ? '<strong>A calculator may be used.</strong> You must ensure your calculator meets official examination regulations.'
    : '<strong>You must NOT have a calculator</strong> or access to any calculating aid for this non-calculator section.';

  const isMaths = paper.subject === 'maths';
  const equipment = isMaths
    ? (sec.isCalcAllowed ? 'Pen (black or blue ink), HB pencil, eraser, ruler, calculator.' : 'Pen (black or blue ink), HB pencil, eraser, ruler. <em>Calculators prohibited.</em>')
    : 'Pen (black or blue ink), dictionary / spelling aid where permitted.';

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
            <li><strong>Time allowed:</strong> You have <strong>${durStr}</strong> to complete this section.</li>
            <li><strong>Total marks:</strong> The total mark for this section is <strong>${marks} marks</strong>.</li>
            <li><strong>Equipment:</strong> ${equipment}</li>
            <li><strong>Calculator policy:</strong> ${calcRule}</li>
            <li><strong>Show all working:</strong> Marks are awarded for your methods, calculations, and explanations. Record all intermediate working in the spaces provided.</li>
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
            <span>Section Questions:</span>
            <strong>${sec.questions.length} Questions (Q1 to Q${sec.questions.length})</strong>
          </div>

          <div class="sim-cover-declaration">
            <i class="fa-solid fa-shield-halved"></i>
            <span>Official Examination Environment &bull; Standard Assessment Regulations apply.</span>
          </div>

          <button type="button" class="sim-cover-start-btn" onclick="startSectionQuestions()">
            Open Section Examination Questions <i class="fa-solid fa-arrow-right"></i>
          </button>
        </div>
      </div>
    </div>
  `;

  // Update pills active state (Cover active)
  const pills = document.querySelectorAll('.sim-q-pill');
  pills.forEach((p, idx) => {
    p.classList.toggle('active', idx === 0);
  });

  // Prev / Next button state for Cover
  const prevBtn = document.getElementById('simPrevBtn');
  const nextBtn = document.getElementById('simNextBtn');
  if (prevBtn) {
    if (simCurrentSectionIndex > 0) {
      prevBtn.disabled = false;
      prevBtn.innerHTML = '<i class="fa-solid fa-arrow-left"></i> Return to Section A';
      prevBtn.onclick = () => {
        switchSection(simCurrentSectionIndex - 1, true);
      };
    } else {
      prevBtn.disabled = true;
      prevBtn.innerHTML = '<i class="fa-solid fa-arrow-left"></i> Previous';
      prevBtn.onclick = null;
    }
  }

  if (nextBtn) {
    nextBtn.disabled = false;
    nextBtn.innerHTML = 'Open Questions <i class="fa-solid fa-arrow-right"></i>';
    nextBtn.classList.remove('finish');
    nextBtn.onclick = () => startSectionQuestions();
  }
}

// Render Active Question
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
    prevBtn.disabled = false;
    prevBtn.onclick = () => prevQuestion();
    prevBtn.innerHTML = '<i class="fa-solid fa-arrow-left"></i> Previous';
  }

  if (nextBtn) {
    nextBtn.onclick = () => nextQuestion();
    if (simCurrentQuestionIndex < sec.questions.length) {
      nextBtn.innerHTML = 'Next <i class="fa-solid fa-arrow-right"></i>';
      nextBtn.classList.remove('finish');
    } else {
      if (simCurrentSectionIndex < sections.length - 1) {
        const nextSec = sections[simCurrentSectionIndex + 1];
        nextBtn.innerHTML = `Proceed to ${escapeHtml(nextSec.name)} <i class="fa-solid fa-arrow-right"></i>`;
        nextBtn.classList.remove('finish');
      } else {
        nextBtn.innerHTML = '<i class="fa-solid fa-flag-checkered"></i> Finish &amp; Review All';
        nextBtn.classList.add('finish');
      }
    }
  }
}

// Adapt UI for Subject Modes (Maths vs Writing vs Reading)
function adaptUiForSubject(paper, q, sec) {
  const subject = paper.subject || 'maths';
  const isCalcAllowed = sec ? sec.isCalcAllowed : !!q.isCalcAllowed;

  const mathToolbar = document.getElementById('simMathToolbar');
  const calcLockedBanner = document.getElementById('simCalcLockedBanner');
  const calcDrawer = document.getElementById('simCalcDrawer');
  const calcDrawerWrap = document.getElementById('simCalcDrawerWrap');
  const finalAnsCard = document.getElementById('simFinalAnsCard');

  const readingSourcePane = document.getElementById('simReadingSourcePane');
  const scenarioCard = document.getElementById('simScenarioCard');

  const planningBox = document.getElementById('simPlanningBox');
  const wordCountBadge = document.getElementById('simWordCountBadge');
  const writingChecklist = document.getElementById('simWritingChecklist');
  const workingTitleText = document.getElementById('simWorkingTitleText');
  const mcqContainer = document.getElementById('simMcqContainer');

  if (subject === 'writing') {
    if (mathToolbar) mathToolbar.style.display = 'none';
    if (calcLockedBanner) calcLockedBanner.style.display = 'none';
    if (calcDrawerWrap) calcDrawerWrap.style.display = 'none';
    if (calcDrawer) calcDrawer.style.display = 'none';
    if (finalAnsCard) finalAnsCard.style.display = 'none';
    if (readingSourcePane) readingSourcePane.style.display = 'none';
    if (scenarioCard) scenarioCard.style.display = 'block';

    if (planningBox) planningBox.style.display = 'block';
    if (wordCountBadge) wordCountBadge.style.display = 'inline-flex';
    if (writingChecklist) {
      writingChecklist.style.display = 'block';
      renderChecklist(q.checklist || [], sec);
    }
    if (workingTitleText) workingTitleText.innerText = 'Draft Your Written Response in the Spaces';
    if (mcqContainer) mcqContainer.style.display = 'none';

  } else if (subject === 'reading') {
    if (mathToolbar) mathToolbar.style.display = 'none';
    if (calcLockedBanner) calcLockedBanner.style.display = 'none';
    if (calcDrawerWrap) calcDrawerWrap.style.display = 'none';
    if (calcDrawer) calcDrawer.style.display = 'none';
    if (planningBox) planningBox.style.display = 'none';
    if (wordCountBadge) wordCountBadge.style.display = 'none';
    if (writingChecklist) writingChecklist.style.display = 'none';

    if (readingSourcePane && paper.sourceTexts && paper.sourceTexts.length > 0) {
      readingSourcePane.style.display = 'block';
      renderSourceTabs(paper.sourceTexts);
    } else {
      if (readingSourcePane) readingSourcePane.style.display = 'none';
    }

    if (workingTitleText) workingTitleText.innerText = 'Record Your Reading Comprehension Answer';

    if (q.expectedType === 'multiple-choice' && q.options) {
      if (mcqContainer) {
        mcqContainer.style.display = 'flex';
        renderMcqOptions(q.options, q.num, sec);
      }
      if (finalAnsCard) finalAnsCard.style.display = 'none';
    } else {
      if (mcqContainer) mcqContainer.style.display = 'none';
      if (finalAnsCard) finalAnsCard.style.display = 'flex';
    }

  } else {
    // MATHS MODE
    if (mathToolbar) mathToolbar.style.display = 'flex';
    if (finalAnsCard) finalAnsCard.style.display = 'flex';
    if (readingSourcePane) readingSourcePane.style.display = 'none';
    if (scenarioCard) scenarioCard.style.display = 'block';
    if (planningBox) planningBox.style.display = 'none';
    if (wordCountBadge) wordCountBadge.style.display = 'none';
    if (writingChecklist) writingChecklist.style.display = 'none';
    if (mcqContainer) mcqContainer.style.display = 'none';
    if (workingTitleText) workingTitleText.innerText = 'Type Your Working & Calculations in the Spaces';

    // Calculator Section Check (Docked side-by-side in Section B, completely hidden in Section A)
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
        calcDrawer.style.display = 'none'; // Completely disabled/hidden for Section A Non-Calc
        calcDrawer.classList.add('locked');
      }
    }
  }
}

// Source Tabs Renderer for Reading Exams
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

// Multiple Choice Option Renderer
function renderMcqOptions(options, qNum, sec) {
  const container = document.getElementById('simMcqContainer');
  if (!container) return;
  container.innerHTML = '';

  const secId = sec ? sec.id : 'A';
  const savedChoice = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_sec_${secId}_q${qNum}_ans`)
    || (secId === 'A' ? localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_q${qNum}_ans`) : '')
    || '';

  options.forEach((opt) => {
    const label = document.createElement('label');
    label.className = `sim-mcq-label ${savedChoice === opt ? 'selected' : ''}`;
    label.innerHTML = `
      <input type="radio" name="sim_mcq_q${qNum}" value="${escapeHtml(opt)}" ${savedChoice === opt ? 'checked' : ''} onchange="handleMcqSelect('${escapeHtml(opt)}', ${qNum})">
      <span>${escapeHtml(opt)}</span>
    `;
    container.appendChild(label);
  });
}

function handleMcqSelect(choice, qNum) {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const sections = getPaperSections(paper);
  const sec = sections[simCurrentSectionIndex] || sections[0];
  const secId = sec.id;

  localStorage.setItem(`mfs_sim_${simCurrentPaperKey}_sec_${secId}_q${qNum}_ans`, choice);
  const labels = document.querySelectorAll('.sim-mcq-label');
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

// Writing Checklist Renderer
function renderChecklist(items, sec) {
  const container = document.getElementById('simChecklistItems');
  if (!container) return;
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
  if (!textarea || !icon) return;

  if (textarea.style.display === 'none') {
    textarea.style.display = 'block';
    icon.className = 'fa-solid fa-chevron-up';
  } else {
    textarea.style.display = 'none';
    icon.className = 'fa-solid fa-chevron-down';
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
}

function toggleTimerPause() {
  simTimerActive = !simTimerActive;
  const icon = document.getElementById('simTimerPauseIcon');
  if (icon) {
    icon.className = simTimerActive ? 'fa-solid fa-pause' : 'fa-solid fa-play';
  }
}

// Fullscreen Management with clean Escape handling
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

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && document.fullscreenElement) {
    document.exitFullscreen().catch(() => {});
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

// Calculator Engine
function calcDigit(digit) {
  const screen = document.getElementById('simCalcScreen');
  if (calcWaitingForOperand) {
    calcCurrentVal = String(digit);
    calcWaitingForOperand = false;
  } else {
    calcCurrentVal = calcCurrentVal === '0' ? String(digit) : calcCurrentVal + digit;
  }
  screen.innerText = calcCurrentVal;
}

function calcDecimal() {
  const screen = document.getElementById('simCalcScreen');
  if (calcWaitingForOperand) {
    calcCurrentVal = '0.';
    calcWaitingForOperand = false;
  } else if (!calcCurrentVal.includes('.')) {
    calcCurrentVal += '.';
  }
  screen.innerText = calcCurrentVal;
}

function calcOp(op) {
  const screen = document.getElementById('simCalcScreen');
  const inputVal = parseFloat(calcCurrentVal);

  if (calcPendingOp && !calcWaitingForOperand) {
    calcCalculate();
  } else {
    calcMemory = inputVal;
  }

  calcPendingOp = op;
  calcWaitingForOperand = true;
}

function calcCalculate() {
  const screen = document.getElementById('simCalcScreen');
  const inputVal = parseFloat(calcCurrentVal);

  if (calcPendingOp === '+') calcMemory += inputVal;
  else if (calcPendingOp === '-') calcMemory -= inputVal;
  else if (calcPendingOp === '×') calcMemory *= inputVal;
  else if (calcPendingOp === '÷') calcMemory = inputVal !== 0 ? calcMemory / inputVal : 'Error';

  calcCurrentVal = String(calcMemory);
  calcPendingOp = null;
  calcWaitingForOperand = true;
  screen.innerText = calcCurrentVal;
}

function calcClear() {
  calcCurrentVal = '0';
  calcMemory = 0;
  calcPendingOp = null;
  calcWaitingForOperand = false;
  document.getElementById('simCalcScreen').innerText = '0';
}

function calcSqrt() {
  const val = parseFloat(calcCurrentVal);
  if (val >= 0) {
    calcCurrentVal = String(Math.sqrt(val));
    calcWaitingForOperand = true;
    document.getElementById('simCalcScreen').innerText = calcCurrentVal;
  }
}

// Submit Modal & Side-by-Side Model Solution Comparison
function openSubmitModal() {
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
  if (modal) modal.classList.add('open');
}

function closeSubmitModal() {
  const modal = document.getElementById('simSubmitModal');
  if (modal) modal.classList.remove('open');
}
