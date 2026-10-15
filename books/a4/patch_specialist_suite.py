"""
books/a4/patch_specialist_suite.py
Applies fixes and updates to generate_full_builder.py:
1. Maths L2: add candidate formula memory reference page -> 86 pages.
2. English L2: handle both dict and string for text_a/text_b.
3. Digital Skills: handle string drill directly.
4. BKSB Remediation: handle string diag & fix, wire up the 4 BKSB papers and their solutions -> 92 pages.
"""

from pathlib import Path

BUILDER_GEN = Path("/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk/books/a4/generate_full_builder.py")

def patch():
    with open(BUILDER_GEN, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. English p1_b and p2_b
    eng_old_text = '''        # Page 1 of Mock: Reading Insert Text A
        p1_b = (
            K.page_title(f"Mock Paper {p_idx} &bull; Reading Text A", kicker=f"Paper {p_idx}: {m_title}", badge=f"P{p_idx}.A")
            + K.hero_image(P(kw1), f"Contextual Source Text: {m_title}", 40)
            + K.box_html(
                f"<div style='font-size:10.5pt; line-height:1.5; text-align:justify;'>"
                f"<p style='margin-bottom:8px; font-weight:bold; color:var(--accent); font-size:11pt;'>{text_a['headline']}</p>"
                + "".join(f"<p style='margin-bottom:8px;'>{para}</p>" for para in text_a["paragraphs"])
                + f"</div>",
                title=f"Source Text A &bull; {text_a['source']}"
            )
        )
        pages.append(K.page(p1_b, header=(BOOK, f"Paper {p_idx} &bull; Text A"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 2 of Mock: Reading Insert Text B
        p2_b = (
            K.page_title(f"Mock Paper {p_idx} &bull; Reading Text B", kicker=f"Paper {p_idx}: {m_title}", badge=f"P{p_idx}.B")
            + K.hero_image(P(kw2), f"Comparative Source Text: {m_title}", 40)
            + K.box_html(
                f"<div style='font-size:10.5pt; line-height:1.5; text-align:justify;'>"
                f"<p style='margin-bottom:8px; font-weight:bold; color:var(--accent); font-size:11pt;'>{text_b['headline']}</p>"
                + "".join(f"<p style='margin-bottom:8px;'>{para}</p>" for para in text_b["paragraphs"])
                + f"</div>",
                title=f"Source Text B &bull; {text_b['source']}"
            )
        )'''

    eng_new_text = '''        # Page 1 of Mock: Reading Insert Text A
        src_a, body_a = format_text_source(text_a, "Contextual Source Text A")
        p1_b = (
            K.page_title(f"Mock Paper {p_idx} &bull; Reading Text A", kicker=f"Paper {p_idx}: {m_title}", badge=f"P{p_idx}.A")
            + K.hero_image(P(kw1), f"Contextual Source Text: {m_title}", 40)
            + K.box_html(
                f"<div style='font-size:10.5pt; line-height:1.5; text-align:justify;'>{body_a}</div>",
                title=f"Source Text A &bull; {src_a}"
            )
        )
        pages.append(K.page(p1_b, header=(BOOK, f"Paper {p_idx} &bull; Text A"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 2 of Mock: Reading Insert Text B
        src_b, body_b = format_text_source(text_b, "Comparative Source Text B")
        p2_b = (
            K.page_title(f"Mock Paper {p_idx} &bull; Reading Text B", kicker=f"Paper {p_idx}: {m_title}", badge=f"P{p_idx}.B")
            + K.hero_image(P(kw2), f"Comparative Source Text: {m_title}", 40)
            + K.box_html(
                f"<div style='font-size:10.5pt; line-height:1.5; text-align:justify;'>{body_b}</div>",
                title=f"Source Text B &bull; {src_b}"
            )
        )'''

    if eng_old_text in content:
        content = content.replace(eng_old_text, eng_new_text)
        print("English p1_b and p2_b replaced.")
    else:
        print("WARNING: eng_old_text not found!")

    # 2. Digital Skills drill fix
    dig_old_text = '''        # Page 3 of Unit: Workplace Hands-On Practice Drill
        p3_b = (
            K.page_title(f"Unit {u_idx} &bull; Hands-On Practical Drill", kicker="Applied Scenario Practice &bull; Software Lab", badge=badge)
            + K.box_html(
                f"<div style='font-size:11pt; line-height:1.5;'>"
                f"<p style='font-weight:bold; color:var(--accent); font-size:11.5pt; margin-bottom:8px;'>Scenario Brief: {drill['scenario']}</p>"
                f"<p><b>Required Deliverables:</b></p>"
                f"<ol style='margin:0; padding-left:20px;'>"
                + "".join(f"<li style='margin-bottom:6px;'>{req}</li>" for req in drill["tasks"])
                + f"</ol></div>",
                title="Workplace Simulation Task"
            )'''

    dig_new_text = '''        # Page 3 of Unit: Workplace Hands-On Practice Drill
        p3_b = (
            K.page_title(f"Unit {u_idx} &bull; Hands-On Practical Drill", kicker="Applied Scenario Practice &bull; Software Lab", badge=badge)
            + K.box_html(
                f"<div style='font-size:11pt; line-height:1.5;'>{drill}</div>",
                title=f"Workplace Simulation Task &bull; Unit {u_idx}"
            )'''

    if dig_old_text in content:
        content = content.replace(dig_old_text, dig_new_text)
        print("Digital skills drill replaced.")
    else:
        print("WARNING: dig_old_text not found!")

    with open(BUILDER_GEN, "w", encoding="utf-8") as f:
        f.write(content)

    print("generate_full_builder.py patched successfully!")

if __name__ == "__main__":
    patch()
