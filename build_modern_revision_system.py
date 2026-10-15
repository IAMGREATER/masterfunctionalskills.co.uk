import os, sys, re, glob
import lxml.html
from lxml import etree

PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"
TOPICS_DIR = os.path.join(PROJECT_DIR, "topics")

CURRICULUM_MATHS = [
    ("functional-skills-numbers-and-place-value.html", "Numbers & Place Value"),
    ("functional-skills-ordering-numbers.html", "Ordering Numbers"),
    ("functional-skills-addition-and-subtraction.html", "Addition & Subtraction"),
    ("functional-skills-multiplication.html", "Multiplication"),
    ("functional-skills-division.html", "Division"),
    ("functional-skills-bidmas.html", "BIDMAS / Order of Operations"),
    ("functional-skills-rounding-and-estimating.html", "Rounding & Estimating"),
    ("functional-skills-fractions.html", "Fractions"),
    ("functional-skills-decimals.html", "Decimals"),
    ("functional-skills-percentages.html", "Percentages"),
    ("functional-skills-fractions-decimals-and-percentages.html", "FDP Conversions"),
    ("functional-skills-ratio.html", "Ratio & Proportion"),
    ("functional-skills-proportion.html", "Direct & Inverse Proportion"),
    ("functional-skills-formulas.html", "Algebra & Formulas"),
    ("functional-skills-money.html", "Money & Finance"),
    ("functional-skills-best-buys.html", "Best Buys & Unit Pricing"),
    ("functional-skills-interest-and-compound-interest.html", "Simple & Compound Interest"),
    ("functional-skills-time.html", "Time & Timetables"),
    ("functional-skills-speed.html", "Speed, Distance & Time"),
    ("functional-skills-density.html", "Density & Compound Units"),
    ("functional-skills-unit-conversions.html", "Unit Conversions"),
    ("functional-skills-length.html", "Length & Dimensions"),
    ("functional-skills-weight.html", "Weight & Mass"),
    ("functional-skills-capacity.html", "Capacity & Volume Units"),
    ("functional-skills-perimeter.html", "Perimeter"),
    ("functional-skills-area.html", "Area"),
    ("functional-skills-volume.html", "Volume"),
    ("functional-skills-surface-area.html", "Surface Area"),
    ("functional-skills-2d-shapes.html", "2D Shapes"),
    ("functional-skills-3d-shapes.html", "3D Shapes"),
    ("functional-skills-nets.html", "Nets of 3D Shapes"),
    ("functional-skills-plans-and-elevations.html", "Plans & Elevations"),
    ("functional-skills-angles.html", "Angles & Bearings"),
    ("functional-skills-angles-in-2d-shapes.html", "Angles in Polygons"),
    ("functional-skills-circles.html", "Circles & Circumference"),
    ("functional-skills-coordinates.html", "Coordinates"),
    ("functional-skills-maps-and-scale-drawings.html", "Maps & Scale Drawings"),
    ("functional-skills-mean-median-mode-and-range.html", "Averages (Mean, Median, Mode, Range)"),
    ("functional-skills-estimating-the-mean.html", "Estimating the Mean"),
    ("functional-skills-grouped-data.html", "Grouped Frequency Tables"),
    ("functional-skills-data-tables.html", "Data Tables"),
    ("functional-skills-bar-charts.html", "Bar Charts"),
    ("functional-skills-line-graphs.html", "Line Graphs"),
    ("functional-skills-pie-charts.html", "Pie Charts"),
    ("functional-skills-scatter-graphs.html", "Scatter Graphs & Correlation"),
    ("functional-skills-conversion-graphs.html", "Conversion Graphs"),
    ("functional-skills-probability.html", "Probability"),
    ("functional-skills-probability-tables.html", "Probability Outcomes & Tables")
]

CURRICULUM_ENGLISH = [
    ("reading-fact-or-opinion.html", "Fact or Opinion"),
    ("reading-meaning.html", "Words in Context & Meaning"),
    ("reading-specialist-words.html", "Specialist Vocabulary"),
    ("reading-presentational-features.html", "Presentational Features"),
    ("reading-investigating-layout.html", "Layout Devices"),
    ("reading-investigating-image.html", "Images & Visual Effects"),
    ("reading-language-features.html", "Language Techniques"),
    ("reading-point-of-view-and-line-of-argument.html", "Point of View & Bias"),
    ("reading-styles-of-writing-and-voice.html", "Tone, Style & Voice"),
    ("reading-text-types.html", "Text Types & Purpose"),
    ("reading-comparing-texts.html", "Comparing Texts"),
    ("reading-why-do-writers-write.html", "The Writer's Purpose"),
    ("reading-the-exam.html", "Reading Exam Strategy"),
    ("writing-planning-your-answer.html", "Planning Written Responses"),
    ("writing-communicating.html", "Communicating Clearly"),
    ("writing-context.html", "Context & Purpose"),
    ("writing-assessing-audience.html", "Audience & Register"),
    ("writing-form-presentational-and-language-features.html", "Format & Conventions"),
    ("writing-organisational-markers.html", "Organisational Markers"),
    ("writing-linking-up-your-answer.html", "Paragraphing & Cohesion"),
    ("writing-grammar.html", "Grammar & Sentence Structures"),
    ("writing-tenses.html", "Consistency of Tense"),
    ("writing-perfecting-your-punctuation.html", "Punctuation Mastery"),
    ("writing-spelling.html", "Spelling Rules & Strategies"),
    ("writing-fantastic-finalising.html", "Proofreading & Editing"),
    ("writing-why-are-you-writing.html", "Purpose in Writing"),
    ("writing-the-exam.html", "Writing Exam Strategy")
]

def get_next_topic(filename, is_english):
    curr = CURRICULUM_ENGLISH if is_english else CURRICULUM_MATHS
    for i, (fn, name) in enumerate(curr):
        if fn == filename:
            if i + 1 < len(curr):
                return curr[i + 1]
            return curr[0]
    return (curr[0][0], curr[0][1]) if curr else ("revise.html", "Revision Directory")

def clean_tree_from_katex_and_junk(tree):
    # 1. Drop katex-mathml completely
    for m in tree.xpath('.//*[contains(@class, "katex-mathml")]'):
        m.drop_tree()
        
    # 2. Clean katex html containers to clean plain-text spans
    for k in tree.xpath('.//*[contains(@class, "katex")]'):
        txt = k.text_content().strip()
        # Clean common math symbols
        txt = txt.replace(' ', ' ')
        parent = k.getparent()
        if parent is not None:
            span = etree.Element('span')
            span.set('class', 'mfs-clean-math')
            span.text = txt
            k.addprevious(span)
            k.drop_tree()

    # 3. Drop scripts, styles, noscripts
    for bad in tree.xpath('.//script | .//style | .//noscript'):
        bad.drop_tree()
        
    # 4. Clean images
    for img in tree.xpath('.//img'):
        src = img.get('src', '')
        if src.startswith('../assets/'):
            src = src.replace('../assets/', 'assets/')
        elif src.startswith('/assets/'):
            src = src.lstrip('/')
        elif src.startswith('app/uploads/'):
            src = 'assets/img/pfs/' + os.path.basename(src)
        if '%20' in src:
            src = src.split('%20')[0].strip()
        src = src.split(' ')[0].strip()
        img.set('src', src)
        for a in ['width', 'height', 'data-lazy-src', 'data-lazy-srcset', 'data-lazy-sizes', 'loading', 'decoding']:
            if img.get(a):
                del img.attrib[a]
        img.set('class', 'img-fluid')
        img.set('loading', 'lazy')
