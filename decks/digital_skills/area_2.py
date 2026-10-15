#!/usr/bin/env python3
"""Area 2: Creating and Editing Digital Content (Cards 11-24)"""
import xml.etree.ElementTree as ET
CARDS = [ { 'answer_text': 'Ctrl + Enter.',
    'challenge_prompt': 'What keyboard shortcut inserts a new page break '
                        'instantly in Microsoft Word or Google Docs?',
    'dfe_code': 'DFS 2.1',
    'golden_rule': 'Use Heading styles to automatically create clickable Contents pages!',
    'id': 'dfs-11',
    'level': 'l2',
    'level_label': 'Level 1 / 2',
    'number': 11,
    'rule_body': 'Use built-in Heading Styles (Heading 1 for main titles, '
                 'Heading 2 for subheadings) instead of manually bolding and '
                 'enlarging text. This creates an automatic table of contents '
                 'and screen-reader structure.',
    'rule_heading': 'H1, H2 &amp; Consistent Hierarchy',
    'strand_name': 'Creating Content',
    'strand_theme': 'orange',
    'subject': 'digital',
    'subject_label': 'Digital Skills',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" '
                'xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(60, 20)">\n'
                '            <rect x="0" y="0" width="340" height="130" rx="8" '
                'fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>\n'
                '            <text x="170" y="26" font-size="12" '
                'font-weight="900" fill="#1e40af" '
                'text-anchor="middle">BUILT-IN HEADING STYLES</text>\n'
                '            <text x="30" y="55" font-size="13" '
                'font-weight="900" fill="#1e3a8a">Heading 1: Major Document '
                'Title</text>\n'
                '            <text x="30" y="80" font-size="11" '
                'font-weight="800" fill="#2563eb">Heading 2: Section '
                'Subheading</text>\n'
                '            <text x="30" y="105" font-size="10.5" '
                'font-weight="700" fill="#475569">Normal: Body text with 1.15 '
                'line spacing</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Word Processing: Headings &amp; Styles',
    'watch_out': 'Use Ctrl + Enter for new pages — never press Enter multiple times.'},
  { 'answer_text': 'Merge Cells.',
    'challenge_prompt': 'What table feature combines two or more adjacent '
                        'cells into a single large cell?',
    'dfe_code': 'DFS 2.2',
    'golden_rule': 'Use tables to align numbers and facts rather than pressing '
                   'the Spacebar or Tab key!',
    'id': 'dfs-12',
    'level': 'l2',
    'level_label': 'Level 1 / 2',
    'number': 12,
    'rule_body': 'Tables: Insert rows and columns to align comparative data '
                 'neatly. Merge cells to create spanning banner headers. Set '
                 'header rows to repeat across page breaks.',
    'rule_heading': 'Organising Information into Columns',
    'strand_name': 'Creating Content',
    'strand_theme': 'orange',
    'subject': 'digital',
    'subject_label': 'Digital Skills',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" '
                'xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(60, 20)">\n'
                '            <rect x="0" y="0" width="340" height="130" rx="8" '
                'fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>\n'
                '            <rect x="20" y="20" width="300" height="25" '
                'fill="#1e3a8a"/>\n'
                '            <text x="170" y="37" font-size="11" '
                'font-weight="800" fill="#ffffff" text-anchor="middle">Merged '
                'Header Cell</text>\n'
                '            <line x1="20" y1="45" x2="320" y2="45" '
                'stroke="#cbd5e1"/>\n'
                '            <line x1="170" y1="45" x2="170" y2="115" '
                'stroke="#cbd5e1"/>\n'
                '            <text x="95" y="75" font-size="11" '
                'font-weight="700" fill="#0f172a" text-anchor="middle">Column '
                'A</text>\n'
                '            <text x="245" y="75" font-size="11" '
                'font-weight="700" fill="#0f172a" text-anchor="middle">Column '
                'B</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Word Processing: Tables &amp; Lists',
    'watch_out': 'Never align text by tapping the spacebar repeatedly — it '
                 'falls out of alignment on other screens.'},
  { 'answer_text': 'Alt Text allows screen readers to describe the image to '
                   'visually impaired users.',
    'challenge_prompt': 'Why should you provide Alt Text (alternative text) '
                        'when inserting an image into a document or website?',
    'dfe_code': 'DFS 2.3',
    'golden_rule': 'Drag corner handles only so images keep their proper proportions!',
    'id': 'dfs-13',
    'level': 'l2',
    'level_label': 'Level 1 / 2',
    'number': 13,
    'rule_body': 'Always resize images using CORNER handles to maintain '
                 'original aspect ratio (prevent squishing). Text Wrapping: '
                 "'Square' or 'Tight' wraps text smoothly around the picture. "
                 'Always add Alt Text for accessibility.',
    'rule_heading': 'Square, Tight &amp; Aspect Ratio',
    'strand_name': 'Creating Content',
    'strand_theme': 'orange',
    'subject': 'digital',
    'subject_label': 'Digital Skills',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" '
                'xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(60, 20)">\n'
                '            <rect x="0" y="0" width="340" height="130" rx="8" '
                'fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>\n'
                '            <rect x="25" y="30" width="75" height="70" '
                'fill="#bae6fd" stroke="#0284c7" rx="4"/>\n'
                '            <text x="62" y="70" font-size="10" '
                'font-weight="800" fill="#0369a1" '
                'text-anchor="middle">IMAGE</text>\n'
                '            <g transform="translate(120, 35)">\n'
                '              <text x="0" y="15" font-size="10.5" '
                'font-weight="700" fill="#0f172a">Text wraps neatly '
                'around</text>\n'
                '              <text x="0" y="35" font-size="10.5" '
                'font-weight="700" fill="#0f172a">the image without '
                'strange</text>\n'
                '              <text x="0" y="55" font-size="10.5" '
                'font-weight="700" fill="#0f172a">blank gaps on the '
                'page.</text>\n'
                '              <text x="0" y="75" font-size="10" '
                'font-weight="800" fill="#16a34a">Wrapping: Square</text>\n'
                '            </g>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Images &amp; Text Wrapping',
    'watch_out': 'Always add Alt Text to images for accessibility and screen readers.'},
  { 'answer_text': 'D14.',
    'challenge_prompt': 'What cell reference is located at the intersection of '
                        'column D and row 14?',
    'dfe_code': 'DFS 2.4',
    'golden_rule': 'Column Letter ALWAYS comes before the Row Number (e.g. C5, '
                   'NEVER 5C)!',
    'id': 'dfs-14',
    'level': 'l2',
    'level_label': 'Level 1 / 2',
    'number': 14,
    'rule_body': 'Columns: Lettered vertically (A, B, C...). Rows: Numbered '
                 'horizontally (1, 2, 3...). Cell Reference: The intersection '
                 'letter + number (e.g. B4 = column B, row 4). Format cells as '
                 'Currency (£), Percentage (%), or Date.',
    'rule_heading': 'Columns, Rows &amp; Cell References',
    'strand_name': 'Creating Content',
    'strand_theme': 'orange',
    'subject': 'digital',
    'subject_label': 'Digital Skills',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" '
                'xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(60, 20)">\n'
                '            <rect x="0" y="0" width="340" height="130" rx="8" '
                'fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>\n'
                '            <rect x="20" y="20" width="40" height="25" '
                'fill="#e2e8f0"/>\n'
                '            <rect x="60" y="20" width="80" height="25" '
                'fill="#e2e8f0"/><text x="100" y="37" font-size="11" '
                'font-weight="800" fill="#0f172a" '
                'text-anchor="middle">A</text>\n'
                '            <rect x="140" y="20" width="80" height="25" '
                'fill="#3b82f6"/><text x="180" y="37" font-size="11" '
                'font-weight="900" fill="#ffffff" '
                'text-anchor="middle">B</text>\n'
                '            <rect x="220" y="20" width="80" height="25" '
                'fill="#e2e8f0"/><text x="260" y="37" font-size="11" '
                'font-weight="800" fill="#0f172a" '
                'text-anchor="middle">C</text>\n'
                '            <rect x="20" y="45" width="40" height="25" '
                'fill="#e2e8f0"/><text x="40" y="62" font-size="11" '
                'font-weight="800" fill="#0f172a" '
                'text-anchor="middle">1</text>\n'
                '            <rect x="20" y="70" width="40" height="25" '
                'fill="#3b82f6"/><text x="40" y="87" font-size="11" '
                'font-weight="900" fill="#ffffff" '
                'text-anchor="middle">2</text>\n'
                '            <rect x="140" y="70" width="80" height="25" '
                'fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>\n'
                '            <text x="180" y="87" font-size="11" '
                'font-weight="900" fill="#1e40af" text-anchor="middle">B2 '
                '★</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Spreadsheets: Anatomy of a Sheet',
    'watch_out': 'Format raw numbers as Currency (£) so the pound sign appears '
                 'automatically.'},
  { 'answer_text': '=B4*C4.',
    'challenge_prompt': 'Write the formula to multiply the quantity in cell B4 '
                        'by the unit price in cell C4.',
    'dfe_code': 'DFS 2.5',
    'golden_rule': "Always begin spreadsheet formulas with '=' (e.g. =A1+B1)!",
    'id': 'dfs-15',
    'level': 'l2',
    'level_label': 'Level 1 / 2',
    'number': 15,
    'rule_body': "Every formula in Excel / Google Sheets MUST begin with '=': "
                 'Add: =A1+B1. Subtract: =A1-B1. Multiply: =A1*B1 (asterisk). '
                 'Divide: =A1/B1 (forward slash). Never type hardcoded numbers '
                 'into formulas.',
    'rule_heading': 'Always Start with an Equals Sign (=)',
    'strand_name': 'Creating Content',
    'strand_theme': 'orange',
    'subject': 'digital',
    'subject_label': 'Digital Skills',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" '
                'xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(60, 20)">\n'
                '            <rect x="0" y="0" width="340" height="130" rx="8" '
                'fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>\n'
                '            <text x="170" y="26" font-size="12" '
                'font-weight="900" fill="#15803d" '
                'text-anchor="middle">SPREADSHEET OPERATORS</text>\n'
                '            <text x="30" y="55" font-size="11.5" '
                'font-weight="800" fill="#0f172a">Addition: =B2 + C2</text>\n'
                '            <text x="30" y="78" font-size="11.5" '
                'font-weight="800" fill="#0f172a">Subtraction: =B2 - '
                'C2</text>\n'
                '            <text x="30" y="101" font-size="11.5" '
                'font-weight="800" fill="#2563eb">Multiplication: =B2 * C2  '
                '(Asterisk *)</text>\n'
                '            <text x="30" y="122" font-size="11.5" '
                'font-weight="800" fill="#dc2626">Division: =B2 / C2  (Slash '
                '/)</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Spreadsheets: Basic Arithmetic',
    'watch_out': "Use '*' to multiply and '/' to divide — never type the letter 'x'."},
  { 'answer_text': '=AVERAGE(D3:D15).',
    'challenge_prompt': 'Write the function to calculate the average of sales '
                        'in cells D3 to D15.',
    'dfe_code': 'DFS 2.6',
    'golden_rule': 'The colon (:) indicates a contiguous cell range from start '
                   'to finish!',
    'id': 'dfs-16',
    'level': 'l2',
    'level_label': 'Level 1 / 2',
    'number': 16,
    'rule_body': '=SUM(B2:B10): Adds all numbers in range. =AVERAGE(B2:B10): '
                 'Calculates mean. =MAX(B2:B10): Finds highest value. '
                 "=MIN(B2:B10): Finds lowest value. Colon (:) means 'through "
                 "to'.",
    'rule_heading': 'Ranges with Colons (e.g. B2:B10)',
    'strand_name': 'Creating Content',
    'strand_theme': 'orange',
    'subject': 'digital',
    'subject_label': 'Digital Skills',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" '
                'xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(60, 20)">\n'
                '            <rect x="0" y="0" width="340" height="130" rx="8" '
                'fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>\n'
                '            <text x="170" y="26" font-size="12" '
                'font-weight="900" fill="#1e40af" text-anchor="middle">CORE '
                'EXCEL FUNCTIONS</text>\n'
                '            <text x="30" y="55" font-size="11" '
                'font-weight="800" fill="#0f172a">• =SUM(C2:C20)  →  Total of '
                'all 19 cells</text>\n'
                '            <text x="30" y="80" font-size="11" '
                'font-weight="800" fill="#0f172a">• =AVERAGE(C2:C20)  →  Mean '
                'average score</text>\n'
                '            <text x="30" y="105" font-size="11" '
                'font-weight="800" fill="#059669">• =MAX(C2:C20)  •  '
                '=MIN(C2:C20)</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Spreadsheets: SUM &amp; AVERAGE',
    'watch_out': "Don't write '=SUM(A1+A2)' — either write '=SUM(A1:A2)' or "
                 "'=A1+A2'."},
  { 'answer_text': '=COUNTA(B2:B30).',
    'challenge_prompt': 'Which function should you use to count how many '
                        'employees signed in on a text attendance sheet in '
                        'cells B2 to B30?',
    'dfe_code': 'DFS 2.7',
    'golden_rule': 'Use COUNTA to count attendee names or text entries!',
    'id': 'dfs-17',
    'level': 'l2',
    'level_label': 'Level 1 / 2',
    'number': 17,
    'rule_body': '=COUNT(range): Counts ONLY cells containing NUMBERS. '
                 '=COUNTA(range): Counts ALL non-empty cells (numbers, text, '
                 "symbols). Think 'Count All' (COUNTA).",
    'rule_heading': 'Count Numbers vs Count Non-Empty Cells',
    'strand_name': 'Creating Content',
    'strand_theme': 'orange',
    'subject': 'digital',
    'subject_label': 'Digital Skills',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" '
                'xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(40, 20)">\n'
                '            <rect x="0" y="0" width="180" height="125" rx="8" '
                'fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>\n'
                '            <text x="90" y="24" font-size="12" '
                'font-weight="800" fill="#1e40af" '
                'text-anchor="middle">=COUNT(A1:A10)</text>\n'
                '            <text x="15" y="55" font-size="10.5" '
                'font-weight="700" fill="#0f172a">Counts NUMBERS only</text>\n'
                '            <text x="15" y="80" font-size="10.5" '
                'font-weight="700" fill="#475569">Ignores names and '
                'text</text>\n'
                '            <rect x="15" y="92" width="150" height="24" '
                'rx="4" fill="#3b82f6"/>\n'
                '            <text x="90" y="108" font-size="10.5" '
                'font-weight="800" fill="#ffffff" '
                'text-anchor="middle">Numerical tallies</text>\n'
                '          </g>\n'
                '          <g transform="translate(240, 20)">\n'
                '            <rect x="0" y="0" width="180" height="125" rx="8" '
                'fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>\n'
                '            <text x="90" y="24" font-size="12" '
                'font-weight="800" fill="#15803d" '
                'text-anchor="middle">=COUNTA(A1:A10)</text>\n'
                '            <text x="15" y="55" font-size="10.5" '
                'font-weight="700" fill="#0f172a">Counts ALL non-empty</text>\n'
                '            <text x="15" y="80" font-size="10.5" '
                'font-weight="700" fill="#475569">Counts names, codes &amp; '
                'text</text>\n'
                '            <rect x="15" y="92" width="150" height="24" '
                'rx="4" fill="#16a34a"/>\n'
                '            <text x="90" y="108" font-size="10.5" '
                'font-weight="800" fill="#ffffff" '
                'text-anchor="middle">Attendee rosters</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Spreadsheets: COUNT vs COUNTA',
    'watch_out': 'If you use COUNT on a column of patient names, the answer '
                 'will be 0!'},
  { 'answer_text': '=IF(B2>1000, "Yes", "No").',
    'challenge_prompt': "Write an IF formula for cell D2 that displays 'Yes' "
                        "if cell B2 is greater than 1000, and 'No' otherwise.",
    'dfe_code': 'DFS 2.8',
    'golden_rule': 'Text outputs in IF statements MUST be enclosed in '
                   'quotation marks ("...")!',
    'id': 'dfs-18',
    'level': 'l2',
    'level_label': 'Level 1 / 2',
    'number': 18,
    'rule_body': 'Syntax: 1. Test condition (e.g. B2>=50). 2. Value if TRUE in '
                 'quotes ("Pass"). 3. Value if FALSE in quotes ("Fail"). '
                 'Example: =IF(B2>=50, "Pass", "Fail").',
    'rule_heading': '=IF(condition, value_if_true, value_if_false)',
    'strand_name': 'Creating Content',
    'strand_theme': 'orange',
    'subject': 'digital',
    'subject_label': 'Digital Skills',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" '
                'xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(60, 20)">\n'
                '            <rect x="0" y="0" width="340" height="130" rx="8" '
                'fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>\n'
                '            <text x="170" y="26" font-size="12" '
                'font-weight="900" fill="#0f172a" text-anchor="middle">IF '
                'STATEMENT LOGIC</text>\n'
                '            <rect x="20" y="45" width="300" height="32" '
                'rx="4" fill="#1e3a8a"/>\n'
                '            <text x="170" y="66" font-size="11" '
                'font-weight="900" fill="#ffffff" text-anchor="middle">=IF(C2 '
                '&gt;= 100, "Bonus", "No")</text>\n'
                '            <text x="30" y="105" font-size="10.5" '
                'font-weight="700" fill="#475569">If C2 is 100+, outputs '
                "'Bonus'; otherwise outputs 'No'</text>\n"
                '          </g>\n'
                '</svg>',
    'title': 'Spreadsheets: Simple IF Statements',
    'watch_out': "Don't forget the commas separating the three arguments."},
  { 'answer_text': 'The Filter tool (filtering the Department column by '
                   "'Finance').",
    'challenge_prompt': 'What spreadsheet tool would you use to view only '
                        "employees who work in the 'Finance' department?",
    'dfe_code': 'DFS 2.9',
    'golden_rule': 'Filtering hides rows; sorting changes their sequence!',
    'id': 'dfs-19',
    'level': 'l2',
    'level_label': 'Level 1 / 2',
    'number': 19,
    'rule_body': 'Sort: Reorders rows (A–Z alphabetical, or Largest to '
                 'Smallest numerical). Filter: Temporarily hides rows that do '
                 "not match criteria (e.g. show ONLY customers in 'Oxford').",
    'rule_heading': 'Order vs Isolate',
    'strand_name': 'Creating Content',
    'strand_theme': 'orange',
    'subject': 'digital',
    'subject_label': 'Digital Skills',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" '
                'xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(40, 20)">\n'
                '            <rect x="0" y="0" width="180" height="125" rx="8" '
                'fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>\n'
                '            <text x="90" y="24" font-size="12" '
                'font-weight="800" fill="#1e40af" text-anchor="middle">SORT '
                '(Reorder)</text>\n'
                '            <text x="15" y="55" font-size="10.5" '
                'font-weight="700" fill="#0f172a">• A to Z '
                '(Alphabetical)</text>\n'
                '            <text x="15" y="78" font-size="10.5" '
                'font-weight="700" fill="#0f172a">• High to Low '
                '(Sales)</text>\n'
                '            <text x="15" y="101" font-size="10.5" '
                'font-weight="700" fill="#0f172a">• Keeps all records '
                'visible</text>\n'
                '          </g>\n'
                '          <g transform="translate(240, 20)">\n'
                '            <rect x="0" y="0" width="180" height="125" rx="8" '
                'fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>\n'
                '            <text x="90" y="24" font-size="12" '
                'font-weight="800" fill="#15803d" text-anchor="middle">FILTER '
                '(Isolate)</text>\n'
                '            <text x="15" y="55" font-size="10.5" '
                'font-weight="700" fill="#0f172a">• Funnel icon on '
                'headers</text>\n'
                '            <text x="15" y="78" font-size="10.5" '
                'font-weight="700" fill="#0f172a">• Hides non-matching '
                'rows</text>\n'
                '            <text x="15" y="101" font-size="10.5" '
                'font-weight="700" fill="#0f172a">• e.g. Show \'London\' '
                'only</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Spreadsheets: Sorting &amp; Filtering',
    'watch_out': 'Make sure all data columns are selected before sorting, or '
                 'columns will become mismatched!'},
  { 'answer_text': 'A line chart (ideal for showing continuous trends over '
                   'time).',
    'challenge_prompt': 'Which chart type is best for showing sales figures '
                        'over 12 consecutive months?',
    'dfe_code': 'DFS 2.10',
    'golden_rule': 'Every chart must have a clear descriptive Title and '
                   'labelled X and Y axes!',
    'id': 'dfs-20',
    'level': 'l2',
    'level_label': 'Level 1 / 2',
    'number': 20,
    'rule_body': 'To score full marks on spreadsheet charts: 1. Select '
                 'category labels AND numerical data together. 2. Choose '
                 'appropriate chart type (Bar for categories, Line for '
                 'trends). 3. Add Chart Title, Axis Titles, and Legend.',
    'rule_heading': 'Titles, Axes &amp; Legends',
    'strand_name': 'Creating Content',
    'strand_theme': 'orange',
    'subject': 'digital',
    'subject_label': 'Digital Skills',
    'svg_html': """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="380" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="190" y="26" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle">CHART LABELLING CHECKLIST</text>
            <text x="25" y="55" font-size="10.5" font-weight="800" fill="#2563eb">[✓] Meaningful Chart Title at top</text>
            <text x="25" y="80" font-size="10.5" font-weight="800" fill="#2563eb">[✓] Horizontal Axis Title (e.g. Month / Department)</text>
            <text x="25" y="105" font-size="10.5" font-weight="800" fill="#2563eb">[✓] Vertical Axis Title (e.g. Revenue (£) / Patient Count)</text>
          </g>
</svg>""",
    'title': 'Spreadsheets: Creating Charts',
    'watch_out': "Don't include the 'Total' row when highlighting data for a "
                 'pie chart — it distorts the slices.'},
  { 'answer_text': '1. Using bullet points instead of dense paragraphs. 2. '
                   'Maintaining high contrast between text and background.',
    'challenge_prompt': 'State two design principles that make a presentation '
                        'slide easy for an audience to read.',
    'dfe_code': 'DFS 2.11',
    'golden_rule': 'Slides are visual prompts for the speaker, not essays to '
                   'read aloud!',
    'id': 'dfs-21',
    'level': 'l2',
    'level_label': 'Level 1 / 2',
    'number': 21,
    'rule_body': 'Best practice: 6 × 6 Rule: Maximum 6 bullet points per '
                 'slide, with 6 words per bullet. Use consistent Slide Master '
                 'layouts, high-contrast fonts (dark on light), and avoid '
                 'distracting animations.',
    'rule_heading': 'The 6 × 6 Rule &amp; Slide Masters',
    'strand_name': 'Creating Content',
    'strand_theme': 'orange',
    'subject': 'digital',
    'subject_label': 'Digital Skills',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" '
                'xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(60, 20)">\n'
                '            <rect x="0" y="0" width="340" height="130" rx="8" '
                'fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>\n'
                '            <text x="170" y="26" font-size="12" '
                'font-weight="900" fill="#1e40af" text-anchor="middle">SLIDE '
                'PRESENTATION RULES</text>\n'
                '            <text x="30" y="55" font-size="11" '
                'font-weight="800" fill="#0f172a">• 6 × 6 Rule: Avoid dense '
                'walls of text</text>\n'
                '            <text x="30" y="80" font-size="11" '
                'font-weight="800" fill="#0f172a">• High-contrast colours for '
                'legibility</text>\n'
                '            <text x="30" y="105" font-size="11" '
                'font-weight="800" fill="#059669">• Consistent corporate theme '
                'across all slides</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Presentations: Slide Design',
    'watch_out': "Don't use low-contrast text (e.g. yellow font on white "
                 'background).'},
  { 'answer_text': 'In the Speaker Notes pane (using Presenter View).',
    'challenge_prompt': 'Where should a presenter put detailed talking points '
                        'that they do not want the audience to see on the main '
                        'screen?',
    'dfe_code': 'DFS 2.12',
    'golden_rule': 'Put detailed speech text in the Speaker Notes, NOT on the '
                   'slide itself!',
    'id': 'dfs-22',
    'level': 'l2',
    'level_label': 'Level 1 / 2',
    'number': 22,
    'rule_body': 'Speaker Notes Pane: Area underneath each slide where the '
                 "presenter writes their talking script. In 'Presenter View', "
                 "notes are visible on the speaker's laptop screen while the "
                 'audience only sees the slides.',
    'rule_heading': 'Visible to Speaker Only',
    'strand_name': 'Creating Content',
    'strand_theme': 'orange',
    'subject': 'digital',
    'subject_label': 'Digital Skills',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" '
                'xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(60, 20)">\n'
                '            <rect x="0" y="0" width="340" height="130" rx="8" '
                'fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>\n'
                '            <rect x="40" y="15" width="260" height="55" '
                'rx="4" fill="#ffffff" stroke="#94a3b8"/>\n'
                '            <text x="170" y="45" font-size="11" '
                'font-weight="800" fill="#0f172a" '
                'text-anchor="middle">Projector View: Audience sees this '
                'slide</text>\n'
                '            <rect x="40" y="78" width="260" height="40" '
                'rx="4" fill="#fef3c7" stroke="#d97706"/>\n'
                '            <text x="170" y="102" font-size="10.5" '
                'font-weight="800" fill="#b45309" text-anchor="middle">Speaker '
                'Notes: Only visible to presenter on laptop</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Presentations: Speaker Notes',
    'watch_out': "Make sure your display is set to 'Extend' rather than "
                 "'Duplicate' to use Presenter View."},
  { 'answer_text': 'Track Changes.',
    'challenge_prompt': 'What tool allows multiple team members to review a '
                        'Word document and propose text edits without '
                        'overwriting the original text?',
    'dfe_code': 'DFS 2.13',
    'golden_rule': 'Always accept or reject all tracked changes before sending '
                   'documents to clients!',
    'id': 'dfs-23',
    'level': 'l2',
    'level_label': 'Level 1 / 2',
    'number': 23,
    'rule_body': 'Track Changes records every edit (strikethroughs, insertions '
                 'in coloured ink). Other reviewers can: 1. Add Comments to '
                 "discuss points. 2. 'Accept' or 'Reject' individual changes "
                 'before finalizing.',
    'rule_heading': 'Comments &amp; Suggesting Edits',
    'strand_name': 'Creating Content',
    'strand_theme': 'orange',
    'subject': 'digital',
    'subject_label': 'Digital Skills',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" '
                'xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(60, 20)">\n'
                '            <rect x="0" y="0" width="340" height="130" rx="8" '
                'fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.8"/>\n'
                '            <text x="170" y="26" font-size="12" '
                'font-weight="900" fill="#5b21b6" text-anchor="middle">REVIEW '
                '&amp; COLLABORATION</text>\n'
                '            <text x="30" y="55" font-size="11" '
                'font-weight="700" fill="#dc2626"><tspan '
                'text-decoration="line-through">The project will end in '
                'June.</tspan></text>\n'
                '            <text x="30" y="78" font-size="11" '
                'font-weight="800" fill="#059669">The project will conclude in '
                'August. (Inserted)</text>\n'
                '            <text x="30" y="105" font-size="10.5" '
                'font-weight="800" fill="#7c3aed">Review buttons: [✓ Accept]  '
                '[✗ Reject]</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Collaboration: Track Changes',
    'watch_out': 'Leaving tracked changes active can leak internal '
                 'confidential comments.'},
  { 'answer_text': '1. Formatting, fonts, and layout remain fixed across all '
                   'devices. 2. The recipient cannot easily edit or corrupt '
                   'the text.',
    'challenge_prompt': 'Give two reasons why job applications require CVs to '
                        'be submitted as PDF files.',
    'dfe_code': 'DFS 2.14',
    'golden_rule': 'Save as PDF to lock your formatting before printing or '
                   'emailing!',
    'id': 'dfs-24',
    'level': 'l2',
    'level_label': 'Level 1 / 2',
    'number': 24,
    'rule_body': 'Why export to PDF: 1. Universal compatibility (opens on any '
                 'phone/PC without needing Word). 2. Preserves exact layout, '
                 'fonts, and images. 3. Prevents accidental editing. 4. '
                 'Smaller file size.',
    'rule_heading': 'File → Export → Create PDF',
    'strand_name': 'Creating Content',
    'strand_theme': 'orange',
    'subject': 'digital',
    'subject_label': 'Digital Skills',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" '
                'xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(60, 20)">\n'
                '            <rect x="0" y="0" width="340" height="130" rx="8" '
                'fill="#fef2f2" stroke="#dc2626" stroke-width="1.8"/>\n'
                '            <text x="170" y="26" font-size="12" '
                'font-weight="900" fill="#991b1b" text-anchor="middle">WHY '
                'CONVERT TO PDF?</text>\n'
                '            <text x="30" y="55" font-size="11" '
                'font-weight="800" fill="#0f172a">✓ Formatting is locked and '
                'preserved</text>\n'
                '            <text x="30" y="80" font-size="11" '
                'font-weight="800" fill="#0f172a">✓ Opens on any device '
                'without Microsoft Office</text>\n'
                '            <text x="30" y="105" font-size="11" '
                'font-weight="800" fill="#059669">✓ Ideal format for invoices, '
                'certificates &amp; CVs</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Exporting &amp; Converting to PDF',
    'watch_out': 'Always keep your original .docx or .xlsx master file in case '
                 'you need to edit later.'}]
for card in CARDS:
    ET.fromstring(card["svg_html"])
