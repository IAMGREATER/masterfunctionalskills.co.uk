# -*- coding: utf-8 -*-
"""
Master Functional Skills (MFS) - Level 1 Digital Skills (Skill Area 2)
Author: Abdul (MFS Pedagogical Systems)
"""

LEVEL_1_SKILL_2 = [
    {
        "slug": "l1-word-processing-professional",
        "code": "L1.2.1",
        "skill_area": "2. Creating and Editing",
        "title": "Professional Document Formatting and Styles",
        "time": "15 Mins",
        "lead": "Format workplace documents to accredited standards: insert automated headers and footers with page numbers, apply built-in Heading Styles, insert formatted data tables, and manage page breaks.",
        "objectives": [
            "Insert running headers, footers, and automated page numbering",
            "Apply built-in Heading Styles (Heading 1, Heading 2) for document structure and accessibility",
            "Insert and format tables with header rows, borders, and column alignment"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Level 1 Digital Skills - Headers, Footers & Word Styles",
        "steps": [
            {
                "title": "Headers, Footers, and Automated Page Numbers",
                "body": "<p>Professional multi-page reports require consistent headers and footers:</p><ul><li><strong>Header (Top Margin):</strong> Typically contains the organisation name, document title, or date.</li><li><strong>Footer (Bottom Margin):</strong> Typically contains automated page numbering (e.g. <em>'Page 1 of 4'</em>) and confidentiality markings.</li><li><strong>Automated Page Numbers:</strong> Go to <strong>Insert &gt; Page Number &gt; Bottom of Page</strong>. Never type numbers manually, or every page will display the number 1!</li></ul>",
                "shortcuts": [
                    {"label": "Insert Page Break", "key": "Ctrl + Enter"}
                ]
            },
            {
                "title": "Using Built-In Heading Styles (Accessibility)",
                "body": "<p>Do not simply make titles bigger and bold manually. Use the <strong>Styles Gallery</strong> on the Home ribbon:</p><ul><li><strong>Heading 1:</strong> Main topic or chapter titles.</li><li><strong>Heading 2:</strong> Subsections within a topic.</li><li><strong>Normal:</strong> Standard body paragraphs.</li></ul><p>Screen readers use heading styles to help visually impaired users navigate documents quickly.</p>",
                "ui_sim": {
                    "title": "Word Styles Gallery Ribbon",
                    "content": "<div style='display:flex; gap:10px; background:#f8fafc; padding:8px 12px; border-radius:4px; border:1px solid #cbd5e1;'><div style='border:1px solid #94a3b8; background:#ffffff; padding:4px 10px; border-radius:4px; text-align:center;'><span style='font-size:0.75rem; color:#64748b;'>Normal</span><br><strong style='font-size:0.85rem;'>AaBbCc</strong></div><div style='border:2px solid #0284c7; background:#e0f2fe; padding:4px 10px; border-radius:4px; text-align:center;'><span style='font-size:0.75rem; color:#0369a1;'>Heading 1</span><br><strong style='font-size:0.95rem; color:#0369a1;'>AaBbCc</strong></div><div style='border:1px solid #94a3b8; background:#ffffff; padding:4px 10px; border-radius:4px; text-align:center;'><span style='font-size:0.75rem; color:#64748b;'>Heading 2</span><br><strong style='font-size:0.85rem;'>AaBbCc</strong></div></div>"
                }
            },
            {
                "title": "Inserting and Formatting Tables",
                "body": "<p>To present structured information neatly:</p><ol><li>Click <strong>Insert &gt; Table</strong> and drag across the grid to choose rows and columns (e.g. 3 columns × 4 rows).</li><li>Format the top row as a <strong>Header Row</strong> (Bold text, soft background shading).</li><li>Ensure text aligns to the left and numerical figures align to the right.</li></ol>"
            }
        ],
        "exam_model": {
            "scenario": "A health administrator has written a 6-page patient information booklet. The instructions state: 'Add automated page numbers in the centre of the footer, and format the main section title 'Clinic Services' using Heading 1 style.' Explain the steps required.",
            "steps": [
                {
                    "action": "Insert Page Numbers",
                    "solution": "Go to Insert > Page Number > Bottom of Page, and select the centered number format.",
                    "mark": "[M1]",
                    "rationale": "Correctly uses automated page numbering rather than manual typing."
                },
                {
                    "action": "Apply Heading Style",
                    "solution": "Select 'Clinic Services' and click 'Heading 1' in the Styles group on the Home ribbon.",
                    "mark": "[A1]",
                    "rationale": "Applies structural semantic style for accessibility."
                }
            ],
            "tutor_rule": "In Level 1 exams, always use the Styles gallery rather than manual font size buttons when instructions specify 'Heading 1' or 'Heading 2'."
        },
        "drills": [
            {
                "question": "Why should you use the 'Page Number' tool instead of typing numbers at the bottom of each page manually?",
                "options": [
                    {"text": "Automated page numbers update correctly on every page, whereas typing manually repeats the same number on every page", "correct": True},
                    {"text": "Manual numbers take up too much memory", "correct": False},
                    {"text": "Typing numbers deletes the text in your document", "correct": False},
                    {"text": "Printers refuse to print manual numbers", "correct": False}
                ],
                "explanation": "Headers and footers repeat across pages; automated fields calculate page numbers dynamically."
            },
            {
                "question": "What keyboard shortcut inserts a clean Page Break to start the next section on a fresh page?",
                "options": [
                    {"text": "Ctrl + Enter", "correct": True},
                    {"text": "Shift + Delete", "correct": False},
                    {"text": "Alt + F4", "correct": False},
                    {"text": "Tab + Space", "correct": False}
                ],
                "explanation": "Ctrl + Enter forces an immediate page break without having to press Enter twenty times."
            },
            {
                "question": "What is the primary benefit of using built-in Heading Styles (Heading 1, Heading 2) in long documents?",
                "options": [
                    {"text": "It structures the document for accessibility, screen readers, and automatic tables of contents", "correct": True},
                    {"text": "It sends the document to your printer automatically", "correct": False},
                    {"text": "It translates the text into other languages", "correct": False},
                    {"text": "It compresses the file into a ZIP archive", "correct": False}
                ],
                "explanation": "Styles establish an accessible document hierarchy used by assistive tools and automated navigation."
            }
        ],
        "practice": {
            "task": "You are formatting a workplace staff induction booklet. Describe how you would insert a running header with the text 'Staff Induction 2026' and a 3-column table on page 2.",
            "scaffold_starter": "Header instructions: \nTable instructions: ",
            "model_answer": "Header: Double-click in the top margin (or go to Insert > Header), type 'Staff Induction 2026', format as right-aligned and 10 pt font, then close the header.\nTable: Click on page 2, go to Insert > Table, select 3 columns by 4 rows, enter column headers in the top row, and apply bold formatting with shaded background.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Accessing and formatting running header."},
                {"tag": "[1 Mark]", "desc": "Inserting 3-column table with formatted header row."}
            ]
        },
        "revision_links": [
            {"label": "Folder Hierarchies & Sizes", "href": "l1-file-management-hierarchies.html"},
            {"label": "Combining Software & PDF Export", "href": "l1-combining-software-pdf-export.html"},
            {"label": "Workplace Email Etiquette", "href": "l1-workplace-email-etiquette.html"}
        ]
    },
    {
        "slug": "l1-spreadsheet-design-formatting",
        "code": "L1.2.2",
        "skill_area": "2. Creating and Editing",
        "title": "Spreadsheet Layout, Sorting and Formatting",
        "time": "15 Mins",
        "lead": "Design clear, readable spreadsheets for workplace use: format numbers as currency and percentages, adjust column widths to prevent ### overflow errors, merge and centre title cells, and sort data alphabetically and numerically.",
        "objectives": [
            "Format data types: Currency (£), Percentages (%), Decimals, and Dates",
            "Adjust column widths and row heights to eliminate '###' display errors and text truncation",
            "Sort data records in Ascending (A-Z, lowest first) and Descending (Z-A, highest first) order"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Level 1 Digital Skills - Spreadsheet Layout & Sorting",
        "steps": [
            {
                "title": "Fixing the '###' Display Error (Column Widths)",
                "body": "<p>When a number or date is too wide to fit inside its column, Excel does not cut off the digits — it displays <strong>###</strong> across the cell to warn you that data is hidden.</p><p>To fix this: Double-click the <strong>divider line between the column letters</strong> at the top (e.g. between column B and C). The column will automatically expand to fit the widest entry (AutoFit)!</p>",
                "shortcuts": [
                    {"label": "Select Entire Column", "key": "Ctrl + Space"},
                    {"label": "Select Entire Row", "key": "Shift + Space"}
                ]
            },
            {
                "title": "Formatting Numbers: Currency, Decimals, and Percentages",
                "body": "<p>Raw numbers look unprofessional. Format them on the <strong>Number group</strong> of the ribbon:</p><ul><li><strong>Currency (£):</strong> Formats figures with a pound sign and 2 decimal places (e.g. <code>£45.50</code>).</li><li><strong>Increase / Decrease Decimals:</strong> Controls decimal precision (e.g. rounding <code>14.2857</code> to <code>14.3</code>).</li><li><strong>Percentage (%):</strong> Multiplies by 100 and displays the percent sign (e.g. <code>0.15</code> becomes <code>15%</code>).</li><li><strong>Merge &amp; Centre:</strong> Combines multiple cells across the top of a table into one wide header banner.</li></ul>"
            },
            {
                "title": "Sorting Data Records (Ascending vs Descending)",
                "body": "<p>Sorting organises records logically without re-typing:</p><ul><li><strong>Ascending (A to Z / Smallest to Largest):</strong> Alphabetical order from A to Z, or numbers from lowest to highest.</li><li><strong>Descending (Z to A / Largest to Smallest):</strong> Reverse alphabetical, or numbers from highest to lowest.</li></ul><p>Always highlight the entire table before sorting to ensure related columns stay together!</p>",
                "ui_sim": {
                    "title": "Spreadsheet Sort & Filter Ribbon",
                    "content": "<div style='display:flex; gap:12px; align-items:center; background:#f8fafc; padding:8px 14px; border-radius:4px; border:1px solid #cbd5e1;'><button style='background:#ffffff; border:1px solid #94a3b8; padding:4px 10px; border-radius:4px; font-weight:700;'><i class='fa-solid fa-arrow-down-a-z' style='color:#0284c7;'></i> Sort A to Z</button><button style='background:#ffffff; border:1px solid #94a3b8; padding:4px 10px; border-radius:4px; font-weight:700;'><i class='fa-solid fa-arrow-down-z-a' style='color:#0284c7;'></i> Sort Z to A</button><button style='background:#ffffff; border:1px solid #94a3b8; padding:4px 10px; border-radius:4px;'><i class='fa-solid fa-filter' style='color:#f59e0b;'></i> Filter</button></div>"
                }
            }
        ],
        "exam_model": {
            "scenario": "A medical supplies spreadsheet shows cell C4 displaying '#####'. The instructions state: 'Make all data in column C fully visible, format cells C2:C10 as Currency to two decimal places, and sort the table by Cost in descending order.' Describe the actions required.",
            "steps": [
                {
                    "action": "Fix column width",
                    "solution": "Double-click the boundary between column C and column D headers to AutoFit column width.",
                    "mark": "[B1]",
                    "rationale": "Resolves number clipping / ### display issue."
                },
                {
                    "action": "Format currency",
                    "solution": "Select C2:C10 and apply Currency format (£) with 2 decimal places.",
                    "mark": "[B1]",
                    "rationale": "Standard financial formatting."
                },
                {
                    "action": "Sort descending",
                    "solution": "Select the table and sort by Column C (Cost) from Largest to Smallest (Descending).",
                    "mark": "[M1]",
                    "rationale": "Applies descending numerical sort."
                }
            ],
            "tutor_rule": "In Level 1 exams, marks are always allocated for: 1. Making all data visible (no clipped text or ###); 2. Correct currency formatting; 3. Proper sort direction."
        },
        "drills": [
            {
                "question": "What does a row of hashtags '######' displayed inside a spreadsheet cell mean?",
                "options": [
                    {"text": "The number or date is too wide to fit in the current column width", "correct": True},
                    {"text": "The formula contains a spelling mistake", "correct": False},
                    {"text": "The computer is infected with a virus", "correct": False},
                    {"text": "The cell has been permanently deleted", "correct": False}
                ],
                "explanation": "Hashtags appear when a numeric value or date exceeds the visible column boundary."
            },
            {
                "question": "If you sort a staff list by 'Salary' in DESCENDING order, which salary will be at the very top of the table?",
                "options": [
                    {"text": "The highest salary", "correct": True},
                    {"text": "The lowest salary", "correct": False},
                    {"text": "The average salary", "correct": False},
                    {"text": "Zero", "correct": False}
                ],
                "explanation": "Descending order sorts from largest to smallest (Z-A / highest to lowest)."
            },
            {
                "question": "What tool combines multiple adjacent cells into a single wide cell across a table header?",
                "options": [
                    {"text": "Merge & Centre", "correct": True},
                    {"text": "AutoSum", "correct": False},
                    {"text": "Crop", "correct": False},
                    {"text": "Page Break", "correct": False}
                ],
                "explanation": "Merge & Centre combines selected cells into one unified banner cell."
            }
        ],
        "practice": {
            "task": "A department manager asks you to prepare a staff overtime table. Explain how you would format the numbers in the 'Overtime Pay' column as British pounds and pence, and sort the list alphabetically by staff surname.",
            "scaffold_starter": "Formatting pay: \nSorting surnames: ",
            "model_answer": "Formatting pay: Highlight the overtime pay column and choose 'Currency' from the Number Format dropdown, ensuring the '£' symbol and two decimal places are set.\nSorting surnames: Select the entire table data, click Sort & Filter > Custom Sort, choose 'Surname' column, and sort in Ascending order (A to Z).",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Applying Currency (£) format with 2 decimal places."},
                {"tag": "[1 Mark]", "desc": "Sorting by Surname in Ascending (A to Z) order."}
            ]
        },
        "revision_links": [
            {"label": "Spreadsheet Formulas & Functions", "href": "l1-spreadsheet-formulas-functions.html"},
            {"label": "Charts & Data Visualisation", "href": "l1-data-visualisation-charts.html"},
            {"label": "Combining Software & PDF Export", "href": "l1-combining-software-pdf-export.html"}
        ]
    },
    {
        "slug": "l1-spreadsheet-formulas-functions",
        "code": "L1.2.3",
        "skill_area": "2. Creating and Editing",
        "title": "Spreadsheet Formulas: SUM, AVERAGE and COUNT",
        "time": "15 Mins",
        "lead": "Master essential spreadsheet calculations: write basic arithmetic formulas (+, -, *, /), apply core statistical functions (=SUM, =AVERAGE, =COUNT), and replicate formulas down columns using the fill handle.",
        "objectives": [
            "Construct arithmetic formulas using +, -, * (multiplication), and / (division)",
            "Apply core functions: =SUM() for totals, =AVERAGE() for means, and =COUNT() for items",
            "Use the Fill Handle (bottom right drag) to replicate formulas across rows and columns"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Level 1 Digital Skills - SUM, AVERAGE & Replication",
        "steps": [
            {
                "title": "Arithmetic Operators in Spreadsheets",
                "body": "<p>Computers do not use the '×' or '÷' symbols found on school calculators. Always use standard keyboard symbols:</p><ul><li><strong>Addition:</strong> <code>+</code> (e.g. <code>=B2+C2</code>)</li><li><strong>Subtraction:</strong> <code>-</code> (e.g. <code>=B2-C2</code>)</li><li><strong>Multiplication:</strong> <code>*</code> (Asterisk, e.g. <code>=B2*D2</code>)</li><li><strong>Division:</strong> <code>/</code> (Forward slash, e.g. <code>=E2/12</code>)</li></ul>",
                "callout": {
                    "type": "warning",
                    "title": "Exam Rule: Never Hardcode Numbers!",
                    "text": "Never write <code>=15*4</code> in an exam cell! You MUST use the cell references: <code>=B2*C2</code>. If input values change, cell reference formulas update automatically."
                }
            },
            {
                "title": "Core Functions: SUM, AVERAGE, and COUNT",
                "body": "<p>A <strong>Function</strong> is a built-in formula that carries out complex calculations on a range of cells:</p><ul><li><code>=SUM(B2:B10)</code>: Adds all numbers in cells B2 down to B10 together.</li><li><code>=AVERAGE(B2:B10)</code>: Calculates the arithmetic mean (adds values and divides by count).</li><li><code>=COUNT(B2:B10)</code>: Counts how many cells in that range contain numerical values.</li></ul>",
                "ui_sim": {
                    "title": "Formulas & Ranges Demonstration",
                    "content": "<table style='width:100%; border-collapse:collapse; background:#ffffff; font-family:monospace; font-size:0.85rem;'><tr style='background:#f1f5f9;'><th style='border:1px solid #cbd5e1; padding:4px;'>Cell</th><th style='border:1px solid #cbd5e1; padding:4px;'>Formula Typed</th><th style='border:1px solid #cbd5e1; padding:4px;'>Purpose</th></tr><tr><td style='border:1px solid #cbd5e1; padding:4px;'>B11</td><td style='border:1px solid #cbd5e1; padding:4px; color:#0369a1; font-weight:700;'>=SUM(B2:B10)</td><td style='border:1px solid #cbd5e1; padding:4px;'>Total of all entries</td></tr><tr><td style='border:1px solid #cbd5e1; padding:4px;'>B12</td><td style='border:1px solid #cbd5e1; padding:4px; color:#0f766e; font-weight:700;'>=AVERAGE(B2:B10)</td><td style='border:1px solid #cbd5e1; padding:4px;'>Mean average score</td></tr><tr><td style='border:1px solid #cbd5e1; padding:4px;'>B13</td><td style='border:1px solid #cbd5e1; padding:4px; color:#d97706; font-weight:700;'>=COUNT(B2:B10)</td><td style='border:1px solid #cbd5e1; padding:4px;'>Number of records</td></tr></table>"
                }
            },
            {
                "title": "Replicating Formulas with the Fill Handle",
                "body": "<p>Instead of retyping a formula 50 times down a column:</p><ol><li>Click on the cell with the completed formula.</li><li>Hover your mouse over the <strong>bottom-right corner</strong> of the cell until the cursor turns into a thin black cross (<strong>+</strong>) — this is the <strong>Fill Handle</strong>.</li><li>Click and drag downwards. The formula will automatically copy down, updating its row references (relative referencing)!</li></ol>"
            }
        ],
        "exam_model": {
            "scenario": "A clinic pharmacy spreadsheet records: Unit Price in cell C2, and Quantity in cell D2. In cell E2, the total cost must be calculated. Cells C2:D10 contain further items. State the formula for cell E2, and describe how to calculate total costs for all other items down to row 10.",
            "steps": [
                {
                    "action": "Write the multiplication formula",
                    "solution": "=C2*D2",
                    "mark": "[B1]",
                    "rationale": "Formula correctly uses '=' and the '*' multiplication operator with cell references."
                },
                {
                    "action": "Replicate down the column",
                    "solution": "Use the Fill Handle in the bottom-right corner of cell E2 and drag down to cell E10.",
                    "mark": "[M1]",
                    "rationale": "Replicates formula using relative referencing."
                }
            ],
            "tutor_rule": "In Level 1 exams, you will be asked to state the formula and show how to replicate it. Remember: multiply is '*', divide is '/', total is '=SUM()'."
        },
        "drills": [
            {
                "question": "Which formula correctly calculates the arithmetic mean of values in cells B2 to B8?",
                "options": [
                    {"text": "=AVERAGE(B2:B8)", "correct": True},
                    {"text": "=MEAN(B2:B8)", "correct": False},
                    {"text": "=SUM(B2:B8)/COUNT", "correct": False},
                    {"text": "=TOTAL(B2:B8)", "correct": False}
                ],
                "explanation": "=AVERAGE() is the built-in spreadsheet function used to find the mean value."
            },
            {
                "question": "What keyboard symbol is used in spreadsheets to MULTIPLY two numbers or cell references?",
                "options": [
                    {"text": "* (Asterisk)", "correct": True},
                    {"text": "x (Letter x)", "correct": False},
                    {"text": "• (Bullet point)", "correct": False},
                    {"text": "& (Ampersand)", "correct": False}
                ],
                "explanation": "The asterisk (*) is the mathematical operator for multiplication in spreadsheets and programming."
            },
            {
                "question": "What happens when you drag the Fill Handle down from a cell containing '=B2*C2'?",
                "options": [
                    {"text": "The formula copies down, automatically adjusting to =B3*C3, =B4*C4, etc.", "correct": True},
                    {"text": "It deletes all formulas in the column", "correct": False},
                    {"text": "It turns the cells into pie charts", "correct": False},
                    {"text": "It freezes the computer", "correct": False}
                ],
                "explanation": "Relative cell references increment automatically when copied with the Fill Handle."
            }
        ],
        "practice": {
            "task": "A spreadsheet records weekly patient visits in cells D2 to D6. Write down the exact formulas needed for:<br>1. Total patient visits in cell D7<br>2. Average weekly visits in cell D8",
            "scaffold_starter": "1. Total formula in D7: =\n2. Average formula in D8: =",
            "model_answer": "1. Total formula in D7: =SUM(D2:D6)\n2. Average formula in D8: =AVERAGE(D2:D6)",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Using =SUM(D2:D6) for the total."},
                {"tag": "[1 Mark]", "desc": "Using =AVERAGE(D2:D6) for the mean average."}
            ]
        },
        "revision_links": [
            {"label": "Spreadsheet Layout & Sorting", "href": "l1-spreadsheet-design-formatting.html"},
            {"label": "Charts & Data Visualisation", "href": "l1-data-visualisation-charts.html"},
            {"label": "Combining Software & PDF Export", "href": "l1-combining-software-pdf-export.html"}
        ]
    },
    {
        "slug": "l1-data-visualisation-charts",
        "code": "L1.2.4",
        "skill_area": "2. Creating and Editing",
        "title": "Charts and Data Visualisation",
        "time": "15 Mins",
        "lead": "Convert spreadsheet numbers into meaningful visual charts: choose between column, bar, and pie charts, format chart titles and axis labels, and interpret visual trends for workplace presentations.",
        "objectives": [
            "Select appropriate chart types: Column/Bar for comparing categories; Pie charts for proportions of a whole",
            "Highlight non-adjacent data ranges correctly using the Ctrl key",
            "Add meaningful chart titles, axis labels (X & Y), and legend keys"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Level 1 Digital Skills - Creating & Formatting Charts",
        "steps": [
            {
                "title": "Selecting the Right Chart Type",
                "body": "<p>A chart tells a visual story in a glance:</p><ul><li><strong>Column / Bar Chart:</strong> Best for <strong>comparing different items or categories</strong> (e.g. comparing attendance across 5 clinic sites or monthly expenses).</li><li><strong>Pie Chart:</strong> Best for showing <strong>proportions of a whole (percentages totaling 100%)</strong> (e.g. breakdown of energy use or percentage of staff by job role).</li><li><strong>Line Graph:</strong> Best for tracking <strong>changes over continuous time</strong> (e.g. patient temperatures over 24 hours).</li></ul>",
                "callout": {
                    "type": "tutor",
                    "title": "Tutor Abdul's Golden Chart Rule",
                    "text": "If comparing distinct items: use a <strong>Column Chart</strong>. If showing parts of 100%: use a <strong>Pie Chart</strong>. Never use a Pie Chart for changes over time!"
                }
            },
            {
                "title": "How to Create a Chart in Excel",
                "body": "<ol><li>Select the labels AND the numbers you want in the chart (do not include the 'Total' row, or the total bar will distort the scale!).</li><li>If labels and data are in separate columns, hold <kbd class='dfs-kbd'>Ctrl</kbd> to highlight both ranges.</li><li>Go to the <strong>Insert</strong> tab on the ribbon.</li><li>Click <strong>Insert Column Chart</strong> or <strong>Insert Pie Chart</strong>.</li></ol>",
                "shortcuts": [
                    {"label": "Create Instant Default Chart", "key": "F11"},
                    {"label": "Select Non-Adjacent Cells", "key": "Ctrl + Click"}
                ]
            },
            {
                "title": "Essential Chart Elements (Mark Scheme Checklist)",
                "body": "<p>An unlabelled chart will score zero marks in an exam! Ensure your chart includes:</p><ul><li><strong>Chart Title:</strong> Explains clearly what the chart shows (e.g. <em>'Monthly Clinic Appointments by Department 2026'</em>).</li><li><strong>Horizontal Axis Title (X-Axis):</strong> Labels the categories (e.g. <em>'Department'</em>).</li><li><strong>Vertical Axis Title (Y-Axis):</strong> Labels the values and units (e.g. <em>'Number of Patients'</em>).</li><li><strong>Data Labels or Legend:</strong> Clarifies colour keys when comparing multiple series.</li></ul>",
                "ui_sim": {
                    "title": "Formatted Column Chart Preview",
                    "content": "<div style='background:#ffffff; border:1px solid #cbd5e1; padding:12px; border-radius:4px; text-align:center;'><strong style='color:#0f172a; font-size:0.95rem;'>Quarterly Vaccine Uptake 2026</strong><div style='display:flex; justify-content:space-around; align-items:flex-end; height:100px; padding:10px 20px; border-left:2px solid #64748b; border-bottom:2px solid #64748b; margin:10px 0;'><div style='width:35px; height:45%; background:#0284c7; border-radius:3px 3px 0 0;'></div><div style='width:35px; height:70%; background:#0284c7; border-radius:3px 3px 0 0;'></div><div style='width:35px; height:90%; background:#0284c7; border-radius:3px 3px 0 0;'></div><div style='width:35px; height:60%; background:#0284c7; border-radius:3px 3px 0 0;'></div></div><div style='font-size:0.75rem; color:#64748b;'>Quarter 1 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Quarter 2 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Quarter 3 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Quarter 4</div></div>"
                }
            }
        ],
        "exam_model": {
            "scenario": "A health centre manager wants to compare the number of blood tests conducted across four branches: Central (140), North (90), West (110), and East (80). You create a column chart. List three elements that must be added to the chart to make it fully labelled for a board meeting.",
            "steps": [
                {
                    "action": "Add Chart Title",
                    "solution": "Add an informative chart title, e.g. 'Blood Tests Conducted by Branch'.",
                    "mark": "[B1]",
                    "rationale": "Clearly conveys the dataset purpose."
                },
                {
                    "action": "Add Axis Titles",
                    "solution": "Add X-Axis title 'Clinic Branch' and Y-Axis title 'Number of Tests'.",
                    "mark": "[B1]",
                    "rationale": "Labels both measurement units and category variables."
                },
                {
                    "action": "Select correct chart type",
                    "solution": "Ensure a Column or Bar chart is used (not a line graph or scatter plot).",
                    "mark": "[B1]",
                    "rationale": "Matches chart format to categorical comparison."
                }
            ],
            "tutor_rule": "In Level 1 exams, you will be penalized if you include the 'Total' row inside your chart data range. Always exclude the total row!"
        },
        "drills": [
            {
                "question": "Which chart type is best for showing the proportion of total budget spent by each department (percentages of 100%)?",
                "options": [
                    {"text": "Pie Chart", "correct": True},
                    {"text": "Line Graph", "correct": False},
                    {"text": "Scatter Plot", "correct": False},
                    {"text": "Radar Chart", "correct": False}
                ],
                "explanation": "Pie charts illustrate proportional parts of a single whole."
            },
            {
                "question": "Why should you NOT include the 'Total' row when highlighting data to generate a column chart?",
                "options": [
                    {"text": "The massive total column will distort the scale, making all individual data bars look tiny and difficult to compare", "correct": True},
                    {"text": "Excel crashes if you highlight totals", "correct": False},
                    {"text": "Totals can only be displayed in red font", "correct": False},
                    {"text": "Printers refuse to print total columns", "correct": False}
                ],
                "explanation": "Including totals doubles the graph scale and squashes individual category comparisons."
            },
            {
                "question": "What key do you hold down on your keyboard to select two separate, non-adjacent columns in Excel?",
                "options": [
                    {"text": "Ctrl Key", "correct": True},
                    {"text": "Shift Key", "correct": False},
                    {"text": "Alt Key", "correct": False},
                    {"text": "Tab Key", "correct": False}
                ],
                "explanation": "Holding Ctrl allows selecting multiple non-touching ranges of cells."
            }
        ],
        "practice": {
            "task": "A local community clinic tracks patient satisfaction ratings (Excellent: 45%, Good: 35%, Fair: 15%, Poor: 5%). State which chart type you would choose to display this data and list two formatting features you would include to make the chart easy to understand.",
            "scaffold_starter": "Chart Type: \nFeature 1: \nFeature 2: ",
            "model_answer": "Chart Type: A Pie Chart (or 2D Column Chart) because the data represents percentages of a whole.\nFeature 1: A clear descriptive title: 'Patient Satisfaction Survey Results 2026'.\nFeature 2: Data labels on each slice showing the exact percentage numbers, and a clear legend identifying each rating.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Selecting Pie Chart or Column Chart with valid justification."},
                {"tag": "[1 Mark]", "desc": "Describing clear title and data labels / legend."}
            ]
        },
        "revision_links": [
            {"label": "Spreadsheet Formulas & SUM", "href": "l1-spreadsheet-formulas-functions.html"},
            {"label": "Spreadsheet Layout & Sorting", "href": "l1-spreadsheet-design-formatting.html"},
            {"label": "Designing Digital Presentations", "href": "l1-presentations-multimedia.html"}
        ]
    },
    {
        "slug": "l1-presentations-multimedia",
        "code": "L1.2.5",
        "skill_area": "2. Creating and Editing",
        "title": "Designing Digital Presentations and Slide Design",
        "time": "15 Mins",
        "lead": "Design engaging slide decks in software like PowerPoint: apply consistent themes, select appropriate slide layouts, insert bullet points and images, add speaker notes, and apply subtle slide transitions.",
        "objectives": [
            "Select appropriate slide layouts (Title Slide, Title and Content, Two Content)",
            "Apply consistent slide themes, readable colour contrast, and concise bullet points",
            "Add speaker notes and apply appropriate slide transitions without distracting animations"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Level 1 Digital Skills - PowerPoint Slides & Presentation Design",
        "steps": [
            {
                "title": "Choosing Slide Layouts",
                "body": "<p>When adding a new slide (<kbd class='dfs-kbd'>Ctrl + M</kbd>), always select a layout suited to your content:</p><ul><li><strong>Title Slide:</strong> First slide of your deck. Contains presentation title, subtitle, and speaker name.</li><li><strong>Title and Content:</strong> Standard slide layout. Has a title banner at the top and a large content box for bullet points, a table, or a chart.</li><li><strong>Two Content / Comparison:</strong> Features two columns side by side — ideal for comparing pros and cons or placing a photo next to text.</li></ul>",
                "shortcuts": [
                    {"label": "New Slide", "key": "Ctrl + M"},
                    {"label": "Start Slide Show", "key": "F5"}
                ]
            },
            {
                "title": "Principles of Professional Slide Design",
                "body": "<p>Avoid cluttered slides that overwhelm the audience:</p><ul><li><strong>The 6×6 Rule:</strong> Aim for no more than 6 bullet points per slide, with roughly 6 words per bullet.</li><li><strong>High Contrast:</strong> Dark text on light backgrounds (or white text on deep navy) ensures clear legibility from the back of a meeting room.</li><li><strong>Consistent Theme:</strong> Use the same fonts, brand colours, and layout styling across every slide in the deck.</li></ul>",
                "callout": {
                    "type": "tutor",
                    "title": "Tutor Abdul's Golden Presentation Tip",
                    "text": "Slides are visual prompts for the audience, not a teleprompter for you to read word-for-word! Use concise bullets on screen and write detailed explanations in your <strong>Speaker Notes</strong>."
                }
            },
            {
                "title": "Adding Speaker Notes & Slide Transitions",
                "body": "<p>To present with confidence:</p><ul><li><strong>Speaker Notes:</strong> Click the <strong>Notes</strong> button at the bottom of PowerPoint. Type your private talking points here. When using Presenter View on a projector, only you can see the notes on your laptop screen!</li><li><strong>Slide Transitions:</strong> The animation when moving from one slide to the next (e.g. <strong>Fade</strong> or <strong>Push</strong>). Keep transitions subtle and consistent across all slides; avoid spinning or noisy effects.</li></ul>",
                "ui_sim": {
                    "title": "PowerPoint Slide & Notes View",
                    "content": "<div style='background:#f8fafc; border:1px solid #cbd5e1; padding:10px; border-radius:4px; font-size:0.85rem;'><div style='background:#ffffff; border:1px solid #94a3b8; height:90px; padding:10px; border-radius:4px; margin-bottom:8px;'><h4 style='color:#0f172a; margin-bottom:4px;'>Fire Evacuation Protocols</h4><ul style='padding-left:18px; color:#475569;'><li>Sound the nearest alarm</li><li>Evacuate via marked fire exits</li><li>Assemble at Point B</li></ul></div><div style='background:#f1f5f9; padding:6px; border:1px dashed #94a3b8; font-size:0.78rem; color:#334155;'><i class='fa-regular fa-note-sticky' style='color:#f59e0b;'></i> <strong>Speaker Notes:</strong> Remind staff that elevators must not be used during fire drills.</div></div>"
                }
            }
        ],
        "exam_model": {
            "scenario": "A trainer is designing a 5-slide presentation on 'Infection Control'. Explain two design rules they should follow to ensure the slides are accessible and professional, and state where the trainer should type their personal talking notes.",
            "steps": [
                {
                    "action": "First design rule",
                    "solution": "Use concise bullet points (short key phrases rather than huge paragraphs of text).",
                    "mark": "[B1]",
                    "rationale": "Prevents cognitive overload and maintains visual clarity."
                },
                {
                    "action": "Second design rule",
                    "solution": "Ensure strong colour contrast between text and background (e.g. dark text on light cream/white background).",
                    "mark": "[B1]",
                    "rationale": "Ensures legibility and accessibility for audience members with visual impairments."
                },
                {
                    "action": "Location for private notes",
                    "solution": "In the Speaker Notes pane at the bottom of the slide window.",
                    "mark": "[B1]",
                    "rationale": "Speaker notes are visible only to the presenter."
                }
            ],
            "tutor_rule": "In Level 1 exams, presentation questions test layout simplicity: 'Concise bullets', 'High contrast', and 'Speaker notes'."
        },
        "drills": [
            {
                "question": "What keyboard key starts a slide show from the very first slide in Microsoft PowerPoint?",
                "options": [
                    {"text": "F5", "correct": True},
                    {"text": "F1", "correct": False},
                    {"text": "Ctrl + P", "correct": False},
                    {"text": "Esc", "correct": False}
                ],
                "explanation": "F5 launches the slide show from slide 1; Shift + F5 starts from the current active slide."
            },
            {
                "question": "Where should a presenter type personal reminders and talking prompts that the audience cannot see on the main screen?",
                "options": [
                    {"text": "In the Speaker Notes pane below the slide", "correct": True},
                    {"text": "Directly into the slide title box in tiny 4pt font", "correct": False},
                    {"text": "In the Recycle Bin", "correct": False},
                    {"text": "On the slide master background", "correct": False}
                ],
                "explanation": "Speaker notes appear on the presenter's private display monitor without showing on the projector."
            },
            {
                "question": "Why should flashy, spinning slide transitions be avoided in professional workplace presentations?",
                "options": [
                    {"text": "They distract the audience from the content and look unprofessional", "correct": True},
                    {"text": "They cause computer monitors to overheat", "correct": False},
                    {"text": "They erase slide text automatically", "correct": False},
                    {"text": "They prevent PowerPoint from saving", "correct": False}
                ],
                "explanation": "Subtle transitions maintain professional focus, whereas excessive animations distract."
            }
        ],
        "practice": {
            "task": "You are creating a short presentation for new apprentices. Describe the steps to insert a new slide with a 'Title and Content' layout, add two bullet points, and apply a subtle 'Fade' transition.",
            "scaffold_starter": "New slide: \nContent: \nTransition: ",
            "model_answer": "New slide: On the Home tab, click the 'New Slide' dropdown and select 'Title and Content'.\nContent: Type 'Key Safety Rules' in the title box, and enter two concise bullet points in the main text box.\nTransition: Go to the 'Transitions' tab, click 'Fade', and click 'Apply To All' for consistency.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Selecting Title and Content layout and entering concise bullets."},
                {"tag": "[1 Mark]", "desc": "Applying a subtle transition (Fade) consistently."}
            ]
        },
        "revision_links": [
            {"label": "Professional Word Formatting", "href": "l1-word-processing-professional.html"},
            {"label": "Charts & Data Visualisation", "href": "l1-data-visualisation-charts.html"},
            {"label": "Combining Software & PDF Export", "href": "l1-combining-software-pdf-export.html"}
        ]
    },
    {
        "slug": "l1-combining-software-pdf-export",
        "code": "L1.2.6",
        "skill_area": "2. Creating and Editing",
        "title": "Integrating Applications and PDF Export",
        "time": "15 Mins",
        "lead": "Integrate content across multiple software applications: copy spreadsheet charts and tables into Word documents and PowerPoint slides, use Print Preview, and export documents as accessible PDF files.",
        "objectives": [
            "Copy and paste data tables and charts from spreadsheets into word-processed reports",
            "Understand paste options (linking data vs pasting as static picture)",
            "Use Print Preview to check margins and export finished files as read-only PDFs"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Level 1 Digital Skills - Combining Applications & PDF Export",
        "steps": [
            {
                "title": "Copying Content Between Applications",
                "body": "<p>In workplace tasks, you often generate calculations in Excel and need to showcase them in a Word report or PowerPoint presentation:</p><ol><li>In your spreadsheet, select the table or chart.</li><li>Copy it (<kbd class='dfs-kbd'>Ctrl + C</kbd>).</li><li>Switch to your Word document (<kbd class='dfs-kbd'>Alt + Tab</kbd>) and position your cursor.</li><li>Paste it (<kbd class='dfs-kbd'>Ctrl + V</kbd>).</li></ol>",
                "shortcuts": [
                    {"label": "Copy", "key": "Ctrl + C"},
                    {"label": "Paste", "key": "Ctrl + V"},
                    {"label": "Switch Between Open Windows", "key": "Alt + Tab"}
                ]
            },
            {
                "title": "Paste Options: Linked Data vs Picture",
                "body": "<p>When pasting a table or chart into Word, click the <strong>Paste Options</strong> button:</p><ul><li><strong>Link Data (Keep Source Formatting):</strong> If figures in your original Excel sheet change, the chart inside Word updates automatically!</li><li><strong>Picture:</strong> Pastes the chart as a static image. It cannot be edited, but it guarantees that nobody can tamper with your figures.</li></ul>"
            },
            {
                "title": "Print Preview and Exporting as PDF",
                "body": "<p>Before distributing any finished report:</p><ul><li><strong>Print Preview (<kbd class='dfs-kbd'>Ctrl + P</kbd>):</strong> Check that tables and charts do not split awkwardly across page breaks, and ensure text margins look balanced.</li><li><strong>Export to PDF:</strong> Click <strong>File &gt; Export &gt; Create PDF/XPS</strong> (or <strong>File &gt; Save As &gt; PDF</strong>). A PDF locks formatting so it looks identical on any PC, tablet, or smartphone without font shifting.</li></ul>",
                "ui_sim": {
                    "title": "Export to PDF Dialogue",
                    "content": "<div style='background:#f8fafc; border:1px solid #cbd5e1; padding:10px; border-radius:4px; font-size:0.85rem;'><div style='color:#0f172a; font-weight:700; margin-bottom:6px;'><i class='fa-solid fa-file-pdf' style='color:#dc2626;'></i> Publish as PDF</div><div style='display:flex; justify-content:space-between; align-items:center;'><div>File name: <strong>Clinical_Audit_Report_2026.pdf</strong><br><span style='color:#64748b;'>Optimised for: Standard (publishing online and printing)</span></div><button style='background:#dc2626; color:#ffffff; border:none; padding:6px 14px; border-radius:4px; font-weight:700;'>Publish</button></div></div>"
                }
            }
        ],
        "exam_model": {
            "scenario": "A clinic supervisor creates an expenses spreadsheet and wants to include the final bar chart inside a formal Word report for the board. Explain how to copy the chart into Word, and explain why the supervisor should save the final completed report as a PDF before emailing it to board members.",
            "steps": [
                {
                    "action": "Copy and paste process",
                    "solution": "Select the chart in Excel, press Ctrl+C (Copy), switch to Word, and press Ctrl+V (Paste).",
                    "mark": "[B1]",
                    "rationale": "Demonstrates inter-application data transfer."
                },
                {
                    "action": "State reason for PDF format",
                    "solution": "PDF preserves exact formatting, prevents accidental editing, and opens reliably on all devices without requiring Microsoft Word.",
                    "mark": "[B1]",
                    "rationale": "Explains universal compatibility and document integrity."
                }
            ],
            "tutor_rule": "In Level 1 exams, 'Save as PDF' is the benchmark answer whenever asked how to share a document securely so that formatting does not get broken."
        },
        "drills": [
            {
                "question": "What is the primary advantage of saving a finished workplace report as a PDF rather than a Word document before sending it to clients?",
                "options": [
                    {"text": "PDF preserves layout and formatting identically across all devices and prevents accidental text editing", "correct": True},
                    {"text": "PDF files delete themselves after 24 hours", "correct": False},
                    {"text": "PDF files make your computer run faster", "correct": False},
                    {"text": "PDF files can only be read on paper", "correct": False}
                ],
                "explanation": "PDFs lock visual presentation and prevent formatting shifts or unintended changes across devices."
            },
            {
                "question": "What keyboard shortcut allows you to quickly switch between your open Excel spreadsheet and your Word document?",
                "options": [
                    {"text": "Alt + Tab", "correct": True},
                    {"text": "Ctrl + P", "correct": False},
                    {"text": "Shift + Enter", "correct": False},
                    {"text": "F1", "correct": False}
                ],
                "explanation": "Alt + Tab switches between active application windows smoothly."
            },
            {
                "question": "Why should you always check 'Print Preview' before printing or exporting a multi-page document?",
                "options": [
                    {"text": "To check that headings, tables, and images are not awkwardly split across page breaks", "correct": True},
                    {"text": "To test the internet speed", "correct": False},
                    {"text": "To clean the printer cartridges", "correct": False},
                    {"text": "To change the computer password", "correct": False}
                ],
                "explanation": "Print Preview displays exact page layout, margins, and breaks before committing to paper or export."
            }
        ],
        "practice": {
            "task": "A company is publishing an annual health review. Describe the process of taking a quarterly patient attendance chart from Excel and placing it into section 3 of a Word report, followed by exporting the document as a PDF.",
            "scaffold_starter": "1. Copying: \n2. Pasting in Word: \n3. PDF Export: ",
            "model_answer": "1. Copying: In Excel, click on the attendance chart and press Ctrl + C.\n2. Pasting: In Word, scroll to section 3, click where the chart should go, and press Ctrl + V (or choose Paste as Linked Data).\n3. PDF Export: Click File > Export > Create PDF/XPS, choose a clear filename ('Annual_Health_Review_2026.pdf'), and click Publish.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Copying from spreadsheet and pasting into the correct section of Word."},
                {"tag": "[1 Mark]", "desc": "Using File > Export or Save As to publish as PDF."}
            ]
        },
        "revision_links": [
            {"label": "Professional Word Formatting", "href": "l1-word-processing-professional.html"},
            {"label": "Charts & Data Visualisation", "href": "l1-data-visualisation-charts.html"},
            {"label": "Workplace Email Etiquette", "href": "l1-workplace-email-etiquette.html"}
        ]
    }
]
