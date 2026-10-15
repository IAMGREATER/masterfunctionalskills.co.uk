"""
build_pilots.py — Pilot pages for the A4 "Fill the Page" kit.

    python3 books/a4/build_pilots.py            # builds both pilots + QA
    python3 books/a4/build_pilots.py spag       # just one

Outputs -> assets/downloads/pilots/Pilot_SPaG_L2_A4.pdf, Pilot_Maths_L2_A4.pdf (+ _contact.png)
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "spag"))

import a4_kit as K  # noqa: E402

OUT = K.SITE_ROOT / "assets" / "downloads" / "pilots"
COV = K.COVER_DIR


def ph(keywords, theme=None, exclude=()):
    """Photo lookup (returns None -> tidy placeholder)."""
    return K.photo(keywords, theme, exclude)


# =============================================================================
# SPaG Level 2 pilot
# =============================================================================
def spag_pilot():
    import spag_l2_84p_units_1_13 as U
    import spag_l2_84p_diag_vocab as DV

    units = {u["unit"]: u for u in U.UNITS_1_TO_13}
    BOOK = "SPaG Level 2 Mastery"
    pages = [K.front_cover(COV / "spag_l2_mastery_cover-01.png")]
    used = set()

    def P(keys):
        p = ph(keys, "spag", used) or ph(keys, "english", used) or ph(keys, None, used)
        if p:
            used.add(p)
        return p

    # ---- p2 inside cover
    pages.append(K.inside_cover(
        "Spelling, Punctuation &amp; Grammar",
        "Level 2 &bull; Big rules, real workplace examples and lots of practice.",
        "SPaG Level 2",
        [("1&ndash;13", "Sentences, commas, semicolons, apostrophes", "6"),
         ("14&ndash;26", "Verbs, agreement, homophones, spelling", "32"),
         ("V", "Visual vocabulary: workplace words", "58"),
         ("M", "Exam practice and mock papers", "70"),
         ("&#10003;", "Answers", "80")],
        footer=BOOK))

    # ---- p3 meet your guides / how a unit works
    body = (K.page_title("How a unit works", kicker="Before you start",
                         lead="Every unit is a two-page spread. Learn on the left. Practise on the right.")
            + K.character_bubble(K.cartoon("tutor teacher woman"), "Priya &bull; your tutor",
                                 "Hi! I'm Priya. On the <b>left page</b> I explain one rule with a picture, "
                                 "a Golden Rule and a common trap to avoid.", "left", 52, "#7c3aed")
            + K.character_bubble(K.cartoon("learner student man"), "Sam &bull; a learner like you",
                                 "I'm Sam. On the <b>right page</b> I try the exercises. "
                                 "I write on the lines, then check the answers at the back.", "right", 52, "#0d9488")
            + K.two_col(
                K.rule_box("Left page = Learn",
                           K.bullets(["<b>A</b> &ndash; the idea, in plain English",
                                      "<b>B</b> &ndash; the rule, step by step",
                                      "<b>C</b> &ndash; wrong vs right example"])),
                K.rule_box("Right page = Practise",
                           K.bullets(["<b>A</b> &ndash; tick the right answer",
                                      "<b>B</b> &ndash; rewrite the sentence",
                                      "<b>C</b> &ndash; write your own"])))
            + K.hero_image(P("adult learner studying notebook desk"),
                           "Little and often: one unit a day is better than five on a Sunday.", 40, fill=True))
    pages.append(K.page(body, header=(BOOK, "Start here"), footer=BOOK, page_no=3))

    # ---- Murphy spreads
    extra = {
        12: dict(
            idea="<b>it's</b> is short for <b>it is</b> or <b>it has</b>.<br><b>its</b> means "
                 "<b>belonging to it</b> &ndash; like <i>his</i> or <i>her</i>. No apostrophe!",
            rule="<div class='formula-strip'><span class='fpill'>it's = it is / it has</span>"
                 "<span class='fpill'>its = belonging to it</span></div>"
                 "Say <b>'it is'</b> out loud in the gap.<ul><li>If it makes sense, write <b>it's</b>: "
                 "<i>It's cold in the server room.</i></li><li>If not, write <b>its</b>: "
                 "<i>The firm changed its logo.</i></li></ul>",
            watch="<b>its'</b> is never correct. It does not exist!",
            photo="server room data centre technician", cap="IT technicians write reports where its / it's matters.",
            cartoon="confused thinking", name="Sam", short="Its or It's?", mcq=slice(0, 3),
            golden="If you can't say <b>'it is'</b> or <b>'it has'</b> in that spot, rub out the apostrophe.",
            prompt="Write <b>two sentences</b> about a work computer: one with <b>it's</b> and one with <b>its</b>."),
        11: dict(
            idea="An apostrophe can show that something <b>belongs</b> to someone: "
                 "<i>the manager's office</i> = the office of the manager.",
            rule="<div class='formula-strip'><span class='fpill'>one owner: 's</span>"
                 "<span class='fpill'>plural ending in s: s'</span><span class='fpill'>plural without s: 's</span></div>"
                 "<ul><li><b>One</b> tenant &rarr; the <b>tenant's</b> lease</li>"
                 "<li><b>Many</b> tenants &rarr; the <b>tenants'</b> committee</li>"
                 "<li><b>Irregular</b> plural &rarr; the <b>children's</b> play area, the <b>men's</b> room</li></ul>",
            watch="Never use an apostrophe for a simple plural: <i>six pallet's</i> &#10007; &rarr; <i>six pallets</i> &#10003;",
            photo="office building reception workplace", cap="Signs, notices and contracts all use possessive apostrophes.",
            cartoon="pointing explaining", name="Priya", short="Apostrophes for Owners", mcq=slice(1, 4),
            golden="Cover the apostrophe with your finger. The word on the left must name the <b>owner</b>.",
            prompt="Write <b>two rules</b> for a staff room. Use <i>the manager's</i> and <i>the staff's</i>."),
    }

    pno = 4
    for un in (12, 11):
        u, x = units[un], extra[un]
        g_title, g_text = (u["golden_rule"].split(":", 1) if ":" in u["golden_rule"] else ("Golden Rule", u["golden_rule"]))
        left = (K.page_title(x["short"], kicker=f"Unit {un} &bull; {u['strand']}", badge=un)
                + K.character_bubble(K.cartoon(x["cartoon"]), x["name"], f"<b style='color:var(--accent)'>A &nbsp;The idea</b><br>{x['idea']}",
                                     "left", 40, "#7c3aed" if x["name"] == "Priya" else "#0d9488")
                + K.rule_box(f"B &nbsp;{u['rule_title']}", x["rule"])
                + K.tip_pair(x.get("golden", g_text.strip()), x["watch"], golden_title=g_title.title())
                + K.two_col(K.compare(u["worked_bad"], u["worked_good"], stacked=True,
                                      bad_label="C &nbsp;&#10007; Wrong", good_label="&#10003; Right"),
                            K.hero_image(P(x["photo"]), x["cap"], 50, fill=True),
                            ratio=(1.45, 1), fill=True))
        pages.append(K.page(left, header=(BOOK, f"Unit {un} &bull; Learn"), footer=BOOK, page_no=pno))
        pno += 1

        mcq = [{"q": q, "options": [o[3:] if o[1] == ")" else o for o in opts]} for q, opts, _ in u["exercise_a"][x["mcq"]]]
        rew = [(f"<b>{lab}:</b> <i>{s}</i>", 2) for lab, s, _ in u["exercise_b"][:2]]
        right = (K.section("A", "Tick the correct sentence")
                 + K.exercise_list(mcq)
                 + K.section("B", "Rewrite it correctly")
                 + K.exercise_list(rew, start=4)
                 + K.fill_lines(f"<span style='color:var(--accent)'>C &nbsp;Your turn:</span> " + x["prompt"], min_mm=36, gap_mm=10))
        pages.append(K.page(right, header=(BOOK, f"Unit {un} &bull; Practise"), footer=BOOK, page_no=pno))
        pno += 1

    # ---- visual vocabulary page (prefixes)
    vm = DV.VOCABULARY_MODULES[0]
    simple = {
        "Anti-": ("antivirus", "Install <b>antivirus</b> software on every laptop.", "antivirus laptop security"),
        "Bi-": ("bilateral", "The two companies signed a <b>bilateral</b> deal.", "handshake business deal"),
        "Co- / Con-": ("collaborate", "Our teams <b>collaborate</b> on the project.", "team collaboration meeting"),
        "De-": ("de-escalate", "Stay calm to <b>de-escalate</b> an angry customer.", "customer service desk"),
        "Fore-": ("forecast", "The sales <b>forecast</b> for May looks good.", "forecast chart graph"),
        "Mal-": ("malfunction", "The printer had a <b>malfunction</b> again.", "broken printer repair"),
        "Mis-": ("miscalculate", "Don't <b>miscalculate</b> the delivery cost.", "calculator receipt"),
        "Multi-": ("multidisciplinary", "A <b>multidisciplinary</b> NHS team met today.", "hospital nurse doctor team"),
    }
    tiles = []
    for pre, meaning, _ex, _ctx in vm["table_rows"]:
        w, sent, keys = simple[pre]
        tiles.append((P(keys), f"{w} <span style='font-weight:500;color:#64748b;font-size:12.5pt'>({pre.lower()} = {meaning.split('/')[0].strip().lower()})</span>", sent))
    tiles.append((P("construction site builder"), "subcontractor <span style='font-weight:500;color:#64748b;font-size:12.5pt'>(sub- = under)</span>",
                  "A <b>subcontractor</b> fitted the new windows."))
    body = (K.page_title("Workplace Words: Prefixes", kicker="Visual vocabulary &bull; Module 1",
                         lead="A prefix goes at the <b>start</b> of a word and changes its meaning.")
            + K.photo_grid(tiles, cols=3, fill=True, min_tile_mm=62))
    pages.append(K.page(body, header=(BOOK, "Visual vocabulary"), footer=BOOK, page_no=pno))
    pno += 1

    # ---- practice page: proofreading
    u = units[12]
    memo = K.clean_legacy(u["proofreading_text"]).replace("<h4", "<h3").replace("</h4>", "</h3>")
    body = (K.page_title("Proofreading Challenge", kicker="Practice &bull; Unit 12", badge="P")
            + K.box_html(memo, "Find and correct 5 its / it's errors")
            + K.table(["", "Error (copy it)", "Correction"],
                      [[f"<b>{i}</b>", "<div style='height:9mm'></div>", ""] for i in range(1, 6)],
                      ["10mm", "50%", "50%"])
            + K.fill_notes("The rule I used most was...", 22))
    pages.append(K.page(body, header=(BOOK, "Practice"), footer=BOOK, page_no=pno))
    pno += 1

    # ---- exam-style writing page
    body = (K.page_title("Exam Practice: Write an Email", kicker="Mock task &bull; 15 marks",
                         badge="M")
            + K.two_col(
                K.box_html("You work at <b>Riverside Trade Park</b>. The car park will be closed for repairs next week."
                           "<br><br>Write an <b>email to all tenants</b> to:"
                           + K.bullets(["explain why the car park is closing", "say where staff can park instead",
                                        "ask tenants to tell their visitors"])
                           + "Use <b>at least two</b> possessive apostrophes correctly.", "Your task")
                + K.tip_pair("Plan 3 paragraphs before you write.", "Check every apostrophe at the end.", "Plan", "Check"),
                K.diagram(K.letter_layout("email", 78, 128, colour="#3b0764"), "Email layout"),
                ratio=(1.25, 1))
            + K.fill_lines("Write your email here:", min_mm=70))
    pages.append(K.page(body, header=(BOOK, "Exam practice"), footer=BOOK, page_no=pno))
    pno += 1

    # ---- answers
    blocks = []
    for un in (12, 11):
        u = units[un]
        a = "".join(f"<b>{i}.</b> {ans} &nbsp; " for i, (_, _, ans) in enumerate(u["exercise_a"][extra[un]["mcq"]], 1))
        b = "".join(f"<p><b>{i}.</b> {ans}</p>" for i, (_, _, ans) in enumerate(u["exercise_b"][:2], 4))
        blocks.append((f"Unit {un} &ndash; Section A", f"<p>{a}</p>"))
        blocks.append((f"Unit {un} &ndash; Section B", b))
    blocks.append(("Proofreading (Unit 12 memo)", K.bullets(units[12]["proofreading_errors"])))
    blocks.append(("Prefix check", "<p>anti = against &bull; bi = two &bull; co = together &bull; de = reverse &bull; "
                                   "fore = before &bull; mal = bad &bull; mis = wrongly &bull; multi = many &bull; sub = under</p>"))
    body = (K.page_title("Answers", kicker="Check your work") + K.answer_columns(blocks)
            + K.fill_notes("My corrections &ndash; what will I do differently next time?", 30))
    pages.append(K.page(body, header=(BOOK, "Answers"), footer=BOOK, page_no=pno))

    pages.append(K.back_cover(COV / "spag_mastery_cover_page-2.png"))
    return pages


# =============================================================================
# Maths Level 2 pilot
# =============================================================================
def maths_pilot():
    BOOK = "Maths Level 2 Core Study Guide"
    used = set()

    def P(keys):
        p = ph(keys, "maths", used) or ph(keys, None, used)
        if p:
            used.add(p)
        return p

    pages = [K.front_cover(COV / "maths_l2_core_cover_page-1.png")]
    pages.append(K.inside_cover(
        "Maths Level 2 Core Study Guide",
        "All 39 Level 2 standards &bull; Big diagrams &bull; Real-life problems &bull; Full worked answers.",
        "Maths Level 2",
        [("1", "Number: percentages, fractions, ratio", "3"),
         ("2", "Measure, shape &amp; space", "28"),
         ("3", "Handling data: charts, averages, probability", "52"),
         ("M", "Mock exam (Section A &amp; B)", "76"),
         ("&#10003;", "Answers &amp; mark scheme", "82")],
        footer=BOOK))

    # ---- concept 1: percentages
    bar = K._svg(176, 36, "".join(
        [f'<rect x="{3 + i * 17}" y="2" width="17" height="14" fill="{"#0284c7" if i < 3 else "#e0f2fe"}" stroke="#0c4a6e" stroke-width="0.6"/>'
         f'<text x="{11.5 + i * 17}" y="11" font-size="4.6" text-anchor="middle" fill="{"#fff" if i < 3 else "#0c4a6e"}">£24</text>' for i in range(10)])
        + '<text x="3" y="25" font-size="5" font-weight="700" fill="#0c4a6e">£240 in 10 equal parts &#8594; each part (10%) = £24</text>'
        + '<text x="3" y="33" font-size="5" font-weight="700" fill="#0284c7">30% = 3 parts = 3 &#215; £24 = £72</text>')
    body = (K.page_title("Percentages of Amounts", kicker="Number &bull; Standard N7", badge=4)
            + K.hero_image(P("shop sale discount price tag"), "A 30% off sale: how much do you really save?", 55, fill=True)
            + K.diagram(bar)
            + K.two_col(
                K.rule_box("The 10% method", K.bullets(["<b>10%</b>: divide by 10",
                                                        "<b>5%</b>: halve the 10%",
                                                        "<b>1%</b>: divide by 100",
                                                        "Add the parts you need"])),
                K.worked_example("A £240 coat is 30% off. Find the sale price.",
                                 ["10% of £240 = £24", "30% = 3 &times; £24 = £72", "£240 &minus; £72 = <b>£168</b>"]))
            + K.tip_pair("Always find <b>10%</b> first. Build everything else from it.",
                         "Is the question asking for the <b>saving</b> or the <b>new price</b>?"))
    pages.append(K.page(body, header=(BOOK, "Unit 4 &bull; Number"), footer=BOOK, page_no=3))

    # ---- concept 2: area of compound shapes
    body = (K.page_title("Area of Compound Shapes", kicker="Measure &amp; Shape &bull; Standard M12", badge=15)
            + K.two_col(
                K.hero_image(P("wooden floor room flooring"), "Flooring is sold by the m&sup2;.", 60, fill=True),
                K.diagram(K.shape("lshape", {"W": 10, "H": 8, "w_cut": 4, "h_cut": 3}, 92, 80), "An L-shaped room", fill=True),
                ratio=(1, 1.1), fill=True)
            + K.rule_box("Split it into rectangles",
                         "<b>Area of a rectangle = length &times; width.</b> Split the shape into rectangles "
                         "<b>A</b> and <b>B</b>. Find each area, then <b>add</b>.")
            + K.worked_example("Find the area of the L-shaped room.",
                               ["Missing sides: 10 &minus; 4 = 6 m and 8 &minus; 3 = 5 m",
                                "A: 6 &times; 8 = 48 m&sup2; &nbsp;&nbsp; B: 4 &times; 5 = 20 m&sup2;",
                                "Total: 48 + 20 = <b>68 m&sup2;</b>"])
            + K.tip_pair("Area is always in <b>square</b> units: m&sup2;, cm&sup2;.",
                         "Don't add the side lengths &ndash; that gives the <b>perimeter</b>, not the area."))
    pages.append(K.page(body, header=(BOOK, "Unit 15 &bull; Shape"), footer=BOOK, page_no=4))

    # ---- concept 3: charts
    body = (K.page_title("Bar Charts &amp; Pie Charts", kicker="Handling Data &bull; Standard D3", badge=28)
            + K.diagram(K.bar_chart([("Mon", 34), ("Tue", 41), ("Wed", 28), ("Thu", 52), ("Fri", 63), ("Sat", 75)],
                                    "Café customers this week", "Customers", 178, 70))
            + K.two_col(
                K.diagram(K.pie_chart([("Coffee", 45), ("Tea", 25), ("Juice", 20), ("Water", 10)], "Drinks sold (%)", 92, 56)),
                K.worked_example("How many <b>more</b> customers came on Saturday than Wednesday?",
                                 ["Sat = 75, Wed = 28", "75 &minus; 28 = <b>47</b>"]),
                ratio=(1.05, 1))
            + K.hero_image(P("cafe coffee shop barista"), "A café owner uses charts to decide how many staff to book.", 34, fill=True)
            + K.tip_pair("Check the <b>scale</b> first: what is one gridline worth?",
                         "A pie chart shows <b>shares</b>, not totals."))
    pages.append(K.page(body, header=(BOOK, "Unit 28 &bull; Data"), footer=BOOK, page_no=5))

    # ---- concept 4: scales
    body = (K.page_title("Scales, Time &amp; Temperature", kicker="Measure &bull; Standards M3&ndash;M5", badge=18)
            + K.diagram(K.number_line(-10, 10, 1, {-6: "&minus;6&deg;C night", 4: "4&deg;C day"}, 178, 40, 2,
                                      jumps=[(-6, 4, "+10&deg;")]))
            + K.two_col(
                K.diagram(K.thermometer(18, -10, 40, 5, 100, 42), "Reads 18&deg;C", fill=True),
                K.diagram(K.clock_face(2, 45, 58), "2:45 &ndash; quarter to three")
                + K.rule_box("Read any scale", K.bullets(["Find two labelled marks", "Count the gaps",
                                                          "Work out what <b>one gap</b> is worth"])),
                ratio=(0.55, 1), fill=True)
            + K.worked_example("At night it was &minus;6&deg;C. At midday it was 4&deg;C. How much did it rise?",
                               ["&minus;6 up to 0 = 6 degrees, then 0 up to 4 = 4 degrees",
                                "6 + 4 = <b>10&deg;C</b>"]))
    pages.append(K.page(body, header=(BOOK, "Unit 18 &bull; Measure"), footer=BOOK, page_no=6))

    # ---- practice page 1
    qs = [{"q": "A sofa costs <b>£650</b>. In a sale it is <b>20% off</b>. Find the sale price.", "marks": 2},
          {"q": "A garden is a rectangle <b>12 m</b> long and <b>7.5 m</b> wide. Turf costs <b>£4.20 per m&sup2;</b>. "
                "How much will it cost to turf the whole garden?", "marks": 3, "weight": 1.3},
          {"q": "The temperature at 6 am was <b>&minus;4&deg;C</b>. At 3 pm it was <b>9&deg;C</b>. How much did it rise?", "marks": 1},
          {"q": "Sam earns <b>£1,850</b> a month. He spends <b>35%</b> on rent. How much is left after rent?", "marks": 2},
          {"q": "A recipe for 4 people uses <b>300 g</b> of rice. How much rice is needed for <b>10</b> people?", "marks": 2}]
    body = (K.page_title("Practice: Mixed Problems", kicker="Practice page &bull; Section A (no calculator)", badge="P")
            + K.practice_stack(qs))
    pages.append(K.page(body, header=(BOOK, "Practice"), footer=BOOK, page_no=7))

    # ---- practice page 2 (charts)
    body = (K.page_title("Practice: Charts &amp; Data", kicker="Practice page &bull; Section B (calculator)", badge="P")
            + K.diagram(K.bar_chart([("Jan", 120), ("Feb", 95), ("Mar", 140), ("Apr", 160), ("May", 185)],
                                    "Bikes sold by a shop", "Bikes", 178, 78, colour="#f59e0b"))
            + K.practice_stack([
                {"q": "How many bikes were sold altogether from January to May?", "marks": 2},
                {"q": "What is the <b>mean</b> number of bikes sold per month?", "marks": 2},
                {"q": "Sales in June were <b>15% more</b> than in May. How many bikes were sold in June?", "marks": 3, "weight": 1.3},
            ], start=1))
    pages.append(K.page(body, header=(BOOK, "Practice"), footer=BOOK, page_no=8))

    # ---- mock exam page 1
    body = (K.page_title("Mock Exam &bull; Question 1", kicker="Section B &bull; Calculator allowed &bull; 6 marks", badge="M")
            + K.two_col(
                K.para("Aisha is fitting a new floor in her L-shaped kitchen (diagram). Flooring comes in "
                       "<b>packs that cover 2.5 m&sup2;</b> and cost <b>£32.99</b> each. She needs <b>10% extra</b> for cutting.")
                + K.para("<b>(a)</b> How many packs must she buy? &nbsp; <b>(b)</b> What is the total cost?"),
                K.diagram(K.shape("lshape", {"W": 6, "H": 5, "w_cut": 2.5, "h_cut": 2}, 82, 64)),
                ratio=(1.25, 1))
            + K.fill_grid("Show all your working. Check your answer.", 120))
    pages.append(K.page(body, header=(BOOK, "Mock exam"), footer=BOOK, page_no=9))

    # ---- mock exam page 2
    body = (K.page_title("Mock Exam &bull; Question 2", kicker="Section B &bull; Calculator allowed &bull; 5 marks", badge="M")
            + K.two_col(
                K.para("A café sold <b>480</b> drinks on Saturday. The pie chart shows the types of drink sold.")
                + K.para("<b>(a)</b> How many coffees were sold? <br><b>(b)</b> The owner says &lsquo;We sold more than 100 juices.&rsquo; "
                         "Is she right? Show how you decide."),
                K.diagram(K.pie_chart([("Coffee", 45), ("Tea", 25), ("Juice", 20), ("Water", 10)], "", 92, 58)),
                ratio=(1.1, 1))
            + K.fill_grid("Show all your working.", 120))
    pages.append(K.page(body, header=(BOOK, "Mock exam"), footer=BOOK, page_no=10))

    # ---- answers
    blocks = [
        ("Percentages (p3)", "<p>15% of £60: 10% = £6, 5% = £3 &rarr; <b>£9</b></p>"),
        ("Practice 1", K.bullets(["£650 &minus; £130 = <b>£520</b>", "12 &times; 7.5 = 90 m&sup2;; 90 &times; £4.20 = <b>£378</b>",
                                  "&minus;4 to 9 = <b>13&deg;C</b>", "35% of £1,850 = £647.50; left = <b>£1,202.50</b>",
                                  "300 &divide; 4 = 75 g per person; 75 &times; 10 = <b>750 g</b>"], ordered=True)),
        ("Practice 2", K.bullets(["120+95+140+160+185 = <b>700 bikes</b>", "700 &divide; 5 = <b>140</b>",
                                  "185 &times; 1.15 = 212.75 &rarr; <b>213 bikes</b>"], ordered=True)),
        ("Mock Q1", "<p>Area = (3.5 &times; 5) + (2.5 &times; 3) = 17.5 + 7.5 = 25 m&sup2;. Add 10%: 27.5 m&sup2;. "
                    "27.5 &divide; 2.5 = 11 packs. Cost = 11 &times; £32.99 = <b>£362.89</b>.</p>"),
        ("Mock Q2", "<p>(a) 45% of 480 = <b>216</b> coffees. (b) 20% of 480 = 96 juices. 96 &lt; 100, so <b>she is wrong</b>.</p>"),
        ("Mark scheme codes", "<p><b>M1</b> method &bull; <b>A1</b> accurate answer &bull; <b>C1</b> clear conclusion. "
                              "Always show working &ndash; method marks are given even if the final answer is wrong.</p>"),
    ]
    body = (K.page_title("Answers &amp; Mark Scheme", kicker="Check your work") + K.answer_columns(blocks)
            + K.fill_notes("My corrections &ndash; what will I do differently next time?", 30))
    pages.append(K.page(body, header=(BOOK, "Answers"), footer=BOOK, page_no=11))

    pages.append(K.back_cover(COV / "maths_l2_core_cover_page-2.png"))
    return pages


def build(which=("spag", "maths")):
    reps = []
    if "spag" in which:
        r = K.render_pdf(spag_pilot(), OUT / "Pilot_SPaG_L2_A4.pdf", theme="spag", title="Pilot SPaG L2 A4")
        rep = K.qa_report(r["pdf"], html_path=r["html"])
        rep["overflow"] = r["overflow"]
        reps.append(rep)
    if "maths" in which:
        r = K.render_pdf(maths_pilot(), OUT / "Pilot_Maths_L2_A4.pdf", theme="maths", title="Pilot Maths L2 A4")
        rep = K.qa_report(r["pdf"], html_path=r["html"])
        rep["overflow"] = r["overflow"]
        reps.append(rep)
    for rep in reps:
        K.print_report(rep)
        print(f"  overflowing pages: {rep['overflow'] or 'none'}\n")
    return reps


if __name__ == "__main__":
    build(sys.argv[1:] or ("spag", "maths"))
