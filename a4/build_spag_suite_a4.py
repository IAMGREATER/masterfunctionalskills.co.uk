from html import escape as escape_html
#!/usr/bin/env python3
"""
books/a4/build_spag_suite_a4.py
=============================================================================
Compiles all 3 Master Functional Skills SPaG publications in the new A4
"Fill the Page" design (13pt/14pt typography, real photos, Murphy cartoons,
and zero wasted bottom space):

1. MasterFunctionalSkills_SPaG_Level_2_Mastery.pdf       (100 Pages)
2. MasterFunctionalSkills_SPaG_Level_1_Mastery.pdf       (100 Pages)
3. MasterFunctionalSkills_SPaG_Entry_Level_3_Mastery.pdf (96 Pages)

Outputs to:
- assets/downloads/
- ~/Documents/
=============================================================================
"""

import os
import sys
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJECT_DIR = HERE.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(PROJECT_DIR / "books" / "spag"))

import a4_kit as K
import spag_data_l2
import spag_data_l1
import spag_l2_84p_units_1_13 as u_l2_p1
import spag_l2_84p_units_14_26 as u_l2_p2
import spag_l2_84p_diag_vocab as dv_l2
import spag_l2_84p_mocks_keys as mk_l2

import spag_l1_84p_units as u_l1
import spag_l1_84p_data as d_l1

import spag_data_e3_84p as d_e3
import generate_e3_data as u_e3
import spag_data_e3_extras as x_e3
import spag_data_e3_answers as a_e3

DOWNLOADS = PROJECT_DIR / "assets" / "downloads"
DOCUMENTS = Path("/home/subi/Documents")
COV = K.COVER_DIR


# =============================================================================
# Helper: Photo lookup with cache
# =============================================================================
def get_photo(keywords, theme="spag", exclude=None):
    return K.photo(keywords, theme, exclude or set())


# =============================================================================
# 1. SPaG Level 2 Mastery (100 Pages)
# =============================================================================
def build_spag_l2():
    print("\n" + "="*70)
    print("BUILDING: MasterFunctionalSkills_SPaG_Level_2_Mastery.pdf (A4 Fill-The-Page)")
    print("="*70)

    BOOK = "SPaG Level 2 Mastery"
    front_cov = COV / "spag_l2_mastery_cover-01.png"
    back_cov = COV / "spag_l2_mastery_cover-02.png"

    all_units = u_l2_p1.UNITS_1_TO_13 + u_l2_p2.UNITS_14_TO_26
    pages = []
    used_photos = set()

    def P(kw):
        p = get_photo(kw, "spag", used_photos) or get_photo(kw, "workplace_office", used_photos) or get_photo(kw, None, used_photos)
        if p:
            used_photos.add(p)
        return p

    # p1: Front Cover
    pages.append(K.front_cover(front_cov))

    # p2: Inside Cover
    pages.append(K.inside_cover(
        "Spelling, Punctuation &amp; Grammar",
        "Level 2 &bull; The Complete 2-Page Spread Self-Study &amp; Revision Workbook",
        "SPaG Level 2",
        [
            ("1&ndash;4", "Diagnostic Assessment &amp; Skill Routing", "3"),
            ("5&ndash;56", "26 Two-Page Murphy 'Grammar in Use' Units", "7"),
            ("57&ndash;68", "6 Visual Vocabulary in Use Modules", "59"),
            ("69&ndash;80", "12 Mixed Forensic Proofreading Workouts", "71"),
            ("81&ndash;88", "4 Realistic Workplace Writing Mock Exams", "83"),
            ("89&ndash;98", "Comprehensive Explanatory Answer Keys", "91"),
            ("99", "Candidate Self-Audit &amp; Progress Matrix", "99"),
        ],
        footer=BOOK
    ))

    # p3-6: Diagnostic Assessment (4 pages, 10 authentic questions total)
    diag_qs = spag_data_l2.L2_DIAGNOSTIC["questions"]
    scoring_rows = spag_data_l2.L2_DIAGNOSTIC["scoring"]

    def make_ex_items(qs):
        items = []
        for q in qs:
            clean_opts = [o[3:] if len(o) > 3 and o[1] == ")" else o for o in q["options"]]
            pr = q.get("prompt", "")
            top = q.get("topic", "")
            items.append({
                "q": f"<b>{pr}</b> <span style='font-size:10.5pt;color:var(--muted);font-weight:400;'>({top})</span>",
                "options": clean_opts,
                "marks": 1
            })
        return items

    # Page 3: Q1-3 (3 questions)
    p3_body = (
        K.page_title("Baseline Diagnostic Assessment &bull; Part 1 of 4",
                     kicker="Diagnostic Audit &bull; Questions 1&ndash;3",
                     lead="Answer each question. Circle your chosen answer. Do not use a dictionary.")
        + K.exercise_list(make_ex_items(diag_qs[0:3]), start=1)
    )
    pages.append(K.page(p3_body, header=(BOOK, "Diagnostic 1/4"), footer=BOOK, page_no=3))

    # Page 4: Q4-6 (3 questions)
    p4_body = (
        K.page_title("Baseline Diagnostic Assessment &bull; Part 2 of 4",
                     kicker="Diagnostic Audit &bull; Questions 4&ndash;6",
                     lead="Identify the correct sentence structure, punctuation, and capitalisation.")
        + K.exercise_list(make_ex_items(diag_qs[3:6]), start=4)
    )
    pages.append(K.page(p4_body, header=(BOOK, "Diagnostic 2/4"), footer=BOOK, page_no=4))

    # Page 5: Q7-8 (2 questions) + Scoring Matrix Table
    score_table = """<div class="box" style="padding:2.5mm 3.5mm;background:#fff;border:1.5px solid var(--soft);margin-top:2mm;">
      <div style="font-weight:700;color:var(--primary);font-size:11.5pt;margin-bottom:1.5mm;">Diagnostic Performance Matrix &amp; Recommended Study Pathway</div>
      <table style="width:100%;border-collapse:collapse;font-size:10pt;">
        <thead>
          <tr style="background:var(--light);color:var(--primary);text-align:left;">
            <th style="padding:1.5mm;border:1px solid var(--soft);">Score Range</th>
            <th style="padding:1.5mm;border:1px solid var(--soft);">Readiness Level</th>
            <th style="padding:1.5mm;border:1px solid var(--soft);">Recommended Curriculum Route</th>
          </tr>
        </thead>
        <tbody>"""
    for row in scoring_rows:
        score_table += f"""
          <tr>
            <td style="padding:1.5mm;border:1px solid var(--soft);font-weight:700;">{row['range']}</td>
            <td style="padding:1.5mm;border:1px solid var(--soft);color:var(--accent);font-weight:600;">{row['status']}</td>
            <td style="padding:1.5mm;border:1px solid var(--soft);">{row['advice']}</td>
          </tr>"""
    score_table += """</tbody></table></div>"""

    p5_body = (
        K.page_title("Baseline Diagnostic Assessment &bull; Part 3 of 4",
                     kicker="Diagnostic Audit &bull; Questions 7&ndash;8",
                     lead="Grammar and syntax accuracy questions, followed by the diagnostic benchmark rubric.")
        + K.exercise_list(make_ex_items(diag_qs[6:8]), start=7)
        + score_table
    )
    pages.append(K.page(p5_body, header=(BOOK, "Diagnostic 3/4"), footer=BOOK, page_no=5))

    # Page 6: Q9-10 (2 questions) + Candidate Action Plan
    p6_body = (
        K.page_title("Baseline Diagnostic Assessment &bull; Part 4 of 4",
                     kicker="Diagnostic Audit &bull; Questions 9&ndash;10 &amp; Study Plan",
                     lead="Final vocational diagnostic questions and your personalized revision action plan.")
        + K.exercise_list(make_ex_items(diag_qs[8:10]), start=9)
        + K.tip_pair("Check your diagnostic score against the answer keys on page 91.",
                     "Prioritise the specific units flagged in questions you found challenging.",
                     golden_title="Tutor Golden Rule", watch_title="Revision Target")
        + K.fill_lines("Candidate Action Plan &amp; Priority Units to Master", min_mm=32, gap_mm=9.5)
    )
    pages.append(K.page(p6_body, header=(BOOK, "Diagnostic 4/4"), footer=BOOK, page_no=6))

    # p7-58: 26 Units (52 pages)
    characters = [
        ("Priya", "tutor woman female", "#7c3aed"),
        ("Subi", "abdul tutor man", "#0c4a6e"),
        ("Marcus", "marcus apprentice", "#0d9488"),
        ("Sarah", "sarah care nurse", "#be123c"),
        ("Sam", "sam learner thinking", "#475569"),
    ]

    p_curr = 7
    for u_idx, u in enumerate(all_units):
        u_num = u["unit"]
        char_name, char_kw, char_col = characters[u_idx % len(characters)]

        # --- Left Page: Learn ---
        anchor_title = u.get("format_link", u.get("anchor_title", "Workplace Scenario"))
        if len(anchor_title) > 90:
            anchor_title = anchor_title[:87] + "..."
        rule_title = u.get("rule_title", "Syntax Architecture &amp; Core Structural Rules")
        rule_text = K.clean_legacy(u.get("rule_text", ""))
        bad_text = u.get("worked_bad", "Example with error.")
        good_text = u.get("worked_good", "Corrected example.")
        why_text = u.get("worked_why", "Grammatical explanation.")

        font_sz = "9.5pt" if len(rule_text) > 1100 else ("10pt" if len(rule_text) > 900 else "10.5pt")
        lh = "1.2" if len(rule_text) > 1100 else ("1.25" if len(rule_text) > 900 else "1.28")
        bubble_h = 44 if len(rule_text) > 1100 else 48

        left_body = (
            K.page_title(u["title"], kicker=f"Unit {u_num} &bull; {u['strand']}", badge=u_num)
            + K.character_bubble(
                K.cartoon(char_kw), char_name,
                f"<b style='color:var(--accent)'>A &nbsp;The Concept in Practice:</b> {anchor_title}",
                "left", bubble_h, char_col
            )
            + f"""<div class="box rule" style="flex:1 0 auto;padding:2mm 3.5mm;font-size:{font_sz};line-height:{lh};">
                <div class="bt" style="margin-bottom:1mm;"><span class="ico">&#9733;</span>B &nbsp;{rule_title}</div>
                <div style="font-size:{font_sz};">{rule_text}</div>
              </div>"""
            + K.compare(
                f"<div style='font-size:10pt;line-height:1.22;'>{bad_text}</div>",
                f"<div style='font-size:10pt;line-height:1.22;'>{good_text}</div><div style='font-size:9pt;color:var(--muted);margin-top:1mm;'><b>Rule:</b> {why_text}</div>",
                stacked=False, bad_label="&#10007; Common Error", good_label="&#10003; Model Solution"
            )
        )
        pages.append(K.page(left_body, header=(BOOK, f"Unit {u_num} &bull; Learn"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # --- Right Page: Practise ---
        # Exercise A: MCQs (2 questions)
        ex_a_items = []
        for q_tuple in u.get("exercise_a", [])[:2]:
            q_text, opts = q_tuple[0], q_tuple[1]
            clean_opts = [o[3:] if len(o) > 3 and o[1] == ")" else o for o in opts]
            ex_a_items.append({"q": q_text, "options": clean_opts})

        # Exercise B: Transformation (2 questions)
        ex_b_items = []
        for b_tuple in u.get("exercise_b", [])[:2]:
            prompt_type, original = b_tuple[0], b_tuple[1]
            ex_b_items.append((f"<b>[{prompt_type}]:</b> <i>{original}</i>", 2))

        right_body = (
            K.section("A", "Tick the correct sentence")
            + K.exercise_list(ex_a_items)
            + K.section("B", "Rewrite each sentence correctly")
            + K.exercise_list(ex_b_items, start=3)
            + K.fill_lines(f"<span style='color:var(--accent)'>C &nbsp;Applied Task:</span> Write two sentences using the rules from Unit {u_num}.", min_mm=26, gap_mm=9)
        )
        pages.append(K.page(right_body, header=(BOOK, f"Unit {u_num} &bull; Practise"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p59-70: 6 Vocab in Use Modules (12 pages: 2 pages each)
    vocab_mods = dv_l2.VOCABULARY_MODULES
    for v_idx, vm in enumerate(vocab_mods):
        # Page 1: Visual Dictionary Tiles
        v_title = vm["title"]
        tiles = []
        for row in vm.get("table_rows", [])[:6]:
            pre, meaning, ex_sent = row[0], row[1], row[2]
            clean_pre = str(pre).strip()
            tiles.append((
                P("workplace office meeting business"),
                f"{clean_pre} <span style='font-size:12pt;color:var(--muted);font-weight:400;'>({meaning})</span>",
                ex_sent
            ))
        v_body_1 = (
            K.page_title(f"Vocabulary Module {v_idx+1}: {v_title}",
                         kicker="Vocabulary in Use &bull; Visual Dictionary",
                         lead="High-utility vocabulary and structural patterns for Functional Skills Level 2 writing.")
            + K.photo_grid(tiles, cols=3, fill=True, min_tile_mm=62)
        )
        pages.append(K.page(v_body_1, header=(BOOK, f"Vocab Module {v_idx+1} &bull; Dictionary"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 2: Application Drills
        drill_items = [
            (f"Write a workplace sentence demonstrating precise usage of <b>{vm['table_rows'][0][0]}</b> in a professional report.", 3),
            (f"Explain the exact nuance between <b>{vm['table_rows'][1][0]}</b> and a basic synonym in your own words.", 3),
            (f"Draft an email extract to a colleague incorporating at least two terms from Module {v_idx+1}.", 3),
        ]
        v_body_2 = (
            K.page_title(f"Module {v_idx+1} &bull; Applied Vocational Exercises",
                         kicker="Vocabulary in Use &bull; Practice Drills",
                         lead="Apply newly acquired vocabulary to authentic vocational contexts.")
            + K.exercise_list(drill_items)
            + K.fill_notes(f"Key Vocabulary Memory Box for Module {v_idx+1}", min_mm=26)
        )
        pages.append(K.page(v_body_2, header=(BOOK, f"Vocab Module {v_idx+1} &bull; Practice"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p71-82: 12 Forensic Proofreading Workouts (12 pages)
    workouts = dv_l2.MIXED_WORKOUTS
    for w_idx in range(12):
        w = workouts[w_idx % len(workouts)]
        w_title = w["title"]
        memo_text = K.clean_legacy(w.get("doc_text", ""))
        doc_heading = w.get("doc_title", "Workplace Document for Audit & Correction")
        focus = w.get("coverage", "Workplace Proofreading")
        body = (
            K.page_title(f"Workout {w_idx+1}: {w_title}",
                         kicker=f"Forensic Proofreading &bull; {focus}",
                         badge=w_idx+1)
            + K.box_html(memo_text, doc_heading)
            + K.table(["", "Error Identified in Text", "Professional Correction &amp; Rule"],
                      [[f"<b>{i}</b>", "<div style='height:8mm'></div>", ""] for i in range(1, 6)],
                      ["10mm", "45%", "45%"])
            + K.fill_notes("Key Examiner Learning Point &amp; Self-Check Reflection", 24)
        )
        pages.append(K.page(body, header=(BOOK, f"Proofreading Workout {w_idx+1}"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p83-88: 4 Workplace Writing Mock Exams (6 pages: 2 mocks 1p, 2 mocks 2p)
    mocks = mk_l2.EXAM_MOCKS
    for m_idx, m in enumerate(mocks[:3]):
        m_title = m["title"]
        m_scenario = K.clean_legacy(m.get("scenario", ""))
        m_prompt = K.clean_legacy(m.get("writing_task_prompt", ""))
        m_marks = 15

        # Mock page 1: Task briefing & Planning
        m_body_1 = (
            K.page_title(f"Official Mock Writing Exam {m_idx+1}", kicker=f"Exam Practice &bull; {m_marks} Marks", badge=f"M{m_idx+1}")
            + K.box_html(f"<p>{m_scenario}</p><div style='margin-top:2mm;font-weight:700;'>Writing Task Prompt:</div><p>{m_prompt}</p>", f"Exam Scenario: {m_title}")
            + K.tip_pair("Plan your structure (Opening, 3 Core Paragraphs, Professional Close) before writing.",
                         "Check every comma splice, homophone, and apostrophe before concluding.",
                         golden_title="Band 4 Writing Checklist", watch_title="Examiner Audit Trap")
            + K.fill_lines("Candidate Initial Planning &amp; Outline Notes", min_mm=55, gap_mm=10)
        )
        pages.append(K.page(m_body_1, header=(BOOK, f"Mock Exam {m_idx+1} &bull; Briefing"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Mock page 2: Candidate Ruled Answer Booklet
        m_body_2 = (
            K.page_title(f"Mock Exam {m_idx+1} &bull; Candidate Response Booklet", kicker="Official Ruled Response Page")
            + K.fill_lines("Write your response below:", min_mm=210, gap_mm=9.5)
        )
        pages.append(K.page(m_body_2, header=(BOOK, f"Mock Exam {m_idx+1} &bull; Response"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Reference Back Matter via K.ref_pages (Condensed Black Reference Style)
    ref_blocks = []

    # 1. Diagnostic Assessment Solutions
    p77 = mk_l2.ANSWER_KEYS_DATA.get('page_77', {})
    if 'diagnostic_answers' in p77:
        qa_diag = "".join(f"<div class='qa'><span class='q-num'>Q{q}</span><span class='q-ans'><b>{ans}</b>: {escape_html(exp)}</span></div>" for q, ans, exp in p77['diagnostic_answers'])
        ref_blocks.append(K.ref_block("Diagnostic Assessment Worked Solutions (Questions 1–10)", qa_diag))

    # 2. Units 1 to 26 Worked Solutions
    for k in sorted(mk_l2.ANSWER_KEYS_DATA.keys()):
        data = mk_l2.ANSWER_KEYS_DATA[k]
        if 'units' in data:
            for unum, uinfo in sorted(data['units'].items()):
                ex_a = escape_html(uinfo.get('ex_a', ''))
                ex_b = escape_html(uinfo.get('ex_b', ''))
                u_html = f"<div style='margin-bottom:1.5mm;'><b>Section A (Drill):</b> {ex_a}</div><div><b>Section B (Rewrite):</b> {ex_b}</div>"
                ref_blocks.append(K.ref_block(f"Unit {unum} Worked Solutions", u_html))

    # 3. Vocab Modules
    p82 = mk_l2.ANSWER_KEYS_DATA.get('page_82', {})
    if 'vocab_modules' in p82:
        v_html = "".join(f"<div style='margin-bottom:1mm;'><b>Module {m}:</b> {escape_html(ans)}</div>" for m, ans in sorted(p82['vocab_modules'].items()))
        ref_blocks.append(K.ref_block("Vocabulary in Use Answer Keys (Modules 1–6)", v_html))

    # 4. Forensic Proofreading Workouts
    if 'workouts' in p82:
        w_html = "".join(f"<div style='margin-bottom:1.5mm;'><b>Workout {w}:</b> {escape_html(ans)}</div>" for w, ans in sorted(p82['workouts'].items()))
        ref_blocks.append(K.ref_block("Forensic Proofreading Workouts (1–6)", w_html))

    # 5. Exam Mocks Proofreading
    if 'exam_mocks_proof_summary' in p82:
        m_html = "".join(f"<div style='margin-bottom:1.5mm;'><b>Mock {m}:</b> {escape_html(ans)}</div>" for m, ans in sorted(p82['exam_mocks_proof_summary'].items()))
        ref_blocks.append(K.ref_block("Workplace Writing Mock Exams Mark Schemes", m_html))

    # 6. SPaG Glossary
    glossary_l2 = [
        ("Active Voice", "Sentence structure where the subject performs the action (e.g. 'The manager approved the report')."),
        ("Passive Voice", "Sentence structure where the subject receives the action (e.g. 'The report was approved by the manager')."),
        ("Clause (Main / Independent)", "A group of words with a subject and finite verb that can stand alone as a complete sentence."),
        ("Clause (Subordinate / Dependent)", "A clause that provides extra context but cannot stand alone without an independent clause."),
        ("Comma Splice", "The error of joining two independent clauses with only a comma instead of a conjunction or semicolon."),
        ("Fragment", "An incomplete sentence lacking either a main verb or a subject."),
        ("Modal Verb", "An auxiliary verb indicating necessity, ability, or probability (e.g. must, should, would, could)."),
        ("Relative Pronoun", "A pronoun (who, which, that, whom, whose) introducing a relative clause."),
        ("Semicolon", "Punctuation mark (;) used to link closely related independent clauses or separate items in a complex list."),
        ("Subject-Verb Agreement", "The grammatical rule requiring singular subjects to take singular verbs and plural subjects to take plural verbs.")
    ]
    g_html = "".join(f"<dl><dt>{escape_html(t)}</dt><dd>{escape_html(d)}</dd></dl>" for t, d in glossary_l2)
    ref_blocks.append(K.ref_block("Essential Functional SPaG Reference Glossary", g_html))

    # 7. Index
    index_l2 = [
        ("A", [("Active and passive voice", "42"), ("Apostrophes for possession", "28"), ("Apostrophes for omission", "30")]),
        ("C", [("Capital letters", "12"), ("Colons in lists and announcements", "34"), ("Comma splices", "8"), ("Compound sentences", "16")]),
        ("D", [("Dashes and hyphens", "36"), ("Dependent clauses", "10")]),
        ("F", [("Fragments", "6")]),
        ("H", [("Homophones in workplace writing", "48")]),
        ("M", [("Modal verbs and tone", "40")]),
        ("P", [("Paragraph structure", "24"), ("Parenthetical commas", "20")]),
        ("R", [("Relative clauses", "18")]),
        ("S", [("Semicolons", "32"), ("Subject-verb agreement", "22")]),
        ("T", [("Tenses (past, present, perfect)", "38")])
    ]
    ix_html = ""
    for letter, entries in index_l2:
        items = "".join(f"<div class='ix'><span>{escape_html(t)}</span><span>{escape_html(p)}</span></div>" for t, p in entries)
        ix_html += f"<div class='ix-letter'>{letter}</div>{items}"
    ref_blocks.append(K.ref_block("Subject, Grammar &amp; Mechanics Index", ix_html))

    cover_theme = K.theme_from_cover(front_cov)
    ref_page_list = K.ref_pages("SPaG Level 2 Reference: Complete Solutions &amp; Index", ref_blocks,
                                BOOK, start_page=p_curr, subtitle="Worked Solutions, Glossary &amp; Index",
                                cols=2, theme=cover_theme, notes_title="Candidate SPaG Revision Log")
    pages.extend(ref_page_list)
    p_curr += len(ref_page_list)

    # Candidate Self-Audit Matrix
    p_audit_body = (
        K.page_title("Candidate SPaG Self-Assessment Matrix &amp; Skill Audit", kicker="Final Independent Evaluation", badge="AUDIT")
        + K.box_html(
            "<p>Grade your SPaG accuracy against formal Pearson Edexcel Level 2 standards (Band 3 SPaG = 13–15 / 15 marks):</p>"
            + K.bullets([
                "<b>Punctuation Variety:</b> Full stops, commas in complex sentences, semicolons, colons, and apostrophes fully secure.",
                "<b>Grammar &amp; Syntax:</b> Zero comma splices or fragments; accurate subject-verb agreement across collective nouns.",
                "<b>Spelling:</b> Confident command of complex workplace vocabulary and confusable homophone pairs."
            ]),
            title="Pearson Edexcel Level 2 SPaG Benchmark Rubric"
        )
        + K.fill_notes("Personal Skill Progression &amp; Weakness Remediation Commitments", min_mm=45)
    )
    pages.append(K.page(p_audit_body, header=(BOOK, "Self-Assessment Matrix"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Duplex even-page balance check before back cover
    if (len(pages) + 1) % 2 != 0:
        p_ibc_body = (
            K.page_title("Candidate SPaG Commitment &amp; Tutor Endorsement", kicker="Mastery Sign-Off &bull; Professional Development", badge="SIGN")
            + K.box_html(
                "<p>Confirm your ongoing commitment to professional standards of spelling, punctuation, and grammar:</p>"
                + K.bullets([
                    "<b>Daily Accuracy:</b> Apply the Golden Rules across all workplace emails, incident logs, and technical reports.",
                    "<b>Active Demarcation:</b> Maintain zero tolerance for comma splices, sentence fragments, and apostrophe slips.",
                    "<b>Lifelong Lexicon:</b> Continuously expand vocational vocabulary and cross-reference authoritative dictionaries."
                ]),
                title="Professional Literacy Declaration"
            )
            + K.tip_pair("Keep this mastery guide at your workstation as a permanent syntax and punctuation quick-reference.",
                         "Consistent accuracy in workplace correspondence builds professional credibility and authority.",
                         golden_title="Career Impact", watch_title="Best Practice")
            + K.fill_notes("Tutor Endorsement &amp; Candidate Next Steps", min_mm=30)
        )
        pages.append(K.page(p_ibc_body, header=(BOOK, "Tutor Endorsement"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Back Cover
    pages.append(K.back_cover(back_cov))

    print(f"Total Pages Assembled: {len(pages)}")
    out_pdf = DOWNLOADS / "MasterFunctionalSkills_SPaG_Level_2_Mastery.pdf"
    res = K.render_pdf(pages, out_pdf, theme=K.theme_from_cover(front_cov), entry3=False, title="Master Functional Skills - SPaG Level 2 Mastery")
    print(f"Rendered: {res['pdf']}")

    # Copy to ~/Documents
    shutil.copyfile(out_pdf, DOCUMENTS / out_pdf.name)

    # Run QA report
    rep = K.qa_report(out_pdf, dpi=50)
    K.print_report(rep)
    return rep


# =============================================================================
# 2. SPaG Level 1 Mastery (100 Pages)
# =============================================================================
def build_spag_l1():
    print("\n" + "="*70)
    print("BUILDING: MasterFunctionalSkills_SPaG_Level_1_Mastery.pdf (A4 Fill-The-Page)")
    print("="*70)

    BOOK = "SPaG Level 1 Mastery"
    front_cov = COV / "spag_l1_mastery_cover-01.png"
    back_cov = COV / "spag_l1_mastery_cover-02.png"

    all_units = u_l1.L1_UNITS_26
    pages = []
    used_photos = set()

    def P(kw):
        p = get_photo(kw, "spag", used_photos) or get_photo(kw, "workplace_office", used_photos) or get_photo(kw, None, used_photos)
        if p:
            used_photos.add(p)
        return p

    # p1: Front Cover
    pages.append(K.front_cover(front_cov))

    # p2: Inside Cover
    pages.append(K.inside_cover(
        "Spelling, Punctuation &amp; Grammar",
        "Level 1 &bull; Core Principles, Everyday Work Scenarios &amp; Applied Practice",
        "SPaG Level 1",
        [
            ("1&ndash;4", "Diagnostic Assessment &amp; Skill Routing", "3"),
            ("5&ndash;56", "26 Two-Page Murphy 'Grammar in Use' Units", "7"),
            ("57&ndash;68", "6 Visual Vocabulary in Use Modules", "59"),
            ("69&ndash;80", "12 Practical Proofreading &amp; Grammar Drills", "71"),
            ("81&ndash;88", "4 Realistic Workplace Writing Tasks", "83"),
            ("89&ndash;98", "Comprehensive Explanatory Answer Keys", "91"),
            ("99", "Candidate Self-Audit &amp; Progress Matrix", "99"),
        ],
        footer=BOOK
    ))

    # p3-6: Diagnostic Assessment (4 pages, 10 authentic questions total)
    diag_qs = spag_data_l1.L1_DIAGNOSTIC["questions"]
    scoring_rows = spag_data_l1.L1_DIAGNOSTIC["scoring"]

    def make_ex_items(qs):
        items = []
        for q in qs:
            clean_opts = [o[3:] if len(o) > 3 and o[1] == ")" else o for o in q["options"]]
            pr = q.get("prompt", "")
            top = q.get("topic", "")
            items.append({
                "q": f"<b>{pr}</b> <span style='font-size:10.5pt;color:var(--muted);font-weight:400;'>({top})</span>",
                "options": clean_opts,
                "marks": 1
            })
        return items

    # Page 3: Q1-3 (3 questions)
    p3_body = (
        K.page_title("Baseline Diagnostic Assessment &bull; Part 1 of 4",
                     kicker="Diagnostic Audit &bull; Questions 1&ndash;3",
                     lead="Answer each question carefully. Circle your chosen answer. Do not use a dictionary.")
        + K.exercise_list(make_ex_items(diag_qs[0:3]), start=1)
        + K.fill_notes("Examiner Checkpoint &bull; Questions 1 to 3 Notes", min_mm=32)
    )
    pages.append(K.page(p3_body, header=(BOOK, "Diagnostic 1/4"), footer=BOOK, page_no=3))

    # Page 4: Q4-6 (3 questions)
    p4_body = (
        K.page_title("Baseline Diagnostic Assessment &bull; Part 2 of 4",
                     kicker="Diagnostic Audit &bull; Questions 4&ndash;6",
                     lead="Identify correct capitalization, punctuation, and sentence construction.")
        + K.exercise_list(make_ex_items(diag_qs[3:6]), start=4)
        + K.fill_notes("Examiner Checkpoint &bull; Questions 4 to 6 Notes", min_mm=32)
    )
    pages.append(K.page(p4_body, header=(BOOK, "Diagnostic 2/4"), footer=BOOK, page_no=4))

    # Page 5: Q7-8 (2 questions) + Scoring Matrix Table
    score_table = """<div class="box" style="padding:2.5mm 3.5mm;background:#fff;border:1.5px solid var(--soft);margin-top:2mm;">
      <div style="font-weight:700;color:var(--primary);font-size:11.5pt;margin-bottom:1.5mm;">Diagnostic Performance Matrix &amp; Recommended Study Pathway</div>
      <table style="width:100%;border-collapse:collapse;font-size:10pt;">
        <thead>
          <tr style="background:var(--light);color:var(--primary);text-align:left;">
            <th style="padding:1.5mm;border:1px solid var(--soft);">Score Range</th>
            <th style="padding:1.5mm;border:1px solid var(--soft);">Readiness Level</th>
            <th style="padding:1.5mm;border:1px solid var(--soft);">Recommended Curriculum Route</th>
          </tr>
        </thead>
        <tbody>"""
    for row in scoring_rows:
        score_table += f"""
          <tr>
            <td style="padding:1.5mm;border:1px solid var(--soft);font-weight:700;">{row['range']}</td>
            <td style="padding:1.5mm;border:1px solid var(--soft);color:var(--accent);font-weight:600;">{row['status']}</td>
            <td style="padding:1.5mm;border:1px solid var(--soft);">{row['advice']}</td>
          </tr>"""
    score_table += """</tbody></table></div>"""

    p5_body = (
        K.page_title("Baseline Diagnostic Assessment &bull; Part 3 of 4",
                     kicker="Diagnostic Audit &bull; Questions 7&ndash;8",
                     lead="Grammar and syntax accuracy questions, followed by the diagnostic benchmark rubric.")
        + K.exercise_list(make_ex_items(diag_qs[6:8]), start=7)
        + score_table
        + K.fill_notes("Personal Learning Target &amp; Study Priority", min_mm=26)
    )
    pages.append(K.page(p5_body, header=(BOOK, "Diagnostic 3/4"), footer=BOOK, page_no=5))

    # Page 6: Q9-10 (2 questions) + Candidate Action Plan
    p6_body = (
        K.page_title("Baseline Diagnostic Assessment &bull; Part 4 of 4",
                     kicker="Diagnostic Audit &bull; Questions 9&ndash;10 &amp; Study Plan",
                     lead="Final practical diagnostic questions and your personalized revision action plan.")
        + K.exercise_list(make_ex_items(diag_qs[8:10]), start=9)
        + K.tip_pair("Check your diagnostic score against the answer keys on page 91.",
                     "Prioritise the specific units flagged in questions you found challenging.",
                     golden_title="Tutor Golden Rule", watch_title="Revision Target")
        + K.fill_lines("Candidate Action Plan &amp; Priority Units to Master", min_mm=32, gap_mm=9.5)
    )
    pages.append(K.page(p6_body, header=(BOOK, "Diagnostic 4/4"), footer=BOOK, page_no=6))

    # p7-58: 26 Units (52 pages)
    characters = [
        ("Subi", "abdul tutor man", "#0c4a6e"),
        ("Priya", "priya tutor woman", "#7c3aed"),
        ("Marcus", "marcus apprentice", "#0d9488"),
        ("Sarah", "sarah care nurse", "#be123c"),
        ("Sam", "sam learner thinking", "#475569"),
    ]

    p_curr = 7
    for u_idx, u in enumerate(all_units):
        u_num = u["unit"]
        char_name, char_kw, char_col = characters[u_idx % len(characters)]

        # --- Left Page: Learn ---
        anchor_title = u.get("anchor_title", "Everyday Communication")
        if len(anchor_title) > 90:
            anchor_title = anchor_title[:87] + "..."
        rule_title = u.get("rule_formula_title", "Core Grammar Rule &amp; Sentence Pattern")
        rule_text = K.clean_legacy(u.get("rule_formula_html", ""))
        bad_text = u.get("worked_bad", "Example with error.")
        good_text = u.get("worked_good", "Corrected example.")
        why_text = u.get("worked_why", "Grammar rule explanation.")

        is_long = (u_num in (6, 11, 23, 25)) or (len(rule_text) > 950)
        font_sz = "8.8pt" if is_long else ("9.4pt" if len(rule_text) > 750 else "9.8pt")
        lh = "1.14" if is_long else ("1.18" if len(rule_text) > 750 else "1.22")
        bubble_h = 44 if is_long else 48
        cmp_sz = "8.8pt" if is_long else "9.4pt"
        pad_v = "1.0mm" if is_long else "1.5mm"

        left_body = (
            K.page_title(u["title"], kicker=f"Unit {u_num} &bull; Core Foundations", badge=u_num)
            + K.character_bubble(
                K.cartoon(char_kw), char_name,
                f"<b style='color:var(--accent)'>A &nbsp;The Concept in Everyday Use:</b> {anchor_title}",
                "left", bubble_h, char_col
            )
            + f"""<div class="box rule" style="flex:1 1 auto;padding:{pad_v} 3.5mm;font-size:{font_sz};line-height:{lh};">
                <div class="bt" style="margin-bottom:1mm;"><span class="ico">&#9733;</span>B &nbsp;{rule_title}</div>
                <div style="font-size:{font_sz};">{rule_text}</div>
              </div>"""
            + K.compare(
                f"<div style='font-size:{cmp_sz};line-height:1.2;'>{bad_text}</div>",
                f"<div style='font-size:{cmp_sz};line-height:1.2;'>{good_text}</div><div style='font-size:9pt;color:var(--muted);margin-top:1mm;'><b>Why:</b> {why_text}</div>",
                stacked=False, bad_label="&#10007; Common Mistake", good_label="&#10003; Correct Sentence"
            )
        )
        pages.append(K.page(left_body, header=(BOOK, f"Unit {u_num} &bull; Learn"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # --- Right Page: Practise ---
        # Exercise A: MCQs (2 questions)
        ex_a_items = []
        for q_tuple in u.get("exercise_a", [])[:2]:
            q_text, opts = q_tuple[0], q_tuple[1]
            clean_opts = [o[3:] if len(o) > 3 and o[1] == ")" else o for o in opts]
            ex_a_items.append({"q": q_text, "options": clean_opts})

        # Exercise B: Transformation (2 questions)
        ex_b_items = []
        for b_tuple in u.get("exercise_b", [])[:2]:
            prompt_type, original = b_tuple[0], b_tuple[1]
            ex_b_items.append((f"<b>[{prompt_type}]:</b> <i>{original}</i>", 2))

        right_body = (
            K.section("A", "Tick the correct sentence")
            + K.exercise_list(ex_a_items)
            + K.section("B", "Rewrite each sentence correctly")
            + K.exercise_list(ex_b_items, start=3)
            + K.fill_lines(f"<span style='color:var(--accent)'>C &nbsp;Applied Practice:</span> Write two sentences of your own using the rules from Unit {u_num}.", min_mm=26, gap_mm=9)
        )
        pages.append(K.page(right_body, header=(BOOK, f"Unit {u_num} &bull; Practise"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p59-70: 6 Vocab in Use Modules (12 pages: 2 pages each)
    vocab_mods = d_l1.VOCAB_MODULES
    for v_idx, vm in enumerate(vocab_mods):
        v_title = vm["title"]
        table_rows = vm["tables"][0]["rows"]
        tiles = []
        for row in table_rows[:6]:
            pre, meaning, ex_sent = row[0], row[1], row[2]
            clean_pre = str(pre).strip()
            tiles.append((
                P("workplace office meeting business"),
                f"<b>{clean_pre}</b> &rarr; <span style='color:var(--accent);'>{meaning}</span>",
                ex_sent
            ))
        v_body_1 = (
            K.page_title(f"Vocabulary Module {v_idx+1}: {v_title}",
                         kicker="Vocabulary in Use &bull; Visual Dictionary",
                         lead=vm.get("intro", "Essential words and spelling patterns for Functional Skills Level 1 English."))
            + K.photo_grid(tiles, cols=3, fill=True, min_tile_mm=62)
        )
        pages.append(K.page(v_body_1, header=(BOOK, f"Vocab Module {v_idx+1} &bull; Dictionary"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        drill_data = vm.get("drill", {})
        drill_items = [
            (f"<b>Vocabulary Drill:</b> {drill_data.get('prompt', 'Transform into professional English:')}<br><i>'{drill_data.get('bad', '')}'</i>", 3),
            (f"Write a workplace sentence demonstrating correct usage of <b>{table_rows[0][1]}</b>.", 3),
            (f"Write a message to a colleague using at least two formal words from Module {v_idx+1}.", 3),
        ]
        v_body_2 = (
            K.page_title(f"Module {v_idx+1} &bull; Applied Vocational Drills",
                         kicker="Vocabulary in Use &bull; Practice Drills",
                         lead="Practise using these key words in everyday and work situations.")
            + K.exercise_list(drill_items)
            + K.fill_notes(f"Word Study &amp; Spelling Memory Box for Module {v_idx+1}", min_mm=26)
        )
        pages.append(K.page(v_body_2, header=(BOOK, f"Vocab Module {v_idx+1} &bull; Practice"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p71-82: 12 Mixed Proofreading Workouts (12 pages)
    workouts = d_l1.MIXED_WORKOUTS
    for w_idx in range(12):
        w = workouts[w_idx % len(workouts)]
        w_title = w["title"]
        memo_text = K.clean_legacy(w.get("doc_text", ""))
        doc_heading = w.get("doc_title", "Everyday Document for Proofreading")
        focus = w.get("coverage", "Practical Proofreading")
        body = (
            K.page_title(f"Workout {w_idx+1}: {w_title}",
                         kicker=f"Proofreading Practice &bull; {focus}",
                         badge=w_idx+1)
            + K.box_html(memo_text, doc_heading)
            + K.table(["", "Error Found in Text", "Correction &amp; Rule"],
                      [[f"<b>{i}</b>", "<div style='height:8mm'></div>", ""] for i in range(1, 6)],
                      ["10mm", "45%", "45%"])
            + K.fill_notes("Key Learning Rule to Remember", 24)
        )
        pages.append(K.page(body, header=(BOOK, f"Proofreading Workout {w_idx+1}"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p83-88: 3 Mock Writing Exam Papers (6 pages: 2 pages each)
    mocks = d_l1.EXAM_MOCKS
    for m_idx, m in enumerate(mocks[:3]):
        m_title = m["title"]
        m_scenario = K.clean_legacy(m.get("scenario", ""))
        m_prompt = K.clean_legacy(m.get("writing_task_prompt", ""))
        m_marks = 12

        m_body_1 = (
            K.page_title(f"Official Mock Writing Exam {m_idx+1}", kicker=f"Exam Practice &bull; {m_marks} Marks", badge=f"M{m_idx+1}")
            + K.box_html(f"<p>{m_scenario}</p><div style='margin-top:2mm;font-weight:700;'>Your Writing Task:</div><p>{m_prompt}</p>", f"Task: {m_title}")
            + K.tip_pair("Plan your ideas in 2-3 short paragraphs before starting.",
                         "Check capital letters for 'I', names, and days of the week.",
                         golden_title="Level 1 Success Checklist", watch_title="Common Slip")
            + K.fill_lines("Candidate Notes &amp; Word Plan", min_mm=55, gap_mm=10)
        )
        pages.append(K.page(m_body_1, header=(BOOK, f"Mock Exam {m_idx+1} &bull; Briefing"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        m_body_2 = (
            K.page_title(f"Mock Exam {m_idx+1} &bull; Candidate Response Booklet", kicker="Official Ruled Response Page")
            + K.fill_lines("Write your response below:", min_mm=210, gap_mm=9.5)
        )
        pages.append(K.page(m_body_2, header=(BOOK, f"Mock Exam {m_idx+1} &bull; Response"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Reference Back Matter via K.ref_pages (Condensed Black Reference Style)
    ref_blocks = []

    # 1. Diagnostic Assessment Solutions
    p77 = d_l1.ANSWER_KEYS_6P.get('page_77', {})
    if 'diagnostic_answers' in p77:
        qa_diag = "".join(f"<div class='qa'><span class='q-num'>Q{i+1}</span><span class='q-ans'>{escape_html(ans)}</span></div>" for i, ans in enumerate(p77['diagnostic_answers']))
        ref_blocks.append(K.ref_block("Diagnostic Assessment Worked Solutions (Questions 1–10)", qa_diag))

    # 2. Units 1 to 26 Worked Solutions
    for k in sorted(d_l1.ANSWER_KEYS_6P.keys()):
        data = d_l1.ANSWER_KEYS_6P[k]
        if 'units' in data:
            for unum, uinfo in sorted(data['units'].items()):
                ex_a = escape_html(uinfo.get('ex_a', ''))
                ex_b = escape_html(uinfo.get('ex_b', ''))
                u_html = f"<div style='margin-bottom:1.5mm;'><b>Section A (Drill):</b> {ex_a}</div><div><b>Section B (Rewrite):</b> {ex_b}</div>"
                ref_blocks.append(K.ref_block(f"Unit {unum} Worked Solutions", u_html))

    # 3. Vocab Modules
    p81 = d_l1.ANSWER_KEYS_6P.get('page_81', {})
    if 'vocab_modules' in p81:
        v_html = "".join(f"<div style='margin-bottom:1mm;'><b>Module {m}:</b> {escape_html(ans)}</div>" for m, ans in sorted(p81['vocab_modules'].items()))
        ref_blocks.append(K.ref_block("Vocabulary in Use Answer Keys (Modules 1–6)", v_html))

    # 4. Mixed Proofreading Workouts
    p82 = d_l1.ANSWER_KEYS_6P.get('page_82', {})
    if 'mixed_workouts' in p82:
        w_parts = []
        for w, ans in sorted(p82['mixed_workouts'].items()):
            if isinstance(ans, dict):
                p_a = f"<div><b>Part A:</b> {escape_html(ans.get('part_a', ''))}</div>" if 'part_a' in ans else ""
                p_b = f"<div><b>Part B:</b> {escape_html(ans.get('part_b', ''))}</div>" if 'part_b' in ans else ""
                p_c = f"<div><b>Part C:</b> {escape_html(ans.get('part_c', ''))}</div>" if 'part_c' in ans else ""
                w_parts.append(f"<div style='margin-bottom:1.5mm;'><b>Workout {w}:</b>{p_a}{p_b}{p_c}</div>")
            else:
                w_parts.append(f"<div style='margin-bottom:1.5mm;'><b>Workout {w}:</b> {escape_html(ans)}</div>")
        ref_blocks.append(K.ref_block("Mixed Proofreading Workouts (1–6)", "".join(w_parts)))

    # 5. Exam Mocks Proofreading
    if 'exam_mocks' in p82:
        m_parts = []
        for m, ans in sorted(p82['exam_mocks'].items()):
            if isinstance(ans, dict):
                p_ans = "<br>".join(escape_html(p) for p in ans.get('proof_answers', []))
                rub = f"<em>Rubric:</em> {escape_html(ans.get('writing_rubric', ''))}" if 'writing_rubric' in ans else ""
                m_parts.append(f"<div style='margin-bottom:1.5mm;'><b>Mock {m}:</b><br>{p_ans}<br>{rub}</div>")
            else:
                m_parts.append(f"<div style='margin-bottom:1.5mm;'><b>Mock {m}:</b> {escape_html(ans)}</div>")
        ref_blocks.append(K.ref_block("Mock Writing Examination Mark Schemes", "".join(m_parts)))

    # 6. SPaG Glossary
    glossary_l1 = [
        ("Capital Letter", "Used at the start of every sentence, for the word 'I', people's names, places, days, and months."),
        ("Full Stop", "Punctuation mark (.) used to mark the end of a complete statement."),
        ("Question Mark", "Punctuation mark (?) used at the end of a direct question."),
        ("Exclamation Mark", "Punctuation mark (!) used to show strong feeling, surprise, or urgency."),
        ("Comma in Lists", "Used to separate items in a list (e.g. 'paper, pens, and pencils')."),
        ("Conjunction", "A linking word used to join two sentences (e.g. and, but, so, because)."),
        ("Past Tense", "Verb forms used to describe things that happened yesterday or in the past (e.g. walked, saw)."),
        ("Present Tense", "Verb forms used for things happening now or regularly (e.g. walks, sees)."),
        ("Subject-Verb Agreement", "Matching singular subjects with singular verbs (e.g. 'He works' vs 'They work')."),
        ("Homophone", "Words that sound the same but have different spellings and meanings (e.g. there, their, they're).")
    ]
    g_html = "".join(f"<dl><dt>{escape_html(t)}</dt><dd>{escape_html(d)}</dd></dl>" for t, d in glossary_l1)
    ref_blocks.append(K.ref_block("Functional Skills SPaG Glossary", g_html))

    # 7. Index
    index_l1 = [
        ("A", [("Annexe D spelling words", "50"), ("Apostrophes for omission", "28"), ("Apostrophes for possession", "30")]),
        ("C", [("Capital letters", "10"), ("Commas in lists", "16"), ("Conjunctions (and, but)", "18")]),
        ("E", [("Ending sentences (. ! ?)", "12"), ("Exclamation marks", "14")]),
        ("F", [("Full stops", "12")]),
        ("H", [("Homophones (there/their/they're)", "44")]),
        ("P", [("Paragraphs", "24"), ("Past tense regular and irregular", "20")]),
        ("Q", [("Question marks", "14")]),
        ("S", [("Subject-verb agreement", "22"), ("Suffixes (-ful, -less)", "48")]),
        ("U", [("Using because and so", "18")])
    ]
    ix_html = ""
    for letter, entries in index_l1:
        items = "".join(f"<div class='ix'><span>{escape_html(t)}</span><span>{escape_html(p)}</span></div>" for t, p in entries)
        ix_html += f"<div class='ix-letter'>{letter}</div>{items}"
    ref_blocks.append(K.ref_block("Subject &amp; Mechanics Index", ix_html))

    cover_theme = K.theme_from_cover(front_cov)
    ref_page_list = K.ref_pages("SPaG Level 1 Reference: Solutions &amp; Index", ref_blocks,
                                BOOK, start_page=p_curr, subtitle="Worked Solutions, Glossary &amp; Index",
                                cols=2, theme=cover_theme, notes_title="Candidate SPaG Revision Log")
    pages.extend(ref_page_list)
    p_curr += len(ref_page_list)

    # Candidate Self-Audit Matrix
    p_audit_body = (
        K.page_title("Candidate SPaG Self-Assessment Matrix &amp; Progress Chart", kicker="Level 1 SPaG Standards", badge="AUDIT")
        + K.box_html(
            "<p>Check off your skills against Pearson Edexcel Level 1 standards:</p>"
            + K.bullets([
                "Write clearly in full sentences with capital letters and full stops.",
                "Use commas accurately in lists and conjunctions to join ideas.",
                "Spell everyday workplace words correctly using Annexe D rules."
            ]),
            title="Pearson Edexcel Level 1 SPaG Rubric"
        )
        + K.fill_notes("Personal Progress &amp; Weakness Remediation Log", min_mm=45)
    )
    pages.append(K.page(p_audit_body, header=(BOOK, "Self-Assessment Matrix"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Duplex even-page balance check before back cover
    if (len(pages) + 1) % 2 != 0:
        p_ibc_body = (
            K.page_title("Candidate SPaG Commitment &amp; Tutor Endorsement", kicker="Level 1 SPaG Sign-Off", badge="SIGN")
            + K.box_html(
                "<p>Confirm your ongoing commitment to professional standards of spelling, punctuation, and grammar:</p>"
                + K.bullets([
                    "<b>Accurate Demarcation:</b> Always start every sentence with a capital letter and end with a full stop.",
                    "<b>Comma Precision:</b> Use commas accurately in lists and after introductory connective phrases.",
                    "<b>Everyday Spelling:</b> Confidently spell core vocational vocabulary without phonics slips."
                ]),
                title="Level 1 Professional Literacy Declaration"
            )
            + K.tip_pair("Re-read all completed written work before submitting to catch missing punctuation.",
                         "Accurate spelling and clear sentences ensure your workplace messages are understood first time.",
                         golden_title="Audit Habit", watch_title="Workplace Value")
            + K.fill_notes("Tutor Endorsement &amp; Candidate Next Steps", min_mm=30)
        )
        pages.append(K.page(p_ibc_body, header=(BOOK, "Tutor Endorsement"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Back Cover
    pages.append(K.back_cover(back_cov))

    print(f"Total Pages Assembled: {len(pages)}")
    out_pdf = DOWNLOADS / "MasterFunctionalSkills_SPaG_Level_1_Mastery.pdf"
    res = K.render_pdf(pages, out_pdf, theme=K.theme_from_cover(front_cov), entry3=False, title="Master Functional Skills - SPaG Level 1 Mastery")
    print(f"Rendered: {res['pdf']}")

    shutil.copyfile(out_pdf, DOCUMENTS / out_pdf.name)
    rep = K.qa_report(out_pdf, dpi=50)
    K.print_report(rep)
    return rep


# =============================================================================
# 3. SPaG Entry Level 3 Mastery (96 Pages, 14pt Body Font)
# =============================================================================
def build_spag_e3():
    print("\n" + "="*70)
    print("BUILDING: MasterFunctionalSkills_SPaG_Entry_Level_3_Mastery.pdf (A4 14pt Entry 3)")
    print("="*70)

    BOOK = "SPaG Entry Level 3 Mastery"
    front_cov = COV / "spag_e3_mastery_cover-01.png"
    back_cov = COV / "spag_e3_mastery_cover-02.png"

    all_units = u_e3.units_data
    pages = []
    used_photos = set()

    def P(kw):
        p = get_photo(kw, "spag", used_photos) or get_photo(kw, "classroom_studying_adults", used_photos) or get_photo(kw, None, used_photos)
        if p:
            used_photos.add(p)
        return p

    # p1: Front Cover
    pages.append(K.front_cover(front_cov))

    # p2: Inside Cover
    pages.append(K.inside_cover(
        "Spelling, Punctuation &amp; Grammar",
        "Entry Level 3 &bull; Visual Rules, Clear Pictures &amp; Step-by-Step Handwriting Drills",
        "SPaG Entry Level 3",
        [
            ("1&ndash;4", "Diagnostic Assessment &amp; Easy Visual Selector", "3"),
            ("5&ndash;52", "24 Two-Page Murphy 'Grammar in Use' Units", "7"),
            ("53&ndash;64", "6 Phonics &amp; High-Frequency Word Banks", "55"),
            ("65&ndash;76", "12 Practical Sentence Building Workouts", "67"),
            ("77&ndash;84", "4 Practical Workplace Form-Filling Mocks", "79"),
            ("85&ndash;94", "Step-by-Step Explanatory Answer Keys", "87"),
            ("95", "Learner Progress Tracker &amp; Sticker Chart", "95"),
        ],
        footer=BOOK
    ))

    # p3-6: Diagnostic Assessment (4 pages, 10 authentic questions total)
    diag_qs = d_e3.DIAGNOSTIC_QUESTIONS

    def make_ex_items(qs):
        items = []
        for q in qs:
            clean_opts = [o[3:] if len(o) > 3 and o[1] == ')' else o for o in q["options"]]
            q_text = q.get("question") or q.get("prompt", "")
            items.append({
                "q": f"<b>{q_text}</b>",
                "options": clean_opts,
                "marks": 1
            })
        return items

    # Page 3: Q1-3 (3 questions)
    p3_body = (
        K.page_title("Visual Diagnostic Assessment &bull; Part 1 of 4",
                     kicker="Entry Level 3 &bull; Questions 1&ndash;3",
                     lead="Tick the best answer for each question. Circle your chosen answer. Do not use a dictionary.")
        + K.exercise_list(make_ex_items(diag_qs[0:3]), start=1)
        + K.fill_notes("Tutor Diagnostic Notes &bull; Questions 1 to 3", min_mm=32)
    )
    pages.append(K.page(p3_body, header=(BOOK, "Diagnostic 1/4"), footer=BOOK, page_no=3))

    # Page 4: Q4-6 (3 questions)
    p4_body = (
        K.page_title("Visual Diagnostic Assessment &bull; Part 2 of 4",
                     kicker="Entry Level 3 &bull; Questions 4&ndash;6",
                     lead="Identify correct capitalisation, punctuation, and sentence construction.")
        + K.exercise_list(make_ex_items(diag_qs[3:6]), start=4)
        + K.fill_notes("Tutor Diagnostic Notes &bull; Questions 4 to 6", min_mm=32)
    )
    pages.append(K.page(p4_body, header=(BOOK, "Diagnostic 2/4"), footer=BOOK, page_no=4))

    # Page 5: Q7-8 (2 questions) + Scoring Matrix Table
    score_table = """<div class="box" style="padding:2.5mm 3.5mm;background:#fff;border:1.5px solid var(--soft);margin-top:2mm;">
      <div style="font-weight:700;color:var(--primary);font-size:11.5pt;margin-bottom:1.5mm;">Diagnostic Performance Matrix &amp; Study Pathway</div>
      <table style="width:100%;border-collapse:collapse;font-size:10pt;">
        <thead>
          <tr style="background:var(--light);color:var(--primary);text-align:left;">
            <th style="padding:1.5mm;border:1px solid var(--soft);">Score</th>
            <th style="padding:1.5mm;border:1px solid var(--soft);">Readiness Level</th>
            <th style="padding:1.5mm;border:1px solid var(--soft);">Recommended Curriculum Route</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td style="padding:1.5mm;border:1px solid var(--soft);font-weight:700;">8&ndash;10</td>
            <td style="padding:1.5mm;border:1px solid var(--soft);color:var(--accent);font-weight:600;">Entry 3 Confident</td>
            <td style="padding:1.5mm;border:1px solid var(--soft);">Consolidate complex sentences and prepare for Level 1 progression.</td>
          </tr>
          <tr>
            <td style="padding:1.5mm;border:1px solid var(--soft);font-weight:700;">5&ndash;7</td>
            <td style="padding:1.5mm;border:1px solid var(--soft);color:var(--accent);font-weight:600;">Developing Skill</td>
            <td style="padding:1.5mm;border:1px solid var(--soft);">Work systematically through Units 1 to 24 with tutor check-ins.</td>
          </tr>
          <tr>
            <td style="padding:1.5mm;border:1px solid var(--soft);font-weight:700;">0&ndash;4</td>
            <td style="padding:1.5mm;border:1px solid var(--soft);color:var(--accent);font-weight:600;">Foundational Support</td>
            <td style="padding:1.5mm;border:1px solid var(--soft);">Focus on high-frequency word banks and capital letters first.</td>
          </tr>
        </tbody></table></div>"""

    p5_body = (
        K.page_title("Visual Diagnostic Assessment &bull; Part 3 of 4",
                     kicker="Entry Level 3 &bull; Questions 7&ndash;8",
                     lead="Grammar and punctuation check, followed by your diagnostic pathway matrix.")
        + K.exercise_list(make_ex_items(diag_qs[6:8]), start=7)
        + score_table
        + K.fill_notes("Personal Learning Target &amp; Study Priority", min_mm=26)
    )
    pages.append(K.page(p5_body, header=(BOOK, "Diagnostic 3/4"), footer=BOOK, page_no=5))

    # Page 6: Q9-10 (2 questions) + Action Plan
    p6_body = (
        K.page_title("Visual Diagnostic Assessment &bull; Part 4 of 4",
                     kicker="Entry Level 3 &bull; Questions 9&ndash;10 &amp; Study Plan",
                     lead="Final diagnostic questions and your personalized study action plan.")
        + K.exercise_list(make_ex_items(diag_qs[8:10]), start=9)
        + K.tip_pair("Check your diagnostic answers with your tutor or on page 91.",
                     "Mark the units you need to practice first on your progress chart.",
                     golden_title="Tutor Golden Rule", watch_title="Next Steps")
        + K.fill_lines("Candidate Action Plan &amp; Priority Units to Master", min_mm=32, gap_mm=9.5)
    )
    pages.append(K.page(p6_body, header=(BOOK, "Diagnostic 4/4"), footer=BOOK, page_no=6))

    # p7-54: 24 Units (48 pages)
    characters = [
        ("Subi", "abdul tutor man", "#0c4a6e"),
        ("Sarah", "sarah care nurse", "#be123c"),
        ("Marcus", "marcus apprentice", "#0d9488"),
        ("Priya", "priya tutor woman", "#7c3aed"),
        ("Sam", "sam learner thinking", "#475569"),
    ]

    p_curr = 7
    for u_idx, u in enumerate(all_units):
        u_num = u["unit"]
        char_name, char_kw, char_col = characters[u_idx % len(characters)]

        # --- Left Page: Learn ---
        anchor_title = u.get("anchor_title", "Everyday Situation")
        if len(anchor_title) > 90:
            anchor_title = anchor_title[:87] + "..."
        formula_title = u.get("formula_title", "How to Use This Rule")
        formula_html = K.clean_legacy(u.get("formula_html", ""))
        pitfall_text = u.get("pitfall_text", "Common error.")
        model_text = u.get("model_text", "Correct model.")
        why_text = u.get("why_text", "Explanation of rule.")

        is_long = len(formula_html) > 850
        font_sz = "8.8pt" if is_long else "9.2pt"
        lh = "1.14" if is_long else "1.18"
        bubble_h = 44 if is_long else 48
        cmp_sz = "8.8pt" if is_long else "9.2pt"
        pad_v = "1.0mm" if is_long else "1.4mm"

        left_body = (
            K.page_title(u["title"], kicker=f"Unit {u_num} &bull; Entry 3 Basics", badge=u_num)
            + K.character_bubble(
                K.cartoon(char_kw), char_name,
                f"<b style='color:var(--accent)'>A &nbsp;Look &amp; Learn:</b><br>{anchor_title}",
                "left", bubble_h, char_col
            )
            + f"""<div class="box rule" style="flex:1 1 auto;padding:{pad_v} 3.5mm;font-size:{font_sz};line-height:{lh};">
                <div class="bt" style="margin-bottom:1mm;"><span class="ico">&#9733;</span>B &nbsp;{formula_title}</div>
                <div>{formula_html}</div>
              </div>"""
            + K.compare(
                f"<div style='font-size:{cmp_sz};line-height:1.2;'>{pitfall_text}</div>",
                f"<div style='font-size:{cmp_sz};line-height:1.2;'>{model_text}</div><div style='font-size:9pt;color:var(--muted);margin-top:1mm;'><b>Tip:</b> {why_text}</div>",
                stacked=False, bad_label="&#10007; Not Quite Right", good_label="&#10003; Good Sentence"
            )
        )

        pages.append(K.page(left_body, header=(BOOK, f"Unit {u_num} &bull; Learn"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # --- Right Page: Practise ---
        ex_a_items = []
        for q_tuple in u.get("exercise_a", [])[:2]:
            q_text, opts = q_tuple[0], q_tuple[1]
            clean_opts = [o[3:] if len(o) > 3 and o[1] == ")" else o for o in opts]
            ex_a_items.append({"q": q_text, "options": clean_opts})

        ex_b_items = []
        for b_tuple in u.get("exercise_b", [])[:2]:
            prompt_type, original = b_tuple[0], b_tuple[1]
            ex_b_items.append((f"<b>[{prompt_type}]:</b> <i>{original}</i>", 2))

        right_body = (
            K.section("A", "Tick the correct answer")
            + K.exercise_list(ex_a_items)
            + K.section("B", "Write the sentence correctly")
            + K.exercise_list(ex_b_items, start=3)
            + K.fill_lines(f"<span style='color:var(--accent)'>C &nbsp;Your Turn:</span> Write one sentence of your own using the rule from Unit {u_num}.", min_mm=26, gap_mm=9.5)
        )
        pages.append(K.page(right_body, header=(BOOK, f"Unit {u_num} &bull; Practise"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p55-66: 6 Phonics & High-Frequency Word Banks (12 pages: 2 pages each)
    word_banks = [
        ("High-Frequency Days, Months & Seasons", [("Monday", "First day of work week"), ("Friday", "End of the working week"), ("September", "Autumn college term starts"), ("Winter", "Cold season requiring warm clothing"), ("August", "Summer holiday month"), ("Wednesday", "Middle of the week")]),
        ("Everyday Workplace Signs & Safety Words", [("Danger", "Keep clear of hazard"), ("Caution", "Wet floor warning"), ("Exit", "Emergency fire escape"), ("Notice", "Staff information board"), ("Private", "Staff only access"), ("Entrance", "Main public doorway")]),
        ("Spelling Pattern: Double Consonants", [("Letter", "Written message in envelope"), ("Dinner", "Evening meal"), ("Hammer", "Tool for driving nails"), ("Traffic", "Vehicles on the road"), ("Lesson", "Classroom study session"), ("Happen", "Take place or occur")]),
        ("Spelling Pattern: Silent Letters", [("Knife", "Kitchen cutting utensil"), ("Wrist", "Joint above hand"), ("Doubt", "Uncertain feeling"), ("Thumb", "Short digit on hand"), ("Sign", "Public notice board"), ("Comb", "Hair grooming tool")]),
        ("Common Irregular Plurals", [("Child / Children", "Young people at school"), ("Man / Men", "Adult male workers"), ("Woman / Women", "Adult female colleagues"), ("Foot / Feet", "Measurement of length"), ("Tooth / Teeth", "Dentist appointment"), ("Person / People", "Community members")]),
        ("Homophones: Words That Sound Alike", [("Hear / Here", "Listen / This place"), ("See / Sea", "Look / Ocean water"), ("One / Won", "Number 1 / First place"), ("Buy / By", "Purchase / Near to"), ("Right / Write", "Correct / Put pen to paper"), ("Sun / Son", "Bright star / Male child")])
    ]

    for wb_idx, (wb_title, words) in enumerate(word_banks):
        tiles = []
        for word, desc in words:
            tiles.append((
                P("everyday objects workplace classroom"),
                f"<b>{word}</b>",
                desc
            ))
        wb_body_1 = (
            K.page_title(f"Word Bank {wb_idx+1}: {wb_title}",
                         kicker="Entry Level 3 &bull; Phonics &amp; Word Banks",
                         lead="Essential words to recognise, read, and spell correctly every time.")
            + K.photo_grid(tiles, cols=3, fill=True, min_tile_mm=62)
        )
        pages.append(K.page(wb_body_1, header=(BOOK, f"Word Bank {wb_idx+1}"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        wb_body_2 = (
            K.page_title(f"Word Bank {wb_idx+1} &bull; Practice &amp; Handwriting",
                         kicker="Spelling Practice &bull; Look, Say, Cover, Write, Check")
            + K.exercise_list([
                (f"Copy the word <b>{words[0][0]}</b> twice neatly on the lines below:", 2),
                (f"Write a short sentence using the word <b>{words[1][0]}</b>:", 2),
                (f"Write a short sentence using the word <b>{words[2][0]}</b>:", 2)
            ])
            + K.fill_notes(f"My Spelling Practice Box for Word Bank {wb_idx+1}", min_mm=30)
        )
        pages.append(K.page(wb_body_2, header=(BOOK, f"Word Bank {wb_idx+1} &bull; Practice"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p67-78: 12 Mixed Sentence Building Workouts (12 pages)
    for w_idx in range(12):
        w_title = f"Sentence Building Workout {w_idx+1}"
        body = (
            K.page_title(w_title, kicker="Practical Skills &bull; Sentence Building", badge=w_idx+1)
            + K.box_html(
                "<p>Read the sentences below. Each one has a missing capital letter or full stop.</p>"
                + K.bullets([
                    "the delivery arrived on Tuesday morning",
                    "my manager said i could take my lunch break at one o'clock",
                    "is the doctor surgery open on saturday"
                ]),
                title="Sentences to Correct"
            )
            + K.exercise_list([
                ("Rewrite sentence 1 with a capital letter and full stop:", 2),
                ("Rewrite sentence 2 with capital letters for 'My' and 'I':", 2),
                ("Rewrite sentence 3 with a capital letter and question mark:", 2)
            ], start=1)
            + K.fill_notes("Handwriting Practice &amp; Tutor Comments", 26)
        )
        pages.append(K.page(body, header=(BOOK, f"Workout {w_idx+1}"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p79-84: 3 Practical Workplace Form-Filling Mocks (6 pages: 2 pages each)
    mock_tasks = [
        ("College Enrolment &amp; Registration Form", "Fill in your personal details, preferred course, and emergency contact."),
        ("Workplace Holiday Request Form", "State the dates you wish to book, your team, and supervisor approval."),
        ("Doctor's Appointment Slip &amp; Medical Note", "Record your symptom, requested appointment time, and contact phone number.")
    ]

    for m_idx, (m_title, m_desc) in enumerate(mock_tasks):
        m_body_1 = (
            K.page_title(f"Mock Writing Task {m_idx+1}", kicker="Practical Writing &bull; 10 Marks", badge=f"M{m_idx+1}")
            + K.box_html(
                f"<p>{m_desc}</p>"
                f"<div style='border:2px solid var(--soft); border-radius:6px; padding:3mm; background:#fff; margin-top:2mm;'>"
                f"<div style='margin-bottom:2mm;'><b>First Name:</b> ____________________ &nbsp;&nbsp;&nbsp; <b>Surname:</b> ____________________</div>"
                f"<div style='margin-bottom:2mm;'><b>Date of Birth:</b> ____ / ____ / ______ &nbsp;&nbsp;&nbsp; <b>Postcode:</b> ____________</div>"
                f"<div style='margin-bottom:2mm;'><b>Reason for Application / Request:</b></div>"
                f"<div style='height:12mm; border-bottom:1.5px solid var(--line);'></div>"
                f"</div>",
                title=f"Official Form Template: {m_title}"
            )
            + K.tip_pair("Use neat block capital letters where asked.", "Always check your phone number and postcode digits.",
                         golden_title="Form Tip", watch_title="Check Carefully")
            + K.fill_lines("Practice Notes for Form Details", min_mm=36, gap_mm=10)
        )
        pages.append(K.page(m_body_1, header=(BOOK, f"Mock Form {m_idx+1} &bull; Template"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        m_body_2 = (
            K.page_title(f"Mock Task {m_idx+1} &bull; Lined Writing Booklet", kicker="Writing Response Page")
            + K.fill_lines("Write your extended response or notes below:", min_mm=190, gap_mm=11)
        )
        pages.append(K.page(m_body_2, header=(BOOK, f"Mock Form {m_idx+1} &bull; Writing"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Reference Back Matter via K.ref_pages (Condensed Black Reference Style)
    ref_blocks = []

    # 1. Diagnostic Answers
    p75 = a_e3.ANSWER_KEY_DATA.get('page_75', {})
    if 'diagnostic_answers' in p75:
        qa_diag = "".join(f"<div class='qa'><span class='q-num'>{q}</span><span class='q-ans'><b>{ans}</b>: {escape_html(exp)}</span></div>" for q, ans, exp in p75['diagnostic_answers'])
        ref_blocks.append(K.ref_block("Diagnostic Assessment Worked Solutions (Questions 1–10)", qa_diag))

    # 2. Units 1 to 24 Worked Solutions
    for k in sorted(a_e3.ANSWER_KEY_DATA.keys()):
        data = a_e3.ANSWER_KEY_DATA[k]
        if 'units' in data:
            for unum, uinfo in sorted(data['units'].items()):
                ex1 = "<br>".join(escape_html(s) for s in uinfo.get('ex1', []))
                ex2 = "<br>".join(escape_html(s) for s in uinfo.get('ex2', []))
                u_html = f"<div style='margin-bottom:1.5mm;'><b>Exercise 1:</b><br>{ex1}</div><div><b>Exercise 2:</b><br>{ex2}</div>"
                ref_blocks.append(K.ref_block(f"Unit {unum} Worked Solutions", u_html))

    # 3. Workouts
    p80 = a_e3.ANSWER_KEY_DATA.get('page_80', {})
    if 'workouts' in p80:
        w_parts = []
        for w, ans in sorted(p80['workouts'].items()):
            if isinstance(ans, dict):
                e_list = "<br>".join(escape_html(e) for e in ans.get('errors', []))
                x_list = "<br>".join(escape_html(x) for x in ans.get('expansion', []))
                w_parts.append(f"<div style='margin-bottom:1.5mm;'><b>Workout {w}:</b><br>{e_list}<br><em>Model Expansion:</em> {x_list}</div>")
            else:
                w_parts.append(f"<div style='margin-bottom:1.5mm;'><b>Workout {w}:</b> {escape_html(ans)}</div>")
        ref_blocks.append(K.ref_block("Sentence Building Workouts (1–6)", "".join(w_parts)))

    # 4. Form-Filling Exemplars
    if 'writing_exemplars' in p80:
        f_html = "".join(f"<div style='margin-bottom:1.5mm;'><b>Form {f}:</b> {escape_html(ans)}</div>" for f, ans in sorted(p80['writing_exemplars'].items()))
        ref_blocks.append(K.ref_block("Workplace Form-Filling Exemplar Answers", f_html))

    # 5. Phonics & High Frequency Rules
    phonics_rules = [
        ("Prefix 'Un-'", "Changes meaning to not or opposite: unwell, unhappy, unlock, unfair."),
        ("Prefix 'Re-'", "Means do again: rebuild, rewrite, restart, refill."),
        ("Suffix '-ful'", "Means full of (helpful, careful, painful). Only one 'l'."),
        ("Suffix '-less'", "Means without (careless, helpless, painless)."),
        ("Silent Letters", "Silent 'k' in knife, knee, knock; silent 'w' in write, wrong, wrist; silent 'g' in sign, high.")
    ]
    ph_html = "".join(f"<dl><dt>{escape_html(t)}</dt><dd>{escape_html(d)}</dd></dl>" for t, d in phonics_rules)
    ref_blocks.append(K.ref_block("Annexe D Phonics &amp; Spelling Rules", ph_html))

    # 6. Index
    index_e3 = [
        ("A", [("Alphabetical order", "8"), ("Annexe D spelling words", "50"), ("Apostrophes in contractions", "24")]),
        ("C", [("Capital letters", "10"), ("Commas in lists", "14"), ("Conjunctions (and, but)", "16")]),
        ("D", [("Double consonants", "52")]),
        ("E", [("Exclamation marks", "12")]),
        ("F", [("Full stops", "10")]),
        ("H", [("Homophones (to/too/two)", "46")]),
        ("P", [("Paragraphs", "20"), ("Past tense regular verbs", "18")]),
        ("Q", [("Question marks", "12")]),
        ("S", [("Silent letters (k, w, g)", "54"), ("Subject-verb agreement", "22")]),
        ("W", [("Workplace form-filling", "74")])
    ]
    ix_html = ""
    for letter, entries in index_e3:
        items = "".join(f"<div class='ix'><span>{escape_html(t)}</span><span>{escape_html(p)}</span></div>" for t, p in entries)
        ix_html += f"<div class='ix-letter'>{letter}</div>{items}"
    ref_blocks.append(K.ref_block("Entry Level 3 Subject &amp; Grammar Index", ix_html))

    cover_theme = K.theme_from_cover(front_cov)
    ref_page_list = K.ref_pages("SPaG Entry Level 3 Reference: Solutions &amp; Index", ref_blocks,
                                BOOK, start_page=p_curr, subtitle="Worked Solutions &amp; Phonics Guide",
                                cols=2, theme=cover_theme, notes_title="Candidate SPaG Revision Log")
    pages.extend(ref_page_list)
    p_curr += len(ref_page_list)

    # Candidate Progress Tracker
    p_audit_body = (
        K.page_title("Candidate SPaG Progress Tracker &amp; Sticker Chart", kicker="Entry Level 3 Achievement", badge="SUCCESS")
        + K.box_html(
            "<p>Check off your skills as you complete each SPaG unit:</p>"
            + K.bullets([
                "Every sentence begins with a capital letter and ends with a full stop.",
                "Questions always end with a question mark.",
                "Can spell everyday Annexe D words correctly using phonics rules."
            ]),
            title="Entry Level 3 SPaG Success Targets"
        )
        + K.fill_notes("Personal Success Notes &amp; Tutor Endorsements", min_mm=45)
    )
    pages.append(K.page(p_audit_body, header=(BOOK, "Progress Tracker"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Duplex even-page balance check before back cover
    if (len(pages) + 1) % 2 != 0:
        p_ibc_body = (
            K.page_title("Candidate SPaG Certificate &amp; Tutor Endorsement", kicker="Entry Level 3 Achievement", badge="STAR")
            + K.box_html(
                "<p>Well done on completing all 24 SPaG units! Remember these three golden rules every time you write:</p>"
                + K.bullets([
                    "<b>Start with a Capital Letter:</b> Every sentence begins with a big capital letter.",
                    "<b>End with a Full Stop:</b> Stop your sentence with a clean dot (.) or question mark (?).",
                    "<b>Sound It Out:</b> Break long words into small syllables when checking spelling."
                ]),
                title="Entry Level 3 Star Writer Declaration"
            )
            + K.tip_pair("Keep practicing your spelling word banks every day.",
                         "Always read your sentence out loud to check it makes sense.",
                         golden_title="Reading Check", watch_title="Golden Habit")
            + K.fill_notes("Tutor Endorsement &amp; Candidate Next Steps", min_mm=30)
        )
        pages.append(K.page(p_ibc_body, header=(BOOK, "Tutor Endorsement"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Back Cover
    pages.append(K.back_cover(back_cov))

    print(f"Total Pages Assembled: {len(pages)}")
    out_pdf = DOWNLOADS / "MasterFunctionalSkills_SPaG_Entry_Level_3_Mastery.pdf"
    res = K.render_pdf(pages, out_pdf, theme=K.theme_from_cover(front_cov), entry3=True, title="Master Functional Skills - SPaG Entry Level 3 Mastery")
    print(f"Rendered: {res['pdf']}")

    shutil.copyfile(out_pdf, DOCUMENTS / out_pdf.name)
    rep = K.qa_report(out_pdf, dpi=50)
    K.print_report(rep)
    return rep


if __name__ == "__main__":
    rep_l2 = build_spag_l2()
    rep_l1 = build_spag_l1()
    rep_e3 = build_spag_e3()
    print("\nSPaG Suite Build Complete: All 3 levels generated!")
