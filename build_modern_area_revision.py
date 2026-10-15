import os

PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"
OUTPUT_FILE = os.path.join(PROJECT_DIR, "functional-skills-area.html")

html_content = """<!DOCTYPE html>
<html lang="en-GB" data-theme="sapphire" data-tint="cream">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Area Revision Guide | Functional Skills Maths Level 1 & Level 2 | Master Functional Skills</title>
  <meta name="description" content="Complete Functional Skills Maths Level 1 & Level 2 Area revision guide. Master rectangle, triangle, trapezium, and compound shapes with formulas, worked exam models, and interactive practice.">
  <link rel="stylesheet" href="assets/css/mfs-theme.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
  
  <style>
    /* ==========================================================================
       MODERN REVISION PAGE STYLES — MASTER FUNCTIONAL SKILLS
       ========================================================================== */

    /* Breadcrumbs Bar */
    .revision-breadcrumb-bar {
      background: var(--bg-card);
      border-bottom: 1px solid var(--border);
      padding: 12px 0;
      font-size: 0.85rem;
    }
    .revision-breadcrumbs {
      display: flex;
      align-items: center;
      gap: 8px;
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
    .revision-hero-card::after {
      content: "";
      position: absolute;
      top: -60px;
      right: -60px;
      width: 320px;
      height: 320px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(37, 99, 235, 0.25) 0%, rgba(37, 99, 235, 0) 70%);
      pointer-events: none;
    }
    .revision-hero-pill-row {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      margin-bottom: 14px;
    }
    .badge-pill-accent {
      background: var(--accent);
      color: #ffffff;
      font-size: 0.78rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 4px 12px;
      border-radius: var(--radius-full);
    }
    .badge-pill-gold {
      background: #f59e0b;
      color: #070d1e;
      font-size: 0.78rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 4px 12px;
      border-radius: var(--radius-full);
    }
    .badge-pill-outline {
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid rgba(255, 255, 255, 0.25);
      color: #e2e8f0;
      font-size: 0.78rem;
      font-weight: 600;
      padding: 4px 12px;
      border-radius: var(--radius-full);
    }
    .revision-hero-title {
      font-size: 2.35rem;
      font-weight: 800;
      line-height: 1.2;
      margin-bottom: 12px;
      color: #ffffff;
    }
    .revision-hero-title span {
      color: #60a5fa;
    }
    .revision-hero-desc {
      font-size: 1.05rem;
      line-height: 1.6;
      color: #cbd5e1;
      max-width: 820px;
      margin-bottom: 24px;
    }
    .revision-hero-meta-bar {
      display: flex;
      align-items: center;
      gap: 20px;
      flex-wrap: wrap;
      font-size: 0.88rem;
      color: #94a3b8;
      border-top: 1px solid rgba(255, 255, 255, 0.12);
      padding-top: 18px;
    }
    .hero-meta-item {
      display: inline-flex;
      align-items: center;
      gap: 7px;
    }
    .hero-meta-item i {
      color: #60a5fa;
    }
    .hero-quick-actions {
      margin-left: auto;
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
    }
    .btn-hero-dl {
      background: #f59e0b;
      color: #070d1e;
      font-weight: 800;
      padding: 9px 18px;
      border-radius: var(--radius-md);
      text-decoration: none;
      font-size: 0.88rem;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }
    .btn-hero-dl:hover {
      background: #d97706;
      color: #ffffff;
      transform: translateY(-1px);
    }
    .btn-hero-cards {
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.3);
      color: #ffffff;
      font-weight: 700;
      padding: 9px 18px;
      border-radius: var(--radius-md);
      text-decoration: none;
      font-size: 0.88rem;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }
    .btn-hero-cards:hover {
      background: rgba(255, 255, 255, 0.2);
      color: #ffffff;
    }

    /* 2-Column Responsive Layout */
    .revision-layout {
      display: grid;
      grid-template-columns: 290px 1fr;
      gap: 36px;
      padding: 40px 0 80px;
      align-items: start;
    }
    @media (max-width: 991px) {
      .revision-layout {
        grid-template-columns: 1fr;
      }
      .revision-sidebar {
        display: none; /* Collapsed on mobile, available via sticky mobile toggle */
      }
    }

    /* Sticky Left Table of Contents */
    .revision-sidebar {
      position: sticky;
      top: 90px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 20px;
      box-shadow: var(--shadow-sm);
    }
    .sidebar-toc-title {
      font-size: 0.95rem;
      font-weight: 800;
      color: var(--navy-dark);
      text-transform: uppercase;
      letter-spacing: 0.06em;
      margin-bottom: 14px;
      padding-bottom: 10px;
      border-bottom: 2px solid var(--border-light);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .sidebar-toc-list {
      list-style: none;
      padding: 0;
      margin: 0 0 20px 0;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }
    .sidebar-toc-link {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 8px 12px;
      border-radius: var(--radius-sm);
      color: var(--text-secondary);
      font-size: 0.86rem;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.2s ease;
    }
    .sidebar-toc-link:hover {
      background: var(--accent-light);
      color: var(--accent);
      padding-left: 16px;
    }
    .sidebar-toc-link.active {
      background: var(--accent-light);
      color: var(--accent);
      font-weight: 700;
      border-left: 3px solid var(--accent);
    }
    .sidebar-toc-link i {
      font-size: 0.8rem;
      width: 16px;
      text-align: center;
      opacity: 0.85;
    }
    .sidebar-toc-badge {
      margin-left: auto;
      font-size: 0.7rem;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 4px;
      background: var(--border-light);
      color: var(--text-muted);
    }

    /* Sidebar Promo Card */
    .sidebar-cards-promo {
      background: linear-gradient(135deg, #070d1e 0%, #1e293b 100%);
      color: #ffffff;
      border-radius: var(--radius-md);
      padding: 16px;
      text-align: center;
      border: 1px solid rgba(255, 255, 255, 0.12);
      margin-top: 14px;
    }
    .sidebar-cards-promo img {
      width: 100%;
      max-height: 120px;
      object-fit: contain;
      margin-bottom: 10px;
      filter: drop-shadow(0 8px 16px rgba(0,0,0,0.4));
    }
    .sidebar-cards-promo h4 {
      font-size: 0.95rem;
      font-weight: 800;
      margin-bottom: 4px;
      color: #ffffff;
    }
    .sidebar-cards-promo p {
      font-size: 0.78rem;
      color: #cbd5e1;
      margin-bottom: 12px;
      line-height: 1.4;
    }
    .btn-sidebar-shop {
      display: block;
      background: #f59e0b;
      color: #070d1e;
      font-weight: 800;
      font-size: 0.8rem;
      padding: 8px;
      border-radius: var(--radius-sm);
      text-decoration: none;
      transition: background 0.2s ease;
    }
    .btn-sidebar-shop:hover {
      background: #d97706;
      color: #ffffff;
    }

    /* Mobile TOC Floating Bar */
    .mobile-toc-bar {
      display: none;
      position: sticky;
      top: 70px;
      z-index: 100;
      background: var(--bg-card);
      border-bottom: 1px solid var(--border);
      padding: 10px 16px;
      box-shadow: var(--shadow-sm);
    }
    @media (max-width: 991px) {
      .mobile-toc-bar {
        display: flex;
        align-items: center;
        justify-content: space-between;
      }
    }
    .btn-mobile-toc {
      background: var(--accent-light);
      border: 1px solid var(--accent-border);
      color: var(--accent);
      padding: 6px 14px;
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    /* Main Revision Content Blocks */
    .revision-section {
      margin-bottom: 48px;
      scroll-margin-top: 100px;
    }
    .section-header-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 18px;
      padding-bottom: 10px;
      border-bottom: 2px solid var(--border-light);
    }
    .section-title {
      font-size: 1.6rem;
      font-weight: 800;
      color: var(--navy-dark);
      display: flex;
      align-items: center;
      gap: 12px;
      margin: 0;
    }
    .section-title i {
      color: var(--accent);
    }
    .section-lead-text {
      font-size: 1.02rem;
      line-height: 1.65;
      color: var(--text-secondary);
      margin-bottom: 22px;
    }

    /* COLOR-CODED COMPONENT 1: Golden Rules & Formulas (Amber/Gold) */
    .rule-card-amber {
      background: #fffbeb;
      border: 1px solid #fde68a;
      border-left: 5px solid #f59e0b;
      border-radius: var(--radius-md);
      padding: 20px 22px;
      margin-bottom: 18px;
      box-shadow: var(--shadow-sm);
    }
    .rule-card-amber-header {
      display: flex;
      align-items: center;
      gap: 10px;
      color: #92400e;
      font-weight: 800;
      font-size: 1.05rem;
      margin-bottom: 8px;
    }
    .rule-card-amber-header i {
      font-size: 1.25rem;
      color: #f59e0b;
    }
    .rule-card-amber p {
      color: #78350f;
      font-size: 0.94rem;
      line-height: 1.6;
      margin: 0 0 10px 0;
    }
    .rule-formula-box {
      background: #ffffff;
      border: 1px solid #fcd34d;
      border-radius: var(--radius-sm);
      padding: 10px 16px;
      font-family: inherit;
      font-weight: 800;
      font-size: 1.15rem;
      color: #b45309;
      display: inline-block;
      letter-spacing: 0.02em;
    }

    /* COLOR-CODED COMPONENT 2: Core Concept / Theory Cards (Oxford Blue/Sapphire) */
    .theory-card-blue {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 24px;
      margin-bottom: 24px;
      box-shadow: var(--shadow-sm);
    }
    .theory-grid-2col {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      align-items: center;
    }
    @media (max-width: 768px) {
      .theory-grid-2col {
        grid-template-columns: 1fr;
      }
    }
    .shape-diagram-box {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: var(--radius-md);
      padding: 20px;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }
    .shape-diagram-box svg {
      max-width: 100%;
      height: auto;
    }

    /* COLOR-CODED COMPONENT 3: Stepped Worked Models (Emerald Green) */
    .worked-model-card {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-top: 4px solid #10b981;
      border-radius: var(--radius-lg);
      padding: 24px;
      margin-bottom: 28px;
      box-shadow: var(--shadow-sm);
    }
    .model-header-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
      margin-bottom: 16px;
    }
    .badge-worked-model {
      background: #ecfdf5;
      border: 1px solid #a7f3d0;
      color: #065f46;
      font-size: 0.82rem;
      font-weight: 800;
      padding: 4px 12px;
      border-radius: var(--radius-full);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .model-marks-pill {
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--text-muted);
    }
    .model-question-stem {
      background: var(--bg-page);
      border-left: 3px solid #10b981;
      padding: 16px 20px;
      border-radius: var(--radius-md);
      font-size: 1.02rem;
      line-height: 1.6;
      color: var(--text-primary);
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
      background: #10b981;
      color: #ffffff;
      font-size: 0.85rem;
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
      font-size: 0.98rem;
      margin-bottom: 4px;
    }
    .step-math-line {
      font-family: monospace;
      font-size: 0.98rem;
      font-weight: 700;
      color: #065f46;
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      padding: 6px 12px;
      border-radius: var(--radius-sm);
      display: inline-block;
      margin: 4px 0 6px;
    }
    .mark-scheme-tag {
      font-size: 0.8rem;
      font-weight: 700;
      color: #047857;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .model-final-answer-callout {
      background: linear-gradient(135deg, #064e3b 0%, #065f46 100%);
      color: #ffffff;
      padding: 14px 20px;
      border-radius: var(--radius-md);
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
    }
    .model-final-text {
      font-weight: 800;
      font-size: 1.1rem;
    }

    /* COLOR-CODED COMPONENT 4: Examiner Traps & Warnings (Coral/Red Alert) */
    .trap-card-coral {
      background: #fef2f2;
      border: 1px solid #fecaca;
      border-left: 5px solid #ef4444;
      border-radius: var(--radius-md);
      padding: 18px 22px;
      margin-bottom: 18px;
    }
    .trap-card-coral-header {
      display: flex;
      align-items: center;
      gap: 10px;
      color: #991b1b;
      font-weight: 800;
      font-size: 1.05rem;
      margin-bottom: 6px;
    }
    .trap-card-coral-header i {
      color: #ef4444;
      font-size: 1.25rem;
    }
    .trap-card-coral p {
      color: #7f1d1d;
      font-size: 0.93rem;
      line-height: 1.6;
      margin: 0 0 8px 0;
    }
    .trap-remedy-pill {
      background: #ffffff;
      border: 1px solid #fca5a5;
      padding: 8px 14px;
      border-radius: var(--radius-sm);
      font-size: 0.88rem;
      color: #1e293b;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }

    /* COLOR-CODED COMPONENT 5: Interactive Practice Questions */
    .practice-q-card {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 24px;
      margin-bottom: 24px;
      box-shadow: var(--shadow-sm);
    }
    .practice-q-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
    }
    .practice-q-num {
      font-size: 1.08rem;
      font-weight: 800;
      color: var(--navy-dark);
    }
    .practice-q-marks {
      background: var(--accent-light);
      border: 1px solid var(--accent-border);
      color: var(--accent);
      font-size: 0.8rem;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: var(--radius-full);
    }
    .practice-q-stem {
      font-size: 1.02rem;
      line-height: 1.65;
      color: var(--text-primary);
      margin-bottom: 18px;
    }
    .working-scratchpad-area {
      margin-bottom: 16px;
    }
    .working-scratchpad-label {
      display: block;
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--text-secondary);
      margin-bottom: 6px;
    }
    .working-scratchpad-input {
      width: 100%;
      min-height: 85px;
      padding: 12px 16px;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      background: var(--bg-page);
      font-family: inherit;
      font-size: 0.92rem;
      color: var(--text-primary);
      resize: vertical;
      box-sizing: border-box;
      transition: border-color 0.2s ease;
    }
    .working-scratchpad-input:focus {
      outline: none;
      border-color: var(--accent);
      background: #ffffff;
    }
    .practice-q-toolbar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }
    .btn-reveal-solution {
      background: var(--navy-dark);
      color: #ffffff;
      border: none;
      padding: 9px 18px;
      border-radius: var(--radius-md);
      font-weight: 700;
      font-size: 0.88rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }
    .btn-reveal-solution:hover {
      background: var(--navy-soft);
    }
    .solution-drawer {
      margin-top: 20px;
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      border-radius: var(--radius-md);
      padding: 20px;
      display: none;
      animation: slideDown 0.25s ease;
    }
    .solution-drawer.open {
      display: block;
    }
    @keyframes slideDown {
      from { opacity: 0; transform: translateY(-8px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .solution-drawer-title {
      font-weight: 800;
      color: #166534;
      font-size: 1rem;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .self-marking-bar {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-top: 16px;
      padding-top: 14px;
      border-top: 1px dashed #bbf7d0;
    }
    .btn-mark-eval {
      padding: 6px 12px;
      border-radius: var(--radius-sm);
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
      border: 1px solid transparent;
      transition: all 0.15s ease;
    }
    .btn-eval-success {
      background: #dcfce7;
      color: #166534;
      border-color: #86efac;
    }
    .btn-eval-success:hover {
      background: #bbf7d0;
    }
    .btn-eval-retry {
      background: #fee2e2;
      color: #991b1b;
      border-color: #fca5a5;
    }
    .btn-eval-retry:hover {
      background: #fecaca;
    }

    /* DOWNLOADS TILES */
    .download-tiles-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }
    @media (max-width: 600px) {
      .download-tiles-grid {
        grid-template-columns: 1fr;
      }
    }
    .download-tile-card {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 22px;
      display: flex;
      align-items: center;
      gap: 16px;
      text-decoration: none;
      transition: all 0.2s ease;
    }
    .download-tile-card:hover {
      border-color: var(--accent);
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
    }
    .download-tile-icon {
      width: 50px;
      height: 50px;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.5rem;
      flex-shrink: 0;
    }
    .icon-pdf { background: #fee2e2; color: #dc2626; }
    .icon-answers { background: #dcfce7; color: #16a34a; }
    .download-tile-info strong {
      display: block;
      color: var(--navy-dark);
      font-size: 0.98rem;
      margin-bottom: 3px;
    }
    .download-tile-info span {
      font-size: 0.82rem;
      color: var(--text-muted);
    }

    /* REVISION CARDS SHOWCASE */
    .revision-cards-showcase-box {
      background: linear-gradient(135deg, #070d1e 0%, #172554 100%);
      color: #ffffff;
      border-radius: var(--radius-lg);
      padding: 36px;
      display: grid;
      grid-template-columns: 1fr 1.2fr;
      gap: 32px;
      align-items: center;
      border: 1px solid rgba(255, 255, 255, 0.15);
      box-shadow: var(--shadow-lg);
    }
    @media (max-width: 768px) {
      .revision-cards-showcase-box {
        grid-template-columns: 1fr;
        text-align: center;
      }
    }
    .cards-showcase-text h3 {
      font-size: 1.6rem;
      font-weight: 800;
      color: #ffffff;
      margin-bottom: 10px;
    }
    .cards-showcase-text p {
      color: #cbd5e1;
      font-size: 0.95rem;
      line-height: 1.6;
      margin-bottom: 20px;
    }
    .btn-cards-order-now {
      background: #f59e0b;
      color: #070d1e;
      font-weight: 800;
      padding: 12px 24px;
      border-radius: var(--radius-md);
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }
    .btn-cards-order-now:hover {
      background: #d97706;
      color: #ffffff;
    }
    .cards-showcase-visual img {
      max-width: 100%;
      height: auto;
      max-height: 240px;
      filter: drop-shadow(0 15px 30px rgba(0, 0, 0, 0.5));
    }
  </style>
</head>
<body>

  <!-- TOP TRUST BAR WITH DYSLEXIA TINT PICKER -->
  <div class="mfs-top-bar">
    <div class="mfs-container mfs-top-bar-inner">
      <div class="top-trust-items">
        <span class="top-trust-item"><i class="fa-solid fa-building-columns"></i> Pearson Edexcel & City & Guilds Aligned</span>
      </div>
      <div class="top-contacts">
        <div class="mfs-access-bar">
          <!-- DYSLEXIA BACKGROUND TINT PICKER -->
          <div class="mfs-tint-dropdown-wrap">
            <button type="button" id="tintToggle" class="btn-tint-toggle" onclick="toggleTintMenu(event)" title="Change dyslexia background tint or remove tint">
              <span class="tint-swatch-indicator" id="tintCurrentSwatch"></span>
              <span id="tintLabel">Cream Tint</span>
              <i class="fa-solid fa-chevron-down" style="font-size:0.62rem; opacity:0.75; margin-left:2px;"></i>
            </button>
            <div id="tintMenu" class="tint-picker-menu">
              <div class="tint-picker-title"><i class="fa-solid fa-glasses"></i> Dyslexia Reading Tint</div>
              <button type="button" class="tint-option-btn active" data-tint="cream" onclick="setSiteTint('cream', event)">
                <span class="swatch swatch-cream"></span>
                <span class="tint-name">Cream <small class="tint-badge-def">Default</small></span>
                <i class="fa-solid fa-check check-icon"></i>
              </button>
              <button type="button" class="tint-option-btn" data-tint="peach" onclick="setSiteTint('peach', event)">
                <span class="swatch swatch-peach"></span>
                <span class="tint-name">Soft Peach</span>
                <i class="fa-solid fa-check check-icon"></i>
              </button>
              <button type="button" class="tint-option-btn" data-tint="cool" onclick="setSiteTint('cool', event)">
                <span class="swatch swatch-cool"></span>
                <span class="tint-name">Cool Mist</span>
                <i class="fa-solid fa-check check-icon"></i>
              </button>
              <button type="button" class="tint-option-btn" data-tint="sage" onclick="setSiteTint('sage', event)">
                <span class="swatch swatch-sage"></span>
                <span class="tint-name">Soft Sage</span>
                <i class="fa-solid fa-check check-icon"></i>
              </button>
              <div class="tint-divider"></div>
              <button type="button" class="tint-option-btn" data-tint="none" onclick="setSiteTint('none', event)">
                <span class="swatch swatch-none"></span>
                <span class="tint-name">No Tint (White)</span>
                <i class="fa-solid fa-check check-icon"></i>
              </button>
            </div>
          </div>
          <button type="button" class="btn-dyslexia-toggle" onclick="openGlobalSearch()" title="Search topics (Ctrl+K)">
            <i class="fa-solid fa-magnifying-glass"></i> Search
          </button>
          <button id="dyslexiaToggle" class="btn-dyslexia-toggle" onclick="toggleDyslexiaMode()" title="Toggle Dyslexia High-Readability Mode">
            <i class="fa-solid fa-universal-access"></i> Dyslexia
          </button>
          <button id="themeToggle" class="mfs-theme-pill" onclick="toggleTheme()" title="Switch Palette: Sapphire vs Emerald">
            <i class="fa-solid fa-palette"></i> <span id="themeLabel">Sapphire</span>
          </button>
        </div>
        <a href="tel:020XXXXXXXX" class="top-contact-link"><i class="fa-solid fa-phone"></i> <strong>020 XXXX XXXX</strong></a>
        <a href="https://wa.me/447564525425" target="_blank" rel="noopener" class="top-contact-link"><i class="fa-brands fa-whatsapp"></i> <strong>+44 (0)7564 525425</strong></a>
      </div>
    </div>
  </div>

  <!-- MAIN NAVIGATION -->
  <!-- MAIN NAVIGATION -->
  <header class="mfs-navbar">
    <div class="revision-page-wrapper mfs-navbar-inner">
      <a href="index.html" class="mfs-brand">
        <div class="mfs-brand-icon"><i class="fa-solid fa-graduation-cap"></i></div>
        <div class="mfs-brand-text">
          <div class="mfs-brand-title">MASTER<span>FUNCTIONALSKILLS</span></div>
          <div class="mfs-brand-subtitle">Delivering Skills • Achieving Goals</div>
        </div>
      </a>

      <nav class="mfs-nav-wrapper">
        <ul class="mfs-nav-menu">
          <li class="mfs-nav-item">
            <a href="functional-skills-maths-level-2.html" class="mfs-nav-link"><i class="fa-solid fa-calculator" style="color:#0284c7; margin-right:5px;"></i> Maths <i class="fa-solid fa-chevron-down" style="font-size:0.72rem; margin-left:3px;"></i></a>
            <div class="mfs-dropdown-menu mfs-dropdown-compact">
              <a href="functional-skills-maths-level-2.html" class="mfs-dropdown-item">Maths Level 2</a>
              <a href="functional-skills-maths-level-1.html" class="mfs-dropdown-item">Maths Level 1</a>
              <a href="entry-level-3-maths.html" class="mfs-dropdown-item">Entry Level 3 Maths</a>
              <div class="mfs-dropdown-divider" style="margin:4px 0; border-top:1px solid #e2e8f0;"></div>
              <a href="pass-mark-calculator.html" class="mfs-dropdown-item"><i class="fa-solid fa-calculator" style="color:var(--accent); font-size:0.85rem; margin-right:6px;"></i> Pass Mark Calculator</a>
              <a href="diagnostic-test.html" class="mfs-dropdown-item"><i class="fa-solid fa-chart-pie" style="color:#059669; font-size:0.85rem; margin-right:6px;"></i> Diagnostic Test</a>
              <a href="functional-skills-nets.html" class="mfs-dropdown-item"><i class="fa-solid fa-cube" style="color:#0284c7; font-size:0.85rem; margin-right:6px;"></i> 3D Net Folder</a>
            </div>
          </li>
          <li class="mfs-nav-item">
            <a href="functional-skills-english-level-2.html" class="mfs-nav-link"><i class="fa-solid fa-pen-nib" style="color:#0284c7; margin-right:5px;"></i> English <i class="fa-solid fa-chevron-down" style="font-size:0.72rem; margin-left:3px;"></i></a>
            <div class="mfs-dropdown-menu mfs-dropdown-compact">
              <a href="functional-skills-english-level-2.html" class="mfs-dropdown-item">English Level 2</a>
              <a href="functional-skills-english-level-1.html" class="mfs-dropdown-item">English Level 1</a>
              <div class="mfs-dropdown-divider" style="margin:4px 0; border-top:1px solid #e2e8f0;"></div>
              <a href="pass-mark-calculator.html#english" class="mfs-dropdown-item"><i class="fa-solid fa-calculator" style="color:var(--accent); font-size:0.85rem; margin-right:6px;"></i> Pass Mark Calculator</a>
              <a href="diagnostic-test.html" class="mfs-dropdown-item"><i class="fa-solid fa-chart-pie" style="color:#059669; font-size:0.85rem; margin-right:6px;"></i> Diagnostic Test</a>
            </div>
          </li>
          <li class="mfs-nav-item">
            <a href="digital-functional-skills.html" class="mfs-nav-link"><i class="fa-solid fa-laptop-code" style="color:#0284c7; margin-right:5px;"></i> Digital Skills <i class="fa-solid fa-chevron-down" style="font-size:0.72rem; margin-left:3px;"></i></a>
            <div class="mfs-dropdown-menu mfs-dropdown-compact">
              <a href="digital-functional-skills.html" class="mfs-dropdown-item">Digital Skills Hub</a>
              <a href="digital-functional-skills-mock-exam.html" class="mfs-dropdown-item"><i class="fa-solid fa-laptop-code" style="color:#2563eb; font-size:0.85rem; margin-right:6px;"></i> Pearson Mock Simulator</a>
              <a href="digital-functional-skills-past-papers.html" class="mfs-dropdown-item">Past Papers &amp; Data Files</a>
            </div>
          </li>
          <li class="mfs-nav-item">
            <a href="pass-mark-calculator.html" class="mfs-nav-link"><i class="fa-solid fa-screwdriver-wrench" style="color:#0284c7; margin-right:5px;"></i> Tools <i class="fa-solid fa-chevron-down" style="font-size:0.72rem; margin-left:3px;"></i></a>
            <div class="mfs-dropdown-menu mfs-dropdown-compact">
              <a href="pass-mark-calculator.html" class="mfs-dropdown-item"><i class="fa-solid fa-calculator" style="color:var(--accent); font-size:0.85rem; margin-right:6px;"></i> Pass Mark Calculator</a>
              <a href="diagnostic-test.html" class="mfs-dropdown-item"><i class="fa-solid fa-chart-pie" style="color:#059669; font-size:0.85rem; margin-right:6px;"></i> Diagnostic Skill Checker</a>
              <a href="digital-functional-skills-mock-exam.html" class="mfs-dropdown-item"><i class="fa-solid fa-laptop-code" style="color:#2563eb; font-size:0.85rem; margin-right:6px;"></i> Pearson Exam Simulator</a>
              <a href="bksb-remediation.html" class="mfs-dropdown-item"><i class="fa-solid fa-arrows-split-up-and-left" style="color:#8b5cf6; font-size:0.85rem; margin-right:6px;"></i> BKSB Remediation Bridge</a>
              <a href="functional-skills-nets.html" class="mfs-dropdown-item"><i class="fa-solid fa-cube" style="color:#0284c7; font-size:0.85rem; margin-right:6px;"></i> 3D Net Folding Tool</a>
            </div>
          </li>
          <li class="mfs-nav-item"><a href="tutors.html" class="mfs-nav-link"><i class="fa-solid fa-chalkboard-user" style="color:#0284c7; margin-right:5px;"></i> Tutor Hub</a></li>
          <li class="mfs-nav-item">
            <a href="functional-skills-past-papers.html" class="mfs-nav-link"><i class="fa-regular fa-file-lines" style="color:#0284c7; margin-right:5px;"></i> Past Papers <i class="fa-solid fa-chevron-down" style="font-size:0.72rem; margin-left:3px;"></i></a>
            <div class="mfs-dropdown-menu mfs-dropdown-compact">
              <a href="functional-skills-past-papers.html" class="mfs-dropdown-item">All Past Papers Hub</a>
              <a href="edexcel-functional-skills-maths-level-2-past-papers.html" class="mfs-dropdown-item">Pearson Edexcel Papers</a>
              <a href="pass-mark-calculator.html" class="mfs-dropdown-item"><i class="fa-solid fa-calculator" style="color:var(--accent); font-size:0.85rem; margin-right:6px;"></i> Grade Boundaries Calculator</a>
            </div>
          </li>
          <li class="mfs-nav-item"><a href="revision-cards.html" class="mfs-nav-link mfs-nav-link-amber" style="color:#f59e0b; font-weight:700;"><i class="fa-solid fa-layer-group" style="color:#f59e0b; margin-right:5px;"></i> Revision Cards</a></li>
          <li class="mfs-nav-item"><a href="shop.html" class="mfs-nav-link mfs-nav-link-amber" style="color:#f59e0b; font-weight:700;"><i class="fa-solid fa-basket-shopping" style="color:#f59e0b; margin-right:5px;"></i> Shop</a></li>
        </ul>
      </nav>

      <div class="mfs-nav-actions">
        <a href="functional-skills-exam.html" class="btn-nav-exam"><i class="fa-solid fa-calendar-check"></i> Book Exam</a>
      </div>
    </div>
  </header>

  <!-- BREADCRUMBS -->
  <div class="revision-breadcrumb-bar">
    <div class="mfs-container">
      <div class="revision-breadcrumbs">
        <a href="index.html"><i class="fa-solid fa-house"></i> Home</a>
        <i class="fa-solid fa-chevron-right"></i>
        <a href="revise.html">Revise Hub</a>
        <i class="fa-solid fa-chevron-right"></i>
        <a href="functional-skills-maths-level-2.html">Maths Level 2</a>
        <i class="fa-solid fa-chevron-right"></i>
        <span>Measures, Shape & Space</span>
        <i class="fa-solid fa-chevron-right"></i>
        <span class="current">Area Revision</span>
      </div>
    </div>
  </div>

  <!-- HERO SECTION -->
  <section class="revision-hero-card">
    <div class="mfs-container">
      <div class="revision-hero-pill-row">
        <span class="badge-pill-accent"><i class="fa-solid fa-calculator"></i> MATHEMATICS</span>
        <span class="badge-pill-gold">LEVEL 1 &amp; LEVEL 2</span>
        <span class="badge-pill-outline">OFQUAL SPECIFICATION: MEASURES, SHAPE &amp; SPACE</span>
      </div>

      <h1 class="revision-hero-title">
        Functional Skills Area: <span>Formulas, Models &amp; Exam Practice</span>
      </h1>

      <p class="revision-hero-desc">
        Master calculating 2D surface area across rectangles, triangles, parallelograms, trapeziums, and compound L-shapes. Learn to solve multi-step workplace problems including flooring coverage, lawn turf, paint quantities, and material wastage calibrated to Pearson Edexcel &amp; City &amp; Guilds standards.
      </p>

      <div class="revision-hero-meta-bar">
        <div class="hero-meta-item">
          <i class="fa-solid fa-clock"></i> <strong>Est. Study Time:</strong> 25-35 Mins
        </div>
        <div class="hero-meta-item">
          <i class="fa-solid fa-book-open"></i> <strong>Curriculum Standards:</strong> Pearson L1 (18-19) &bull; L2 (19-20)
        </div>
        <div class="hero-meta-item">
          <i class="fa-solid fa-circle-check"></i> <strong>4 Interactive Exam Practice Tasks</strong>
        </div>

        <div class="hero-quick-actions">
          <a href="#downloads" class="btn-hero-dl">
            <i class="fa-regular fa-file-pdf"></i> Free Worksheet &amp; Answers
          </a>
          <a href="shop.html" class="btn-hero-cards">
            <i class="fa-solid fa-layer-group"></i> Revision Cards (£12.99)
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- MOBILE TABLE OF CONTENTS BAR -->
  <div class="mobile-toc-bar">
    <div style="font-weight:700; color:var(--navy-dark); font-size:0.9rem;">
      <i class="fa-solid fa-list-check" style="color:var(--accent);"></i> Area Revision Blueprint
    </div>
    <button type="button" class="btn-mobile-toc" onclick="toggleMobileToc()">
      <span>Table of Contents</span> <i class="fa-solid fa-bars"></i>
    </button>
  </div>

  <!-- MAIN 2-COLUMN LAYOUT -->
  <main class="mfs-container">
    <div class="revision-layout">

      <!-- ============================================== -->
      <!-- LEFT COLUMN: STICKY BLUEPRINT / TABLE OF CONTENTS -->
      <!-- ============================================== -->
      <aside class="revision-sidebar" id="sidebarNav">
        <div class="sidebar-toc-title">
          <span><i class="fa-solid fa-compass-drafting" style="color:var(--accent);"></i> Topic Blueprint</span>
          <span style="font-size:0.75rem; color:var(--text-muted); font-weight:600;">8 Sections</span>
        </div>

        <ul class="sidebar-toc-list" id="tocList">
          <li>
            <a href="#specification" class="sidebar-toc-link active">
              <i class="fa-solid fa-clipboard-check"></i> Specification &amp; Standards
            </a>
          </li>
          <li>
            <a href="#golden-rules" class="sidebar-toc-link">
              <i class="fa-solid fa-lightbulb"></i> Golden Rules &amp; Formulas
              <span class="sidebar-toc-badge">Must Know</span>
            </a>
          </li>
          <li>
            <a href="#skill-rectangles" class="sidebar-toc-link">
              <i class="fa-solid fa-vector-square"></i> Squares &amp; Rectangles
            </a>
          </li>
          <li>
            <a href="#skill-triangles" class="sidebar-toc-link">
              <i class="fa-solid fa-play" style="transform: rotate(-90deg);"></i> Triangles
            </a>
          </li>
          <li>
            <a href="#skill-trapeziums" class="sidebar-toc-link">
              <i class="fa-solid fa-draw-polygon"></i> Parallelograms &amp; Trapeziums
            </a>
          </li>
          <li>
            <a href="#skill-compound" class="sidebar-toc-link">
              <i class="fa-solid fa-shapes"></i> Compound L-Shapes
            </a>
          </li>
          <li>
            <a href="#worked-models" class="sidebar-toc-link">
              <i class="fa-solid fa-file-signature"></i> Worked Exam Models
              <span class="sidebar-toc-badge" style="background:#dcfce7; color:#166534;">M1 / A1</span>
            </a>
          </li>
          <li>
            <a href="#examiner-traps" class="sidebar-toc-link">
              <i class="fa-solid fa-triangle-exclamation"></i> Common Examiner Traps
              <span class="sidebar-toc-badge" style="background:#fee2e2; color:#991b1b;">Lost Marks</span>
            </a>
          </li>
          <li>
            <a href="#practice-questions" class="sidebar-toc-link">
              <i class="fa-solid fa-pencil"></i> Interactive Exam Practice
            </a>
          </li>
          <li>
            <a href="#downloads" class="sidebar-toc-link">
              <i class="fa-regular fa-file-pdf"></i> Printable Worksheet &amp; Answers
            </a>
          </li>
          <li>
            <a href="#revision-cards" class="sidebar-toc-link">
              <i class="fa-solid fa-layer-group"></i> Pocket Revision Cards
            </a>
          </li>
        </ul>

        <!-- Sidebar Revision Card Promo -->
        <div class="sidebar-cards-promo">
          <img src="assets/img/books/flashcards_maths_l2.svg" alt="Maths Level 2 Revision Cards Deck">
          <h4>Need Portable Revision?</h4>
          <p>Condense all 39 Maths Level 2 formulas and trap warnings into high-gloss pocket revision cards.</p>
          <a href="shop.html" class="btn-sidebar-shop">
            <i class="fa-solid fa-basket-shopping"></i> Order Revision Cards (£12.99)
          </a>
        </div>
      </aside>

      <!-- ============================================== -->
      <!-- RIGHT COLUMN: MAIN EDUCATIONAL REVISION CONTENT -->
      <!-- ============================================== -->
      <div class="revision-content">

        <!-- 1. SPECIFICATION & LEARNING OBJECTIVES -->
        <section id="specification" class="revision-section">
          <div class="section-header-row">
            <h2 class="section-title"><i class="fa-solid fa-clipboard-check"></i> Specification &amp; Learning Outcomes</h2>
          </div>
          <p class="section-lead-text">
            Area questions assess your ability to measure the two-dimensional space occupied by flat surfaces, carpets, garden lawns, tiles, and walls. Below are the exact requirements regulated by Ofqual for Pearson Edexcel and City &amp; Guilds examinations.
          </p>

          <div class="theory-card-blue">
            <div style="display:grid; grid-template-columns: 1fr 1fr; gap:20px;">
              <div>
                <h4 style="font-size:1.02rem; font-weight:800; color:var(--navy-dark); margin-bottom:10px; display:flex; align-items:center; gap:8px;">
                  <span style="background:#e0e7ff; color:#3730a3; padding:2px 8px; border-radius:4px; font-size:0.75rem;">LEVEL 1</span> Core Outcomes
                </h4>
                <ul style="padding-left:18px; margin:0; font-size:0.92rem; color:var(--text-secondary); line-height:1.65;">
                  <li>Find the area of rectangles and squares using \( \text{Length} \times \text{Width} \)</li>
                  <li>Use appropriate metric area units: \( \text{cm}^2 \), \( \text{m}^2 \), and \( \text{mm}^2 \)</li>
                  <li>Calculate simple rectangular compound shapes by addition</li>
                  <li>Solve 1-step practical flooring and turfing cost tasks</li>
                </ul>
              </div>
              <div>
                <h4 style="font-size:1.02rem; font-weight:800; color:var(--navy-dark); margin-bottom:10px; display:flex; align-items:center; gap:8px;">
                  <span style="background:#fef3c7; color:#92400e; padding:2px 8px; border-radius:4px; font-size:0.75rem;">LEVEL 2</span> Advanced Outcomes
                </h4>
                <ul style="padding-left:18px; margin:0; font-size:0.92rem; color:var(--text-secondary); line-height:1.65;">
                  <li>Calculate the area of triangles using \( \frac{1}{2} \times \text{base} \times \text{perpendicular height} \)</li>
                  <li>Calculate trapeziums: \( \text{Area} = \frac{a + b}{2} \times h \)</li>
                  <li>Calculate complex multi-shape compound areas (L, T, and U shapes)</li>
                  <li>Multi-step problems: paint coverage, tile pack rounding, and 10% wastage</li>
                </ul>
              </div>
            </div>
          </div>
        </section>

        <!-- 2. GOLDEN RULES & CORE FORMULAS -->
        <section id="golden-rules" class="revision-section">
          <div class="section-header-row">
            <h2 class="section-title"><i class="fa-solid fa-lightbulb"></i> Golden Rules &amp; Essential Formulas</h2>
          </div>
          <p class="section-lead-text">
            Commit these golden principles to memory before entering the examination. Most lost marks on area questions are due to unit mismatches or confusing perimeter with area.
          </p>

          <!-- Golden Rule 1: Perimeter vs Area -->
          <div class="rule-card-amber">
            <div class="rule-card-amber-header">
              <i class="fa-solid fa-ruler-combined"></i>
              <span>Golden Rule 1: Never Confuse Perimeter and Area</span>
            </div>
            <p>
              <strong>Perimeter</strong> is the <em>one-dimensional distance</em> around the outside edge (measured in \( \text{cm} \), \( \text{m} \)). <br>
              <strong>Area</strong> is the <em>two-dimensional flat surface</em> inside the boundary (always measured in <strong>square units</strong>: \( \text{cm}^2 \), \( \text{m}^2 \)).
            </p>
            <div class="rule-formula-box">
              Always state area units with a square index: \( \text{cm}^2 \) or \( \text{m}^2 \)
            </div>
          </div>

          <!-- Golden Rule 2: Matching Units -->
          <div class="rule-card-amber">
            <div class="rule-card-amber-header">
              <i class="fa-solid fa-arrows-split-up-and-left"></i>
              <span>Golden Rule 2: Convert All Dimensions to the SAME Unit First</span>
            </div>
            <p>
              Examiners deliberately mix metres and centimetres in the same question (e.g., length = \( 3.5\,\text{m} \), width = \( 80\,\text{cm} \)). You must convert both to metres (\( 80\,\text{cm} = 0.8\,\text{m} \)) <em>before</em> multiplying. Multiplying \( 3.5 \times 80 \) gives \( 280\,\text{m}^2 \), which is wrong by a factor of 100!
            </p>
            <div class="rule-formula-box">
              Rule: \( 1\,\text{m} = 100\,\text{cm} \quad \implies \quad 80\,\text{cm} \div 100 = 0.8\,\text{m} \)
            </div>
          </div>

          <!-- Golden Rule 3: Triangle Perpendicular Height -->
          <div class="rule-card-amber">
            <div class="rule-card-amber-header">
              <i class="fa-solid fa-triangle-exclamation"></i>
              <span>Golden Rule 3: For Triangles, Use Perpendicular Height (Never the Slant)</span>
            </div>
            <p>
              The height must make a strict \( 90^\circ \) right angle with the base. Never use the slanted hypotenuse side for area calculations.
            </p>
            <div class="rule-formula-box">
              Triangle Area = \( \frac{1}{2} \times \text{base} \times \text{vertical height} \)
            </div>
          </div>

          <!-- Golden Rule 4: Trapezium Parallel Sides -->
          <div class="rule-card-amber">
            <div class="rule-card-amber-header">
              <i class="fa-solid fa-draw-polygon"></i>
              <span>Golden Rule 4: Average the Parallel Sides First for Trapeziums</span>
            </div>
            <p>
              Identify the two sides that run parallel to each other (\( a \) and \( b \)). Add them together, divide by 2 to find their average, then multiply by the vertical distance (\( h \)) between them.
            </p>
            <div class="rule-formula-box">
              Trapezium Area = \( \left(\frac{a + b}{2}\right) \times h \)
            </div>
          </div>
        </section>

        <!-- 3. SKILL 1: SQUARES & RECTANGLES -->
        <section id="skill-rectangles" class="revision-section">
          <div class="section-header-row">
            <h2 class="section-title"><i class="fa-solid fa-vector-square"></i> Skill 1: Area of Squares &amp; Rectangles</h2>
          </div>
          <p class="section-lead-text">
            The foundation of 2D geometry. To find the surface area of any rectangular space, multiply its length by its width.
          </p>

          <div class="theory-card-blue">
            <div class="theory-grid-2col">
              <div>
                <h4 style="font-weight:800; color:var(--navy-dark); font-size:1.15rem; margin-bottom:8px;">Standard Formula:</h4>
                <div style="background:#eff6ff; border:1px solid #bfdbfe; padding:12px 18px; border-radius:8px; font-weight:800; font-size:1.25rem; color:#1d4ed8; margin-bottom:14px;">
                  \( \text{Area} = \text{Length} \times \text{Width} \)
                </div>
                <p style="color:var(--text-secondary); font-size:0.92rem; line-height:1.6; margin-bottom:12px;">
                  <strong>Example:</strong> A hospital consultation room measures \( 6.5\,\text{m} \) long and \( 4\,\text{m} \) wide.
                </p>
                <div style="background:#f8fafc; border-left:3px solid var(--accent); padding:10px 14px; font-size:0.92rem; color:var(--text-primary); margin-bottom:10px;">
                  \( \text{Area} = 6.5 \times 4 = 26\,\text{m}^2 \)
                </div>
                <p style="font-size:0.85rem; color:var(--text-muted);">
                  <i class="fa-solid fa-circle-info" style="color:var(--accent);"></i> For a square, both dimensions are equal: \( \text{Area} = \text{side}^2 \).
                </p>
              </div>

              <div class="shape-diagram-box">
                <svg viewBox="0 0 280 160" width="280" height="160">
                  <rect x="25" y="25" width="210" height="110" fill="#dbeafe" stroke="#2563eb" stroke-width="2.5" rx="4"/>
                  <!-- Dimensions -->
                  <text x="130" y="18" font-family="sans-serif" font-size="12" font-weight="700" fill="#1e3a8a" text-anchor="middle">Length = 6.5 m</text>
                  <text x="245" y="85" font-family="sans-serif" font-size="12" font-weight="700" fill="#1e3a8a" text-anchor="start">Width = 4 m</text>
                  <!-- Inner Text -->
                  <text x="130" y="80" font-family="sans-serif" font-size="14" font-weight="800" fill="#1e40af" text-anchor="middle">Area = 6.5 × 4</text>
                  <text x="130" y="100" font-family="sans-serif" font-size="16" font-weight="900" fill="#1e3a8a" text-anchor="middle">= 26 m²</text>
                </svg>
              </div>
            </div>
          </div>
        </section>

        <!-- 4. SKILL 2: TRIANGLES -->
        <section id="skill-triangles" class="revision-section">
          <div class="section-header-row">
            <h2 class="section-title"><i class="fa-solid fa-play" style="transform: rotate(-90deg);"></i> Skill 2: Area of Triangles</h2>
          </div>
          <p class="section-lead-text">
            A triangle is always exactly <strong>half of a rectangle</strong> with the same base and height. That is why you must always divide by 2.
          </p>

          <div class="theory-card-blue">
            <div class="theory-grid-2col">
              <div>
                <h4 style="font-weight:800; color:var(--navy-dark); font-size:1.15rem; margin-bottom:8px;">Standard Formula:</h4>
                <div style="background:#eff6ff; border:1px solid #bfdbfe; padding:12px 18px; border-radius:8px; font-weight:800; font-size:1.25rem; color:#1d4ed8; margin-bottom:14px;">
                  \( \text{Area} = \frac{\text{Base} \times \text{Height}}{2} \)
                </div>
                <p style="color:var(--text-secondary); font-size:0.92rem; line-height:1.6; margin-bottom:12px;">
                  <strong>Example:</strong> A triangular gable roof end has a base of \( 8\,\text{m} \) and a vertical peak height of \( 3.5\,\text{m} \).
                </p>
                <div style="background:#f8fafc; border-left:3px solid var(--accent); padding:10px 14px; font-size:0.92rem; color:var(--text-primary); margin-bottom:10px;">
                  \( \text{Area} = \frac{8 \times 3.5}{2} = \frac{28}{2} = 14\,\text{m}^2 \)
                </div>
                <div style="background:#fef2f2; border:1px solid #fecaca; border-radius:6px; padding:8px 12px; font-size:0.82rem; color:#991b1b;">
                  <strong>Common Exam Trap:</strong> Candidates often forget to divide by 2 and write \( 28\,\text{m}^2 \), losing the final accuracy mark!
                </div>
              </div>

              <div class="shape-diagram-box">
                <svg viewBox="0 0 280 160" width="280" height="160">
                  <!-- Triangle -->
                  <polygon points="30,130 250,130 140,25" fill="#fef3c7" stroke="#d97706" stroke-width="2.5"/>
                  <!-- Vertical Perpendicular Height Dotted Line -->
                  <line x1="140" y1="25" x2="140" y2="130" stroke="#b45309" stroke-width="1.8" stroke-dasharray="4"/>
                  <!-- Right angle square -->
                  <rect x="140" y="118" width="12" height="12" fill="none" stroke="#b45309" stroke-width="1.2"/>
                  <!-- Dimension labels -->
                  <text x="140" y="148" font-family="sans-serif" font-size="12" font-weight="700" fill="#78350f" text-anchor="middle">Base = 8 m</text>
                  <text x="148" y="75" font-family="sans-serif" font-size="11" font-weight="700" fill="#b45309">Height = 3.5 m</text>
                  <!-- Formula inside -->
                  <text x="80" y="90" font-family="sans-serif" font-size="13" font-weight="800" fill="#92400e">(8 × 3.5) ÷ 2</text>
                  <text x="80" y="108" font-family="sans-serif" font-size="15" font-weight="900" fill="#78350f">= 14 m²</text>
                </svg>
              </div>
            </div>
          </div>
        </section>

        <!-- 5. SKILL 3: PARALLELOGRAMS & TRAPEZIUMS -->
        <section id="skill-trapeziums" class="revision-section">
          <div class="section-header-row">
            <h2 class="section-title"><i class="fa-solid fa-draw-polygon"></i> Skill 3: Parallelograms &amp; Trapeziums</h2>
          </div>
          <p class="section-lead-text">
            Trapezium questions appear frequently in Level 2 calculator papers. The key is identifying the two parallel sides and taking their mean.
          </p>

          <div class="theory-card-blue">
            <div class="theory-grid-2col">
              <div>
                <h4 style="font-weight:800; color:var(--navy-dark); font-size:1.15rem; margin-bottom:8px;">Trapezium Formula:</h4>
                <div style="background:#eff6ff; border:1px solid #bfdbfe; padding:12px 18px; border-radius:8px; font-weight:800; font-size:1.2rem; color:#1d4ed8; margin-bottom:14px;">
                  \( \text{Area} = \left(\frac{a + b}{2}\right) \times h \)
                </div>
                <p style="color:var(--text-secondary); font-size:0.92rem; line-height:1.6; margin-bottom:10px;">
                  <strong>Example:</strong> A garden patio is shaped like a trapezium with parallel sides \( a = 6\,\text{m} \) and \( b = 10\,\text{m} \), and perpendicular height \( h = 5\,\text{m} \).
                </p>
                <div style="background:#f8fafc; border-left:3px solid var(--accent); padding:10px 14px; font-size:0.92rem; color:var(--text-primary); margin-bottom:10px;">
                  <strong>Step 1:</strong> Average parallel sides: \( \frac{6 + 10}{2} = \frac{16}{2} = 8\,\text{m} \)<br>
                  <strong>Step 2:</strong> Multiply by height: \( 8 \times 5 = 40\,\text{m}^2 \)
                </div>
              </div>

              <div class="shape-diagram-box">
                <svg viewBox="0 0 280 160" width="280" height="160">
                  <!-- Trapezium -->
                  <polygon points="60,30 200,30 250,130 30,130" fill="#e0e7ff" stroke="#4338ca" stroke-width="2.5"/>
                  <!-- Height Dotted Line -->
                  <line x1="60" y1="30" x2="60" y2="130" stroke="#4338ca" stroke-width="1.8" stroke-dasharray="4"/>
                  <rect x="60" y="118" width="12" height="12" fill="none" stroke="#4338ca" stroke-width="1.2"/>
                  <!-- Labels -->
                  <text x="130" y="22" font-family="sans-serif" font-size="12" font-weight="700" fill="#312e81" text-anchor="middle">Top (a) = 6 m</text>
                  <text x="140" y="148" font-family="sans-serif" font-size="12" font-weight="700" fill="#312e81" text-anchor="middle">Bottom (b) = 10 m</text>
                  <text x="70" y="85" font-family="sans-serif" font-size="11" font-weight="700" fill="#4338ca">h = 5 m</text>
                  <!-- Calculation text -->
                  <text x="155" y="80" font-family="sans-serif" font-size="13" font-weight="800" fill="#3730a3">((6 + 10) ÷ 2) × 5</text>
                  <text x="155" y="100" font-family="sans-serif" font-size="16" font-weight="900" fill="#1e1b4b">= 40 m²</text>
                </svg>
              </div>
            </div>
          </div>
        </section>

        <!-- 6. SKILL 4: COMPOUND L-SHAPES -->
        <section id="skill-compound" class="revision-section">
          <div class="section-header-row">
            <h2 class="section-title"><i class="fa-solid fa-shapes"></i> Skill 4: Compound Shapes (L-Shapes &amp; Cut-Outs)</h2>
          </div>
          <p class="section-lead-text">
            Compound shapes are formed by combining two or more basic shapes. The foolproof exam technique is to <strong>split the shape</strong> with a neat dotted line and calculate each section independently.
          </p>

          <div class="theory-card-blue">
            <div class="theory-grid-2col">
              <div>
                <h4 style="font-weight:800; color:var(--navy-dark); font-size:1.15rem; margin-bottom:8px;">Stepped Split Method:</h4>
                <ol style="padding-left:18px; margin:0 0 14px 0; font-size:0.92rem; color:var(--text-secondary); line-height:1.65;">
                  <li><strong>Find missing sides:</strong> Opposite sides must balance (e.g. \( 11\,\text{m} - 4\,\text{m} = 7\,\text{m} \)).</li>
                  <li><strong>Draw a split line:</strong> Divide the L-shape into Rectangle A and Rectangle B.</li>
                  <li><strong>Calculate both areas:</strong> Multiply length by width for each.</li>
                  <li><strong>Sum the total:</strong> Add Area A + Area B.</li>
                </ol>
                <div style="background:#eff6ff; border-left:3px solid var(--accent); padding:10px 14px; font-size:0.9rem; color:var(--navy-dark);">
                  <strong>Rectangle A:</strong> \( 7\,\text{m} \times 4\,\text{m} = 28\,\text{m}^2 \)<br>
                  <strong>Rectangle B:</strong> \( 11\,\text{m} \times 3\,\text{m} = 33\,\text{m}^2 \)<br>
                  <strong>Total Compound Area:</strong> \( 28 + 33 = 61\,\text{m}^2 \)
                </div>
              </div>

              <div class="shape-diagram-box">
                <svg viewBox="0 0 280 170" width="280" height="170">
                  <!-- L-Shape polygon -->
                  <polygon points="30,20 120,20 120,80 240,80 240,140 30,140" fill="#f1f5f9" stroke="#0f172a" stroke-width="2.5"/>
                  <!-- Split Dotted Line -->
                  <line x1="30" y1="80" x2="120" y2="80" stroke="#2563eb" stroke-width="2" stroke-dasharray="4"/>
                  <!-- Label A and B -->
                  <text x="75" y="55" font-family="sans-serif" font-size="14" font-weight="900" fill="#2563eb" text-anchor="middle">A (28 m²)</text>
                  <text x="135" y="115" font-family="sans-serif" font-size="14" font-weight="900" fill="#059669" text-anchor="middle">B (33 m²)</text>
                  <!-- Outer Dimension Labels -->
                  <text x="15" y="85" font-family="sans-serif" font-size="11" font-weight="700" fill="#0f172a" text-anchor="middle">7 m</text>
                  <text x="75" y="14" font-family="sans-serif" font-size="11" font-weight="700" fill="#0f172a" text-anchor="middle">4 m</text>
                  <text x="135" y="155" font-family="sans-serif" font-size="11" font-weight="700" fill="#0f172a" text-anchor="middle">Total Base = 11 m</text>
                  <text x="255" y="115" font-family="sans-serif" font-size="11" font-weight="700" fill="#0f172a">3 m</text>
                </svg>
              </div>
            </div>
          </div>
        </section>

        <!-- 7. PEARSON EDEXCEL WORKED EXAM MODELS -->
        <section id="worked-models" class="revision-section">
          <div class="section-header-row">
            <h2 class="section-title"><i class="fa-solid fa-file-signature"></i> Pearson Edexcel Step-by-Step Worked Models</h2>
            <span style="font-size:0.85rem; font-weight:700; color:#059669;"><i class="fa-solid fa-award"></i> Official Mark Schemes</span>
          </div>
          <p class="section-lead-text">
            These full exam questions demonstrate how examiners allocate Method Marks (<strong>M</strong>), Process Marks (<strong>P</strong>), and Accuracy Marks (<strong>A</strong>).
          </p>

          <!-- MODEL 1: Level 1 Turf Question -->
          <div class="worked-model-card">
            <div class="model-header-bar">
              <span class="badge-worked-model">Worked Exam Model #1 • Level 1</span>
              <span class="model-marks-pill"><i class="fa-solid fa-check-double"></i> 3 Marks Total</span>
            </div>

            <div class="model-question-stem">
              <strong>Exam Context:</strong> Sarah is re-turfing her rectangular garden lawn. The lawn measures \( 9\,\text{m} \) long and \( 6\,\text{m} \) wide. Lawn turf is sold in rolls that cover \( 1\,\text{m}^2 \) each, priced at £4.75 per roll. Calculate the total cost to turf Sarah's entire lawn.
            </div>

            <div class="model-steps-list">
              <div class="model-step-row">
                <span class="step-number-bubble">Step 1</span>
                <div class="step-detail-body">
                  <div class="step-detail-title">Calculate the total surface area of the rectangular lawn</div>
                  <div class="step-math-line">\text{Area} = 9\,\text{m} \times 6\,\text{m} = 54\,\text{m}^2</div>
                  <div class="mark-scheme-tag"><i class="fa-solid fa-circle-check"></i> [M1] Method mark for \( 9 \times 6 \)</div>
                </div>
              </div>

              <div class="model-step-row">
                <span class="step-number-bubble">Step 2</span>
                <div class="step-detail-body">
                  <div class="step-detail-title">Determine the total number of rolls and calculate total cost</div>
                  <div class="step-math-line">54\,\text{rolls} \times £4.75 = £256.50</div>
                  <div class="mark-scheme-tag"><i class="fa-solid fa-circle-check"></i> [M1] Method mark for multiplying area by £4.75</div>
                </div>
              </div>

              <div class="model-step-row">
                <span class="step-number-bubble">Step 3</span>
                <div class="step-detail-body">
                  <div class="step-detail-title">Format final currency answer correctly</div>
                  <div class="step-math-line">£256.50 \quad (\text{Note: money must have 2 decimal places, never } £256.5)</div>
                  <div class="mark-scheme-tag"><i class="fa-solid fa-circle-check"></i> [A1] Accuracy mark for £256.50</div>
                </div>
              </div>
            </div>

            <div class="model-final-answer-callout">
              <div class="model-final-text">
                <i class="fa-solid fa-award"></i> Final Exam Answer: £256.50
              </div>
              <span style="font-size:0.85rem; opacity:0.9;">Full 3/3 Marks Achieved</span>
            </div>
          </div>

          <!-- MODEL 2: Level 2 Multi-Step Flooring with Wastage -->
          <div class="worked-model-card">
            <div class="model-header-bar">
              <span class="badge-worked-model" style="background:#eff6ff; border-color:#93c5fd; color:#1e40af;">Worked Exam Model #2 • Level 2</span>
              <span class="model-marks-pill"><i class="fa-solid fa-check-double"></i> 5 Marks Total</span>
            </div>

            <div class="model-question-stem">
              <strong>Exam Context:</strong> An NHS clinic manager needs new vinyl flooring for an L-shaped corridor. The corridor has a floor area of \( 48\,\text{m}^2 \). The flooring contractor recommends adding <strong>10% extra area for cutting wastage</strong>. Vinyl tiles are sold in packs that cover \( 2.5\,\text{m}^2 \) each, costing £34.50 per pack. Packs cannot be split. Calculate the total cost to buy enough packs of tiles.
            </div>

            <div class="model-steps-list">
              <div class="model-step-row">
                <span class="step-number-bubble">Step 1</span>
                <div class="step-detail-body">
                  <div class="step-detail-title">Calculate the 10% wastage allowance and total area needed</div>
                  <div class="step-math-line">10\% \text{ of } 48\,\text{m}^2 = 4.8\,\text{m}^2 \quad \implies \quad 48 + 4.8 = 52.8\,\text{m}^2</div>
                  <div class="mark-scheme-tag"><i class="fa-solid fa-circle-check"></i> [P1] Process mark for finding 10% and adding to total area</div>
                </div>
              </div>

              <div class="model-step-row">
                <span class="step-number-bubble">Step 2</span>
                <div class="step-detail-body">
                  <div class="step-detail-title">Calculate the exact number of tile packs needed</div>
                  <div class="step-math-line">52.8\,\text{m}^2 \div 2.5\,\text{m}^2 = 21.12 \text{ packs}</div>
                  <div class="mark-scheme-tag"><i class="fa-solid fa-circle-check"></i> [P1] Process mark for dividing required area by pack coverage</div>
                </div>
              </div>

              <div class="model-step-row">
                <span class="step-number-bubble">Step 3</span>
                <div class="step-detail-body">
                  <div class="step-detail-title">Round UP to the nearest whole pack (Real-World Context)</div>
                  <div class="step-math-line">21.12 \text{ packs} \implies 22 \text{ full packs must be purchased}</div>
                  <div class="mark-scheme-tag"><i class="fa-solid fa-circle-check"></i> [M1] Method mark for rounding up to 22 (cannot buy 0.12 of a pack)</div>
                </div>
              </div>

              <div class="model-step-row">
                <span class="step-number-bubble">Step 4</span>
                <div class="step-detail-body">
                  <div class="step-detail-title">Multiply full pack count by cost per pack</div>
                  <div class="step-math-line">22 \times £34.50 = £759.00</div>
                  <div class="mark-scheme-tag"><i class="fa-solid fa-circle-check"></i> [A1] Accuracy mark for correct total of £759</div>
                </div>
              </div>
            </div>

            <div class="model-final-answer-callout">
              <div class="model-final-text">
                <i class="fa-solid fa-award"></i> Final Exam Answer: £759 (22 packs)
              </div>
              <span style="font-size:0.85rem; opacity:0.9;">Full 5/5 Marks Achieved</span>
            </div>
          </div>
        </section>

        <!-- 8. COMMON EXAMINER TRAPS -->
        <section id="examiner-traps" class="revision-section">
          <div class="section-header-row">
            <h2 class="section-title"><i class="fa-solid fa-triangle-exclamation" style="color:#ef4444;"></i> Common Examiner Traps &amp; Lost Marks</h2>
          </div>
          <p class="section-lead-text">
            Official Pearson Edexcel examiner reports highlight that over 35% of candidates lose marks on area questions due to simple, avoidable errors.
          </p>

          <div class="trap-card-coral">
            <div class="trap-card-coral-header">
              <i class="fa-solid fa-circle-xmark"></i>
              <span>Trap 1: Rounding DOWN Pack Quantities</span>
            </div>
            <p>
              In normal maths, \( 21.12 \) rounds down to \( 21 \). But in Functional Skills trade contexts, if you buy 21 packs you will run out of tiles and leave a section of the corridor bare! <strong>Always round UP</strong> to the next whole pack when buying materials.
            </p>
            <div class="trap-remedy-pill">
              <i class="fa-solid fa-circle-check" style="color:#16a34a;"></i> <strong>Exam Fix:</strong> 21.12 packs &rarr; Round UP to 22 packs.
            </div>
          </div>

          <div class="trap-card-coral">
            <div class="trap-card-coral-header">
              <i class="fa-solid fa-circle-xmark"></i>
              <span>Trap 2: Mismatched Units (\( \text{m} \) and \( \text{cm} \))</span>
            </div>
            <p>
              Length given in metres (\( 4.2\,\text{m} \)) and width given in centimetres (\( 75\,\text{cm} \)). Candidates multiply \( 4.2 \times 75 = 315 \), failing to convert \( 75\,\text{cm} \) into \( 0.75\,\text{m} \).
            </p>
            <div class="trap-remedy-pill">
              <i class="fa-solid fa-circle-check" style="color:#16a34a;"></i> <strong>Exam Fix:</strong> Convert both to metres before multiplying: \( 4.2 \times 0.75 = 3.15\,\text{m}^2 \).
            </div>
          </div>

          <div class="trap-card-coral">
            <div class="trap-card-coral-header">
              <i class="fa-solid fa-circle-xmark"></i>
              <span>Trap 3: Money Written With 1 Decimal Place</span>
            </div>
            <p>
              A candidate completes the maths correctly and writes \( £256.5 \) instead of \( £256.50 \). Pearson mark schemes state: <em>"Penalise £256.5 on accuracy mark"</em>. Money must always have two decimal places.
            </p>
            <div class="trap-remedy-pill">
              <i class="fa-solid fa-circle-check" style="color:#16a34a;"></i> <strong>Exam Fix:</strong> Write £256.50 (with the trailing zero).
            </div>
          </div>
        </section>

        <!-- 9. INTERACTIVE PRACTICE EXAM QUESTIONS -->
        <section id="practice-questions" class="revision-section">
          <div class="section-header-row">
            <h2 class="section-title"><i class="fa-solid fa-pencil"></i> Interactive Exam Practice Questions</h2>
            <span style="font-size:0.85rem; color:var(--text-muted); font-weight:600;">Self-Marked Practice</span>
          </div>
          <p class="section-lead-text">
            Test yourself under timed exam conditions. Type your step-by-step working into the scratchpad, then click <strong>Reveal Step-by-Step Solution</strong> to self-assess against the official mark scheme.
          </p>

          <!-- PRACTICE Q1 -->
          <div class="practice-q-card">
            <div class="practice-q-header">
              <span class="practice-q-num">Question 1: Rectangle Area &amp; Unit Conversion</span>
              <span class="practice-q-marks">3 Marks &bull; Non-Calculator</span>
            </div>
            <div class="practice-q-stem">
              A bespoke timber shelf measures \( 2.5\,\text{m} \) long and \( 40\,\text{cm} \) wide. <br>
              Calculate the total surface area of the top of the shelf in <strong>square metres (\( \text{m}^2 \))</strong>.
            </div>
            <div class="working-scratchpad-area">
              <label class="working-scratchpad-label"><i class="fa-solid fa-calculator"></i> Digital Working-Out Scratchpad (Type your method here):</label>
              <textarea class="working-scratchpad-input" placeholder="Step 1: Convert 40 cm into metres...&#10;Step 2: Multiply length by width...&#10;Final Answer:"></textarea>
            </div>
            <div class="practice-q-toolbar">
              <button type="button" class="btn-reveal-solution" onclick="toggleSolution('sol-q1')">
                <i class="fa-solid fa-eye"></i> Reveal Step-by-Step Solution
              </button>
              <span style="font-size:0.82rem; color:var(--text-muted);"><i class="fa-solid fa-shield-halved"></i> Method Marks: M1, A1</span>
            </div>

            <div id="sol-q1" class="solution-drawer">
              <div class="solution-drawer-title"><i class="fa-solid fa-circle-check"></i> Official Worked Mark Scheme:</div>
              <ul style="padding-left:18px; line-height:1.65; color:#14532d; font-size:0.92rem; margin:0 0 10px 0;">
                <li><strong>Step 1: Convert width to metres:</strong> \( 40\,\text{cm} \div 100 = 0.4\,\text{m} \) <em>[1 Mark for unit conversion]</em></li>
                <li><strong>Step 2: Multiply length by width:</strong> \( 2.5 \times 0.4 = 1.0\,\text{m}^2 \) <em>[1 Mark for method]</em></li>
                <li><strong>Final Answer:</strong> \( 1\,\text{m}^2 \) (or \( 1.0\,\text{m}^2 \)) <em>[1 Mark for accuracy with units]</em></li>
              </ul>
              <div class="self-marking-bar">
                <span style="font-size:0.84rem; font-weight:700; color:#166534;">Self-Check Your Score:</span>
                <button type="button" class="btn-mark-eval btn-eval-success" onclick="this.textContent='Full Marks! 🎉'">Got 3/3 Marks</button>
                <button type="button" class="btn-mark-eval btn-eval-retry" onclick="this.textContent='Reviewing Units 🔁'">Need More Practice</button>
              </div>
            </div>
          </div>

          <!-- PRACTICE Q2 -->
          <div class="practice-q-card">
            <div class="practice-q-header">
              <span class="practice-q-num">Question 2: Triangular Sail Area</span>
              <span class="practice-q-marks">3 Marks &bull; Calculator</span>
            </div>
            <div class="practice-q-stem">
              A sailmaker needs to cut a triangular canvas sail with a base of \( 6.4\,\text{m} \) and a perpendicular height of \( 4.5\,\text{m} \). Canvas costs £18.50 per square metre. <br>
              Calculate the total cost of canvas needed for this sail.
            </div>
            <div class="working-scratchpad-area">
              <label class="working-scratchpad-label"><i class="fa-solid fa-calculator"></i> Digital Working-Out Scratchpad:</label>
              <textarea class="working-scratchpad-input" placeholder="Step 1: Calculate triangle area (base × height ÷ 2)...&#10;Step 2: Multiply area by £18.50..."></textarea>
            </div>
            <div class="practice-q-toolbar">
              <button type="button" class="btn-reveal-solution" onclick="toggleSolution('sol-q2')">
                <i class="fa-solid fa-eye"></i> Reveal Step-by-Step Solution
              </button>
              <span style="font-size:0.82rem; color:var(--text-muted);"><i class="fa-solid fa-shield-halved"></i> Method Marks: M1, M1, A1</span>
            </div>

            <div id="sol-q2" class="solution-drawer">
              <div class="solution-drawer-title"><i class="fa-solid fa-circle-check"></i> Official Worked Mark Scheme:</div>
              <ul style="padding-left:18px; line-height:1.65; color:#14532d; font-size:0.92rem; margin:0 0 10px 0;">
                <li><strong>Step 1: Triangle Area:</strong> \( (6.4 \times 4.5) \div 2 = 28.8 \div 2 = 14.4\,\text{m}^2 \) <em>[1 Mark]</em></li>
                <li><strong>Step 2: Cost Calculation:</strong> \( 14.4 \times £18.50 = £266.40 \) <em>[1 Mark for multiplication]</em></li>
                <li><strong>Final Answer:</strong> £266.40 (Must include 2 decimal places for pence) <em>[1 Mark]</em></li>
              </ul>
              <div class="self-marking-bar">
                <span style="font-size:0.84rem; font-weight:700; color:#166534;">Self-Check Your Score:</span>
                <button type="button" class="btn-mark-eval btn-eval-success" onclick="this.textContent='Full Marks! 🎉'">Got 3/3 Marks</button>
                <button type="button" class="btn-mark-eval btn-eval-retry" onclick="this.textContent='Reviewing Triangles 🔁'">Need More Practice</button>
              </div>
            </div>
          </div>

          <!-- PRACTICE Q3 -->
          <div class="practice-q-card">
            <div class="practice-q-header">
              <span class="practice-q-num">Question 3: Trapezium Parking Bay</span>
              <span class="practice-q-marks">4 Marks &bull; Level 2 Standard</span>
            </div>
            <div class="practice-q-stem">
              A delivery van loading bay has the shape of a trapezium with parallel sides of \( 5.2\,\text{m} \) and \( 8.8\,\text{m} \). The distance between the parallel sides is \( 6\,\text{m} \). <br>
              Tarmac sealant costs £4.20 per square metre. Calculate the total cost to seal the entire loading bay.
            </div>
            <div class="working-scratchpad-area">
              <label class="working-scratchpad-label"><i class="fa-solid fa-calculator"></i> Digital Working-Out Scratchpad:</label>
              <textarea class="working-scratchpad-input" placeholder="Step 1: Average parallel sides (a + b) ÷ 2...&#10;Step 2: Multiply by height...&#10;Step 3: Multiply area by £4.20..."></textarea>
            </div>
            <div class="practice-q-toolbar">
              <button type="button" class="btn-reveal-solution" onclick="toggleSolution('sol-q3')">
                <i class="fa-solid fa-eye"></i> Reveal Step-by-Step Solution
              </button>
              <span style="font-size:0.82rem; color:var(--text-muted);"><i class="fa-solid fa-shield-halved"></i> Method Marks: M1, M1, M1, A1</span>
            </div>

            <div id="sol-q3" class="solution-drawer">
              <div class="solution-drawer-title"><i class="fa-solid fa-circle-check"></i> Official Worked Mark Scheme:</div>
              <ul style="padding-left:18px; line-height:1.65; color:#14532d; font-size:0.92rem; margin:0 0 10px 0;">
                <li><strong>Step 1: Add parallel sides:</strong> \( 5.2 + 8.8 = 14.0\,\text{m} \) <em>[1 Mark]</em></li>
                <li><strong>Step 2: Average and multiply by height:</strong> \( (14 \div 2) \times 6 = 7 \times 6 = 42\,\text{m}^2 \) <em>[1 Mark]</em></li>
                <li><strong>Step 3: Cost calculation:</strong> \( 42 \times £4.20 = £176.40 \) <em>[1 Mark]</em></li>
                <li><strong>Final Answer:</strong> £176.40 <em>[1 Mark]</em></li>
              </ul>
              <div class="self-marking-bar">
                <span style="font-size:0.84rem; font-weight:700; color:#166534;">Self-Check Your Score:</span>
                <button type="button" class="btn-mark-eval btn-eval-success" onclick="this.textContent='Full Marks! 🎉'">Got 4/4 Marks</button>
                <button type="button" class="btn-mark-eval btn-eval-retry" onclick="this.textContent='Reviewing Trapeziums 🔁'">Need More Practice</button>
              </div>
            </div>
          </div>
        </section>

        <!-- 10. PRINTABLE DOWNLOADS -->
        <section id="downloads" class="revision-section">
          <div class="section-header-row">
            <h2 class="section-title"><i class="fa-regular fa-file-pdf"></i> Free Printable Worksheets &amp; Answer Keys</h2>
          </div>
          <p class="section-lead-text">
            Download our dyslexia-friendly, double-spaced practice worksheets and comprehensive tutor mark schemes for offline study.
          </p>

          <div class="download-tiles-grid">
            <a href="worksheets/area-worksheet.html" target="_blank" class="download-tile-card">
              <div class="download-tile-icon icon-pdf">
                <i class="fa-regular fa-file-pdf"></i>
              </div>
              <div class="download-tile-info">
                <strong>Area Practice Worksheet (PDF)</strong>
                <span>15 Exam-calibrated questions &bull; Printable</span>
              </div>
            </a>

            <a href="worksheets/area-answers.html" target="_blank" class="download-tile-card">
              <div class="download-tile-icon icon-answers">
                <i class="fa-solid fa-circle-check"></i>
              </div>
              <div class="download-tile-info">
                <strong>Full Worked Answers &amp; Mark Scheme</strong>
                <span>Step-by-step model methods &bull; Pearson criteria</span>
              </div>
            </a>
          </div>
        </section>

        <!-- 11. REVISION CARDS SHOWCASE -->
        <section id="revision-cards" class="revision-section">
          <div class="revision-cards-showcase-box">
            <div class="cards-showcase-text">
              <span style="background:#f59e0b; color:#070d1e; font-weight:800; font-size:0.75rem; padding:3px 10px; border-radius:9999px; text-transform:uppercase; letter-spacing:0.06em; display:inline-block; margin-bottom:12px;">★ FLAGSHIP PHYSICAL PACK</span>
              <h3>Pocket Revision Cards: Maths Level 2</h3>
              <p>
                64 high-gloss, color-coded revision cards covering Area, Volume, Fractions, Ratio, and Probability. Features essential exam formulas on the front with common traps, stepped method marks, and worked models on the back.
              </p>
              <a href="shop.html" class="btn-cards-order-now">
                <i class="fa-solid fa-basket-shopping"></i> Order Pocket Revision Cards (£12.99) &rarr;
              </a>
            </div>

            <div class="cards-showcase-visual" style="text-align:center;">
              <img src="assets/img/books/flashcards_maths_l2.svg" alt="Master Functional Skills Pocket Revision Cards 3D Stack">
            </div>
          </div>
        </section>

      </div>
    </div>
  </main>

  <!-- FOOTER -->
  <footer style="background:#070d1e; color:#ffffff; padding:60px 0 30px; border-top:1px solid rgba(255,255,255,0.1);">
    <div class="mfs-container">
      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap:36px; margin-bottom:40px;">
        <div>
          <div style="font-weight:900; font-size:1.2rem; letter-spacing:1px; margin-bottom:12px;">
            MASTER<span style="color:#60a5fa;">FUNCTIONALSKILLS</span>
          </div>
          <p style="font-size:0.88rem; color:#94a3b8; line-height:1.6; margin-bottom:16px;">
            The UK's leading Functional Skills revision and examination specialist. Fast-track your Level 2 qualification for university, nursing, and apprenticeships.
          </p>
        </div>
        <div>
          <h4 style="font-size:0.95rem; font-weight:800; color:#ffffff; margin-bottom:14px; text-transform:uppercase;">Maths Revision</h4>
          <ul style="list-style:none; padding:0; margin:0; font-size:0.86rem; color:#cbd5e1; display:flex; flex-direction:column; gap:8px;">
            <li><a href="functional-skills-maths-level-2.html" style="color:#cbd5e1; text-decoration:none;">Maths Level 2 Directory</a></li>
            <li><a href="functional-skills-area.html" style="color:#60a5fa; text-decoration:none; font-weight:700;">Area & Perimeter Revision</a></li>
            <li><a href="functional-skills-fractions.html" style="color:#cbd5e1; text-decoration:none;">Fractions & Decimals</a></li>
            <li><a href="shop.html" style="color:#f59e0b; text-decoration:none; font-weight:700;">Pocket Revision Cards Store</a></li>
          </ul>
        </div>
        <div>
          <h4 style="font-size:0.95rem; font-weight:800; color:#ffffff; margin-bottom:14px; text-transform:uppercase;">Book Exams</h4>
          <ul style="list-style:none; padding:0; margin:0; font-size:0.86rem; color:#cbd5e1; display:flex; flex-direction:column; gap:8px;">
            <li><a href="exam-maths-l2.html" style="color:#cbd5e1; text-decoration:none;">Book Maths Level 2 Exam (£149)</a></li>
            <li><a href="exam-english-l2.html" style="color:#cbd5e1; text-decoration:none;">Book English Level 2 Exam (£149)</a></li>
            <li><a href="functional-skills-past-papers.html" style="color:#cbd5e1; text-decoration:none;">Free Past Papers</a></li>
            <li><a href="contact-us.html" style="color:#cbd5e1; text-decoration:none;">Speak to a Tutor</a></li>
          </ul>
        </div>
      </div>
      <div style="border-top:1px solid rgba(255,255,255,0.08); padding-top:20px; text-align:center; font-size:0.8rem; color:#64748b;">
        &copy; 2026 Master Functional Skills. All rights reserved. Ofqual Regulated Qualification Standards.
      </div>
    </div>
  </footer>

  <!-- DYSLEXIA TINT SCRIPT -->
  <script src="assets/js/mfs-tint.js"></script>

  <!-- INTERACTIVE FUNCTIONS & SCROLLSPY SCRIPT -->
  <script>
    // Reveal Solution Drawer
    function toggleSolution(id) {
      const drawer = document.getElementById(id);
      if (drawer) {
        drawer.classList.toggle('open');
      }
    }

    // Toggle Mobile Table of Contents
    function toggleMobileToc() {
      const sidebar = document.getElementById('sidebarNav');
      if (sidebar) {
        if (sidebar.style.display === 'block') {
          sidebar.style.display = 'none';
        } else {
          sidebar.style.display = 'block';
          sidebar.scrollIntoView({ behavior: 'smooth' });
        }
      }
    }

    // Sticky ScrollSpy Active State
    window.addEventListener('scroll', function() {
      const sections = document.querySelectorAll('.revision-section');
      const navLinks = document.querySelectorAll('.sidebar-toc-link');
      let currentSectionId = '';

      sections.forEach(function(sec) {
        const top = sec.offsetTop - 120;
        const height = sec.offsetHeight;
        if (window.scrollY >= top && window.scrollY < top + height) {
          currentSectionId = sec.getAttribute('id');
        }
      });

      if (currentSectionId) {
        navLinks.forEach(function(link) {
          link.classList.remove('active');
          if (link.getAttribute('href') === '#' + currentSectionId) {
            link.classList.add('active');
          }
        });
      }
    });
  </script>
</body>
</html>
"""

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"[OK] Generated gold-standard modern revision page at {OUTPUT_FILE} ({len(html_content)} bytes)")
