import re

with open('/home/subi/Projects/masterfunctionalskills.co.uk/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Navigation Bar to include Revise Topics link
nav_target = '<a href="#courses">Courses & Classes</a>'
nav_replacement = '''<a href="#courses">Courses & Classes</a>
        <a href="#revise">Revise Topics</a>'''

if '<a href="#revise">' not in content:
    content = content.replace(nav_target, nav_replacement, 1)
    print("Nav bar updated with Revise Topics link.")

# 2. Prepare the Revise Section HTML
revise_section_html = '''
  <!-- REVISE CURRICULUM & TOPIC-BY-TOPIC DIRECTORY -->
  <section class="mfs-section bg-light" id="revise">
    <div class="mfs-container">
      <div class="section-head text-center" style="max-width: 820px; margin: 0 auto 36px;">
        <span class="section-tag" style="background:#e0f2fe; color:#0284c7;">CURRICULUM REVISION DIRECTORY</span>
        <h2 style="font-size:2.2rem; color:var(--mfs-navy); margin: 10px 0 14px;">Functional Skills Revise Hub: Topic-by-Topic Guides</h2>
        <p style="color:var(--mfs-gray); font-size:1.05rem; line-height:1.6;">
          Master every individual standard assessed by Pearson Edexcel, City & Guilds, and NCFE. Click any topic below to open tutor golden rules, high-frequency examiner traps, and step-by-step worked model answers.
        </p>
      </div>

      <!-- Tab Switcher -->
      <div class="revise-nav-tabs">
        <button class="rev-tab-btn active" onclick="switchReviseTab('tab-maths-l2')">
          <i class="fa-solid fa-calculator"></i> Maths Level 2 (Curriculum Hub)
        </button>
        <button class="rev-tab-btn" onclick="switchReviseTab('tab-english-l2')">
          <i class="fa-solid fa-pen-nib"></i> English Level 2 (Writing & Reading)
        </button>
        <button class="rev-tab-btn" onclick="switchReviseTab('tab-l1-foundations')">
          <i class="fa-solid fa-stairs"></i> Level 1 Foundations (Stepping Stones)
        </button>
      </div>

      <!-- TAB 1: MATHS LEVEL 2 -->
      <div class="revise-tab-panel active" id="tab-maths-l2">
        <!-- Cluster 1: Numbers -->
        <div class="cluster-box">
          <div class="cluster-header">
            <div class="cluster-icon cluster-icon-blue"><i class="fa-solid fa-arrow-down-1-9"></i></div>
            <div>
              <h3>Cluster 1: Number & The Number System</h3>
              <p style="margin:0; font-size:0.85rem; color:var(--mfs-gray);">Fractions, percentages, compound interest, ratio, scale pricing & formulas</p>
            </div>
            <span>7 Core Topics</span>
          </div>
          <div class="topics-grid">
            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Fractions, Decimals & Percentages (FDP)</span>
                <span class="topic-badge badge-core">Core</span>
              </div>
              <p class="topic-summary">Conversions between recurring decimals, fractions, and percentages; finding fractional parts of quantities.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('m2-fdp')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Reverse Percentages (Original Value)</span>
                <span class="topic-badge badge-hot">High Exam Frequency</span>
              </div>
              <p class="topic-summary">Calculating original price before VAT or sale discount using decimal multipliers (e.g. divide by 0.85 or 1.20).</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('m2-reverse-pct')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Compound Interest & Depreciation</span>
                <span class="topic-badge badge-core">Core</span>
              </div>
              <p class="topic-summary">Repeated percentage growth and decay over multiple years using power multipliers: A = P × (1 ± r)ⁿ.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('m2-compound')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Ratio & Direct Proportion</span>
                <span class="topic-badge badge-hot">High Exam Frequency</span>
              </div>
              <p class="topic-summary">Dividing amounts into 3-part ratios, scaling recipes, unitary method, and sharing grant funds.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('m2-ratio')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Best Buy & Unit Value Comparison</span>
                <span class="topic-badge badge-core">Core</span>
              </div>
              <p class="topic-summary">Unit rate analysis (cost per 100g, ml per £) comparing multi-pack deals to identify best commercial value.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('m2-best-buy')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">BIDMAS & Negative Number Operations</span>
                <span class="topic-badge badge-core">Core</span>
              </div>
              <p class="topic-summary">Order of operations with brackets and powers; bank balance debits/credits and temperature drops.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('m2-bidmas')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Workplace Formulas & Substitution</span>
                <span class="topic-badge badge-pass">Pass Essential</span>
              </div>
              <p class="topic-summary">Substituting values into multi-variable workplace formulas: wages, vehicle hire, and temperature conversions.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('m2-formulas')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>
          </div>
        </div>

        <!-- Cluster 2: Measures & Shape -->
        <div class="cluster-box">
          <div class="cluster-header">
            <div class="cluster-icon cluster-icon-green"><i class="fa-solid fa-shapes"></i></div>
            <div>
              <h3>Cluster 2: Measures, Shape & Space</h3>
              <p style="margin:0; font-size:0.85rem; color:var(--mfs-gray);">Area of compound shapes, perimeter, circles, volume, scale diagrams & speed</p>
            </div>
            <span>7 Core Topics</span>
          </div>
          <div class="topics-grid">
            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Perimeter & Circumference</span>
                <span class="topic-badge badge-core">Core</span>
              </div>
              <p class="topic-summary">Boundary measurements, fencing, skirting boards, and circumference of circular boundaries (C = πd).</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('m2-perimeter')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Area of Compound & L-Shaped Spaces</span>
                <span class="topic-badge badge-hot">High Exam Frequency</span>
              </div>
              <p class="topic-summary">Splitting irregular floorplans into rectangles and trapeziums ((a+b)/2 × h) for tiling, turfing, and carpeting.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('m2-area')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Area of Circles & Semicircles</span>
                <span class="topic-badge badge-hot">High Exam Frequency</span>
              </div>
              <p class="topic-summary">Using A = πr² to calculate circular lawns, patios, and composite circular garden features.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('m2-circles')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Volume of 3D Prisms & Cylinders</span>
                <span class="topic-badge badge-core">Core</span>
              </div>
              <p class="topic-summary">Cuboids, triangular prisms, water storage tanks, and cylinder volume capacity (V = πr²h).</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('m2-volume')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Scale Drawings, Floor Plans & Bearings</span>
                <span class="topic-badge badge-hot">High Exam Frequency</span>
              </div>
              <p class="topic-summary">Converting architectural scale ratios (1:50, 1:100), measuring grid plans, and 3-figure compass bearings.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('m2-scale')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Speed, Distance, Time & Density</span>
                <span class="topic-badge badge-pass">Pass Essential</span>
              </div>
              <p class="topic-summary">Converting decimal hours (e.g. 2.4 hrs = 2h 24m), travel speeds (S = D/T), and material density.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('m2-sdt')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Metric & Imperial Unit Conversions</span>
                <span class="topic-badge badge-core">Core</span>
              </div>
              <p class="topic-summary">Converting miles to km (5 miles ≈ 8 km), kg to pounds (1 kg ≈ 2.2 lbs), and litres to gallons.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('m2-units')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>
          </div>
        </div>

        <!-- Cluster 3: Data & Stats -->
        <div class="cluster-box">
          <div class="cluster-header">
            <div class="cluster-icon cluster-icon-amber"><i class="fa-solid fa-chart-pie"></i></div>
            <div>
              <h3>Cluster 3: Handling Data & Statistics</h3>
              <p style="margin:0; font-size:0.85rem; color:var(--mfs-gray);">Averages, range comparison, scatter graphs, probability & pie charts</p>
            </div>
            <span>5 Core Topics</span>
          </div>
          <div class="topics-grid">
            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Mean, Median, Mode & Range Comparison</span>
                <span class="topic-badge badge-hot">High Exam Frequency</span>
              </div>
              <p class="topic-summary">Comparing two datasets using an average (mean/median) and a measure of spread/consistency (range).</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('m2-averages')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Scatter Diagrams & Correlation</span>
                <span class="topic-badge badge-core">Core</span>
              </div>
              <p class="topic-summary">Plotting points, drawing accurate lines of best fit, positive/negative correlation, and reliable interpolation.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('m2-scatter')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Probability (Single & Combined Events)</span>
                <span class="topic-badge badge-hot">High Exam Frequency</span>
              </div>
              <p class="topic-summary">Calculating fractional/decimal probability, sample space grids, tree diagrams, and independent event outcomes.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('m2-probability')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Grouped Frequency Tables & Estimated Mean</span>
                <span class="topic-badge badge-pass">Pass Essential</span>
              </div>
              <p class="topic-summary">Finding class midpoints, multiplying by frequency (fx), and calculating estimated mean from interval tables.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('m2-frequency')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Dual Bar, Pie & Line Graphs</span>
                <span class="topic-badge badge-core">Core</span>
              </div>
              <p class="topic-summary">Calculating pie chart sector angles (360° ÷ total), drawing dual comparative bar charts, and trend line reading.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('m2-charts')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 2: ENGLISH LEVEL 2 -->
      <div class="revise-tab-panel" id="tab-english-l2">
        <!-- Cluster 1: Writing Formats -->
        <div class="cluster-box">
          <div class="cluster-header">
            <div class="cluster-icon cluster-icon-red"><i class="fa-solid fa-file-pen"></i></div>
            <div>
              <h3>Cluster 1: Writing Formats & Composition</h3>
              <p style="margin:0; font-size:0.85rem; color:var(--mfs-gray);">Formal letters, articles, workplace emails, reports & persuasive speeches</p>
            </div>
            <span>5 Core Topics</span>
          </div>
          <div class="topics-grid">
            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Formal Business Letters</span>
                <span class="topic-badge badge-hot">High Exam Frequency</span>
              </div>
              <p class="topic-summary">Mastering 2-address format, formal date, Dear Sir/Madam (Yours faithfully) vs Dear Mr Smith (Yours sincerely).</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('e2-letter')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Persuasive Articles (Community & Workplace)</span>
                <span class="topic-badge badge-hot">High Exam Frequency</span>
              </div>
              <p class="topic-summary">Crafting engaging headlines, bylines, subheadings, rhetorical questions, and balanced persuasive arguments.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('e2-article')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Professional Workplace Emails</span>
                <span class="topic-badge badge-core">Core</span>
              </div>
              <p class="topic-summary">Subject line precision, professional salutations, bulleted action points, and courteous sign-offs.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('e2-email')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Formal Reports & Proposals</span>
                <span class="topic-badge badge-pass">Pass Essential</span>
              </div>
              <p class="topic-summary">Report title, purpose/terms of reference, findings under numbered subheadings, conclusions, and recommendations.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('e2-report')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Persuasive Speeches & Rhetoric (AFOREST)</span>
                <span class="topic-badge badge-core">Core</span>
              </div>
              <p class="topic-summary">Audience hooks, alliteration, facts, opinions, rhetorical questions, emotive language, and triads.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('e2-speech')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>
          </div>
        </div>

        <!-- Cluster 2: SPaG -->
        <div class="cluster-box">
          <div class="cluster-header">
            <div class="cluster-icon cluster-icon-purple"><i class="fa-solid fa-spell-check"></i></div>
            <div>
              <h3>Cluster 2: SPaG (Spelling, Punctuation & Grammar)</h3>
              <p style="margin:0; font-size:0.85rem; color:var(--mfs-gray);">Fixing comma splices, apostrophes, complex sentences & tense agreement</p>
            </div>
            <span>5 Core Topics</span>
          </div>
          <div class="topics-grid">
            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Eliminating Comma Splices & Run-Ons</span>
                <span class="topic-badge badge-hot">High Exam Frequency</span>
              </div>
              <p class="topic-summary">Replacing commas between main clauses with full stops, semicolons, or coordinating conjunctions (FANBOYS).</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('e2-commas')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Apostrophes of Possession vs Contraction</span>
                <span class="topic-badge badge-core">Core</span>
              </div>
              <p class="topic-summary">Singular vs plural possession (the nurse's badge vs the nurses' station); eliminating it's vs its confusion.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('e2-apostrophes')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Complex & Compound Sentences</span>
                <span class="topic-badge badge-pass">Pass Essential</span>
              </div>
              <p class="topic-summary">Using subordinating connectives (although, whereas, because) and fronted adverbials with commas.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('e2-sentences')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Subject-Verb Agreement & Tense Control</span>
                <span class="topic-badge badge-core">Core</span>
              </div>
              <p class="topic-summary">Ensuring singular/plural concord and avoiding erratic tense jumping between past, present, and future.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('e2-agreement')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Paragraphing & Cohesive Devices (PEEL)</span>
                <span class="topic-badge badge-core">Core</span>
              </div>
              <p class="topic-summary">Structuring arguments with Point, Evidence, Explanation, Link; using transitional discourse markers.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('e2-paragraphs')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>
          </div>
        </div>

        <!-- Cluster 3: Reading Analysis -->
        <div class="cluster-box">
          <div class="cluster-header">
            <div class="cluster-icon cluster-icon-blue"><i class="fa-solid fa-book-open-reader"></i></div>
            <div>
              <h3>Cluster 3: Reading Analysis & Comprehension</h3>
              <p style="margin:0; font-size:0.85rem; color:var(--mfs-gray);">Author purpose, bias detection, synthesising two texts & layout features</p>
            </div>
            <span>5 Core Topics</span>
          </div>
          <div class="topics-grid">
            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Identifying Purpose & Target Audience</span>
                <span class="topic-badge badge-core">Core</span>
              </div>
              <p class="topic-summary">Distinguishing between texts written to persuade, inform, instruct, or advise; evaluating intended demographic.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('e2-purpose')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Detecting Bias, Fact vs Opinion</span>
                <span class="topic-badge badge-hot">High Exam Frequency</span>
              </div>
              <p class="topic-summary">Identifying subjective bias, commercial sponsorship, emotive exaggeration, and empirical factual statements.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('e2-bias')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Comparing Ideas Across Two Texts (Synthesis)</span>
                <span class="topic-badge badge-hot">High Exam Frequency</span>
              </div>
              <p class="topic-summary">Synthesising similarities and differences between two contrasting passages with precise evidence citation.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('e2-comparison')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Organizational & Layout Features</span>
                <span class="topic-badge badge-pass">Pass Essential</span>
              </div>
              <p class="topic-summary">Analyzing how subheadings, bullet points, callout boxes, and bold text guide reader navigation.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('e2-layout')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Implicit vs Explicit Meaning (Inference)</span>
                <span class="topic-badge badge-core">Core</span>
              </div>
              <p class="topic-summary">Reading between the lines: extracting subtle subtext and implied meaning beyond literal stated facts.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('e2-inference')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 3: LEVEL 1 FOUNDATIONS -->
      <div class="revise-tab-panel" id="tab-l1-foundations">
        <!-- Maths L1 -->
        <div class="cluster-box">
          <div class="cluster-header">
            <div class="cluster-icon cluster-icon-blue"><i class="fa-solid fa-1"></i></div>
            <div>
              <h3>Maths Level 1: Essential Building Blocks</h3>
              <p style="margin:0; font-size:0.85rem; color:var(--mfs-gray);">Foundational stepping stones required for apprentice gateways and Level 2 progression</p>
            </div>
            <span>4 Key Topics</span>
          </div>
          <div class="topics-grid">
            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Place Value, Rounding & Estimation</span>
                <span class="topic-badge badge-core">Core</span>
              </div>
              <p class="topic-summary">Ordering large numbers, rounding to nearest 10, 100, 1000, and checking answers with front-end estimation.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('m1-place-value')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Simple Fractions & Benchmark Percentages</span>
                <span class="topic-badge badge-hot">High Exam Frequency</span>
              </div>
              <p class="topic-summary">Calculating 10%, 25%, 50%, 75% of whole numbers and finding equivalent fractions (1/2 = 2/4 = 50%).</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('m1-fractions')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Simple Perimeter & Area of Rectangles</span>
                <span class="topic-badge badge-core">Core</span>
              </div>
              <p class="topic-summary">Calculating perimeter by adding all four outer sides; area of simple rectangles using length × width.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('m1-perimeter-area')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Money Calculations & 12/24-Hour Time</span>
                <span class="topic-badge badge-pass">Pass Essential</span>
              </div>
              <p class="topic-summary">Adding and subtracting currency with two decimal places; converting between 12-hour am/pm and 24-hour clock.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('m1-money-time')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>
          </div>
        </div>

        <!-- English L1 -->
        <div class="cluster-box">
          <div class="cluster-header">
            <div class="cluster-icon cluster-icon-green"><i class="fa-solid fa-pencil"></i></div>
            <div>
              <h3>English Level 1: Foundational Literacy</h3>
              <p style="margin:0; font-size:0.85rem; color:var(--mfs-gray);">Sentence punctuation, everyday emails, main idea identification & dictionary skills</p>
            </div>
            <span>4 Key Topics</span>
          </div>
          <div class="topics-grid">
            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Sentence Punctuation & Capitalisation</span>
                <span class="topic-badge badge-core">Core</span>
              </div>
              <p class="topic-summary">Mastering capital letters for proper nouns and sentence starts; ending sentences accurately with full stops.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('e1-sentence-basics')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Everyday Workplace & Community Emails</span>
                <span class="topic-badge badge-hot">High Exam Frequency</span>
              </div>
              <p class="topic-summary">Writing clear, friendly emails to colleagues or service providers with suitable openings, message points, and sign-offs.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('e1-informal-email')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Extracting Main Ideas & Key Facts</span>
                <span class="topic-badge badge-core">Core</span>
              </div>
              <p class="topic-summary">Skimming notices, letters, and short articles to find specific dates, times, phone numbers, and core instructions.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('e1-reading-main')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>

            <div class="topic-item">
              <div class="topic-top">
                <span class="topic-title">Alphabetical Order & Index Searching</span>
                <span class="topic-badge badge-pass">Pass Essential</span>
              </div>
              <p class="topic-summary">Arranging words and names in alphabetical order to the second and third letters for filing and directory lookups.</p>
              <div class="topic-bottom">
                <a href="javascript:void(0)" onclick="openTopicModal('e1-alphabetical')" class="btn-topic-action">View Key Rule & Exam Example →</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- TOPIC WORKED EXAMPLE MODAL -->
  <div id="topicModal" class="mfs-modal-backdrop" onclick="handleBackdropClick(event)">
    <div class="mfs-modal-content">
      <div class="mfs-modal-header">
        <div class="mfs-modal-title-group">
          <h3 id="modalTopicTitle">Topic Title</h3>
          <div class="mfs-modal-meta">
            <span id="modalTopicLevel" class="topic-badge badge-core">Level 2</span>
            <span id="modalTopicCluster" style="font-size:0.82rem; color:var(--mfs-gray);">Cluster Name</span>
          </div>
        </div>
        <button class="mfs-modal-close" onclick="closeTopicModal()" aria-label="Close modal">&times;</button>
      </div>
      <div class="mfs-modal-body">
        <div class="modal-rule-card">
          <div class="modal-rule-title">
            <i class="fa-solid fa-graduation-cap"></i> Tutor Golden Rule
          </div>
          <p id="modalTopicRule" class="modal-rule-text">Tutor rule goes here.</p>
        </div>

        <div class="modal-example-card">
          <h4><i class="fa-solid fa-pencil"></i> Pearson Edexcel / City & Guilds Exam-Style Worked Model</h4>
          <div id="modalTopicQuestion" class="modal-example-question">Question text goes here.</div>
          <div id="modalTopicSteps" class="modal-example-steps">Step-by-step working goes here.</div>
        </div>

        <div class="modal-trap-card">
          <strong><i class="fa-solid fa-triangle-exclamation"></i> Common Examiner Trap:</strong>
          <span id="modalTopicTrap">Trap explanation goes here.</span>
        </div>

        <div class="modal-footer-cta">
          <a id="modalWhatsAppLink" href="https://wa.me/447564525425" target="_blank" rel="noopener" class="btn-cta-green">
            <i class="fa-brands fa-whatsapp"></i> Book 1-to-1 Lesson on this Topic
          </a>
          <a href="#shop" onclick="closeTopicModal()" class="btn-cta-blue">
            <i class="fa-solid fa-box-archive"></i> Order Revision Cards (£9.99)
          </a>
        </div>
      </div>
    </div>
  </div>
'''

# Insert Revise section before shop
target_marker = '<!-- REVISION CARDS & MERCHANDISE SHOP -->'
if 'id="revise"' not in content:
    if target_marker in content:
        content = content.replace(target_marker, revise_section_html + '\n  ' + target_marker, 1)
        print("Revise section HTML inserted successfully before #shop.")
    else:
        print("ERROR: Target marker not found in index.html")

# 3. Add JavaScript topic database and modal handlers
topic_js = '''
  <script>
    // Tab switching for Revise Hub
    function switchReviseTab(tabId) {
      document.querySelectorAll('.rev-tab-btn').forEach(btn => btn.classList.remove('active'));
      event.target.closest('.rev-tab-btn').classList.add('active');

      document.querySelectorAll('.revise-tab-panel').forEach(panel => panel.classList.remove('active'));
      const activePanel = document.getElementById(tabId);
      if (activePanel) {
        activePanel.classList.add('active');
      }
    }

    // Modal data dictionary
    const topicData = {
      'm2-fdp': {
        title: 'Fractions, Decimals & Percentages (FDP)',
        level: 'Maths Level 2',
        cluster: 'Number & The Number System',
        rule: 'To convert any fraction to a percentage, divide the top by the bottom and multiply by 100 (e.g. 7 ÷ 8 × 100 = 87.5%). Always express recurring decimals accurately (e.g. 1/3 = 0.333... or 33.3%).',
        question: 'A community clinic has 240 patients registered. In one month, 3/8 of the patients attended a wellness screening, and 35% attended a flu vaccination clinic. How many MORE patients attended the wellness screening than the flu vaccination?',
        steps: '<ol><li><strong>Calculate 3/8 of 240:</strong><br>240 ÷ 8 = 30<br>30 × 3 = <strong>90 patients</strong></li><li><strong>Calculate 35% of 240:</strong><br>0.35 × 240 = <strong>84 patients</strong></li><li><strong>Calculate the difference:</strong><br>90 - 84 = <strong>6 patients</strong></li><li><strong>Final Stated Answer:</strong> 6 more patients attended the wellness screening.</li></ol>',
        trap: 'Rounding 3/8 to 0.37 and multiplying, which causes rounding discrepancies. Always divide by the denominator first, then multiply by the numerator.'
      },
      'm2-reverse-pct': {
        title: 'Reverse Percentages (Original Value)',
        level: 'Maths Level 2',
        cluster: 'Number & The Number System',
        rule: 'NEVER calculate the percentage of the sale/final price and add or subtract it! If a value drops by 15%, the sale price is 85% (0.85). Divide the sale price by 0.85 to find the original 100%.',
        question: 'A specialist medical monitor is sold on promotion for £297.50, which includes a 15% promotional discount. What was the original full price before the discount?',
        steps: '<ol><li><strong>Identify the remaining percentage:</strong><br>100% - 15% = 85% = <strong>0.85</strong></li><li><strong>Form the equation:</strong><br>Original Price × 0.85 = £297.50</li><li><strong>Divide to find the original:</strong><br>Original Price = £297.50 ÷ 0.85 = <strong>£350.00</strong></li><li><strong>Check working:</strong><br>15% of £350 = £52.50. £350 - £52.50 = £297.50. Confirmed!</li></ol>',
        trap: 'Calculating 15% of £297.50 (£44.63) and adding it to get £342.13. This scores 0 marks on Pearson Edexcel!'
      },
      'm2-compound': {
        title: 'Compound Interest & Depreciation',
        level: 'Maths Level 2',
        cluster: 'Number & The Number System',
        rule: 'Use the multiplier formula: Final = Principal × (Multiplier)ⁿ where n is the number of years. For 3.2% interest, multiplier = 1 + 0.032 = 1.032.',
        question: 'An NHS healthcare trust invests £12,000 into high-yield educational equipment. The fund grows at an annual compound interest rate of 4.5% per annum for 3 years. Calculate the final balance. Give your answer to 2 decimal places.',
        steps: '<ol><li><strong>Determine the decimal multiplier:</strong><br>100% + 4.5% = 104.5% = <strong>1.045</strong></li><li><strong>Apply the power formula:</strong><br>Balance = £12,000 × (1.045)³</li><li><strong>Calculate:</strong><br>(1.045)³ = 1.141166125<br>£12,000 × 1.141166125 = <strong>£13,693.99</strong></li><li><strong>Final Answer:</strong> £13,693.99</li></ol>',
        trap: 'Multiplying 4.5% by 3 (13.5%) for simple interest. In compound interest, each year earns interest on the previous interest.'
      },
      'm2-ratio': {
        title: 'Ratio & Direct Proportion',
        level: 'Maths Level 2',
        cluster: 'Number & The Number System',
        rule: 'To share in a ratio: 1) Add the parts to find total parts; 2) Divide total by number of parts to get the value of 1 part; 3) Multiply 1 part by each share ratio.',
        question: 'A regional training budget of £27,000 is shared between Digital Resources, Tutor Salaries, and Facilities in the ratio 4 : 5 : 1. How much more is spent on Tutor Salaries than Digital Resources?',
        steps: '<ol><li><strong>Add all parts:</strong><br>4 + 5 + 1 = <strong>10 total parts</strong></li><li><strong>Find 1 part:</strong><br>£27,000 ÷ 10 = <strong>£2,700 per part</strong></li><li><strong>Calculate individual amounts:</strong><br>Tutor Salaries (5 parts) = 5 × £2,700 = £13,500<br>Digital Resources (4 parts) = 4 × £2,700 = £10,800</li><li><strong>Calculate difference:</strong><br>£13,500 - £10,800 = <strong>£2,700</strong></li></ol>',
        trap: 'Confusing "sharing in a ratio" with "scaling up when one part is already known". Always read whether the given number is the TOTAL or ONE SPECIFIC SHARE.'
      },
      'm2-best-buy': {
        title: 'Best Buy & Unit Value Comparison',
        level: 'Maths Level 2',
        cluster: 'Number & The Number System',
        rule: 'Always convert both offers to an identical benchmark unit, such as cost in pence per 100g or per 100ml. State a clear concluding sentence comparing the two values.',
        question: 'Supplier A offers 750ml of hospital sanitiser for £3.45. Supplier B offers 1.2 litres of the same sanitiser for £5.16. Which supplier offers the better value for money? Show all calculations.',
        steps: '<ol><li><strong>Convert Supplier B volume to ml:</strong><br>1.2 litres = 1,200 ml</li><li><strong>Calculate cost per 100ml for Supplier A:</strong><br>345p ÷ 7.5 = <strong>46.00p per 100ml</strong></li><li><strong>Calculate cost per 100ml for Supplier B:</strong><br>516p ÷ 12.0 = <strong>43.00p per 100ml</strong></li><li><strong>Comparison & Conclusion:</strong><br>Supplier B is cheaper by 3p per 100ml (43p < 46p), therefore <strong>Supplier B offers the better value</strong>.</li></ol>',
        trap: 'Leaving the calculation with two decimal numbers without writing a written conclusion naming the supplier. Examiners require a final comparison statement.'
      },
      'm2-bidmas': {
        title: 'BIDMAS & Negative Numbers',
        level: 'Maths Level 2',
        cluster: 'Number & The Number System',
        rule: 'Operations order: Brackets → Indices → Division/Multiplication (left to right) → Addition/Subtraction. Subtracting a negative number becomes addition (e.g. 5 - (-3) = 8).',
        question: 'Evaluate the expression: 40 - 4 × (3 + 2)² + (-15)',
        steps: '<ol><li><strong>Brackets first:</strong> (3 + 2) = 5</li><li><strong>Indices next:</strong> 5² = 25</li><li><strong>Multiplication:</strong> 4 × 25 = 100</li><li><strong>Left to right addition/subtraction:</strong><br>40 - 100 + (-15) = -60 - 15 = <strong>-75</strong></li></ol>',
        trap: 'Subtracting 4 from 40 first (40 - 4 = 36) before multiplying. Multiplication MUST be performed before subtraction.'
      },
      'm2-formulas': {
        title: 'Workplace Formulas & Substitution',
        level: 'Maths Level 2',
        cluster: 'Number & The Number System',
        rule: 'Carefully follow brackets and order of operations inside formulas. Pay close attention to units (e.g. converting minutes to hours or cm to metres) before substituting.',
        question: 'A paramedic vehicle rental company uses the cost formula: C = 45 + 1.25(M - 50) where C is total cost in pounds and M is miles driven. Calculate the total cost for driving 146 miles.',
        steps: '<ol><li><strong>Substitute M = 146 into the formula:</strong><br>C = 45 + 1.25(146 - 50)</li><li><strong>Resolve brackets:</strong><br>146 - 50 = 96</li><li><strong>Multiply:</strong><br>1.25 × 96 = £120</li><li><strong>Add fixed fee:</strong><br>C = 45 + 120 = <strong>£165.00</strong></li></ol>',
        trap: 'Multiplying 1.25 by 146 first without subtracting the 50 free miles included in the brackets.'
      },
      'm2-perimeter': {
        title: 'Perimeter & Circumference',
        level: 'Maths Level 2',
        cluster: 'Measures, Shape & Space',
        rule: 'Perimeter is the total boundary distance around the 2D shape. For circles, Circumference = π × d (or 2 × π × r). Never confuse diameter with radius.',
        question: 'A running track consists of a central rectangle of length 80m and two semicircular ends with diameter 40m. What is the total distance of one complete lap around the perimeter of the track? (Use π = 3.14)',
        steps: '<ol><li><strong>Combine the two semicircular ends:</strong><br>Two semicircles = 1 complete circle with diameter d = 40m.</li><li><strong>Calculate circle circumference:</strong><br>C = π × d = 3.14 × 40 = <strong>125.6m</strong></li><li><strong>Add the two straight lengths:</strong><br>Two straight sides = 80m + 80m = 160m</li><li><strong>Total Lap Perimeter:</strong><br>160m + 125.6m = <strong>285.6 metres</strong></li></ol>',
        trap: 'Adding the internal width (40m) into the perimeter. Perimeter is ONLY the external boundary.'
      },
      'm2-area': {
        title: 'Area of Compound & L-Shaped Spaces',
        level: 'Maths Level 2',
        cluster: 'Measures, Shape & Space',
        rule: 'Split irregular L-shaped floorplans into two distinct rectangles. Clearly label dimensions of each rectangle and sum their areas. Always state units in m².',
        question: 'A hospital ward floor is L-shaped: overall length 14m, overall width 10m. The cutout section is 6m long by 4m wide. Medical linoleum flooring costs £18.50 per m² and is sold in whole packs of 5 m². Calculate the total cost of the flooring.',
        steps: '<ol><li><strong>Calculate area by subtraction:</strong><br>Total bounding box = 14m × 10m = 140 m²<br>Cutout area = 6m × 4m = 24 m²<br>Ward floor area = 140 - 24 = <strong>116 m²</strong></li><li><strong>Calculate packs needed:</strong><br>116 ÷ 5 = 23.2 packs → Round UP to <strong>24 whole packs</strong></li><li><strong>Calculate total cost:</strong><br>24 packs × 5 m² = 120 m²<br>120 m² × £18.50 = <strong>£2,220.00</strong></li></ol>',
        trap: 'Multiplying 116 directly by £18.50 without rounding up packs. If materials are sold in packs, you must round up to the nearest whole pack before calculating cost.'
      },
      'm2-circles': {
        title: 'Area of Circles & Semicircles',
        level: 'Maths Level 2',
        cluster: 'Measures, Shape & Space',
        rule: 'Area of a circle = π × r². If the question gives diameter d, halve it first to find radius r (r = d ÷ 2).',
        question: 'A circular memorial garden has a diameter of 7.2 metres. The center has a circular water feature with radius 1.2 metres. The remainder of the garden will be covered in decorative gravel. What is the gravel area? (Use π = 3.142. Round to 2 d.p.)',
        steps: '<ol><li><strong>Garden radius:</strong> r₁ = 7.2 ÷ 2 = 3.6m<br>Total garden area = 3.142 × 3.6² = 3.142 × 12.96 = <strong>40.72 m²</strong></li><li><strong>Water feature area:</strong> r₂ = 1.2m<br>Feature area = 3.142 × 1.2² = 3.142 × 1.44 = <strong>4.52 m²</strong></li><li><strong>Gravel area:</strong><br>40.72 - 4.52 = <strong>36.20 m²</strong></li></ol>',
        trap: 'Squaring the diameter directly (7.2²) instead of halving to find radius first.'
      },
      'm2-volume': {
        title: 'Volume of 3D Prisms & Cylinders',
        level: 'Maths Level 2',
        cluster: 'Measures, Shape & Space',
        rule: 'Volume of Prism = Cross-sectional Area × Length. For a cylinder: Volume = π × r² × h. Remember: 1 m³ = 1,000 litres.',
        question: 'A rainwater tank is a cylinder with diameter 1.6m and height 2.5m. Can this tank hold 5,000 litres of water? Justify your answer. (Use π = 3.142)',
        steps: '<ol><li><strong>Radius of tank:</strong> r = 1.6 ÷ 2 = 0.8m</li><li><strong>Calculate volume in m³:</strong><br>V = π × r² × h = 3.142 × (0.8)² × 2.5<br>V = 3.142 × 0.64 × 2.5 = <strong>5.0272 m³</strong></li><li><strong>Convert m³ to litres:</strong><br>5.0272 × 1,000 = <strong>5,027.2 litres</strong></li><li><strong>Conclusion:</strong><br>Yes, the tank can hold 5,000 litres because 5,027.2 litres > 5,000 litres.</li></ol>',
        trap: 'Forgetting to convert m³ to litres (1 m³ = 1000 litres) or omitting the written decision word (Yes/No).'
      },
      'm2-scale': {
        title: 'Scale Drawings & Bearings',
        level: 'Maths Level 2',
        cluster: 'Measures, Shape & Space',
        rule: 'Scale 1:50 means 1 cm on the drawing = 50 cm in real life (0.5m). Always measure carefully and state bearings with 3 figures (e.g. 065° not 65°).',
        question: 'On an architectural site plan with a scale of 1:200, a staff parking bay measures 3.5 cm long by 1.8 cm wide. What is the actual real-life area of the parking bay in square metres?',
        steps: '<ol><li><strong>Calculate real length:</strong><br>3.5 cm × 200 = 700 cm = <strong>7.0 metres</strong></li><li><strong>Calculate real width:</strong><br>1.8 cm × 200 = 360 cm = <strong>3.6 metres</strong></li><li><strong>Calculate actual area:</strong><br>7.0m × 3.6m = <strong>25.2 m²</strong></li></ol>',
        trap: 'Multiplying the drawing area (3.5 × 1.8 = 6.3 cm²) by 200. You must multiply by 200² (40,000) or convert dimensions to real metres FIRST!'
      },
      'm2-sdt': {
        title: 'Speed, Distance, Time & Density',
        level: 'Maths Level 2',
        cluster: 'Measures, Shape & Space',
        rule: 'Time in minutes MUST be converted to decimal hours by dividing by 60! 36 minutes = 36 ÷ 60 = 0.6 hours. Never write 1 hour 36 minutes as 1.36!',
        question: 'A mobile healthcare team travels 147 miles between health clinics. The journey departs at 08:45 and arrives at 11:15. Calculate their average speed in miles per hour (mph).',
        steps: '<ol><li><strong>Calculate journey duration:</strong><br>From 08:45 to 11:15 = 2 hours and 30 minutes</li><li><strong>Convert to decimal hours:</strong><br>30 mins ÷ 60 = 0.5 hours → Total time = <strong>2.5 hours</strong></li><li><strong>Calculate speed:</strong><br>Speed = Distance ÷ Time = 147 miles ÷ 2.5 hours = <strong>58.8 mph</strong></li></ol>',
        trap: 'Writing 2 hours 30 mins as 2.3 and calculating 147 ÷ 2.3 = 63.9 mph. This is an immediate error.'
      },
      'm2-units': {
        title: 'Metric & Imperial Conversions',
        level: 'Maths Level 2',
        cluster: 'Measures, Shape & Space',
        rule: 'Key conversion benchmarks: 1 mile ≈ 1.6 km (5 miles ≈ 8 km), 1 kg ≈ 2.2 pounds, 1 gallon ≈ 4.5 litres, 1 inch ≈ 2.54 cm.',
        question: 'A patient is weighed in the UK clinic as 14 stone and 4 pounds. The medication dosage chart requires patient body mass in kilograms. Given 1 stone = 14 pounds and 1 kg = 2.2 pounds, calculate the patient weight in kg. Round to the nearest whole kg.',
        steps: '<ol><li><strong>Convert total weight to pounds:</strong><br>(14 stone × 14) + 4 = 196 + 4 = <strong>200 pounds</strong></li><li><strong>Convert pounds to kilograms:</strong><br>200 ÷ 2.2 = <strong>90.909 kg</strong></li><li><strong>Round to nearest whole kg:</strong><br>90.909 kg → <strong>91 kg</strong></li></ol>',
        trap: 'Multiplying pounds by 2.2 instead of dividing. 1 kg is heavier than 1 pound, so the number of kg must be smaller than pounds.'
      },
      'm2-averages': {
        title: 'Mean, Median, Mode & Range Comparison',
        level: 'Maths Level 2',
        cluster: 'Handling Data & Statistics',
        rule: 'To compare two groups on Functional Skills exams, you MUST write TWO comparative sentences: 1) Compare the average (Mean or Median); 2) Compare the spread/consistency (Range). Use context words.',
        question: 'Clinic A wait times (minutes): 18, 22, 25, 29, 31 (Mean: 25.0, Range: 13). Clinic B wait times: 12, 14, 28, 36, 45 (Mean: 27.0, Range: 33). Write two comparative statements evaluating the performance of the two clinics.',
        steps: '<ol><li><strong>Average statement:</strong><br>"On average, patients at Clinic A had shorter wait times than Clinic B because their mean is lower (25 minutes compared to 27 minutes)."</li><li><strong>Consistency / Range statement:</strong><br>"Wait times at Clinic A were much more consistent and predictable than Clinic B because Clinic A has a smaller range (13 minutes compared to 33 minutes)."</li></ol>',
        trap: 'Saying "Clinic B has a bigger range so they did better". A smaller range means greater consistency and reliability!'
      },
      'm2-scatter': {
        title: 'Scatter Diagrams & Correlation',
        level: 'Maths Level 2',
        cluster: 'Handling Data & Statistics',
        rule: 'Always draw a straight line of best fit using a ruler, balancing points equally above and below the line. State the type of correlation: positive, negative, or no correlation.',
        question: 'A health study records weekly revision hours and mock exam percentages. The data shows that as revision hours increase, exam percentages consistently increase. Describe the correlation and explain how to predict the score for 7 hours of study.',
        steps: '<ol><li><strong>Describe correlation:</strong><br>There is a <strong>strong positive correlation</strong> between revision hours and exam percentages.</li><li><strong>Method of prediction:</strong><br>Draw a straight line of best fit through the data points. Locate 7 hours on the horizontal x-axis, draw a vertical dashed line to meet the line of best fit, then read across to the vertical y-axis to interpolate the predicted score.</li></ol>',
        trap: 'Connecting the points dot-to-dot instead of drawing one continuous straight line of best fit with a ruler.'
      },
      'm2-probability': {
        title: 'Probability (Single & Combined Events)',
        level: 'Maths Level 2',
        cluster: 'Handling Data & Statistics',
        rule: 'Probability = (Favourable Outcomes) ÷ (Total Possible Outcomes). P(Event will NOT happen) = 1 - P(Event will happen). Express answers as simplified fractions, decimals, or percentages.',
        question: 'In an apprenticeship cohort of 40 learners, 14 study Healthcare, 18 study Business Administration, and 8 study Digital Support. If a learner is chosen at random to speak at an open day, what is the probability that they do NOT study Business Administration? Give your answer as a simplified fraction.',
        steps: '<ol><li><strong>Identify non-Business learners:</strong><br>Healthcare (14) + Digital (8) = <strong>22 learners</strong></li><li><strong>Form the probability fraction:</strong><br>P(Not Business) = 22 / 40</li><li><strong>Simplify fraction:</strong><br>Divide numerator and denominator by 2 = <strong>11 / 20</strong> (or 0.55 / 55%)</li></ol>',
        trap: 'Writing probability as a ratio (e.g. 11:9). Probabilities MUST be written as a fraction, decimal, or percentage, never a ratio.'
      },
      'm2-frequency': {
        title: 'Grouped Frequency Tables & Estimated Mean',
        level: 'Maths Level 2',
        cluster: 'Handling Data & Statistics',
        rule: 'For grouped data: 1) Find the midpoint of each interval; 2) Multiply Midpoint × Frequency (fx); 3) Sum all fx values; 4) Divide by Total Frequency (sum of f).',
        question: 'Wait times at an assessment center: 0-10 mins (f=4), 10-20 mins (f=11), 20-30 mins (f=5). Calculate the estimated mean wait time.',
        steps: '<ol><li><strong>Find midpoints:</strong><br>0-10: 5<br>10-20: 15<br>20-30: 25</li><li><strong>Multiply midpoints by frequency (fx):</strong><br>5 × 4 = 20<br>15 × 11 = 165<br>25 × 5 = 125</li><li><strong>Calculate totals:</strong><br>Total fx = 20 + 165 + 125 = 310<br>Total frequency = 4 + 11 + 5 = 20</li><li><strong>Estimated Mean:</strong><br>310 ÷ 20 = <strong>15.5 minutes</strong></li></ol>',
        trap: 'Dividing total fx by 3 (the number of rows) instead of 20 (the total number of people/frequency).'
      },
      'm2-charts': {
        title: 'Dual Bar, Pie & Line Graphs',
        level: 'Maths Level 2',
        cluster: 'Handling Data & Statistics',
        rule: 'To calculate pie chart angles: Angle = (Category Frequency ÷ Total Frequency) × 360°. Always label axes, including units and a clear title.',
        question: 'A survey of 72 adult learners asked their preferred study mode: 36 chose Online Evening, 18 chose Weekend Bootcamp, and 18 chose Self-Paced. Calculate the sector angle for Weekend Bootcamp in a pie chart.',
        steps: '<ol><li><strong>Find degrees per learner:</strong><br>360° ÷ 72 total learners = <strong>5° per learner</strong></li><li><strong>Calculate Weekend Bootcamp angle:</strong><br>18 learners × 5° = <strong>90°</strong> (a right angle)</li><li><strong>Check full circle:</strong><br>(36 × 5°) + 90° + 90° = 180° + 90° + 90° = 360°. Correct.</li></ol>',
        trap: 'Dividing 72 by 360 instead of dividing 360 by the total 72.'
      },
      'e2-letter': {
        title: 'Formal Business Letter Writing',
        level: 'English Level 2',
        cluster: 'Writing Formats & Composition',
        rule: 'Include 2 addresses (Sender top right, Recipient top left), formal date, formal salutation, subject line, 3-4 structured paragraphs, and the correct sign-off: "Yours faithfully" (unknown name) vs "Yours sincerely" (named recipient).',
        question: 'Write a formal letter to your local council chief executive objecting to proposed library closures in your community. Explain the negative impacts on adult learners and propose alternative funding ideas.',
        steps: '<ol><li><strong>Sender Address:</strong> Top right corner, followed by date (e.g. 10 October 2026).</li><li><strong>Recipient Address:</strong> Left margin below date: Chief Executive, City Council, Civic Centre.</li><li><strong>Salutation:</strong> Dear Chief Executive (or Dear Mr Vance).</li><li><strong>Subject Line:</strong> RE: Proposed Community Library Closures - Formal Objection</li><li><strong>Body Paragraphs:</strong><br>- Para 1: Purpose of writing and firm objection.<br>- Para 2: Impact on adult education, digital access, and jobseekers.<br>- Para 3: Viable alternative solutions (community volunteers, shared spaces).</li><li><strong>Sign-off:</strong> Yours faithfully (if unnamed) or Yours sincerely (if named), followed by full printed name.</li></ol>',
        trap: 'Using informal sign-offs like "Best regards" or "Thanks", or mixing up "Yours faithfully" with a named recipient.'
      },
      'e2-article': {
        title: 'Persuasive Articles (Community & Workplace)',
        level: 'English Level 2',
        cluster: 'Writing Formats & Composition',
        rule: 'Articles require: 1) Eye-catching Headline; 2) Byline (By Education Specialist); 3) Introductory hook; 4) Subheadings for each major point; 5) Balanced persuasive argument; 6) Memorable call to action.',
        question: 'Write an article for a local newspaper promoting the importance of adult education and gaining Level 2 Functional Skills qualifications.',
        steps: '<ol><li><strong>Headline:</strong> Unlocking Potential: Why Functional Skills Level 2 Is Your Passport to Career Success</li><li><strong>Byline:</strong> By Lead Academic Specialist</li><li><strong>Introductory Hook:</strong> Rhetorical question addressing the reader: "Have you ever found your career progression blocked by the absence of a GCSE Maths or English certificate?"</li><li><strong>Subheadings & Content:</strong><br>- <em>The Gateway to Nursing and Higher Education</em><br>- <em>Flexible Learning Built for Busy Adults</em><br>- <em>Confidence Beyond the Classroom</em></li><li><strong>Call to Action:</strong> Encourage the reader to take the first step towards enrolment today.</li></ol>',
        trap: 'Writing an essay without article formatting (forgetting headline, subheadings, and engaging reader address).'
      },
      'e2-email': {
        title: 'Professional Workplace Emails',
        level: 'English Level 2',
        cluster: 'Writing Formats & Composition',
        rule: 'Emails require: Precise Subject Line, polite opening (e.g. "Dear Colleagues / Good morning Team"), concise paragraphs with bullet points for readability, clear deadlines/actions, and a professional sign-off.',
        question: 'Write an email to departmental staff announcing a new remote exam protocol. Outline equipment requirements, scheduled practice runs, and technical support contacts.',
        steps: '<ol><li><strong>Subject Line:</strong> Urgent: Mandatory Remote Functional Skills Exam Protocols & Setup Instructions</li><li><strong>Salutation:</strong> Dear Team,</li><li><strong>Opening:</strong> State the purpose clearly in the first sentence.</li><li><strong>Bulleted Details:</strong> Use bullet points for webcam requirements, quiet room standards, and photo ID submission.</li><li><strong>Call to Action / Next Steps:</strong> Specify the deadline for completing practice run-throughs.</li><li><strong>Sign-off:</strong> Kind regards, / Best regards, followed by full job title.</li></ol>',
        trap: 'Writing long dense blocks of unbroken text. Workplace emails must use bullet points and clear white space for dyslexia-friendly clarity.'
      },
      'e2-report': {
        title: 'Formal Reports & Proposals',
        level: 'English Level 2',
        cluster: 'Writing Formats & Composition',
        rule: 'Formal reports MUST include: 1) Title; 2) Purpose / Terms of Reference; 3) Numbered/labelled Subheadings for Findings; 4) Conclusion; 5) Actionable Recommendations.',
        question: 'Write a workplace report evaluating staff digital skills and recommending the rollout of Digital Functional Skills training.',
        steps: '<ol><li><strong>Title:</strong> Report on Administrative Digital Competencies and Training Needs</li><li><strong>Terms of Reference:</strong> "This report investigates existing digital literacy levels across the department and evaluates the impact of delivering Level 2 Digital Functional Skills."</li><li><strong>Findings:</strong><br>- <em>Current Productivity Bottlenecks</em><br>- <em>Data Security Compliance</em></li><li><strong>Conclusions:</strong> Summarise that 68% of staff would benefit from formal qualification training.</li><li><strong>Recommendations:</strong> 1) Implement 6-week cohort workshops; 2) Partner with MasterFunctionalSkills for diagnostic testing.</li></ol>',
        trap: 'Forgetting the Recommendations section. Reports on Pearson Edexcel English Writing exams lose 3-4 marks if practical recommendations are omitted.'
      },
      'e2-speech': {
        title: 'Persuasive Speeches & Rhetoric (AFOREST)',
        level: 'English Level 2',
        cluster: 'Writing Formats & Composition',
        rule: 'Speeches must establish direct audience rapport ("Good morning governors and colleagues"), use AFOREST devices (Alliteration, Facts, Opinions, Rhetorical questions, Emotive language, Statistics, Triads), and end with an inspirational rallying call.',
        question: 'Deliver a persuasive speech to college governors advocating for free evening child-care facilities to support adult learners attending Functional Skills classes.',
        steps: '<ol><li><strong>Opening:</strong> "Good evening members of the board. Look around our community and ask yourselves: how many brilliant minds are left behind simply because they cannot afford childcare?"</li><li><strong>AFOREST Devices:</strong><br>- Triad: "We have the space, we have the passion, and we have the moral obligation to act."<br>- Statistics: "Over 42% of our absent learners cite child-care conflicts."</li><li><strong>Counter-argument:</strong> Acknowledge financial cost and refute it with long-term retention benefits.</li><li><strong>Closing:</strong> "Let us tear down this barrier tonight. Thank you."</li></ol>',
        trap: 'Writing in an essay style without addressing the audience or using speech markers ("Thank you for listening").'
      },
      'e2-commas': {
        title: 'Eliminating Comma Splices & Run-Ons',
        level: 'English Level 2',
        cluster: 'SPaG (Spelling, Punctuation & Grammar)',
        rule: 'A comma splice occurs when two complete sentences (independent clauses) are joined by only a comma. Fix it using: 1) A full stop; 2) A semicolon (;); or 3) A comma with a coordinating conjunction (for, and, nor, but, or, yet, so).',
        question: 'Identify the comma splice in this sentence and demonstrate two correct ways to repair it: "The mock exam was challenging, many students completed it with high marks."',
        steps: '<ol><li><strong>Diagnosis:</strong> "The mock exam was challenging" and "many students completed it with high marks" are two independent clauses incorrectly joined by a comma.</li><li><strong>Correction 1 (Semicolon):</strong> "The mock exam was challenging; many students completed it with high marks."</li><li><strong>Correction 2 (Conjunction):</strong> "The mock exam was challenging, but many students completed it with high marks."</li><li><strong>Correction 3 (Two sentences):</strong> "The mock exam was challenging. Many students completed it with high marks."</li></ol>',
        trap: 'Using a comma before "however" without a semicolon or full stop beforehand (e.g. "...challenging, however many students..." is still a comma splice!).'
      },
      'e2-apostrophes': {
        title: 'Apostrophes of Possession vs Contraction',
        level: 'English Level 2',
        cluster: 'SPaG (Spelling, Punctuation & Grammar)',
        rule: 'Possession: Singular noun adds \'s (the patient\'s chart). Regular plural adds only an apostrophe after s (the patients\' charts). Irregular plural adds \'s (children\'s ward). Contraction: it\'s = it is. Its = belonging to it (no apostrophe!).',
        question: 'Correct the apostrophe errors in this passage: "The hospital updated it\'s policy regarding visitors passes. Both doctor\'s and nurses\' lockers have been relocated to the childrens unit."',
        steps: '<ol><li><strong>it\'s → its:</strong> "Its policy" (possessive pronoun, no apostrophe).</li><li><strong>visitors → visitors\':</strong> Plural possession (the passes belonging to multiple visitors).</li><li><strong>doctor\'s → doctors\':</strong> Plural doctors (both doctors\' and nurses\' lockers).</li><li><strong>childrens → children\'s:</strong> Irregular plural noun requires \'s (children\'s unit).</li></ol>',
        trap: 'Writing "it\'s" for possession. "It\'s" ONLY means "it is" or "it has". If you cannot substitute "it is", do NOT use an apostrophe.'
      },
      'e2-sentences': {
        title: 'Complex & Compound Sentences',
        level: 'English Level 2',
        cluster: 'SPaG (Spelling, Punctuation & Grammar)',
        rule: 'To achieve Top Band in Pearson Edexcel English Writing, you must vary sentence structures: simple sentences, compound sentences (with FANBOYS), and complex sentences starting with subordinating connectives (Although, Whereas, Because, Since).',
        question: 'Combine these two simple sentences into a high-level complex sentence using a fronted subordinate clause: "The candidate experienced severe exam anxiety. She achieved 88% on her Pearson Edexcel Level 2 exam."',
        steps: '<ol><li><strong>Subordinating connective choice:</strong> "Although" or "Even though" to show contrast.</li><li><strong>Fronted clause with comma:</strong><br>"Although the candidate experienced severe exam anxiety, she achieved 88% on her Pearson Edexcel Level 2 exam."</li><li><strong>Alternative compound structure:</strong><br>"The candidate experienced severe exam anxiety; nevertheless, she achieved 88% on her Pearson Edexcel Level 2 exam."</li></ol>',
        trap: 'Omitting the comma after a fronted subordinate clause (e.g. "Although she was tired she studied" needs a comma after "tired").'
      },
      'e2-agreement': {
        title: 'Subject-Verb Agreement & Tense Control',
        level: 'English Level 2',
        cluster: 'SPaG (Spelling, Punctuation & Grammar)',
        rule: 'Singular subjects take singular verbs (The team of researchers IS publishing). Avoid shifting between past and present tense within the same paragraph.',
        question: 'Identify and correct the agreement and tense shifts in: "The group of apprentices are arriving early yesterday, and they discusses the assignment."',
        steps: '<ol><li><strong>Subject agreement:</strong> "The group" is a collective singular subject → "The group was" (or "The apprentices were").</li><li><strong>Tense consistency:</strong> "Yesterday" requires past tense throughout: "arrived" and "discussed".</li><li><strong>Corrected sentence:</strong> "The group of apprentices arrived early yesterday, and they discussed the assignment."</li></ol>',
        trap: 'Letting words between the subject and verb confuse you (e.g. in "The list of requirements ARE ready", the subject is "list" [singular], so it must be "IS ready").'
      },
      'e2-paragraphs': {
        title: 'Paragraphing & Cohesive Devices (PEEL)',
        level: 'English Level 2',
        cluster: 'SPaG (Spelling, Punctuation & Grammar)',
        rule: 'Every body paragraph should follow PEEL: Point (Topic sentence) → Evidence / Example → Explanation (How it impacts/proves the point) → Link (Connecting back to the main question/thesis).',
        question: 'Demonstrate a model PEEL paragraph arguing for funded online revision resources for apprentice healthcare workers.',
        steps: '<ol><li><strong>Point:</strong> First and foremost, funded online revision portals significantly reduce attrition rates among healthcare apprentices.</li><li><strong>Evidence:</strong> For instance, NHS trusts that introduced 24/7 digital revision modules recorded a 32% increase in first-time Level 2 pass rates.</li><li><strong>Explanation:</strong> This is because shift workers cannot attend fixed classroom timetables, whereas modular bite-sized lessons allow them to revise flexibly between ward duties.</li><li><strong>Link:</strong> Therefore, investing in turnkey digital learning is both an educational and operational necessity.</li></ol>',
        trap: 'Writing one massive unbroken page of text. Functional Skills examiners immediately deduct marks if clear paragraphs are missing.'
      },
      'e2-purpose': {
        title: 'Identifying Purpose & Target Audience',
        level: 'English Level 2',
        cluster: 'Reading Analysis & Comprehension',
        rule: 'Texts are created to Persuade, Inform, Advise, Instruct, or Entertain. Identify purpose by examining tone, language techniques (imperative verbs for instructing; emotive adjectives for persuading), and visual features.',
        question: 'A text contains the phrases: "You must submit your application by Friday", "Complete steps 1 to 4 in order", and "Ensure your ID is verified". What is the primary purpose and tone of this text?',
        steps: '<ol><li><strong>Primary Purpose:</strong> To <strong>instruct / direct</strong> the reader on how to complete an application.</li><li><strong>Tone:</strong> Formal, authoritative, and direct.</li><li><strong>Evidence:</strong> Use of imperative (command) verbs ("submit", "complete", "ensure") and chronological numbered steps.</li></ol>',
        trap: 'Selecting "persuade" simply because the text gives advice. If it commands specific procedural actions, it is instructing.'
      },
      'e2-bias': {
        title: 'Detecting Bias, Fact vs Opinion',
        level: 'English Level 2',
        cluster: 'Reading Analysis & Comprehension',
        rule: 'Facts can be independently verified with evidence and data. Opinions are personal beliefs or value judgements. Bias occurs when a writer presents only one side, uses emotive adjectives, or has a commercial/financial incentive.',
        question: 'Evaluate whether this statement contains bias: "Our revolutionary tutoring platform is undisputed as the only effective way to pass your Maths exam, outperforming outdated traditional schools."',
        steps: '<ol><li><strong>Bias Identification:</strong> The statement exhibits heavy commercial bias.</li><li><strong>Emotive / Subjective Language:</strong> Words like "revolutionary", "undisputed", and "outdated" are value judgements, not proven facts.</li><li><strong>One-sidedness:</strong> Dismisses all traditional schools without providing independent comparative statistical proof.</li></ol>',
        trap: 'Treating quotes from company directors or advertisements as impartial facts.'
      },
      'e2-comparison': {
        title: 'Comparing Ideas Across Two Texts (Synthesis)',
        level: 'English Level 2',
        cluster: 'Reading Analysis & Comprehension',
        rule: 'When comparing two texts on Pearson Edexcel English Reading: 1) Cite points from BOTH texts; 2) Use comparative conjunctions (Similarly, In contrast, However, Whereas); 3) Synthesise ideas rather than writing two separate summaries.',
        question: 'Text A argues that remote online exams reduce learner stress. Text B argues that remote exams increase technical anxiety. Write a synthesised comparative response.',
        steps: '<ol><li><strong>Model Comparative Synthesis:</strong><br>"Both texts discuss the psychological impact of remote examinations on adult candidates. In Text A, the author contends that sitting exams at home reduces stress by removing travel pressures and unfamiliar classroom environments. In contrast, Text B highlights that learners frequently suffer heightened anxiety regarding internet reliability, webcams, and software crashes. While Text A focuses primarily on convenience, Text B emphasises the need for robust technical onboarding."</li></ol>',
        trap: 'Writing about Text A in paragraph 1, then Text B in paragraph 2 without directly comparing them sentence-by-sentence with comparative connectives.'
      },
      'e2-layout': {
        title: 'Organizational & Layout Features',
        level: 'English Level 2',
        cluster: 'Reading Analysis & Comprehension',
        rule: 'Explain HOW layout features help the reader. Never just say "it looks nice". Bullet points break down complex lists; bold font highlights urgency; text boxes isolate critical warnings.',
        question: 'Why has the author used a shaded text box and bullet points in an exam candidate briefing guide?',
        steps: '<ol><li><strong>Shaded Text Box Purpose:</strong> Visually isolates crucial examination rules from the main narrative, immediately drawing the reader\'s eye so vital regulations are not overlooked.</li><li><strong>Bullet Points Purpose:</strong> Breaks down complex technical requirements into discrete, digestible steps, allowing candidates to check off items one by one for clarity.</li></ol>',
        trap: 'Giving vague answers like "to make it interesting". Marks are only awarded for explaining how it aids reader understanding and information retrieval.'
      },
      'e2-inference': {
        title: 'Implicit vs Explicit Meaning (Inference)',
        level: 'English Level 2',
        cluster: 'Reading Analysis & Comprehension',
        rule: 'Explicit meaning is directly stated in black and white. Implicit meaning is implied or hinted at beneath the surface ("reading between the lines").',
        question: 'The text states: "James checked his watch for the fourth time in five minutes, his fingers drumming against the silent computer screen." What can you infer about James\'s feelings?',
        steps: '<ol><li><strong>Explicit facts:</strong> James looked at his watch 4 times and tapped his fingers.</li><li><strong>Valid Inferences:</strong> James is experiencing extreme impatience, anxiety, or stress due to a delay or technical freeze.</li><li><strong>Evidence:</strong> Frequent time-checking and nervous finger tapping are universal physical indicators of anxious anticipation.</li></ol>',
        trap: 'Making wild guesses that have no textual evidence (e.g. guessing he had an argument with his boss). Inferences must be firmly tethered to textual clues.'
      },
      'm1-place-value': {
        title: 'Place Value, Rounding & Estimation',
        level: 'Maths Level 1',
        cluster: 'Maths Level 1 Essentials',
        rule: 'Look at the digit immediately to the right: if 5 or more, round UP; if 4 or less, round DOWN. Front-end estimation rounds to 1 significant figure to quickly check reasonableness.',
        question: 'Estimate the total cost of purchasing 19 ergonomic desk chairs at £48.75 each.',
        steps: '<ol><li><strong>Round items to nearest 10:</strong> 19 chairs ≈ 20 chairs</li><li><strong>Round price to nearest 10:</strong> £48.75 ≈ £50</li><li><strong>Estimate:</strong> 20 × £50 = <strong>£1,000</strong></li><li><strong>Actual Check:</strong> 19 × £48.75 = £926.25. The estimate of £1,000 is reasonable and confirms calculation order.</li></ol>',
        trap: 'Calculating the exact answer when the question explicitly states "Estimate". Estimating questions require rounded working for full marks.'
      },
      'm1-fractions': {
        title: 'Simple Fractions & Benchmark Percentages',
        level: 'Maths Level 1',
        cluster: 'Maths Level 1 Essentials',
        rule: 'Core benchmarks: 50% = 1/2 (divide by 2); 25% = 1/4 (divide by 4); 10% = 1/10 (divide by 10); 75% = 3/4 (find 25% and multiply by 3).',
        question: 'A retail store offers 25% off a training uniform costing £64. How much is the discount, and what is the sale price?',
        steps: '<ol><li><strong>Calculate 25% discount:</strong><br>25% = 1/4 → £64 ÷ 4 = <strong>£16.00 discount</strong></li><li><strong>Calculate sale price:</strong><br>£64 - £16 = <strong>£48.00</strong></li></ol>',
        trap: 'Stopping at £16 when asked for the sale price. Always check if the question asks for the DISCOUNT or the FINAL PRICE.'
      },
      'm1-perimeter-area': {
        title: 'Simple Perimeter & Area of Rectangles',
        level: 'Maths Level 1',
        cluster: 'Maths Level 1 Essentials',
        rule: 'Perimeter = 2 × (Length + Width) (distance around outside). Area = Length × Width (surface inside in square units cm² or m²).',
        question: 'A classroom noticeboard is 3m wide and 1.5m high. What is: a) the perimeter for border ribbon, and b) the area for backing paper?',
        steps: '<ol><li><strong>Perimeter:</strong> 3m + 1.5m + 3m + 1.5m = <strong>9 metres</strong> of border ribbon.</li><li><strong>Area:</strong> 3m × 1.5m = <strong>4.5 m²</strong> of backing paper.</li></ol>',
        trap: 'Confusing units (e.g. putting m² for perimeter or m for area).'
      },
      'm1-money-time': {
        title: 'Money Calculations & 12/24-Hour Time',
        level: 'Maths Level 1',
        cluster: 'Maths Level 1 Essentials',
        rule: 'Always include the £ or p symbol. Never write £4.5 (write £4.50 with two decimal places). For 24-hour time, add 12 to PM hours (e.g. 3:45 pm = 15:45).',
        question: 'A training webinar begins at 14:15 and lasts for 1 hour and 50 minutes. What time does the webinar conclude in 12-hour am/pm clock format?',
        steps: '<ol><li><strong>Add 1 hour:</strong> 14:15 + 1 hr = 15:15</li><li><strong>Add 50 minutes:</strong> 15:15 + 45m = 16:00 + 5m = <strong>16:05</strong></li><li><strong>Convert 16:05 to 12-hour time:</strong><br>16:05 - 12 = <strong>4:05 pm</strong></li></ol>',
        trap: 'Forgetting to specify am or pm when converting to 12-hour time format.'
      },
      'e1-sentence-basics': {
        title: 'Sentence Punctuation & Capitalisation',
        level: 'English Level 1',
        cluster: 'English Level 1 Essentials',
        rule: 'Every sentence MUST start with a capital letter and end with a full stop, question mark, or exclamation mark. Capitalise the pronoun "I", names of people, days, months, and specific places.',
        question: 'Correct the capitalization and punctuation in: "on wednesdays i travel to oxford with sarah to attend my maths class"',
        steps: '<ol><li><strong>Capitalise start of sentence:</strong> "On"</li><li><strong>Capitalise proper nouns:</strong> "Wednesdays", "I", "Oxford", "Sarah"</li><li><strong>Add terminating punctuation:</strong> Full stop at the end.</li><li><strong>Corrected:</strong> "On Wednesdays I travel to Oxford with Sarah to attend my maths class."</li></ol>',
        trap: 'Leaving the personal pronoun "i" in lower-case.'
      },
      'e1-informal-email': {
        title: 'Everyday Workplace & Community Emails',
        level: 'English Level 1',
        cluster: 'English Level 1 Essentials',
        rule: 'Include: Clear subject line, greeting (Hi David / Dear Sarah), short paragraphs stating the message, and a friendly sign-off (Best regards / Thanks).',
        question: 'Write a short email to your course tutor explaining that you will be 15 minutes late for your Functional Skills lesson due to transport delays.',
        steps: '<ol><li><strong>Subject:</strong> Late arrival for today\'s lesson - [Your Name]</li><li><strong>Greeting:</strong> Dear Tutor,</li><li><strong>Message:</strong> "I am writing to let you know that my bus is delayed in traffic. I expect to arrive approximately 15 minutes late at 10:15. I will join the class as quietly as possible."</li><li><strong>Sign-off:</strong> Thanks, [Your Name]</li></ol>',
        trap: 'Sending emails with no subject line or no greeting.'
      },
      'e1-reading-main': {
        title: 'Extracting Main Ideas & Key Facts',
        level: 'English Level 1',
        cluster: 'English Level 1 Essentials',
        rule: 'Skim read headlines and subheadings to locate where the topic is discussed. Scan for specific numbers, dates, times, and capitalised names.',
        question: 'A community flyer says: "Free drop-in digital help every Thursday from 10am to 12pm in Room 4 at St Mary\'s Hub. Bring your own tablet or laptop." What day, time, and location is the session?',
        steps: '<ol><li><strong>Day:</strong> Every Thursday</li><li><strong>Time:</strong> 10:00 am to 12:00 pm</li><li><strong>Location:</strong> Room 4, St Mary\'s Hub</li><li><strong>Requirement:</strong> Bring your own tablet or laptop.</li></ol>',
        trap: 'Giving incomplete information (e.g. stating "Thursday" but omitting the room or hub name).'
      },
      'e1-alphabetical': {
        title: 'Alphabetical Order & Index Searching',
        level: 'English Level 1',
        cluster: 'English Level 1 Essentials',
        rule: 'Check the first letter of each word. If first letters are identical, look at the second letter; if those are identical, look at the third letter.',
        question: 'Place these patient medical record surnames in alphabetical order: Brown, Bailey, Baker, Bennett, Barnes.',
        steps: '<ol><li>All begin with \'B\'. Look at the second letter: Bailey (Ba), Baker (Ba), Barnes (Ba), Bennett (Be), Brown (Br).</li><li>Order the \'Ba\' words by third letter: Ba<strong>i</strong>ley, Ba<strong>k</strong>er, Ba<strong>r</strong>nes.</li><li>Full alphabetical order: <strong>Bailey, Baker, Barnes, Bennett, Brown</strong>.</li></ol>',
        trap: 'Stopping after comparing only the first two letters when words share the same initial two letters.'
      }
    };

    function openTopicModal(topicId) {
      const data = topicData[topicId];
      if (!data) return;

      document.getElementById('modalTopicTitle').innerText = data.title;
      document.getElementById('modalTopicLevel').innerText = data.level;
      document.getElementById('modalTopicCluster').innerText = data.cluster;
      document.getElementById('modalTopicRule').innerText = data.rule;
      document.getElementById('modalTopicQuestion').innerHTML = data.question;
      document.getElementById('modalTopicSteps').innerHTML = data.steps;
      document.getElementById('modalTopicTrap').innerText = data.trap;

      const waText = encodeURIComponent(`Hello, I would like to book 1-to-1 tutoring on the Functional Skills topic: ${data.title} (${data.level})`);
      document.getElementById('modalWhatsAppLink').href = `https://wa.me/447564525425?text=${waText}`;

      const modal = document.getElementById('topicModal');
      modal.classList.add('active');
      document.body.style.overflow = 'hidden';
    }

    function closeTopicModal() {
      const modal = document.getElementById('topicModal');
      modal.classList.remove('active');
      document.body.style.overflow = '';
    }

    function handleBackdropClick(event) {
      if (event.target === document.getElementById('topicModal')) {
        closeTopicModal();
      }
    }

    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        closeTopicModal();
      }
    });
  </script>
'''

# Replace or append scripts
if 'openTopicModal' not in content:
    idx = content.rfind('</body>')
    if idx != -1:
        content = content[:idx] + topic_js + '\n' + content[idx:]
        print("Topic modal JavaScript and data dictionary inserted successfully.")

with open('/home/subi/Projects/masterfunctionalskills.co.uk/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html successfully.")
