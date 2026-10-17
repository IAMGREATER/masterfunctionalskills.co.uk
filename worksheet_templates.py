#!/usr/bin/env python3
"""
Master Functional Skills - Standardized HTML Templates for Worksheets & Tutor Answer Keys.
Designed for high legibility, dyslexia accessibility, A4 print optimization, and Pearson Edexcel alignment.
"""

import re

def clean_sub_piece(text):
    text = re.sub(r"£\s*_+", "<span class=\"q-unit-prefix\">£</span><div class=\"q-answer-input-box sm\"></div>", text)
    text = re.sub(r"_+", "<div class=\"q-answer-input-box sm\"></div>", text)
    return text

def render_clean_answer_row(label, raw_box):
    b = (raw_box or "").strip()
    if "in the workspace" in b.lower():
        return f"""<div class="q-answer-row">
        <span class="q-workspace-badge"><i class="fa-solid fa-pen-to-square"></i> {b}</span>
      </div>"""
    if re.fullmatch(r"_+", b):
        width_cls = "lg" if len(b) > 30 else "md"
        lbl_html = f"<span class=\"q-answer-label\">{label}</span>" if label else ""
        return f"""<div class="q-answer-row">
        {lbl_html}
        <div class="q-answer-input-box {width_cls}"></div>
      </div>"""
    m_pound = re.fullmatch(r"£\s*_+(?:\s*\(([^)]+)\))?", b)
    if m_pound:
        extra = f" <span class=\"q-unit-suffix\">({m_pound.group(1)})</span>" if m_pound.group(1) else ""
        lbl_html = f"<span class=\"q-answer-label\">{label}</span>" if label else ""
        return f"""<div class="q-answer-row">
        {lbl_html}
        <span class="q-unit-prefix">£</span>
        <div class="q-answer-input-box md"></div>{extra}
      </div>"""
    m_suffix = re.fullmatch(r"_+\s+([a-zA-Z0-9%²³°/ -]+)", b)
    if m_suffix:
        unit = m_suffix.group(1).strip()
        lbl_html = f"<span class=\"q-answer-label\">{label}</span>" if label else ""
        return f"""<div class="q-answer-row">
        {lbl_html}
        <div class="q-answer-input-box md"></div>
        <span class="q-unit-suffix">{unit}</span>
      </div>"""
    if b in ["1 : ____", "____ : ____"] or re.fullmatch(r"1\s*:\s*_+", b) or re.fullmatch(r"_+\s*:\s*_+", b):
        lbl_html = f"<span class=\"q-answer-label\">{label}</span>" if label else ""
        if b.startswith("1"):
            return f"""<div class="q-answer-row">
        {lbl_html}
        <span class="q-unit-prefix">1 :</span>
        <div class="q-answer-input-box xs"></div>
      </div>"""
        else:
            return f"""<div class="q-answer-row">
        {lbl_html}
        <div class="q-answer-input-box xs"></div>
        <span class="q-unit-prefix">:</span>
        <div class="q-answer-input-box xs"></div>
      </div>"""
    m_order = re.match(r"(Smallest|Largest|Lightest|Heaviest|1st):\s*_\+\s+(?:to\s+|(?:to\s+))?(Largest|Smallest|Heaviest|Lightest|5th):\s*_\+", b)
    if m_order:
        lbl_html = f"<span class=\"q-answer-label\">{label}</span>" if label else ""
        from_lbl, to_lbl = m_order.group(1), m_order.group(2)
        return f"""<div class="q-answer-row">
        {lbl_html}
        <span class="q-answer-sublabel">{from_lbl}:</span>
        <div class="q-answer-input-box md"></div>
        <span class="q-answer-separator">&rarr;</span>
        <span class="q-answer-sublabel">{to_lbl}:</span>
        <div class="q-answer-input-box md"></div>
      </div>"""
    pills_match = re.match(r"^(Correct\s*/\s*Incorrect|Yes\s*/\s*No|Valid\s*/\s*Flawed|Sufficient\s*/\s*Insufficient|Justified\s*/\s*Not Justified)(?::\s*(.*))?$", b, re.IGNORECASE)
    if pills_match:
        opts_str = pills_match.group(1)
        rest = pills_match.group(2) or ""
        pills_html = " / ".join([f"<span class=\"pill-opt\">{opt.strip()}</span>" for opt in opts_str.split("/")])
        pills_container = f"<div class=\"q-choice-pills\"><span class=\"pills-title\">Decision:</span> {pills_html}</div>"
        rest_cleaned = clean_sub_piece(rest)
        lbl_html = f"<span class=\"q-answer-label\">{label}</span>" if label and label != "Decision & Rounded Value =" else ""
        return f"""<div class="q-answer-row">
        {lbl_html}
        {pills_container}
        {rest_cleaned}
      </div>"""
    if "|" in b:
        lbl_html = f"<span class=\"q-answer-label\">{label}</span>" if label else ""
        items = b.split("|")
        rendered_items = [clean_sub_piece(it.strip()) for it in items]
        joined = " <span class=\"q-item-sep\">|</span> ".join(rendered_items)
        return f"""<div class="q-answer-row">
        {lbl_html}
        {joined}
      </div>"""
    if b.startswith("Although"):
        return f"""<div class="q-answer-row q-answer-row-multiline">
        <span class="q-answer-sublabel">Although:</span>
        <div class="q-answer-line-fill"></div>
      </div>"""
    lbl_html = f"<span class=\"q-answer-label\">{label}</span>" if label else ""
    cleaned = clean_sub_piece(b)
    return f"""<div class="q-answer-row">
        {lbl_html}
        {cleaned}
      </div>"""

def render_worksheet(data):
    title = data['title']
    slug = data['slug']
    subject = data.get('subject', 'Mathematics')
    spec_codes = data.get('spec_codes', 'Pearson Edexcel Functional Skills')
    formula_hint = data.get('formula_hint', 'Show full step-by-step working out to secure method marks.')
    back_url = data.get('back_url', f"../functional-skills-{slug}.html")
    ans_url = f"{slug}-answers.html"
    total_marks = data.get('total_marks', 18)
    
    # Render sections
    sections_html = ""
    for sec in data.get('sections', []):
        sec_title = sec['title']
        sec_meta = sec.get('meta', '')
        sections_html += f"""
    <!-- {sec_title} -->
    <div class="tier-header">
      <span>{sec_title}</span>
      <span class="tier-marks">{sec_meta}</span>
    </div>
"""
        for q in sec['questions']:
            diagram_html = ""
            if q.get('svg'):
                diagram_html = f"""
      <div class="q-diagram-wrap">
        {q['svg']}
      </div>"""
            
            lines_count = q.get('lines', 4)
            lines_divs = "\n".join(["          <div class=\"working-line\"></div>" for _ in range(lines_count)])
            
            unit_str = f" {q['unit']}" if q.get('unit') else ""
            ans_box_val = f"_____________{unit_str}" if not q.get('choice_box') else q.get('choice_box')
            ans_label = q.get('ans_label', 'Answer =')

            sections_html += f"""
    <div class="q-card">
      <div class="q-card-head">
        <span class="q-title">{q['title']}</span>
        <span class="q-marks">[{q['marks']} Marks]</span>
      </div>
      <div class="q-stem">
        {q['stem']}
      </div>{diagram_html}
      <div class="q-working-area">
        <div class="working-label">Show your full working out here:</div>
        <div class="working-lines-box">
{lines_divs}
        </div>
      </div>
      {render_clean_answer_row(ans_label, ans_box_val)}
    </div>
"""

    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Master Functional Skills — {title} Worksheet (Level 1 & Level 2)</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    @page {{
      size: A4 portrait;
      margin: 12mm 15mm 12mm 15mm;
    }}
    *, *::before, *::after {{
      box-sizing: border-box;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      color: #0f172a;
      background: #f8fafc;
      margin: 0;
      padding: 0;
      font-size: 11pt;
      line-height: 1.5;
    }}
    .print-bar {{
      background: #0b172d;
      color: #f8fafc;
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 1000;
      box-shadow: 0 2px 10px rgba(0,0,0,0.15);
    }}
    .print-bar a {{
      color: #93c5fd;
      text-decoration: none;
      font-weight: 600;
      font-size: 0.95rem;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }}
    .print-bar a:hover {{
      color: #ffffff;
      text-decoration: underline;
    }}
    .btn-action-print {{
      background: #2563eb;
      color: #ffffff;
      border: none;
      padding: 8px 20px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.95rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: background 0.2s;
    }}
    .btn-action-print:hover {{
      background: #1d4ed8;
    }}
    .btn-action-mode,
    .btn-action-answers,
    .btn-action-practice,
    .btn-action-mode,
    .btn-action-answers,
    .btn-action-practice,
    .btn-action-sheet {{
      color: #ffffff !important;
      border: none;
      padding: 8px 18px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.95rem;
      text-decoration: none !important;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      margin-right: 12px;
      transition: background 0.2s;
    }}
    .old-btn-action-sheet {{
      color: #ffffff !important;
      border: none;
      padding: 8px 18px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.95rem;
      text-decoration: none !important;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      margin-right: 12px;
      transition: background 0.2s;
    }}
    .old-btn-action-answers {{
      background: #059669;
      color: #ffffff;
      border: none;
      padding: 8px 18px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.95rem;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      margin-right: 12px;
    }}
    .btn-action-answers:hover {{
      background: #047857;
    }}
    .nav-pill-group {{
      display: inline-flex;
      align-items: center;
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.22);
      border-radius: 8px;
      padding: 3px;
      margin-right: 12px;
      vertical-align: middle;
    }}
    .nav-pill-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      padding: 6px 0;
      width: 115px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.88rem;
      color: #cbd5e1;
      text-decoration: none;
      transition: all 0.15s ease-in-out;
      cursor: pointer;
      white-space: nowrap;
      user-select: none;
      border: none;
      background: transparent;
      box-sizing: border-box;
    }}
    .nav-pill-btn:hover:not(.active) {{
      background: rgba(255, 255, 255, 0.18);
      color: #ffffff;
      text-decoration: none;
    }}
    .nav-pill-btn.active {{
      background: #2563eb;
      color: #ffffff;
      cursor: default;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.25);
    }}


    @media (max-width: 900px) {{
      .print-bar {{
        padding: 10px 14px;
        flex-direction: column;
        align-items: stretch;
        gap: 8px;
      }}
      .print-bar > div:first-child {{
        text-align: center;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }}
      .print-bar > div:first-child a {{
        font-size: 0.85rem;
        display: inline-flex;
        max-width: 100%;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
      }}
      .print-bar > div:last-child {{
        display: flex;
        align-items: center;
        justify-content: center;
        flex-wrap: wrap;
        gap: 6px;
      }}
      .print-bar > div:last-child > * {{
        margin-right: 0 !important;
      }}
      .btn-action-mode,
      .btn-action-practice,
      .btn-action-answers,
      .btn-action-sheet,
      .btn-action-print {{
        padding: 6px 12px;
        font-size: 0.85rem;
      }}
      .nav-pill-group {{
        margin-right: 0;
      }}
      .nav-pill-btn {{
        width: 100px;
        font-size: 0.82rem;
        padding: 5px 0;
      }}
    }}
    @media (max-width: 480px) {{
      .print-bar > div:last-child {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 6px;
      }}
      .nav-pill-group {{
        grid-column: span 2;
        width: 100%;
      }}
      .nav-pill-btn {{
        flex: 1;
        width: auto;
      }}
      .btn-action-mode,
      .btn-action-practice,
      .btn-action-answers,
      .btn-action-sheet,
      .btn-action-print {{
        justify-content: center;
        width: 100%;
      }}
    }}
    @media print {{
      .print-bar {{
        display: none !important;
      }}
      body {{
        background: #ffffff !important;
      }}
      .page-sheet {{
        box-shadow: none !important;
        border: none !important;
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
      }}
      .q-card {{
        page-break-inside: avoid;
      }}
    }}

    .page-sheet {{
      max-width: 860px;
      margin: 24px auto;
      background: #ffffff;
      padding: 32px 40px;
      border-radius: 8px;
      border: 1px solid #e2e8f0;
      box-shadow: 0 4px 20px rgba(0,0,0,0.06);
    }}
    .sheet-head {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      border-bottom: 2.5px solid #0b172d;
      padding-bottom: 16px;
      margin-bottom: 20px;
    }}
    .brand-title {{
      font-size: 1.45rem;
      font-weight: 900;
      color: #0b172d;
      letter-spacing: -0.5px;
    }}
    .brand-title span {{
      color: #2563eb;
    }}
    .brand-subtitle {{
      font-size: 0.88rem;
      color: #64748b;
      margin-top: 2px;
      font-weight: 500;
    }}
    .sheet-meta-badge {{
      background: #eff6ff;
      border: 1.5px solid #bfdbfe;
      color: #1e40af;
      padding: 8px 16px;
      border-radius: 6px;
      text-align: right;
    }}
    .sheet-meta-badge .topic-name {{
      font-size: 1.15rem;
      font-weight: 800;
      display: block;
    }}
    .sheet-meta-badge .spec-tag {{
      font-size: 0.78rem;
      color: #3b82f6;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .learner-bar {{
      display: grid;
      grid-template-columns: 2.5fr 1.5fr 1fr;
      gap: 16px;
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      padding: 10px 16px;
      margin-bottom: 20px;
      font-size: 0.95rem;
    }}
    .learner-bar-item strong {{
      color: #0b172d;
    }}
    .dotted-line {{
      display: inline-block;
      width: 65%;
      border-bottom: 1.5px dotted #94a3b8;
      height: 12px;
      margin-left: 6px;
    }}

    .recall-banner {{
      background: #fffbeb;
      border-left: 4px solid #f59e0b;
      border-radius: 4px;
      padding: 10px 14px;
      margin-bottom: 24px;
      font-size: 0.92rem;
      color: #78350f;
      display: flex;
      align-items: flex-start;
      gap: 10px;
    }}
    .recall-banner i {{
      font-size: 1.1rem;
      margin-top: 2px;
      color: #d97706;
    }}

    .tier-header {{
      background: #f1f5f9;
      border-left: 4px solid #2563eb;
      padding: 6px 12px;
      font-size: 0.92rem;
      font-weight: 800;
      color: #0b172d;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin: 24px 0 16px 0;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .tier-header .tier-marks {{
      font-size: 0.8rem;
      font-weight: 700;
      color: #2563eb;
      background: #ffffff;
      padding: 2px 8px;
      border-radius: 4px;
      border: 1px solid #cbd5e1;
    }}

    .q-card {{
      border: 1.5px solid #cbd5e1;
      border-radius: 8px;
      padding: 18px 20px;
      margin-bottom: 22px;
      background: #ffffff;
    }}
    .q-card-head {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #e2e8f0;
      padding-bottom: 8px;
      margin-bottom: 12px;
    }}
    .q-title {{
      font-weight: 800;
      color: #0b172d;
      font-size: 1rem;
    }}
    .q-marks {{
      font-weight: 700;
      color: #2563eb;
      font-size: 0.88rem;
      background: #eff6ff;
      padding: 3px 10px;
      border-radius: 4px;
      border: 1px solid #bfdbfe;
    }}
    .q-stem {{
      font-size: 1.02rem;
      color: #0f172a;
      line-height: 1.6;
      margin-bottom: 14px;
    }}

    .q-diagram-wrap {{
      text-align: center;
      margin: 14px 0;
      padding: 10px;
      background: #faf8f2;
      border: 1px dashed #cbd5e1;
      border-radius: 6px;
    }}
    .q-diagram-wrap svg {{
      max-width: 100%;
      height: auto;
    }}

    .q-working-area {{
      margin: 14px 0;
      background: #ffffff;
    }}
    .working-label {{
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: #64748b;
      font-weight: 700;
      margin-bottom: 4px;
    }}
    .working-lines-box {{
      border: 1px solid #e2e8f0;
      border-radius: 4px;
      background: #ffffff;
      padding: 0 10px;
    }}
    .working-line {{
      height: 24px;
      border-bottom: 1px dashed #e2e8f0;
    }}
    .working-line:last-child {{
      border-bottom: none;
    }}

    .q-answer-row {{
      display: flex;
      justify-content: flex-end;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px 12px;
      margin-top: 14px;
      padding-top: 12px;
      border-top: 1px solid #e2e8f0;
    }}
    .q-answer-label {{
      font-weight: 700;
      color: #0b172d;
      font-size: 0.95rem;
    }}
    .q-answer-sublabel {{
      font-weight: 600;
      color: #1e293b;
      font-size: 0.9rem;
    }}
    .q-unit-prefix, .q-unit-suffix {{
      font-weight: 700;
      color: #0b172d;
      font-size: 1.05rem;
    }}
    .q-item-sep {{
      color: #cbd5e1;
      font-weight: 400;
      margin: 0 4px;
    }}
    .q-answer-separator {{
      font-weight: 600;
      color: #64748b;
      font-size: 1.05rem;
    }}
    .q-choice-pills {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 10px;
      background: #f8fafc;
      border: 1.5px solid #cbd5e1;
      border-radius: 6px;
      font-size: 0.85rem;
      font-weight: 600;
      color: #334155;
    }}
    .pills-title {{
      color: #64748b;
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    .pill-opt {{
      padding: 2px 6px;
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 4px;
      color: #0f172a;
    }}
    .q-workspace-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 12px;
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      border-radius: 6px;
      color: #1d4ed8;
      font-weight: 600;
      font-size: 0.88rem;
    }}
    .q-answer-input-box {{
      border: 2px solid #0b172d;
      border-radius: 5px;
      background: #ffffff;
      height: 38px;
      min-width: 140px;
      box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05);
      display: inline-block;
      vertical-align: middle;
    }}
    .q-answer-input-box.xs {{ min-width: 65px; }}
    .q-answer-input-box.sm {{ min-width: 105px; }}
    .q-answer-input-box.md {{ min-width: 160px; }}
    .q-answer-input-box.lg {{ min-width: 240px; }}
    .q-answer-row-multiline {{
      width: 100%;
      display: flex;
      align-items: flex-end;
      gap: 12px;
    }}
    .q-answer-line-fill {{
      flex: 1;
      height: 28px;
      border-bottom: 2px solid #0b172d;
    }}

    .sheet-footer {{
      border-top: 1px solid #e2e8f0;
      padding-top: 14px;
      margin-top: 30px;
      display: flex;
      justify-content: space-between;
      color: #94a3b8;
      font-size: 0.8rem;
    }}
  </style>
</head>
<body>

  <div class="print-bar">
    <div>
      <a href="{back_url}"><i class="fa-solid fa-arrow-left"></i> Back to {title} Revision Guide</a>
    </div>
    <div>
      <a href="{slug}-workout.html" class="btn-action-answers" style="background:#2563eb; margin-right:10px;"><i class="fa-solid fa-repeat"></i> Switch to Skill Workout</a>
      <div class="nav-pill-group">
        <span class="nav-pill-btn active"><i class="fa-solid fa-file-lines"></i> Questions</span>
        <a href="{ans_url}" class="nav-pill-btn"><i class="fa-solid fa-check-double"></i> Answers</a>
      </div>
      <button type="button" class="btn-action-print" onclick="window.print()"><i class="fa-solid fa-print"></i> Print / Save to PDF</button>
    </div>
  </div>

  <div class="page-sheet">
    <div class="sheet-head">
      <div>
        <div class="brand-title">MASTER<span>FUNCTIONALSKILLS</span></div>
        <div class="brand-subtitle">Ofqual Regulated Standards • {subject} Curriculum</div>
      </div>
      <div class="sheet-meta-badge">
        <span class="topic-name">{title}</span>
        <span class="spec-tag">{spec_codes}</span>
      </div>
    </div>

    <div class="learner-bar">
      <div class="learner-bar-item"><strong>Learner:</strong> <span class="dotted-line"></span></div>
      <div class="learner-bar-item"><strong>Date:</strong> <span class="dotted-line"></span></div>
      <div class="learner-bar-item" style="text-align:right;"><strong>Score:</strong> _____ / {total_marks}</div>
    </div>

    <div class="recall-banner">
      <i class="fa-solid fa-lightbulb"></i>
      <div>
        <strong>Examiner Rule for {title}:</strong> {formula_hint}
      </div>
    </div>

{sections_html}

    <div class="sheet-footer">
      <div>Master Functional Skills • Pearson Edexcel Curriculum Aligned • 100% Original IP</div>
      <div>Page 1 of 1 • Rev 2026.1</div>
    </div>
  </div>
</body>
</html>"""


def render_answers(data):
    title = data['title']
    slug = data['slug']
    subject = data.get('subject', 'Mathematics')
    spec_codes = data.get('spec_codes', 'Pearson Edexcel Functional Skills')
    back_url = data.get('back_url', f"../functional-skills-{slug}.html")
    sheet_url = f"{slug}-worksheet.html"
    total_marks = data.get('total_marks', 18)
    
    sections_html = ""
    for sec in data.get('sections', []):
        sec_title = sec['title']
        sec_meta = sec.get('meta', '')
        sections_html += f"""
    <div class="tier-divider">
      <span>{sec_title} Solutions</span>
      <span>{sec_meta}</span>
    </div>
"""
        for q in sec['questions']:
            steps_rows = ""
            for desc, code in q.get('step_rows', []):
                steps_rows += f"""
        <div class="step-row">
          <span>{desc}</span>
          <span class="mark-code">{code}</span>
        </div>"""
            
            pitfall_html = ""
            if q.get('pitfall'):
                pitfall_html = f"""
      <div class="pitfall-box">
        <strong>⚠️ Examiner Trap Alert:</strong>
        {q['pitfall']}
      </div>"""
            
            alt_html = ""
            if q.get('alt_method'):
                alt_html = f"""
      <div class="alt-method-box">
        <strong>💡 Alternative Method:</strong>
        {q['alt_method']}
      </div>"""
            
            reverse_html = ""
            if q.get('reverse_check'):
                reverse_html = f"""
      <div class="reverse-check-box">
        <strong>🔄 Reverse Sanity Check:</strong> {q['reverse_check']}
      </div>"""

            sections_html += f"""
    <div class="ans-card">
      <div class="ans-card-head">
        <span class="ans-q-num">{q['title']} Model Solution</span>
        <span class="ans-marks-badge">[{q['marks']} Marks Total]</span>
      </div>
      <div class="ans-stem-quote">
        {q['stem']}
      </div>
      <div class="mark-steps-box">
        <div class="step-title">Step-by-Step Marking Criteria:</div>
{steps_rows}
      </div>
      <div class="final-award-box">
        <span class="award-label">Award Final Answer Mark:</span>
        <span class="award-val">{q['final_answer']}</span>
      </div>{pitfall_html}{alt_html}{reverse_html}
    </div>
"""

    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Master Functional Skills — {title} Answer Key & Mark Scheme (Level 1 & Level 2)</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    @page {{
      size: A4 portrait;
      margin: 12mm 15mm 12mm 15mm;
    }}
    *, *::before, *::after {{
      box-sizing: border-box;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      color: #0f172a;
      background: #f0fdf4;
      margin: 0;
      padding: 0;
      font-size: 11pt;
      line-height: 1.5;
    }}
    .print-bar {{
      background: #064e3b;
      color: #f8fafc;
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 1000;
      box-shadow: 0 2px 10px rgba(0,0,0,0.15);
    }}
    .print-bar a {{
      color: #a7f3d0;
      text-decoration: none;
      font-weight: 600;
      font-size: 0.95rem;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }}
    .print-bar a:hover {{
      color: #ffffff;
      text-decoration: underline;
    }}
    .btn-action-print {{
      background: #10b981;
      color: #ffffff;
      border: none;
      padding: 8px 20px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.95rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: background 0.2s;
    }}
    .btn-action-print:hover {{
      background: #059669;
    }}
    .btn-action-mode,
    .btn-action-answers,
    .btn-action-practice,
    .btn-action-sheet {{
      color: #ffffff !important;
      border: none;
      padding: 8px 18px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.95rem;
      text-decoration: none !important;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      margin-right: 12px;
      transition: background 0.2s;
    }}
    .old-btn-action-sheet {{
      background: #2563eb;
      color: #ffffff;
      border: none;
      padding: 8px 18px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.95rem;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      margin-right: 12px;
    }}
    .btn-action-sheet:hover {{
      background: #1d4ed8;
    }}
    .nav-pill-group {{
      display: inline-flex;
      align-items: center;
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.22);
      border-radius: 8px;
      padding: 3px;
      margin-right: 12px;
      vertical-align: middle;
    }}
    .nav-pill-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      padding: 6px 0;
      width: 115px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.88rem;
      color: #cbd5e1;
      text-decoration: none;
      transition: all 0.15s ease-in-out;
      cursor: pointer;
      white-space: nowrap;
      user-select: none;
      border: none;
      background: transparent;
      box-sizing: border-box;
    }}
    .nav-pill-btn:hover:not(.active) {{
      background: rgba(255, 255, 255, 0.18);
      color: #ffffff;
      text-decoration: none;
    }}
    .nav-pill-btn.active {{
      background: #059669;
      color: #ffffff;
      cursor: default;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.25);
    }}


    @media (max-width: 900px) {{
      .print-bar {{
        padding: 10px 14px;
        flex-direction: column;
        align-items: stretch;
        gap: 8px;
      }}
      .print-bar > div:first-child {{
        text-align: center;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }}
      .print-bar > div:first-child a {{
        font-size: 0.85rem;
        display: inline-flex;
        max-width: 100%;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
      }}
      .print-bar > div:last-child {{
        display: flex;
        align-items: center;
        justify-content: center;
        flex-wrap: wrap;
        gap: 6px;
      }}
      .print-bar > div:last-child > * {{
        margin-right: 0 !important;
      }}
      .btn-action-mode,
      .btn-action-practice,
      .btn-action-answers,
      .btn-action-sheet,
      .btn-action-print {{
        padding: 6px 12px;
        font-size: 0.85rem;
      }}
      .nav-pill-group {{
        margin-right: 0;
      }}
      .nav-pill-btn {{
        width: 100px;
        font-size: 0.82rem;
        padding: 5px 0;
      }}
    }}
    @media (max-width: 480px) {{
      .print-bar > div:last-child {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 6px;
      }}
      .nav-pill-group {{
        grid-column: span 2;
        width: 100%;
      }}
      .nav-pill-btn {{
        flex: 1;
        width: auto;
      }}
      .btn-action-mode,
      .btn-action-practice,
      .btn-action-answers,
      .btn-action-sheet,
      .btn-action-print {{
        justify-content: center;
        width: 100%;
      }}
    }}
    @media print {{
      .print-bar {{
        display: none !important;
      }}
      body {{
        background: #ffffff !important;
      }}
      .page-sheet {{
        box-shadow: none !important;
        border: none !important;
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
      }}
      .ans-card {{
        page-break-inside: avoid;
      }}
    }}

    .page-sheet {{
      max-width: 860px;
      margin: 24px auto;
      background: #ffffff;
      padding: 32px 40px;
      border-radius: 8px;
      border: 1px solid #bbf7d0;
      box-shadow: 0 4px 20px rgba(0,0,0,0.06);
    }}
    .sheet-head {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      border-bottom: 2.5px solid #064e3b;
      padding-bottom: 16px;
      margin-bottom: 20px;
    }}
    .brand-title {{
      font-size: 1.45rem;
      font-weight: 900;
      color: #064e3b;
      letter-spacing: -0.5px;
    }}
    .brand-title span {{
      color: #10b981;
    }}
    .brand-subtitle {{
      font-size: 0.88rem;
      color: #047857;
      margin-top: 2px;
      font-weight: 600;
    }}
    .sheet-meta-badge {{
      background: #ecfdf5;
      border: 1.5px solid #a7f3d0;
      color: #065f46;
      padding: 8px 16px;
      border-radius: 6px;
      text-align: right;
    }}
    .sheet-meta-badge .topic-name {{
      font-size: 1.15rem;
      font-weight: 800;
      display: block;
    }}
    .sheet-meta-badge .spec-tag {{
      font-size: 0.78rem;
      color: #059669;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .scheme-summary-bar {{
      background: #f0fdf4;
      border: 1px solid #86efac;
      border-radius: 6px;
      padding: 12px 18px;
      margin-bottom: 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.95rem;
      color: #065f46;
    }}

    .tier-divider {{
      background: #f0fdf4;
      border-left: 4px solid #059669;
      padding: 6px 12px;
      font-size: 0.92rem;
      font-weight: 800;
      color: #064e3b;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin: 24px 0 16px 0;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .ans-card {{
      border: 1.5px solid #cbd5e1;
      border-radius: 8px;
      padding: 18px 20px;
      margin-bottom: 24px;
      background: #ffffff;
    }}
    .ans-card-head {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #e2e8f0;
      padding-bottom: 8px;
      margin-bottom: 12px;
    }}
    .ans-q-num {{
      font-weight: 800;
      color: #064e3b;
      font-size: 1.05rem;
    }}
    .ans-marks-badge {{
      font-weight: 700;
      color: #047857;
      background: #ecfdf5;
      padding: 3px 10px;
      border-radius: 4px;
      border: 1px solid #a7f3d0;
      font-size: 0.88rem;
    }}
    .ans-stem-quote {{
      font-size: 0.94rem;
      color: #475569;
      background: #f8fafc;
      border-left: 3px solid #cbd5e1;
      padding: 8px 12px;
      margin-bottom: 14px;
      font-style: italic;
    }}

    .mark-steps-box {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 14px 16px;
      margin-bottom: 14px;
    }}
    .step-title {{
      font-weight: 800;
      color: #0f172a;
      font-size: 0.9rem;
      margin-bottom: 8px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .step-row {{
      margin-bottom: 8px;
      line-height: 1.6;
      font-size: 0.98rem;
      color: #1e293b;
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      border-bottom: 1px dashed #f1f5f9;
      padding-bottom: 6px;
    }}
    .step-row:last-child {{
      border-bottom: none;
      padding-bottom: 0;
      margin-bottom: 0;
    }}
    .mark-code {{
      font-weight: 800;
      color: #2563eb;
      font-family: monospace;
      font-size: 0.9rem;
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      padding: 1px 6px;
      border-radius: 4px;
      white-space: nowrap;
      margin-left: 12px;
    }}

    .final-award-box {{
      background: #ecfdf5;
      border: 1.5px solid #10b981;
      border-radius: 6px;
      padding: 10px 16px;
      margin-bottom: 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .award-label {{
      font-weight: 800;
      color: #065f46;
      font-size: 0.92rem;
    }}
    .award-val {{
      font-weight: 900;
      color: #047857;
      font-size: 1.15rem;
      font-family: monospace;
      text-decoration: underline;
    }}

    .pitfall-box {{
      background: #fffbeb;
      border-left: 4px solid #f59e0b;
      border-radius: 4px;
      padding: 10px 14px;
      margin-bottom: 10px;
      font-size: 0.9rem;
      color: #92400e;
      line-height: 1.5;
    }}
    .pitfall-box strong {{
      color: #b45309;
      display: block;
      margin-bottom: 2px;
    }}

    .alt-method-box {{
      background: #eff6ff;
      border-left: 4px solid #3b82f6;
      border-radius: 4px;
      padding: 8px 12px;
      margin-bottom: 10px;
      font-size: 0.88rem;
      color: #1e40af;
      line-height: 1.5;
    }}

    .reverse-check-box {{
      background: #fdf4ff;
      border-left: 4px solid #c084fc;
      border-radius: 4px;
      padding: 8px 12px;
      font-size: 0.88rem;
      color: #6b21a8;
      line-height: 1.5;
    }}

    .sheet-footer {{
      border-top: 1px solid #e2e8f0;
      padding-top: 14px;
      margin-top: 30px;
      display: flex;
      justify-content: space-between;
      color: #94a3b8;
      font-size: 0.8rem;
    }}
  </style>
</head>
<body>

  <div class="print-bar">
    <div>
      <a href="{back_url}"><i class="fa-solid fa-arrow-left"></i> Back to {title} Revision Guide</a>
    </div>
    <div>
      <a href="{slug}-workout-answers.html" class="btn-action-answers" style="background:#2563eb; margin-right:10px;"><i class="fa-solid fa-repeat"></i> Workout Answers</a>
      <div class="nav-pill-group">
        <a href="{sheet_url}" class="nav-pill-btn"><i class="fa-solid fa-file-lines"></i> Questions</a>
        <span class="nav-pill-btn active"><i class="fa-solid fa-check-double"></i> Answers</span>
      </div>
      <button type="button" class="btn-action-print" onclick="window.print()"><i class="fa-solid fa-print"></i> Print / Save to PDF</button>
    </div>
  </div>

  <div class="page-sheet">
    <div class="sheet-head">
      <div>
        <div class="brand-title">MASTER<span>FUNCTIONALSKILLS</span></div>
        <div class="brand-subtitle">Official Tutor Examiner Mark Scheme &amp; Model Solutions</div>
      </div>
      <div class="sheet-meta-badge">
        <span class="topic-name">{title}</span>
        <span class="spec-tag">{spec_codes}</span>
      </div>
    </div>

    <div class="scheme-summary-bar">
      <div><strong>Total Marks Available:</strong> {total_marks} Marks (Pass Threshold: ~{int(total_marks * 0.65)}/{total_marks})</div>
      <div><strong>Examiner Standard:</strong> Full Method (M) and Process (P) marks awarded even if final arithmetic errs.</div>
    </div>

{sections_html}

    <div class="sheet-footer">
      <div>Master Functional Skills • Pearson Edexcel Official Marking Guide • 100% Original Content</div>
      <div>Page 1 of 1 • Rev 2026.1</div>
    </div>
  </div>
</body>
</html>"""
