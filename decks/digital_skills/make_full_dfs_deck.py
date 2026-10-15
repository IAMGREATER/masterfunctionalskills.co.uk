#!/usr/bin/env python3
"""
Full Builder for Deck 5: Digital Functional Skills (Cards 1-50)
Covers all 5 National DFSQ Standards.
"""
import os
import pprint
import xml.etree.ElementTree as ET

def wrap_svg(inner_content, height=170):
    svg = f'<svg viewBox="0 0 460 {height}" width="100%" height="{height}" xmlns="http://www.w3.org/2000/svg">\n{inner_content}\n</svg>'
    ET.fromstring(svg)
    return svg

# Import Area 1
from build_complete_dfs import CARDS_1

CARDS_2 = [
    # 11. Word Processing: Headings & Styles
    {
        "id": "dfs-11",
        "number": 11,
        "title": "Word Processing: Headings &amp; Styles",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Creating Content",
        "strand_theme": "orange",
        "dfe_code": "DFS 2.1",
        "rule_heading": "H1, H2 &amp; Consistent Hierarchy",
        "rule_body": "Use built-in Heading Styles (Heading 1 for main titles, Heading 2 for subheadings) instead of manually bolding and enlarging text. This creates an automatic table of contents and screen-reader structure.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#1e40af" text-anchor="middle">BUILT-IN HEADING STYLES</text>
            <text x="30" y="55" font-size="13" font-weight="900" fill="#1e3a8a">Heading 1: Major Document Title</text>
            <text x="30" y="80" font-size="11" font-weight="800" fill="#2563eb">Heading 2: Section Subheading</text>
            <text x="30" y="105" font-size="10.5" font-weight="700" fill="#475569">Normal: Body text with 1.15 line spacing</text>
          </g>"""),
        "golden_rule": "Heading styles automatically build clickable navigation panes in long documents!",
        "watch_out": "Don't press Enter multiple times to create a new page — use Page Break (Ctrl + Enter).",
        "challenge_prompt": "What keyboard shortcut inserts a new page break instantly in Microsoft Word or Google Docs?",
        "answer_text": "Ctrl + Enter."
    },

    # 12. Word Processing: Lists & Tables
    {
        "id": "dfs-12",
        "number": 12,
        "title": "Word Processing: Tables &amp; Lists",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Creating Content",
        "strand_theme": "orange",
        "dfe_code": "DFS 2.2",
        "rule_heading": "Organising Information into Columns",
        "rule_body": "Tables: Insert rows and columns to align comparative data neatly. Merge cells to create spanning banner headers. Set header rows to repeat across page breaks.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <rect x="20" y="20" width="300" height="25" fill="#1e3a8a"/>
            <text x="170" y="37" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">Merged Header Cell</text>
            <line x1="20" y1="45" x2="320" y2="45" stroke="#cbd5e1"/>
            <line x1="170" y1="45" x2="170" y2="115" stroke="#cbd5e1"/>
            <text x="95" y="75" font-size="11" font-weight="700" fill="#0f172a" text-anchor="middle">Column A</text>
            <text x="245" y="75" font-size="11" font-weight="700" fill="#0f172a" text-anchor="middle">Column B</text>
          </g>"""),
        "golden_rule": "Use tables to align numbers and facts rather than pressing the Spacebar or Tab key!",
        "watch_out": "Never align text by tapping the spacebar repeatedly — it falls out of alignment on other screens.",
        "challenge_prompt": "What table feature combines two or more adjacent cells into a single large cell?",
        "answer_text": "Merge Cells."
    },

    # 13. Word Processing: Images & Text Wrapping
    {
        "id": "dfs-13",
        "number": 13,
        "title": "Images &amp; Text Wrapping",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Creating Content",
        "strand_theme": "orange",
        "dfe_code": "DFS 2.3",
        "rule_heading": "Square, Tight &amp; Aspect Ratio",
        "rule_body": "Always resize images using CORNER handles to maintain original aspect ratio (prevent squishing). Text Wrapping: 'Square' or 'Tight' wraps text smoothly around the picture. Always add Alt Text for accessibility.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <rect x="25" y="30" width="75" height="70" fill="#bae6fd" stroke="#0284c7" rx="4"/>
            <text x="62" y="70" font-size="10" font-weight="800" fill="#0369a1" text-anchor="middle">IMAGE</text>
            <g transform="translate(120, 35)">
              <text x="0" y="15" font-size="10.5" font-weight="700" fill="#0f172a">Text wraps neatly around</text>
              <text x="0" y="35" font-size="10.5" font-weight="700" fill="#0f172a">the image without strange</text>
              <text x="0" y="55" font-size="10.5" font-weight="700" fill="#0f172a">blank gaps on the page.</text>
              <text x="0" y="75" font-size="10" font-weight="800" fill="#16a34a">Wrapping: Square</text>
            </g>
          </g>"""),
        "golden_rule": "Drag from corner handles only — never drag side handles or you will distort the image!",
        "watch_out": "Adding Alt Text to graphics is a legal accessibility requirement under UK web standards.",
        "challenge_prompt": "Why should you provide Alt Text (alternative text) when inserting an image into a document or website?",
        "answer_text": "Alt Text allows screen readers to describe the image to visually impaired users."
    },

    # 14. Spreadsheets: Anatomy
    {
        "id": "dfs-14",
        "number": 14,
        "title": "Spreadsheets: Anatomy of a Sheet",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Creating Content",
        "strand_theme": "orange",
        "dfe_code": "DFS 2.4",
        "rule_heading": "Columns, Rows &amp; Cell References",
        "rule_body": "Columns: Lettered vertically (A, B, C...). Rows: Numbered horizontally (1, 2, 3...). Cell Reference: The intersection letter + number (e.g. B4 = column B, row 4). Format cells as Currency (£), Percentage (%), or Date.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <rect x="20" y="20" width="40" height="25" fill="#e2e8f0"/>
            <rect x="60" y="20" width="80" height="25" fill="#e2e8f0"/><text x="100" y="37" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle">A</text>
            <rect x="140" y="20" width="80" height="25" fill="#3b82f6"/><text x="180" y="37" font-size="11" font-weight="900" fill="#ffffff" text-anchor="middle">B</text>
            <rect x="220" y="20" width="80" height="25" fill="#e2e8f0"/><text x="260" y="37" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle">C</text>
            <rect x="20" y="45" width="40" height="25" fill="#e2e8f0"/><text x="40" y="62" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle">1</text>
            <rect x="20" y="70" width="40" height="25" fill="#3b82f6"/><text x="40" y="87" font-size="11" font-weight="900" fill="#ffffff" text-anchor="middle">2</text>
            <rect x="140" y="70" width="80" height="25" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
            <text x="180" y="87" font-size="11" font-weight="900" fill="#1e40af" text-anchor="middle">B2 ★</text>
          </g>"""),
        "golden_rule": "Column Letter ALWAYS comes before the Row Number (e.g. C5, NEVER 5C)!",
        "watch_out": "Format raw numbers as Currency (£) so the pound sign appears automatically.",
        "challenge_prompt": "What cell reference is located at the intersection of column D and row 14?",
        "answer_text": "D14."
    },

    # 15. Spreadsheet Formulas: Basic Arithmetic
    {
        "id": "dfs-15",
        "number": 15,
        "title": "Spreadsheets: Basic Arithmetic",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Creating Content",
        "strand_theme": "orange",
        "dfe_code": "DFS 2.5",
        "rule_heading": "Always Start with an Equals Sign (=)",
        "rule_body": "Every formula in Excel / Google Sheets MUST begin with '=': Add: =A1+B1. Subtract: =A1-B1. Multiply: =A1*B1 (asterisk). Divide: =A1/B1 (forward slash). Never type hardcoded numbers into formulas.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#15803d" text-anchor="middle">SPREADSHEET OPERATORS</text>
            <text x="30" y="55" font-size="11.5" font-weight="800" fill="#0f172a">Addition: =B2 + C2</text>
            <text x="30" y="78" font-size="11.5" font-weight="800" fill="#0f172a">Subtraction: =B2 - C2</text>
            <text x="30" y="101" font-size="11.5" font-weight="800" fill="#2563eb">Multiplication: =B2 * C2  (Asterisk *)</text>
            <text x="30" y="122" font-size="11.5" font-weight="800" fill="#dc2626">Division: =B2 / C2  (Slash /)</text>
          </g>"""),
        "golden_rule": "Always use cell references (e.g. =A2*B2) so formulas recalculate when numbers change!",
        "watch_out": "Typing 'A1+B1' without an equals sign will just display the letters as plain text.",
        "challenge_prompt": "Write the formula to multiply the quantity in cell B4 by the unit price in cell C4.",
        "answer_text": "=B4*C4."
    },

    # 16. Spreadsheet Functions: SUM, AVERAGE, MIN, MAX
    {
        "id": "dfs-16",
        "number": 16,
        "title": "Spreadsheets: SUM &amp; AVERAGE",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Creating Content",
        "strand_theme": "orange",
        "dfe_code": "DFS 2.6",
        "rule_heading": "Ranges with Colons (e.g. B2:B10)",
        "rule_body": "=SUM(B2:B10): Adds all numbers in range. =AVERAGE(B2:B10): Calculates mean. =MAX(B2:B10): Finds highest value. =MIN(B2:B10): Finds lowest value. Colon (:) means 'through to'.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#1e40af" text-anchor="middle">CORE EXCEL FUNCTIONS</text>
            <text x="30" y="55" font-size="11" font-weight="800" fill="#0f172a">• =SUM(C2:C20)  →  Total of all 19 cells</text>
            <text x="30" y="80" font-size="11" font-weight="800" fill="#0f172a">• =AVERAGE(C2:C20)  →  Mean average score</text>
            <text x="30" y="105" font-size="11" font-weight="800" fill="#059669">• =MAX(C2:C20)  •  =MIN(C2:C20)</text>
          </g>"""),
        "golden_rule": "The colon (:) indicates a contiguous cell range from start to finish!",
        "watch_out": "Don't write '=SUM(A1+A2)' — either write '=SUM(A1:A2)' or '=A1+A2'.",
        "challenge_prompt": "Write the function to calculate the average of sales in cells D3 to D15.",
        "answer_text": "=AVERAGE(D3:D15)."
    },

    # 17. Spreadsheet Functions: COUNT & COUNTA
    {
        "id": "dfs-17",
        "number": 17,
        "title": "Spreadsheets: COUNT vs COUNTA",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Creating Content",
        "strand_theme": "orange",
        "dfe_code": "DFS 2.7",
        "rule_heading": "Count Numbers vs Count Non-Empty Cells",
        "rule_body": "=COUNT(range): Counts ONLY cells containing NUMBERS. =COUNTA(range): Counts ALL non-empty cells (numbers, text, symbols). Think 'Count All' (COUNTA).",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="90" y="24" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">=COUNT(A1:A10)</text>
            <text x="15" y="55" font-size="10.5" font-weight="700" fill="#0f172a">Counts NUMBERS only</text>
            <text x="15" y="80" font-size="10.5" font-weight="700" fill="#475569">Ignores names and text</text>
            <rect x="15" y="92" width="150" height="24" rx="4" fill="#3b82f6"/>
            <text x="90" y="108" font-size="10.5" font-weight="800" fill="#ffffff" text-anchor="middle">Numerical tallies</text>
          </g>
          <g transform="translate(240, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
            <text x="90" y="24" font-size="12" font-weight="800" fill="#15803d" text-anchor="middle">=COUNTA(A1:A10)</text>
            <text x="15" y="55" font-size="10.5" font-weight="700" fill="#0f172a">Counts ALL non-empty</text>
            <text x="15" y="80" font-size="10.5" font-weight="700" fill="#475569">Counts names, codes &amp; text</text>
            <rect x="15" y="92" width="150" height="24" rx="4" fill="#16a34a"/>
            <text x="90" y="108" font-size="10.5" font-weight="800" fill="#ffffff" text-anchor="middle">Attendee rosters</text>
          </g>"""),
        "golden_rule": "Use COUNTA to count attendee names or text entries!",
        "watch_out": "If you use COUNT on a column of patient names, the answer will be 0!",
        "challenge_prompt": "Which function should you use to count how many employees signed in on a text attendance sheet in cells B2 to B30?",
        "answer_text": "=COUNTA(B2:B30)."
    },

    # 18. Spreadsheet Logic: Simple IF Statements
    {
        "id": "dfs-18",
        "number": 18,
        "title": "Spreadsheets: Simple IF Statements",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Creating Content",
        "strand_theme": "orange",
        "dfe_code": "DFS 2.8",
        "rule_heading": "=IF(condition, value_if_true, value_if_false)",
        "rule_body": "Syntax: 1. Test condition (e.g. B2>=50). 2. Value if TRUE in quotes (\"Pass\"). 3. Value if FALSE in quotes (\"Fail\"). Example: =IF(B2>=50, \"Pass\", \"Fail\").",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle">IF STATEMENT LOGIC</text>
            <rect x="20" y="45" width="300" height="32" rx="4" fill="#1e3a8a"/>
            <text x="170" y="66" font-size="11" font-weight="900" fill="#ffffff" text-anchor="middle">=IF(C2 &gt;= 100, "Bonus", "No")</text>
            <text x="30" y="105" font-size="10.5" font-weight="700" fill="#475569">If C2 is 100+, outputs 'Bonus'; otherwise outputs 'No'</text>
          </g>"""),
        "golden_rule": "Text outputs in IF statements MUST be enclosed in quotation marks (\"...\")!",
        "watch_out": "Don't forget the commas separating the three arguments.",
        "challenge_prompt": "Write an IF formula for cell D2 that displays 'Yes' if cell B2 is greater than 1000, and 'No' otherwise.",
        "answer_text": "=IF(B2>1000, \"Yes\", \"No\")."
    },

    # 19. Spreadsheets: Sorting & Filtering
    {
        "id": "dfs-19",
        "number": 19,
        "title": "Spreadsheets: Sorting &amp; Filtering",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Creating Content",
        "strand_theme": "orange",
        "dfe_code": "DFS 2.9",
        "rule_heading": "Order vs Isolate",
        "rule_body": "Sort: Reorders rows (A–Z alphabetical, or Largest to Smallest numerical). Filter: Temporarily hides rows that do not match criteria (e.g. show ONLY customers in 'Oxford').",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="90" y="24" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">SORT (Reorder)</text>
            <text x="15" y="55" font-size="10.5" font-weight="700" fill="#0f172a">• A to Z (Alphabetical)</text>
            <text x="15" y="78" font-size="10.5" font-weight="700" fill="#0f172a">• High to Low (Sales)</text>
            <text x="15" y="101" font-size="10.5" font-weight="700" fill="#0f172a">• Keeps all records visible</text>
          </g>
          <g transform="translate(240, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
            <text x="90" y="24" font-size="12" font-weight="800" fill="#15803d" text-anchor="middle">FILTER (Isolate)</text>
            <text x="15" y="55" font-size="10.5" font-weight="700" fill="#0f172a">• Funnel icon on headers</text>
            <text x="15" y="78" font-size="10.5" font-weight="700" fill="#0f172a">• Hides non-matching rows</text>
            <text x="15" y="101" font-size="10.5" font-weight="700" fill="#0f172a">• e.g. Show 'London' only</text>
          </g>"""),
        "golden_rule": "Filtering hides rows; sorting changes their sequence!",
        "watch_out": "Make sure all data columns are selected before sorting, or columns will become mismatched!",
        "challenge_prompt": "What spreadsheet tool would you use to view only employees who work in the 'Finance' department?",
        "answer_text": "The Filter tool (filtering the Department column by 'Finance')."
    },

    # 20. Spreadsheet Charts: Selection & Labelling
    {
        "id": "dfs-20",
        "number": 20,
        "title": "Spreadsheets: Creating Charts",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Creating Content",
        "strand_theme": "orange",
        "dfe_code": "DFS 2.10",
        "rule_heading": "Titles, Axes &amp; Legends",
        "rule_body": "To score full marks on spreadsheet charts: 1. Select category labels AND numerical data together. 2. Choose appropriate chart type (Bar for categories, Line for trends). 3. Add Chart Title, Axis Titles, and Legend.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle">CHART LABELLING CHECKLIST</text>
            <text x="30" y="55" font-size="11" font-weight="800" fill="#2563eb">[✓] Meaningful Chart Title at top</text>
            <text x="30" y="80" font-size="11" font-weight="800" fill="#2563eb">[✓] Horizontal Axis Title (e.g. Month / Department)</text>
            <text x="30" y="105" font-size="11" font-weight="800" fill="#2563eb">[✓] Vertical Axis Title (e.g. Revenue (£) / Patient Count)</text>
          </g>"""),
        "golden_rule": "Every chart must have a clear descriptive Title and labelled X and Y axes!",
        "watch_out": "Don't include the 'Total' row when highlighting data for a pie chart — it distorts the slices.",
        "challenge_prompt": "Which chart type is best for showing sales figures over 12 consecutive months?",
        "answer_text": "A line chart (ideal for showing continuous trends over time)."
    },

    # 21. Presentations: Consistent Slide Design
    {
        "id": "dfs-21",
        "number": 21,
        "title": "Presentations: Slide Design",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Creating Content",
        "strand_theme": "orange",
        "dfe_code": "DFS 2.11",
        "rule_heading": "The 6 × 6 Rule &amp; Slide Masters",
        "rule_body": "Best practice: 6 × 6 Rule: Maximum 6 bullet points per slide, with 6 words per bullet. Use consistent Slide Master layouts, high-contrast fonts (dark on light), and avoid distracting animations.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#1e40af" text-anchor="middle">SLIDE PRESENTATION RULES</text>
            <text x="30" y="55" font-size="11" font-weight="800" fill="#0f172a">• 6 × 6 Rule: Avoid dense walls of text</text>
            <text x="30" y="80" font-size="11" font-weight="800" fill="#0f172a">• High-contrast colours for legibility</text>
            <text x="30" y="105" font-size="11" font-weight="800" fill="#059669">• Consistent corporate theme across all slides</text>
          </g>"""),
        "golden_rule": "Slides are visual prompts for the speaker, not essays to read aloud!",
        "watch_out": "Don't use low-contrast text (e.g. yellow font on white background).",
        "challenge_prompt": "State two design principles that make a presentation slide easy for an audience to read.",
        "answer_text": "1. Using bullet points instead of dense paragraphs. 2. Maintaining high contrast between text and background."
    },

    # 22. Presentations: Presenter Notes
    {
        "id": "dfs-22",
        "number": 22,
        "title": "Presentations: Speaker Notes",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Creating Content",
        "strand_theme": "orange",
        "dfe_code": "DFS 2.12",
        "rule_heading": "Visible to Speaker Only",
        "rule_body": "Speaker Notes Pane: Area underneath each slide where the presenter writes their talking script. In 'Presenter View', notes are visible on the speaker's laptop screen while the audience only sees the slides.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <rect x="40" y="15" width="260" height="55" rx="4" fill="#ffffff" stroke="#94a3b8"/>
            <text x="170" y="45" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle">Projector View: Audience sees this slide</text>
            <rect x="40" y="78" width="260" height="40" rx="4" fill="#fef3c7" stroke="#d97706"/>
            <text x="170" y="102" font-size="10.5" font-weight="800" fill="#b45309" text-anchor="middle">Speaker Notes: Only visible to presenter on laptop</text>
          </g>"""),
        "golden_rule": "Put detailed speech text in the Speaker Notes, NOT on the slide itself!",
        "watch_out": "Make sure your display is set to 'Extend' rather than 'Duplicate' to use Presenter View.",
        "challenge_prompt": "Where should a presenter put detailed talking points that they do not want the audience to see on the main screen?",
        "answer_text": "In the Speaker Notes pane (using Presenter View)."
    },

    # 23. Digital Collaboration: Track Changes
    {
        "id": "dfs-23",
        "number": 23,
        "title": "Collaboration: Track Changes",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Creating Content",
        "strand_theme": "orange",
        "dfe_code": "DFS 2.13",
        "rule_heading": "Comments &amp; Suggesting Edits",
        "rule_body": "Track Changes records every edit (strikethroughs, insertions in coloured ink). Other reviewers can: 1. Add Comments to discuss points. 2. 'Accept' or 'Reject' individual changes before finalizing.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#5b21b6" text-anchor="middle">REVIEW &amp; COLLABORATION</text>
            <text x="30" y="55" font-size="11" font-weight="700" fill="#dc2626"><tspan text-decoration="line-through">The project will end in June.</tspan></text>
            <text x="30" y="78" font-size="11" font-weight="800" fill="#059669">The project will conclude in August. (Inserted)</text>
            <text x="30" y="105" font-size="10.5" font-weight="800" fill="#7c3aed">Review buttons: [✓ Accept]  [✗ Reject]</text>
          </g>"""),
        "golden_rule": "Always accept or reject all tracked changes before sending documents to clients!",
        "watch_out": "Leaving tracked changes active can leak internal confidential comments.",
        "challenge_prompt": "What tool allows multiple team members to review a Word document and propose text edits without overwriting the original text?",
        "answer_text": "Track Changes."
    },

    # 24. Exporting to PDF
    {
        "id": "dfs-24",
        "number": 24,
        "title": "Exporting &amp; Converting to PDF",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Creating Content",
        "strand_theme": "orange",
        "dfe_code": "DFS 2.14",
        "rule_heading": "File → Export → Create PDF",
        "rule_body": "Why export to PDF: 1. Universal compatibility (opens on any phone/PC without needing Word). 2. Preserves exact layout, fonts, and images. 3. Prevents accidental editing. 4. Smaller file size.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#fef2f2" stroke="#dc2626" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#991b1b" text-anchor="middle">WHY CONVERT TO PDF?</text>
            <text x="30" y="55" font-size="11" font-weight="800" fill="#0f172a">✓ Formatting is locked and preserved</text>
            <text x="30" y="80" font-size="11" font-weight="800" fill="#0f172a">✓ Opens on any device without Microsoft Office</text>
            <text x="30" y="105" font-size="11" font-weight="800" fill="#059669">✓ Ideal format for invoices, certificates &amp; CVs</text>
          </g>"""),
        "golden_rule": "Save as PDF to lock your formatting before printing or emailing!",
        "watch_out": "Always keep your original .docx or .xlsx master file in case you need to edit later.",
        "challenge_prompt": "Give two reasons why job applications require CVs to be submitted as PDF files.",
        "answer_text": "1. Formatting, fonts, and layout remain fixed across all devices. 2. The recipient cannot easily edit or corrupt the text."
    }
]

print(f"Validated DFS Area 2: {len(CARDS_2)} cards")
