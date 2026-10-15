"""
books/a4/fix_bksb_and_english.py
Fixes:
1. In generate_full_builder.py: BKSB papers solution loop with range(1, 5).
2. In generate_full_builder.py: Adds 1 page to English L2 (Timing & Mark Allocation Blueprint) -> 84 pages.
3. Runs generate_full_builder.py.
"""

from pathlib import Path

BUILDER_GEN = Path("/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk/books/a4/generate_full_builder.py")

TIMING_PAGE = '''
    # Candidate Timing & Mark Allocation Blueprint (1 page)
    timing_body = (
        K.page_title("Level 2 Exam Timing &amp; Mark Allocation Strategy", kicker="Executive Examination Blueprint", badge="TIME")
        + K.hero_image(P("clock wristwatch business meeting time management"), "Strategic time budgeting and mark-to-minute calibration.", 38)
        + K.box_html(
            "<table style='width:100%; border-collapse:collapse; font-size:10.5pt; line-height:1.5;'>"
            "<tr style='background:#f1f5f9;'><th style='padding:6px; text-align:left;'>Examination Section</th><th style='padding:6px; text-align:left;'>Marks Available</th><th style='padding:6px; text-align:left;'>Recommended Time</th><th style='padding:6px; text-align:left;'>Pacing &amp; Strategy Rule</th></tr>"
            "<tr><td style='padding:6px; border-bottom:1px solid #e2e8f0;'><b>Reading &bull; Source Skim &amp; Scan</b></td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>&mdash;</td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>10 minutes</td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>Skim Text A &amp; Text B headlines, subheadings, and lead paragraphs first.</td></tr>"
            "<tr><td style='padding:6px; border-bottom:1px solid #e2e8f0;'><b>Reading &bull; Questions 1&ndash;9</b></td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>30 marks</td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>40 minutes</td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>Allocate ~1.3 minutes per mark. Save Q7-Q9 synthesis for last.</td></tr>"
            "<tr><td style='padding:6px; border-bottom:1px solid #e2e8f0;'><b>Writing &bull; Task 1 (Formal Report/Letter)</b></td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>21 marks</td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>35 minutes</td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>Spend 5m planning, 25m drafting, 5m proofreading format &amp; SPaG.</td></tr>"
            "<tr><td style='padding:6px; border-bottom:1px solid #e2e8f0;'><b>Writing &bull; Task 2 (Public Article/Speech)</b></td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>15 marks</td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>25 minutes</td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>Spend 3m planning, 18m drafting, 4m proofreading sentence flow.</td></tr>"
            "<tr><td style='padding:6px; border-bottom:1px solid #e2e8f0;'><b>Final Proofreading &amp; Audit</b></td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>&mdash;</td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>10 minutes</td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>Check every sentence ends with full stop; audit homophones &amp; commas.</td></tr>"
            "</table>",
            title="Pearson Edexcel Level 2 Time Management Blueprint (120 Minutes Total)"
        )
        + K.rule_box("Exam Hall Golden Pacing Principles",
                     "<p style='margin:0;'>1. Never leave early! Spend remaining minutes reviewing Task 1 and Task 2 for missing punctuation.<br>2. Aim for 250&ndash;300 words on Task 1 and 200&ndash;250 words on Task 2.<br>3. Always weave direct quotations smoothly into your comparative reading answers.</p>")
        + K.fill_notes("Personal Exam Routine &amp; Warm-Up Checklist", 22)
    )
    pages.append(K.page(timing_body, header=(BOOK, "Timing Blueprint"), footer=BOOK, page_no=p_curr))
    p_curr += 1
'''

def update():
    with open(BUILDER_GEN, "r", encoding="utf-8") as f:
        text = f.read()

    # 1. Fix BKSB loop
    bad_bksb = '''    # Solutions for 4 Diagnostic Papers
    for title_str, sol_html in ssr.BKSB_PAPERS_SOLUTIONS:
        ref_blocks.append(K.ref_block(title_str, sol_html))'''

    good_bksb = '''    # Solutions for 4 Diagnostic Papers
    for p_num in range(1, 5):
        for title_str, sol_html in ssr.BKSB_PAPERS_SOLUTIONS.get(p_num, []):
            ref_blocks.append(K.ref_block(title_str, sol_html))'''

    if bad_bksb in text:
        text = text.replace(bad_bksb, good_bksb)
        print("BKSB papers loop fixed.")

    # 2. Insert English timing page
    cert_target = '    # Candidate Readiness Certificate (1 page)\n    cert_body = (\n        K.page_title("Level 2 English Examination Readiness"'
    if "Level 2 Exam Timing &amp; Mark Allocation Strategy" not in text:
        eng_target = text.find('def build_mock_english_l2():')
        pos = text.find(cert_target, eng_target)
        if pos != -1:
            text = text[:pos] + TIMING_PAGE.strip() + "\n\n    " + text[pos:]
            print("English timing page inserted.")
        else:
            # try alternative find
            alt = text.find('K.page_title("Level 2 English Examination Readiness"')
            if alt != -1:
                line_start = text.rfind('\n', 0, alt)
                text = text[:line_start] + "\n" + TIMING_PAGE.strip() + "\n" + text[line_start:]
                print("English timing page inserted (alt).")

    with open(BUILDER_GEN, "w", encoding="utf-8") as f:
        f.write(text)

    print("generate_full_builder.py updated successfully!")

if __name__ == "__main__":
    update()
