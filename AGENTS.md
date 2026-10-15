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
