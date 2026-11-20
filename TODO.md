# Master Functional Skills (MFS) — Backlog & Improvement Tasks

## 🧠 Planned Feature (To Come Back To — Nov 2026): Interactive Video Comprehension & Concept-Checking Quizzes

### Core Architecture & UX Rules
- **Clean MP4s (Zero Re-Rendering):** Never burn quizzes into video files. Drive all questions from lightweight JSON paired with existing `.vtt` chapter timestamps.
- **No Hard-Locked Gates:** Never force mid-video pop-ups without a skip/toggle or lock webpage text below a video (respects mobile native fullscreen players, YouTube embeds, learners revising without audio, and learners jumping straight to one mock question).
- **MFS Dark Blue Styling:** Cards must follow the unified `#0a0f1d` / `#0f172a` gradient theme (`#0284c7` accent bar, `#38bdf8` tags) and maintain full Dyslexia Tint compatibility.

### 1. Revision Topic Videos (Short, 3–6 mins)
- **3-Question "60-Second Concept Check" Card** placed directly beneath the video player.
- Focus on process & traps (no heavy calculation): **Q1 Setup** (e.g. padded zeros `15.00`), **Q2 Process/Order** (e.g. BIDMAS priority), **Q3 Sense-Check / Unit**.
- **"Rewatch This Step" Timestamp Jump:** Wrong answers explain *why* and provide a one-click **`▶ Watch [Sonya/Emma/Subi] explain this step (MM:SS)`** button using `.vtt` cue timestamps.

### 2. Mock Paper Model Solution Walkthroughs (20–40 mins)
- **Per-Question Examiner Trap Checks (`CCQs`)** synced to `.vtt` Question Chapters (`Q1`, `Q2`, `Q3`...) directly beneath the player.
- **Optional Interactive Toggle:** `Pause after each question for a quick check [ON / OFF]` — gently pauses at chapter end (never mid-sentence) and highlights the question's Concept Check with a `Continue to next question →` button.
- **4 Core CCQ Archetypes:**
  1. **Unit & Capacity vs. Volume/Area Traps** (e.g. why `m³` vs `litres` vs `m²` matters on the answer line).
  2. **Forgotten Yes/No Decision Sentences** (explicitly stating *Yes/No* AND comparing the two calculated figures).
  3. **Real-World Rounding Direction** (why `4.2` minibuses/tins rounds UP to `5` instead of down to `4`).
  4. **Reverse Calculation Checks** (identifying valid inverse checks).

---

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
