# Master Functional Skills (MFS) — Backlog & Improvement Tasks

## ✅ Completed & Live (20 Nov 2026): Interactive Video Comprehension & Concept-Checking Quizzes

> **Status:** **Done & Live** (`assets/data/mfs-video-checks.json`, `assets/js/mfs-video-checks.js`, `assets/css/mfs-video-checks.css`) — deployed across all `161` walkthroughs (`92` Topic/E3/SLC + `69` Mock/Past Papers; `550` total checks), all `245` topic pages, `video-solution.html`, and `mfs-video-modal.js` (`sw.js` `v18`). Zero MP4/VTT edits, `Pause after each question` defaults `OFF`, full Dyslexia Mode & Tint support, `0` Playwright QA failures (`1440×900` & `375×812`).

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

## ✅ Completed & Live (20 Nov 2026): Level 1 vs Level 2 Curriculum & Resource Separation (Sprint 6)

> **Status:** **Done & Live** — Zero shared worksheets (`0` L1 hub/topic links pointing to non-L1 worksheets), Emerald Green (`#16a34a`) Level 1 vs Amber Gold (`#f59e0b` / `#d97706`) Level 2 differentiation across `252` revision topic pages (`92` L1, `111` L2, `49` E3) and all 4 L1/L2 subject hubs, `mfs-video-modal.{css,js}` wired across all 6 hubs, and all `38` Maths L1 Python tuple leaks + `93` wrong Level 2 `.mfs-pill-l1` tags + `64` stale `LEVEL 1 & LEVEL 2` hero pills resolved cleanly.

### Verified Objectives Achieved
1. **Dedicated Worksheets & Fluency Drills**:
   - L1 and L2 topic guides and hubs point strictly to their tier-calibrated worksheets (`worksheets/*-level-1-*.html` vs Level 2 sheets; `0` cross-tier leaks).
2. **Visual Level Differentiation**:
   - Applied Emerald Green `.badge-pill-l1` / `.hero-level-badge-l1` / `.topic-tier-pill.tier-l1` (`#16a34a` / `#dcfce7`) for Level 1 vs Amber Gold `.badge-pill-l2` / `.hero-level-badge-l2` / `.topic-tier-pill.tier-l2` (`#f59e0b` / `#fef3c7`) for Level 2 and Teal `.badge-pill-e3` (`#0d9488`) for Entry Level 3, plus `data-level` hero accent borders.
   - Added row-level Tier pills (`38/38` Maths L1, `44/44` Maths L2, `33/33` English L1, `46/46` English L2) and updated hub curriculum counts (`38` Maths L1, `44` Maths L2, `46` English L2).
3. **100% Maths Visual Board Coverage & Tier-Calibrated Worked Models**:
   - Removed stale `Level 1` footer pills from `26` true Level 2-only Maths pages and fixed all `38` Maths L1 tutor tip tuple leaks (`.mfs-l1-tutor-tip` with verified avatars).

---

## ✅ Completed & Live (20 Nov 2026): Master Site Uniform Design Language System (Sprint 6)

> **Status:** **Done & Live** (`assets/css/mfs-revision.css?v=20261120v10`, `assets/css/mfs-theme.css?v=20261120v10`, `sw.js` `v19`) — Standardized typography tokens, role-based Emerald/Amber/Navy/Teal palette, `100%` visual Maths master board coverage (`41/41` Maths L2, `38/38` Maths L1, `24/24` Maths E3), `107` Maths L1 worked-model step boards (`.mfs-step-calc-board`), and `50` pastel Core Skill cards with full Dyslexia Mode/Tint compatibility and `0` Playwright QA failures (`1440×900` & `375×812`).

### Verified Objectives Achieved
1. **Standardized Font Scales & Role-Based Tokens**:
   - Defined `:root` tokens (`--mfs-fs-calc: 1.28rem`, `--mfs-fs-heading: 1.25rem`, `--mfs-fs-body: 1.04rem`, `--mfs-fs-pill: 0.92rem`), Teal `.mark-scheme-tag` badges (`#0f766e` on `#f0fdfa`), Emerald Level 1 / final-answer chips, and Amber Gold Level 2 / caution accents.
2. **Component Layout & Responsive Master Boards**:
   - Built `42` bespoke high-contrast `.math-visual-card` / `.math-master-table` / `.mfs-pastel-grid` boards (`16` Maths L2 + `26` Maths L1 via `scripts/build_maths_visual_boards.py`), wrapped inside `.math-master-table-wrap` for clean mobile scrolling (`0px` horizontal overflow).
3. **Dyslexia-Friendly & Eye-Catching Visual Standard (100% Maths Rollout)**:
   - Upgraded `107` Maths L1 `.model-step-col-desc` calculation boxes and `50` Core Skill boxes into spacious pastel containers (`#f0fdf4`, `#f0f9ff`, `#fefce8`, `#f0fdfa`) with `tabular-nums`, generous `line-height: 1.85` under `data-dyslexia="true"`, and zero broken internal anchors.
