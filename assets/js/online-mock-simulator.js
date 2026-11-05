/**
 * Master Functional Skills - Online Mock Exam Simulator Engine
 * Comprehensive multi-subject support for Mathematics (Sec A & Sec B),
 * English Writing (Tasks with live word counter & proofreading), and
 * English Reading (Source Insert tabs & reading comprehension).
 */

// Global State
let simCurrentPaperKey = 'edexcel-maths-l1-paper-1';
let simCurrentQuestionIndex = 0;
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
    durationMinutes: 105,
    pdfUrl: 'https://passfunctionalskills.co.uk/app/uploads/2024/10/PAST_PAPER_1_FS_Maths_SecAB_PMAT1_N01_Level_1.pdf',
    modelSolutionPdf: 'assets/downloads/past-papers/edexcel/maths-level-1/FS_Maths_Level_1_Past_Paper_1_Model_Solution_MFS.pdf',
    videoSolutionSlug: '',
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
      },
      {
        num: 5,
        section: 'Section B: Calculator',
        isCalcAllowed: true,
        marks: 3,
        markTags: '[M1, A1, B1]',
        scenarioTitle: 'Cafe Drinks Ratio & Check',
        scenarioText: 'Johan works in a cafe. One morning he sells 48 cups of tea and 12 cups of coffee.',
        promptText: '(a) Write the ratio of the number of cups of tea to the number of cups of coffee in its simplest form.\n(b) Show a check of your answer.',
        unit: '',
        expectedType: 'text',
        modelSolution: '(a) Ratio Tea : Coffee = 48 : 12 [M1]\nDivide both by 12: 4 : 1 [A1]\n(b) Reverse check: 4 × 12 = 48 [B1]',
        finalBenchmark: '4 : 1'
      },
      {
        num: 6,
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
        num: 7,
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
        num: 8,
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
        num: 9,
        section: 'Section B: Calculator',
        isCalcAllowed: true,
        marks: 4,
        markTags: '[M1, A1, M1, A1]',
        scenarioTitle: 'Call Centre Daily Phone Calls Analysis',
        scenarioText: 'Kai works in a call centre. Phone calls received:\nMonday: 240, Tuesday: 140, Wednesday: 185, Thursday: 80, Friday: 225.',
        promptText: '(a) Work out the total number of calls received over the 5 days.\n(b) Work out the range of the number of phone calls.',
        unit: 'calls',
        expectedType: 'number',
        modelSolution: '(a) Total = 240 + 140 + 185 + 80 + 225 = 870 calls [M1, A1]\n(b) Range = Highest - Lowest = 240 - 80 = 160 calls [M1, A1]',
        finalBenchmark: '870 calls / Range: 160'
      },
      {
        num: 10,
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
        num: 11,
        section: 'Section B: Calculator',
        isCalcAllowed: true,
        marks: 4,
        markTags: '[M1, M1, M1, A1]',
        scenarioTitle: 'Cuboid Tomato Container Dimensions',
        scenarioText: 'Dennis is making a cuboid plant container with capacity 180 litres (1 litre = 1000 cm³). The height is 40 cm and width is 55 cm.',
        promptText: 'Work out the length of the container to the nearest whole centimetre.',
        unit: 'cm',
        expectedType: 'number',
        modelSolution: 'Step 1: Volume = 180 × 1000 = 180,000 cm³ [M1]\nStep 2: Base cross-section = 55 × 40 = 2,200 cm² [M1]\nStep 3: Length = 180,000 ÷ 2,200 = 81.818... cm [M1]\nStep 4: Round to nearest whole cm: 82 cm [A1]',
        finalBenchmark: '82 cm'
      },
      {
        num: 12,
        section: 'Section B: Calculator',
        isCalcAllowed: true,
        marks: 5,
        markTags: '[M1, M1, M1, A1, B1]',
        scenarioTitle: 'James House Purchase Deposit Calculation',
        scenarioText: 'James wants to buy a house priced at a quarter of a million pounds (£250,000). The deposit is 15%. James has £18,500 in savings and borrows £15,000 from family.',
        promptText: '(a) Does James have enough money to pay the deposit? Show working to support your decision.\n(b) Show a check of your percentage calculation.',
        unit: '£',
        expectedType: 'decision',
        modelSolution: '(a) Price = £250,000 [M1]\nDeposit = 0.15 × £250,000 = £37,500 [M1]\nJames\'s money = £18,500 + £15,000 = £33,500 [M1]\n£33,500 < £37,500 --> No, he is short by £4,000 [A1]\n(b) Check: 10% = £25,000; 5% = £12,500; £25,000 + £12,500 = £37,500 [B1]',
        finalBenchmark: 'No (short by £4,000)'
      }
    ]
  },

  // =========================================================================
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

  const subjectName = isWriting ? 'English Writing' : (isReading ? 'English Reading' : 'Mathematics');
  const levelName = key.includes('l2') || key.includes('level-2') ? 'Level 2' : 'Level 1';
  const paperNum = key.match(/paper-(\d+)/) ? key.match(/paper-(\d+)/)[1] : (key.match(/practice-(\d+)/) ? `Practice ${key.match(/practice-(\d+)/)[1]}` : '1');

  if (isWriting) {
    return {
      title: `Edexcel Functional Skills ${subjectName} ${levelName} — Paper ${paperNum}`,
      board: 'Pearson Edexcel',
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
    return {
      title: `Edexcel Functional Skills ${subjectName} ${levelName} — Paper ${paperNum}`,
      board: 'Pearson Edexcel',
      subject: 'reading',
      level: levelName,
      paperNumber: paperNum,
      durationMinutes: 60,
      sourceTexts: [
        { id: 'text-a', label: 'Text A', title: 'Text A: Informational Article', content: `Source Text A for Paper ${paperNum}.\nPlease consult the official Question Paper PDF if full text extraction is in progress.` },
        { id: 'text-b', label: 'Text B', title: 'Text B: Guidance Webpage', content: `Source Text B for Paper ${paperNum}.\nPlease consult the official Question Paper PDF if full text extraction is in progress.` }
      ],
      questions: [
        {
          num: 1,
          section: 'Reading Comprehension',
          isCalcAllowed: false,
          marks: 2,
          markTags: '[2 marks]',
          scenarioTitle: 'Text A Retrieval',
          scenarioText: 'Refer to Text A in the Source Booklet.',
          promptText: 'Identify two key facts or instructions provided in Text A.',
          unit: '',
          expectedType: 'text',
          modelSolution: 'Refer to official Pearson Edexcel mark scheme for verified answers.',
          finalBenchmark: 'Model Answer'
        }
      ]
    };
  }

  // Fallback to Maths Level 1 Paper 1
  return MFS_MOCK_DATA['edexcel-maths-l1-paper-1'];
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
});

// Load and Render Paper
function loadPaper(paperKey) {
  simCurrentPaperKey = paperKey;
  const paper = getOrCreatePaper(paperKey);
  simCurrentQuestionIndex = 0;

  // Header Title
  const titleDisplay = document.getElementById('simPaperTitleDisplay');
  if (titleDisplay) titleDisplay.innerText = paper.title;

  // Set Timer based on paper duration
  simTimerSeconds = (paper.durationMinutes || 60) * 60;
  updateTimerDisplay();

  // Render question pills
  renderQuestionPills(paper);

  // Render first question / task
  renderCurrentQuestion();
}

function handlePaperChange(newKey) {
  loadPaper(newKey);
}

// Render Navigation Pills
function renderQuestionPills(paper) {
  const container = document.getElementById('simPillsContainer');
  if (!container) return;
  container.innerHTML = '';

  paper.questions.forEach((q, idx) => {
    const pill = document.createElement('button');
    pill.type = 'button';
    pill.className = `sim-q-pill ${idx === simCurrentQuestionIndex ? 'active' : ''}`;
    
    // Label
    if (paper.subject === 'writing') {
      pill.innerText = `Task ${q.num}`;
    } else {
      pill.innerText = `Q${q.num}`;
    }

    // Check saved state
    const saved = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_q${q.num}_working`);
    if (saved && saved.trim().length > 0) {
      pill.classList.add('answered');
    }

    pill.onclick = () => jumpToQuestion(idx);
    container.appendChild(pill);
  });
}

// Render Active Question
function renderCurrentQuestion() {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const q = paper.questions[simCurrentQuestionIndex];
  if (!q) return;

  const subject = paper.subject || 'maths';

  // Meta Badges
  const qNumBadge = document.getElementById('simQNumBadge');
  const qSectionTag = document.getElementById('simQSectionTag');
  const qMarksBadge = document.getElementById('simQMarksBadge');

  if (subject === 'writing') {
    if (qNumBadge) qNumBadge.innerText = `Task ${q.num} of ${paper.questions.length}`;
    if (qSectionTag) qSectionTag.innerText = q.section || 'Written Composition & SPaG';
    if (qMarksBadge) qMarksBadge.innerText = `${q.marks} Marks • ${q.markTags || ''}`;
  } else if (subject === 'reading') {
    if (qNumBadge) qNumBadge.innerText = `Question ${q.num} of ${paper.questions.length}`;
    if (qSectionTag) qSectionTag.innerText = q.section || 'Reading Comprehension';
    if (qMarksBadge) qMarksBadge.innerText = `${q.marks} Mark${q.marks > 1 ? 's' : ''}`;
  } else {
    if (qNumBadge) qNumBadge.innerText = `Question ${q.num} of ${paper.questions.length}`;
    if (qSectionTag) qSectionTag.innerText = q.section;
    if (qMarksBadge) qMarksBadge.innerText = `${q.marks} Marks • ${q.markTags || ''}`;
  }

  // Scenario
  const scenTitle = document.getElementById('simScenarioTitle');
  const scenText = document.getElementById('simScenarioText');
  if (scenTitle) scenTitle.innerHTML = `<i class="fa-solid fa-file-circle-check" style="color:var(--sim-blue);"></i> ${q.scenarioTitle}`;
  if (scenText) scenText.innerText = q.scenarioText;

  // Prompt
  const promptText = document.getElementById('simPromptText');
  if (promptText) promptText.innerText = q.promptText;

  // Mode Specific UI Adaptations
  adaptUiForSubject(paper, q);

  // Restore User Working & Answers
  const userWorking = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_q${q.num}_working`) || '';
  const textarea = document.getElementById('simWorkingTextarea');
  if (textarea) textarea.value = userWorking;

  const userAns = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_q${q.num}_ans`) || '';
  const finalInput = document.getElementById('simFinalInput');
  if (finalInput) finalInput.value = userAns;

  // Update Word Counter in Writing Mode
  if (subject === 'writing') {
    updateWordCount(userWorking, q.targetWords);
  }

  // Unit Badge
  const unitBadge = document.getElementById('simUnitBadge');
  if (unitBadge) {
    unitBadge.innerText = q.unit || '';
    unitBadge.style.display = q.unit ? 'inline-flex' : 'none';
  }

  // Update Pills active state
  const pills = document.querySelectorAll('.sim-q-pill');
  pills.forEach((p, idx) => {
    p.classList.toggle('active', idx === simCurrentQuestionIndex);
  });

  // Prev / Next button state
  const prevBtn = document.getElementById('simPrevBtn');
  const nextBtn = document.getElementById('simNextBtn');
  if (prevBtn) prevBtn.disabled = simCurrentQuestionIndex === 0;
  if (nextBtn) {
    if (simCurrentQuestionIndex === paper.questions.length - 1) {
      nextBtn.innerHTML = '<i class="fa-solid fa-flag-checkered"></i> Finish &amp; Review';
      nextBtn.classList.add('finish');
    } else {
      nextBtn.innerHTML = 'Next <i class="fa-solid fa-arrow-right"></i>';
      nextBtn.classList.remove('finish');
    }
  }
}

// Adapt UI for Subject Modes (Maths vs Writing vs Reading)
function adaptUiForSubject(paper, q) {
  const subject = paper.subject || 'maths';

  const mathToolbar = document.getElementById('simMathToolbar');
  const calcLockedBanner = document.getElementById('simCalcLockedBanner');
  const calcDrawer = document.getElementById('simCalcDrawer');
  const finalAnsCard = document.getElementById('simFinalAnsCard');

  const readingSourcePane = document.getElementById('simReadingSourcePane');
  const scenarioCard = document.getElementById('simScenarioCard');

  const planningBox = document.getElementById('simPlanningBox');
  const wordCountBadge = document.getElementById('simWordCountBadge');
  const writingChecklist = document.getElementById('simWritingChecklist');
  const workingTitleText = document.getElementById('simWorkingTitleText');
  const mcqContainer = document.getElementById('simMcqContainer');

  if (subject === 'writing') {
    // WRITING MODE
    if (mathToolbar) mathToolbar.style.display = 'none';
    if (calcLockedBanner) calcLockedBanner.style.display = 'none';
    if (calcDrawer) calcDrawer.style.display = 'none';
    if (finalAnsCard) finalAnsCard.style.display = 'none';
    if (readingSourcePane) readingSourcePane.style.display = 'none';
    if (scenarioCard) scenarioCard.style.display = 'block';

    if (planningBox) planningBox.style.display = 'block';
    if (wordCountBadge) wordCountBadge.style.display = 'inline-flex';
    if (writingChecklist) {
      writingChecklist.style.display = 'block';
      renderChecklist(q.checklist || []);
    }
    if (workingTitleText) workingTitleText.innerText = 'Draft Your Written Response in the Spaces';
    if (mcqContainer) mcqContainer.style.display = 'none';

  } else if (subject === 'reading') {
    // READING MODE
    if (mathToolbar) mathToolbar.style.display = 'none';
    if (calcLockedBanner) calcLockedBanner.style.display = 'none';
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

    // Handle Multiple Choice vs Open Text
    if (q.expectedType === 'multiple-choice' && q.options) {
      if (mcqContainer) {
        mcqContainer.style.display = 'flex';
        renderMcqOptions(q.options, q.num);
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

    // Calculator Section Check
    if (q.isCalcAllowed) {
      if (calcLockedBanner) calcLockedBanner.style.display = 'none';
      if (calcDrawer) {
        calcDrawer.style.display = 'block';
        calcDrawer.classList.remove('locked');
      }
    } else {
      if (calcLockedBanner) calcLockedBanner.style.display = 'flex';
      if (calcDrawer) {
        calcDrawer.style.display = 'block';
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
    btn.innerHTML = `<i class="fa-regular fa-file-lines"></i> ${txt.label || txt.title}`;
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
function renderMcqOptions(options, qNum) {
  const container = document.getElementById('simMcqContainer');
  if (!container) return;
  container.innerHTML = '';

  const savedChoice = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_q${qNum}_ans`) || '';

  options.forEach((opt) => {
    const label = document.createElement('label');
    label.className = `sim-mcq-label ${savedChoice === opt ? 'selected' : ''}`;
    label.innerHTML = `
      <input type="radio" name="sim_mcq_q${qNum}" value="${opt}" ${savedChoice === opt ? 'checked' : ''} onchange="handleMcqSelect('${opt}', ${qNum})">
      <span>${opt}</span>
    `;
    container.appendChild(label);
  });
}

function handleMcqSelect(choice, qNum) {
  localStorage.setItem(`mfs_sim_${simCurrentPaperKey}_q${qNum}_ans`, choice);
  const labels = document.querySelectorAll('.sim-mcq-label');
  labels.forEach(l => {
    const radio = l.querySelector('input');
    l.classList.toggle('selected', radio && radio.checked);
  });
  indicateSaveStatus();
}

// Writing Checklist Renderer
function renderChecklist(items) {
  const container = document.getElementById('simChecklistItems');
  if (!container) return;
  container.innerHTML = '';

  const paper = getOrCreatePaper(simCurrentPaperKey);
  const qNum = paper.questions[simCurrentQuestionIndex].num;

  items.forEach((item, idx) => {
    const saved = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_q${qNum}_chk_${idx}`) === '1';
    const row = document.createElement('label');
    row.className = 'sim-checklist-item';
    row.innerHTML = `
      <input type="checkbox" ${saved ? 'checked' : ''} onchange="handleChecklistToggle(${idx}, this.checked)">
      <span>${item}</span>
    `;
    container.appendChild(row);
  });
}

function handleChecklistToggle(idx, checked) {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const qNum = paper.questions[simCurrentQuestionIndex].num;
  localStorage.setItem(`mfs_sim_${simCurrentPaperKey}_q${qNum}_chk_${idx}`, checked ? '1' : '0');
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
  const qNum = paper.questions[simCurrentQuestionIndex].num;
  localStorage.setItem(`mfs_sim_${simCurrentPaperKey}_q${qNum}_planning`, val);
  indicateSaveStatus();
}

// Navigation Handlers
function nextQuestion() {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  if (simCurrentQuestionIndex < paper.questions.length - 1) {
    simCurrentQuestionIndex++;
    renderCurrentQuestion();
    window.scrollTo({ top: 120, behavior: 'smooth' });
  } else {
    openSubmitModal();
  }
}

function prevQuestion() {
  if (simCurrentQuestionIndex > 0) {
    simCurrentQuestionIndex--;
    renderCurrentQuestion();
    window.scrollTo({ top: 120, behavior: 'smooth' });
  }
}

function jumpToQuestion(index) {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  if (index >= 0 && index < paper.questions.length) {
    simCurrentQuestionIndex = index;
    renderCurrentQuestion();
    window.scrollTo({ top: 120, behavior: 'smooth' });
  }
}

// Input Handlers
function handleWorkingInput(val) {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const qNum = paper.questions[simCurrentQuestionIndex].num;
  localStorage.setItem(`mfs_sim_${simCurrentPaperKey}_q${qNum}_working`, val);

  // Update pill answered status
  const pills = document.querySelectorAll('.sim-q-pill');
  if (pills[simCurrentQuestionIndex]) {
    pills[simCurrentQuestionIndex].classList.toggle('answered', val.trim().length > 0);
  }

  // Update word counter if writing
  if (paper.subject === 'writing') {
    updateWordCount(val, paper.questions[simCurrentQuestionIndex].targetWords);
  }

  indicateSaveStatus();
}

function handleAnswerInput(val) {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const qNum = paper.questions[simCurrentQuestionIndex].num;
  localStorage.setItem(`mfs_sim_${simCurrentPaperKey}_q${qNum}_ans`, val);
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
  const qNum = paper.questions[simCurrentQuestionIndex].num;
  const isFlagged = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_q${qNum}_flagged`) === '1';

  if (isFlagged) {
    localStorage.setItem(`mfs_sim_${simCurrentPaperKey}_q${qNum}_flagged`, '0');
    if (btn) btn.classList.remove('flagged');
  } else {
    localStorage.setItem(`mfs_sim_${simCurrentPaperKey}_q${qNum}_flagged`, '1');
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

// Countdown Timer
function startTimer() {
  if (simTimerInterval) clearInterval(simTimerInterval);
  simTimerInterval = setInterval(() => {
    if (simTimerActive && simTimerSeconds > 0) {
      simTimerSeconds--;
      updateTimerDisplay();
    }
  }, 1000);
}

function updateTimerDisplay() {
  const disp = document.getElementById('simTimerDisplay');
  if (!disp) return;

  const mins = Math.floor(simTimerSeconds / 60);
  const secs = simTimerSeconds % 60;
  disp.innerText = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;

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

// Fullscreen
function toggleSimFullscreen() {
  const shell = document.getElementById('simAppShell');
  if (!document.fullscreenElement) {
    if (shell.requestFullscreen) shell.requestFullscreen();
    shell.classList.add('fullscreen');
  } else {
    if (document.exitFullscreen) document.exitFullscreen();
    shell.classList.remove('fullscreen');
  }
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
  const container = document.getElementById('simReviewList');
  container.innerHTML = '';

  paper.questions.forEach((q) => {
    const userWorking = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_q${q.num}_working`) || '(No response entered)';
    const userAns = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_q${q.num}_ans`) || '';

    const row = document.createElement('div');
    row.className = 'sim-review-row';

    const itemLabel = paper.subject === 'writing' ? `Task ${q.num}` : `Question ${q.num}`;

    row.innerHTML = `
      <div>
        <div class="sim-review-col-title" style="color:var(--sim-navy);">
          <i class="fa-solid fa-user-pen" style="color:var(--sim-blue);"></i> ${itemLabel}: Your Response &amp; Working
        </div>
        <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:6px; padding:10px; font-size:0.85rem; font-family:'Courier New', monospace; white-space:pre-wrap; min-height:80px; margin-bottom:8px;">${userWorking}</div>
        ${userAns ? `
        <div style="font-size:0.9rem; font-weight:800; color:var(--sim-navy);">
          Your Concluded Answer: <span style="background:#e0f2fe; padding:2px 8px; border-radius:4px; color:#0369a1;">${userAns} ${q.unit || ''}</span>
        </div>` : ''}
      </div>
      <div>
        <div class="sim-review-col-title" style="color:var(--sim-emerald);">
          <i class="fa-solid fa-award" style="color:var(--sim-green);"></i> Accredited Master Model &amp; Mark Scheme [${q.markTags || ''}]
        </div>
        <div style="background:#f0fdf4; border:1px solid #86efac; border-radius:6px; padding:10px; font-size:0.85rem; font-family:'Courier New', monospace; white-space:pre-wrap; min-height:80px; margin-bottom:8px; color:#14532d;">${q.modelSolution}</div>
        <div style="font-size:0.9rem; font-weight:800; color:#15803d;">
          Model Benchmark: <span style="background:#dcfce7; padding:2px 8px; border-radius:4px;">${q.finalBenchmark}</span>
        </div>
      </div>
    `;
    container.appendChild(row);
  });

  // Watch Walkthrough button
  const videoBtn = document.getElementById('simModalWatchVideoBtn');
  if (paper.videoSolutionSlug) {
    videoBtn.style.display = 'inline-flex';
    videoBtn.href = `video-solution.html?topic=${paper.videoSolutionSlug}`;
  } else {
    videoBtn.style.display = 'none';
  }

  // Open modal
  document.getElementById('simSubmitModal').classList.add('open');
}

function closeSubmitModal() {
  document.getElementById('simSubmitModal').classList.remove('open');
}
