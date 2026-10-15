#!/usr/bin/env python3
"""
generate_audit_catalog.py
Generates the comprehensive visual image audit catalog HTML page:
/home/subi/Projects/masterfunctionalskills.co.uk/image_audit_catalog.html
"""

import os, sys, html
import visual_curriculum_catalog as vcc
from build_all_curriculum_pages import CURRICULUM_MATHS, CURRICULUM_ENGLISH
from collections import Counter

# Proposed new image metadata for English topics to eliminate repetition
PROPOSED_ENGLISH = {
    "reading-fact-or-opinion.html": {
        "concept": "Printed broadsheet newspaper article with side-by-side news reporting and editorial opinion columns.",
        "why": "Currently reuses writing_notes.jpg (4x). An authentic newspaper clipping directly represents identifying facts vs journalist opinions.",
        "photo_file": "journalism_media/newspaper_editorial.jpg",
        "unsplash_search": "newspaper article editorial journalism"
    },
    "reading-meaning.html": {
        "concept": "Hardcover dictionary or glossary open on a study desk with a magnifying glass over highlighted definitions.",
        "why": "Currently reuses library_books.jpg (3x). A dictionary with highlighted word definitions directly illustrates determining word meaning in context.",
        "photo_file": "classroom_studying_adults/dictionary_magnifier.jpg",
        "unsplash_search": "dictionary magnifying glass definition vocabulary"
    },
    "reading-specialist-words.html": {
        "concept": "Technical engineering maintenance blueprint or clinical pharmacology manual with labelled domain terminology.",
        "why": "Currently reuses library_books.jpg (3x). A vocational manual demonstrates decoding specialist trade/clinical jargon.",
        "photo_file": "workplace_office/technical_manual.jpg",
        "unsplash_search": "technical manual blueprint specifications engineering"
    },
    "reading-presentational-features.html": {
        "concept": "Modern magazine spread or instructional company handbook showing callout text boxes, subheadings, and visual sidebars.",
        "why": "Currently reuses presentation.jpg (2x). An authentic multi-column printed layout illustrates presentational devices in practice.",
        "photo_file": "workplace_office/magazine_layout_features.jpg",
        "unsplash_search": "magazine layout typography editorial brochure"
    },
    "reading-investigating-layout.html": {
        "concept": "Professional multi-fold informational leaflet or workplace policy bulletin showcasing bullet points, bold headers, and columns.",
        "why": "Currently reuses whiteboard_planning.jpg (4x). A printed informational leaflet represents layout analysis for functional reading.",
        "photo_file": "workplace_office/brochure_pamphlet.jpg",
        "unsplash_search": "brochure pamphlet printed document layout"
    },
    "reading-investigating-image.html": {
        "concept": "Photojournalist or communications editor reviewing printed photo proofs and infographic charts on an editorial lightboard.",
        "why": "Currently reuses presentation.jpg (2x). Examining photo proofs directly represents analyzing image choices and visual impact.",
        "photo_file": "workplace_office/photo_editor_proofs.jpg",
        "unsplash_search": "photo proofs editorial photography contact sheet"
    },
    "reading-language-features.html": {
        "concept": "Public relations campaign poster or high-impact advert featuring bold rhetorical slogans, rule of three, and emotive language.",
        "why": "Currently reuses student_studying_laptop.jpg (5x). A persuasive advertising campaign clearly illustrates rhetorical devices and language techniques.",
        "photo_file": "retail_shop/advertising_billboard.jpg",
        "unsplash_search": "advertising billboard poster persuasive campaign"
    },
    "reading-point-of-view-and-line-of-argument.html": {
        "concept": "Balanced courtroom or boardroom debate table with two opposing case folders and scales of justice motif.",
        "why": "Currently reuses desk_laptop.jpg (5x). Opposing case files visually signify identifying bias, authorial stance, and balanced arguments.",
        "photo_file": "workplace_office/boardroom_debate.jpg",
        "unsplash_search": "debate discussion boardroom case files"
    },
    "reading-styles-of-writing-and-voice.html": {
        "concept": "Side-by-side visual comparison of a formal legal contract on parchment next to an informal smartphone messaging exchange.",
        "why": "Currently reuses student_studying_laptop.jpg (5x). Directly contrasts formal institutional voice with casual colloquial style.",
        "photo_file": "workplace_office/formal_contract_letter.jpg",
        "unsplash_search": "formal document contract signature letter"
    },
    "reading-text-types.html": {
        "concept": "Visual montage of authentic daily text types: a culinary recipe card, a public transport notice, an online product review, and an editorial.",
        "why": "Currently reuses library_books.jpg (3x). Shows the 4 core text types tested in Functional Skills: instructive, informative, persuasive, descriptive.",
        "photo_file": "everyday_objects/mixed_text_types.jpg",
        "unsplash_search": "newspaper magazine letter book collection"
    },
    "reading-comparing-texts.html": {
        "concept": "Dual monitor workstation showing two contrasting articles side-by-side with comparison notes on a clipboard.",
        "why": "Currently reuses desk_laptop.jpg (5x). Dual-screen document analysis directly mirrors the Level 2 exam requirement to compare Text A and Text B.",
        "photo_file": "workplace_office/dual_screen_research.jpg",
        "unsplash_search": "dual monitor computer comparison office"
    },
    "reading-why-do-writers-write.html": {
        "concept": "Investigative journalist writing an article with research notes, press badge, and highlighted background documents.",
        "why": "Currently reuses writing_notes.jpg (4x). Captures authorial purpose: writing to expose, inform, advise, or entertain.",
        "photo_file": "journalism_media/journalist_writing.jpg",
        "unsplash_search": "journalist notebook press reporting writer"
    },
    "reading-the-exam.html": {
        "concept": "Official examination desk setup with Pearson Edexcel reading answer booklet, analogue desk clock, and black ink pens.",
        "why": "Currently reuses adult_learners_class.jpg (2x). Direct visual representation of the timed exam environment and strategy.",
        "photo_file": "classroom_studying_adults/exam_desk_clock.jpg",
        "unsplash_search": "exam desk paper clock test test-taking"
    },
    "writing-planning-your-answer.html": {
        "concept": "Handwritten mind-map and structured 5-paragraph brainstorm diagram with coloured highlighters on lined exam paper.",
        "why": "Currently reuses whiteboard_planning.jpg (4x). A candidate's mind-map planning sheet illustrates effective pre-writing strategy.",
        "photo_file": "classroom_studying_adults/mindmap_planning.jpg",
        "unsplash_search": "mind map brainstorm notes handwriting plan"
    },
    "writing-communicating.html": {
        "concept": "Executive business letter typed on company letterhead with formal salutation, body paragraphs, and professional signature.",
        "why": "Currently reuses team_meeting.jpg (2x). An authentic printed business letter illustrates professional workplace communication.",
        "photo_file": "workplace_office/formal_letterhead.jpg",
        "unsplash_search": "formal letter document letterhead signature"
    },
    "writing-context.html": {
        "concept": "Workplace bulletin board in an NHS hospital with clinical notices, staff updates, and health & safety briefings.",
        "why": "Currently reuses desk_laptop.jpg (5x). Shows real-world context dictating writing tone, format, and urgency.",
        "photo_file": "healthcare_care/hospital_noticeboard.jpg",
        "unsplash_search": "bulletin board noticeboard hospital notices"
    },
    "writing-assessing-audience.html": {
        "concept": "Communications team reviewing demographic audience persona profiles and tone-of-voice style guide.",
        "why": "Currently reuses team_meeting.jpg (2x). Target audience persona cards reinforce matching vocabulary to reader demographics.",
        "photo_file": "workplace_office/audience_personas.jpg",
        "unsplash_search": "demographics target audience marketing persona"
    },
    "writing-form-presentational-and-language-features.html": {
        "concept": "Desktop publishing layout editor showing report formatting: bold running headers, subheadings, bullet points, and footer page numbers.",
        "why": "Currently reuses whiteboard_planning.jpg (4x). Direct visual demonstration of formal layout devices required in writing tasks.",
        "photo_file": "workplace_office/desktop_publishing.jpg",
        "unsplash_search": "document design desktop publishing layout"
    },
    "writing-organisational-markers.html": {
        "concept": "Close-up of written manuscript with discourse transition markers ('Furthermore', 'Consequently', 'On the other hand') neatly underlined in green.",
        "why": "Currently reuses writing_notes.jpg (4x). Shows how signposts and connective markers organize paragraph progression.",
        "photo_file": "classroom_studying_adults/highlighted_transitions.jpg",
        "unsplash_search": "highlighter pen text notes studying"
    },
    "writing-linking-up-your-answer.html": {
        "concept": "Architectural interlocking paving or bridge masonry structure symbolising cohesive transitions bridging consecutive paragraphs.",
        "why": "Currently reuses desk_laptop.jpg (5x). Visual metaphor for paragraph cohesion and logical thematic flow.",
        "photo_file": "construction_trades/interlocking_masonry.jpg",
        "unsplash_search": "bridge connection interlocking structure"
    },
    "writing-grammar.html": {
        "concept": "Teacher or editor's desk with red-ink grammar proofreading annotations correcting subject-verb agreement and comma splices.",
        "why": "Currently reuses student_studying_laptop.jpg (5x). Red-pen editorial markup visually represents grammatical precision.",
        "photo_file": "classroom_studying_adults/grammar_proofreading.jpg",
        "unsplash_search": "proofreading editing red pen manuscript"
    },
    "writing-tenses.html": {
        "concept": "Chronological workplace shift handover logbook tracking past shift incidents, current tasks, and future handovers.",
        "why": "Currently reuses writing_notes.jpg (4x). Practical demonstration of keeping past, present, and future tenses consistent.",
        "photo_file": "healthcare_care/shift_handover_log.jpg",
        "unsplash_search": "logbook shift notes medical handover"
    },
    "writing-perfecting-your-punctuation.html": {
        "concept": "Vintage typographical printing press letter blocks featuring colon, semicolon, question mark, and apostrophe.",
        "why": "Currently reuses student_studying_laptop.jpg (5x). Focuses attention specifically on punctuation marks rather than a generic laptop.",
        "photo_file": "workplace_office/typography_punctuation_blocks.jpg",
        "unsplash_search": "typography letterpress punctuation typeset"
    },
    "writing-spelling.html": {
        "concept": "Spelling tiles arranged on table with commonly tested adult homophones (their / there / they're; practice / practise).",
        "why": "Currently reuses student_studying_laptop.jpg (5x). Tactile letter tiles emphasize spelling patterns, prefixes, and homophone discrimination.",
        "photo_file": "classroom_studying_adults/spelling_letter_tiles.jpg",
        "unsplash_search": "scrabble tiles letters spelling words"
    },
    "writing-fantastic-finalising.html": {
        "concept": "Quality assurance audit checklist with green ballpoint ticks beside each proofreading criteria box.",
        "why": "Currently reuses desk_laptop.jpg (5x). Illustrates candidate final proofreading routine in the last 10 minutes of the exam.",
        "photo_file": "workplace_office/checklist_clipboard.jpg",
        "unsplash_search": "checklist clipboard ticking tasks complete"
    },
    "writing-why-are-you-writing.html": {
        "concept": "Clear call-to-action campaign flyers with bold headline 'Support Our Community Centre' and donation slip.",
        "why": "Currently reuses whiteboard_planning.jpg (4x). Directly illustrates writing with clear persuasive purpose and desired reader action.",
        "photo_file": "retail_shop/call_to_action_flyer.jpg",
        "unsplash_search": "flyer leaflet campaign call to action"
    },
    "writing-the-exam.html": {
        "concept": "Official Pearson Functional Skills Writing examination paper with allocated marks, time management annotations, and pen.",
        "why": "Currently reuses adult_learners_class.jpg (2x). Authentic exam conditions and timing strategy.",
        "photo_file": "classroom_studying_adults/writing_exam_paper.jpg",
        "unsplash_search": "exam test paper writing test ballpoint pen"
    }
}

# Proposed authentic photos & refined body diagrams for Maths topics
PROPOSED_MATHS = {
    "functional-skills-numbers-and-place-value.html": {
        "title_photo": "retail_shop/warehouse_stock.jpg",
        "title_concept": "Warehouse logistics inventory tallying 6-figure stock SKU numbers and barcodes.",
        "why_title_flagged": "Currently shows a place-value column diagram in the hero instead of an authentic vocational image.",
        "proposed_title_image": "High-res photo of automated warehouse barcode scanning tracking batch numbers up to 1,000,000.",
        "body_diagram_status": "Column chart is functional but visually flat. Needs colour-differentiated place-value blocks (Thousands = Blue, Hundreds = Amber, Units = Green)."
    },
    "functional-skills-ordering-numbers.html": {
        "title_photo": "retail_shop/warehouse_stock.jpg",
        "title_concept": "Sorting warehouse shelf tiers and delivery crates by sequential order numbers.",
        "why_title_flagged": "Reuses warehouse_stock photo. Needs a distinct visual of chronological ascending/descending order sorting.",
        "proposed_title_image": "Digital sorting conveyor or chronological shipping pallet labels.",
        "body_diagram_status": "Needs a stepped elevation staircase diagram showing ascending vs descending order clearly."
    },
    "functional-skills-addition-and-subtraction.html": {
        "title_photo": "money_shopping_bills/receipt_checking.jpg",
        "title_concept": "Auditor checking business expense receipts, itemized additions, and VAT subtractions.",
        "why_title_flagged": "Hero displays an SVG decimal column calculation instead of a real-life context.",
        "proposed_title_image": "Clear photo of commercial till receipt with printed subtotal, tax addition, and total payment.",
        "body_diagram_status": "Body diagram should be a clean, two-tone ledger column addition with carried digits cleanly badged in circular pills."
    },
    "functional-skills-multiplication.html": {
        "title_photo": "construction_trades/builder_measuring.jpg",
        "title_concept": "Construction estimator calculating bulk packs of bricks (46 packs × 35 bricks).",
        "why_title_flagged": "Hero title displays the raw SVG grid method calculation. User specifically flagged: 'The images for the maths revision titles should not just be a screenshot of the working'.",
        "proposed_title_image": "Authentic photo of construction pallet packs with delivery manifest or timber stack multiplication.",
        "body_diagram_status": "The Grid Method SVG is good in Core Skill 1, but needs subtle shadow depth, softer gridlines, and clearer arrow annotations leading into the subtotal sum."
    },
    "functional-skills-division.html": {
        "title_photo": "healthcare_care/medicine_tablets.jpg",
        "title_concept": "Hospital pharmacy technician dividing batch medication ampoules equally across 4 ward trollies.",
        "why_title_flagged": "Hero title displays a bus-stop division bracket with remainder numbers. Flawed as a title hero.",
        "proposed_title_image": "Clean clinical photo of medication dispensing or catering meal tray portioning.",
        "body_diagram_status": "Bus stop diagram in body is clear, but should feature a step-by-step 3-phase progression (Division -> Remainder -> Carry) rather than a single static bracket."
    },
    "functional-skills-bidmas.html": {
        "title_photo": "money_shopping_bills/calculator_finance.jpg",
        "title_concept": "Accountant evaluating complex financial mortgage formula on a multi-line scientific calculator.",
        "why_title_flagged": "Hero title displays 4 SVG formula boxes with math equations. User explicitly called out BIDMAS needing an appropriate title image, not a screenshot of workings.",
        "proposed_title_image": "Crisp photo of a Casio/scientific calculator display showing multi-operation formula with brackets (180 - 4 × 5²).",
        "body_diagram_status": "In Core Skill 1, replace the text boxes with a hierarchical pyramid / pyramid tiers showing B at the apex, down to AS at the base."
    },
    "functional-skills-rounding-and-estimating.html": {
        "title_photo": "retail_shop/supermarket_aisle.jpg",
        "title_concept": "Shopper checking supermarket grocery shelf prices and mental tally before checkout.",
        "why_title_flagged": "Hero title displays an SVG number line with 47 rounded to 50. User specifically noted: 'rounding and estimating would have an appropriate image... not just a screenshot of the working'.",
        "proposed_title_image": "High-res photograph of supermarket price tags on shelves with a basket, or an electronic fuel pump gauge showing rounding to the nearest pound/litre.",
        "body_diagram_status": "Number line diagram belongs inside the body of the lesson. It should show a dual number line (nearest 10, nearest 100, and 1 significant figure estimation benchmark)."
    },
    "functional-skills-fractions.html": {
        "title_photo": "kitchen_cooking_recipes/kitchen_scales.jpg",
        "title_concept": "Pastry chef scaling recipe ingredients (measuring 3/4 kg flour and 1/3 litre milk).",
        "why_title_flagged": "Hero title displays SVG bar models. Needs an authentic culinary/trade portioning photograph.",
        "proposed_title_image": "Baker portioning bread dough on wooden surface with dough cutter and fractional measuring scale.",
        "body_diagram_status": "Fraction bar models in the body are helpful, but need shaded grid segmentations with clear denominator bracket callouts."
    },
    "functional-skills-decimals.html": {
        "title_photo": "money_shopping_bills/coins_pounds.jpg",
        "title_concept": "Cashier counting British coins and banknote float during end-of-day till reconciliation.",
        "why_title_flagged": "Hero displays vertical column addition SVG. Needs a real currency/precision measurement visual.",
        "proposed_title_image": "UK currency coins (£2, £1, 50p, 20p, 10p, 5p) neatly stacked on a commercial till drawer.",
        "body_diagram_status": "Decimal place value chart in body should highlight the decimal point with a vertical neon highlight column and zero-padding rules."
    },
    "functional-skills-percentages.html": {
        "title_photo": "retail_shop/clothing_store.jpg",
        "title_concept": "High street store seasonal clearance with prominent '30% OFF EVERYTHING' and 'PLUS 5% EXTRA' sale tags.",
        "why_title_flagged": "Hero displays the bubble method calculation. Needs an authentic retail discount or VAT invoice photo.",
        "proposed_title_image": "High street retail window with bold 20% / 50% discount promotional signage.",
        "body_diagram_status": "Bubble method tree in body needs circular bubble nodes connected by directional curved arrows with distinct pastel fills."
    },
    "functional-skills-ratio.html": {
        "title_photo": "construction_trades/builder_measuring.jpg",
        "title_concept": "Builder mixing concrete according to statutory 1 : 2 : 4 ratio specification (cement : sand : gravel).",
        "why_title_flagged": "Hero displays SVG ratio bar blocks. Title should showcase the practical workplace application.",
        "proposed_title_image": "Concrete mixer and bags of aggregate materials on building site with measuring shovel.",
        "body_diagram_status": "Singapore bar model in body should have tactile, brick-like segmented blocks with bracket callouts for '1 part = £90'."
    },
    "functional-skills-speed.html": {
        "title_photo": "travel_transport_timetables/tube_underground.jpg",
        "title_concept": "London transport train operator tracking transit speed and timetable schedule.",
        "why_title_flagged": "Hero displays DST formula triangle. Formula triangle belongs in the body, not the hero title.",
        "proposed_title_image": "Train cab console with digital speedometer and railway signal track, or courier van GPS speedometer.",
        "body_diagram_status": "DST formula triangle in body needs interactive-looking 'cover-up' tabs showing the resulting formula when each variable is obscured."
    },
    "functional-skills-perimeter.html": {
        "title_photo": "home_diy_decorating/measuring_floor.jpg",
        "title_concept": "Carpenter measuring room perimeter boundary with laser distance measure for skirting boards.",
        "why_title_flagged": "Hero displays an L-shape perimeter sketch. Needs a real room installation or garden fencing photo.",
        "proposed_title_image": "Carpenter using a yellow tape measure along the base of a newly plastered wall for skirting boards.",
        "body_diagram_status": "Compound shape in body needs animated/dashed walking footprints around the perimeter with missing sides clearly color-coded."
    },
    "functional-skills-area.html": {
        "title_photo": "home_diy_decorating/paint_roller_wall.jpg",
        "title_concept": "Decorator calculating square meterage of walls to determine litres of paint required.",
        "why_title_flagged": "Hero displays compound L-shape area split sketch. Needs an authentic flooring or tiling application image.",
        "proposed_title_image": "Tiler laying ceramic square floor tiles with spacers and measuring tape on bathroom floor.",
        "body_diagram_status": "Compound L-shape diagram in body should clearly show the dashed partition cut separating Shape A (blue) from Shape B (amber)."
    },
    "functional-skills-volume.html": {
        "title_photo": "everyday_objects/delivery_parcel.jpg",
        "title_concept": "Warehouse forklift loading cubic pallet containers into freight shipping container.",
        "why_title_flagged": "Hero displays an isometric cuboid SVG. Needs real packaging/shipping warehouse logistics photography.",
        "proposed_title_image": "Stacked corrugated cardboard shipping boxes on wooden pallets in distribution centre.",
        "body_diagram_status": "3D cuboid diagram in body should have realistic 3D perspective shading and a translucent cutaway showing internal 1 cm³ unit cubes."
    },
    "functional-skills-circles.html": {
        "title_photo": "measuring_tools/circular_wheel.jpg",
        "title_concept": "Bicycle workshop mechanic measuring wheel circumference, rim diameter, and spoke radius.",
        "why_title_flagged": "Hero displays an annotated circle SVG with pi formulas. Needs an authentic circular engineering photo.",
        "proposed_title_image": "Close-up of precision bicycle wheel gear hub with circular disc brake and calibrated rim.",
        "body_diagram_status": "Circle diagram in body needs bold colour-coded radial lines (Radius = Emerald, Diameter = Sapphire, Circumference = Ruby)."
    },
    "functional-skills-angles.html": {
        "title_photo": "measuring_tools/ruler_geometry.jpg",
        "title_concept": "Architect using clear 360-degree protractor on technical drafting board to measure building angles.",
        "why_title_flagged": "Hero displays straight-line and triangle angle sketches. Needs a real drafting/carpentry photo.",
        "proposed_title_image": "Architectural drafting desk with 180° acrylic protractor, compass, and blueprint.",
        "body_diagram_status": "Angle diagrams in body should show clear arc wedges with angle measurements in contrasting badges."
    },
    "functional-skills-coordinates.html": {
        "title_photo": "maps_directions/compass_direction.jpg",
        "title_concept": "Marine navigator plotting coordinates and navigational waypoints on maritime nautical chart.",
        "why_title_flagged": "Hero displays a 4-quadrant Cartesian grid SVG. Needs a real navigation/radar/GPS photo.",
        "proposed_title_image": "Marine nautical chart with brass dividers and compass plotting latitude/longitude coordinates.",
        "body_diagram_status": "Cartesian grid in body needs prominent arrow markers illustrating the mnemonic 'Along the corridor (x), up the stairs (y)'."
    },
    "functional-skills-mean-median-mode-and-range.html": {
        "title_photo": "charts_data_screens/analytics_dashboard.jpg",
        "title_concept": "Quality control analyst examining hospital emergency department wait-time statistics on a dashboard.",
        "why_title_flagged": "Hero displays 4 math equation cards. Needs a real business analytics/data screen photo.",
        "proposed_title_image": "Dual analytics screens displaying patient wait-time averages, frequency curves, and performance metrics.",
        "body_diagram_status": "Averages summary in body should feature a visual comparison chart comparing how outliers distort the Mean vs the Median."
    },
    "functional-skills-probability.html": {
        "title_photo": "everyday_objects/probability_dice.jpg",
        "title_concept": "Quality assurance testing assessing component failure risk and defect probabilities.",
        "why_title_flagged": "Hero displays an SVG probability scale bar (0 to 1). Needs a real chance/gaming/risk analysis photo.",
        "proposed_title_image": "Macro photo of pair of red gaming dice showing rolled values, or clinical risk assessment matrix.",
        "body_diagram_status": "Probability scale in body should feature continuous gradient shading from crimson (0, Impossible) through amber (0.5) to emerald (1, Certain)."
    },
    "functional-skills-scatter-graphs.html": {
        "title_photo": "charts_data_screens/scatter_plot_graph.jpg",
        "title_concept": "Clinical research report plotting patient dosage levels against recovery time.",
        "why_title_flagged": "Hero displays a simple scatter plot SVG. Needs a professional statistical research publication visual.",
        "proposed_title_image": "Printed clinical research journal page showing scientific scatter plots with regression trendlines.",
        "body_diagram_status": "Scatter plot in body should clearly show the 'sandwich method' for drawing a balanced line of best fit."
    },
    "functional-skills-unit-conversions.html": {
        "title_photo": "measuring_tools/tape_measure.jpg",
        "title_concept": "Tradesperson using dual metric-imperial tape measure on construction project.",
        "why_title_flagged": "Hero displays metric staircase text boxes. Needs a real measuring tool photo.",
        "proposed_title_image": "Close-up of metal tape measure showing millimetres, centimetres, and inches against timber beam.",
        "body_diagram_status": "Metric staircase in body should have stepped physical stairs showing multiplication (going down) and division (going up)."
    },
    "functional-skills-pie-charts.html": {
        "title_photo": "charts_data_screens/pie_chart_analysis.jpg",
        "title_concept": "Corporate financial annual review document showing departmental expenditure breakdown by sector.",
        "why_title_flagged": "Hero displays an SVG pie chart with angle formula. Needs a real printed corporate report photo.",
        "proposed_title_image": "Glossy annual company report open on desk showing segmented 3D pie charts and financial percentages.",
        "body_diagram_status": "Pie chart diagram in body should clearly display protractor overlay showing how 90° and 180° angles are measured from 12 o'clock."
    }
}

# Extract current data from curriculum and visual catalog
maths_data = []
maths_photos_list = []
for fn, title in CURRICULUM_MATHS:
    photo, caption, _, _, svg = vcc.get_topic_visual(fn)
    maths_photos_list.append(photo)
    maths_data.append({
        "fn": fn,
        "title": title,
        "photo": photo,
        "caption": caption,
        "has_svg": bool(svg),
        "svg": svg
    })

english_data = []
english_photos_list = []
for fn, title in CURRICULUM_ENGLISH:
    photo, caption, _, _, svg = vcc.get_topic_visual(fn)
    english_photos_list.append(photo)
    english_data.append({
        "fn": fn,
        "title": title,
        "photo": photo,
        "caption": caption,
        "has_svg": bool(svg),
        "svg": svg
    })

maths_counts = Counter(maths_photos_list)
english_counts = Counter(english_photos_list)


def generate_full_audit_html():
    maths_cards_html = ""
    for idx, item in enumerate(maths_data, 1):
        fn = item["fn"]
        title = item["title"]
        photo = item["photo"]
        caption = item["caption"]
        has_svg = item["has_svg"]
        svg_content = item["svg"]

        # Lookup proposal or generate default
        prop = PROPOSED_MATHS.get(fn, {
            "title_photo": photo,
            "title_concept": caption,
            "why_title_flagged": "Hero displays an SVG calculation screenshot rather than an authentic vocational scene." if has_svg else "Stock photo connection is weak or generic.",
            "proposed_title_image": f"Authentic workplace photograph representing {title} in practical adult life (e.g. trades, healthcare, retail, or transport).",
            "body_diagram_status": "Lesson diagram needs clean mathematical styling, clear axis scaling, and contrasting callouts."
        })

        # Visual thumbnail currently displayed in hero
        if has_svg and svg_content:
            current_visual_render = f"""
            <div class="visual-badge-flagged"><i class="fa-solid fa-triangle-exclamation"></i> Flagged: Screenshot of Working</div>
            <div class="svg-preview-box">{svg_content}</div>
            """
        else:
            current_visual_render = f"""
            <div class="visual-badge-photo"><i class="fa-solid fa-image"></i> Photo Asset</div>
            <div class="photo-preview-box">
              <img src="assets/img/book_photos/{photo}" alt="{title}" loading="lazy" />
            </div>
            """

        maths_cards_html += f"""
        <div class="audit-card" id="maths-{idx}" data-subject="maths">
          <div class="audit-card-header">
            <div class="header-left">
              <span class="topic-index">Maths #{idx}</span>
              <h3 class="topic-name">{title}</h3>
            </div>
            <div class="header-right">
              <a href="{fn}" target="_blank" class="btn-view-live"><i class="fa-solid fa-arrow-up-right-from-square"></i> View Page</a>
            </div>
          </div>

          <div class="audit-grid">
            <!-- CURRENT VISUAL COLUMN -->
            <div class="audit-col current-col">
              <div class="col-title"><i class="fa-solid fa-eye"></i> What is Currently Shown</div>
              {current_visual_render}
              <div class="current-meta">
                <p><strong>Mapped Caption / Context:</strong> {caption}</p>
                <div class="flag-explanation">
                  <strong>Issue Flagged:</strong> {prop['why_title_flagged']}
                </div>
              </div>
            </div>

            <!-- PROPOSED SOLUTION COLUMN -->
            <div class="audit-col proposed-col">
              <div class="col-title"><i class="fa-solid fa-lightbulb"></i> Proposed Solution for Your Approval</div>
              
              <div class="proposal-box">
                <div class="prop-subheading"><i class="fa-solid fa-camera"></i> 1. Proposed Hero Title Image:</div>
                <p class="prop-text"><strong>Concept:</strong> {prop['proposed_title_image']}</p>
                <div class="recommended-action-badge">
                  <i class="fa-solid fa-arrow-right"></i> Move working-out calculations strictly to lesson body; use authentic high-res context photo for title hero.
                </div>
              </div>

              <div class="proposal-box" style="margin-top:14px;">
                <div class="prop-subheading"><i class="fa-solid fa-chart-line"></i> 2. Proposed Body Diagram Upgrade:</div>
                <p class="prop-text">{prop['body_diagram_status']}</p>
              </div>

              <!-- INTERACTIVE FEEDBACK BOX -->
              <div class="feedback-action-box">
                <div class="feedback-heading">Your Decision for This Topic:</div>
                <div class="feedback-options">
                  <label class="radio-label">
                    <input type="radio" name="decision-{fn}" value="approve" checked> <span>✓ Approve Proposed Change</span>
                  </label>
                  <label class="radio-label">
                    <input type="radio" name="decision-{fn}" value="custom"> <span>✎ I Have a Suggestion</span>
                  </label>
                  <label class="radio-label">
                    <input type="radio" name="decision-{fn}" value="keep"> <span>✕ Keep Current</span>
                  </label>
                </div>
                <textarea class="feedback-textarea" id="note-{fn}" placeholder="Add your specific feedback or image ideas for {title}..."></textarea>
              </div>
            </div>
          </div>
        </div>
        """

    english_cards_html = ""
    for idx, item in enumerate(english_data, 1):
        fn = item["fn"]
        title = item["title"]
        photo = item["photo"]
        caption = item["caption"]
        count = english_counts.get(photo, 1)

        prop = PROPOSED_ENGLISH.get(fn, {
            "concept": "Unique workplace non-fiction reading/writing scenario matching exact unit title.",
            "why": f"Currently reuses {photo} ({count}x).",
            "photo_file": "workplace_office/desk_laptop.jpg",
            "unsplash_search": "office paperwork writing"
        })

        repeat_warning = ""
        if count > 1:
            repeat_warning = f'<span class="badge-repeated"><i class="fa-solid fa-repeat"></i> Repeated {count} Times in English</span>'

        english_cards_html += f"""
        <div class="audit-card" id="english-{idx}" data-subject="english">
          <div class="audit-card-header">
            <div class="header-left">
              <span class="topic-index">English #{idx}</span>
              <h3 class="topic-name">{title}</h3>
              {repeat_warning}
            </div>
            <div class="header-right">
              <a href="{fn}" target="_blank" class="btn-view-live"><i class="fa-solid fa-arrow-up-right-from-square"></i> View Page</a>
            </div>
          </div>

          <div class="audit-grid">
            <!-- CURRENT VISUAL COLUMN -->
            <div class="audit-col current-col">
              <div class="col-title"><i class="fa-solid fa-eye"></i> Current Photo (Repeated)</div>
              <div class="photo-preview-box">
                <img src="assets/img/book_photos/{photo}" alt="{title}" loading="lazy" />
              </div>
              <div class="current-meta">
                <p><strong>Current File:</strong> <code>{photo}</code></p>
                <p><strong>Current Context:</strong> {caption}</p>
                <div class="flag-explanation">
                  <strong>Issue:</strong> {prop['why']}
                </div>
              </div>
            </div>

            <!-- PROPOSED SOLUTION COLUMN -->
            <div class="audit-col proposed-col">
              <div class="col-title"><i class="fa-solid fa-wand-magic-sparkles"></i> Proposed Unique Replacement</div>
              
              <div class="proposal-box">
                <div class="prop-subheading"><i class="fa-solid fa-camera-retro"></i> Curated Distinct Visual:</div>
                <p class="prop-text"><strong>Visual Concept:</strong> {prop['concept']}</p>
                <p class="prop-text" style="font-size:0.88rem; color:#64748b; margin-top:6px;">
                  <strong>Recommended Unsplash Query:</strong> <code>{prop['unsplash_search']}</code>
                </p>
                <div class="recommended-action-badge">
                  <i class="fa-solid fa-check"></i> Replaces generic laptop/desk with dedicated subject-accurate photography.
                </div>
              </div>

              <!-- INTERACTIVE FEEDBACK BOX -->
              <div class="feedback-action-box">
                <div class="feedback-heading">Your Decision for This Topic:</div>
                <div class="feedback-options">
                  <label class="radio-label">
                    <input type="radio" name="decision-{fn}" value="approve" checked> <span>✓ Approve Proposed Photo</span>
                  </label>
                  <label class="radio-label">
                    <input type="radio" name="decision-{fn}" value="custom"> <span>✎ I Have a Suggestion</span>
                  </label>
                  <label class="radio-label">
                    <input type="radio" name="decision-{fn}" value="keep"> <span>✕ Keep Current</span>
                  </label>
                </div>
                <textarea class="feedback-textarea" id="note-{fn}" placeholder="Add your feedback or suggest an image for {title}..."></textarea>
              </div>
            </div>
          </div>
        </div>
        """

    full_html = f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Master Functional Skills — Visual Image & Diagram Audit Catalog</title>
  <link rel="stylesheet" href="assets/css/mfs-theme.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <style>
    :root {{
      --navy: #070d1e;
      --navy-light: #0d1e3d;
      --accent: #2563eb;
      --amber: #f59e0b;
      --emerald: #10b981;
      --crimson: #e11d48;
      --bg-audit: #f8fafc;
      --card-bg: #ffffff;
      --border-color: #cbd5e1;
    }}
    body {{
      font-family: 'Inter', system-ui, -apple-system, sans-serif;
      margin: 0;
      padding: 0;
      background: var(--bg-audit);
      color: #0f172a;
      line-height: 1.6;
    }}
    .audit-header {{
      background: linear-gradient(135deg, var(--navy) 0%, var(--navy-light) 100%);
      color: #ffffff;
      padding: 40px 24px;
      border-bottom: 4px solid var(--accent);
    }}
    .audit-header-inner {{
      max-width: 1500px;
      margin: 0 auto;
    }}
    .audit-title {{
      font-size: 2.2rem;
      font-weight: 800;
      margin: 0 0 10px 0;
      letter-spacing: -0.02em;
    }}
    .audit-title span {{
      color: #38bdf8;
    }}
    .audit-subtitle {{
      font-size: 1.15rem;
      color: #cbd5e1;
      max-width: 900px;
      margin: 0 0 24px 0;
    }}
    .stats-bar {{
      display: flex;
      gap: 16px;
      flex-wrap: wrap;
    }}
    .stat-pill {{
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid rgba(255, 255, 255, 0.2);
      padding: 8px 16px;
      border-radius: 8px;
      font-size: 0.92rem;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .stat-pill strong {{
      color: #38bdf8;
      font-size: 1.1rem;
    }}

    /* Navigation Bar */
    .audit-nav-bar {{
      background: #ffffff;
      border-bottom: 1px solid var(--border-color);
      position: sticky;
      top: 0;
      z-index: 1000;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }}
    .audit-nav-inner {{
      max-width: 1500px;
      margin: 0 auto;
      padding: 12px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
    }}
    .nav-tabs {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }}
    .btn-tab {{
      background: #f1f5f9;
      border: 1px solid #cbd5e1;
      padding: 8px 18px;
      border-radius: 20px;
      font-size: 0.92rem;
      font-weight: 700;
      color: #475569;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .btn-tab.active, .btn-tab:hover {{
      background: var(--accent);
      color: #ffffff;
      border-color: var(--accent);
    }}
    .btn-export {{
      background: #059669;
      color: #ffffff;
      border: none;
      padding: 9px 20px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.92rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: background 0.2s;
    }}
    .btn-export:hover {{
      background: #047857;
    }}

    /* Main Container */
    .audit-container {{
      max-width: 1500px;
      margin: 32px auto;
      padding: 0 24px 80px;
    }}

    /* Section Banner */
    .section-banner {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-left: 6px solid var(--accent);
      border-radius: 10px;
      padding: 20px 24px;
      margin-bottom: 24px;
    }}
    .section-banner h2 {{
      margin: 0 0 6px 0;
      font-size: 1.4rem;
      color: var(--navy);
    }}
    .section-banner p {{
      margin: 0;
      color: #475569;
      font-size: 0.98rem;
    }}

    /* Audit Card */
    .audit-card {{
      background: var(--card-bg);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      margin-bottom: 24px;
      box-shadow: 0 3px 10px rgba(0,0,0,0.03);
      overflow: hidden;
      transition: transform 0.2s, box-shadow 0.2s;
    }}
    .audit-card:hover {{
      box-shadow: 0 6px 16px rgba(0,0,0,0.06);
    }}
    .audit-card-header {{
      background: #f8fafc;
      border-bottom: 1px solid #e2e8f0;
      padding: 14px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
    }}
    .header-left {{
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }}
    .topic-index {{
      background: #0f172a;
      color: #ffffff;
      font-size: 0.78rem;
      font-weight: 800;
      text-transform: uppercase;
      padding: 4px 10px;
      border-radius: 6px;
      letter-spacing: 0.05em;
    }}
    .topic-name {{
      margin: 0;
      font-size: 1.25rem;
      font-weight: 800;
      color: #0f172a;
    }}
    .btn-view-live {{
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      color: var(--accent);
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 0.85rem;
      font-weight: 700;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}
    .btn-view-live:hover {{
      background: var(--accent);
      color: #ffffff;
    }}
    .badge-repeated {{
      background: #fef3c7;
      color: #92400e;
      border: 1px solid #fde68a;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 6px;
    }}

    /* 2-Column Grid */
    .audit-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      padding: 20px;
    }}
    @media (max-width: 900px) {{
      .audit-grid {{
        grid-template-columns: 1fr;
      }}
    }}
    .audit-col {{
      display: flex;
      flex-direction: column;
    }}
    .col-title {{
      font-size: 0.95rem;
      font-weight: 800;
      color: #334155;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .current-col {{
      background: #fafaf9;
      border: 1px solid #e7e5e4;
      border-radius: 8px;
      padding: 16px;
    }}
    .proposed-col {{
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      border-radius: 8px;
      padding: 16px;
    }}

    /* Previews */
    .visual-badge-flagged {{
      background: #fee2e2;
      color: #991b1b;
      border: 1px solid #fca5a5;
      font-size: 0.8rem;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 4px;
      margin-bottom: 8px;
      display: inline-block;
    }}
    .visual-badge-photo {{
      background: #e0f2fe;
      color: #0369a1;
      border: 1px solid #bae6fd;
      font-size: 0.8rem;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 4px;
      margin-bottom: 8px;
      display: inline-block;
    }}
    .svg-preview-box {{
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      padding: 10px;
      margin-bottom: 12px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }}
    .photo-preview-box {{
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      overflow: hidden;
      margin-bottom: 12px;
      max-height: 220px;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .photo-preview-box img {{
      width: 100%;
      height: 220px;
      object-fit: cover;
      display: block;
    }}
    .current-meta {{
      font-size: 0.9rem;
      color: #475569;
    }}
    .current-meta p {{
      margin: 4px 0;
    }}
    .flag-explanation {{
      background: #fff1f2;
      border: 1px solid #fecdd3;
      border-left: 4px solid var(--crimson);
      border-radius: 6px;
      padding: 8px 12px;
      color: #881337;
      margin-top: 10px;
      font-size: 0.88rem;
    }}

    /* Proposal Card */
    .proposal-box {{
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      padding: 14px 16px;
    }}
    .prop-subheading {{
      font-size: 0.95rem;
      font-weight: 800;
      color: #065f46;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .prop-text {{
      font-size: 0.94rem;
      color: #1e293b;
      margin: 0;
      line-height: 1.5;
    }}
    .recommended-action-badge {{
      margin-top: 10px;
      background: #ecfdf5;
      border: 1px solid #a7f3d0;
      color: #065f46;
      font-size: 0.84rem;
      font-weight: 700;
      padding: 6px 10px;
      border-radius: 6px;
    }}

    /* Feedback Form Elements */
    .feedback-action-box {{
      margin-top: 16px;
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      padding: 14px 16px;
    }}
    .feedback-heading {{
      font-size: 0.88rem;
      font-weight: 800;
      color: #0f172a;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-bottom: 10px;
    }}
    .feedback-options {{
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
      margin-bottom: 10px;
    }}
    .radio-label {{
      font-size: 0.88rem;
      font-weight: 600;
      color: #334155;
      display: flex;
      align-items: center;
      gap: 6px;
      cursor: pointer;
    }}
    .feedback-textarea {{
      width: 100%;
      box-sizing: border-box;
      height: 65px;
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      padding: 8px 10px;
      font-family: inherit;
      font-size: 0.88rem;
      resize: vertical;
      outline: none;
    }}
    .feedback-textarea:focus {{
      border-color: var(--accent);
      box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15);
    }}
  </style>
</head>
<body>

  <!-- HEADER -->
  <header class="audit-header">
    <div class="audit-header-inner">
      <h1 class="audit-title">Master Functional Skills &mdash; <span>Image &amp; Diagram Audit Catalog</span></h1>
      <p class="audit-subtitle">
        Comprehensive visual review document mapping all images and diagrams across the website and A4 publication suites. Use this draft to review current visuals, assess topic connections, and approve or customize proposed replacements.
      </p>

      <div class="stats-bar">
        <div class="stat-pill"><i class="fa-solid fa-calculator"></i> <span>Maths Units:</span> <strong>48 Topics</strong></div>
        <div class="stat-pill"><i class="fa-solid fa-pen-nib"></i> <span>English Units:</span> <strong>27 Topics</strong></div>
        <div class="stat-pill"><i class="fa-solid fa-repeat" style="color:#f59e0b;"></i> <span>Repetitions Flagged:</span> <strong>5 English Stock Photos</strong></div>
        <div class="stat-pill"><i class="fa-solid fa-triangle-exclamation" style="color:#ef4444;"></i> <span>Maths Title Flaws:</span> <strong>Raw Calculation Screenshots</strong></div>
      </div>
    </div>
  </header>

  <!-- STICKY NAV BAR -->
  <nav class="audit-nav-bar">
    <div class="audit-nav-inner">
      <div class="nav-tabs">
        <button class="btn-tab active" onclick="filterCards('all')">All Units (75)</button>
        <button class="btn-tab" onclick="filterCards('maths')">Maths Units (48)</button>
        <button class="btn-tab" onclick="filterCards('english')">English Units (27)</button>
      </div>
      <div>
        <button class="btn-export" onclick="exportFeedback()"><i class="fa-solid fa-download"></i> Save / Export My Feedback</button>
      </div>
    </div>
  </nav>

  <!-- MAIN CONTAINER -->
  <main class="audit-container">

    <!-- MATHS SECTION -->
    <div id="maths-section">
      <div class="section-banner">
        <h2><i class="fa-solid fa-calculator" style="color:var(--accent);"></i> Section 1: Mathematics Revision Units (48 Topics)</h2>
        <p>
          <strong>User Feedback Addressed:</strong> Hero titles must not be raw screenshots of calculations (e.g. partition grids, short division brackets). Below, every topic's current visual is displayed alongside a proposed authentic real-world workplace photograph for the title, and a professional vector diagram specification for the lesson body.
        </p>
      </div>
      {maths_cards_html}
    </div>

    <!-- ENGLISH SECTION -->
    <div id="english-section">
      <div class="section-banner" style="border-left-color: #059669; margin-top:40px;">
        <h2><i class="fa-solid fa-pen-nib" style="color:#059669;"></i> Section 2: English Revision Units (27 Topics)</h2>
        <p>
          <strong>User Feedback Addressed:</strong> Current English photos are acceptable in quality but heavily repeat (e.g. <code>desk_laptop.jpg</code> and <code>student_studying_laptop.jpg</code> appear 5 times each). Below is a curated proposal for distinct, topic-specific photography (e.g. authentic newspapers for Fact vs Opinion, dictionaries with highlighters for Word Meaning, letters on letterhead for Communication).
        </p>
      </div>
      {english_cards_html}
    </div>

  </main>

  <script>
    function filterCards(subject) {{
      document.querySelectorAll('.btn-tab').forEach(b => b.classList.remove('active'));
      event.target.classList.add('active');

      const cards = document.querySelectorAll('.audit-card');
      const mathsSec = document.getElementById('maths-section');
      const engSec = document.getElementById('english-section');

      if (subject === 'all') {{
        mathsSec.style.display = 'block';
        engSec.style.display = 'block';
        cards.forEach(c => c.style.display = 'block');
      }} else if (subject === 'maths') {{
        mathsSec.style.display = 'block';
        engSec.style.display = 'none';
        cards.forEach(c => {{
          c.style.display = c.dataset.subject === 'maths' ? 'block' : 'none';
        }});
      }} else if (subject === 'english') {{
        mathsSec.style.display = 'none';
        engSec.style.display = 'block';
        cards.forEach(c => {{
          c.style.display = c.dataset.subject === 'english' ? 'block' : 'none';
        }});
      }}
    }}

    function exportFeedback() {{
      const feedbackData = [];
      document.querySelectorAll('.audit-card').forEach(card => {{
        const id = card.id;
        const title = card.querySelector('.topic-name').innerText;
        const decisionInput = card.querySelector('input[type="radio"]:checked');
        const decision = decisionInput ? decisionInput.value : 'approve';
        const note = card.querySelector('.feedback-textarea').value.trim();
        
        feedbackData.push({{
          id: id,
          topic: title,
          decision: decision,
          notes: note
        }});
      }});

      const jsonStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(feedbackData, null, 2));
      const dl = document.createElement('a');
      dl.setAttribute("href", jsonStr);
      dl.setAttribute("download", "mfs_image_audit_feedback.json");
      document.body.appendChild(dl);
      dl.click();
      dl.remove();
      alert("Feedback exported successfully! You can share this file or review notes.");
    }}
  </script>
</body>
</html>
"""

    out_file = "/home/subi/Projects/masterfunctionalskills.co.uk/image_audit_catalog.html"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Audit catalog HTML generated at: {out_file}")

generate_full_audit_html()
