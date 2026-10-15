# spag_content_e3.py
# ==============================================================================
# Master Functional Skills English: Entry Level 3 SPaG Curriculum
# Mapped strictly to Ofqual Entry Level 3 Functional Skills English Subject Content
# Follows the Raymond Murphy 'Grammar in Use' Two-Page Spread Architectural Schema
#
# Design Standards:
# - Dyslexia-friendly: warm cream tint (#FDFBF7), deep slate text (#1F2937),
#   ragged-right alignment (no justification), generous leading (line-height 1.55),
#   accessible visual chunking cards with left accent borders:
#     * Rule / Context: Sky Blue tint (#F0F9FF, border: #0284C7)
#     * Correct Model: Mint tint (#F0FDF4, border: #16A34A)
#     * Pitfall / Contrast: Rose tint (#FEF2F2, border: #DC2626)
#     * Golden Rule / Memory Hook: Amber tint (#FEFCE8, border: #D97706)
# - Two-Page Facing Spread Architecture:
#     * Left Page: Situational Anchor [A], Structural Formula [B],
#                  Compare & Contrast [C], Golden Rule Memory Hook [D]
#     * Right Page: Exercise 1 (Recognition/Discrimination),
#                   Exercise 2 (Cloze/Sentence Completion),
#                   Exercise 3 (Forensic Proofreading with authentic workplace scenario),
#                   Exercise 4 (Applied Functional Writing Prompt)
# ==============================================================================

E3_UNITS = [
    {
        "unit": 1,
        "format": "Personal Details Form / Postcard",
        "title": "Capital Letters for 'I', Names, Places, Days & Months",
        "subtitle": "Filling in Enrolment Forms & Writing Holiday Postcards",
        "rule_title": "Core Grammar Rule: When Must You Use a Capital Letter?",
        "rule_text": """<div style="background:#f0f9ff; border-left:4px solid #0284c7; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#0369a1; font-size:9.5pt;">[A] Situational Anchor: Enrolment Forms &amp; Friendly Postcards</strong><br>
When you fill in an official enrolment form at college, sign up for a training course, or write a postcard to a friend, capital letters show where names, dates, and sentences begin. Without them, forms are rejected and messages are confusing to read.
</div>

<div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#15803d; font-size:9.5pt;">[B] Syntax Architecture: The 5 Rules for Capital Letters</strong>
<ul style="margin:4px 0 0 16px; padding:0;">
  <li><strong>1. The Personal Pronoun 'I':</strong> Always capitalised when talking about yourself (e.g. <em>"Today <strong>I</strong> started my new job."</em> &mdash; never a small 'i').</li>
  <li><strong>2. Names of People:</strong> First names and surnames (e.g. <em><strong>S</strong>arah <strong>J</strong>enkins</em>, <em><strong>D</strong>r <strong>A</strong>hmed</em>).</li>
  <li><strong>3. Names of Places &amp; Streets:</strong> Towns, cities, roads, and shops (e.g. <em><strong>L</strong>ondon</em>, <em><strong>H</strong>igh <strong>S</strong>treet</em>, <em><strong>T</strong>esco</em>).</li>
  <li><strong>4. Days of the Week:</strong> <em><strong>M</strong>onday, <strong>T</strong>uesday, <strong>W</strong>ednesday, <strong>T</strong>hursday, <strong>F</strong>riday, <strong>S</strong>aturday, <strong>S</strong>unday</em>.</li>
  <li><strong>5. Months of the Year:</strong> <em><strong>J</strong>anuary, <strong>F</strong>ebruary, <strong>M</strong>arch, <strong>A</strong>pril, <strong>M</strong>ay, <strong>J</strong>une, <strong>J</strong>uly, <strong>A</strong>ugust, <strong>S</strong>eptember, <strong>O</strong>ctober, <strong>N</strong>ovember, <strong>D</strong>ecember</em>.</li>
  <li><strong>6. Sentence Starters:</strong> The very first letter of every new sentence.</li>
</ul>
</div>

<div style="background:#fef2f2; border-left:4px solid #dc2626; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#b91c1c; font-size:9.5pt;">[C] Compare &amp; Contrast: Common Pitfalls</strong><br>
<span style="color:#dc2626; font-weight:bold;">Incorrect:</span> <em>on friday i met mr ahmed in birmingham.</em><br>
<span style="color:#16a34a; font-weight:bold;">Correct:</span> <em><strong>O</strong>n <strong>F</strong>riday, <strong>I</strong> met <strong>M</strong>r <strong>A</strong>hmed in <strong>B</strong>irmingham.</em><br>
<span style="color:#4b5563; font-size:8pt;"><strong>Why:</strong> 'On' starts the sentence; 'Friday' is a day; 'I' is the pronoun; 'Mr Ahmed' is a name; 'Birmingham' is a place.</span>
</div>

<div style="background:#fefce8; border-left:4px solid #d97706; padding:8px 12px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#b45309; font-size:9.5pt;">[D] Golden Rule &amp; Memory Hook: Remember 'MINTS'</strong><br>
<strong>M</strong> &rarr; <strong>M</strong>onths (<em>March, July</em>)<br>
<strong>I</strong> &rarr; The letter <strong>'I'</strong> (<em>I am learning</em>)<br>
<strong>N</strong> &rarr; <strong>N</strong>ames of people and places (<em>David, Bristol</em>)<br>
<strong>T</strong> &rarr; <strong>T</strong>itles of people and streets (<em>Mr, Mrs, Queen Street</em>)<br>
<strong>S</strong> &rarr; <strong>S</strong>tart of every sentence (<em><strong>T</strong>he course starts tomorrow.</em>)
</div>""",
        "format_link": "On personal details forms and postcards, missing capital letters makes your writing look careless and causes official records to have errors.",
        "worked_bad": "last friday i visited leeds with uncle david. we had lunch on queen street.",
        "worked_good": "Last Friday, I visited Leeds with Uncle David. We had lunch on Queen Street.",
        "worked_why": "Capitalised 'Last' and 'We' (sentence starts), 'Friday' (day), 'I' (pronoun), 'Leeds' (city), 'Uncle David' (title and name), and 'Queen Street' (street name).",
        "exercise_a": [
            ("Which sentence capitalises the personal pronoun 'I' correctly?",
             ["A) When i finish work, i walk home.",
              "B) When I finish work, I walk home.",
              "C) When I finish work, i walk home."],
             "B"),
            ("Which sentence capitalises days of the week and months correctly?",
             ["A) The dental clinic is open every tuesday in november.",
              "B) The dental clinic is open every Tuesday in November.",
              "C) The dental clinic is open every Tuesday in november."],
             "B"),
            ("Which personal details entry capitalises town and street names correctly?",
             ["A) 24 High Street, Manchester, M4 1AB",
              "B) 24 high street, manchester, M4 1AB",
              "C) 24 High street, Manchester, M4 1AB"],
             "A"),
            ("Choose the sentence that uses correct capital letters throughout:",
             ["A) on wednesday, amir and I travelled to bristol.",
              "B) On Wednesday, Amir and I travelled to Bristol.",
              "C) On wednesday, Amir and i travelled to Bristol."],
             "B")
        ],
        "proofreading_title": "Format 1 Applied Proofreading: Adult Education Enrolment Form",
        "proofreading_scenario": "A learner filled in this notes section on a college registration form. There are <strong>5 capital letter errors</strong>.",
        "proofreading_text": """<div style="background:#ffffff; border:1px solid #cbd5e1; padding:8px 12px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; font-size:8.5pt; line-height:1.5; color:#1f2937;">
<p style="margin:0 0 6px 0;"><strong>Applicant Name:</strong> mark stevens | <strong>Course:</strong> Customer Service Skills</p>
<p style="margin:0 0 6px 0;">i am writing to confirm my place on the evening course. My manager at tesco suggested this training to improve my workplace communication.</p>
<p style="margin:0;">Can i attend the induction session in leeds on thursday 15 October?</p>
</div>""",
        "proofreading_errors": [
            "Missing capital letters in applicant name ('mark stevens' -> 'Mark Stevens')",
            "Missing capital letter on pronoun at start of sentence ('i am writing' -> 'I am writing')",
            "Missing capital letter for business proper noun ('tesco' -> 'Tesco')",
            "Missing capital letter on pronoun in question ('Can i attend' -> 'Can I attend')",
            "Missing capital letters for place and day ('leeds on thursday' -> 'Leeds on Thursday')"
        ],
        "writing_prompt": "Write <strong>two complete sentences</strong> for a postcard to a friend about a weekend trip. Include the name of a town, a day of the week, and the pronoun 'I' with 100% accurate capital letters."
    },
    {
        "unit": 2,
        "format": "Community Notice / Information Flyer",
        "title": "Full Stops & Question Marks: Statements vs Questions",
        "subtitle": "Writing Clear Notices for Community Boards & Leaflets",
        "rule_title": "Core Grammar Rule: How to End a Sentence: Statement or Question?",
        "rule_text": """<div style="background:#f0f9ff; border-left:4px solid #0284c7; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#0369a1; font-size:9.5pt;">[A] Situational Anchor: Community Centre Notices</strong><br>
Community notices give vital information to residents. Some sentences state facts (e.g. library opening hours), while others ask readers for their help or opinions. Every sentence must end with the correct punctuation mark so the reader knows whether to take in a fact or answer a question.
</div>

<div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#15803d; font-size:9.5pt;">[B] Syntax Architecture: Statements vs Questions</strong>
<ul style="margin:4px 0 0 16px; padding:0;">
  <li><strong>Statement (Tells a fact):</strong> Ends with a <strong>Full Stop (.)</strong>.<br>
      <code>[Subject] + [Verb] + [Fact / Details] + [ . ]</code><br>
      <em>Example: The community garden opens at 10:00 AM on Saturday.</em></li>
  <li><strong>Question (Asks for information):</strong> Ends with a <strong>Question Mark (?)</strong>.<br>
      <code>[Question Word: Who/What/Where/When/Why/How or Auxiliary: Can/Do/Are/Is] + [Subject] + [Verb] + [ ? ]</code><br>
      <em>Example: Would you like to volunteer as a gardener?</em></li>
</ul>
</div>

<div style="background:#fef2f2; border-left:4px solid #dc2626; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#b91c1c; font-size:9.5pt;">[C] Compare &amp; Contrast: Standard vs Confused Punctuation</strong><br>
<span style="color:#dc2626; font-weight:bold;">Incorrect:</span> <em>Can you attend the neighbourhood meeting. All residents are welcome?</em><br>
<span style="color:#16a34a; font-weight:bold;">Correct:</span> <em>Can you attend the neighbourhood meeting? All residents are welcome.</em><br>
<span style="color:#4b5563; font-size:8pt;"><strong>Why:</strong> The first sentence asks a direct question (needs '?'). The second sentence tells a fact (needs '.').</span>
</div>

<div style="background:#fefce8; border-left:4px solid #d97706; padding:8px 12px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#b45309; font-size:9.5pt;">[D] Golden Rule &amp; Memory Hook</strong><br>
If your voice rises at the end because you expect an answer, it is a <strong>question (?)</strong>.<br>
If your sentence gives information and finishes a thought, it is a <strong>statement (.)</strong>.<br>
<em>Never put a full stop and question mark together (.?)!</em>
</div>""",
        "format_link": "In community notices, mixing up full stops and question marks confuses residents about whether an event is confirmed or if their response is required.",
        "worked_bad": "The health centre offers free flu jabs. Do you want to protect your family.",
        "worked_good": "The health centre offers free flu jabs. Do you want to protect your family?",
        "worked_why": "The second sentence begins with the auxiliary verb 'Do' and asks for information, so it requires a question mark (?).",
        "exercise_a": [
            ("Which sentence is a question that requires a question mark?",
             ["A) The library offers free computer access",
              "B) Where can I register for computer classes",
              "C) You can book an appointment at the main desk"],
             "B"),
            ("Which sentence is a statement that requires a full stop?",
             ["A) How many people can attend the workshop",
              "B) Can you bring your own laptop tomorrow",
              "C) The workshop takes place in Room 4"],
             "C"),
            ("Choose the correctly punctuated sentence pair for a community flyer:",
             ["A) Are you looking for part-time work? We have five new vacancies.",
              "B) Are you looking for part-time work. We have five new vacancies?",
              "C) Are you looking for part-time work? We have five new vacancies?"],
             "A"),
            ("Identify the sentence with the correct end punctuation:",
             ["A) Do you need help with your council tax form.",
              "B) Do you need help with your council tax form?",
              "C) Do you need help with your council tax form!?"],
             "B")
        ],
        "proofreading_title": "Format 2 Applied Proofreading: Community Library Notice",
        "proofreading_scenario": "A volunteer prepared this flyer for the community centre noticeboard. There are <strong>5 punctuation errors</strong> (missing or swapped full stops and question marks).",
        "proofreading_text": """<div style="background:#ffffff; border:1px solid #cbd5e1; padding:8px 12px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; font-size:8.5pt; line-height:1.5; color:#1f2937;">
<h4 style="margin:0 0 6px 0; color:#0369a1;">Riverside Community Hub &bull; Free Digital Skills Club</h4>
<p style="margin:0 0 6px 0;">Do you want to learn how to use a smartphone or tablet.</p>
<p style="margin:0 0 6px 0;">Our friendly volunteers run drop-in sessions every Wednesday afternoon? You do not need any previous computer experience</p>
<p style="margin:0;">Would you like to reserve a space today. Refreshments are provided free of charge?</p>
</div>""",
        "proofreading_errors": [
            "Question ends with a full stop ('or tablet.' -> 'or tablet?')",
            "Statement ends with a question mark ('Wednesday afternoon?' -> 'Wednesday afternoon.')",
            "Missing full stop at end of sentence ('computer experience' -> 'computer experience.')",
            "Question ends with a full stop ('a space today.' -> 'a space today?')",
            "Statement ends with a question mark ('free of charge?' -> 'free of charge.')"
        ],
        "writing_prompt": "Write <strong>two sentences</strong> for a community board notice about a sports club. Write one statement stating when the club meets (ending with a full stop) and one question asking residents if they would like to join (ending with a question mark)."
    },
    {
        "unit": 3,
        "format": "Safety Sign / Workplace Instructions",
        "title": "Exclamation Marks & Urgent Instructions",
        "subtitle": "Writing Clear Warning Signs & Kitchen Hygiene Rules",
        "rule_title": "Core Grammar Rule: Exclamation Marks for Danger & Imperatives for Steps",
        "rule_text": """<div style="background:#f0f9ff; border-left:4px solid #0284c7; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#0369a1; font-size:9.5pt;">[A] Situational Anchor: Workplace Safety &amp; Kitchen Rules</strong><br>
In kitchens, warehouses, and care homes, clear safety instructions prevent injuries. Urgent warnings need exclamation marks to alert staff instantly. Step-by-step instructions use imperative (bossy) verbs so staff know exactly what actions to take.
</div>

<div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#15803d; font-size:9.5pt;">[B] Syntax Architecture: Warnings vs Imperatives</strong>
<ul style="margin:4px 0 0 16px; padding:0;">
  <li><strong>Urgent Danger / Emergency:</strong> Ends with an <strong>Exclamation Mark (!)</strong>.<br>
      <code>[Urgent Hazard / Caution Word] + [ ! ]</code><br>
      <em>Examples: Danger! Wet floor! &bull; Stop! Forklift trucks in operation!</em></li>
  <li><strong>Routine Workplace Instruction (Command):</strong> Starts with an <strong>Imperative Verb</strong> and ends with a <strong>Full Stop (.)</strong>.<br>
      <code>[Base Action Verb: Wash / Wear / Keep / Turn off] + [Object / Instruction] + [ . ]</code><br>
      <em>Examples: Wash your hands before touching food. &bull; Wear protective boots in the warehouse.</em></li>
</ul>
</div>

<div style="background:#fef2f2; border-left:4px solid #dc2626; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#b91c1c; font-size:9.5pt;">[C] Compare &amp; Contrast: Overuse of Exclamation Marks</strong><br>
<span style="color:#dc2626; font-weight:bold;">Incorrect:</span> <em>Please wipe the counter! Put knives in the drawer! Wear an apron!</em><br>
<span style="color:#16a34a; font-weight:bold;">Correct:</span> <em>Caution! Sharp knives! Wipe the counter with sanitiser. Store knives in the secure drawer.</em><br>
<span style="color:#4b5563; font-size:8pt;"><strong>Why:</strong> Exclamation marks are for genuine hazards or emergencies. Overusing them on normal steps makes instructions stressful and unreadable.</span>
</div>

<div style="background:#fefce8; border-left:4px solid #d97706; padding:8px 12px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#b45309; font-size:9.5pt;">[D] Golden Rule &amp; Memory Hook</strong><br>
Reserve exclamation marks (<strong>!</strong>) for <strong>real emergencies, hazards, and urgent commands</strong>.<br>
For regular workplace tasks, start with an imperative verb (<em>Clean, Check, Store</em>) and end with a calm <strong>full stop (.)</strong>.
</div>""",
        "format_link": "Workplace safety notices must be clear and direct. Misplaced exclamation marks weaken critical emergency warnings, while missing full stops make procedures hard to follow.",
        "worked_bad": "fire exit do not block! keep corridors clear at all times!",
        "worked_good": "Warning! Fire exit! Keep corridors clear at all times.",
        "worked_why": "Used exclamation marks for the urgent emergency warning and an imperative sentence with a full stop for the daily maintenance instruction.",
        "exercise_a": [
            ("Which sentence is an urgent safety warning that correctly uses an exclamation mark?",
             ["A) Watch out! The metal surface is extremely hot!",
              "B) The metal surface is hot today.",
              "C) Please wipe the metal surface with a cloth."],
             "A"),
            ("Which sentence is a workplace instruction starting with an imperative verb?",
             ["A) You might want to switch off the computer.",
              "B) Switch off the computer at the end of your shift.",
              "C) Switching off computers is very helpful."],
             "B"),
            ("Choose the correctly punctuated safety rule for a workshop:",
             ["A) Danger! Eye protection must be worn in this area.",
              "B) Danger? Eye protection must be worn in this area?",
              "C) Danger eye protection must be worn in this area!"],
             "A"),
            ("Identify the imperative verb in: <em>'Sanitise all food prep surfaces before lunch.'</em>",
             ["A) surfaces", "B) prep", "C) Sanitise"],
             "C")
        ],
        "proofreading_title": "Format 3 Applied Proofreading: Commercial Kitchen Safety Poster",
        "proofreading_scenario": "A head chef wrote this hygiene and safety sign for the restaurant kitchen. There are <strong>5 SPaG errors</strong> involving exclamation marks, imperatives, and capital letters.",
        "proofreading_text": """<div style="background:#ffffff; border:1px solid #cbd5e1; padding:8px 12px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; font-size:8.5pt; line-height:1.5; color:#1f2937;">
<h4 style="margin:0 0 6px 0; color:#b91c1c;">KITCHEN SAFETY &amp; HYGIENE RULES</h4>
<p style="margin:0 0 6px 0;">danger! Deep fat fryer reaches 180&deg;C.</p>
<p style="margin:0 0 6px 0;">Wash your hands with soap before touching raw chicken! Keep raw meat on the bottom shelf of the fridge!</p>
<p style="margin:0;">clean all stainless steel worktops after every shift! report any broken equipment to chef marco immediately?</p>
</div>""",
        "proofreading_errors": [
            "Missing capital letter on urgent hazard ('danger!' -> 'Danger!')",
            "Routine hygiene step should end with full stop, not exclamation mark ('raw chicken!' -> 'raw chicken.')",
            "Routine storage rule should end with full stop, not exclamation mark ('of the fridge!' -> 'of the fridge.')",
            "Missing capital letter at start of imperative sentence ('clean all' -> 'Clean all')",
            "Instruction ends with incorrect question mark ('chef marco immediately?' -> 'Chef Marco immediately.')"
        ],
        "writing_prompt": "Write <strong>two sentences</strong> for a safety notice in a retail stockroom. Write one urgent warning using an exclamation mark (e.g. <em>Caution! Falling boxes!</em>) and one clear instruction starting with an imperative verb (e.g. <em>Stack...</em> or <em>Store...</em>) ending with a full stop."
    },
    {
        "unit": 4,
        "format": "Short Note to Colleague / Handover Message",
        "title": "Joining Sentences with 'And' & 'But'",
        "subtitle": "Writing Compound Sentences for Smooth Workplace Handovers",
        "rule_title": "Core Grammar Rule: Connecting Ideas with 'And' and 'But'",
        "rule_text": """<div style="background:#f0f9ff; border-left:4px solid #0284c7; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#0369a1; font-size:9.5pt;">[A] Situational Anchor: Shift Handover Notes</strong><br>
When you finish your shift in a cafe, shop, or clinic, you leave a short note for the next team member. Writing lots of short, repetitive sentences makes notes slow to read. Joining related thoughts with <strong>and</strong> or <strong>but</strong> creates clear, professional compound sentences.
</div>

<div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#15803d; font-size:9.5pt;">[B] Syntax Architecture: Adding vs Contrasting</strong>
<ul style="margin:4px 0 0 16px; padding:0;">
  <li><strong>'And' connects two similar ideas:</strong> It adds extra information.<br>
      <code>[Sentence 1] + and + [Sentence 2]</code><br>
      <em>Example: I locked the cash register <strong>and</strong> I put the keys in the safe.</em></li>
  <li><strong>'But' connects two contrasting or unexpected ideas:</strong> It highlights a problem, difference, or exception.<br>
      <code>[Sentence 1] + but + [Sentence 2]</code><br>
      <em>Example: We received thirty customer orders, <strong>but</strong> two boxes were missing.</em></li>
</ul>
</div>

<div style="background:#fef2f2; border-left:4px solid #dc2626; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#b91c1c; font-size:9.5pt;">[C] Compare &amp; Contrast: Choosing the Right Link</strong><br>
<span style="color:#dc2626; font-weight:bold;">Incorrect:</span> <em>The morning was very busy and we ran out of milk.</em> (Hides the contrast/issue)<br>
<span style="color:#16a34a; font-weight:bold;">Correct:</span> <em>The morning was very busy, <strong>but</strong> we ran out of milk.</em><br>
<span style="color:#4b5563; font-size:8pt;"><strong>Why:</strong> Running out of milk is a problem and a contrast to normal service, so 'but' is the correct connective.</span>
</div>

<div style="background:#fefce8; border-left:4px solid #d97706; padding:8px 12px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#b45309; font-size:9.5pt;">[D] Golden Rule &amp; Memory Hook</strong><br>
Use <strong>'and'</strong> to <strong>add</strong> things together (Positive + Positive).<br>
Use <strong>'but'</strong> when there is a <strong>bump in the road</strong> &mdash; a contrast, twist, or problem!
</div>""",
        "format_link": "In workplace notes, using 'and' and 'but' appropriately ensures your colleagues understand both completed tasks and pending issues quickly.",
        "worked_bad": "I restocked the shelves. I swept the stockroom. The delivery arrived. Three boxes were damaged.",
        "worked_good": "I restocked the shelves and swept the stockroom. The delivery arrived, but three boxes were damaged.",
        "worked_why": "Joined the two completed tasks with 'and', and joined the delivery and damaged items with 'but' to highlight the problem.",
        "exercise_a": [
            ("Choose the correct connective: <em>'Liam cleaned the coffee machine [ and / but ] he wiped down all the tables.'</em>",
             ["A) and", "B) but"],
             "A"),
            ("Choose the correct connective: <em>'We phoned the delivery driver [ and / but ] his phone was switched off.'</em>",
             ["A) and", "B) but"],
             "B"),
            ("Which sentence correctly joins two similar completed tasks?",
             ["A) I answered customer emails, but I filed the paper invoices.",
              "B) I answered customer emails and I filed the paper invoices.",
              "C) I answered customer emails but filed nothing."],
             "B"),
            ("Which sentence correctly shows contrast or a workplace issue?",
             ["A) The customer liked the sofa, but she could not afford the delivery fee.",
              "B) The customer liked the sofa and she could not afford the delivery fee.",
              "C) The customer liked the sofa so she could not afford the delivery fee."],
             "A")
        ],
        "proofreading_title": "Format 4 Applied Proofreading: Coffee Shop Shift Handover Note",
        "proofreading_scenario": "A barista left this handover note for the evening supervisor. There are <strong>5 SPaG errors</strong> involving sentence joining, connectives, and punctuation.",
        "proofreading_text": """<div style="background:#ffffff; border:1px solid #cbd5e1; padding:8px 12px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; font-size:8.5pt; line-height:1.5; color:#1f2937;">
<p style="margin:0 0 6px 0;"><strong>Shift Handover Note &bull; 2:00 PM</strong></p>
<p style="margin:0 0 6px 0;">Hi Priya. The lunch rush was really hectic but we managed to serve all customers quickly.</p>
<p style="margin:0 0 6px 0;">I washed all the cups and I mopped the floor. We wanted to bake more blueberry muffins and the oven temperature gauge broke at 1:30 PM.</p>
<p style="margin:0;">The engineer is coming on wednesday he will fix the thermostat.</p>
</div>""",
        "proofreading_errors": [
            "Missing comma after informal greeting ('Hi Priya.' -> 'Hi Priya,')",
            "Incorrect connective for positive result ('hectic but we managed' -> 'hectic, and we managed' or keep 'but' with comma)",
            "Incorrect connective showing contrast/problem ('muffins and the oven' -> 'muffins, but the oven')",
            "Missing capital letter for day of the week ('wednesday' -> 'Wednesday')",
            "Run-on sentence needing connective or full stop ('on Wednesday he will fix' -> 'on Wednesday, and he will fix')"
        ],
        "writing_prompt": "Write <strong>two compound sentences</strong> for a handover note to a colleague: one sentence using <strong>'and'</strong> to join two routine tasks you finished, and one sentence using <strong>'but'</strong> to explain a minor issue that needs their attention."
    },
    {
        "unit": 5,
        "format": "Everyday Note / Absence Message",
        "title": "Giving Reasons & Results: 'Because' & 'So'",
        "subtitle": "Explaining Delays & Absences to Supervisors and Tutors",
        "rule_title": "Core Grammar Rule: Cause and Effect: When to Use 'Because' vs 'So'",
        "rule_text": """<div style="background:#f0f9ff; border-left:4px solid #0284c7; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#0369a1; font-size:9.5pt;">[A] Situational Anchor: Workplace Absence &amp; Delay Notes</strong><br>
When you are unwell, attending a doctor's appointment, or running late due to train delays, you must notify your employer or tutor. You need to explain the reason (why) and the result (what happens next). Using <strong>because</strong> and <strong>so</strong> makes your message clear and polite.
</div>

<div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#15803d; font-size:9.5pt;">[B] Syntax Architecture: Cause (Because) vs Effect (So)</strong>
<ul style="margin:4px 0 0 16px; padding:0;">
  <li><strong>'Because' introduces the REASON / CAUSE (Answers 'Why?'):</strong><br>
      <code>[Situation / Action] + because + [Reason]</code><br>
      <em>Example: I cannot attend college today <strong>because</strong> I have a severe migraine.</em></li>
  <li><strong>'So' introduces the RESULT / EFFECT (Answers 'What happened next?'):</strong><br>
      <code>[Cause / Reason] + so + [Result]</code><br>
      <em>Example: My morning train was cancelled, <strong>so</strong> I will arrive twenty minutes late.</em></li>
</ul>
</div>

<div style="background:#fef2f2; border-left:4px solid #dc2626; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#b91c1c; font-size:9.5pt;">[C] Compare &amp; Contrast: Mixing Up Cause and Result</strong><br>
<span style="color:#dc2626; font-weight:bold;">Incorrect:</span> <em>I am going to the doctor so I have a chest infection.</em> (Nonsense order!)<br>
<span style="color:#16a34a; font-weight:bold;">Correct:</span> <em>I am going to the doctor <strong>because</strong> I have a chest infection.</em><br>
<span style="color:#16a34a; font-weight:bold;">Also Correct:</span> <em>I have a chest infection, <strong>so</strong> I am going to the doctor.</em><br>
<span style="color:#4b5563; font-size:8pt;"><strong>Why:</strong> The illness is the cause; visiting the doctor is the result.</span>
</div>

<div style="background:#fefce8; border-left:4px solid #d97706; padding:8px 12px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#b45309; font-size:9.5pt;">[D] Golden Rule &amp; Memory Hook</strong><br>
<strong>Because</strong> looks backwards at the <strong>cause</strong> (<em>Why did this happen?</em>).<br>
<strong>So</strong> looks forwards at the <strong>consequence</strong> (<em>What is the result?</em>).
</div>""",
        "format_link": "In everyday workplace messages, getting 'because' and 'so' the wrong way around can lead managers to misunderstand emergency situations.",
        "worked_bad": "I missed my shift so I had car trouble. I could not phone you because my battery died so I borrowed a phone.",
        "worked_good": "I missed my shift because I had car trouble. My phone battery died, so I borrowed a phone to contact you.",
        "worked_why": "Used 'because' to explain the reason for the absence, and 'so' to link the dead battery to borrowing a phone.",
        "exercise_a": [
            ("Choose the correct connective: <em>'Chloe stayed home [ because / so ] she had a high fever.'</em>",
             ["A) because", "B) so"],
             "A"),
            ("Choose the correct connective: <em>'The delivery van broke down, [ because / so ] the packages arrived late.'</em>",
             ["A) because", "B) so"],
             "B"),
            ("Which sentence correctly explains the reason for an absence?",
             ["A) I cannot attend work so I have a medical appointment.",
              "B) I cannot attend work because I have a medical appointment.",
              "C) I have a medical appointment because I cannot attend work."],
             "B"),
            ("Which sentence correctly shows cause and result using 'so'?",
             ["A) The road was flooded, so buses were diverted.",
              "B) Buses were diverted, so the road was flooded.",
              "C) The road was flooded because buses were diverted."],
             "A")
        ],
        "proofreading_title": "Format 5 Applied Proofreading: Absence Message to Team Leader",
        "proofreading_scenario": "An apprentice sent this message to their team leader. There are <strong>5 SPaG errors</strong> involving 'because', 'so', capital letters, and full stops.",
        "proofreading_text": """<div style="background:#ffffff; border:1px solid #cbd5e1; padding:8px 12px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; font-size:8.5pt; line-height:1.5; color:#1f2937;">
<p style="margin:0 0 6px 0;">Good morning Brenda.</p>
<p style="margin:0 0 6px 0;">i am very sorry but I cannot come in today so my boiler burst overnight. The kitchen is flooded because I need to wait for the emergency plumber.</p>
<p style="margin:0;">I will complete my coursework from home so i have my laptop with me</p>
</div>""",
        "proofreading_errors": [
            "Missing capital letter on pronoun ('i am very sorry' -> 'I am very sorry')",
            "Incorrect connective for reason ('today so my boiler burst' -> 'today because my boiler burst')",
            "Reversed cause and effect ('flooded because I need to wait' -> 'flooded, so I need to wait')",
            "Missing capital letter on pronoun in final sentence ('so i have' -> 'because I have' or 'so I have')",
            "Missing full stop at the end of the message ('laptop with me' -> 'laptop with me.')"
        ],
        "writing_prompt": "Write <strong>two sentences</strong> to your line manager explaining why you will be 30 minutes late tomorrow. In the first sentence, use <strong>'because'</strong> to give the reason. In the second sentence, use <strong>'so'</strong> to explain how you will make up the lost time."
    },
    {
        "unit": 6,
        "format": "Daily Work Routine / Task Checklist",
        "title": "Present Tense: Everyday Routines & Regular Verbs",
        "subtitle": "Describing Daily Shift Duties & Habitual Tasks",
        "rule_title": "Core Grammar Rule: Present Simple & The Third-Person 's' Rule",
        "rule_text": """<div style="background:#f0f9ff; border-left:4px solid #0284c7; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#0369a1; font-size:9.5pt;">[A] Situational Anchor: Daily Job Routines</strong><br>
When you describe what you or your workmates do every day, you use the simple present tense. Job descriptions, daily work logs, and handover checklists rely on accurate present tense verbs.
</div>

<div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#15803d; font-size:9.5pt;">[B] Syntax Architecture: The 's' on the Verb</strong>
<ul style="margin:4px 0 0 16px; padding:0;">
  <li><strong>I / You / We / They:</strong> Use the <strong>Base Verb</strong> (no extra letters).<br>
      <em>Examples: I <strong>start</strong> at 8:00 AM. &bull; We <strong>clean</strong> the shelves. &bull; They <strong>check</strong> the deliveries.</em></li>
  <li><strong>He / She / It (Singular Person or Object):</strong> Add <strong>-s</strong> or <strong>-es</strong> to the verb!<br>
      <em>Examples: He <strong>starts</strong> at 8:00 AM. &bull; She <strong>cleans</strong> the shelves. &bull; The store <strong>opens</strong> early.</em></li>
  <li><strong>Spelling Rule for -es:</strong> If the verb ends in <em>-ch, -sh, -ss, -x, -o</em>, add <strong>-es</strong>:<br>
      <em>watch &rarr; watch<strong>es</strong> &bull; wash &rarr; wash<strong>es</strong> &bull; pass &rarr; pass<strong>es</strong> &bull; fix &rarr; fix<strong>es</strong> &bull; go &rarr; go<strong>es</strong></em>.</li>
</ul>
</div>

<div style="background:#fef2f2; border-left:4px solid #dc2626; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#b91c1c; font-size:9.5pt;">[C] Compare &amp; Contrast: Missing Third-Person 's'</strong><br>
<span style="color:#dc2626; font-weight:bold;">Incorrect:</span> <em>Marcus unlock the door and he wash the floor.</em><br>
<span style="color:#16a34a; font-weight:bold;">Correct:</span> <em>Marcus unlock<strong>s</strong> the door and he wash<strong>es</strong> the floor.</em><br>
<span style="color:#4b5563; font-size:8pt;"><strong>Why:</strong> 'Marcus' is one person (he), so regular verbs require -s or -es.</span>
</div>

<div style="background:#fefce8; border-left:4px solid #d97706; padding:8px 12px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#b45309; font-size:9.5pt;">[D] Golden Rule &amp; Memory Hook</strong><br>
One person (<em>he, she, Marcus, the manager</em>) gives the verb an <strong>'s'</strong>!<br>
More than one person (<em>we, they, the cleaners</em>) leaves the verb <strong>plain</strong>.<br>
<em>(I and You also stay plain: I work, you work).</em>
</div>""",
        "format_link": "In job descriptions and training sheets, missing third-person -s endings looks grammatically incomplete and fails Ofqual Entry 3 criteria.",
        "worked_bad": "Every morning Sarah arrive at nine, open the shop, and check the emails.",
        "worked_good": "Every morning, Sarah arrives at nine, opens the shop, and checks the emails.",
        "worked_why": "Sarah is singular (she), so all three present tense verbs need the -s suffix (arrives, opens, checks).",
        "exercise_a": [
            ("Select the correct verb: <em>'The warehouse supervisor [ check / checks ] all safety equipment daily.'</em>",
             ["A) check", "B) checks"],
             "B"),
            ("Select the correct verb: <em>'Our apprentices [ attend / attends ] college every Thursday.'</em>",
             ["A) attend", "B) attends"],
             "A"),
            ("Which sentence uses the correct third-person -es spelling?",
             ["A) Elena watchs the front entrance during lunch.",
              "B) Elena watches the front entrance during lunch.",
              "C) Elena watch the front entrance during lunch."],
             "B"),
            ("Choose the sentence with 100% accurate present tense verbs:",
             ["A) I prepares the food and Michael serve the customers.",
              "B) I prepare the food and Michael serves the customers.",
              "C) I prepare the food and Michael serve the customers."],
             "B")
        ],
        "proofreading_title": "Format 6 Applied Proofreading: Care Home Assistant Duty Log",
        "proofreading_scenario": "A senior carer drafted this daily routine list for a new care assistant. There are <strong>5 present tense verb errors</strong>.",
        "proofreading_text": """<div style="background:#ffffff; border:1px solid #cbd5e1; padding:8px 12px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; font-size:8.5pt; line-height:1.5; color:#1f2937;">
<h4 style="margin:0 0 6px 0; color:#0369a1;">Oaklands Care Home &bull; Morning Shift Routine</h4>
<p style="margin:0 0 6px 0;">Every morning, Gemma greet each resident and help them with breakfast.</p>
<p style="margin:0 0 6px 0;">She check their medication charts carefully. Later, she wash the tea trays and clean the dining area.</p>
<p style="margin:0;">At 11:00 AM, the care manager discuss the afternoon activities with the team.</p>
</div>""",
        "proofreading_errors": [
            "Missing -s on third-person verb ('Gemma greet' -> 'Gemma greets')",
            "Missing -s on third-person verb ('and help' -> 'and helps')",
            "Missing -s on third-person verb ('She check' -> 'She checks')",
            "Missing -es on verb ending in -sh ('she wash' -> 'she washes')",
            "Missing -es on verb ending in -ss ('manager discuss' -> 'manager discusses')"
        ],
        "writing_prompt": "Write <strong>two sentences</strong> describing a regular daily routine at college or work. In one sentence write about what you do yourself using 'I' (e.g. <em>'I arrive...'</em>). In the other sentence, write about what a colleague does using 'He' or 'She' (remembering to add -s to the verb)."
    },
    {
        "unit": 7,
        "format": "Incident Report Log / Completed Task Note",
        "title": "Past Tense: Regular Verbs with -ed",
        "subtitle": "Reporting Workplace Events That Happened Yesterday",
        "rule_title": "Core Grammar Rule: How to Form the Regular Past Tense (-ed)",
        "rule_text": """<div style="background:#f0f9ff; border-left:4px solid #0284c7; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#0369a1; font-size:9.5pt;">[A] Situational Anchor: Workplace Incident &amp; Task Logs</strong><br>
When you write an incident report or record completed tasks at the end of the day, you describe events that are already finished. For most regular verbs in English, you show the past tense by adding <strong>-ed</strong>.
</div>

<div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#15803d; font-size:9.5pt;">[B] Syntax Architecture: 4 Rules for Adding -ed</strong>
<ul style="margin:4px 0 0 16px; padding:0;">
  <li><strong>1. Standard Regular Verbs:</strong> Just add <strong>-ed</strong>.<br>
      <em>clean &rarr; clean<strong>ed</strong> &bull; check &rarr; check<strong>ed</strong> &bull; inspect &rarr; inspect<strong>ed</strong> &bull; walk &rarr; walk<strong>ed</strong></em></li>
  <li><strong>2. Verbs ending in silent 'e':</strong> Just add <strong>-d</strong>.<br>
      <em>arrive &rarr; arrive<strong>d</strong> &bull; close &rarr; close<strong>d</strong> &bull; serve &rarr; serve<strong>d</strong></em></li>
  <li><strong>3. Short 1-syllable verbs (1 short vowel + 1 consonant):</strong> Double the last consonant before adding <strong>-ed</strong>.<br>
      <em>stop &rarr; stop<strong>ped</strong> &bull; drop &rarr; drop<strong>ped</strong> &bull; plan &rarr; plan<strong>ned</strong></em></li>
  <li><strong>4. Verbs ending in consonant + 'y':</strong> Change 'y' to <strong>-ied</strong>.<br>
      <em>tidy &rarr; tid<strong>ied</strong> &bull; carry &rarr; carr<strong>ied</strong> &bull; hurry &rarr; hurr<strong>ied</strong></em></li>
</ul>
</div>

<div style="background:#fef2f2; border-left:4px solid #dc2626; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#b91c1c; font-size:9.5pt;">[C] Compare &amp; Contrast: Spelling Pitfalls</strong><br>
<span style="color:#dc2626; font-weight:bold;">Incorrect:</span> <em>Yesterday the engineer arrive and stoped the leaking pipe.</em><br>
<span style="color:#16a34a; font-weight:bold;">Correct:</span> <em>Yesterday the engineer arrive<strong>d</strong> and stop<strong>ped</strong> the leaking pipe.</em><br>
<span style="color:#4b5563; font-size:8pt;"><strong>Why:</strong> 'Arrive' ends in e so it adds 'd' (arrived); 'stop' is a 1-1-1 word so it doubles the 'p' (stopped, not stoped).</span>
</div>

<div style="background:#fefce8; border-left:4px solid #d97706; padding:8px 12px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#b45309; font-size:9.5pt;">[D] Golden Rule &amp; Memory Hook</strong><br>
If it happened yesterday, add <strong>-ed</strong> to the action!<br>
Watch out: <strong>stop &rarr; stopped</strong> (double p), <strong>plan &rarr; planned</strong> (double n).<br>
Never leave the verb in the present tense when reporting a past incident!
</div>""",
        "format_link": "Accurate past tense endings in incident reports protect you legally by stating exactly when and how safety actions were taken.",
        "worked_bad": "Yesterday the customer trip on the carpet and drop her shopping bags.",
        "worked_good": "Yesterday the customer tripped on the carpet and dropped her shopping bags.",
        "worked_why": "Both 'trip' and 'drop' are short verbs with one short vowel and one consonant, so their final consonants double before adding -ed (tripped, dropped).",
        "exercise_a": [
            ("Select the correct past tense verb: <em>'The security guard [ lock / locked ] the front gates at 10:00 PM.'</em>",
             ["A) lock", "B) locked"],
             "B"),
            ("Choose the correct spelling with consonant doubling: <em>'The train suddenly [ stoped / stopped ] outside the station.'</em>",
             ["A) stoped", "B) stopped"],
             "B"),
            ("Which sentence spells the past tense of 'tidy' correctly?",
             ["A) Chloe tidyed the staff room yesterday.",
              "B) Chloe tidied the staff room yesterday.",
              "C) Chloe tidied the staff room yesterday."],
             "B"),
            ("Select the incident report sentence with correct past tense verbs throughout:",
             ["A) The maintenance worker repaired the handrail and painted the steps.",
              "B) The maintenance worker repair the handrail and paint the steps.",
              "C) The maintenance worker repared the handrail and paint the steps."],
             "A")
        ],
        "proofreading_title": "Format 7 Applied Proofreading: Warehouse Accident Log",
        "proofreading_scenario": "A warehouse supervisor wrote this log after a minor incident yesterday afternoon. There are <strong>5 regular past tense errors</strong>.",
        "proofreading_text": """<div style="background:#ffffff; border:1px solid #cbd5e1; padding:8px 12px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; font-size:8.5pt; line-height:1.5; color:#1f2937;">
<h4 style="margin:0 0 6px 0; color:#b91c1c;">Incident Log &bull; Date: 12 October 2026 &bull; Bay 3</h4>
<p style="margin:0 0 6px 0;">At 14:15, a pallet truck slip on a wet patch of floor. The operative droped a crate of tins.</p>
<p style="margin:0 0 6px 0;">I immediately inspect the floor surface and warn other staff members. We clean the area thoroughly.</p>
<p style="margin:0;">The health and safety officer arrive at 14:45 and signed off the report.</p>
</div>""",
        "proofreading_errors": [
            "Missing past tense ending on regular verb ('slip' -> 'slipped')",
            "Spelling error in consonant doubling ('droped' -> 'dropped')",
            "Missing past tense ending on regular verb ('inspect' -> 'inspected')",
            "Missing past tense ending on regular verb ('clean' -> 'cleaned')",
            "Missing past tense ending on regular verb ending in e ('arrive' -> 'arrived')"
        ],
        "writing_prompt": "Write <strong>two complete sentences</strong> for a workplace incident log describing two tasks you completed yesterday afternoon (e.g. using verbs like <em>cleaned, checked, reported, repaired, inspected</em>)."
    },
    {
        "unit": 8,
        "format": "Shift Handover Report / Customer Log",
        "title": "Common Irregular Past Verbs",
        "subtitle": "Mastering 'went', 'saw', 'had', 'came', 'did', 'said', 'took', 'was/were'",
        "rule_title": "Core Grammar Rule: Irregular Past Tense Verbs That Do Not Add -ed",
        "rule_text": """<div style="background:#f0f9ff; border-left:4px solid #0284c7; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#0369a1; font-size:9.5pt;">[A] Situational Anchor: Workplace Handovers &amp; Logs</strong><br>
Many of the most important verbs in English do not follow the -ed rule. Instead, the whole word changes in the past tense. When telling your manager what happened on your shift, you must use these irregular forms correctly.
</div>

<div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#15803d; font-size:9.5pt;">[B] Syntax Architecture: The 'Essential 8' Irregular Past Verbs</strong>
<ul style="margin:4px 0 0 16px; padding:0;">
  <li><strong>go &rarr; went</strong> (<em>I went to the store room.</em> &mdash; never 'goed')</li>
  <li><strong>see &rarr; saw</strong> (<em>I saw the customer.</em> &mdash; never 'seed' or 'I seen')</li>
  <li><strong>have &rarr; had</strong> (<em>We had a delivery.</em> &mdash; never 'haved')</li>
  <li><strong>come &rarr; came</strong> (<em>The manager came in.</em> &mdash; never 'comed')</li>
  <li><strong>do &rarr; did</strong> (<em>He did the paperwork.</em> &mdash; never 'dided' or 'he done')</li>
  <li><strong>say &rarr; said</strong> (<em>She said thank you.</em> &mdash; never 'sayed')</li>
  <li><strong>take &rarr; took</strong> (<em>I took the parcel.</em> &mdash; never 'taked')</li>
  <li><strong>be &rarr; was / were</strong> (<em>I was happy. / They were late.</em> &mdash; never 'beed')</li>
</ul>
</div>

<div style="background:#fef2f2; border-left:4px solid #dc2626; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#b91c1c; font-size:9.5pt;">[C] Compare &amp; Contrast: Non-Standard vs Standard Past</strong><br>
<span style="color:#dc2626; font-weight:bold;">Incorrect:</span> <em>I seen the customer, so I taked her details and goed to the office.</em><br>
<span style="color:#16a34a; font-weight:bold;">Correct:</span> <em>I <strong>saw</strong> the customer, so I <strong>took</strong> her details and <strong>went</strong> to the office.</em><br>
<span style="color:#4b5563; font-size:8pt;"><strong>Why:</strong> The past of 'see' is 'saw'; 'take' is 'took'; 'go' is 'went'.</span>
</div>

<div style="background:#fefce8; border-left:4px solid #d97706; padding:8px 12px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#b45309; font-size:9.5pt;">[D] Golden Rule &amp; Memory Hook</strong><br>
Never say <em>'I seen'</em> or <em>'I done'</em> on an exam paper!<br>
Always write: <strong>I saw</strong> &bull; <strong>I did</strong> &bull; <strong>I went</strong> &bull; <strong>I took</strong> &bull; <strong>I came</strong>.
</div>""",
        "format_link": "Using irregular past verbs correctly in handover notes demonstrates vocational maturity and ensures you meet the Ofqual grammar standard.",
        "worked_bad": "Yesterday the courier comed to reception and said he haved three parcels.",
        "worked_good": "Yesterday the courier came to reception and said he had three parcels.",
        "worked_why": "The past tense of 'come' is 'came' and the past tense of 'have' is 'had'.",
        "exercise_a": [
            ("Choose the correct irregular past verb: <em>'At lunch time, I [ went / goed ] to the bank to deposit the takings.'</em>",
             ["A) goed", "B) went"],
             "B"),
            ("Choose the standard past tense form: <em>'The supervisor [ saw / seen ] the accident yesterday morning.'</em>",
             ["A) saw", "B) seen"],
             "A"),
            ("Which sentence uses the correct past tense of 'take' and 'do'?",
             ["A) Jamal took the meter reading and did the weekly safety audit.",
              "B) Jamal taked the meter reading and done the weekly safety audit.",
              "C) Jamal took the meter reading and dided the weekly safety audit."],
             "A"),
            ("Identify the sentence with correct irregular past verbs throughout:",
             ["A) The inspector came early, had a brief meeting, and said the site was safe.",
              "B) The inspector comed early, haved a brief meeting, and sayed the site was safe.",
              "C) The inspector came early, had a brief meeting, and sayed the site was safe."],
             "A")
        ],
        "proofreading_title": "Format 8 Applied Proofreading: Delivery Driver Handover Report",
        "proofreading_scenario": "A delivery driver completed this shift handover sheet. There are <strong>5 irregular past verb errors</strong>.",
        "proofreading_text": """<div style="background:#ffffff; border:1px solid #cbd5e1; padding:8px 12px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; font-size:8.5pt; line-height:1.5; color:#1f2937;">
<h4 style="margin:0 0 6px 0; color:#0369a1;">Swift Logistics &bull; Driver Shift Handover</h4>
<p style="margin:0 0 6px 0;">This morning I goed to the central depot at 06:30. I seen thirty pallets waiting on Bay 2.</p>
<p style="margin:0 0 6px 0;">The warehouse clerk comed out and haved the signature keys ready. I done all fifteen city deliveries before 13:00.</p>
<p style="margin:0;">The customer on Station Road taked the heavy parcel directly into the shop.</p>
</div>""",
        "proofreading_errors": [
            "Incorrect past tense of 'go' ('goed' -> 'went')",
            "Non-standard past tense of 'see' ('I seen' -> 'I saw')",
            "Incorrect past tense of 'come' ('comed' -> 'came')",
            "Incorrect past tense of 'have' ('haved' -> 'had')",
            "Incorrect past tense of 'do' and 'take' ('I done' -> 'I did'; 'taked' -> 'took')"
        ],
        "writing_prompt": "Write <strong>two complete sentences</strong> describing what you did yesterday at work or college. Include at least two irregular past verbs from the target list (<em>went, saw, had, came, did, said, took</em>)."
    },
    {
        "unit": 9,
        "format": "Staff Noticeboard / Equipment Update",
        "title": "Subject-Verb Agreement: Singular vs Plural",
        "subtitle": "Matching Subjects with 'is/are', 'has/have', 'was/were'",
        "rule_title": "Core Grammar Rule: Singular Subjects Need Singular Verbs",
        "rule_text": """<div style="background:#f0f9ff; border-left:4px solid #0284c7; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#0369a1; font-size:9.5pt;">[A] Situational Anchor: Staff Noticeboard Updates</strong><br>
When posting updates on the staff noticeboard or sending an email to colleagues about broken equipment or company news, your verbs must match your subject. If one item is broken, use a singular verb. If several items are broken, use a plural verb.
</div>

<div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#15803d; font-size:9.5pt;">[B] Syntax Architecture: Singular vs Plural Verbs</strong>
<ul style="margin:4px 0 0 16px; padding:0;">
  <li><strong>IS vs ARE (Present Tense):</strong><br>
      &bull; <em>The printer <strong>is</strong> out of order.</em> (Singular: 1 printer)<br>
      &bull; <em>The printers <strong>are</strong> out of order.</em> (Plural: 2+ printers)</li>
  <li><strong>HAS vs HAVE (Present Tense):</strong><br>
      &bull; <em>The new apprentice <strong>has</strong> arrived.</em> (Singular: 1 person)<br>
      &bull; <em>The new apprentices <strong>have</strong> arrived.</em> (Plural: 2+ people)</li>
  <li><strong>WAS vs WERE (Past Tense):</strong><br>
      &bull; <em>The fire alarm <strong>was</strong> tested yesterday.</em> (Singular)<br>
      &bull; <em>The fire alarms <strong>were</strong> tested yesterday.</em> (Plural)<br>
      &bull; <em><strong>You were</strong></em> (Special rule: 'You' ALWAYS takes 'were', never 'you was'!).</li>
</ul>
</div>

<div style="background:#fef2f2; border-left:4px solid #dc2626; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#b91c1c; font-size:9.5pt;">[C] Compare &amp; Contrast: The 'You was' Trap</strong><br>
<span style="color:#dc2626; font-weight:bold;">Incorrect:</span> <em>The tools is in the van and you was scheduled to drive.</em><br>
<span style="color:#16a34a; font-weight:bold;">Correct:</span> <em>The tools <strong>are</strong> in the van and you <strong>were</strong> scheduled to drive.</em><br>
<span style="color:#4b5563; font-size:8pt;"><strong>Why:</strong> 'Tools' is plural so it needs 'are'. In standard English, 'you' always pairs with 'were'.</span>
</div>

<div style="background:#fefce8; border-left:4px solid #d97706; padding:8px 12px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#b45309; font-size:9.5pt;">[D] Golden Rule &amp; Memory Hook</strong><br>
<strong>One thing</strong> &rarr; <em>is / has / was</em><br>
<strong>More than one</strong> &rarr; <em>are / have / were</em><br>
<strong>Never write 'we was' or 'you was'</strong> &mdash; always <em>we were / you were</em>!
</div>""",
        "format_link": "Subject-verb agreement errors (like 'the machines is broken' or 'we was late') are heavily penalised by Functional Skills examiners.",
        "worked_bad": "The computers is very slow today. Both technicians has been called to fix them.",
        "worked_good": "The computers are very slow today. Both technicians have been called to fix them.",
        "worked_why": "'Computers' is plural so it needs 'are'. 'Technicians' is plural so it needs 'have'.",
        "exercise_a": [
            ("Choose the correct verb: <em>'The main photocopier [ is / are ] waiting for replacement toner.'</em>",
             ["A) is", "B) are"],
             "A"),
            ("Choose the correct verb: <em>'Several staff members [ has / have ] requested overtime this weekend.'</em>",
             ["A) has", "B) have"],
             "B"),
            ("Select the standard English sentence:",
             ["A) You was very helpful during the inspection.",
              "B) You were very helpful during the inspection.",
              "C) You is very helpful during the inspection."],
             "B"),
            ("Choose the sentence with correct subject-verb agreement throughout:",
             ["A) The customer service desk are closed and the lights is off.",
              "B) The customer service desk is closed and the lights are off.",
              "C) The customer service desk is closed and the lights is off."],
             "B")
        ],
        "proofreading_title": "Format 9 Applied Proofreading: Staff Room Noticeboard Memo",
        "proofreading_scenario": "An office junior pinned this notice to the staff board. There are <strong>5 subject-verb agreement errors</strong>.",
        "proofreading_text": """<div style="background:#ffffff; border:1px solid #cbd5e1; padding:8px 12px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; font-size:8.5pt; line-height:1.5; color:#1f2937;">
<h4 style="margin:0 0 6px 0; color:#0369a1;">STAFF NOTICEBOARD &bull; Office Refurbishment Update</h4>
<p style="margin:0 0 6px 0;">All staff members is reminded that the second floor meeting rooms is closed for painting.</p>
<p style="margin:0 0 6px 0;">The decorators has completed the reception hallway. Yesterday we was unable to use the lift because contractors were moving heavy furniture.</p>
<p style="margin:0;">The facility manager have ordered new ergonomic chairs for every desk.</p>
</div>""",
        "proofreading_errors": [
            "Plural subject requires plural verb ('members is reminded' -> 'members are reminded')",
            "Plural subject requires plural verb ('meeting rooms is closed' -> 'meeting rooms are closed')",
            "Plural subject requires plural verb ('decorators has completed' -> 'decorators have completed')",
            "Plural pronoun requires plural past verb ('we was unable' -> 'we were unable')",
            "Singular subject requires singular verb ('facility manager have ordered' -> 'facility manager has ordered')"
        ],
        "writing_prompt": "Write <strong>two complete sentences</strong> for a staff noticeboard about workplace equipment. In sentence 1, use a singular subject with <strong>'is'</strong> or <strong>'has'</strong>. In sentence 2, use a plural subject with <strong>'are'</strong> or <strong>'have'</strong>."
    },
    {
        "unit": 10,
        "format": "Stock Order / Shopping & Inventory List",
        "title": "Commas in Simple Lists",
        "subtitle": "Writing Kitchen Orders, Tool Checklists & Supply Requisitions",
        "rule_title": "Core Grammar Rule: How to Punctuate Items in a Simple List",
        "rule_text": """<div style="background:#f0f9ff; border-left:4px solid #0284c7; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#0369a1; font-size:9.5pt;">[A] Situational Anchor: Workplace Orders &amp; Checklists</strong><br>
In kitchens, construction sites, and retail stockrooms, you frequently write supply orders and equipment lists. Commas separate the items cleanly so suppliers do not deliver the wrong goods or mix items together.
</div>

<div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#15803d; font-size:9.5pt;">[B] Syntax Architecture: The List Formula</strong><br>
<code>[Item 1], [Item 2], [Item 3] and [Item 4].</code>
<ul style="margin:4px 0 0 16px; padding:0;">
  <li>Put a <strong>comma (,)</strong> between each item in the list.</li>
  <li>Use the word <strong>'and'</strong> before the very last item.</li>
  <li><strong>Do NOT</strong> put a comma before or after the word 'and' in a simple list.</li>
  <li>End the sentence with a <strong>full stop (.)</strong>.</li>
</ul>
</div>

<div style="background:#fef2f2; border-left:4px solid #dc2626; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#b91c1c; font-size:9.5pt;">[C] Compare &amp; Contrast: Too Few or Too Many Commas</strong><br>
<span style="color:#dc2626; font-weight:bold;">Missing Commas:</span> <em>Please order milk butter eggs and flour.</em> (Items blend together)<br>
<span style="color:#dc2626; font-weight:bold;">Too Many Commas:</span> <em>Please order milk, butter, eggs, and, flour.</em> (Awkward pauses)<br>
<span style="color:#16a34a; font-weight:bold;">Correct:</span> <em>Please order milk, butter, eggs and flour.</em><br>
<span style="color:#4b5563; font-size:8pt;"><strong>Why:</strong> Commas separate the first three items; 'and' connects the final item cleanly without extra commas.</span>
</div>

<div style="background:#fefce8; border-left:4px solid #d97706; padding:8px 12px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#b45309; font-size:9.5pt;">[D] Golden Rule &amp; Memory Hook</strong><br>
Separate items with a <strong>comma</strong>, but replace the last comma with <strong>'and'</strong>.<br>
<em>Never put a comma after 'and'!</em>
</div>""",
        "format_link": "Clear list punctuation on supply requisitions ensures colleagues and suppliers process your orders without miscounting or combining items.",
        "worked_bad": "For the painting project we need brushes rollers white gloss masking tape and sandpaper.",
        "worked_good": "For the painting project, we need brushes, rollers, white gloss, masking tape and sandpaper.",
        "worked_why": "Placed commas after 'brushes', 'rollers', and 'white gloss', followed by 'and' before the final item 'sandpaper'.",
        "exercise_a": [
            ("Which sentence punctuates the list of supplies correctly?",
             ["A) The office needs pens paper envelopes, and stamps.",
              "B) The office needs pens, paper, envelopes and stamps.",
              "C) The office needs pens paper, envelopes and stamps."],
             "B"),
            ("Identify the sentence with correct list comma placement:",
             ["A) Before leaving, please check the windows, doors, lights and heaters.",
              "B) Before leaving please check the windows, doors, lights, and, heaters.",
              "C) Before leaving please check the windows doors lights and heaters."],
             "A"),
            ("Where should the commas go in: <em>'The salon ordered shampoo conditioner towels and hairspray.'</em>?",
             ["A) after shampoo, conditioner",
              "B) after salon, shampoo, conditioner",
              "C) after shampoo, conditioner, and"],
             "A"),
            ("Choose the correctly punctuated kitchen requisition:",
             ["A) The chef requested potatoes, onions, carrots and garlic.",
              "B) The chef requested potatoes onions carrots and garlic.",
              "C) The chef requested potatoes, onions, carrots, and, garlic."],
             "A")
        ],
        "proofreading_title": "Format 10 Applied Proofreading: Bakery Weekly Supply Order Memo",
        "proofreading_scenario": "A bakery apprentice prepared this supply order memo. There are <strong>5 punctuation errors</strong> involving list commas and full stops.",
        "proofreading_text": """<div style="background:#ffffff; border:1px solid #cbd5e1; padding:8px 12px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; font-size:8.5pt; line-height:1.5; color:#1f2937;">
<h4 style="margin:0 0 6px 0; color:#0369a1;">Sunrise Bakery &bull; Weekly Ingredients Order</h4>
<p style="margin:0 0 6px 0;">Please order strong white flour brown sugar yeast and unsalted butter for Monday morning</p>
<p style="margin:0 0 6px 0;">We also need cocoa powder, dark chocolate chips, vanilla extract, and, ground cinnamon.</p>
<p style="margin:0;">For the cafe counter, please order napkins wooden stirrers coffee beans and compostable cups.</p>
</div>""",
        "proofreading_errors": [
            "Missing list commas in sentence 1 ('flour brown sugar yeast and' -> 'flour, brown sugar, yeast and')",
            "Missing full stop at the end of sentence 1 ('Monday morning' -> 'Monday morning.')",
            "Unnecessary commas around 'and' in sentence 2 ('extract, and, ground' -> 'extract and ground')",
            "Missing list commas in sentence 3 ('napkins wooden stirrers coffee beans and' -> 'napkins, wooden stirrers, coffee beans and')",
            "Ensure sentence starts with capital letter and ends with full stop."
        ],
        "writing_prompt": "Write <strong>two complete sentences</strong> ordering items for a workplace project or shopping trip. Include a list of at least <strong>four items</strong> in one of the sentences, punctuating each item with correct commas and 'and'."
    },
    {
        "unit": 11,
        "format": "Stocktake / Inventory Count Sheet",
        "title": "Plural Nouns: Adding -s, -es, and Changing -y to -ies",
        "subtitle": "Organising Stockrooms & Counting Workplace Goods",
        "rule_title": "Core Grammar Rule: The 3 Rules for Making Nouns Plural",
        "rule_text": """<div style="background:#f0f9ff; border-left:4px solid #0284c7; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#0369a1; font-size:9.5pt;">[A] Situational Anchor: Stocktakes &amp; Inventory Records</strong><br>
During a stocktake in a shop, salon, hotel, or warehouse, you must count items and record their plural names accurately. Misspelling plurals leads to confusion on digital inventory spreadsheets and lost stock.
</div>

<div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#15803d; font-size:9.5pt;">[B] Syntax Architecture: 3 Core Plural Rules</strong>
<ul style="margin:4px 0 0 16px; padding:0;">
  <li><strong>1. Most English Nouns: Just add -s:</strong><br>
      <em>desk &rarr; desk<strong>s</strong> &bull; book &rarr; book<strong>s</strong> &bull; order &rarr; order<strong>s</strong> &bull; item &rarr; item<strong>s</strong></em></li>
  <li><strong>2. Hissing Endings (-s, -ss, -sh, -ch, -x): Add -es:</strong><br>
      <em>box &rarr; box<strong>es</strong> &bull; dish &rarr; dish<strong>es</strong> &bull; sandwich &rarr; sandwich<strong>es</strong> &bull; glass &rarr; glass<strong>es</strong> &bull; bus &rarr; bus<strong>es</strong></em></li>
  <li><strong>3. Consonant + 'y': Change 'y' to -ies:</strong><br>
      <em>delivery &rarr; deliver<strong>ies</strong> &bull; company &rarr; compan<strong>ies</strong> &bull; battery &rarr; batter<strong>ies</strong></em><br>
      <span style="font-size:8pt; color:#4b5563;">(Note: If preceded by a vowel, just add -s: <em>day &rarr; days &bull; key &rarr; keys &bull; tray &rarr; trays</em>).</span></li>
</ul>
</div>

<div style="background:#fef2f2; border-left:4px solid #dc2626; padding:8px 12px; margin-bottom:8px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#b91c1c; font-size:9.5pt;">[C] Compare &amp; Contrast: Common Plural Misspellings</strong><br>
<span style="color:#dc2626; font-weight:bold;">Incorrect:</span> <em>We received ten boxs, twelve factorys, and fifteen glass's.</em><br>
<span style="color:#16a34a; font-weight:bold;">Correct:</span> <em>We received ten box<strong>es</strong>, twelve factor<strong>ies</strong>, and fifteen glass<strong>es</strong>.</em><br>
<span style="color:#4b5563; font-size:8pt;"><strong>Why:</strong> Never use an apostrophe to make a noun plural! 'Box' needs -es; 'factory' changes -y to -ies; 'glass' ends in -ss so it adds -es.</span>
</div>

<div style="background:#fefce8; border-left:4px solid #d97706; padding:8px 12px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; line-height:1.55; color:#1f2937;">
<strong style="color:#b45309; font-size:9.5pt;">[D] Golden Rule &amp; Memory Hook</strong><br>
Hissing sound (<em>-ch, -sh, -s, -ss, -x</em>) &rarr; add <strong>-es</strong> (<em>boxes, dishes</em>).<br>
Consonant + <strong>y</strong> &rarr; drop the y, add <strong>-ies</strong> (<em>batteries, copies</em>).<br>
<strong>Apostrophes are NEVER used for ordinary plurals!</strong>
</div>""",
        "format_link": "In stock records, writing accurate plurals prevents costly inventory mismatches and shows professional attention to detail.",
        "worked_bad": "The warehouse contains fifty watchs, twenty batterys, and thirty parcel's.",
        "worked_good": "The warehouse contains fifty watches, twenty batteries and thirty parcels.",
        "worked_why": "'Watch' ends in -ch so it adds -es; 'battery' ends in consonant + y so it changes to -ies; 'parcels' is a regular plural that simply adds -s without an apostrophe.",
        "exercise_a": [
            ("Select the correct plural form of 'box':",
             ["A) boxs", "B) boxes", "C) box's"],
             "B"),
            ("Select the correct plural form of 'delivery':",
             ["A) deliverys", "B) deliveryes", "C) deliveries"],
             "C"),
            ("Which sentence contains ONLY correctly spelled plural nouns?",
             ["A) We packed five boxes of dishes and ten glasses.",
              "B) We packed five boxs of dishs and ten glasss.",
              "C) We packed five box's of dishes and ten glasses."],
             "A"),
            ("Choose the correct plural for 'company' and 'branch':",
             ["A) The three companys opened new branchs.",
              "B) The three companies opened new branches.",
              "C) The three company's opened new branch's."],
             "B")
        ],
        "proofreading_title": "Format 11 Applied Proofreading: Hotel Housekeeping Supply Stocktake",
        "proofreading_scenario": "A housekeeping supervisor completed these inventory notes. There are <strong>5 plural spelling errors</strong>.",
        "proofreading_text": """<div style="background:#ffffff; border:1px solid #cbd5e1; padding:8px 12px; border-radius:4px; font-family:'Lexend','Atkinson Hyperlegible',sans-serif; font-size:8.5pt; line-height:1.5; color:#1f2937;">
<h4 style="margin:0 0 6px 0; color:#0369a1;">Grand Hotel &bull; Linen &amp; Supply Room Stocktake</h4>
<p style="margin:0 0 6px 0;">On the upper shelves, we counted twenty pillow's and twelve woollen blanketes.</p>
<p style="margin:0 0 6px 0;">The bathroom supplies include fifty clean dishs, thirty bar's of soap, and eighty bottle of shampoo.</p>
<p style="margin:0;">We also need two new batterys for the emergency torchs in corridor 4.</p>
</div>""",
        "proofreading_errors": [
            "Incorrect apostrophe in plural ('pillow\\'s' -> 'pillows')",
            "Incorrect plural ending on regular noun ('blanketes' -> 'blankets')",
            "Incorrect plural on hissing sound word ('dishs' -> 'dishes')",
            "Incorrect apostrophe in plural ('bar\\'s' -> 'bars')",
            "Incorrect plurals on consonant+y and hissing sound ('batterys' -> 'batteries'; 'torchs' -> 'torches')"
        ],
        "writing_prompt": "Write <strong>two complete sentences</strong> recording items counted during a workplace stocktake. Include at least one plural noun ending in <strong>-es</strong> (e.g. <em>boxes, watches, glasses</em>) and one plural noun ending in <strong>-ies</strong> (e.g. <em>batteries, deliveries, companies</em>)."
    }
]


# ==============================================================================
# E3 SPELLING DATA
# 5 Core Spelling Rules + 60 Common Exception Words + Spelling Test
# Strictly mapped to Entry Level 3 Functional Skills English criteria
# ==============================================================================

E3_SPELLING_DATA = {
    "rules": [
        ("1. Adding -s and -es to Make Plural Nouns",
         "Most nouns simply add <strong>-s</strong> (<em>job &rarr; jobs, shop &rarr; shops, tool &rarr; tools, card &rarr; cards</em>).<br>"
         "Nouns ending in a hissing sound (<strong>-s, -ss, -sh, -ch, -x</strong>) must add <strong>-es</strong> because you cannot pronounce another 's' without an extra syllable:<br>"
         "<em>bus &rarr; buses, class &rarr; classes, dish &rarr; dishes, match &rarr; matches, box &rarr; boxes</em>.<br>"
         "<strong>Exam Warning:</strong> Never use an apostrophe (<em>'s</em>) to make a noun plural!"),

        ("2. Adding -ing to Everyday Verbs",
         "When adding <strong>-ing</strong> to verbs to show ongoing action:<br>"
         "&bull; <strong>Just add -ing:</strong> <em>walk &rarr; walking, clean &rarr; cleaning, wash &rarr; washing</em>.<br>"
         "&bull; <strong>Drop silent 'e':</strong> If the verb ends in a silent 'e', drop the 'e' before adding <em>-ing</em>: <em>make &rarr; making, write &rarr; writing, close &rarr; closing, drive &rarr; driving</em>.<br>"
         "&bull; <strong>Double the consonant:</strong> In short words with 1 short vowel + 1 consonant, double the last letter: <em>shop &rarr; shopping, run &rarr; running, plan &rarr; planning, sit &rarr; sitting</em>."),

        ("3. Adding -ed to Regular Past Tense Verbs",
         "To show that an action finished in the past:<br>"
         "&bull; <strong>Most regular verbs:</strong> Add <strong>-ed</strong>: <em>look &rarr; looked, paint &rarr; painted, clean &rarr; cleaned</em>.<br>"
         "&bull; <strong>Verbs ending in 'e':</strong> Just add <strong>-d</strong>: <em>arrive &rarr; arrived, live &rarr; lived, use &rarr; used</em>.<br>"
         "&bull; <strong>Consonant doubling:</strong> In short 1-syllable verbs with 1 vowel + 1 consonant, double the final consonant: <em>stop &rarr; stopped, drop &rarr; dropped, slip &rarr; slipped</em>.<br>"
         "&bull; <strong>Consonant + 'y':</strong> Change 'y' to <strong>-ied</strong>: <em>tidy &rarr; tidied, carry &rarr; carried, hurry &rarr; hurried</em>."),

        ("4. High-Frequency E3 Homophones Mastery",
         "Homophones are words that sound the same but have different spellings and meanings:<br>"
         "&bull; <strong>There</strong> (a place or statement: <em>put it over there / there is a meeting</em>)<br>"
         "&bull; <strong>Their</strong> (belongs to them: <em>their manager / their coats</em>)<br>"
         "&bull; <strong>They're</strong> (short for 'they are': <em>they're working late tonight</em>)<br>"
         "&bull; <strong>To</strong> (direction or action: <em>go to work / pleased to meet you</em>)<br>"
         "&bull; <strong>Too</strong> (also or excessive: <em>me too / the coffee is too hot</em>)<br>"
         "&bull; <strong>Two</strong> (the number 2: <em>two parcels / two hours</em>)<br>"
         "&bull; <strong>Here</strong> (this place: <em>sign here</em>) vs. <strong>Hear</strong> (with your ear: <em>can you hear me?</em>)"),

        ("5. Common Prefixes & Suffixes (un-, -ful, -less)",
         "Adding prefixes and suffixes creates new everyday words without changing root rules:<br>"
         "&bull; <strong>Prefix un- (means 'not' or opposite):</strong> Attaches directly without changing spelling: <em>happy &rarr; unhappy, well &rarr; unwell, safe &rarr; unsafe, tidy &rarr; untidy, kind &rarr; unkind</em>.<br>"
         "&bull; <strong>Suffix -ful (always ONE 'l'!):</strong> <em>help &rarr; helpful, care &rarr; careful, hope &rarr; hopeful, use &rarr; useful</em>. (Only the word <em>full</em> has two l's!).<br>"
         "&bull; <strong>Suffix -less (means 'without'):</strong> <em>care &rarr; careless, help &rarr; helpless, hope &rarr; hopeless</em>.")
    ],

    "common_exception_words": [
        # 60 Common Exception & High-Frequency Words for Entry Level 3
        # Grouped into 6 thematic vocational clusters
        ("1. Workplace, Training & Administration",
         ["address", "answer", "busy", "business", "calendar", "centre", "complete", "difficult", "exercise", "experience"]),
        ("2. Communication, Advice & Time",
         ["decide", "describe", "different", "early", "enough", "February", "forward", "history", "important", "interest"]),
        ("3. Measurement, Science & Materials",
         ["accident", "actual", "bicycle", "circle", "earth", "eight", "experiment", "length", "material", "minute"]),
        ("4. People, Community & Healthcare",
         ["breath", "breathe", "build", "famous", "favourite", "guard", "guide", "heard", "heart", "medicine"]),
        ("5. Knowledge, Learning & Language",
         ["grammar", "group", "height", "imagine", "increase", "island", "knowledge", "learn", "library", "natural"]),
        ("6. Everyday Actions & Requests",
         ["appear", "arrive", "believe", "caught", "consider", "continue", "extreme", "fruit", "mention", "question"])
    ],

    "spelling_test": [
        ("Which is the correct plural spelling of 'glass'?",
         ["A) glasss", "B) glasses", "C) glass's"],
         "B"),
        ("Which word correctly drops the silent 'e' before adding -ing?",
         ["A) writeing", "B) writting", "C) writing"],
         "C"),
        ("Choose the correct spelling with consonant doubling:",
         ["A) stoped", "B) stopped", "C) stopt"],
         "B"),
        ("Select the correct homophone: <em>'The students collected [ there / their / they're ] ID badges.'</em>",
         ["A) there", "B) their", "C) they're"],
         "B"),
        ("Select the correct homophone: <em>'It is [ to / too / two ] cold to work outside.'</em>",
         ["A) to", "B) too", "C) two"],
         "B"),
        ("Which word is spelled with the single 'l' suffix?",
         ["A) carefull", "B) careful", "C) carful"],
         "B"),
        ("Choose the correct spelling for the first month of the year:",
         ["A) Febrary", "B) Febuary", "C) February"],
         "C"),
        ("Select the correct spelling of the place where books are borrowed:",
         ["A) libary", "B) library", "C) libreary"],
         "B"),
        ("Choose the correctly spelled word for a medical treatment:",
         ["A) medicine", "B) medecine", "C) medisin"],
         "A"),
        ("Which word correctly changes -y to -ies in the plural?",
         ["A) deliverys", "B) deliveries", "C) deliveryes"],
         "B")
    ]
}


# ==============================================================================
# E3 MIXED WORKOUT
# 2 Mixed Proofreading Workplace Tasks (5 errors each)
# ==============================================================================

E3_MIXED_WORKOUT = [
    {
        "num": 1,
        "format": "Short Handover Note to Colleague",
        "title": "Workout 1: Retail Stockroom Handover Message",
        "scenario": "A retail assistant drafted this handover note on the stockroom whiteboard for their morning colleague. Find and correct the <strong>5 SPaG errors</strong>.",
        "text": """Hi David,<br>
Yesterday afternoon i unpacked thirty boxes of stock. The delivery arrived at two o'clock and three crates was damaged. I stoped the driver and he signed the return sheet. Can you please check the new deliveries on wednesday.<br>
Thanks, Chloe""",
        "errors": [
            "Missing capital letter on pronoun 'I' ('afternoon i unpacked' -> 'afternoon I unpacked')",
            "Subject-verb agreement error with plural subject ('three crates was damaged' -> 'three crates were damaged')",
            "Consonant doubling spelling error in regular past verb ('stoped' -> 'stopped')",
            "Missing capital letter for day of the week ('on wednesday' -> 'on Wednesday')",
            "Question ends with a full stop instead of question mark ('on Wednesday.' -> 'on Wednesday?')"
        ]
    },
    {
        "num": 2,
        "format": "Message on Staff Noticeboard",
        "title": "Workout 2: Staff Car Park & Facilities Notice",
        "scenario": "A facilities coordinator typed this notice for the staff canteen bulletin board. Find and correct the <strong>5 SPaG errors</strong>.",
        "text": """ATTENTION ALL STAFF MEMBERS<br>
The main car park will be closed on friday 18 October because contractors is resurfacing the tarmac. Please park on Church road or use public transport! All employees must display their permit? Do not park in the emergency ambulance bays!""",
        "errors": [
            "Missing capital letter for day of the week ('on friday' -> 'on Friday')",
            "Subject-verb agreement error with plural subject ('contractors is resurfacing' -> 'contractors are resurfacing')",
            "Missing capital letter on street name ('Church road' -> 'Church Road')",
            "Statement incorrectly ends with a question mark ('their permit?' -> 'their permit.')",
            "Urgent instruction or warning should use an exclamation mark or calm imperative with proper punctuation ('ambulance bays!' -> 'ambulance bays.')"
        ]
    }
]


# ==============================================================================
# E3 DIAGNOSTIC ASSESSMENT
# 10 Baseline Multiple Choice Questions covering the full Entry 3 SPaG spectrum
# ==============================================================================

E3_DIAGNOSTIC = [
    {
        "q_num": 1,
        "question": "Which sentence uses capital letters correctly for days, months, and the pronoun 'I'?",
        "options": [
            "A) On monday, i have an appointment in manchester.",
            "B) On Monday, I have an appointment in Manchester.",
            "C) On Monday, i have an appointment in Manchester."
        ],
        "answer": "B",
        "topic": "Capital Letters (Unit 1)"
    },
    {
        "q_num": 2,
        "question": "Which sentence is a question that requires a question mark at the end?",
        "options": [
            "A) What time does the afternoon shift start",
            "B) The afternoon shift starts at two o'clock",
            "C) Please arrive ten minutes before your shift starts"
        ],
        "answer": "A",
        "topic": "Sentence Boundaries & Question Marks (Unit 2)"
    },
    {
        "q_num": 3,
        "question": "Which sentence is an urgent safety warning that correctly ends with an exclamation mark?",
        "options": [
            "A) Danger! High voltage cables overhead!",
            "B) Danger? High voltage cables overhead?",
            "C) Danger. High voltage cables overhead."
        ],
        "answer": "A",
        "topic": "Exclamation Marks & Urgent Warnings (Unit 3)"
    },
    {
        "q_num": 4,
        "question": "Choose the best connective to show contrast: <em>'Liam applied for the supervisor job, [ ___ ] he did not get an interview.'</em>",
        "options": [
            "A) and",
            "B) but",
            "C) so"
        ],
        "answer": "B",
        "topic": "Compound Sentences with 'And' & 'But' (Unit 4)"
    },
    {
        "q_num": 5,
        "question": "Select the sentence that correctly explains the reason for being late:",
        "options": [
            "A) I was late so the motorway was closed.",
            "B) I was late because the motorway was closed.",
            "C) Because I was late so the motorway was closed."
        ],
        "answer": "B",
        "topic": "Giving Reasons with 'Because' & 'So' (Unit 5)"
    },
    {
        "q_num": 6,
        "question": "Which verb form correctly completes the everyday routine: <em>'Every morning, the chef [ ___ ] the kitchen equipment.'</em>?",
        "options": [
            "A) sanitize",
            "B) sanitizes",
            "C) sanitizing"
        ],
        "answer": "B",
        "topic": "Present Tense & Third-Person 's' (Unit 6)"
    },
    {
        "q_num": 7,
        "question": "Choose the correct regular past tense spelling with consonant doubling:",
        "options": [
            "A) The nurse droped the thermometer.",
            "B) The nurse dropped the thermometer.",
            "C) The nurse dropt the thermometer."
        ],
        "answer": "B",
        "topic": "Regular Past Tense with -ed (Unit 7)"
    },
    {
        "q_num": 8,
        "question": "Which sentence uses standard irregular past tense verbs?",
        "options": [
            "A) I saw the manager and took the paperwork to her office.",
            "B) I seen the manager and taked the paperwork to her office.",
            "C) I saw the manager and taked the paperwork to her office."
        ],
        "answer": "A",
        "topic": "Common Irregular Past Verbs (Unit 8)"
    },
    {
        "q_num": 9,
        "question": "Select the sentence with correct subject-verb agreement:",
        "options": [
            "A) The fire extinguishers was checked yesterday.",
            "B) The fire extinguishers were checked yesterday.",
            "C) The fire extinguishers is checked yesterday."
        ],
        "answer": "B",
        "topic": "Subject-Verb Agreement (Unit 9)"
    },
    {
        "q_num": 10,
        "question": "Which sentence correctly punctuates the list of items with commas?",
        "options": [
            "A) We ordered apples, bananas, pears and oranges.",
            "B) We ordered apples, bananas, pears, and, oranges.",
            "C) We ordered apples bananas pears and oranges."
        ],
        "answer": "A",
        "topic": "Commas in Lists & Plural Nouns (Units 10 & 11)"
    }
]


# ==============================================================================
# E3 UNIT MODELS & SYNTAX ARCHITECTURE
# Formulas, exemplars, grammatical breakdowns, extra drills, and reinforcement
# ==============================================================================

E3_MODELS = {
    1: {
        "formula": "<code>[Capital: Start of Sentence]</code> + <code>[Proper Noun: Person / Place]</code> + <code>[Pronoun 'I']</code> + <code>[Day / Month]</code> + <code>[Full Stop .]</code>",
        "exemplar": "Last Friday, Amir and I travelled to Manchester for a college training day.",
        "breakdown": "<span class='syntax-badge syntax-cap'>Sentence Starter:</span> Last &bull; <span class='syntax-badge syntax-cap'>Day:</span> Friday &bull; <span class='syntax-badge syntax-cap'>Person:</span> Amir &bull; <span class='syntax-badge syntax-cap'>Pronoun:</span> I &bull; <span class='syntax-badge syntax-cap'>City:</span> Manchester &bull; <span class='syntax-badge syntax-punc'>End Punctuation:</span> full stop .",
        "extra_drill": ("Which address is capitalised correctly for an envelope?",
                        ["A) 12 Oxford street, Leeds, LS1 4DY",
                         "B) 12 Oxford Street, Leeds, LS1 4DY",
                         "C) 12 oxford street, leeds, ls1 4dy"],
                        "B"),
        "reinforce": [
            ("Fix the missing capital letters: <em>'every tuesday i visit dr patel in bristol.'</em>",
             "Every Tuesday, I visit Dr Patel in Bristol."),
            ("Fix the personal details error: <em>'applicant: john smith from london.'</em>",
             "Applicant: John Smith from London.")
        ]
    },
    2: {
        "formula": "<code>[Question Word: Who/What/Where/When/Why/How OR Can/Do/Are]</code> + <code>[Subject]</code> + <code>[Verb Phrase]</code> + <code>[Question Mark ?]</code>",
        "exemplar": "Can you attend the community garden meeting at the library on Wednesday?",
        "breakdown": "<span class='syntax-badge syntax-conn'>Auxiliary Opener:</span> Can &bull; <span class='syntax-badge syntax-sub'>Subject:</span> you &bull; <span class='syntax-badge syntax-verb'>Base Verb:</span> attend &bull; <span class='syntax-badge syntax-punc'>End Mark:</span> question mark ?",
        "extra_drill": ("Identify the sentence that requires a question mark:",
                        ["A) How many volunteers signed the registration sheet",
                         "B) Many volunteers signed the registration sheet",
                         "C) Please sign the registration sheet before you leave"],
                        "A"),
        "reinforce": [
            ("Punctuate correctly: <em>'Where is the nearest pharmacy'</em>",
             "Where is the nearest pharmacy?"),
            ("Punctuate correctly: <em>'The library opens at nine o'clock'</em>",
             "The library opens at nine o'clock.")
        ]
    },
    3: {
        "formula": "<code>[Urgent Hazard: Danger! / Caution!]</code> + <code>[Imperative Action Verb]</code> + <code>[Safety Instruction]</code> + <code>[Full Stop .]</code>",
        "exemplar": "Caution! Slippery floor! Walk carefully and clean up any spills immediately.",
        "breakdown": "<span class='syntax-badge syntax-punc'>Warning Mark:</span> Caution! &bull; <span class='syntax-badge syntax-verb'>Imperative Verbs:</span> Walk ... clean up &bull; <span class='syntax-badge syntax-punc'>End Mark:</span> full stop .",
        "extra_drill": ("Which sentence begins with a clear imperative (bossy) verb?",
                        ["A) You must remember to lock the back door.",
                         "B) Lock the back door securely at the end of your shift.",
                         "C) Locking the back door is very important."],
                        "B"),
        "reinforce": [
            ("Rewrite as an imperative command: <em>'You should sanitize the worktop.'</em>",
             "Sanitize the worktop before preparing food."),
            ("Fix the punctuation: <em>'Stop! Forklift trucks in operation.'</em>",
             "Stop! Forklift trucks in operation!")
        ]
    },
    4: {
        "formula": "<code>[Sentence 1: Task Completed]</code> + <code>[Connective: and / but]</code> + <code>[Sentence 2: Task or Issue]</code> + <code>[Full Stop .]</code>",
        "exemplar": "I restocked the retail shelves, but the delivery driver forgot the fresh milk.",
        "breakdown": "<span class='syntax-badge syntax-sub'>Subject 1:</span> I &bull; <span class='syntax-badge syntax-verb'>Verb 1:</span> restocked &bull; <span class='syntax-badge syntax-conn'>Contrasting Connective:</span> but &bull; <span class='syntax-badge syntax-sub'>Subject 2:</span> driver &bull; <span class='syntax-badge syntax-verb'>Verb 2:</span> forgot &bull; <span class='syntax-badge syntax-punc'>End Mark:</span> full stop .",
        "extra_drill": ("Choose the correct connective: <em>'We cleaned all the tables [ ___ ] we washed the floor.'</em>",
                        ["A) and", "B) but"],
                        "A"),
        "reinforce": [
            ("Join with 'and': <em>'I counted the cash. I locked the till.'</em>",
             "I counted the cash and I locked the till."),
            ("Join with 'but': <em>'We phoned the client. Nobody answered.'</em>",
             "We phoned the client, but nobody answered.")
        ]
    },
    5: {
        "formula": "<code>[Main Statement: Absence / Delay]</code> + <code>[Connective: because / so]</code> + <code>[Reason or Result]</code> + <code>[Full Stop .]</code>",
        "exemplar": "I will arrive thirty minutes late today because my train was delayed by signal failures.",
        "breakdown": "<span class='syntax-badge syntax-sub'>Subject:</span> I &bull; <span class='syntax-badge syntax-verb'>Verb:</span> will arrive &bull; <span class='syntax-badge syntax-conn'>Reason Connective:</span> because &bull; <span class='syntax-badge syntax-sub'>Cause:</span> train was delayed &bull; <span class='syntax-badge syntax-punc'>End Mark:</span> full stop .",
        "extra_drill": ("Which sentence correctly uses 'so' to show result?",
                        ["A) The bus broke down, so I walked to the clinic.",
                         "B) I walked to the clinic, so the bus broke down.",
                         "C) The bus broke down because I walked to the clinic."],
                        "A"),
        "reinforce": [
            ("Join with 'because': <em>'I cannot work today. I have a high fever.'</em>",
             "I cannot work today because I have a high fever."),
            ("Join with 'so': <em>'The road was blocked. The driver took a detour.'</em>",
             "The road was blocked, so the driver took a detour.")
        ]
    },
    6: {
        "formula": "<code>[Singular Subject: He / She / Worker]</code> + <code>[Present Verb + s / es]</code> + <code>[Routine Workplace Task]</code> + <code>[Full Stop .]</code>",
        "exemplar": "Every morning, the receptionist welcomes visitors, checks their passes, and answers incoming calls.",
        "breakdown": "<span class='syntax-badge syntax-sub'>Singular Subject:</span> receptionist &bull; <span class='syntax-badge syntax-verb'>Third-person Verbs:</span> welcomes ... checks ... answers &bull; <span class='syntax-badge syntax-punc'>End Mark:</span> full stop .",
        "extra_drill": ("Select the correct third-person present verb:",
                        ["A) David wash the company van every Friday.",
                         "B) David washes the company van every Friday.",
                         "C) David washs the company van every Friday."],
                        "B"),
        "reinforce": [
            ("Fix the verb agreement: <em>'The security guard patrol the building.'</em>",
             "The security guard patrols the building."),
            ("Fix the verb agreement: <em>'She fix the broken printers.'</em>",
             "She fixes the broken printers.")
        ]
    },
    7: {
        "formula": "<code>[Time: Yesterday / Last shift]</code> + <code>[Subject]</code> + <code>[Regular Past Verb + ed]</code> + <code>[Workplace Details]</code> + <code>[Full Stop .]</code>",
        "exemplar": "Yesterday afternoon, the maintenance technician inspected the fire doors and repaired the lock.",
        "breakdown": "<span class='syntax-badge syntax-time'>Time:</span> Yesterday &bull; <span class='syntax-badge syntax-sub'>Subject:</span> technician &bull; <span class='syntax-badge syntax-verb'>Regular Past Verbs:</span> inspected ... repaired &bull; <span class='syntax-badge syntax-punc'>End Mark:</span> full stop .",
        "extra_drill": ("Which sentence doubles the consonant correctly in the past tense?",
                        ["A) The driver stoped at the traffic lights.",
                         "B) The driver stopped at the traffic lights.",
                         "C) The driver stopt at the traffic lights."],
                        "B"),
        "reinforce": [
            ("Change to past tense: <em>'I clean the counter and tidy the shelves.'</em>",
             "I cleaned the counter and tidied the shelves."),
            ("Fix the spelling: <em>'The worker planed the project.'</em>",
             "The worker planned the project.")
        ]
    },
    8: {
        "formula": "<code>[Subject]</code> + <code>[Irregular Past Verb: went / saw / took / had / came / did]</code> + <code>[Details]</code> + <code>[Full Stop .]</code>",
        "exemplar": "Yesterday morning, Liam went to the depot, saw the manager, and took the delivery keys.",
        "breakdown": "<span class='syntax-badge syntax-sub'>Subject:</span> Liam &bull; <span class='syntax-badge syntax-verb'>Irregular Verbs:</span> went ... saw ... took &bull; <span class='syntax-badge syntax-punc'>End Mark:</span> full stop .",
        "extra_drill": ("Which sentence uses standard irregular past verbs?",
                        ["A) The clerk comed in and dided the filing.",
                         "B) The clerk came in and did the filing.",
                         "C) The clerk came in and done the filing."],
                        "B"),
        "reinforce": [
            ("Correct the non-standard past: <em>'I seen the customer at the till.'</em>",
             "I saw the customer at the till."),
            ("Correct the non-standard past: <em>'He goed home early because he was sick.'</em>",
             "He went home early because he was sick.")
        ]
    },
    9: {
        "formula": "<code>[Singular: Subject is / has / was]</code> vs <code>[Plural: Subjects are / have / were]</code>",
        "exemplar": "The supervisor is pleased because all apprentices have passed their safety assessments.",
        "breakdown": "<span class='syntax-badge syntax-sub'>Singular:</span> supervisor is &bull; <span class='syntax-badge syntax-conn'>Connective:</span> because &bull; <span class='syntax-badge syntax-sub'>Plural:</span> apprentices have passed &bull; <span class='syntax-badge syntax-punc'>End Mark:</span> full stop .",
        "extra_drill": ("Select the sentence with correct subject-verb agreement:",
                        ["A) Both deliveries was on time today.",
                         "B) Both deliveries were on time today.",
                         "C) Both deliveries is on time today."],
                        "B"),
        "reinforce": [
            ("Fix the agreement error: <em>'The computer are broken.'</em>",
             "The computer is broken."),
            ("Fix the agreement error: <em>'You was very helpful yesterday.'</em>",
             "You were very helpful yesterday.")
        ]
    },
    10: {
        "formula": "<code>[Intro Clause]</code> + <code>[Item 1],</code> <code>[Item 2],</code> <code>[Item 3] and </code> <code>[Item 4].</code>",
        "exemplar": "The chef ordered potatoes, carrots, onions and garlic for the restaurant soup.",
        "breakdown": "<span class='syntax-badge syntax-sub'>Subject:</span> chef &bull; <span class='syntax-badge syntax-verb'>Verb:</span> ordered &bull; <span class='syntax-badge syntax-punc'>List Commas:</span> potatoes, carrots, onions &bull; <span class='syntax-badge syntax-conn'>Final Conjunction:</span> and garlic &bull; <span class='syntax-badge syntax-punc'>End Mark:</span> .",
        "extra_drill": ("Which sentence punctuates the tool list correctly?",
                        ["A) We need a hammer, nails, tape and a screwdriver.",
                         "B) We need a hammer, nails, tape, and, a screwdriver.",
                         "C) We need a hammer nails tape and a screwdriver."],
                        "A"),
        "reinforce": [
            ("Add commas: <em>'Please buy apples oranges lemons and bananas.'</em>",
             "Please buy apples, oranges, lemons and bananas."),
            ("Fix unnecessary comma: <em>'We need pens, pencils, and, paper.'</em>",
             "We need pens, pencils and paper.")
        ]
    },
    11: {
        "formula": "<code>[Regular: -s]</code> + <code>[Hissing: -es]</code> + <code>[Consonant + y: -ies]</code>",
        "exemplar": "The stockroom contains fifty boxes, twenty batteries, and thirty notebooks.",
        "breakdown": "<span class='syntax-badge syntax-noun'>-es Plural:</span> boxes (from box) &bull; <span class='syntax-badge syntax-noun'>-ies Plural:</span> batteries (from battery) &bull; <span class='syntax-badge syntax-noun'>-s Plural:</span> notebooks &bull; <span class='syntax-badge syntax-punc'>End Mark:</span> .",
        "extra_drill": ("Select the correct plural form of 'sandwich':",
                        ["A) sandwichs", "B) sandwiches", "C) sandwich's"],
                        "B"),
        "reinforce": [
            ("Make plural: <em>'one city &rarr; two ...'</em>",
             "two cities"),
            ("Make plural: <em>'one glass &rarr; three ...'</em>",
             "three glasses")
        ]
    }
}


# ==============================================================================
# E3 COMPLETE ANSWERS REPOSITORY
# Full answer keys for Units 1–11, Spelling Test, Workouts & Diagnostic
# ==============================================================================

E3_ANSWERS = {
    "units": {
        1: {
            "title": "Unit 1: Capital Letters for 'I', Names, Places, Days & Months",
            "exercise_a": [
                ("Q1", "B", "The personal pronoun 'I' must always be capitalised on its own ('When I finish work, I walk home')."),
                ("Q2", "B", "Days of the week ('Tuesday') and months of the year ('November') require capital letters."),
                ("Q3", "A", "Both street names ('High Street') and city names ('Manchester') require capital letters."),
                ("Q4", "B", "'On' starts the sentence; 'Wednesday' is a day; 'Amir' is a name; 'I' is the personal pronoun; 'Bristol' is a city.")
            ],
            "proofreading_errors": [
                "Applicant name missing capital letters: 'mark stevens' -> 'Mark Stevens'",
                "Sentence starting with small 'i': 'i am writing' -> 'I am writing'",
                "Company proper noun missing capital letter: 'tesco' -> 'Tesco'",
                "Pronoun 'i' in question missing capital letter: 'Can i attend' -> 'Can I attend'",
                "Place name and day of the week missing capital letters: 'leeds on thursday' -> 'Leeds on Thursday'"
            ],
            "model_writing": "Last Friday, I travelled to Leeds to visit my aunt. We walked along Queen Street and had lunch in the market."
        },
        2: {
            "title": "Unit 2: Full Stops & Question Marks: Statements vs Questions",
            "exercise_a": [
                ("Q1", "B", "'Where can I register for computer classes' asks for information, so it requires a question mark (?)."),
                ("Q2", "C", "'The workshop takes place in Room 4' gives information (statement), so it ends with a full stop (.)."),
                ("Q3", "A", "Sentence 1 asks a question ('?'); Sentence 2 states a fact ('.')."),
                ("Q4", "B", "'Do you need help with your council tax form?' starts with auxiliary 'Do' and asks for information, so it needs a question mark.")
            ],
            "proofreading_errors": [
                "Question incorrectly ended with a full stop: 'or tablet.' -> 'or tablet?'",
                "Statement incorrectly ended with a question mark: 'Wednesday afternoon?' -> 'Wednesday afternoon.'",
                "Missing full stop at the end of the sentence: 'computer experience' -> 'computer experience.'",
                "Question incorrectly ended with a full stop: 'a space today.' -> 'a space today?'",
                "Statement incorrectly ended with a question mark: 'free of charge?' -> 'free of charge.'"
            ],
            "model_writing": "The community football club meets every Saturday at 10:00 AM. Would you like to come along and join the team?"
        },
        3: {
            "title": "Unit 3: Exclamation Marks & Urgent Instructions",
            "exercise_a": [
                ("Q1", "A", "'Watch out! The metal surface is extremely hot!' expresses urgent danger and correctly uses exclamation marks."),
                ("Q2", "B", "'Switch off the computer at the end of your shift' begins with the imperative action verb 'Switch off'."),
                ("Q3", "A", "'Danger!' has an exclamation mark for the hazard, followed by a calm imperative rule ending in a full stop."),
                ("Q4", "C", "'Sanitise' is the imperative action verb telling the worker what action to take.")
            ],
            "proofreading_errors": [
                "Missing capital letter on urgent hazard alert: 'danger!' -> 'Danger!'",
                "Routine hygiene step overusing exclamation mark: 'raw chicken!' -> 'raw chicken.'",
                "Routine storage rule overusing exclamation mark: 'of the fridge!' -> 'of the fridge.'",
                "Missing capital letter at start of imperative sentence: 'clean all' -> 'Clean all'",
                "Instruction incorrectly ended with a question mark: 'chef marco immediately?' -> 'Chef Marco immediately.'"
            ],
            "model_writing": "Caution! Falling boxes! Stack all heavy crates on the ground floor shelves."
        },
        4: {
            "title": "Unit 4: Joining Sentences with 'And' & 'But'",
            "exercise_a": [
                ("Q1", "A", "Liam completed two similar tasks, so 'and' is the correct connective."),
                ("Q2", "B", "The driver's phone being switched off is an unexpected obstacle/contrast, so 'but' is correct."),
                ("Q3", "B", "'I answered customer emails and I filed the paper invoices' connects two completed duties smoothly."),
                ("Q4", "A", "'The customer liked the sofa, but she could not afford the delivery fee' correctly contrasts interest with a problem.")
            ],
            "proofreading_errors": [
                "Missing comma after informal greeting: 'Hi Priya.' -> 'Hi Priya,'",
                "Incorrect connective for positive achievement: 'hectic but we managed' -> 'hectic, and we managed' (or add comma before 'but')",
                "Incorrect connective for unexpected problem: 'muffins and the oven temperature gauge broke' -> 'muffins, but the oven temperature gauge broke'",
                "Missing capital letter for day of the week: 'wednesday' -> 'Wednesday'",
                "Run-on sentence between clauses: 'on Wednesday he will fix' -> 'on Wednesday, and he will fix'"
            ],
            "model_writing": "I restocked the fruit display and I swept the front aisle. We received fifty bakery rolls, but six packages were crushed."
        },
        5: {
            "title": "Unit 5: Giving Reasons & Results: 'Because' & 'So'",
            "exercise_a": [
                ("Q1", "A", "'Because' explains the reason why Chloe stayed home (high fever)."),
                ("Q2", "B", "'So' introduces the result of the van breaking down (packages arrived late)."),
                ("Q3", "B", "'I cannot attend work because I have a medical appointment' correctly introduces the cause/reason."),
                ("Q4", "A", "'The road was flooded, so buses were diverted' correctly shows the cause followed by the result.")
            ],
            "proofreading_errors": [
                "Missing capital letter on pronoun 'I': 'i am very sorry' -> 'I am very sorry'",
                "Incorrect connective for giving a reason: 'today so my boiler burst' -> 'today because my boiler burst'",
                "Reversed cause and effect: 'flooded because I need to wait' -> 'flooded, so I need to wait'",
                "Missing capital letter on pronoun: 'so i have' -> 'so I have'",
                "Missing full stop at the end of the message: 'laptop with me' -> 'laptop with me.'"
            ],
            "model_writing": "I will be thirty minutes late tomorrow because my boiler engineer is visiting at 8:00 AM. I will work through my lunch break, so all my daily reports will still be completed on time."
        },
        6: {
            "title": "Unit 6: Present Tense: Everyday Routines & Regular Verbs",
            "exercise_a": [
                ("Q1", "B", "'Supervisor' is singular (he/she), so the verb requires -s ('checks')."),
                ("Q2", "A", "'Apprentices' is plural (they), so the verb takes the base form ('attend')."),
                ("Q3", "B", "'Watch' ends in -ch, so it adds -es in the third person ('watches')."),
                ("Q4", "B", "'I prepare' (first-person base) and 'Michael serves' (third-person singular with -s).")
            ],
            "proofreading_errors": [
                "Missing -s on third-person verb: 'Gemma greet' -> 'Gemma greets'",
                "Missing -s on third-person verb: 'and help them' -> 'and helps them'",
                "Missing -s on third-person verb: 'She check' -> 'She checks'",
                "Missing -es on verb ending in -sh: 'she wash' -> 'she washes'",
                "Missing -es on verb ending in -ss: 'manager discuss' -> 'manager discusses'"
            ],
            "model_writing": "Every morning, I unlock the filing cabinets and check my emails. My colleague David answers the reception telephone and welcomes visitors."
        },
        7: {
            "title": "Unit 7: Past Tense: Regular Verbs with -ed",
            "exercise_a": [
                ("Q1", "B", "The action happened at 10:00 PM yesterday, so the regular past tense 'locked' is required."),
                ("Q2", "B", "'Stop' has one short vowel and one consonant, so the consonant doubles before -ed ('stopped')."),
                ("Q3", "B", "'Tidy' ends in a consonant + y, so 'y' changes to 'i' before -ed ('tidied')."),
                ("Q4", "A", "Both regular verbs are spelled correctly in the past tense ('repaired' and 'painted').")
            ],
            "proofreading_errors": [
                "Missing past tense ending on regular verb: 'slip' -> 'slipped'",
                "Consonant doubling error: 'droped' -> 'dropped'",
                "Missing past tense ending on regular verb: 'inspect' -> 'inspected'",
                "Missing past tense ending on regular verb: 'clean' -> 'cleaned'",
                "Missing past tense ending on regular verb ending in e: 'arrive' -> 'arrived'"
            ],
            "model_writing": "Yesterday afternoon, I cleaned the staff kitchen and inspected the emergency fire doors. I reported the completed tasks to my line manager."
        },
        8: {
            "title": "Unit 8: Common Irregular Past Verbs",
            "exercise_a": [
                ("Q1", "B", "The past tense of 'go' is 'went' (never 'goed')."),
                ("Q2", "A", "Standard English requires 'saw' (never 'I seen' without a helper verb)."),
                ("Q3", "A", "The past tense of 'take' is 'took' and the past tense of 'do' is 'did' ('took ... did')."),
                ("Q4", "A", "'Came', 'had', and 'said' are all standard irregular past verbs.")
            ],
            "proofreading_errors": [
                "Incorrect past tense of 'go': 'goed' -> 'went'",
                "Non-standard past tense of 'see': 'I seen' -> 'I saw'",
                "Incorrect regularised past of 'come': 'comed' -> 'came'",
                "Incorrect regularised past of 'have': 'haved' -> 'had'",
                "Non-standard past of 'do' and 'take': 'I done' -> 'I did'; 'taked' -> 'took'"
            ],
            "model_writing": "Yesterday I went to the main warehouse and saw the delivery supervisor. I had a quick meeting with the team and took the signed paperwork back to the office."
        },
        9: {
            "title": "Unit 9: Subject-Verb Agreement: Singular vs Plural",
            "exercise_a": [
                ("Q1", "A", "'Photocopier' is singular, so it takes 'is' ('photocopier is')."),
                ("Q2", "B", "'Staff members' is plural, so it takes 'have' ('members have requested')."),
                ("Q3", "B", "In standard English, 'you' always takes the plural verb 'were' ('You were very helpful')."),
                ("Q4", "B", "'Desk is closed' (singular) and 'lights are off' (plural).")
            ],
            "proofreading_errors": [
                "Plural subject requires plural verb: 'members is reminded' -> 'members are reminded'",
                "Plural subject requires plural verb: 'meeting rooms is closed' -> 'meeting rooms are closed'",
                "Plural subject requires plural verb: 'decorators has completed' -> 'decorators have completed'",
                "Plural pronoun requires plural past verb: 'we was unable' -> 'we were unable'",
                "Singular subject requires singular verb: 'facility manager have ordered' -> 'facility manager has ordered'"
            ],
            "model_writing": "The new laser printer is located on the ground floor. All department staff members are welcome to collect their access cards today."
        },
        10: {
            "title": "Unit 10: Commas in Simple Lists",
            "exercise_a": [
                ("Q1", "B", "'pens, paper, envelopes and stamps' uses commas between items and connects the final item with 'and' without extra commas."),
                ("Q2", "A", "'windows, doors, lights and heaters' separates list items correctly."),
                ("Q3", "A", "Commas belong after 'shampoo' and 'conditioner' ('shampoo, conditioner, towels and hairspray')."),
                ("Q4", "A", "'potatoes, onions, carrots and garlic' follows the standard list rule.")
            ],
            "proofreading_errors": [
                "Missing commas in list of items: 'flour brown sugar yeast and' -> 'flour, brown sugar, yeast and'",
                "Missing full stop at end of sentence 1: 'Monday morning' -> 'Monday morning.'",
                "Unnecessary commas before and after 'and': 'extract, and, ground' -> 'extract and ground'",
                "Missing commas in list of items: 'napkins wooden stirrers coffee beans and' -> 'napkins, wooden stirrers, coffee beans and'",
                "Full stop must be placed at the end of the sentence."
            ],
            "model_writing": "For the afternoon workshop, we need marker pens, flip charts, sticky notes and name badges. Please ensure all items are on the table before 1:00 PM."
        },
        11: {
            "title": "Unit 11: Plural Nouns: Adding -s, -es, and Changing -y to -ies",
            "exercise_a": [
                ("Q1", "B", "'Box' ends in -x (hissing sound), so it adds -es ('boxes')."),
                ("Q2", "C", "'Delivery' ends in consonant + y, so 'y' changes to -ies ('deliveries')."),
                ("Q3", "A", "'boxes', 'dishes', and 'glasses' all add -es correctly without apostrophes."),
                ("Q4", "B", "'companies' (consonant + y -> -ies) and 'branches' (-ch ending -> -es).")
            ],
            "proofreading_errors": [
                "Incorrect apostrophe used for regular plural: 'pillow\\'s' -> 'pillows'",
                "Incorrect -es added to regular noun: 'blanketes' -> 'blankets'",
                "Missing -es on hissing sound noun: 'dishs' -> 'dishes'",
                "Incorrect apostrophe used for regular plural: 'bar\\'s' -> 'bars'",
                "Incorrect plurals on consonant+y and hissing nouns: 'batterys' -> 'batteries'; 'torchs' -> 'torches'"
            ],
            "model_writing": "During the morning stocktake, we counted forty boxes of supplies and checked twenty emergency batteries. We also filed all customer receipts."
        }
    },
    "spelling_test": [
        ("Q1", "B", "Nouns ending in -ss add -es to form plurals: 'glasses'."),
        ("Q2", "C", "Drop the silent 'e' before adding -ing: 'write' -> 'writing'."),
        ("Q3", "B", "Short 1-syllable word with 1 vowel and 1 consonant doubles the consonant: 'stopped'."),
        ("Q4", "B", "'Their' shows possession (belonging to the students: 'their ID badges')."),
        ("Q5", "B", "'Too' means excessively ('too cold')."),
        ("Q6", "B", "The suffix -ful is always spelled with one 'l': 'careful'."),
        ("Q7", "C", "Remember the internal 'r': 'February'."),
        ("Q8", "B", "Standard spelling with two 'r's: 'library'."),
        ("Q9", "A", "Standard spelling: 'medicine'."),
        ("Q10", "B", "Consonant + y changes to -ies in the plural: 'deliveries'.")
    ],
    "mixed_workout": {
        1: [
            "Missing capital letter on pronoun: 'i unpacked' -> 'I unpacked'",
            "Subject-verb agreement error: 'crates was damaged' -> 'crates were damaged'",
            "Consonant doubling spelling error: 'stoped' -> 'stopped'",
            "Missing capital letter on day: 'on wednesday' -> 'on Wednesday'",
            "Question mark missing at end of question: 'on Wednesday.' -> 'on Wednesday?'"
        ],
        2: [
            "Missing capital letter on day: 'on friday' -> 'on Friday'",
            "Subject-verb agreement error: 'contractors is' -> 'contractors are'",
            "Missing capital letter on street name: 'Church road' -> 'Church Road'",
            "Statement ending with question mark: 'their permit?' -> 'their permit.'",
            "Urgent instruction punctuation: 'ambulance bays!' -> 'ambulance bays.'"
        ]
    },
    "diagnostic": [
        ("Q1", "B", "'On' starts the sentence; 'Monday' is a day; 'I' is the personal pronoun; 'Manchester' is a city."),
        ("Q2", "A", "'What time does the afternoon shift start' asks for information, so it requires a question mark (?)."),
        ("Q3", "A", "'Danger! High voltage cables overhead!' gives an urgent emergency warning and correctly ends with an exclamation mark."),
        ("Q4", "B", "'But' shows the contrasting outcome between applying and not being interviewed."),
        ("Q5", "B", "'Because' explains the reason why the speaker was late (motorway closed)."),
        ("Q6", "B", "'The chef' is singular (he/she), so the present simple verb takes -s: 'sanitizes'."),
        ("Q7", "B", "'Drop' is a 1-syllable word with 1 short vowel and 1 consonant, so the 'p' doubles: 'dropped'."),
        ("Q8", "A", "'Saw' and 'took' are standard irregular past tense verbs in English."),
        ("Q9", "B", "'Extinguishers' is plural, so it requires the plural past verb 'were' ('extinguishers were checked')."),
        ("Q10", "A", "'apples, bananas, pears and oranges' uses commas between items and connects the final item with 'and'.")
    ]
}


# ==============================================================================
# INTEGRITY VERIFICATION & SUMMARY BLOCK
# ==============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("MASTER FUNCTIONAL SKILLS ENGLISH - ENTRY LEVEL 3 SPaG CURRICULUM")
    print("=" * 70)
    print(f"Total Units Loaded: {len(E3_UNITS)}")
    print(f"Total Spelling Rules: {len(E3_SPELLING_DATA['rules'])}")
    total_exceptions = sum(len(words) for _, words in E3_SPELLING_DATA['common_exception_words'])
    print(f"Total Common Exception Words: {total_exceptions}")
    print(f"Total Spelling Test Questions: {len(E3_SPELLING_DATA['spelling_test'])}")
    print(f"Total Mixed Workouts: {len(E3_MIXED_WORKOUT)}")
    print(f"Total Diagnostic MCQs: {len(E3_DIAGNOSTIC)}")
    print(f"Total Unit Models: {len(E3_MODELS)}")
    print(f"Total Units in Answer Key: {len(E3_ANSWERS['units'])}")
    print("=" * 70)
    assert len(E3_UNITS) == 11, "Must have exactly 11 units"
    assert total_exceptions == 60, f"Must have exactly 60 common exception words, found {total_exceptions}"
    assert len(E3_MIXED_WORKOUT) == 2, "Must have exactly 2 mixed workouts"
    assert len(E3_DIAGNOSTIC) == 10, "Must have exactly 10 diagnostic questions"
    assert len(E3_MODELS) == 11, "Must have exactly 11 unit models"
    assert len(E3_ANSWERS["units"]) == 11, "Must have answers for all 11 units"
    print("ALL ASSERTIONS PASSED! File integrity verified.")
