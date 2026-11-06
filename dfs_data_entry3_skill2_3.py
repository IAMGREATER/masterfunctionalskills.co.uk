# -*- coding: utf-8 -*-
"""
Master Functional Skills (MFS) - Entry 3 Digital Skills (Skill Areas 2 & 3)
Author: Abdul (MFS Pedagogical Systems)
"""

ENTRY_3_SKILL_2_3 = [
    # -------------------------------------------------------------------------
    # Skill Area 2: Creating and Editing
    # -------------------------------------------------------------------------
    {
        "slug": "e3-word-processing-basics",
        "code": "E3.2.1",
        "skill_area": "2. Creating and Editing",
        "title": "Word Processing: Entering Text and Fonts",
        "time": "15 Mins",
        "lead": "Learn how to open a word processor, enter text cleanly, select words and paragraphs, change font styles and sizes, and apply bold, italic, and underline styling for emphasis.",
        "objectives": [
            "Open a blank document and type text with correct spacing",
            "Select text using mouse dragging, double-clicking, and keyboard commands",
            "Format text using Font Family, Font Size, Bold (Ctrl+B), Italic (Ctrl+I), and Colour"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Entry 3 Digital Skills - Word Processing Fonts & Text Basics",
        "steps": [
            {
                "title": "Opening a Document and Typing Clean Text",
                "body": "<p>When opening Microsoft Word or Google Docs, choose <strong>Blank Document</strong>. Click into the white page where you see the blinking cursor (insertion point) and begin typing.</p><p>Remember: Only press <kbd class='dfs-kbd'>Enter</kbd> at the end of a paragraph, not at the end of every line. The computer automatically wraps words onto the next line.</p>",
                "shortcuts": [
                    {"label": "New Blank Document", "key": "Ctrl + N"},
                    {"label": "Select All Text", "key": "Ctrl + A"}
                ]
            },
            {
                "title": "Selecting and Highlighting Text",
                "body": "<p>To change how text looks, you must select it first:</p><ul><li><strong>Single Word:</strong> Double-click the word with the left mouse button.</li><li><strong>Entire Paragraph:</strong> Triple-click anywhere inside the paragraph.</li><li><strong>Custom Sentence:</strong> Click and drag your mouse cursor over the words.</li></ul>",
                "callout": {
                    "type": "tutor",
                    "title": "Tutor Abdul's Golden Rule",
                    "text": "Always remember: <strong>Select first, then format!</strong> If no text is selected, font changes will not apply to your existing words."
                }
            },
            {
                "title": "Font Families, Sizes, and Emphasis",
                "body": "<p>On the <strong>Home Ribbon</strong>, locate the <strong>Font group</strong>:</p><ul><li><strong>Font Family:</strong> Clean sans-serif fonts like <strong>Arial</strong>, <strong>Calibri</strong>, or <strong>Lexend</strong> are recommended for dyslexia readability.</li><li><strong>Font Size:</strong> Standard body text is <strong>11 or 12 pt</strong>. Headings should be larger (e.g. <strong>16 to 20 pt</strong>).</li><li><strong>Bold (<kbd class='dfs-kbd'>Ctrl + B</kbd>):</strong> Makes letters thicker for main headings.</li><li><strong>Italic (<kbd class='dfs-kbd'>Ctrl + I</kbd>):</strong> Slants letters for quotes or book titles.</li><li><strong>Underline (<kbd class='dfs-kbd'>Ctrl + U</kbd>):</strong> Adds a line beneath text.</li></ul>",
                "ui_sim": {
                    "title": "Word Processing Font Ribbon Toolbar",
                    "content": "<div style='display:flex; align-items:center; gap:8px; background:#f8fafc; padding:8px 12px; border-radius:4px; border:1px solid #cbd5e1; flex-wrap:wrap;'><div style='background:#ffffff; border:1px solid #94a3b8; padding:4px 8px; border-radius:4px; font-weight:600;'>Lexend <i class='fa-solid fa-chevron-down' style='font-size:0.7rem;'></i></div><div style='background:#ffffff; border:1px solid #94a3b8; padding:4px 8px; border-radius:4px; font-weight:600;'>14 <i class='fa-solid fa-chevron-down' style='font-size:0.7rem;'></i></div><button style='background:#e2e8f0; border:1px solid #cbd5e1; padding:4px 10px; font-weight:800; border-radius:4px;'>B</button><button style='background:#e2e8f0; border:1px solid #cbd5e1; padding:4px 10px; font-style:italic; border-radius:4px;'>I</button><button style='background:#e2e8f0; border:1px solid #cbd5e1; padding:4px 10px; text-decoration:underline; border-radius:4px;'>U</button><div style='border-left:1px solid #cbd5e1; height:24px; margin:0 4px;'></div><div style='display:flex; align-items:center; gap:2px; font-weight:700;'><span style='color:#dc2626;'>A</span><i class='fa-solid fa-caret-down' style='font-size:0.7rem;'></i></div></div>"
                },
                "shortcuts": [
                    {"label": "Make Text Bold", "key": "Ctrl + B"},
                    {"label": "Make Text Italic", "key": "Ctrl + I"},
                    {"label": "Underline Text", "key": "Ctrl + U"}
                ]
            }
        ],
        "exam_model": {
            "scenario": "A health centre worker is typing a notice titled 'Clinic Opening Hours'. The instructions state: 'Make the title Bold, Font Size 18, and change the font to Arial.' Describe the steps required to carry out this formatting.",
            "steps": [
                {
                    "action": "Highlight the title",
                    "solution": "Click and drag across 'Clinic Opening Hours' to select the text.",
                    "mark": "[B1]",
                    "rationale": "Text must be selected before applying font properties."
                },
                {
                    "action": "Apply Font Size and Family",
                    "solution": "In the Home ribbon, change font dropdown to 'Arial' and size dropdown to '18'.",
                    "mark": "[M1]",
                    "rationale": "Correctly changes font attributes from the toolbar."
                },
                {
                    "action": "Apply Bold emphasis",
                    "solution": "Click the 'B' button (or press Ctrl + B).",
                    "mark": "[A1]",
                    "rationale": "Applies bold formatting accurately."
                }
            ],
            "tutor_rule": "In Entry 3 onscreen tests, you will be given an unformatted text document and asked to format the heading. Always check: Size, Font name, and Bold."
        },
        "drills": [
            {
                "question": "What keyboard shortcut quickly turns selected text into BOLD?",
                "options": [
                    {"text": "Ctrl + B", "correct": True},
                    {"text": "Ctrl + U", "correct": False},
                    {"text": "Ctrl + S", "correct": False},
                    {"text": "Ctrl + P", "correct": False}
                ],
                "explanation": "Ctrl + B toggles Bold emphasis on and off for selected words."
            },
            {
                "question": "How can you select a single word quickly with the mouse without dragging?",
                "options": [
                    {"text": "Single-click on the word", "correct": False},
                    {"text": "Double-click on the word", "correct": True},
                    {"text": "Right-click the mouse scroll wheel", "correct": False},
                    {"text": "Hold the spacebar", "correct": False}
                ],
                "explanation": "Double-clicking any word immediately highlights that entire word."
            },
            {
                "question": "Why is it important to use clear sans-serif fonts (like Lexend, Arial, or Calibri) in workplace notices?",
                "options": [
                    {"text": "They use less printer ink than any other font", "correct": False},
                    {"text": "They are clean and much easier for people with dyslexia and visual impairments to read", "correct": True},
                    {"text": "Computers cannot open documents with serif fonts", "correct": False},
                    {"text": "Word processors automatically delete fancy fonts", "correct": False}
                ],
                "explanation": "Clean sans-serif fonts provide distinct letter shapes that enhance readability and accessibility."
            }
        ],
        "practice": {
            "task": "You are creating a staff notice for your department. Explain step-by-step how to make the main heading 'Staff Fire Drill Notice' stand out clearly from the rest of the text.",
            "scaffold_starter": "Step 1: Select the text by...\nStep 2: Increase the font size to...\nStep 3: Make it bold by...",
            "model_answer": "Step 1: Click and drag over 'Staff Fire Drill Notice' to highlight it.\nStep 2: Change the font size on the ribbon to 16 or 18 pt to make it larger than body text.\nStep 3: Click the Bold button (or press Ctrl + B) and centre-align the title on the page.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Selecting/highlighting the heading."},
                {"tag": "[1 Mark]", "desc": "Increasing font size and applying bold emphasis."}
            ]
        },
        "revision_links": [
            {"label": "Document Formatting & Bullets", "href": "e3-formatting-aligning-bullets.html"},
            {"label": "Inserting Images", "href": "e3-combining-images-text.html"},
            {"label": "Spellchecking & Saving", "href": "e3-spellcheck-proofing-saving.html"}
        ]
    },
    {
        "slug": "e3-formatting-aligning-bullets",
        "code": "E3.2.2",
        "skill_area": "2. Creating and Editing",
        "title": "Document Formatting and Bullet Lists",
        "time": "15 Mins",
        "lead": "Master paragraph alignment (left, centre, right), line spacing, creating bulleted lists for key points, and numbered lists for sequential step-by-step instructions.",
        "objectives": [
            "Align paragraphs to the left, centre, or right margin",
            "Create bulleted lists for unordered items and numbered lists for sequential instructions",
            "Adjust line spacing and paragraph indents for a neat, professional layout"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Entry 3 Digital Skills - Alignment & Bullet Lists",
        "steps": [
            {
                "title": "Paragraph Alignment: Left, Centre, and Right",
                "body": "<p>Alignment controls where your text sits across the width of the page:</p><ul><li><strong>Align Left (<kbd class='dfs-kbd'>Ctrl + L</kbd>):</strong> Standard for English text. Lines start neatly down the left margin with a jagged right margin. Easiest to read.</li><li><strong>Centre (<kbd class='dfs-kbd'>Ctrl + E</kbd>):</strong> Positions text right in the middle. Perfect for titles, certificates, and poster headers.</li><li><strong>Align Right (<kbd class='dfs-kbd'>Ctrl + R</kbd>):</strong> Aligns text against the right margin. Often used for dates and letter sender addresses.</li></ul>",
                "shortcuts": [
                    {"label": "Left Align", "key": "Ctrl + L"},
                    {"label": "Centre Align", "key": "Ctrl + E"},
                    {"label": "Right Align", "key": "Ctrl + R"}
                ]
            },
            {
                "title": "Bulleted Lists vs Numbered Lists",
                "body": "<p>Lists break up big blocks of text, making information quick to scan:</p><ul><li><strong>Bullet Points (&bull;):</strong> Use when the <strong>order does not matter</strong> (e.g. equipment needed, ingredients, job perks).</li><li><strong>Numbered Lists (1, 2, 3...):</strong> Use when the <strong>sequence is critical</strong> (e.g. recipes, evacuation procedures, login steps).</li></ul>",
                "ui_sim": {
                    "title": "List Formatting Ribbon Tools",
                    "content": "<div style='display:flex; gap:16px; align-items:center; background:#f8fafc; padding:10px 14px; border-radius:4px; border:1px solid #cbd5e1;'><div style='display:flex; gap:6px;'><button style='background:#ffffff; border:1px solid #94a3b8; padding:4px 8px; border-radius:4px;'><i class='fa-solid fa-list-ul'></i> Bullets</button><button style='background:#ffffff; border:1px solid #94a3b8; padding:4px 8px; border-radius:4px;'><i class='fa-solid fa-list-ol'></i> Numbering</button></div><div style='border-left:1px solid #cbd5e1; height:24px;'></div><div style='display:flex; gap:4px;'><button style='background:#e0f2fe; border:1px solid #0284c7; padding:4px 8px; border-radius:4px;'><i class='fa-solid fa-align-left'></i></button><button style='background:#ffffff; border:1px solid #94a3b8; padding:4px 8px; border-radius:4px;'><i class='fa-solid fa-align-center'></i></button><button style='background:#ffffff; border:1px solid #94a3b8; padding:4px 8px; border-radius:4px;'><i class='fa-solid fa-align-right'></i></button></div></div>"
                }
            },
            {
                "title": "Removing and Adjusting Lists",
                "body": "<p>To turn a list back into normal paragraphs, select the items and click the <strong>Bullets button</strong> again to toggle it off. To finish a list while typing, press <kbd class='dfs-kbd'>Enter</kbd> twice.</p>",
                "callout": {
                    "type": "tutor",
                    "title": "Tutor Abdul's Checklist Tip",
                    "text": "In Entry 3 exams, you are frequently asked: 'Format the items into a bulleted list'. Simply select all the items and click the Bullets button once!"
                }
            }
        ],
        "exam_model": {
            "scenario": "A medical training guide contains five safety rules printed as a single cramped paragraph. Explain how the guide creator can format this information into a bulleted list to make it easier for trainees to read.",
            "steps": [
                {
                    "action": "Separate the points",
                    "solution": "Place each safety rule on its own separate line using Enter.",
                    "mark": "[B1]",
                    "rationale": "Each list entry requires its own line."
                },
                {
                    "action": "Apply Bullet points",
                    "solution": "Select all five lines and click the Bullets button on the Home ribbon.",
                    "mark": "[M1]",
                    "rationale": "Converts plain lines into an aligned bulleted list with consistent left indentation."
                }
            ],
            "tutor_rule": "Numbered lists are for steps; bullet points are for items. Don't mix them up in the exam!"
        },
        "drills": [
            {
                "question": "When should you choose a NUMBERED list instead of a bulleted list?",
                "options": [
                    {"text": "When the order of steps matters (e.g. step 1, step 2, step 3)", "correct": True},
                    {"text": "Only when writing poetry", "correct": False},
                    {"text": "When typing someone's home address", "correct": False},
                    {"text": "When writing an email subject line", "correct": False}
                ],
                "explanation": "Numbered lists indicate strict chronological order or step-by-step procedures."
            },
            {
                "question": "What alignment is typically used for the main title on a flyer or certificate?",
                "options": [
                    {"text": "Centre Alignment", "correct": True},
                    {"text": "Right Alignment", "correct": False},
                    {"text": "Justified Alignment", "correct": False},
                    {"text": "Upside Down Alignment", "correct": False}
                ],
                "explanation": "Centre alignment creates balance and prominence for main document titles."
            },
            {
                "question": "What keyboard shortcut aligns selected text to the LEFT margin in Microsoft Word?",
                "options": [
                    {"text": "Ctrl + L", "correct": True},
                    {"text": "Ctrl + E", "correct": False},
                    {"text": "Ctrl + R", "correct": False},
                    {"text": "Ctrl + J", "correct": False}
                ],
                "explanation": "Ctrl + L aligns text to the left; Ctrl + E centres; Ctrl + R aligns right."
            }
        ],
        "practice": {
            "task": "You are creating a meeting agenda. Write down how you would format the title 'Team Planning Meeting' and the three agenda items: '1. Welcome', '2. Budget Review', '3. Next Steps'.",
            "scaffold_starter": "Title formatting: \nAgenda items formatting: ",
            "model_answer": "Title: Centre-aligned, bold, and font size 16 pt.\nAgenda items: Formatted as a numbered list (1, 2, 3) left-aligned for clear sequential order.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Specifying centre alignment and bold for title."},
                {"tag": "[1 Mark]", "desc": "Specifying a numbered list for the sequential agenda points."}
            ]
        },
        "revision_links": [
            {"label": "Word Processing Basics", "href": "e3-word-processing-basics.html"},
            {"label": "Inserting & Resizing Images", "href": "e3-combining-images-text.html"},
            {"label": "Spellchecking & Saving", "href": "e3-spellcheck-proofing-saving.html"}
        ]
    },
    {
        "slug": "e3-combining-images-text",
        "code": "E3.2.3",
        "skill_area": "2. Creating and Editing",
        "title": "Inserting and Resizing Images",
        "time": "15 Mins",
        "lead": "Learn how to insert pictures and digital logos into documents, resize images proportionally from corner handles without stretching, crop unwanted borders, and position them neatly alongside text.",
        "objectives": [
            "Insert an image into a document from your computer or cloud storage",
            "Resize images proportionally using corner handles without distortion",
            "Use Crop to cut away unwanted outer borders and position images neatly"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Entry 3 Digital Skills - Inserting & Resizing Pictures",
        "steps": [
            {
                "title": "Inserting a Picture",
                "body": "<p>Adding photos or company logos enhances visual interest and communication:</p><ol><li>Click on the page where you want the picture to appear.</li><li>Go to the <strong>Insert</strong> tab on the top ribbon.</li><li>Click <strong>Pictures &gt; This Device</strong>.</li><li>Browse to your folder (e.g. <strong>Pictures</strong>), click your file, and click <strong>Insert</strong>.</li></ol>",
                "shortcuts": [
                    {"label": "Copy Picture", "key": "Ctrl + C"},
                    {"label": "Paste Picture", "key": "Ctrl + V"}
                ]
            },
            {
                "title": "Resizing Images Proportionally (No Squashing!)",
                "body": "<p>When you click on an inserted picture, a border with eight small circular dots (called <strong>sizing handles</strong>) appears around the edges.</p><ul><li><strong>CORRECT: Drag from a CORNER handle:</strong> Both the width and height change together equally. The image stays proportional and natural.</li><li><strong>INCORRECT: Dragging from side or top handles:</strong> This squashes or stretches the photo, making people look abnormally wide or squashed.</li></ul>",
                "callout": {
                    "type": "warning",
                    "title": "Examiner Marking Trap",
                    "text": "Examiners will deduct marks if an image appears visibly stretched or distorted. Always drag from the <strong>corner circles</strong>!"
                }
            },
            {
                "title": "Cropping and Text Wrapping",
                "body": "<p>To trim away unwanted background clutter:</p><ol><li>Click the picture to open the <strong>Picture Format</strong> tab.</li><li>Click the <strong>Crop tool</strong> (<i class='fa-solid fa-crop-simple'></i>).</li><li>Drag the black crop bars inward to cut away unwanted parts, then press <kbd class='dfs-kbd'>Enter</kbd>.</li><li>Click <strong>Wrap Text &gt; Square</strong> so your text flows smoothly around the image rather than pushing it onto a new page.</li></ol>",
                "ui_sim": {
                    "title": "Picture Format & Sizing Handles",
                    "content": "<div style='display:flex; justify-content:center; padding:16px; background:#f1f5f9; border-radius:4px;'><div style='border:2px dashed #0284c7; padding:10px; background:#ffffff; position:relative; width:160px; text-align:center;'><span style='position:absolute; top:-5px; left:-5px; width:10px; height:10px; background:#0284c7; border-radius:50%;'></span><span style='position:absolute; top:-5px; right:-5px; width:10px; height:10px; background:#0284c7; border-radius:50%;'></span><span style='position:absolute; bottom:-5px; left:-5px; width:10px; height:10px; background:#0284c7; border-radius:50%;'></span><span style='position:absolute; bottom:-5px; right:-5px; width:10px; height:10px; background:#0284c7; border-radius:50%;'></span><i class='fa-regular fa-image' style='font-size:2rem; color:#64748b;'></i><div style='font-size:0.75rem; color:#0284c7; font-weight:700; margin-top:4px;'>Drag Corners Only</div></div></div>"
                }
            }
        ],
        "exam_model": {
            "scenario": "A health worker inserts a photo of an ambulance into a safety poster. The photo is too large and spills onto page 2. Explain how to reduce the size of the photo without distorting its shape.",
            "steps": [
                {
                    "action": "Select the picture",
                    "solution": "Click on the ambulance photo to display the sizing handles.",
                    "mark": "[B1]",
                    "rationale": "Sizing handles must be active to resize."
                },
                {
                    "action": "Resize proportionally",
                    "solution": "Click and drag inward from one of the four CORNER handles until the photo fits neatly on page 1.",
                    "mark": "[M1]",
                    "rationale": "Corner handles scale width and height simultaneously to maintain aspect ratio."
                }
            ],
            "tutor_rule": "Always use the word 'corner' when answering image resizing questions in the exam."
        },
        "drills": [
            {
                "question": "Which handle should you drag to resize an image without making it look squashed or stretched?",
                "options": [
                    {"text": "A corner handle", "correct": True},
                    {"text": "The top middle handle", "correct": False},
                    {"text": "The left side handle", "correct": False},
                    {"text": "The bottom middle handle", "correct": False}
                ],
                "explanation": "Dragging corner handles resizes the image proportionally (maintaining the aspect ratio)."
            },
            {
                "question": "What is the name of the tool used to cut away unwanted outer edges of a picture?",
                "options": [
                    {"text": "Crop Tool", "correct": True},
                    {"text": "Spell Check Tool", "correct": False},
                    {"text": "Recycle Bin", "correct": False},
                    {"text": "Format Painter", "correct": False}
                ],
                "explanation": "The Crop tool trims away outer edges or backgrounds from an image."
            },
            {
                "question": "Where on the ribbon do you go to insert a picture stored on your computer?",
                "options": [
                    {"text": "Insert Tab &gt; Pictures", "correct": True},
                    {"text": "Home Tab &gt; Font", "correct": False},
                    {"text": "View Tab &gt; Zoom", "correct": False},
                    {"text": "File Tab &gt; Print", "correct": False}
                ],
                "explanation": "The Insert tab contains tools for adding Pictures, Shapes, Tables, and Icons."
            }
        ],
        "practice": {
            "task": "A student needs to add a logo to a company newsletter. Write down the steps to insert the logo from their Pictures folder and position it at the top right of the newsletter.",
            "scaffold_starter": "Step 1 (Insert): \nStep 2 (Position/Wrap): ",
            "model_answer": "Step 1: Click the Insert tab, select Pictures > This Device, browse to the Pictures folder, choose the logo file and click Insert.\nStep 2: Select the image, click Wrap Text > Square, and drag the logo to the top right corner of the page.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Correct pathway: Insert > Pictures > Select file."},
                {"tag": "[1 Mark]", "desc": "Using Wrap Text and positioning the image at the top right."}
            ]
        },
        "revision_links": [
            {"label": "Word Processing Basics", "href": "e3-word-processing-basics.html"},
            {"label": "Document Formatting & Bullets", "href": "e3-formatting-aligning-bullets.html"},
            {"label": "Spellchecking & Saving", "href": "e3-spellcheck-proofing-saving.html"}
        ]
    },
    {
        "slug": "e3-spellcheck-proofing-saving",
        "code": "E3.2.4",
        "skill_area": "2. Creating and Editing",
        "title": "Spellcheck, Proofreading and Saving Files",
        "time": "15 Mins",
        "lead": "Produce error-free professional documents by running automated spelling and grammar checkers, proofreading text manually, and mastering the crucial difference between 'Save' and 'Save As'.",
        "objectives": [
            "Use the automated spell check and grammar tool to correct errors",
            "Proofread manually to catch words that are spelled correctly but used in the wrong context",
            "Differentiate between Save (Ctrl+S) and Save As (F12) to store files in the correct folder"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Entry 3 Digital Skills - Spellcheck & Saving Documents",
        "steps": [
            {
                "title": "Using the Automated Spell and Grammar Checker",
                "body": "<p>Word processors highlight potential errors with coloured squiggly lines:</p><ul><li><strong>Red Squiggly Line:</strong> Spelling error or unrecognised word.</li><li><strong>Blue or Double Line:</strong> Grammar or punctuation mistake (e.g. missing capital letter or double space).</li></ul><p>To run a full check: Press <kbd class='dfs-kbd'>F7</kbd> or click <strong>Review tab &gt; Spelling &amp; Grammar</strong> (or Editor). Review each suggested word carefully and click <strong>Change</strong>, or click <strong>Ignore</strong> if it is an uncommon name or medical term that is spelled correctly.</p>",
                "shortcuts": [
                    {"label": "Run Spell Check", "key": "F7"},
                    {"label": "Quick Save", "key": "Ctrl + S"}
                ]
            },
            {
                "title": "Why You Still Must Proofread Manually",
                "body": "<p>Computers cannot read your mind. If you type the word <em>'their'</em> instead of <em>'there'</em>, or <em>'from'</em> instead of <em>'form'</em>, the spellchecker will <strong>not</strong> flag an error because both words exist in the dictionary!</p><p>Always read through your completed work sentence by sentence before submitting or printing.</p>",
                "callout": {
                    "type": "tutor",
                    "title": "Tutor Abdul's Exam Wisdom",
                    "text": "In Entry 3 exams, texts frequently contain deliberate errors like <em>'meet'</em> instead of <em>'meat'</em> or <em>'sea'</em> instead of <em>'see'</em>. Spellcheck alone will miss these — your own human eyes must catch them!"
                }
            },
            {
                "title": "Save (<kbd class='dfs-kbd'>Ctrl + S</kbd>) vs Save As (<kbd class='dfs-kbd'>F12</kbd>)",
                "body": "<p>Mastering this difference prevents accidental overwriting of files:</p><ul><li><strong>Save As:</strong> Used the <em>very first time</em> you save a new document, OR when you want to save an existing document with a <strong>new name</strong>, in a <strong>different folder</strong>, or in a <strong>different file format</strong> (such as PDF).</li><li><strong>Save:</strong> Updates the existing file in place. It keeps the current name and location, simply updating the saved content with your latest changes.</li></ul>",
                "ui_sim": {
                    "title": "Save As Dialogue Box",
                    "content": "<div style='background:#f8fafc; border:1px solid #cbd5e1; padding:12px; border-radius:4px;'><div style='color:#0f172a; font-weight:700; margin-bottom:8px;'><i class='fa-solid fa-floppy-disk' style='color:#0284c7;'></i> Save As</div><div style='display:flex; flex-direction:column; gap:6px;'><div style='font-size:0.85rem; color:#475569;'>File name: <input type='text' value='Health Safety Policy 2026.docx' style='width:70%; padding:4px 8px; border:1px solid #94a3b8; border-radius:4px;'></div><div style='font-size:0.85rem; color:#475569;'>Save as type: <span style='font-weight:600; color:#0f172a;'>Word Document (*.docx)</span></div><div style='font-size:0.85rem; color:#475569;'>Location: <span style='color:#0284c7;'><i class='fa-regular fa-folder'></i> Documents &gt; Policies</span></div></div></div>"
                },
                "shortcuts": [
                    {"label": "Save In Place", "key": "Ctrl + S"},
                    {"label": "Save As Window", "key": "F12"}
                ]
            }
        ],
        "exam_model": {
            "scenario": "A clinic worker opens a master blank template called 'Patient Incident Form.docx'. They fill in today's incident report for a patient named Sarah. Explain whether they should click 'Save' or 'Save As', and what filename they should choose.",
            "steps": [
                {
                    "action": "Select Save or Save As",
                    "solution": "They must choose 'Save As'.",
                    "mark": "[B1]",
                    "rationale": "Choosing Save As creates a new copy without overwriting the blank master template."
                },
                {
                    "action": "Select appropriate filename",
                    "solution": "Name it 'Incident Report Sarah 2026-10-20.docx' (or include date/name).",
                    "mark": "[B1]",
                    "rationale": "Gives a distinct, descriptive name that preserves the original template for future use."
                }
            ],
            "tutor_rule": "Whenever you work from a template, always use 'Save As' immediately so the template stays blank."
        },
        "drills": [
            {
                "question": "When should you use 'Save As' instead of normal 'Save'?",
                "options": [
                    {"text": "When you want to save the file with a new name or in a new folder", "correct": True},
                    {"text": "Every single time you type a word", "correct": False},
                    {"text": "Only when shutting down the computer", "correct": False},
                    {"text": "Only when deleting a document", "correct": False}
                ],
                "explanation": "Save As prompts you to choose a filename and destination folder, which is ideal when creating a new copy."
            },
            {
                "question": "What keyboard key starts the automated Spelling and Grammar check in Microsoft Word?",
                "options": [
                    {"text": "F7", "correct": True},
                    {"text": "F1", "correct": False},
                    {"text": "Esc", "correct": False},
                    {"text": "Delete", "correct": False}
                ],
                "explanation": "F7 is the universal shortcut to launch the Spelling and Grammar check tool."
            },
            {
                "question": "Why will the spellcheck tool NOT catch the error in this sentence: 'I went to the beech for a walk'?",
                "options": [
                    {"text": "'Beech' is a real word in the dictionary (a type of tree), so the computer thinks it is spelled correctly", "correct": True},
                    {"text": "The computer is broken", "correct": False},
                    {"text": "Word processors do not check words with double 'e'", "correct": False},
                    {"text": "Sentences starting with 'I' cannot be spellchecked", "correct": False}
                ],
                "explanation": "'Beech' is a correctly spelled word, so the spellchecker does not flag it; manual proofreading is needed to catch the context error ('beach')."
            }
        ],
        "practice": {
            "task": "A care worker has typed up a 3-page monthly resident report. Before emailing it to the manager, state two actions they must take to ensure the document is accurate and saved securely.",
            "scaffold_starter": "Action 1 (Accuracy): \nAction 2 (Saving): ",
            "model_answer": "Action 1: Run the Spelling and Grammar check (F7) and proofread through the document manually to catch any context errors.\nAction 2: Save the document into the official Reports folder with a clear name (e.g. 'Monthly Report October 2026.docx').",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Running spellcheck and manually proofreading the text."},
                {"tag": "[1 Mark]", "desc": "Saving with a clear, descriptive filename in a proper folder."}
            ]
        },
        "revision_links": [
            {"label": "Word Processing Basics", "href": "e3-word-processing-basics.html"},
            {"label": "Organising Files & Folders", "href": "e3-organising-files-folders.html"},
            {"label": "Email Attachments", "href": "e3-email-attachments-contacts.html"}
        ]
    },
    {
        "slug": "e3-spreadsheets-simple-data",
        "code": "E3.2.5",
        "skill_area": "2. Creating and Editing",
        "title": "Entering Data into Simple Spreadsheets",
        "time": "15 Mins",
        "lead": "Understand rows, columns, and cell references in spreadsheet software like Excel, enter text labels and numbers accurately, format numbers as currency, and use simple addition formulas.",
        "objectives": [
            "Identify columns (letters), rows (numbers), and cell references (e.g. B4)",
            "Enter text labels and numerical values into correct cells",
            "Format numerical data as Currency (£) and use basic formulas (=SUM or +)"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Entry 3 Digital Skills - Spreadsheet Cells & Simple Totals",
        "steps": [
            {
                "title": "Understanding the Spreadsheet Grid",
                "body": "<p>A spreadsheet is a powerful grid used for storing lists, managing budgets, and calculating totals:</p><ul><li><strong>Columns:</strong> Run vertically up and down, labelled with letters (<strong>A, B, C, D...</strong>).</li><li><strong>Rows:</strong> Run horizontally left to right, labelled with numbers (<strong>1, 2, 3, 4...</strong>).</li><li><strong>Cell Reference:</strong> The intersection of a column and a row. Column letter comes first, followed by the row number (e.g. cell <strong>C5</strong> is column C, row 5).</li></ul>",
                "ui_sim": {
                    "title": "Spreadsheet Grid & Cell Address",
                    "content": "<table style='width:100%; border-collapse:collapse; background:#ffffff; font-family:monospace; font-size:0.9rem;'><tr style='background:#e2e8f0; text-align:center;'><th style='width:40px; border:1px solid #cbd5e1;'></th><th style='border:1px solid #cbd5e1;'>A</th><th style='border:1px solid #cbd5e1;'>B</th><th style='border:1px solid #cbd5e1;'>C</th></tr><tr><td style='background:#e2e8f0; text-align:center; font-weight:700; border:1px solid #cbd5e1;'>1</td><td style='border:1px solid #cbd5e1; font-weight:700;'>Item Name</td><td style='border:1px solid #cbd5e1; font-weight:700;'>Quantity</td><td style='border:1px solid #cbd5e1; font-weight:700;'>Cost (£)</td></tr><tr><td style='background:#e2e8f0; text-align:center; font-weight:700; border:1px solid #cbd5e1;'>2</td><td style='border:1px solid #cbd5e1;'>Bandages</td><td style='border:1px solid #cbd5e1;'>10</td><td style='border:1px solid #cbd5e1;'>£15.00</td></tr><tr><td style='background:#e2e8f0; text-align:center; font-weight:700; border:1px solid #cbd5e1;'>3</td><td style='border:1px solid #cbd5e1;'>Gloves</td><td style='border:1px solid #cbd5e1;'>25</td><td style='border:1px solid #cbd5e1; background:#fef3c7; border:2px solid #d97706;'>£22.50</td></tr></table>"
                }
            },
            {
                "title": "Entering Labels and Numbers",
                "body": "<p>Click into any cell to type:</p><ul><li><strong>Labels (Text):</strong> Word descriptions (e.g. 'Stationery', 'Total'). Automatically align to the left.</li><li><strong>Numbers / Values:</strong> Digits used for maths. Automatically align to the right.</li><li><strong>Currency Format:</strong> Highlight the numbers and click the <strong>£ (Currency)</strong> button on the ribbon so pennies display neatly with two decimal places (e.g. <code>£15.00</code> instead of <code>15</code>).</li></ul>",
                "callout": {
                    "type": "vocational",
                    "title": "Workplace Supply Tracking",
                    "text": "Clinics and dental practices track stock replenishment in spreadsheets so supervisors know exactly when medical gloves or sterile swabs need reordering."
                }
            },
            {
                "title": "Simple Formulas and AutoSum",
                "body": "<p>Every spreadsheet formula MUST begin with an <strong>equals sign (=)</strong>:</p><ul><li><strong>Simple Addition:</strong> Type <code>=B2+B3</code> and press <kbd class='dfs-kbd'>Enter</kbd>.</li><li><strong>AutoSum Function:</strong> Highlight your numbers and click the <strong>AutoSum (&Sigma;)</strong> button on the ribbon. It automatically inserts <code>=SUM(C2:C5)</code> to add all numbers in that range.</li></ul>",
                "shortcuts": [
                    {"label": "AutoSum Shortcut", "key": "Alt + ="}
                ]
            }
        ],
        "exam_model": {
            "scenario": "A community nursery tracks juice carton expenses in a spreadsheet. In cell C2 the cost is 12.5 and in C3 the cost is 8. Explain how to format the numbers as currency and write the formula needed in cell C4 to calculate the total cost.",
            "steps": [
                {
                    "action": "Format as Currency",
                    "solution": "Select cells C2 to C4 and click the Currency (£) button on the Home ribbon.",
                    "mark": "[B1]",
                    "rationale": "Formats numbers to display the pound symbol and two decimal places (£12.50 and £8.00)."
                },
                {
                    "action": "Write the calculation formula",
                    "solution": "=C2+C3  (or =SUM(C2:C3))",
                    "mark": "[B1]",
                    "rationale": "Formula correctly starts with '=' and adds the two cell references."
                }
            ],
            "tutor_rule": "Never type '=12.5+8' into cell C4 in an exam! You MUST use the cell references (=C2+C3) so that if prices change, the total updates automatically."
        },
        "drills": [
            {
                "question": "What symbol MUST every spreadsheet formula start with?",
                "options": [
                    {"text": "= (Equals sign)", "correct": True},
                    {"text": "+ (Plus sign)", "correct": False},
                    {"text": "# (Hashtag)", "correct": False},
                    {"text": "£ (Pound sign)", "correct": False}
                ],
                "explanation": "All formulas in Excel and Google Sheets must begin with an equals sign (=) to trigger calculation."
            },
            {
                "question": "What is the cell reference for the cell in Column D and Row 7?",
                "options": [
                    {"text": "D7", "correct": True},
                    {"text": "7D", "correct": False},
                    {"text": "Row D", "correct": False},
                    {"text": "D+7", "correct": False}
                ],
                "explanation": "Cell references always write the column letter first, followed by the row number (D7)."
            },
            {
                "question": "Which ribbon tool automatically adds up a column of numbers in a spreadsheet?",
                "options": [
                    {"text": "AutoSum (Σ)", "correct": True},
                    {"text": "Spell Check (F7)", "correct": False},
                    {"text": "Wrap Text", "correct": False},
                    {"text": "Find and Replace", "correct": False}
                ],
                "explanation": "The AutoSum button calculates the total of adjacent numbers using the =SUM() function."
            }
        ],
        "practice": {
            "task": "Look at the table below:<br>Cell B2: 15<br>Cell B3: 25<br>Cell B4: 10<br><br>Write down the exact formula you should enter into cell B5 to find the total of all three cells.",
            "scaffold_starter": "Formula in cell B5: =",
            "model_answer": "=SUM(B2:B4)   (or =B2+B3+B4)",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Starting formula with the '=' sign."},
                {"tag": "[1 Mark]", "desc": "Using correct cell references (B2+B3+B4 or SUM(B2:B4))."}
            ]
        },
        "revision_links": [
            {"label": "Organising Files & Folders", "href": "e3-organising-files-folders.html"},
            {"label": "Saving Documents", "href": "e3-spellcheck-proofing-saving.html"},
            {"label": "Word Processing Basics", "href": "e3-word-processing-basics.html"}
        ]
    },

    # -------------------------------------------------------------------------
    # Skill Area 3: Communicating
    # -------------------------------------------------------------------------
    {
        "slug": "e3-email-compose-reply-forward",
        "code": "E3.3.1",
        "skill_area": "3. Communicating",
        "title": "Composing, Replying and Forwarding Emails",
        "time": "15 Mins",
        "lead": "Master everyday workplace email: write clear subject lines, compose polite messages with appropriate greetings and sign-offs, reply to incoming messages, and forward emails to colleagues.",
        "objectives": [
            "Compose a new email with recipient address, clear subject line, and polite body text",
            "Differentiate between Reply (to sender only) and Reply All (to everyone on the thread)",
            "Forward an existing email to a new contact with an explanatory message"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Entry 3 Digital Skills - Email Basics & Etiquette",
        "steps": [
            {
                "title": "Composing a New Email",
                "body": "<p>Click <strong>New Mail</strong> (or Compose) to open an email window. Every message needs three core parts:</p><ol><li><strong>To:</strong> Type the recipient's exact email address (e.g. <code>sarah.jones@example.co.uk</code>). Addresses must have no spaces and contain an <code>@</code> symbol.</li><li><strong>Subject Line:</strong> A short, informative summary of your message (e.g. <em>'Staff Meeting Agenda - 14th November'</em>). Never leave this blank!</li><li><strong>Email Body:</strong> The message itself. Always start with a polite greeting (<em>'Dear Sarah'</em> or <em>'Good morning Team'</em>) and finish with a sign-off (<em>'Kind regards, Abdul'</em>).</li></ol>",
                "ui_sim": {
                    "title": "Workplace Email Compose Window",
                    "content": "<div style='background:#f8fafc; border:1px solid #cbd5e1; padding:10px; border-radius:4px; font-size:0.88rem;'><div style='margin-bottom:6px;'><strong>To:</strong> <span style='background:#e0f2fe; padding:2px 8px; border-radius:12px; color:#0369a1;'>amanda.clark@healthclinic.org</span></div><div style='margin-bottom:8px;'><strong>Subject:</strong> First Aid Training Rota - October 2026</div><div style='background:#ffffff; border:1px solid #cbd5e1; padding:10px; border-radius:4px; min-height:60px;'>Good morning Amanda,<br><br>Please find attached the updated first aid rota for next week.<br><br>Kind regards,<br>Abdul</div></div>"
                },
                "shortcuts": [
                    {"label": "New Email Shortcut", "key": "Ctrl + N"},
                    {"label": "Send Email", "key": "Ctrl + Enter"}
                ]
            },
            {
                "title": "Replying: Reply vs Reply All",
                "body": "<p>When responding to an email you received:</p><ul><li><strong>Reply:</strong> Sends your response ONLY to the person who sent the email. Use this 90% of the time.</li><li><strong>Reply All:</strong> Sends your response to the sender AND everyone else who was copied into the email. Only use this when everyone on the team genuinely needs to read your reply.</li></ul>",
                "callout": {
                    "type": "warning",
                    "title": "Workplace Etiquette Alert",
                    "text": "Do not click 'Reply All' just to say 'Thank you'! That clutters up everyone's inbox across the whole department."
                }
            },
            {
                "title": "Forwarding an Email",
                "body": "<p><strong>Forward</strong> sends a copy of an email you received to a completely new person who wasn't on the original thread. When forwarding, always type a brief note at the top explaining why you are sharing it (e.g. <em>'Hi David, please see the update from estates below for your information'</em>).</p>"
            }
        ],
        "exam_model": {
            "scenario": "A support worker receives an email from their manager with the subject 'Next Week Shift Cover'. The worker needs to confirm they can work Saturday. Explain which button they should click (Reply, Reply All, or Forward) and write a suitable two-sentence email response.",
            "steps": [
                {
                    "action": "Select the correct action",
                    "solution": "Click 'Reply'",
                    "mark": "[B1]",
                    "rationale": "Reply sends the answer directly back to the manager who asked."
                },
                {
                    "action": "Compose response with proper etiquette",
                    "solution": "Dear Manager,\nThank you for your email. I can confirm that I am available to cover the Saturday shift.\nKind regards,\nAbdul",
                    "mark": "[B1]",
                    "rationale": "Includes greeting, polite confirmation, and professional sign-off."
                }
            ],
            "tutor_rule": "In Entry 3 exams, marks are given for: 1. Subject line filled in; 2. Polite greeting; 3. Clear message; 4. Professional sign-off."
        },
        "drills": [
            {
                "question": "Which part of an email gives the recipient a quick summary of what the message is about before they open it?",
                "options": [
                    {"text": "The Subject Line", "correct": True},
                    {"text": "The Attachment Box", "correct": False},
                    {"text": "The Spam Filter", "correct": False},
                    {"text": "The Sign-off", "correct": False}
                ],
                "explanation": "The Subject line is displayed in the recipient's inbox and explains the topic of the email."
            },
            {
                "question": "What is the difference between 'Reply' and 'Reply All'?",
                "options": [
                    {"text": "Reply sends only to the sender; Reply All sends to the sender and everyone copied on the email", "correct": True},
                    {"text": "Reply deletes the email; Reply All prints it", "correct": False},
                    {"text": "Reply is for friends; Reply All is for work", "correct": False},
                    {"text": "There is no difference", "correct": False}
                ],
                "explanation": "Reply responds solely to the author; Reply All includes every person listed in To and CC."
            },
            {
                "question": "Why should you avoid typing an email in ALL CAPITAL LETTERS?",
                "options": [
                    {"text": "It looks like you are SHOUTING and is considered unprofessional", "correct": True},
                    {"text": "Capital letters take up twice as much disk space", "correct": False},
                    {"text": "Email software blocks capital letters automatically", "correct": False},
                    {"text": "It takes five minutes longer to send", "correct": False}
                ],
                "explanation": "Writing in ALL CAPS online is considered the digital equivalent of shouting and comes across as rude."
            }
        ],
        "practice": {
            "task": "You need to email your tutor, Abdul, to ask for extra practice questions on spreadsheets. Write out the email including:<br>- The Subject line<br>- A polite greeting<br>- Your request<br>- A professional sign-off",
            "scaffold_starter": "Subject: \nGreeting: \nMessage: \nSign-off: ",
            "model_answer": "Subject: Request for Spreadsheet Practice Questions\n\nDear Abdul,\nI hope you are well. Could you please send me some extra practice questions for spreadsheets to help me revise for my exam?\n\nThank you,\nSubi",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Clear, relevant subject line."},
                {"tag": "[1 Mark]", "desc": "Polite greeting, clear request, and professional sign-off."}
            ]
        },
        "revision_links": [
            {"label": "Email Attachments & Contacts", "href": "e3-email-attachments-contacts.html"},
            {"label": "Online Passwords & Scams", "href": "e3-passwords-privacy-scams.html"},
            {"label": "Video Calls & Messaging", "href": "e3-messaging-video-calls.html"}
        ]
    },
    {
        "slug": "e3-email-attachments-contacts",
        "code": "E3.3.2",
        "skill_area": "3. Communicating",
        "title": "Email Attachments and Contacts List",
        "time": "15 Mins",
        "lead": "Learn how to attach documents and photos to emails, open and save received attachments safely, and create contacts in your email address book for quick communication.",
        "objectives": [
            "Attach documents and photos to an outgoing email using the paperclip icon",
            "Open, preview, and safely save received email attachments",
            "Add and organise email contacts in your address book"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Entry 3 Digital Skills - Email Attachments & Address Books",
        "steps": [
            {
                "title": "Adding an Attachment to an Email",
                "body": "<p>An <strong>Attachment</strong> is a separate digital file (such as a Word document, spreadsheet, or photo) sent alongside your email message:</p><ol><li>In your email compose window, click the <strong>Paperclip icon</strong> (<i class='fa-solid fa-paperclip'></i>) labelled <strong>Attach File</strong>.</li><li>Browse through your computer's folders to select your file.</li><li>Click <strong>Open / Insert</strong>.</li><li>The file name and file size will appear below the subject line. Always check that the correct file is attached before clicking Send.</li></ol>",
                "ui_sim": {
                    "title": "Email Attachment Bar",
                    "content": "<div style='display:flex; align-items:center; gap:10px; background:#f1f5f9; padding:8px 12px; border-radius:4px; border:1px solid #cbd5e1;'><i class='fa-solid fa-paperclip' style='color:#0284c7; font-size:1.1rem;'></i> <div style='display:flex; align-items:center; gap:8px; background:#ffffff; border:1px solid #94a3b8; padding:4px 10px; border-radius:16px; font-size:0.85rem;'><i class='fa-regular fa-file-word' style='color:#2563eb;'></i> <strong>Patient_Feedback_Oct.docx</strong> <span style='color:#64748b;'>(245 KB)</span> <i class='fa-solid fa-xmark' style='color:#dc2626; cursor:pointer;'></i></div></div>"
                }
            },
            {
                "title": "Opening and Saving Received Attachments Safely",
                "body": "<p>When you receive an email with a paperclip symbol, it contains an attachment:</p><ul><li>Click the attachment to <strong>Preview</strong> it inside your browser or email app.</li><li>Click <strong>Download / Save As</strong> to save a permanent copy onto your computer (e.g. into your <strong>Documents</strong> folder).</li></ul>",
                "callout": {
                    "type": "warning",
                    "title": "Crucial Cybersecurity Warning",
                    "text": "<strong>NEVER open an attachment from an unknown or suspicious sender!</strong> Email attachments from scammers can contain harmful viruses and malware that lock your computer."
                }
            },
            {
                "title": "Creating and Using Email Contacts",
                "body": "<p>Instead of memorising complicated email addresses, save people into your <strong>Contacts / People</strong> address book:</p><ol><li>Open the Contacts tab in your email program.</li><li>Click <strong>New Contact</strong>.</li><li>Type the person's Full Name, Email Address, and Phone Number.</li><li>Click <strong>Save</strong>. Next time you type their name in the 'To' box, their address will automatically appear!</li></ol>"
            }
        ],
        "exam_model": {
            "scenario": "A dental receptionist needs to email a price list PDF to a patient. Describe the step-by-step procedure to attach the file 'Price_List_2026.pdf' from their Documents folder to the email.",
            "steps": [
                {
                    "action": "Locate and click the attachment tool",
                    "solution": "Click the Paperclip icon (or 'Attach File' button) in the email window.",
                    "mark": "[B1]",
                    "rationale": "Identifies the standard universal attachment command."
                },
                {
                    "action": "Select and attach the file",
                    "solution": "Browse to the 'Documents' folder, click 'Price_List_2026.pdf', and click 'Open' or 'Insert'.",
                    "mark": "[M1]",
                    "rationale": "Correctly navigates to folder and selects the required file."
                }
            ],
            "tutor_rule": "In Entry 3 exams, questions often show a screenshot of an email ribbon and ask: 'Which icon attaches a file?' The answer is always the Paperclip icon."
        },
        "drills": [
            {
                "question": "Which icon is universally used in email software to attach a file to a message?",
                "options": [
                    {"text": "A Paperclip icon", "correct": True},
                    {"text": "A Magnifying glass", "correct": False},
                    {"text": "A Trash can", "correct": False},
                    {"text": "A Printer icon", "correct": False}
                ],
                "explanation": "The paperclip icon is the universal symbol for attaching a document or photo to an email."
            },
            {
                "question": "What should you do if you receive an email with an unexpected .exe or .zip attachment from a stranger?",
                "options": [
                    {"text": "Do not open it; report and delete it immediately", "correct": True},
                    {"text": "Open it immediately to see what it is", "correct": False},
                    {"text": "Forward it to all your friends", "correct": False},
                    {"text": "Save it to your desktop", "correct": False}
                ],
                "explanation": "Unexpected attachments from unknown senders can contain viruses or malware; never open them."
            },
            {
                "question": "What is the primary benefit of saving email addresses in your Contacts address book?",
                "options": [
                    {"text": "You can select contacts quickly without having to re-type long email addresses each time", "correct": True},
                    {"text": "It automatically sends emails without you clicking send", "correct": False},
                    {"text": "It makes your computer run twice as fast", "correct": False},
                    {"text": "It prints emails automatically", "correct": False}
                ],
                "explanation": "Address books prevent typos and save time by auto-filling verified email addresses."
            }
        ],
        "practice": {
            "task": "A colleague has sent you an email containing an attached staff rota spreadsheet. Explain how you would save this spreadsheet onto your computer so you can review it offline later.",
            "scaffold_starter": "Step 1: Open the email and locate...\nStep 2: Click the...\nStep 3: Choose the folder...",
            "model_answer": "Step 1: Open the email and locate the spreadsheet attachment below the subject line.\nStep 2: Click the download arrow or right-click and choose 'Save As'.\nStep 3: Choose the 'Documents' folder on your computer and click 'Save'.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Locating the attachment and clicking download / Save As."},
                {"tag": "[1 Mark]", "desc": "Selecting an appropriate local folder to store the downloaded file."}
            ]
        },
        "revision_links": [
            {"label": "Composing & Replying Emails", "href": "e3-email-compose-reply-forward.html"},
            {"label": "Organising Files & Folders", "href": "e3-organising-files-folders.html"},
            {"label": "Online Passwords & Scams", "href": "e3-passwords-privacy-scams.html"}
        ]
    },
    {
        "slug": "e3-messaging-video-calls",
        "code": "E3.3.3",
        "skill_area": "3. Communicating",
        "title": "Video Calling and Digital Messaging",
        "time": "15 Mins",
        "lead": "Participate confidently in workplace video meetings (such as Microsoft Teams or Zoom): join meetings via links, mute/unmute your microphone, turn your camera on/off, and use chat functions respectfully.",
        "objectives": [
            "Join an online video call using a meeting link or calendar invite",
            "Operate essential call controls: Mute/Unmute microphone and Camera On/Off",
            "Use chat channels respectfully and follow digital meeting etiquette"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Entry 3 Digital Skills - Video Calls & Online Etiquette",
        "steps": [
            {
                "title": "Joining a Video Meeting",
                "body": "<p>Online video calls are essential for team discussions, remote training, and client check-ins:</p><ol><li>Open your meeting invite (in your email or calendar).</li><li>Click the link that says <strong>'Click here to join the meeting'</strong>.</li><li>A preview window will open. Check your appearance, select your audio (computer audio), and click <strong>Join Now</strong>.</li></ol>",
                "ui_sim": {
                    "title": "Video Call Control Toolbar",
                    "content": "<div style='display:flex; justify-content:center; align-items:center; gap:14px; background:#1e293b; color:#ffffff; padding:12px; border-radius:6px;'><button style='background:#334155; border:none; color:#ffffff; padding:8px 12px; border-radius:6px;'><i class='fa-solid fa-video'></i> Camera</button><button style='background:#334155; border:none; color:#ffffff; padding:8px 12px; border-radius:6px;'><i class='fa-solid fa-microphone-slash' style='color:#ef4444;'></i> Muted</button><button style='background:#334155; border:none; color:#ffffff; padding:8px 12px; border-radius:6px;'><i class='fa-regular fa-message'></i> Chat</button><button style='background:#334155; border:none; color:#ffffff; padding:8px 12px; border-radius:6px;'><i class='fa-regular fa-hand'></i> Raise Hand</button><button style='background:#dc2626; border:none; color:#ffffff; padding:8px 14px; border-radius:6px; font-weight:700;'><i class='fa-solid fa-phone-slash'></i> Leave</button></div>"
                }
            },
            {
                "title": "Essential Call Controls: Mic and Camera",
                "body": "<p>During a call, you must control your audio and visual presence:</p><ul><li><strong>Mute / Unmute (<i class='fa-solid fa-microphone'></i>):</strong> Keep your microphone <strong>muted</strong> when you are listening. This blocks out background noises like dogs barking, coughing, or keyboard clicks. Unmute when it is your turn to speak.</li><li><strong>Camera On / Off (<i class='fa-solid fa-video'></i>):</strong> Toggles your webcam. Ensure your lighting is in front of you (not behind you), and use background blur if you are working in a shared room.</li></ul>",
                "callout": {
                    "type": "tutor",
                    "title": "Tutor Abdul's Golden Etiquette Rule",
                    "text": "The golden rule of video meetings: <strong>Stay on mute until you are invited to speak!</strong> Use the 'Raise Hand' button if you have a question so you don't interrupt the presenter."
                }
            },
            {
                "title": "Using the In-Meeting Chat",
                "body": "<p>Click the <strong>Chat bubble icon</strong> to open the sidebar. You can type questions, share links, or post comments without interrupting the speaker. Keep all chat professional, polite, and relevant to the meeting topic.</p>"
            }
        ],
        "exam_model": {
            "scenario": "A student is attending an online group revision session with 15 classmates. The tutor is explaining a difficult topic. Give two pieces of advice on how the student should manage their microphone and camera to ensure a smooth session for everyone.",
            "steps": [
                {
                    "action": "Microphone advice",
                    "solution": "Keep the microphone muted while the tutor is speaking to eliminate background noise.",
                    "mark": "[B1]",
                    "rationale": "Prevents disruptive ambient noises from echoing to other participants."
                },
                {
                    "action": "Camera / participation advice",
                    "solution": "Use the 'Raise Hand' button or type questions into the in-call chat rather than talking over the tutor.",
                    "mark": "[B1]",
                    "rationale": "Maintains orderly, respectful online classroom etiquette."
                }
            ],
            "tutor_rule": "In Entry 3 exams, questions test whether you understand the icons: microphone icon with a diagonal line through it means MUTED."
        },
        "drills": [
            {
                "question": "What does a microphone icon with a line through it indicate during a video call?",
                "options": [
                    {"text": "Your microphone is MUTED and other people cannot hear you", "correct": True},
                    {"text": "Your computer speakers are broken", "correct": False},
                    {"text": "The meeting has ended", "correct": False},
                    {"text": "Your webcam is switched on", "correct": False}
                ],
                "explanation": "A line through the microphone symbol indicates that you are muted."
            },
            {
                "question": "What feature allows you to ask a question in a large meeting without talking over the speaker?",
                "options": [
                    {"text": "Click the 'Raise Hand' button or use the meeting chat", "correct": True},
                    {"text": "Turn off your computer monitor", "correct": False},
                    {"text": "Leave the meeting and rejoin five times", "correct": False},
                    {"text": "Unmute and shout loudly", "correct": False}
                ],
                "explanation": "Raising your virtual hand or posting in the chat alerts the host without disrupting the presentation."
            },
            {
                "question": "Why should you use 'Background Blur' during a workplace video call from home?",
                "options": [
                    {"text": "To protect your home privacy and prevent distracting background movements", "correct": True},
                    {"text": "Because it makes your voice louder", "correct": False},
                    {"text": "To hide from your boss that you are in a meeting", "correct": False},
                    {"text": "It speeds up your internet download speed", "correct": False}
                ],
                "explanation": "Background blur conceals private home surroundings and keeps the focus on the participant."
            }
        ],
        "practice": {
            "task": "You are joining your first online video meeting with your team. State three actions you must perform to set up and join the call successfully.",
            "scaffold_starter": "1. To join: \n2. For audio: \n3. For camera: ",
            "model_answer": "1. Click the meeting link in your calendar or email invite to launch the video application.\n2. Test that your microphone is working and keep it muted when entering the call.\n3. Turn on your webcam and position yourself in good lighting facing the camera.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Clicking the invitation link to join the meeting."},
                {"tag": "[1 Mark]", "desc": "Managing microphone (muting) and webcam appropriately."}
            ]
        },
        "revision_links": [
            {"label": "Composing & Replying Emails", "href": "e3-email-compose-reply-forward.html"},
            {"label": "Display & Accessibility Settings", "href": "e3-accessibility-display-settings.html"},
            {"label": "Online Passwords & Scams", "href": "e3-passwords-privacy-scams.html"}
        ]
    }
]
