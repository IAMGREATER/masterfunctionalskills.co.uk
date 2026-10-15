import os

PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"
OUTPUT_FILE = os.path.join(PROJECT_DIR, "functional-skills-area.html")

html_code = """<!DOCTYPE html>
<html lang="en-GB" data-theme="sapphire" data-tint="cream">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Area: Formulas, Models & Exam Practice | Master Functional Skills</title>
  <meta name="description" content="Dyslexia-friendly Area revision guide for Functional Skills Maths Level 1 & Level 2. Clear spacing, structured cards, large color-coded diagrams, formulas, worked exam models, and interactive practice.">
  <link rel="icon" type="image/svg+xml" href="assets/img/favicon.svg">
  <link rel="icon" type="image/png" sizes="32x32" href="assets/img/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="192x192" href="assets/img/favicon-192x192.png">
  <link rel="apple-touch-icon" href="assets/img/favicon-192x192.png">
  <link rel="shortcut icon" href="favicon.ico">
  <link rel="stylesheet" href="assets/css/mfs-theme.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
  
  <style>
    /* ==========================================================================
       DYSLEXIA-FRIENDLY & PASS FUNCTIONAL SKILLS STYLE SPACING & PROPORTIONS
       ========================================================================== */

    /* Expansive Screen Layout: Pushes contents far left and gives learning materials expansive space */
    .revision-page-wrapper {
      width: 98%;
      max-width: 1720px;
      margin: 0 auto;
      padding: 0 20px;
      box-sizing: border-box;
    }

    /* Dyslexia-Friendly Typography Defaults */
    body {
      line-height: 1.75;
      color: #1e293b;
      background-color: var(--bg-page);
    }
    p {
      line-height: 1.75;
      margin-top: 0;
      margin-bottom: 20px;
      color: #334155;
      font-size: 1.02rem;
    }

    /* Breadcrumbs Bar */
    .revision-breadcrumb-bar {
      background: var(--bg-card);
      border-bottom: 1px solid var(--border);
      padding: 14px 0;
      font-size: 0.88rem;
    }
    .revision-breadcrumbs {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
      color: var(--text-muted);
    }
    .revision-breadcrumbs a {
      color: var(--text-secondary);
      text-decoration: none;
      transition: color 0.2s;
    }
    .revision-breadcrumbs a:hover {
      color: var(--accent);
    }
    .revision-breadcrumbs i {
      font-size: 0.7rem;
      opacity: 0.6;
    }
    .revision-breadcrumbs span.current {
      color: var(--navy-dark);
      font-weight: 700;
    }

    /* Hero Header */
    .revision-hero-card {
      background: linear-gradient(135deg, var(--navy-dark) 0%, #0d1e3d 100%);
      color: #ffffff;
      padding: 40px 0 44px;
      position: relative;
      overflow: hidden;
      border-bottom: 3px solid var(--accent);
    }
    .revision-hero-pill-row {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      margin-bottom: 16px;
    }
    .badge-pill-accent {
      background: var(--accent);
      color: #ffffff;
      font-size: 0.78rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 4px 14px;
      border-radius: var(--radius-full);
    }
    .badge-pill-gold {
      background: #f59e0b;
      color: #070d1e;
      font-size: 0.78rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 4px 14px;
      border-radius: var(--radius-full);
    }
    .badge-pill-outline {
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid rgba(255, 255, 255, 0.25);
      color: #e2e8f0;
      font-size: 0.78rem;
      font-weight: 600;
      padding: 4px 14px;
      border-radius: var(--radius-full);
    }
    .revision-hero-title {
      font-size: 2.35rem;
      font-weight: 800;
      line-height: 1.25;
      margin: 0 0 14px 0;
      color: #ffffff;
    }
    .revision-hero-title span {
      color: #60a5fa;
    }
    .revision-hero-desc {
      font-size: 1.08rem;
      line-height: 1.7;
      color: #cbd5e1;
      max-width: 900px;
      margin-bottom: 24px;
    }
    .revision-hero-meta-bar {
      display: flex;
      align-items: center;
      gap: 24px;
      flex-wrap: wrap;
      font-size: 0.9rem;
      color: #94a3b8;
      border-top: 1px solid rgba(255, 255, 255, 0.12);
      padding-top: 18px;
    }
    .hero-meta-item {
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }
    .hero-quick-actions {
      display: flex;
      gap: 12px;
      margin-top: 20px;
      flex-wrap: wrap;
    }
    .btn-hero-action {
      background: #10b981;
      color: #ffffff;
      font-weight: 700;
      font-size: 0.92rem;
      padding: 10px 22px;
      border-radius: 8px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
    }
    .btn-hero-action:hover {
      background: #059669;
      transform: translateY(-1px);
    }
    .btn-hero-action-secondary {
      background: rgba(255,255,255,0.12);
      color: #ffffff;
      font-weight: 600;
      font-size: 0.92rem;
      padding: 10px 20px;
      border-radius: 8px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      border: 1px solid rgba(255,255,255,0.25);
      transition: all 0.2s;
    }
    .btn-hero-action-secondary:hover {
      background: rgba(255,255,255,0.2);
    }

    /* Main 2-Column Revision Layout */
    .revision-layout {
      display: grid;
      grid-template-columns: 210px minmax(0, 1fr);
      gap: 36px;
      padding: 34px 0 60px;
      align-items: start;
    }
    @media (max-width: 1024px) {
      .revision-layout {
        grid-template-columns: 1fr;
      }
      .revision-sidebar {
        display: none;
      }
    }

    /* Left Sticky Sidebar / Table of Contents */
    .revision-sidebar {
      position: sticky;
      top: 90px;
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 18px 14px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }
    .sidebar-toc-title {
      font-size: 0.88rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--navy-dark);
      padding-bottom: 12px;
      margin-bottom: 12px;
      border-bottom: 2px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .sidebar-toc-list {
      list-style: none;
      padding: 0;
      margin: 0;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }
    .sidebar-toc-link {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 8px 12px;
      border-radius: 6px;
      color: #475569;
      font-size: 0.88rem;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.2s ease;
      border-left: 3px solid transparent;
    }
    .sidebar-toc-link:hover {
      color: var(--accent);
      background: #f0fdf4;
    }
    .sidebar-toc-link.active {
      color: #065f46;
      background: #ecfdf5;
      border-left-color: #10b981;
      font-weight: 700;
    }

    /* Mobile Quick Nav Bar */
    .mobile-toc-bar {
      display: none;
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      padding: 12px 20px;
      position: sticky;
      top: 65px;
      z-index: 40;
      align-items: center;
      justify-content: space-between;
    }
    @media (max-width: 1024px) {
      .mobile-toc-bar {
        display: flex;
      }
    }
    .btn-mobile-toc {
      background: var(--navy-dark);
      color: #ffffff;
      border: none;
      padding: 8px 16px;
      border-radius: 6px;
      font-weight: 600;
      font-size: 0.85rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }

    /* Main Educational Content Area */
    .revision-content {
      min-width: 0;
    }

    /* Content Section Blocks */
    .revision-section {
      margin-bottom: 46px;
      scroll-margin-top: 100px;
    }
    .section-header-row {
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 16px;
      border-bottom: 2px solid var(--border);
      padding-bottom: 12px;
    }
    .section-title {
      font-size: 1.7rem;
      font-weight: 800;
      color: var(--navy-dark);
      margin: 0;
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .section-lead-text {
      font-size: 1.08rem;
      color: #334155;
      line-height: 1.7;
      margin-bottom: 24px;
    }

    /* ==========================================================================
       PASS FUNCTIONAL SKILLS REVISION CARD DESIGN SYSTEM
       ========================================================================== */
    .pfs-card {
      background: #ffffff;
      border: 2px solid #00a8ff;
      border-radius: 8px;
      padding: 28px 32px;
      margin-bottom: 30px;
      box-shadow: 0 1px 4px rgba(0, 168, 255, 0.05);
      position: relative;
    }
    @media (max-width: 640px) {
      .pfs-card {
        padding: 20px 18px;
      }
    }
    .pfs-card-head {
      margin-bottom: 14px;
    }
    .pfs-card-title {
      font-size: 1.45rem;
      font-weight: 800;
      color: #1e293b;
      margin: 0 0 8px 0;
      display: flex;
      align-items: baseline;
      gap: 8px;
      flex-wrap: wrap;
    }
    .pfs-card-title .pfs-prefix {
      color: #00a8ff;
      font-weight: 800;
    }
    .pfs-card-stem {
      font-size: 1.08rem;
      color: #334155;
      margin: 0;
      line-height: 1.65;
    }

    /* Proportional 2-Column Content Split Inside Card */
    .pfs-card-body {
      display: grid;
      grid-template-columns: 1fr 340px;
      gap: 36px;
      align-items: center;
      margin: 20px 0 24px;
    }
    @media (max-width: 990px) {
      .pfs-card-body {
        grid-template-columns: 1fr;
        gap: 22px;
      }
    }

    .pfs-math-col {
      display: flex;
      flex-direction: column;
    }
    .pfs-marks-row {
      display: flex;
      justify-content: flex-end;
      color: #475569;
      font-weight: 700;
      font-size: 0.95rem;
      margin-bottom: 10px;
    }
    .pfs-formula-display {
      font-size: 1.25rem;
      font-weight: 700;
      color: #0f172a;
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-left: 4px solid #00a8ff;
      padding: 16px 20px;
      border-radius: 6px;
      margin-bottom: 16px;
      line-height: 1.5;
    }
    .pfs-steps-box {
      background: #ffffff;
      border: 1px solid #f1f5f9;
      border-radius: 6px;
      padding: 14px 18px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .pfs-step-row {
      display: flex;
      align-items: baseline;
      gap: 12px;
      font-size: 0.98rem;
      color: #334155;
      line-height: 1.6;
    }
    .pfs-step-tag {
      font-weight: 800;
      color: #00a8ff;
      font-size: 0.88rem;
      min-width: 52px;
      flex-shrink: 0;
    }
    .pfs-answer-banner {
      margin-top: 14px;
      background: #f0fdf4;
      border: 1px solid #86efac;
      border-radius: 6px;
      padding: 10px 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      color: #065f46;
      font-weight: 700;
      font-size: 1.02rem;
    }

    /* Proportional SVG Diagram Column */
    .pfs-diagram-col {
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .pfs-diagram-col svg {
      width: 100%;
      max-width: 340px;
      height: auto;
      display: block;
    }

    /* Footer Level & Board Pills */
    .pfs-card-footer {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
      padding-top: 16px;
      border-top: 1px solid #f1f5f9;
    }
    .pfs-pill-l1 {
      background: #16a34a;
      color: #ffffff;
      font-size: 0.76rem;
      font-weight: 800;
      padding: 3px 10px;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.03em;
    }
    .pfs-pill-l2 {
      background: #ea580c;
      color: #ffffff;
      font-size: 0.76rem;
      font-weight: 800;
      padding: 3px 10px;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.03em;
    }
    .pfs-pill-board {
      background: #f1f5f9;
      color: #475569;
      border: 1px solid #cbd5e1;
      font-size: 0.76rem;
      font-weight: 600;
      padding: 3px 10px;
      border-radius: 4px;
    }

    /* Golden Rules (Amber/Gold Dyslexia-Friendly Cards) */
    .rule-card-amber {
      background: #fffbeb;
      border: 1px solid #fde68a;
      border-left: 5px solid #f59e0b;
      border-radius: 12px;
      padding: 22px 26px;
      margin-bottom: 20px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }
    .rule-card-amber-header {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 1.15rem;
      font-weight: 800;
      color: #92400e;
      margin-bottom: 10px;
    }
    .rule-highlight-badge {
      display: inline-block;
      background: #fef3c7;
      border: 1px solid #fde68a;
      padding: 4px 12px;
      border-radius: 6px;
      font-weight: 700;
      color: #b45309;
      font-size: 0.92rem;
      margin-top: 8px;
    }

    /* Worked Exam Models */
    .worked-exam-model-card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-top: 4px solid var(--accent);
      border-radius: 12px;
      padding: 28px 32px;
      margin-bottom: 26px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }
    .model-header-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
      margin-bottom: 14px;
    }
    .badge-worked-model {
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      color: #1e40af;
      font-size: 0.85rem;
      font-weight: 800;
      padding: 4px 12px;
      border-radius: var(--radius-full);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .model-marks-pill {
      background: #ecfdf5;
      border: 1px solid #a7f3d0;
      color: #065f46;
      font-size: 0.85rem;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: var(--radius-full);
    }
    .model-question-stem {
      font-size: 1.08rem;
      line-height: 1.7;
      color: var(--navy-dark);
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 16px 20px;
      margin-bottom: 20px;
    }
    .model-steps-list {
      display: flex;
      flex-direction: column;
      gap: 14px;
      margin-bottom: 20px;
    }
    .model-step-row {
      display: flex;
      gap: 16px;
      align-items: flex-start;
    }
    .step-number-bubble {
      background: var(--navy-dark);
      color: #ffffff;
      font-size: 0.8rem;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 6px;
      flex-shrink: 0;
      line-height: 1.4;
    }
    .step-detail-body {
      flex: 1;
    }
    .step-detail-title {
      font-weight: 700;
      color: var(--navy-dark);
      margin-bottom: 4px;
      font-size: 1rem;
    }
    .step-math-line {
      font-family: inherit;
      color: #047857;
      font-weight: 700;
      margin: 4px 0;
      font-size: 1.02rem;
    }
    .mark-scheme-tag {
      display: inline-block;
      background: #f0fdf4;
      border: 1px solid #86efac;
      color: #166534;
      font-size: 0.78rem;
      font-weight: 800;
      padding: 2px 8px;
      border-radius: 4px;
      margin-top: 4px;
    }
    .model-final-answer-callout {
      background: linear-gradient(135deg, #065f46 0%, #047857 100%);
      color: #ffffff;
      padding: 16px 22px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 10px;
    }
    .model-final-text {
      font-size: 1.15rem;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    /* Examiner Traps */
    .trap-card-coral {
      background: #fff1f2;
      border: 1px solid #fecdd3;
      border-left: 5px solid #f43f5e;
      border-radius: 12px;
      padding: 20px 24px;
      margin-bottom: 18px;
    }
    .trap-card-coral-header {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 1.12rem;
      font-weight: 800;
      color: #9f1239;
      margin-bottom: 8px;
    }
    .trap-solution-badge {
      display: inline-block;
      background: #ffffff;
      border: 1px solid #fecdd3;
      padding: 6px 14px;
      border-radius: 6px;
      color: #881337;
      font-size: 0.92rem;
      margin-top: 8px;
    }

    /* Practice Tasks */
    .practice-q-card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 26px 30px;
      margin-bottom: 24px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.02);
    }
    .practice-q-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
      flex-wrap: wrap;
      gap: 10px;
    }
    .practice-q-num {
      font-size: 1.12rem;
      font-weight: 800;
      color: var(--navy-dark);
    }
    .practice-q-marks {
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--accent);
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      padding: 3px 10px;
      border-radius: var(--radius-full);
    }
    .practice-q-stem {
      font-size: 1.05rem;
      line-height: 1.7;
      color: #1e293b;
      margin-bottom: 18px;
    }
    .working-scratchpad-area {
      margin-bottom: 18px;
    }
    .working-scratchpad-label {
      display: block;
      font-size: 0.85rem;
      font-weight: 700;
      color: #64748b;
      margin-bottom: 6px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .working-scratchpad-input {
      width: 100%;
      min-height: 80px;
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      padding: 12px 16px;
      font-family: inherit;
      font-size: 0.98rem;
      line-height: 1.6;
      color: #1e293b;
      box-sizing: border-box;
      resize: vertical;
    }
    .working-scratchpad-input:focus {
      outline: none;
      border-color: var(--accent);
      background: #ffffff;
      box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15);
    }
    .btn-reveal-solution {
      background: #ffffff;
      border: 2px solid var(--accent);
      color: var(--accent);
      font-weight: 700;
      font-size: 0.92rem;
      padding: 8px 18px;
      border-radius: 6px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
    }
    .btn-reveal-solution:hover {
      background: var(--accent);
      color: #ffffff;
    }
    .solution-drawer {
      display: none;
      margin-top: 18px;
      background: #f0fdf4;
      border: 1px solid #86efac;
      border-radius: 8px;
      padding: 18px 22px;
    }
    .solution-drawer.open {
      display: block;
    }
    .solution-drawer-title {
      font-size: 1rem;
      font-weight: 800;
      color: #166534;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    /* Specification Quick Reference Table */
    .spec-table-box {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 12px;
      overflow: hidden;
      margin-bottom: 24px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }
    .spec-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
    }
    .spec-table th {
      background: #f8fafc;
      color: var(--navy-dark);
      font-weight: 700;
      font-size: 0.88rem;
      padding: 14px 18px;
      border-bottom: 1px solid var(--border);
    }
    .spec-table td {
      padding: 14px 18px;
      font-size: 0.95rem;
      color: #334155;
      border-bottom: 1px solid #f1f5f9;
    }
    .spec-table tr:last-child td {
      border-bottom: none;
    }

    /* Curriculum Progression Banner */
    .progression-banner {
      background: linear-gradient(135deg, var(--navy-dark) 0%, #0d1e3d 100%);
      color: #ffffff;
      border-radius: 14px;
      padding: 34px 40px;
      margin-top: 40px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 24px;
    }
    .progression-text-area {
      max-width: 600px;
    }
    .progression-title {
      font-size: 1.45rem;
      font-weight: 800;
      margin: 0 0 8px 0;
      color: #ffffff;
    }
    .progression-links-group {
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
    }
    .btn-progression-nav {
      background: rgba(255,255,255,0.12);
      border: 1px solid rgba(255,255,255,0.25);
      color: #ffffff;
      font-weight: 700;
      font-size: 0.9rem;
      padding: 10px 18px;
      border-radius: 8px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
    }
    .btn-progression-nav:hover {
      background: #10b981;
      border-color: #10b981;
    }
  </style>
</head>
<body>

  <!-- ============================================== -->
  <!-- TOP GLOBAL NAVIGATION NAVBAR -->
  <!-- ============================================== -->
  <header class="site-header">
    <div class="header-container">
      <div class="logo">
        <a href="index.html" class="logo-link">
          <svg class="logo-icon" viewBox="0 0 40 40" width="34" height="34">
            <defs>
              <linearGradient id="mfsNavGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#1e3a8a"/>
                <stop offset="100%" stop-color="#2563eb"/>
              </linearGradient>
            </defs>
            <rect width="40" height="40" rx="10" fill="url(#mfsNavGrad)"/>
            <path d="M 8 30 L 15 12 L 20 22 L 25 12 L 32 30" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
            <polygon points="20,7 24,10 20,13 16,10" fill="#f59e0b"/>
          </svg>
          <span class="logo-text">Master <span>Functional Skills</span></span>
        </a>
      </div>
      <nav class="main-nav" id="mainNav">
        <a href="index.html" class="nav-link">Home</a>
        <a href="functional-skills-maths-level-2.html" class="nav-link active">Maths</a>
        <a href="functional-skills-english-level-2.html" class="nav-link">English</a>
        <a href="functional-skills-ict-level-2.html" class="nav-link">ICT &amp; Digital</a>
        <a href="shop.html" class="nav-link">Shop</a>
        <a href="contact.html" class="nav-link">Contact</a>
      </nav>
      <div class="header-actions">
        <!-- Dyslexia Overlay & Tint Controller -->
        <div class="tint-dropdown">
          <button type="button" class="btn-tint-toggle" onclick="cycleTint()" title="Dyslexia Background Tint">
            <i class="fa-solid fa-palette"></i> <span class="hide-mobile">Page Tint</span>
          </button>
        </div>
        <a href="shop.html" class="btn-header-cart" title="Shopping Cart">
          <i class="fa-solid fa-cart-shopping"></i>
          <span class="cart-badge-count">0</span>
        </a>
      </div>
    </div>
  </header>

  <!-- ============================================== -->
  <!-- BREADCRUMBS BAR -->
  <!-- ============================================== -->
  <div class="revision-breadcrumb-bar">
    <div class="revision-page-wrapper">
      <div class="revision-breadcrumbs">
        <a href="index.html"><i class="fa-solid fa-house"></i> Home</a>
        <i class="fa-solid fa-chevron-right"></i>
        <a href="functional-skills-maths-level-2.html">Maths Level 1 &amp; Level 2</a>
        <i class="fa-solid fa-chevron-right"></i>
        <a href="functional-skills-maths-level-2.html#measures">Measures, Shape &amp; Space</a>
        <i class="fa-solid fa-chevron-right"></i>
        <span class="current">Area</span>
      </div>
    </div>
  </div>

  <!-- ============================================== -->
  <!-- HERO HEADER (CLEAN & DIRECT TITLE) -->
  <!-- ============================================== -->
  <section class="revision-hero-card">
    <div class="revision-page-wrapper">
      <div class="revision-hero-pill-row">
        <span class="badge-pill-accent"><i class="fa-solid fa-award"></i> Pearson Edexcel &bull; City &amp; Guilds</span>
        <span class="badge-pill-gold"><i class="fa-solid fa-check-double"></i> Level 1 &amp; Level 2 Curriculum</span>
        <span class="badge-pill-outline"><i class="fa-solid fa-clock"></i> 25 Min Revision</span>
      </div>

      <h1 class="revision-hero-title">
        Area: Formulas, Models &amp; Exam Practice
      </h1>
      <p class="revision-hero-desc">
        Master every Functional Skills area question with clear spacing, color-coded proportional diagrams, step-by-step worked formulas, examiner traps, and real-world NHS/vocational models.
      </p>

      <div class="revision-hero-meta-bar">
        <div class="hero-meta-item">
          <i class="fa-solid fa-calculator" style="color:#60a5fa;"></i> <strong>Calculator &amp; Non-Calc Papers</strong>
        </div>
        <div class="hero-meta-item">
          <i class="fa-solid fa-book-open" style="color:#34d399;"></i> <strong>Curriculum Standards:</strong> Pearson L1 (18-19) &bull; L2 (19-20)
        </div>
        <div class="hero-meta-item">
          <i class="fa-solid fa-circle-check" style="color:#fbbf24;"></i> <strong>6 Core Shape Examples + 4 Exam Models</strong>
        </div>
      </div>

      <div class="hero-quick-actions">
        <a href="#core-examples" class="btn-hero-action">
          <i class="fa-solid fa-shapes"></i> View Shape Examples
        </a>
        <a href="#practice-questions" class="btn-hero-action-secondary">
          <i class="fa-solid fa-pencil"></i> Start Exam Practice
        </a>
      </div>
    </div>
  </section>

  <!-- MOBILE TABLE OF CONTENTS BAR -->
  <div class="mobile-toc-bar">
    <div style="font-weight:700; color:var(--navy-dark); font-size:0.9rem;">
      <i class="fa-solid fa-list-check" style="color:var(--accent);"></i> Area Revision Blueprint
    </div>
    <button type="button" class="btn-mobile-toc" onclick="toggleMobileToc()">
      <span>Contents</span> <i class="fa-solid fa-bars"></i>
    </button>
  </div>

  <!-- ============================================== -->
  <!-- MAIN EXPANSIVE 2-COLUMN LAYOUT -->
  <!-- ============================================== -->
  <main class="revision-page-wrapper">
    <div class="revision-layout">

      <!-- ============================================== -->
      <!-- LEFT COLUMN: STICKY BLUEPRINT / TABLE OF CONTENTS -->
      <!-- ============================================== -->
      <aside class="revision-sidebar" id="sidebarNav">
        <div class="sidebar-toc-title">
          <span><i class="fa-solid fa-compass-drafting" style="color:var(--accent);"></i> Topic Contents</span>
          <span style="font-size:0.75rem; color:#64748b; font-weight:700;">7 Sections</span>
        </div>

        <ul class="sidebar-toc-list" id="tocList">
          <li>
            <a href="#specification" class="sidebar-toc-link active">
              <i class="fa-solid fa-clipboard-check"></i> Specification
            </a>
          </li>
          <li>
            <a href="#golden-rules" class="sidebar-toc-link">
              <i class="fa-solid fa-lightbulb"></i> Golden Rules
            </a>
          </li>
          <li>
            <a href="#core-examples" class="sidebar-toc-link">
              <i class="fa-solid fa-shapes"></i> Core Examples
            </a>
          </li>
          <li>
            <a href="#worked-models" class="sidebar-toc-link">
              <i class="fa-solid fa-file-signature"></i> Worked Exam Models
            </a>
          </li>
          <li>
            <a href="#examiner-traps" class="sidebar-toc-link">
              <i class="fa-solid fa-triangle-exclamation"></i> Examiner Traps
            </a>
          </li>
          <li>
            <a href="#practice-questions" class="sidebar-toc-link">
              <i class="fa-solid fa-pencil"></i> Exam Practice
            </a>
          </li>
          <li>
            <a href="#curriculum-links" class="sidebar-toc-link">
              <i class="fa-solid fa-arrow-right"></i> Next Topics
            </a>
          </li>
        </ul>
      </aside>

      <!-- ============================================== -->
      <!-- RIGHT COLUMN: MAIN EDUCATIONAL REVISION CONTENT -->
      <!-- ============================================== -->
      <div class="revision-content">

        <!-- 1. OFQUAL SPECIFICATION & FORMULA SUMMARY TABLE -->
        <section id="specification" class="revision-section">
          <div class="section-header-row">
            <h2 class="section-title"><i class="fa-solid fa-clipboard-check"></i> Curriculum Specification &amp; Formula Guide</h2>
            <span style="font-size:0.88rem; font-weight:700; color:#059669;"><i class="fa-solid fa-check"></i> Level 1 &amp; Level 2 Criteria</span>
          </div>
          <p class="section-lead-text">
            Area measures the <strong>two-dimensional surface inside a boundary</strong>, always recorded in square units (<strong>mm&sup2;</strong>, <strong>cm&sup2;</strong>, <strong>m&sup2;</strong>, or <strong>km&sup2;</strong>).
          </p>

          <div class="spec-table-box">
            <table class="spec-table">
              <thead>
                <tr>
                  <th>Shape</th>
                  <th>Formula</th>
                  <th>Key Dimension Check</th>
                  <th>Exam Level</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Rectangle / Square</strong></td>
                  <td><code>Area = Length &times; Width</code></td>
                  <td>Multiply adjacent perpendicular sides</td>
                  <td><span class="pfs-pill-l1">Level 1</span> <span class="pfs-pill-l2">Level 2</span></td>
                </tr>
                <tr>
                  <td><strong>Parallelogram</strong></td>
                  <td><code>Area = Base &times; Perpendicular Height</code></td>
                  <td>Never use the slanted side</td>
                  <td><span class="pfs-pill-l2">Level 2</span></td>
                </tr>
                <tr>
                  <td><strong>Triangle</strong></td>
                  <td><code>Area = (Base &times; Height) &divide; 2</code></td>
                  <td>Always remember to divide by 2</td>
                  <td><span class="pfs-pill-l1">Level 1</span> <span class="pfs-pill-l2">Level 2</span></td>
                </tr>
                <tr>
                  <td><strong>Trapezium</strong></td>
                  <td><code>Area = ((a + b) &divide; 2) &times; Height</code></td>
                  <td>Find mean of parallel sides first</td>
                  <td><span class="pfs-pill-l2">Level 2</span></td>
                </tr>
                <tr>
                  <td><strong>Compound Shapes</strong></td>
                  <td><code>Total Area = Area A + Area B</code></td>
                  <td>Split with a clean dotted line</td>
                  <td><span class="pfs-pill-l1">Level 1</span> <span class="pfs-pill-l2">Level 2</span></td>
                </tr>
                <tr>
                  <td><strong>Circle</strong></td>
                  <td><code>Area = &pi; &times; Radius&sup2;</code></td>
                  <td>Halve the diameter if diameter is given</td>
                  <td><span class="pfs-pill-l2">Level 2</span></td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <!-- 2. DYSLEXIA-FRIENDLY GOLDEN RULES -->
        <section id="golden-rules" class="revision-section">
          <div class="section-header-row">
            <h2 class="section-title"><i class="fa-solid fa-lightbulb"></i> Golden Rules &amp; Mental Checklists</h2>
          </div>
          <p class="section-lead-text">
            Keep these four rules in mind to avoid the most common calculation mistakes in exam papers.
          </p>

          <!-- Golden Rule 1 -->
          <div class="rule-card-amber">
            <div class="rule-card-amber-header">
              <i class="fa-solid fa-ruler-combined"></i>
              <span>Golden Rule 1: Never Confuse Perimeter and Area</span>
            </div>
            <p>
              <strong>Perimeter</strong> is the <em>one-dimensional distance</em> around the boundary (measured in <strong>cm</strong>, <strong>m</strong>). <br>
              <strong>Area</strong> is the <em>flat two-dimensional surface</em> inside (always measured in <strong>square units</strong>: <strong>cm&sup2;</strong>, <strong>m&sup2;</strong>).
            </p>
            <div class="rule-highlight-badge">
              Always state area answers with a square exponent: cm&sup2; or m&sup2;
            </div>
          </div>

          <!-- Golden Rule 2 -->
          <div class="rule-card-amber">
            <div class="rule-card-amber-header">
              <i class="fa-solid fa-arrows-split-up-and-left"></i>
              <span>Golden Rule 2: Convert All Dimensions to the SAME Unit First</span>
            </div>
            <p>
              Examiners deliberately mix units (e.g. length = <strong>4.2 m</strong>, width = <strong>70 cm</strong>). You must convert both to metres (<strong>70 cm = 0.7 m</strong>) <em>before</em> multiplying. Multiplying 4.2 &times; 70 gives 294 m&sup2;, which is completely wrong!
            </p>
            <div class="rule-highlight-badge">
              Check: 1 m = 100 cm &bull; 70 cm &divide; 100 = 0.7 m &bull; 4.2 &times; 0.7 = 2.94 m&sup2;
            </div>
          </div>

          <!-- Golden Rule 3 -->
          <div class="rule-card-amber">
            <div class="rule-card-amber-header">
              <i class="fa-solid fa-triangle-exclamation"></i>
              <span>Golden Rule 3: Use Perpendicular Height (Never the Slant)</span>
            </div>
            <p>
              For triangles and parallelograms, the height must form a strict 90&deg; right angle with the base. Never use the slanted edge!
            </p>
            <div class="rule-highlight-badge">
              Triangle Area = (Base &times; Vertical Height) &divide; 2
            </div>
          </div>

          <!-- Golden Rule 4 -->
          <div class="rule-card-amber">
            <div class="rule-card-amber-header">
              <i class="fa-solid fa-draw-polygon"></i>
              <span>Golden Rule 4: Average the Parallel Sides First for Trapeziums</span>
            </div>
            <p>
              Add the two parallel boundary sides (a and b), divide by 2 to find their average, then multiply by the vertical separation (h) between them.
            </p>
            <div class="rule-highlight-badge">
              Trapezium Area = ((a + b) &divide; 2) &times; Height
            </div>
          </div>
        </section>

        <!-- ==========================================================================
             3. CORE EXAMPLES (PASS FUNCTIONAL SKILLS STYLE CARDS - OUR OWN UNIQUE VALUES)
             ========================================================================== -->
        <section id="core-examples" class="revision-section">
          <div class="section-header-row">
            <h2 class="section-title"><i class="fa-solid fa-shapes"></i> Core Shape Examples &amp; Step-by-Step Models</h2>
            <span style="font-size:0.88rem; font-weight:700; color:#00a8ff;"><i class="fa-solid fa-layer-group"></i> Proportional Visual Guides</span>
          </div>
          <p class="section-lead-text">
            Each example below features our distinct practical numbers, clean formulas, and proportional color-coded diagrams designed for quick understanding.
          </p>

          <!-- ============================================== -->
          <!-- EXAMPLE 1: AREA OF A RECTANGLE -->
          <!-- ============================================== -->
          <div class="pfs-card" id="example-1">
            <div class="pfs-card-head">
              <h3 class="pfs-card-title">
                <span class="pfs-prefix">Example 1:</span> Area of a Rectangle
              </h3>
              <p class="pfs-card-stem">
                Calculate the area of the rectangle shown to the right.
              </p>
            </div>

            <div class="pfs-card-body">
              <!-- Left Column: Formula & Steps -->
              <div class="pfs-math-col">
                <div class="pfs-marks-row">[2 marks]</div>
                <div class="pfs-formula-display">
                  Area of rectangle = 14 &times; 6 = 84 m&sup2;
                </div>
                <div class="pfs-steps-box">
                  <div class="pfs-step-row">
                    <span class="pfs-step-tag">Step 1:</span>
                    <span>Identify dimensions: Length = <strong>14 m</strong>, Width = <strong>6 m</strong>.</span>
                  </div>
                  <div class="pfs-step-row">
                    <span class="pfs-step-tag">Step 2:</span>
                    <span>Multiply length by width: <strong>14 &times; 6 = 84</strong>.</span>
                  </div>
                  <div class="pfs-step-row">
                    <span class="pfs-step-tag">Step 3:</span>
                    <span>Write the correct square units: <strong>m&sup2;</strong>.</span>
                  </div>
                </div>
                <div class="pfs-answer-banner">
                  <span><i class="fa-solid fa-circle-check"></i> Final Answer: 84 m&sup2;</span>
                  <span style="font-size:0.86rem;">Full 2 Marks</span>
                </div>
              </div>

              <!-- Right Column: Proportional Shape Diagram -->
              <div class="pfs-diagram-col">
                <svg viewBox="0 0 340 190">
                  <defs>
                    <marker id="arrowDark" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
                      <polygon points="0 0, 6 3, 0 6" fill="#0f172a" />
                    </marker>
                    <marker id="arrowDarkRev" markerWidth="6" markerHeight="6" refX="1" refY="3" orient="auto">
                      <polygon points="6 0, 0 3, 6 6" fill="#0f172a" />
                    </marker>
                  </defs>

                  <!-- Solid Warm Terracotta/Orange Fill Rectangle -->
                  <rect x="35" y="30" width="240" height="110" rx="4" fill="#ea580c" stroke="#c2410c" stroke-width="2"/>

                  <!-- Bottom Base Dimension Arrow & Label -->
                  <line x1="35" y1="160" x2="275" y2="160" stroke="#0f172a" stroke-width="2" marker-start="url(#arrowDarkRev)" marker-end="url(#arrowDark)"/>
                  <text x="155" y="180" font-family="system-ui, sans-serif" font-size="18" font-weight="800" fill="#0f172a" text-anchor="middle">14 m</text>

                  <!-- Right Height Dimension Arrow & Label -->
                  <line x1="295" y1="30" x2="295" y2="140" stroke="#0f172a" stroke-width="2" marker-start="url(#arrowDarkRev)" marker-end="url(#arrowDark)"/>
                  <text x="325" y="92" font-family="system-ui, sans-serif" font-size="18" font-weight="800" fill="#0f172a" text-anchor="middle">6 m</text>
                </svg>
              </div>
            </div>

            <!-- Footer Pills -->
            <div class="pfs-card-footer">
              <span class="pfs-pill-l1">FS Level 1</span>
              <span class="pfs-pill-l2">FS Level 2</span>
              <span class="pfs-pill-board">Edexcel</span>
              <span class="pfs-pill-board">City &amp; Guilds</span>
              <span class="pfs-pill-board">NCFE</span>
              <span class="pfs-pill-board">Open Awards</span>
              <span class="pfs-pill-board">Highfield</span>
            </div>
          </div>

          <!-- ============================================== -->
          <!-- EXAMPLE 2: AREA OF A PARALLELOGRAM -->
          <!-- ============================================== -->
          <div class="pfs-card" id="example-2">
            <div class="pfs-card-head">
              <h3 class="pfs-card-title">
                <span class="pfs-prefix">Example 2:</span> Area of a Parallelogram
              </h3>
              <p class="pfs-card-stem">
                Calculate the area of the parallelogram shown to the right.
              </p>
            </div>

            <div class="pfs-card-body">
              <!-- Left Column: Formula & Steps -->
              <div class="pfs-math-col">
                <div class="pfs-marks-row">[2 marks]</div>
                <div class="pfs-formula-display">
                  Area of parallelogram = 11 &times; 6 = 66 cm&sup2;
                </div>
                <div class="pfs-steps-box">
                  <div class="pfs-step-row">
                    <span class="pfs-step-tag">Step 1:</span>
                    <span>Identify base = <strong>11 cm</strong> and perpendicular vertical height = <strong>6 cm</strong>.</span>
                  </div>
                  <div class="pfs-step-row">
                    <span class="pfs-step-tag">Trap Check:</span>
                    <span style="color:#b91c1c; font-weight:600;">Ignore the 8 cm slanted side &mdash; slant heights are never used for area!</span>
                  </div>
                  <div class="pfs-step-row">
                    <span class="pfs-step-tag">Step 2:</span>
                    <span>Multiply: <strong>11 &times; 6 = 66 cm&sup2;</strong>.</span>
                  </div>
                </div>
                <div class="pfs-answer-banner">
                  <span><i class="fa-solid fa-circle-check"></i> Final Answer: 66 cm&sup2;</span>
                  <span style="font-size:0.86rem;">Full 2 Marks</span>
                </div>
              </div>

              <!-- Right Column: Proportional Shape Diagram -->
              <div class="pfs-diagram-col">
                <svg viewBox="0 0 340 190">
                  <defs>
                    <marker id="arrowP" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
                      <polygon points="0 0, 6 3, 0 6" fill="#0f172a" />
                    </marker>
                    <marker id="arrowPRev" markerWidth="6" markerHeight="6" refX="1" refY="3" orient="auto">
                      <polygon points="6 0, 0 3, 6 6" fill="#0f172a" />
                    </marker>
                  </defs>

                  <!-- Solid Sky Blue Parallelogram -->
                  <polygon points="70,35 290,35 240,140 20,140" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>

                  <!-- Perpendicular Dashed Height Line Inside -->
                  <line x1="120" y1="35" x2="120" y2="140" stroke="#0f172a" stroke-width="2" stroke-dasharray="5,4"/>
                  <!-- Right Angle Square -->
                  <rect x="120" y="125" width="14" height="15" fill="none" stroke="#0f172a" stroke-width="1.8"/>
                  <text x="142" y="92" font-family="system-ui, sans-serif" font-size="17" font-weight="800" fill="#ffffff">6 cm</text>

                  <!-- Bottom Base Dimension Arrow & Label -->
                  <line x1="20" y1="162" x2="240" y2="162" stroke="#0f172a" stroke-width="2" marker-start="url(#arrowPRev)" marker-end="url(#arrowP)"/>
                  <text x="130" y="182" font-family="system-ui, sans-serif" font-size="18" font-weight="800" fill="#0f172a" text-anchor="middle">11 cm</text>

                  <!-- Slanted Side Distractor Label -->
                  <text x="28" y="80" font-family="system-ui, sans-serif" font-size="15" font-weight="800" fill="#ffffff">8 cm</text>
                </svg>
              </div>
            </div>

            <!-- Footer Pills -->
            <div class="pfs-card-footer">
              <span class="pfs-pill-l2">FS Level 2</span>
              <span class="pfs-pill-board">Edexcel</span>
              <span class="pfs-pill-board">City &amp; Guilds</span>
              <span class="pfs-pill-board">NCFE</span>
              <span class="pfs-pill-board">Open Awards</span>
              <span class="pfs-pill-board">Highfield</span>
            </div>
          </div>

          <!-- ============================================== -->
          <!-- EXAMPLE 3: AREA OF A TRIANGLE -->
          <!-- ============================================== -->
          <div class="pfs-card" id="example-3">
            <div class="pfs-card-head">
              <h3 class="pfs-card-title">
                <span class="pfs-prefix">Example 3:</span> Area of a Triangle
              </h3>
              <p class="pfs-card-stem">
                Calculate the area of the triangle shown to the right.
              </p>
            </div>

            <div class="pfs-card-body">
              <!-- Left Column: Formula & Steps -->
              <div class="pfs-math-col">
                <div class="pfs-marks-row">[2 marks]</div>
                <div class="pfs-formula-display">
                  Area of triangle = &frac12; &times; 14 &times; 7 = 49 cm&sup2;
                </div>
                <div class="pfs-steps-box">
                  <div class="pfs-step-row">
                    <span class="pfs-step-tag">Step 1:</span>
                    <span>Multiply base by perpendicular vertical height: <strong>14 &times; 7 = 98</strong>.</span>
                  </div>
                  <div class="pfs-step-row">
                    <span class="pfs-step-tag">Step 2:</span>
                    <span>Divide by 2: <strong>98 &divide; 2 = 49</strong>.</span>
                  </div>
                  <div class="pfs-step-row">
                    <span class="pfs-step-tag">Step 3:</span>
                    <span>State the correct metric square units: <strong>49 cm&sup2;</strong>.</span>
                  </div>
                </div>
                <div class="pfs-answer-banner">
                  <span><i class="fa-solid fa-circle-check"></i> Final Answer: 49 cm&sup2;</span>
                  <span style="font-size:0.86rem;">Full 2 Marks</span>
                </div>
              </div>

              <!-- Right Column: Proportional Shape Diagram -->
              <div class="pfs-diagram-col">
                <svg viewBox="0 0 340 210">
                  <defs>
                    <marker id="arrowT" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
                      <polygon points="0 0, 6 3, 0 6" fill="#0f172a" />
                    </marker>
                    <marker id="arrowTRev" markerWidth="6" markerHeight="6" refX="1" refY="3" orient="auto">
                      <polygon points="6 0, 0 3, 6 6" fill="#0f172a" />
                    </marker>
                  </defs>

                  <!-- Solid Olive Green Triangle -->
                  <polygon points="35,160 285,160 115,35" fill="#6ca33e" stroke="#4d7c0f" stroke-width="2"/>

                  <!-- Perpendicular Vertical Height Line Inside -->
                  <line x1="115" y1="35" x2="115" y2="160" stroke="#0f172a" stroke-width="2" marker-start="url(#arrowTRev)" marker-end="url(#arrowT)"/>
                  <!-- Right Angle Indicator -->
                  <rect x="115" y="146" width="14" height="14" fill="none" stroke="#0f172a" stroke-width="1.8"/>
                  <text x="145" y="105" font-family="system-ui, sans-serif" font-size="18" font-weight="800" fill="#0f172a">7 cm</text>

                  <!-- Bottom Base Dimension Arrow & Label -->
                  <line x1="35" y1="182" x2="285" y2="182" stroke="#0f172a" stroke-width="2" marker-start="url(#arrowTRev)" marker-end="url(#arrowT)"/>
                  <text x="160" y="202" font-family="system-ui, sans-serif" font-size="18" font-weight="800" fill="#0f172a" text-anchor="middle">14 cm</text>
                </svg>
              </div>
            </div>

            <!-- Footer Pills -->
            <div class="pfs-card-footer">
              <span class="pfs-pill-l1">FS Level 1</span>
              <span class="pfs-pill-l2">FS Level 2</span>
              <span class="pfs-pill-board">Edexcel</span>
              <span class="pfs-pill-board">City &amp; Guilds</span>
              <span class="pfs-pill-board">NCFE</span>
              <span class="pfs-pill-board">Open Awards</span>
              <span class="pfs-pill-board">Highfield</span>
            </div>
          </div>

          <!-- ============================================== -->
          <!-- EXAMPLE 4: AREA OF A TRAPEZIUM -->
          <!-- ============================================== -->
          <div class="pfs-card" id="example-4">
            <div class="pfs-card-head">
              <h3 class="pfs-card-title">
                <span class="pfs-prefix">Example 4:</span> Area of a Trapezium
              </h3>
              <p class="pfs-card-stem">
                Calculate the area of the trapezium shown to the right.
              </p>
            </div>

            <div class="pfs-card-body">
              <!-- Left Column: Formula & Steps -->
              <div class="pfs-math-col">
                <div class="pfs-marks-row">[2 marks]</div>
                <div class="pfs-formula-display">
                  Area = ((8 + 14) &divide; 2) &times; 6 = 11 &times; 6 = 66 cm&sup2;
                </div>
                <div class="pfs-steps-box">
                  <div class="pfs-step-row">
                    <span class="pfs-step-tag">Step 1:</span>
                    <span>Add parallel sides a and b: <strong>8 + 14 = 22</strong>.</span>
                  </div>
                  <div class="pfs-step-row">
                    <span class="pfs-step-tag">Step 2:</span>
                    <span>Divide by 2 to find mean parallel width: <strong>22 &divide; 2 = 11 cm</strong>.</span>
                  </div>
                  <div class="pfs-step-row">
                    <span class="pfs-step-tag">Step 3:</span>
                    <span>Multiply by perpendicular height: <strong>11 &times; 6 = 66 cm&sup2;</strong>.</span>
                  </div>
                </div>
                <div class="pfs-answer-banner">
                  <span><i class="fa-solid fa-circle-check"></i> Final Answer: 66 cm&sup2;</span>
                  <span style="font-size:0.86rem;">Full 2 Marks</span>
                </div>
              </div>

              <!-- Right Column: Proportional Shape Diagram -->
              <div class="pfs-diagram-col">
                <svg viewBox="0 0 340 210">
                  <defs>
                    <marker id="arrowTr" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
                      <polygon points="0 0, 6 3, 0 6" fill="#0f172a" />
                    </marker>
                    <marker id="arrowTrRev" markerWidth="6" markerHeight="6" refX="1" refY="3" orient="auto">
                      <polygon points="6 0, 0 3, 6 6" fill="#0f172a" />
                    </marker>
                  </defs>

                  <!-- Solid Royal Purple Trapezium -->
                  <polygon points="80,45 220,45 285,155 35,155" fill="#7c3aed" stroke="#6d28d9" stroke-width="2"/>

                  <!-- Parallel Arrow Indicators >> -->
                  <text x="150" y="42" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">&gt;&gt;</text>
                  <text x="160" y="152" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">&gt;&gt;</text>

                  <!-- Top Side Dimension (8 cm) -->
                  <line x1="80" y1="26" x2="220" y2="26" stroke="#0f172a" stroke-width="1.8" marker-start="url(#arrowTrRev)" marker-end="url(#arrowTr)"/>
                  <text x="150" y="20" font-family="system-ui, sans-serif" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">8 cm</text>

                  <!-- Bottom Side Dimension (14 cm) -->
                  <line x1="35" y1="175" x2="285" y2="175" stroke="#0f172a" stroke-width="2" marker-start="url(#arrowTrRev)" marker-end="url(#arrowTr)"/>
                  <text x="160" y="196" font-family="system-ui, sans-serif" font-size="18" font-weight="800" fill="#0f172a" text-anchor="middle">14 cm</text>

                  <!-- Vertical Height Dashed Line (6 cm) -->
                  <line x1="80" y1="45" x2="80" y2="155" stroke="#ffffff" stroke-width="2" stroke-dasharray="5,4"/>
                  <rect x="80" y="141" width="14" height="14" fill="none" stroke="#ffffff" stroke-width="1.8"/>
                  <text x="104" y="105" font-family="system-ui, sans-serif" font-size="16" font-weight="800" fill="#ffffff">6 cm</text>

                  <!-- Distractor Slanted Side (7.5 cm) -->
                  <text x="270" y="100" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">7.5 cm</text>
                </svg>
              </div>
            </div>

            <!-- Footer Pills -->
            <div class="pfs-card-footer">
              <span class="pfs-pill-l2">FS Level 2</span>
              <span class="pfs-pill-board">Edexcel</span>
              <span class="pfs-pill-board">City &amp; Guilds</span>
              <span class="pfs-pill-board">NCFE</span>
              <span class="pfs-pill-board">Open Awards</span>
              <span class="pfs-pill-board">Highfield</span>
            </div>
          </div>

          <!-- ============================================== -->
          <!-- EXAMPLE 5: AREA OF A COMPOUND L-SHAPE -->
          <!-- ============================================== -->
          <div class="pfs-card" id="example-5">
            <div class="pfs-card-head">
              <h3 class="pfs-card-title">
                <span class="pfs-prefix">Example 5:</span> Area of a Compound Shape (L-Shape)
              </h3>
              <p class="pfs-card-stem">
                Calculate the total floor area of the L-shaped workshop shown to the right.
              </p>
            </div>

            <div class="pfs-card-body">
              <!-- Left Column: Formula & Steps -->
              <div class="pfs-math-col">
                <div class="pfs-marks-row">[3 marks]</div>
                <div class="pfs-formula-display">
                  Total Area = Area A + Area B = 42 + 48 = 90 m&sup2;
                </div>
                <div class="pfs-steps-box">
                  <div class="pfs-step-row">
                    <span class="pfs-step-tag">Step 1:</span>
                    <span>Split horizontally: Block A (top) and Block B (bottom).</span>
                  </div>
                  <div class="pfs-step-row">
                    <span class="pfs-step-tag">Step 2:</span>
                    <span><strong>Area of Block A:</strong> 7 m &times; 6 m = <strong>42 m&sup2;</strong>.</span>
                  </div>
                  <div class="pfs-step-row">
                    <span class="pfs-step-tag">Step 3:</span>
                    <span><strong>Area of Block B:</strong> 12 m &times; 4 m = <strong>48 m&sup2;</strong>.</span>
                  </div>
                  <div class="pfs-step-row">
                    <span class="pfs-step-tag">Step 4:</span>
                    <span>Add both areas together: <strong>42 + 48 = 90 m&sup2;</strong>.</span>
                  </div>
                </div>
                <div class="pfs-answer-banner">
                  <span><i class="fa-solid fa-circle-check"></i> Final Answer: 90 m&sup2;</span>
                  <span style="font-size:0.86rem;">Full 3 Marks</span>
                </div>
              </div>

              <!-- Right Column: Proportional Shape Diagram -->
              <div class="pfs-diagram-col">
                <svg viewBox="0 0 340 230">
                  <defs>
                    <marker id="arrowC" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
                      <polygon points="0 0, 6 3, 0 6" fill="#0f172a" />
                    </marker>
                    <marker id="arrowCRev" markerWidth="6" markerHeight="6" refX="1" refY="3" orient="auto">
                      <polygon points="6 0, 0 3, 6 6" fill="#0f172a" />
                    </marker>
                  </defs>

                  <!-- Block A (Top, Sky Blue) -->
                  <rect x="45" y="30" width="130" height="90" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
                  <!-- Block B (Bottom, Emerald Green) -->
                  <rect x="45" y="120" width="240" height="60" fill="#059669" stroke="#047857" stroke-width="2"/>

                  <!-- Red Dashed Split Line -->
                  <line x1="45" y1="120" x2="175" y2="120" stroke="#ef4444" stroke-width="3" stroke-dasharray="6,4"/>

                  <!-- Labels Inside Blocks -->
                  <text x="110" y="80" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#ffffff" text-anchor="middle">A: 7 &times; 6 = 42</text>
                  <text x="165" y="155" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#ffffff" text-anchor="middle">B: 12 &times; 4 = 48</text>

                  <!-- Outer Dimension Labels -->
                  <!-- Top Width (7 m) -->
                  <text x="110" y="22" font-family="system-ui, sans-serif" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">7 m</text>
                  <!-- Total Left Height (10 m) -->
                  <line x1="25" y1="30" x2="25" y2="180" stroke="#0f172a" stroke-width="1.8" marker-start="url(#arrowCRev)" marker-end="url(#arrowC)"/>
                  <text x="14" y="110" font-family="system-ui, sans-serif" font-size="15" font-weight="800" fill="#0f172a" text-anchor="middle">10m</text>
                  <!-- Total Bottom Width (12 m) -->
                  <line x1="45" y1="200" x2="285" y2="200" stroke="#0f172a" stroke-width="2" marker-start="url(#arrowCRev)" marker-end="url(#arrowC)"/>
                  <text x="165" y="220" font-family="system-ui, sans-serif" font-size="17" font-weight="800" fill="#0f172a" text-anchor="middle">12 m</text>
                  <!-- Right Base Height (4 m) -->
                  <text x="305" y="155" font-family="system-ui, sans-serif" font-size="15" font-weight="800" fill="#0f172a">4 m</text>
                  <!-- Inner Step Width (5 m) -->
                  <text x="230" y="112" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#64748b">5 m</text>
                </svg>
              </div>
            </div>

            <!-- Footer Pills -->
            <div class="pfs-card-footer">
              <span class="pfs-pill-l1">FS Level 1</span>
              <span class="pfs-pill-l2">FS Level 2</span>
              <span class="pfs-pill-board">Edexcel</span>
              <span class="pfs-pill-board">City &amp; Guilds</span>
              <span class="pfs-pill-board">NCFE</span>
              <span class="pfs-pill-board">Open Awards</span>
              <span class="pfs-pill-board">Highfield</span>
            </div>
          </div>

          <!-- ============================================== -->
          <!-- EXAMPLE 6: AREA OF A CIRCLE -->
          <!-- ============================================== -->
          <div class="pfs-card" id="example-6">
            <div class="pfs-card-head">
              <h3 class="pfs-card-title">
                <span class="pfs-prefix">Example 6:</span> Area of a Circle
              </h3>
              <p class="pfs-card-stem">
                Calculate the area of the circular hospital helipad shown to the right. Give your answer to 1 decimal place.
              </p>
            </div>

            <div class="pfs-card-body">
              <!-- Left Column: Formula & Steps -->
              <div class="pfs-math-col">
                <div class="pfs-marks-row">[2 marks]</div>
                <div class="pfs-formula-display">
                  Area of circle = &pi; &times; 7&sup2; = 49&pi; &approx; 153.9 m&sup2;
                </div>
                <div class="pfs-steps-box">
                  <div class="pfs-step-row">
                    <span class="pfs-step-tag">Step 1:</span>
                    <span>Identify radius: <strong>r = 7 m</strong>.</span>
                  </div>
                  <div class="pfs-step-row">
                    <span class="pfs-step-tag">Step 2:</span>
                    <span>Square the radius: <strong>7&sup2; = 49</strong>.</span>
                  </div>
                  <div class="pfs-step-row">
                    <span class="pfs-step-tag">Step 3:</span>
                    <span>Multiply by &pi; (3.14159...): <strong>49 &times; &pi; = 153.938... &approx; 153.9 m&sup2;</strong>.</span>
                  </div>
                </div>
                <div class="pfs-answer-banner">
                  <span><i class="fa-solid fa-circle-check"></i> Final Answer: 153.9 m&sup2;</span>
                  <span style="font-size:0.86rem;">Full 2 Marks</span>
                </div>
              </div>

              <!-- Right Column: Proportional Shape Diagram -->
              <div class="pfs-diagram-col">
                <svg viewBox="0 0 340 200">
                  <!-- Solid Amber/Orange Circle -->
                  <circle cx="170" cy="100" r="75" fill="#d97706" stroke="#b45309" stroke-width="2"/>
                  <!-- Center Point -->
                  <circle cx="170" cy="100" r="4" fill="#ffffff"/>
                  <!-- Radius Line -->
                  <line x1="170" y1="100" x2="245" y2="100" stroke="#ffffff" stroke-width="2.5"/>
                  <text x="207" y="90" font-family="system-ui, sans-serif" font-size="16" font-weight="800" fill="#ffffff">r = 7 m</text>
                </svg>
              </div>
            </div>

            <!-- Footer Pills -->
            <div class="pfs-card-footer">
              <span class="pfs-pill-l2">FS Level 2</span>
              <span class="pfs-pill-board">Edexcel</span>
              <span class="pfs-pill-board">City &amp; Guilds</span>
              <span class="pfs-pill-board">NCFE</span>
              <span class="pfs-pill-board">Open Awards</span>
              <span class="pfs-pill-board">Highfield</span>
            </div>
          </div>

        </section>

        <!-- ============================================== -->
        <!-- 4. PEARSON EDEXCEL WORKED EXAM MODELS -->
        <!-- ============================================== -->
        <section id="worked-models" class="revision-section">
          <div class="section-header-row">
            <h2 class="section-title"><i class="fa-solid fa-file-signature"></i> Pearson Edexcel Step-by-Step Worked Models</h2>
            <span style="font-size:0.88rem; font-weight:700; color:#059669;"><i class="fa-solid fa-award"></i> Official Mark Schemes</span>
          </div>
          <p class="section-lead-text">
            These realistic healthcare and vocational exam questions demonstrate how examiners award Method Marks (<strong>M</strong>), Process Marks (<strong>P</strong>), and Accuracy Marks (<strong>A</strong>).
          </p>

          <!-- MODEL 1: NHS CLINIC FLOOR TILING -->
          <div class="worked-exam-model-card">
            <div class="model-header-bar">
              <span class="badge-worked-model">Worked Exam Model #1 &bull; Level 1 &amp; Level 2</span>
              <span class="model-marks-pill"><i class="fa-solid fa-check-double"></i> 4 Marks Total</span>
            </div>

            <div class="model-question-stem">
              <strong>Exam Context:</strong> An NHS healthcare centre manager needs to retile the floor of a new physiotherapy room measuring <strong>8.5 m long</strong> and <strong>4 m wide</strong>. 
              Each box of non-slip floor tiles covers <strong>3.2 m&sup2;</strong> and costs <strong>£28.50</strong> per box. Tiles are only sold in full boxes. 
              <br><br>
              Calculate the total cost to buy enough boxes of tiles for the room floor.
            </div>

            <div class="model-steps-list">
              <div class="model-step-row">
                <span class="step-number-bubble">Step 1</span>
                <div class="step-detail-body">
                  <div class="step-detail-title">Calculate the floor surface area of the room</div>
                  <div class="step-math-line">Area = 8.5 m &times; 4 m = 34 m&sup2;</div>
                  <div class="mark-scheme-tag"><i class="fa-solid fa-circle-check"></i> [M1] Correct method for rectangle area (8.5 &times; 4)</div>
                </div>
              </div>

              <div class="model-step-row">
                <span class="step-number-bubble">Step 2</span>
                <div class="step-detail-body">
                  <div class="step-detail-title">Divide room area by pack coverage to find required boxes</div>
                  <div class="step-math-line">34 &divide; 3.2 = 10.625 boxes</div>
                  <div class="mark-scheme-tag"><i class="fa-solid fa-circle-check"></i> [M1] Process mark for area &divide; 3.2</div>
                </div>
              </div>

              <div class="model-step-row">
                <span class="step-number-bubble">Step 3</span>
                <div class="step-detail-body">
                  <div class="step-detail-title">Round UP to whole boxes (practical real-world rounding)</div>
                  <div class="step-math-line">10.625 boxes &rarr; Round UP to 11 full boxes</div>
                  <div class="mark-scheme-tag"><i class="fa-solid fa-circle-check"></i> [P1] Correct interpretation to round UP to whole units (11)</div>
                </div>
              </div>

              <div class="model-step-row">
                <span class="step-number-bubble">Step 4</span>
                <div class="step-detail-body">
                  <div class="step-detail-title">Calculate total purchase cost</div>
                  <div class="step-math-line">11 &times; £28.50 = £313.50</div>
                  <div class="mark-scheme-tag"><i class="fa-solid fa-circle-check"></i> [A1] Accurate final cost of £313.50</div>
                </div>
              </div>
            </div>

            <div class="model-final-answer-callout">
              <div class="model-final-text">
                <i class="fa-solid fa-award"></i> Final Exam Answer: £313.50 (11 Boxes)
              </div>
              <span style="font-size:0.9rem; opacity:0.95;">Full 4/4 Marks Achieved</span>
            </div>
          </div>

          <!-- MODEL 2: TRAPEZIUM CAR PARK TARMAC -->
          <div class="worked-exam-model-card">
            <div class="model-header-bar">
              <span class="badge-worked-model" style="background:#fef3c7; border-color:#fde68a; color:#92400e;">Worked Exam Model #2 &bull; Level 2</span>
              <span class="model-marks-pill"><i class="fa-solid fa-check-double"></i> 3 Marks Total</span>
            </div>

            <div class="model-question-stem">
              <strong>Exam Context:</strong> An NHS health centre ambulance bay is shaped as a trapezium. The two parallel boundary walls are <strong>24 m</strong> and <strong>36 m</strong> long. The perpendicular distance between these walls is <strong>15 m</strong>. Tarmac surfacing costs <strong>£18 per m&sup2;</strong>. Calculate the total cost to tarmac the bay.
            </div>

            <div class="model-steps-list">
              <div class="model-step-row">
                <span class="step-number-bubble">Step 1</span>
                <div class="step-detail-body">
                  <div class="step-detail-title">Apply the trapezium area formula</div>
                  <div class="step-math-line">Mean of parallel sides = (24 + 36) &divide; 2 = 60 &divide; 2 = 30 m</div>
                  <div class="step-math-line">Area = 30 m &times; 15 m = 450 m&sup2;</div>
                  <div class="mark-scheme-tag"><i class="fa-solid fa-circle-check"></i> [M1] Correct method for trapezium area</div>
                </div>
              </div>

              <div class="model-step-row">
                <span class="step-number-bubble">Step 2</span>
                <div class="step-detail-body">
                  <div class="step-detail-title">Multiply surface area by cost per square metre</div>
                  <div class="step-math-line">450 m&sup2; &times; £18 = £8,100</div>
                  <div class="mark-scheme-tag"><i class="fa-solid fa-circle-check"></i> [M1] Multiplying area by £18</div>
                </div>
              </div>

              <div class="model-step-row">
                <span class="step-number-bubble">Step 3</span>
                <div class="step-detail-body">
                  <div class="step-detail-title">State final total cost</div>
                  <div class="step-math-line">£8,100 (or £8,100.00)</div>
                  <div class="mark-scheme-tag"><i class="fa-solid fa-circle-check"></i> [A1] Accuracy mark for £8,100</div>
                </div>
              </div>
            </div>

            <div class="model-final-answer-callout">
              <div class="model-final-text">
                <i class="fa-solid fa-award"></i> Final Exam Answer: £8,100
              </div>
              <span style="font-size:0.9rem; opacity:0.95;">Full 3/3 Marks Achieved</span>
            </div>
          </div>
        </section>

        <!-- ============================================== -->
        <!-- 5. EXAMINER TRAPS & PITFALLS -->
        <!-- ============================================== -->
        <section id="examiner-traps" class="revision-section">
          <div class="section-header-row">
            <h2 class="section-title"><i class="fa-solid fa-triangle-exclamation"></i> Examiner Traps to Avoid</h2>
          </div>
          <p class="section-lead-text">
            Official examiner reports from Pearson Edexcel highlight the four most frequent reasons candidates drop marks on area questions.
          </p>

          <!-- Trap 1 -->
          <div class="trap-card-coral">
            <div class="trap-card-coral-header">
              <i class="fa-solid fa-circle-xmark"></i>
              <span>Trap 1: Forgetting to Divide by 2 on Triangles</span>
            </div>
            <p>
              Candidates calculate <em>Base &times; Height</em> and immediately write that down as their answer. That gives the area of a rectangle, not a triangle!
            </p>
            <div class="trap-solution-badge">
              <i class="fa-solid fa-check" style="color:#059669;"></i> <strong>Remedy:</strong> Always double check: did I divide by 2? Write &ldquo;&divide; 2&rdquo; in your working immediately.
            </div>
          </div>

          <!-- Trap 2 -->
          <div class="trap-card-coral">
            <div class="trap-card-coral-header">
              <i class="fa-solid fa-circle-xmark"></i>
              <span>Trap 2: Rounding DOWN or Keeping Decimals for Packs/Tins</span>
            </div>
            <p>
              When a question asks for tins of paint or packs of tiles, writing <em>&ldquo;4.3 tins&rdquo;</em> or rounding down to 4 means the job cannot be finished. In the real world, you cannot purchase 0.3 of a tin!
            </p>
            <div class="trap-solution-badge">
              <i class="fa-solid fa-check" style="color:#059669;"></i> <strong>Remedy:</strong> Practical questions require whole units. Always round UP to the nearest whole integer.
            </div>
          </div>

          <!-- Trap 3 -->
          <div class="trap-card-coral">
            <div class="trap-card-coral-header">
              <i class="fa-solid fa-circle-xmark"></i>
              <span>Trap 3: Mixing Centimetres and Metres</span>
            </div>
            <p>
              Length given as 2.4 m and width as 75 cm. Multiplying 2.4 &times; 75 gives 180 m&sup2;, which is completely incorrect!
            </p>
            <div class="trap-solution-badge">
              <i class="fa-solid fa-check" style="color:#059669;"></i> <strong>Remedy:</strong> Convert first: 75 cm &divide; 100 = 0.75 m. Then multiply: 2.4 &times; 0.75 = 1.8 m&sup2;.
            </div>
          </div>

          <!-- Trap 4 -->
          <div class="trap-card-coral">
            <div class="trap-card-coral-header">
              <i class="fa-solid fa-circle-xmark"></i>
              <span>Trap 4: Using Full Dimensions on Split Compound Shapes</span>
            </div>
            <p>
              When splitting an L-shape, candidates frequently use the overall total base for both rectangles, accidentally counting sections twice!
            </p>
            <div class="trap-solution-badge">
              <i class="fa-solid fa-check" style="color:#059669;"></i> <strong>Remedy:</strong> Label each section Block A and Block B. Clearly write the length and width of each block separately.
            </div>
          </div>
        </section>

        <!-- ============================================== -->
        <!-- 6. INTERACTIVE EXAM PRACTICE TASKS -->
        <!-- ============================================== -->
        <section id="practice-questions" class="revision-section">
          <div class="section-header-row">
            <h2 class="section-title"><i class="fa-solid fa-pencil"></i> Interactive Exam Practice Tasks</h2>
            <span style="font-size:0.88rem; font-weight:700; color:var(--accent);"><i class="fa-solid fa-clock"></i> Self-Paced Practice</span>
          </div>
          <p class="section-lead-text">
            Attempt these realistic Pearson Edexcel style exam questions. Type your working in the scratchpad, then reveal the model mark scheme to evaluate your marks.
          </p>

          <!-- PRACTICE QUESTION 1 -->
          <div class="practice-q-card">
            <div class="practice-q-header">
              <span class="practice-q-num">Practice Task 1 &bull; Triangle Roof Gable</span>
              <span class="practice-q-marks">[2 Marks] &bull; Level 1 &amp; Level 2</span>
            </div>
            <div class="practice-q-stem">
              A builder needs to cover a triangular roof gable with timber cladding. The gable has a horizontal base of <strong>7.2 m</strong> and a perpendicular height of <strong>2.8 m</strong>. Calculate the area of cladding required.
            </div>
            <div class="working-scratchpad-area">
              <label class="working-scratchpad-label" for="scratchpad1">Your Working &amp; Calculations:</label>
              <textarea id="scratchpad1" class="working-scratchpad-input" placeholder="Type your working here (e.g. 7.2 * 2.8 / 2 = ...)"></textarea>
            </div>
            <div class="practice-q-toolbar">
              <button type="button" class="btn-reveal-solution" onclick="toggleSolutionDrawer('solDrawer1')">
                <i class="fa-solid fa-eye"></i> <span>Show Model Solution &amp; Mark Scheme</span>
              </button>
            </div>
            <div id="solDrawer1" class="solution-drawer">
              <div class="solution-drawer-title">
                <i class="fa-solid fa-circle-check"></i> Official Mark Scheme Breakdown
              </div>
              <ul style="padding-left:20px; line-height:1.75; color:#166534; margin:0;">
                <li><strong>[M1] Method Mark:</strong> Base &times; Height &divide; 2 &rarr; 7.2 &times; 2.8 &divide; 2 (or 20.16 &divide; 2)</li>
                <li><strong>[A1] Accuracy Mark:</strong> <strong>10.08 m&sup2;</strong> (Units must be m&sup2;)</li>
              </ul>
            </div>
          </div>

          <!-- PRACTICE QUESTION 2 -->
          <div class="practice-q-card">
            <div class="practice-q-header">
              <span class="practice-q-num">Practice Task 2 &bull; Compound L-Shaped Office Suite</span>
              <span class="practice-q-marks">[4 Marks] &bull; Level 2</span>
            </div>
            <div class="practice-q-stem">
              An office manager wants to carpet an L-shaped meeting room. The outer dimensions are: total length <strong>9 m</strong>, total width <strong>8 m</strong>, with an indent reducing the width to <strong>5 m</strong> over a <strong>4 m</strong> stretch. 
              Carpet tiles cost <strong>£16.50 per m&sup2;</strong>. Calculate the total cost to carpet the room.
            </div>
            <div class="working-scratchpad-area">
              <label class="working-scratchpad-label" for="scratchpad2">Your Working &amp; Calculations:</label>
              <textarea id="scratchpad2" class="working-scratchpad-input" placeholder="Type your working here..."></textarea>
            </div>
            <div class="practice-q-toolbar">
              <button type="button" class="btn-reveal-solution" onclick="toggleSolutionDrawer('solDrawer2')">
                <i class="fa-solid fa-eye"></i> <span>Show Model Solution &amp; Mark Scheme</span>
              </button>
            </div>
            <div id="solDrawer2" class="solution-drawer">
              <div class="solution-drawer-title">
                <i class="fa-solid fa-circle-check"></i> Official Mark Scheme Breakdown
              </div>
              <ul style="padding-left:20px; line-height:1.75; color:#166534; margin:0;">
                <li><strong>[M1] Split Shape:</strong> Rectangle A = 9 &times; 5 = 45 m&sup2;, Rectangle B = (8 - 5) &times; 4 = 3 &times; 4 = 12 m&sup2; (or alternative split).</li>
                <li><strong>[M1] Total Area:</strong> 45 + 12 = 57 m&sup2; (or 9 &times; 8 - 5 &times; 3 = 72 - 15 = 57 m&sup2;).</li>
                <li><strong>[M1] Cost Calculation:</strong> 57 &times; £16.50 = £940.50.</li>
                <li><strong>[A1] Final Answer:</strong> <strong>£940.50</strong>.</li>
              </ul>
            </div>
          </div>
        </section>

        <!-- ============================================== -->
        <!-- 7. CURRICULUM PROGRESSION -->
        <!-- ============================================== -->
        <section id="curriculum-links" class="progression-banner">
          <div class="progression-text-area">
            <h3 class="progression-title">Ready for Your Next Revision Step?</h3>
            <p style="color:#cbd5e1; margin:0; line-height:1.6;">
              Solidify your geometric problem-solving by mastering perimeter and 3D volume next.
            </p>
          </div>
          <div class="progression-links-group">
            <a href="functional-skills-perimeter.html" class="btn-progression-nav">
              <i class="fa-solid fa-vector-square"></i> Next: Perimeter Guide
            </a>
            <a href="functional-skills-volume.html" class="btn-progression-nav">
              <i class="fa-solid fa-cube"></i> Volume &amp; 3D Shapes
            </a>
            <a href="functional-skills-maths-level-2.html" class="btn-progression-nav">
              <i class="fa-solid fa-graduation-cap"></i> Maths Index
            </a>
          </div>
        </section>

      </div>
    </div>
  </main>

  <!-- ============================================== -->
  <!-- FOOTER -->
  <!-- ============================================== -->
  <footer class="site-footer">
    <div class="revision-page-wrapper">
      <div class="footer-bottom" style="border-top:1px solid #e2e8f0; padding:24px 0; text-align:center; color:#64748b; font-size:0.88rem;">
        <p>&copy; 2026 Master Functional Skills. All rights reserved. Specialist Functional Skills revision for apprenticeships, healthcare &amp; vocational learners.</p>
      </div>
    </div>
  </footer>

  <!-- Interactive JavaScript Scripts -->
  <script>
    // Solution Drawer Toggler
    function toggleSolutionDrawer(id) {
      var drawer = document.getElementById(id);
      if (drawer) {
        drawer.classList.toggle('open');
      }
    }

    // Mobile Table of Contents Toggler
    function toggleMobileToc() {
      var sidebar = document.getElementById('sidebarNav');
      if (sidebar) {
        if (sidebar.style.display === 'block') {
          sidebar.style.display = 'none';
        } else {
          sidebar.style.display = 'block';
        }
      }
    }

    // Dyslexia Background Tint Cycler
    var tints = ['cream', 'peach', 'mint', 'sage', 'none'];
    var currentTintIndex = 0;
    function cycleTint() {
      currentTintIndex = (currentTintIndex + 1) % tints.length;
      var selectedTint = tints[currentTintIndex];
      document.documentElement.setAttribute('data-tint', selectedTint);
      localStorage.setItem('mfs_user_tint', selectedTint);
    }

    // Scroll Spy for Table of Contents
    window.addEventListener('DOMContentLoaded', function() {
      var savedTint = localStorage.getItem('mfs_user_tint');
      if (savedTint) {
        document.documentElement.setAttribute('data-tint', savedTint);
      }

      var sections = document.querySelectorAll('section.revision-section');
      var navLinks = document.querySelectorAll('.sidebar-toc-link');

      window.addEventListener('scroll', function() {
        var fromTop = window.scrollY + 140;
        sections.forEach(function(section) {
          var top = section.offsetTop;
          var height = section.offsetHeight;
          var id = section.getAttribute('id');
          if (fromTop >= top && fromTop < top + height) {
            navLinks.forEach(function(link) {
              link.classList.remove('active');
              if (link.getAttribute('href') === '#' + id) {
                link.classList.add('active');
              }
            });
          }
        });
      });
    });
  </script>

</body>
</html>
"""

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html_code)

print("functional-skills-area.html successfully generated with original examples and PFS styling!")
