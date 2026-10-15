# Master Functional Skills — A4 "Fill the Page" Design Spec (Draft 3)

All 17 books are printed **A4 portrait (210 × 297 mm)**. Every page must use as much of its
space as possible, like the revision cards: big type, generous spacing, big pictures and diagrams.
**No page may have a large empty area at the bottom.**

## 1. Typography (minimums — never go smaller)
| Element | Size | Notes |
|---|---|---|
| Body text | **13pt** (Lexend / Open Sans), line-height 1.5 | Entry 3 books: **14pt**, line-height 1.6 |
| Box text (rules, tips, traps) | 12.5pt min | |
| Page title (H1) | 26–30pt bold | |
| Section heading (H2) | 18–20pt | |
| Exercise questions | 13pt | |
| Table cells | 12pt min | |
| Running header / footer | 10pt | only exception to the 12pt floor |
| Speech bubbles | 13pt | |

Left-aligned, never justified. Cream page `#FDFBF7`, dark text `#1e293b`. Max ~70 characters per line.

## 2. Page shell
- Page = `210mm × 297mm`, `overflow:hidden`, `page-break-after:always`, padding ~14mm sides, 12mm top/bottom.
- Inside: header (fixed), **body = flex column with `flex:1`**, footer (fixed).
- **Fill rule:** the final block on each page gets `flex:1` so it stretches to the footer. Fill blocks are:
  writing lines, a 5 mm maths grid, a working-out box, a large picture, or a "Notes" panel.
- Content that doesn't fit moves to a new page — **never shrink the font to make it fit.**

## 3. Page types (use these, mix them per book)
1. **Concept page:** title → big hero picture or diagram (35–45% of the page height) → rule box
   → worked example → Golden Rule + Watch Out pair.
2. **Murphy spread (SPaG/grammar):** left = explanation with a cartoon character + speech bubble
   (A/B/C sections); right = numbered exercises with big answer lines filling the page.
3. **Practice page:** 4–6 questions, each with its own working box; the last box fills the page.
4. **Vocabulary/visual dictionary page:** 6–9 picture tiles (photo + word + example sentence) in a grid filling the page.
5. **Exam/mock page:** question at the top, full-height lined paper or a 5 mm grid below.
6. **Answer page:** 2 columns at 12.5pt, fills the page.

## 4. Images
- **Real-life photos:** `assets/img/book_photos/<theme>/` (see `manifest.json`). Use them big:
  a full-width hero (≥ 70 mm tall) or tiles (≥ 55 mm). `object-fit: cover`, 8px rounded corners.
- **Cartoon characters / scenes (Grammar in Use style):** `assets/img/book_cartoons/` (see `manifest.json`).
  Show them at 45–70 mm tall with a speech bubble beside them.
- **Diagrams** (number lines, shapes, charts, letter layouts, screens): inline SVG, at least half the page width,
  labels ≥ 12pt.
- Aim for **at least one large picture or diagram on every teaching page**.

## 5. Covers
Page 1 = front cover (full bleed), page 2 = inside cover, last page = back cover (full bleed).
Existing cover images in `assets/img/books/` stay as they are.

## 6. QA checklist (every book)
- `pdfinfo` → A4 page size, even page count, covers in the right place.
- Render every page at 40 dpi in a contact sheet → **no page with more than ~15% empty space at the bottom**.
- `grep` the builder for font sizes → nothing below 12pt except header/footer.
- Previous version archived as `..._Draft_2.pdf` in `assets/downloads/drafts/` and `~/Documents/MFS_Book_Drafts/`.
