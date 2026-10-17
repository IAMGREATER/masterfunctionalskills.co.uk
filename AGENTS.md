# Master Functional Skills (MFS) — Project Agent Instructions & Model Solutions Routine

This document sets out the core architecture, established rules, and formatting standards for generating, annotating, assembling, and deploying model solutions for Master Functional Skills (`masterfunctionalskills.co.uk`).

---

## 1. Core Formatting & Layout Rules

### A. Right-Margin Boundary & Text-Wrapping (STRICT)
- **Margin Boundary**: In Pearson Edexcel exam booklets, the right working box boundary is at $x \approx 518.2$.
- **Wrapping Threshold**: All handwritten working, calculations, notes, annotations, and mark tags (`[M1]`, `[A1]`, `[B1]`) must stay comfortably within $x \le 480 - 490$.
- **No Overflow Rule**: Never allow text or calculations to cross the right border or fall off the page. Any line approaching $x \approx 480$ must be cleanly broken into two lines with proper indentation.

### B. Accurate Placement & Collision Avoidance
- Annotations must sit strictly inside designated working areas without writing over pre-printed question text, instructions, diagrams, or borders.
- For questions with pre-printed statements or tables inside working boxes, inspect the bounding boxes of existing text blocks ($y_{\text{bottom}}$) and begin handwriting comfortably below them.
- Always verify exact bounding box coordinates of table rows and diagrams before placing highlights or text.

### C. Automated Collision Verification
- Always run automated bounding box collision detection comparing the generated booklet against the original question paper text blocks.
- Require **0 collisions** across all pages before deploying.

### D. Multi-Colour Pedagogical Ink Hierarchy
- **Navy** (`#0f172a` / `(0.06, 0.09, 0.16)`): Student mathematical calculations, working steps, and final answer values.
- **Emerald** (`#0f766e` / `(0.06, 0.46, 0.43)`): Step titles, method guidance, and pedagogical teaching tips.
- **Crimson** (`#dc2626` / `(0.86, 0.15, 0.15)`): Pearson Edexcel official mark scheme allocations (`[M1]`, `[A1]`, `[B1]`) and callouts.
- **Gold** (`#d97706` / `(0.85, 0.47, 0.02)`): Key term highlights and formula callouts.

### E. Typography & Glyph Safety
- The `kalam`, `kalam-reg`, and `caveat` fonts **do not** support Unicode arrows (`←`, `→`) or symbols (`✓`, `✗`) (which produce missing glyph boxes `[]`).
- Always use ASCII arrows (`-->`, `<--`) and render checkmarks using vector shapes (`draw_vector_check()`).

### F. Red Copyright Grid Lines Protocol (Mock Papers)
- Source question papers (e.g. from PFS) often contain embedded copyright grid lines or watermarks configured to appear only upon printing.
- Always strip all watermark/grid layers with `strip_red_watermarks` before annotation so both on-screen viewing and physical printing are 100% clean.

---

## 2. Standard Reformed Booklet Assembly & Deployment

1. Strip blank spare pages and competitor covers.
2. Insert custom high-converting MFS branded Section A and Section B cover pages.
3. Insert Service Promo page after Section A cover, and Merch Promo page at the end of the booklet.
4. Deploy completed 21/22-page PDF booklets to `assets/downloads/past-papers/edexcel/<level>/` and `~/Documents/`.
5. Add the Model Solution download button (`btn-paper-model`) to all 5 website HTML hub files:
   - `edexcel-functional-skills-maths-level-1-past-papers.html`
   - `functional-skills-past-papers.html`
   - `past-papers.html`
   - `test_dyslexia_bar.html`
   - `test_dyslexia_visual.html`

---

## 3. Scope & Protected Papers

- **Level 2 Immutable Constraint**: Under NO circumstances alter Pearson Edexcel Maths Level 2 Past Papers 1 through 10, Practice Papers 1-3, Sample, or Legacy 2018 papers (100% complete and live).
- **Level 1 Scope**: Complete Reformed Past Papers 1 to 10, Practice Papers 1 to 3, and Legacy Papers 2017–2018.

---

## 4. Telegram Progress Updates

- Always keep the user posted on progress, verification results, and completed papers via the DarkNight Telegram bot (`darknight-notify` / `@darknight_subi_bot`).

---

## 5. Video Solution Walkthrough Specifications

### A. Official Designated Voiceover
- **Voice**: **Sonia** (`en-GB-SoniaNeural`)
- **Engine**: Microsoft Edge Neural TTS (`uvx edge-tts`)
- **Speech Rate**: `-2%` (calibrated for clear, patient, dyslexia-friendly instructional cadence).
- **Mastering**: Audio processed via FFmpeg with highpass filter ($80\text{ Hz}$) and EBU R128 loudness normalization (`loudnorm=I=-16:TP=-1.5:LRA=11`), followed by natural step padding ($0.6\text{s}$ pause between working steps, $1.8\text{s}$ conclusion pause).
- **Status**: Officially chosen voice for all Pearson Edexcel Functional Skills video walkthroughs across `masterfunctionalskills.co.uk`.

### B. Video Encoding & Text Artifact Prevention
- **Issue Noted**: 4:2:0 chroma subsampling (`-pix_fmt yuv420p`) causes colored ink ringing/chroma bleed (blue, green, red halos) around fine handwritten text against white canvas backgrounds.
- **Protocol for Full Rerender**:
  - Apply accurate chroma scaling flags: `-sws_flags spline+accurate_rnd+full_chroma_inp+full_chroma_int` and anti-aliased ink rendering.
  - Test `-pix_fmt yuv444p` or optimized x264 chroma parameters (`-crf 12 -preset slow -tune stillimage`) so text remains razor-sharp without color fringing.
- **Rerender Roadmap**: Once AI generation credits / billing are refreshed, re-render both Section A (Non-Calc) and Section B (Calc) Past Paper 10 with Sonia and the clean chroma pipeline, then proceed with the remaining past papers on the website.

---

## 6. Online Revision & Mathematics Visual System Routine

When authoring, redesigning, or auditing learning and revision pages across `masterfunctionalskills.co.uk`:

### A. Centre Branding & Confidentiality (STRICT)
- **Centre Name**: Strictly **Master Functional Skills** (MFS).
- **Confidentiality Mandate**: Never mention Oxford Health, NHS, external hospital trusts, or client partner organisations.
- **Vocational Contexts**: Always use generic, realistic vocational contexts (e.g. *"Community healthcare clinic"*, *"Medical diagnostics facility"*, *"Commercial catering & food services"*, *"Estates & facilities maintenance"*, *"Care home staffing"*).

### B. "No-Squinting" Visual Mathematics Standard
- **Zero Inline Text Strings**: Eliminate cramped, plain inline calculation strings (e.g. never write `145.80 + 39.45 = ...` or `58.7 × 19.4 ÷ 0.48` as plain inline text). Every calculation must be presented in a dedicated visual container.
- **Large Bold Typography**: Numbers and mathematical symbols must be large (`1.25rem` to `2.25rem`), bold, and set to tabular figures (`font-variant-numeric: tabular-nums`).
- **Vertical Place-Value Alignment (`.math-col-board`, `.math-pv-row`)**: Always align place values vertically with explicit column headers (`H`, `T`, `U`, `.`, `t`, `h`).
- **Padded Zeros (`.math-pad-zero`)**: Explicitly pad missing trailing or leading zeros with soft-green dashed boxes (`#dcfce7`) to maintain positional accuracy.
- **Centered Decomposition Slashes (`.math-digit-slashed`)**: Red strike-through lines on cancelled/exchanged digits must pass directly through the centroid of digits (`top: 50%`, `transform: translateY(-50%) rotate(-45deg)`).
- **Visual Unit Bar Models (`.math-bar-model`, `.math-bar-cell`)**: Always use distinct, equal-sized colored blocks for fractions of amounts, reverse fractions, and ratio sharing.
- **BIDMAS Hierarchy & Step-Down Boards (`.math-bidmas-ladder`, `.math-stepdown-board`)**: Use 4-tier color-coded priority badges (Tier 1 B, Tier 2 I, Tier 3 DM, Tier 4 AS). Highlight actively evaluated terms in glowing yellow pills (`.math-target-calc`) connected with downward flow arrows.
- **Stacked Fraction Bars (`.math-stacked-frac`)**: Render compound or algebraic fractions vertically with `.math-stacked-num` and `.math-stacked-den`. Never use non-standard entities like `&frac{...}`.
- **Expansive Master Tables (`.math-master-table`)**: Use high-contrast master tables with 1.35rem fonts and colored headers for directories (e.g. FDP Equivalences, Decimal Places vs. Significant Figures, Remainder Decision Matrix, Directional Estimation).

### C. Re-architected Exam Models & Marking Criteria
- **Multi-Card Architecture (`.exam-model-big-step`)**: Every worked example must be broken into individual step cards with problem stem, visual calculation block, plain-English tutor explanation, and Pearson Edexcel / City & Guilds mark tags (`[M1]`, `[A1]`, `[B1]`).
- **Interactive Practice Scratchpads**: Include auto-saving learner textareas with accredited step-down marking scheme dropdown drawers (`.practice-solution-drawer`).

### D. Automated Quality Assurance Protocols
- **HTML Syntax & Tag Balancing**: Always run an automated Python `html.parser` check verifying `stack remaining == 0` and `errors == 0` before committing.
- **Automated Confidentiality Verification**: Run automated regex searches confirming 0 occurrences of forbidden organisation terms (`oxford health`, `nhs`, `trust`, etc.).
- **Dyslexia Tint Testing**: Ensure all components render cleanly against the site's four dyslexia tints: Cream (`#fdfbf7`), Soft Peach (`#fff7ed`), Cool Mist (`#f0f9ff`), and Soft Sage (`#f0fdf4`).


