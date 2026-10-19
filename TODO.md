# Master Functional Skills (MFS) — Backlog & Improvement Tasks

## 📌 High Priority: Level 1 vs Level 2 Curriculum & Resource Separation

### Background
Currently, the Level 1 and Level 2 Maths revision landing pages share 25 foundational topics and point to the exact same dual-tier worksheets (`worksheets/<topic>-worksheet.html` and `worksheets/<topic>-workout.html`). Learners see identical initial listings and identical shared sheets.

### Target Objectives
1. **Dedicated Worksheets & Fluency Drills**:
   - Split combined worksheets into distinct **Level 1** (core mechanics, single-step operations, foundational scaffolding) and **Level 2** (multi-step problem solving, reverse calculations, contextual exam problems) worksheets.
   - Update topic action bar links on both landing pages so L1 points strictly to L1 worksheets, and L2 points strictly to L2 worksheets.
2. **Visual Level Differentiation**:
   - Introduce distinct color accents / badging for Level 1 vs Level 2 so learners instantly know which tier they are studying.
   - Clarify difficulty indicators on topic rows and practice tests.
3. **Tailored Revision Cards & Video Walkthroughs**:
   - Align explanatory cards and video solutions to the specific Pearson Edexcel mark scheme requirements for each tier (e.g. Level 1 basic units vs Level 2 compound units & comparative data).

---

## 🎨 Scheduled Task: Master Site Uniform Design Language System

### Target Objectives
1. **3–4 Standardized Font Scales**:
   - **Display & Calculations**: `1.25rem` to `1.45rem` (bold 800/900, tabular figures).
   - **Headings & Step Titles**: `1.15rem` to `1.35rem` (bold 800).
   - **Reading / Body / Stems / Explanations**: `1.02rem` to `1.05rem` (line-height 1.6–1.75).
   - **Pills, Badges, Mark Tags & Criteria**: `0.92rem` to `0.95rem` (bold 800, uppercase tracking).
2. **Dedicated Role-Based Color Palette**:
   - **Brand Navy & Blue** (`#0f172a`, `#0284c7`, `#0369a1`): Main structure, primary actions, core working.
   - **Emerald Green** (`#16a34a`, `#15803d`, `#dcfce7`): Final answers, checkmark steps, Level 1 pills.
   - **Amber Gold** (`#f59e0b`, `#d97706`, `#fef3c7`): Golden rules, cautions, Level 2 pills.
   - **Teal / Mark Scheme** (`#0f766e`, `#0d9488`, `#f0fdfa`): Official Pearson Edexcel criteria badges & allocations.
3. **Component Layout Archetypes**:
   - **3-Column Worked Step Grid**: `[Step Pill + Title] | [High-Contrast Calculation Board] | [Teal Criteria Tag]`.
   - **Responsive Master Boards**: 100% full-width grid layouts collapsing gracefully to 1 column on mobile/tablet.
   - **Interactive Practice Drawers**: Uniform layout with scratchpad and collapsible accredited model solutions.
4. **Dyslexia-Friendly & Eye-Catching Visual Standard (Roll-out to all Maths Pages)**:
   - Expand generous visual spacing (`line-height: 1.75`, `padding: 20px–24px`, soft border radii) across all pages.
   - Use high-contrast, dyslexia-friendly pastel containers (soft mint `#f0fdf4`, sky tint `#f0f9ff`, warm amber `#fefce8`) for active calculation blocks.
   - Deploy prominent, intuitive master boards (like Grouped Data and Addition/Subtraction) so complex mathematical operations are instantly clear at a glance.
