#!/usr/bin/env python3
"""
Sprint 6: Build & Inject Bespoke "No-Squinting" Visual Master Boards
across all 16 Maths Level 2 and 26 Maths Level 1 topic pages that lack one.
Idempotent: replaces or inserts cleanly right before <section id="golden-rules".
"""

from pathlib import Path
import re

ROOT = Path("/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk")


def wrap_board(level: str, title: str, badge_label: str, icon: str, body_html: str) -> str:
    badge_cls = "math-visual-badge-l1" if level == "L1" else "math-visual-badge-l2"
    border_col = "#86efac" if level == "L1" else "#fcd34d"
    return (
        f'    <section class="revision-section mfs-visual-master-board" data-mfs-visual-board="sprint6" aria-label="{title}">\n'
        f'      <div class="math-visual-card" style="border-color:{border_col};">\n'
        f'        <div class="math-visual-card-header">\n'
        f'          <div class="math-visual-title"><i class="fa-solid {icon}"></i> {title}</div>\n'
        f'          <span class="math-visual-badge {badge_cls}">{badge_label}</span>\n'
        f'        </div>\n'
        f'{body_html}\n'
        f'      </div>\n'
        f'    </section>\n\n'
    )


def table_wrap(headers: list[str], rows: list[list[str]], l1: bool = False) -> str:
    th_style = ' style="background:#15803d;"' if l1 else ""
    ths = "".join(f"<th{th_style}>{h}</th>" for h in headers)
    trs = []
    for r in rows:
        tds = "".join(f"<td>{c}</td>" for c in r)
        trs.append(f"<tr>{tds}</tr>")
    return (
        '<div class="math-master-table-wrap">\n'
        '  <table class="math-master-table">\n'
        f'    <thead><tr>{ths}</tr></thead>\n'
        f'    <tbody>{"".join(trs)}</tbody>\n'
        '  </table>\n'
        '</div>'
    )


def pastel_grid(cards: list[tuple[str, str, str, str]]) -> str:
    # card = (variant: sky|mint|amber|teal, label, math, note)
    out = ['<div class="mfs-pastel-grid">']
    for var, lbl, math_txt, note in cards:
        out.append(
            f'  <div class="mfs-pastel-card mfs-pastel-{var}">'
            f'<div class="mfs-pastel-label">{lbl}</div>'
            f'<div class="mfs-pastel-math">{math_txt}</div>'
            f'<div class="mfs-pastel-note">{note}</div>'
            f'</div>'
        )
    out.append("</div>")
    return "\n".join(out)


# ==============================================================================
# 16 MATHS LEVEL 2 VISUAL MASTER BOARDS
# ==============================================================================
L2_BOARDS: dict[str, tuple[str, str, str]] = {
    "functional-skills-3d-shapes.html": (
        "3D Solids Master Table &amp; Euler Check (Level 2)",
        "fa-cubes",
        table_wrap(
            ["3D Solid", "Faces (F)", "Edges (E)", "Vertices (V)", "Euler Check (F + V &minus; E)"],
            [
                ["<strong>Cube</strong>", "6 squares", "12", "8", "6 + 8 &minus; 12 = <strong>2</strong>"],
                ["<strong>Cuboid</strong>", "6 rectangles", "12", "8", "6 + 8 &minus; 12 = <strong>2</strong>"],
                ["<strong>Triangular Prism</strong>", "5 (2 tri + 3 rect)", "9", "6", "5 + 6 &minus; 9 = <strong>2</strong>"],
                ["<strong>Square-Based Pyramid</strong>", "5 (1 sq + 4 tri)", "8", "5", "5 + 5 &minus; 8 = <strong>2</strong>"],
                ["<strong>Cylinder</strong>", "3 (2 circles + 1 curved)", "2 curved", "0", "Curved surface"],
                ["<strong>Cone</strong>", "2 (1 circle + 1 curved)", "1 curved", "1 apex", "Curved surface"],
                ["<strong>Sphere</strong>", "1 curved surface", "0", "0", "Curved surface"],
            ],
        ),
    ),
    "functional-skills-comparing-data-sets.html": (
        "Data Comparison Decision Board (Average + Consistency)",
        "fa-scale-balanced",
        table_wrap(
            ["Measure", "What It Tells You", "Example: Day vs Night Shift", "Full-Mark Exam Sentence"],
            [
                [
                    "<strong>Mean or Median</strong><br>(Average)",
                    "Typical performance or middle value",
                    "Day: <strong>96.5%</strong> vs Night: <strong>94.0%</strong>",
                    "Day Shift had a higher average accuracy (96.5% vs 94.0%).",
                ],
                [
                    "<strong>Range</strong><br>(Highest &minus; Lowest)",
                    "Spread &amp; consistency (smaller = more consistent)",
                    "Day: <strong>4.0%</strong> vs Night: <strong>9.0%</strong>",
                    "Day Shift was more consistent because its range was smaller (4.0% vs 9.0%).",
                ],
            ],
        )
        + pastel_grid([
            ("amber", "Higher Is Better", "Sales, Test Scores, Accuracy", "Higher mean/median wins; smaller range = more consistent."),
            ("sky", "Lower Is Better", "Waiting Times, Delays, Defects", "Lower mean/median is faster/better; smaller range = more predictable."),
        ]),
    ),
    "functional-skills-density.html": (
        "Density, Mass &amp; Volume Step-Down Board (Level 2)",
        "fa-cube",
        pastel_grid([
            ("sky", "Stage 1: Match Units First", "g with cm&sup3; | kg with m&sup3;", "1 kg = 1,000 g &bull; 1,000 cm&sup3; = 1 Litre."),
            ("amber", "Stage 2: Density Triangle", "M = D &times; V &bull; D = M &divide; V", "Cover the quantity you need to reveal &times; or &divide;."),
            ("mint", "Stage 3: Worked Check", "0.6 m&sup3; &times; 2,400 kg/m&sup3; = 1,440 kg", "Cuboid (1.5 &times; 0.8 &times; 0.5 = 0.6 m&sup3;) &rarr; 1,440 kg."),
        ]),
    ),
    "functional-skills-estimating-the-mean.html": (
        "Estimated Mean from Grouped Data Master Board",
        "fa-table-cells",
        table_wrap(
            ["Time Interval (mins)", "Midpoint (x)", "Frequency (f)", "Midpoint &times; Freq (f &times; x)"],
            [
                ["0 &le; t &lt; 10", "<strong>5</strong>", "4", "5 &times; 4 = <strong>20</strong>"],
                ["10 &le; t &lt; 20", "<strong>15</strong>", "10", "15 &times; 10 = <strong>150</strong>"],
                ["20 &le; t &lt; 30", "<strong>25</strong>", "6", "25 &times; 6 = <strong>150</strong>"],
                ["<strong>Totals</strong>", "&mdash;", "<strong>&Sigma;f = 20</strong>", "<strong>&Sigma;(f &times; x) = 320</strong>"],
            ],
        )
        + pastel_grid([
            ("sky", "Step 1: Find Midpoints", "(Lower + Upper) &divide; 2", "Midpoint of 10 to 20 is (10 + 20) &divide; 2 = 15."),
            ("amber", "Step 2: Divide by Total Freq", "320 &divide; 20 = 16 mins", "NEVER divide by the number of groups (3)! Always divide by &Sigma;f (20)."),
        ]),
    ),
    "functional-skills-formulas.html": (
        "BIDMAS Substitution &amp; Rearranging Master Board",
        "fa-square-root-variable",
        pastel_grid([
            ("sky", "Forward: Substitute &amp; BIDMAS", "C = 35h + 25 (h = 4)", "Multiply first: 35 &times; 4 = 140 &rarr; 140 + 25 = <strong>&pound;165</strong>."),
            ("amber", "Powers &amp; Brackets First", "A = 3.14 &times; 5&sup2;", "Square radius first (5&sup2; = 25), then 3.14 &times; 25 = <strong>78.5</strong>."),
            ("mint", "Reverse: Undo Outer Ops First", "165 = 35h + 25", "Subtract 25 first (140), then divide by 35 &rarr; <strong>h = 4</strong>."),
        ]),
    ),
    "functional-skills-maps-and-scale-drawings.html": (
        "Scale Ratios &amp; Map Conversion Master Table (Level 2)",
        "fa-map-location-dot",
        table_wrap(
            ["Map / Plan Scale", "1 cm on Plan Equals", "Real Distance for 6 cm", "Direction Rule"],
            [
                ["<strong>1 : 50</strong>", "50 cm = <strong>0.5 m</strong>", "6 &times; 0.5 = <strong>3 m</strong>", "Plan &rarr; Real: &times; scale factor"],
                ["<strong>1 : 100</strong>", "100 cm = <strong>1 m</strong>", "6 &times; 1 = <strong>6 m</strong>", "Real &rarr; Plan: &divide; scale factor"],
                ["<strong>1 : 200</strong>", "200 cm = <strong>2 m</strong>", "6 &times; 2 = <strong>12 m</strong>", "Convert m to cm (&times;100) first"],
                ["<strong>1 : 25,000</strong>", "250 m = <strong>0.25 km</strong>", "6 &times; 0.25 = <strong>1.5 km</strong>", "4 cm = 1 km"],
                ["<strong>1 : 50,000</strong>", "500 m = <strong>0.5 km</strong>", "6 &times; 0.5 = <strong>3.0 km</strong>", "2 cm = 1 km"],
            ],
        ),
    ),
    "functional-skills-nets.html": (
        "3D Solids to Flat 2D Nets Master Reference Table (Level 2)",
        "fa-box-open",
        table_wrap(
            ["3D Shape", "Exact Faces in Flat Net", "Distinct Nets / Key Check"],
            [
                ["<strong>Cube</strong>", "6 identical squares", "<strong>11 valid cube nets</strong> (never 5-in-a-row or U-loop)"],
                ["<strong>Cuboid</strong>", "6 rectangles (3 equal opposite pairs)", "Opposite pairs match when folded 90&deg;"],
                ["<strong>Triangular Prism</strong>", "2 identical triangles + 3 rectangles", "Triangle side lengths match rectangle edges"],
                ["<strong>Square-Based Pyramid</strong>", "1 square base + 4 identical triangles", "4 triangles meet at 1 top apex"],
                ["<strong>Cylinder</strong>", "2 circles + 1 curved rectangle", "Rectangle length = Circle circumference (&pi;d)"],
            ],
        ),
    ),
    "functional-skills-plans-and-elevations.html": (
        "Engineering 3-View Dimension Mapping Board (Level 2)",
        "fa-compass-drafting",
        table_wrap(
            ["2D Orthographic View", "Viewing Direction", "Dimensions Shown (L=6, W=4, H=3)", "Grid Footprint"],
            [
                ["<strong>Plan View</strong>", "Directly from ABOVE (bird's eye)", "Length &times; Width", "<strong>6 cm &times; 4 cm</strong>"],
                ["<strong>Front Elevation</strong>", "Straight on from the FRONT", "Length &times; Height", "<strong>6 cm &times; 3 cm</strong>"],
                ["<strong>Side Elevation</strong>", "Straight on from LEFT / RIGHT", "Width &times; Height", "<strong>4 cm &times; 3 cm</strong>"],
            ],
        ),
    ),
    "functional-skills-surface-area.html": (
        "Surface Area Unwrapped Faces Master Board (Level 2)",
        "fa-layer-group",
        pastel_grid([
            ("sky", "Closed Cuboid (6 Faces)", "2LW + 2LH + 2WH", "5 &times; 3 &times; 2 cm: 2(15) + 2(10) + 2(6) = <strong>62 cm&sup2;</strong>."),
            ("amber", "Open-Top Tank (5 Faces)", "LW + 2LH + 2WH", "Omit the top lid! Count only 1 base + 4 side walls."),
            ("mint", "Cylinder (&pi; = 3.14)", "2&pi;r&sup2; + 2&pi;rh", "r = 4, h = 10: 2(50.24) + 251.20 = <strong>351.68 cm&sup2;</strong>."),
        ]),
    ),
    "functional-skills-symmetry-and-2d-shapes.html": (
        "2D Polygons, Symmetry &amp; Angle Sums Master Table (Level 2)",
        "fa-shapes",
        table_wrap(
            ["2D Shape", "Lines of Symmetry", "Rotational Order", "Interior Angle Sum"],
            [
                ["<strong>Equilateral Triangle</strong>", "3", "Order 3", "180&deg; (60&deg; each)"],
                ["<strong>Isosceles Triangle</strong>", "1", "Order 1", "180&deg; (2 base angles equal)"],
                ["<strong>Square</strong>", "4", "Order 4", "360&deg; (4 &times; 90&deg;)"],
                ["<strong>Rectangle</strong>", "2", "Order 2", "360&deg; (4 &times; 90&deg;)"],
                ["<strong>Parallelogram</strong>", "0", "Order 2", "360&deg; (opposite angles equal)"],
                ["<strong>Regular Pentagon / Hexagon</strong>", "5 / 6", "Order 5 / 6", "540&deg; / 720&deg;"],
            ],
        ),
    ),
    "functional-skills-best-buys.html": (
        "Best Buys &amp; Unit Pricing Comparison Board (Level 2)",
        "fa-tags",
        pastel_grid([
            ("sky", "Pack A: 400 g for &pound;2.40", "&pound;2.40 &divide; 4 = &pound;0.60 / 100 g", "Divide price by number of 100 g units (400 &divide; 100 = 4)."),
            ("mint", "Pack B: 650 g for &pound;3.25", "&pound;3.25 &divide; 6.5 = &pound;0.50 / 100 g", "<strong>Better Value!</strong> Cheaper per 100 g (&pound;0.50 vs &pound;0.60)."),
            ("amber", "Multi-Buy Trap Check", "250 g &times; 3 vs 750 g", "Calculate exact cost per 100 g or per 1 kg AFTER applying offers."),
        ]),
    ),
    "functional-skills-circles.html": (
        "Circles Visual Formula Board (&pi; = 3.14, Level 2)",
        "fa-circle-dot",
        pastel_grid([
            ("sky", "Radius vs Diameter", "d = 2 &times; r &bull; r = d &divide; 2", "If Diameter d = 10 cm, Radius r = <strong>5 cm</strong>."),
            ("amber", "Circumference (Edge)", "C = &pi; &times; d = 31.4 cm", "3.14 &times; 10 = 31.4 cm. Semi-circle perimeter = &frac12;&pi;d + d = <strong>25.7 cm</strong>."),
            ("mint", "Area (Inside Space)", "A = &pi; &times; r&sup2; = 78.5 cm&sup2;", "3.14 &times; 5 &times; 5 = <strong>78.5 cm&sup2;</strong> (never use d in &pi;r&sup2;!)."),
        ]),
    ),
    "functional-skills-coordinates.html": (
        "4-Quadrant Coordinates &amp; Midpoint Master Board (Level 2)",
        "fa-border-all",
        table_wrap(
            ["Quadrant", "X-Direction (Along)", "Y-Direction (Up / Down)", "Sign Pair &amp; Midpoint Rule"],
            [
                ["<strong>Quadrant 1</strong> (Top Right)", "Right (+)", "Up (+)", "<strong>(+x, +y)</strong> e.g. (4, 3)"],
                ["<strong>Quadrant 2</strong> (Top Left)", "Left (&minus;)", "Up (+)", "<strong>(&minus;x, +y)</strong> e.g. (&minus;4, 3)"],
                ["<strong>Quadrant 3</strong> (Bottom Left)", "Left (&minus;)", "Down (&minus;)", "<strong>(&minus;x, &minus;y)</strong> e.g. (&minus;4, &minus;3)"],
                ["<strong>Quadrant 4</strong> (Bottom Right)", "Right (+)", "Down (&minus;)", "<strong>(+x, &minus;y)</strong> e.g. (4, &minus;3)"],
            ],
        )
        + pastel_grid([
            ("sky", "Midpoint Formula", "((x&sub1;+x&sub2;)&divide;2 , (y&sub1;+y&sub2;)&divide;2)", "Between (2, 6) and (8, &minus;2): ((2+8)&divide;2, (6&minus;2)&divide;2) = <strong>(5, 2)</strong>."),
        ]),
    ),
    "functional-skills-interest-and-compound-interest.html": (
        "Simple vs Compound Interest Master Table (&pound;2,000 at 5%)",
        "fa-piggy-bank",
        table_wrap(
            ["Year", "Simple Interest (5% of &pound;2,000)", "Compound Interest (New Balance &times; 1.05)"],
            [
                ["Start", "&pound;2,000.00", "&pound;2,000.00"],
                ["Year 1", "&pound;2,000 + &pound;100 = <strong>&pound;2,100.00</strong>", "&pound;2,000 &times; 1.05 = <strong>&pound;2,100.00</strong>"],
                ["Year 2", "&pound;2,100 + &pound;100 = <strong>&pound;2,200.00</strong>", "&pound;2,100 &times; 1.05 = <strong>&pound;2,205.00</strong>"],
                ["Year 3", "&pound;2,200 + &pound;100 = <strong>&pound;2,300.00</strong>", "&pound;2,205 &times; 1.05 = <strong>&pound;2,315.25</strong>"],
            ],
        ),
    ),
    "functional-skills-mean-median-mode-and-range.html": (
        "4 Statistical Measures Master Comparison Table (Level 2)",
        "fa-chart-bar",
        table_wrap(
            ["Measure", "How to Calculate", "Sort Data First?", "Outliers &amp; Reverse Rule"],
            [
                ["<strong>Mean</strong>", "Sum of all values &divide; Count", "No", "Affected by outliers; <strong>Total = Mean &times; Count</strong>"],
                ["<strong>Median</strong>", "Exact middle value (average middle 2 if even)", "<strong>YES (Smallest &rarr; Largest)</strong>", "Best average when an extreme outlier skews data"],
                ["<strong>Mode</strong>", "Most frequent value (can be none or 2+)", "Helpful", "Only average usable for non-numerical categories"],
                ["<strong>Range</strong>", "Highest value &minus; Lowest value", "Helpful", "Measures spread/consistency (NOT an average!)"],
            ],
        ),
    ),
    "functional-skills-unit-conversions.html": (
        "Metric, Area/Volume &amp; Imperial Conversion Master Table",
        "fa-right-left",
        table_wrap(
            ["Conversion Type", "Exact Multiplier / Factor", "Worked Example"],
            [
                ["<strong>Metric Length</strong>", "1 km = 1,000 m &bull; 1 m = 100 cm &bull; 1 cm = 10 mm", "2.4 m = <strong>240 cm</strong> &bull; 450 cm = <strong>4.5 m</strong>"],
                ["<strong>Metric Mass / Capacity</strong>", "1 t = 1,000 kg &bull; 1 kg = 1,000 g &bull; 1 L = 1,000 ml", "0.8 t = <strong>800 kg</strong> &bull; 1,500 ml = <strong>1.5 L</strong>"],
                ["<strong>Area &amp; Volume (Squared/Cubed!)</strong>", "1 m&sup2; = 100&times;100 = <strong>10,000 cm&sup2;</strong> &bull; 1 L = <strong>1,000 cm&sup3;</strong>", "2 m&sup2; = <strong>20,000 cm&sup2;</strong>"],
                ["<strong>Imperial &harr; Metric (Given in Exam)</strong>", "1 mile &approx; 1.6 km &bull; 1 kg &approx; 2.2 lb &bull; 1 gallon &approx; 4.55 L", "50 miles &times; 1.6 = <strong>80 km</strong>"],
            ],
        ),
    ),
}


# ==============================================================================
# 26 MATHS LEVEL 1 VISUAL MASTER BOARDS (Strictly L1 Scope)
# ==============================================================================
L1_BOARDS: dict[str, tuple[str, str, str]] = {
    "functional-skills-2d-shapes-level-1.html": (
        "Level 1 2D Shapes &amp; Lines of Symmetry Master Table",
        "fa-shapes",
        table_wrap(
            ["2D Shape", "Sides &amp; Equal Sides", "Right Angles (90&deg;)", "Lines of Symmetry"],
            [
                ["<strong>Square</strong>", "4 equal sides", "4 right angles", "<strong>4</strong>"],
                ["<strong>Rectangle</strong>", "2 pairs of equal opposite sides", "4 right angles", "<strong>2</strong> (NOT diagonals!)"],
                ["<strong>Equilateral Triangle</strong>", "3 equal sides", "0 (all 60&deg;)", "<strong>3</strong>"],
                ["<strong>Isosceles Triangle</strong>", "2 equal sides", "Sometimes 1", "<strong>1</strong>"],
                ["<strong>Rhombus / Kite</strong>", "4 equal / 2 pairs adjacent equal", "0 (unless square)", "<strong>2</strong> / <strong>1</strong>"],
                ["<strong>Parallelogram</strong>", "2 pairs parallel equal sides", "0 (unless rectangle)", "<strong>0</strong>"],
            ],
            l1=True,
        ),
    ),
    "functional-skills-3d-shapes-level-1.html": (
        "Level 1 Common 3D Solids: Faces, Edges &amp; Vertices",
        "fa-cubes",
        table_wrap(
            ["3D Shape", "Flat / Curved Faces", "Edges", "Vertices (Corners)"],
            [
                ["<strong>Cube</strong>", "6 equal square faces", "12", "8"],
                ["<strong>Cuboid</strong>", "6 rectangular faces", "12", "8"],
                ["<strong>Triangular Prism</strong>", "5 faces (2 triangles + 3 rectangles)", "9", "6"],
                ["<strong>Square-Based Pyramid</strong>", "5 faces (1 square + 4 triangles)", "8", "5"],
                ["<strong>Cylinder</strong>", "3 faces (2 flat circles + 1 curved)", "2 curved", "0"],
                ["<strong>Cone / Sphere</strong>", "2 faces / 1 curved surface", "1 / 0", "1 / 0"],
            ],
            l1=True,
        ),
    ),
    "functional-skills-angles-and-bearings-level-1.html": (
        "Level 1 Angles &amp; Compass Quarter/Half Turns Master Board",
        "fa-compass",
        pastel_grid([
            ("mint", "Right &amp; Straight Angles", "90&deg; (&frac14; turn) &bull; 180&deg; (&frac12; turn)", "Full circle = <strong>360&deg;</strong>; &frac34; turn = <strong>270&deg;</strong>."),
            ("sky", "Angle Type Names", "Acute &lt; 90&deg; | Obtuse 90&deg;&ndash;180&deg;", "Angles &gt; 180&deg; are <strong>Reflex</strong> angles."),
            ("amber", "8-Point Compass Steps", "Each step = 45&deg; (N &rarr; NE &rarr; E)", "Clockwise from North to East = <strong>90&deg;</strong> (&frac14; turn)."),
        ]),
    ),
    "functional-skills-area-level-1.html": (
        "Level 1 Rectangle, L-Shape Split &amp; Cutout Master Board",
        "fa-vector-square",
        pastel_grid([
            ("mint", "Rectangle Area Rule", "Area = Length &times; Width", "5 m &times; 4 m = <strong>20 m&sup2;</strong> (always square units!)."),
            ("sky", "Split L-Shapes Cleanly", "Area A + Area B", "Rect A (20 m&sup2;) + Rect B (3 &times; 2.5 = 7.5 m&sup2;) = <strong>27.5 m&sup2;</strong>."),
            ("amber", "Windows, Doors &amp; Packs", "Subtract Cutouts &bull; Round UP", "Wall 12 m&sup2; &minus; Window 1.5 m&sup2; = <strong>10.5 m&sup2;</strong>; 27.5 &divide; 4 = 6.875 &rarr; <strong>7 packs</strong>."),
        ]),
    ),
    "functional-skills-bar-charts-level-1.html": (
        "Level 1 Bar Charts &amp; Pictograms Examiner Checklist",
        "fa-chart-column",
        table_wrap(
            ["Chart Element", "What Examiners Check for Full Marks", "Common Trap to Avoid"],
            [
                ["<strong>1. Title &amp; Axis Labels</strong>", "Clear title + both Horizontal and Vertical axis names with units", "Forgetting to label the vertical frequency axis"],
                ["<strong>2. Equal Scale Steps</strong>", "Consistent gaps starting at 0 (e.g. 0, 5, 10, 15, 20)", "Uneven jumps like 0, 5, 10, 12, 20"],
                ["<strong>3. Equal Bar Width &amp; Gaps</strong>", "All bars have equal width and matching gaps between them", "Bars touching (histogram) or varying widths"],
                ["<strong>4. Pictogram Key</strong>", "Clear key e.g. 1 full icon = 4 items, half icon = 2 items", "Counting icons as 1 each without multiplying by the key"],
            ],
            l1=True,
        ),
    ),
    "functional-skills-capacity-level-1.html": (
        "Level 1 Metric Capacity Ladder (ml &harr; cl &harr; Litres)",
        "fa-flask",
        table_wrap(
            ["Unit Conversion", "Multiply / Divide Rule", "Worked Example"],
            [
                ["<strong>Litres &rarr; Millilitres</strong>", "&times; 1,000", "2.4 L &times; 1,000 = <strong>2,400 ml</strong>"],
                ["<strong>Millilitres &rarr; Litres</strong>", "&divide; 1,000", "350 ml &divide; 1,000 = <strong>0.35 L</strong>"],
                ["<strong>Litres &harr; Centilitres</strong>", "&times; 100 / &divide; 100", "1.5 L = <strong>150 cl</strong>"],
                ["<strong>Bottles &amp; Jugs Division</strong>", "Match units FIRST, then divide", "1.5 L &divide; 250 ml = 1,500 &divide; 250 = <strong>6 glasses</strong>"],
            ],
            l1=True,
        ),
    ),
    "functional-skills-formulas-level-1.html": (
        "Level 1 Worded Two-Step Formula Master Board",
        "fa-equals",
        pastel_grid([
            ("mint", "Forward: Multiply Then Add", "Hire = (4 &times; &pound;28) + &pound;35", "4 &times; 28 = 112 &rarr; 112 + 35 = <strong>&pound;147</strong>."),
            ("sky", "Units Must Match Rule", "2,500 g = 2.5 kg", "Convert grams to kg BEFORE multiplying in a &lsquo;Weight in kg&rsquo; rule!"),
            ("amber", "Reverse: Undo Backwards", "&pound;165 = (Hours &times; 30) + 45", "Subtract 45 first (120), then &divide; 30 = <strong>4 hours</strong>."),
        ]),
    ),
    "functional-skills-grouped-data-level-1.html": (
        "Level 1 Tally Gates &amp; Grouped Frequency Table",
        "fa-list-ol",
        table_wrap(
            ["Score Group", "Tally (5-Bar Gates)", "Frequency", "Cross-Check Rule"],
            [
                ["0 &ndash; 9", "||||", "<strong>4</strong>", "Groups NEVER overlap (use 0&ndash;9, then 10&ndash;19)"],
                ["10 &ndash; 19", "||||/  ||||/  |", "<strong>11</strong>", "Cross every 5th bar cleanly for fast counting"],
                ["20 &ndash; 29", "||||/", "<strong>5</strong>", "Sum all frequencies to match total items: 4 + 11 + 5 = <strong>20</strong>"],
            ],
            l1=True,
        ),
    ),
    "functional-skills-interest-and-compound-interest-level-1.html": (
        "Level 1 Simple Interest Shortcut Board (10%, 5% &amp; 1%)",
        "fa-percent",
        pastel_grid([
            ("mint", "10% Shortcut", "Divide by 10 (&divide; 10)", "10% of &pound;800 = <strong>&pound;80</strong>."),
            ("sky", "5% &amp; 1% Shortcuts", "5% = Half of 10% &bull; 1% = &divide; 100", "5% of &pound;800 = 80 &divide; 2 = <strong>&pound;40</strong> per year."),
            ("amber", "Total After Interest", "Start + Yearly Interest", "2 years at 5% on &pound;800: &pound;800 + (&pound;40 &times; 2) = <strong>&pound;880</strong>."),
        ]),
    ),
    "functional-skills-length-level-1.html": (
        "Level 1 Metric Length Conversion Ladder (mm &harr; cm &harr; m &harr; km)",
        "fa-ruler",
        table_wrap(
            ["From &rarr; To", "Operation", "Level 1 Worked Example"],
            [
                ["<strong>km &rarr; m</strong>", "&times; 1,000", "1.8 km &times; 1,000 = <strong>1,800 m</strong>"],
                ["<strong>m &rarr; cm</strong>", "&times; 100", "2.4 m &times; 100 = <strong>240 cm</strong>"],
                ["<strong>cm &rarr; m</strong>", "&divide; 100", "450 cm &divide; 100 = <strong>4.5 m</strong>"],
                ["<strong>cm &harr; mm</strong>", "&times; 10 / &divide; 10", "3.5 cm = <strong>35 mm</strong> &bull; 70 mm = <strong>7 cm</strong>"],
            ],
            l1=True,
        ),
    ),
    "functional-skills-line-graphs-level-1.html": (
        "Level 1 Time-Series Line Graph Reading Board",
        "fa-chart-line",
        pastel_grid([
            ("mint", "Step 1: Find Small Tick Size", "Gap &divide; Number of Squares", "0 to 50 across 5 squares = 50 &divide; 5 = <strong>10 units per square</strong>."),
            ("sky", "Step 2: Read Across &amp; Up", "Follow Grid Lines Cleanly", "Find time on bottom axis &rarr; go straight up to dot &rarr; read left axis."),
            ("amber", "Step 3: Spot Biggest Change", "Steepest Line = Largest Jump", "Rise from 25 to 55 = +30 (larger increase than 15 to 30 = +15)."),
        ]),
    ),
    "functional-skills-maps-and-scale-drawings-level-1.html": (
        "Level 1 Simple Scale Drawings &amp; Maps Master Board",
        "fa-map",
        table_wrap(
            ["Scale Given", "Meaning", "Plan &rarr; Real Life (&times;)", "Real Life &rarr; Plan (&divide;)"],
            [
                ["<strong>1 cm = 2 m</strong>", "Each 1 cm equals 2 metres", "4.5 cm &times; 2 = <strong>9 m</strong>", "12 m &divide; 2 = <strong>6 cm</strong>"],
                ["<strong>1 : 100</strong>", "1 cm = 100 cm = 1 m", "7 cm &times; 1 = <strong>7 m</strong>", "5.5 m &rarr; <strong>5.5 cm</strong>"],
                ["<strong>1 square = 0.5 m</strong>", "2 squares = 1 metre", "8 squares = <strong>4 m</strong>", "3 m &rarr; <strong>6 squares</strong>"],
            ],
            l1=True,
        ),
    ),
    "functional-skills-mean-median-mode-and-range-level-1.html": (
        "Level 1 Mean (Average) &amp; Range Master Board",
        "fa-calculator",
        pastel_grid([
            ("mint", "Step 1: Mean = Add All &divide; Count", "Data: 12, 18, 14, 20, 16", "Sum = 80 &rarr; Mean = 80 &divide; 5 = <strong>16</strong>."),
            ("sky", "Step 2: Range = Biggest &minus; Smallest", "20 &minus; 12 = 8", "Smaller range = more consistent values."),
            ("amber", "Reverse Check", "Mean &times; Count = Total", "16 &times; 5 = <strong>80</strong> confirms your addition had no slip!"),
        ]),
    ),
    "functional-skills-nets-level-1.html": (
        "Level 1 Nets of Cubes, Cuboids &amp; Pyramids Master Table",
        "fa-box-open",
        table_wrap(
            ["3D Shape", "Faces Inside Net", "Quick Fold-Check Rule"],
            [
                ["<strong>Cube</strong>", "6 equal squares", "Count 6 squares; opposite faces never touch directly in the net"],
                ["<strong>Cuboid</strong>", "6 rectangles (3 matching pairs)", "2 Ends + Top/Bottom + Front/Back all match in pairs"],
                ["<strong>Square-Based Pyramid</strong>", "1 square base + 4 triangles", "All 4 triangles fold up to meet at one point"],
            ],
            l1=True,
        ),
    ),
    "functional-skills-perimeter-level-1.html": (
        "Level 1 Perimeter &amp; Missing-Edge Master Board",
        "fa-border-none",
        pastel_grid([
            ("mint", "Perimeter = Outer Rim Walk", "Add ALL Outer Edges", "6 m + 4 m + 6 m + 4 m = <strong>20 m</strong> (units stay m/cm, NEVER m&sup2;!)."),
            ("sky", "Find Missing L-Shape Edges", "Opposite Sides Match Total", "Full width 8 m &minus; partial 5 m = <strong>3 m missing edge</strong>."),
            ("amber", "Subtract Gates &amp; Doorways", "Outer Rim &minus; Gate Width", "Garden rim 20 m &minus; 1.5 m gate = <strong>18.5 m fencing</strong>."),
        ]),
    ),
    "functional-skills-pie-charts-level-1.html": (
        "Level 1 Pie Chart Angles Master Table (360&deg; Full Circle)",
        "fa-chart-pie",
        table_wrap(
            ["Angle / Fraction", "Share of 360&deg; Circle", "Worked Example (Total = 40 People)"],
            [
                ["<strong>360&deg;</strong> (Full Circle)", "1 whole (100%)", "360&deg; &divide; 40 = <strong>9&deg; per person</strong>"],
                ["<strong>180&deg;</strong> (Straight Line)", "&frac12; (50%)", "20 people = 20 &times; 9&deg; = <strong>180&deg;</strong>"],
                ["<strong>90&deg;</strong> (Right Angle)", "&frac14; (25%)", "10 people = 10 &times; 9&deg; = <strong>90&deg;</strong>"],
                ["<strong>45&deg;</strong> (Half of 90&deg;)", "&frac18; (12.5%)", "5 people = 5 &times; 9&deg; = <strong>45&deg;</strong>"],
            ],
            l1=True,
        ),
    ),
    "functional-skills-plans-and-elevations-level-1.html": (
        "Level 1 Plans &amp; Elevations 2D Views Master Board",
        "fa-cubes",
        table_wrap(
            ["View Name", "Camera Position", "Example: 5 &times; 3 &times; 2 Block"],
            [
                ["<strong>Plan View</strong>", "Looking straight DOWN from above", "<strong>5 wide &times; 3 deep</strong> grid"],
                ["<strong>Front Elevation</strong>", "Looking straight at the FRONT", "<strong>5 wide &times; 2 tall</strong> grid"],
                ["<strong>Side Elevation</strong>", "Looking straight from the SIDE", "<strong>3 wide &times; 2 tall</strong> grid"],
            ],
            l1=True,
        ),
    ),
    "functional-skills-time-level-1.html": (
        "Level 1 12/24-Hour Clock &amp; Base-60 Timeline Board",
        "fa-clock",
        pastel_grid([
            ("mint", "PM &harr; 24-Hour (+12 / &minus;12)", "1:45 pm = 13:45 &bull; 21:15 = 9:15 pm", "Morning 12-hr stays same (e.g. 9:15 am = 09:15); 12:30 am = 00:30."),
            ("sky", "Base-60 Jump Method", "09:40 &rarr; 10:00 &rarr; 11:00 &rarr; 11:15", "20 mins + 1 hr + 15 mins = <strong>1 hr 35 mins</strong>."),
            ("amber", "Never Subtract Like Decimals!", "1 hour = 60 minutes (NOT 100!)", "2.5 hours = 2 hrs 30 mins (NOT 2 hrs 50 mins!)."),
        ]),
    ),
    "functional-skills-using-length-area-and-volume-in-calculations-level-1.html": (
        "Level 1 Length (m) vs Area (m&sup2;) vs Volume (m&sup3;) Matrix",
        "fa-ruler-combined",
        table_wrap(
            ["What You Are Doing", "Correct Formula", "Unit", "Exam Rounding Rule"],
            [
                ["<strong>Fencing / Skirting / Trim</strong>", "Add outer lengths (Perimeter)", "<strong>m or cm</strong>", "Round UP packs/rolls"],
                ["<strong>Carpeting / Painting / Turfing</strong>", "Length &times; Width (Area)", "<strong>m&sup2; or cm&sup2;</strong>", "Round UP tins/boxes (6.1 &rarr; 7)"],
                ["<strong>Filling Tanks / Packing Boxes</strong>", "Length &times; Width &times; Height", "<strong>m&sup3; or cm&sup3;</strong>", "Boxes fitting inside: round DOWN!"],
            ],
            l1=True,
        ),
    ),
    "functional-skills-volume-level-1.html": (
        "Level 1 Cube &amp; Cuboid Volume Master Board",
        "fa-cube",
        pastel_grid([
            ("mint", "Volume Formula", "V = Length &times; Width &times; Height", "50 cm &times; 40 cm &times; 30 cm = <strong>60,000 cm&sup3;</strong>."),
            ("sky", "Water Capacity Bridge", "1,000 cm&sup3; = 1 Litre", "60,000 cm&sup3; &divide; 1,000 = <strong>60 Litres</strong>."),
            ("amber", "Match Units Before Multiplying", "1 m = 100 cm", "Never multiply metres by centimetres! Convert first."),
        ]),
    ),
    "functional-skills-circles-level-1.html": (
        "Level 1 Circle Parts &amp; Tray Packing Master Board",
        "fa-circle-dot",
        pastel_grid([
            ("mint", "Radius vs Diameter", "Diameter d = 2 &times; Radius r", "If Radius r = 6 cm, Diameter d = <strong>12 cm</strong> (r = d &divide; 2)."),
            ("sky", "Fitting Tins Inside a Tray", "Across &times; Deep (Whole Tins!)", "10 cm tins in 45 &times; 25 cm tray: (45&divide;10 = <strong>4</strong>) &times; (25&divide;10 = <strong>2</strong>) = <strong>8 tins</strong>."),
        ]),
    ),
    "functional-skills-data-tables-level-1.html": (
        "Level 1 Two-Way Table Cross-Check Master Board",
        "fa-table",
        table_wrap(
            ["Session", "Adults", "Children", "Row Total"],
            [
                ["<strong>Morning</strong>", "18", "12", "18 + 12 = <strong>30</strong>"],
                ["<strong>Afternoon</strong>", "14", "16", "14 + 16 = <strong>30</strong>"],
                ["<strong>Column Total</strong>", "<strong>32</strong>", "<strong>28</strong>", "Grand Total = <strong>60</strong>"],
            ],
            l1=True,
        ),
    ),
    "functional-skills-probability-level-1.html": (
        "Level 1 Probability Scale (0 to 1) Master Table",
        "fa-dice",
        table_wrap(
            ["Word Description", "Decimal (0&ndash;1)", "Fraction", "Percentage", "Example Event"],
            [
                ["<strong>Impossible</strong>", "0", "0", "0%", "Rolling a 7 on a standard 1&ndash;6 die"],
                ["<strong>Unlikely</strong>", "0.25", "&frac14;", "25%", "Picking 1 red marble from 4 (1 red, 3 blue)"],
                ["<strong>Even Chance</strong>", "0.5", "&frac12;", "50%", "Flipping Heads on a fair coin"],
                ["<strong>Likely</strong>", "0.75", "&frac34;", "75%", "Picking a blue marble from 4 (3 blue, 1 red)"],
                ["<strong>Certain</strong>", "1", "1", "100%", "Picking a marble from a bag of only marbles"],
            ],
            l1=True,
        ),
    ),
    "functional-skills-problems-involving-money-level-1.html": (
        "Level 1 Money Alignment, Pence &amp; Budget Check Board",
        "fa-sterling-sign",
        pastel_grid([
            ("mint", "Pad Whole Pounds to 2 DP", "&pound;8 &rarr; &pound;08.00", "Always write 2 digits after the decimal point (&pound;4.5 is &pound;4.50, NOT &pound;4.05!)."),
            ("sky", "Pounds &harr; Pence (&pound;1 = 100p)", "245p = &pound;2.45 &bull; &pound;0.80 = 80p", "Divide pence by 100 for pounds; multiply pounds by 100 for pence."),
            ("amber", "Budget Yes/No Decision", "Compare Total vs Budget", "&pound;48.50 &le; &pound;50.00 Budget &rarr; <strong>Yes</strong> (&pound;1.50 change left)."),
        ]),
    ),
    "functional-skills-proportion-level-1.html": (
        "Level 1 Direct Proportion &amp; Recipe Scaling (Unitary Method)",
        "fa-scale-unbalanced",
        table_wrap(
            ["Step", "Worked Example: 4 Pens Cost &pound;6.00 &rarr; Find Cost of 7 Pens", "Recipe Scaling Rule"],
            [
                ["<strong>Step 1: Divide to find 1 item</strong>", "&pound;6.00 &divide; 4 = <strong>&pound;1.50 per pen</strong>", "Find ingredients for 1 person first"],
                ["<strong>Step 2: Multiply for target</strong>", "7 &times; &pound;1.50 = <strong>&pound;10.50</strong>", "Scale EVERY ingredient by the same factor"],
            ],
            l1=True,
        ),
    ),
    "functional-skills-weight-level-1.html": (
        "Level 1 Metric Weight Ladder (mg &harr; g &harr; kg &harr; Tonnes)",
        "fa-weight-hanging",
        table_wrap(
            ["Conversion", "Multiply / Divide Rule (All 1,000s!)", "Worked Example"],
            [
                ["<strong>Tonnes &harr; kg</strong>", "1 tonne = 1,000 kg (&times;1,000 / &divide;1,000)", "0.8 tonnes = <strong>800 kg</strong>"],
                ["<strong>kg &harr; grams (g)</strong>", "1 kg = 1,000 g (&times;1,000 / &divide;1,000)", "2,500 g = <strong>2.5 kg</strong>"],
                ["<strong>grams (g) &harr; mg</strong>", "1 g = 1,000 mg (&times;1,000 / &divide;1,000)", "1.5 g = <strong>1,500 mg</strong>"],
            ],
            l1=True,
        ),
    ),
}


def main() -> None:
    existing_re = re.compile(
        r'[ \t]*<section class="revision-section mfs-visual-master-board" data-mfs-visual-board="sprint6"[^>]*>.*?</section>\n+',
        re.S,
    )
    golden_re = re.compile(r'(?:[ \t]*<!--[^-\n]*GOLDEN RULES[^-\n]*-->[ \t]*\n)?[ \t]*<section id="golden-rules"', re.I)

    updated = 0
    for level, mapping in [("L2", L2_BOARDS), ("L1", L1_BOARDS)]:
        for fname, (title, icon, inner_html) in mapping.items():
            fp = ROOT / fname
            if not fp.exists():
                raise FileNotFoundError(f"Missing target file: {fname}")
            orig = fp.read_text(encoding="utf-8", errors="ignore")
            cleaned = existing_re.sub("", orig)

            badge = "Level 1 Visual Board" if level == "L1" else "Level 2 Visual Board"
            board_html = wrap_board(level, title, badge, icon, inner_html)

            m = golden_re.search(cleaned)
            if not m:
                raise RuntimeError(f"Could not find <section id=\"golden-rules\" in {fname}")
            idx = m.start()
            new_text = cleaned[:idx] + board_html + cleaned[idx:]

            if new_text != orig:
                fp.write_text(new_text, encoding="utf-8")
                updated += 1

    print(f"VISUAL_BOARDS_OK: l2={len(L2_BOARDS)}, l1={len(L1_BOARDS)}, updated={updated}")


if __name__ == "__main__":
    main()
