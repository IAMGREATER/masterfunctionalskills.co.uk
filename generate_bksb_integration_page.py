import os
import re

PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"

with open(os.path.join(PROJECT_DIR, "generate_modern_services_pages.py"), "r", encoding="utf-8") as f:
    code = f.read()

nav_match = re.search(r'NAV_HEADER = """(.*?)"""', code, re.DOTALL)
NAV_HEADER = nav_match.group(1).strip() if nav_match else ""

footer_match = re.search(r'FOOTER = """(.*?)"""', code, re.DOTALL)
FOOTER = footer_match.group(1).strip() if footer_match else ""

page_html = f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BKSB / OneAdvanced Automated Remediation & API Bridge | Master Functional Skills</title>
  <meta name="description" content="Automated BKSB / OneAdvanced diagnostic results integration for colleges, NHS trusts, and apprenticeships. Convert learner skill gaps into targeted retry sheets and worked solutions.">
  <link rel="stylesheet" href="assets/css/mfs-theme.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
  <style>
    .bridge-hero-badge {{
      background: rgba(37, 99, 235, 0.12);
      color: #2563eb;
      font-weight: 800;
      padding: 6px 16px;
      border-radius: 100px;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 0.85rem;
      margin-bottom: 14px;
    }}
    .flow-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 28px;
      box-shadow: 0 4px 20px rgba(7, 13, 30, 0.04);
      position: relative;
    }}
    .flow-step-num {{
      width: 38px;
      height: 38px;
      border-radius: 10px;
      background: var(--navy);
      color: #ffffff;
      font-weight: 800;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.1rem;
      margin-bottom: 16px;
    }}
  </style>
</head>
<body>
{NAV_HEADER}

  <!-- HERO SECTION -->
  <section class="mfs-hero-section">
    <div class="mfs-container mfs-hero-grid">
      <div class="hero-content">
        <span class="bridge-hero-badge">
          <i class="fa-solid fa-network-wired"></i> Enterprise & College Software Bridge
        </span>
        <h1 style="font-size: 2.6rem;">Automated <span>BKSB / OneAdvanced</span> Results & Remediation</h1>
        <p class="hero-description">
          Eliminate manual screenshots and spreadsheet tracking. Our planned secure API & LTI software bridge connects directly with BKSB / OneAdvanced platforms to ingest learner diagnostic results, automatically generating targeted, dyslexia-friendly retry worksheets and tutor-led worked solutions.
        </p>
        <div class="moat-strip">
          <span class="moat-badge"><i class="fa-solid fa-bolt"></i> Zero Screenshot Friction</span>
          <span class="moat-badge"><i class="fa-solid fa-shield-halved"></i> GDPR & LTI 1.3 Secure</span>
          <span class="moat-badge"><i class="fa-solid fa-graduation-cap"></i> NHS & Apprenticeship Ready</span>
        </div>
        <div class="hero-buttons">
          <a href="#partner-form" class="btn-hero-accent"><i class="fa-solid fa-handshake"></i> Request Pilot Partnership</a>
          <a href="diagnostic-test.html" class="btn-hero-navy"><i class="fa-solid fa-bullseye"></i> Try Free Diagnostic Test</a>
        </div>
      </div>
      <div>
        <div style="background:#ffffff; border-radius:18px; border:1px solid var(--border); padding:28px; box-shadow:0 12px 35px rgba(7,13,30,0.08);">
          <div style="display:flex; align-items:center; gap:12px; margin-bottom:16px;">
            <div style="width:48px; height:48px; border-radius:12px; background:rgba(37,99,235,0.1); color:#2563eb; display:flex; align-items:center; justify-content:center; font-size:1.4rem;">
              <i class="fa-solid fa-server"></i>
            </div>
            <div>
              <h3 style="font-size:1.15rem; color:var(--navy); margin:0;">Direct Software Bridge</h3>
              <span style="font-size:0.8rem; color:var(--text-muted);">BKSB / OneAdvanced → Master Functional Skills</span>
            </div>
          </div>
          <div style="font-size:0.88rem; color:var(--text-secondary); line-height:1.6; display:flex; flex-direction:column; gap:12px;">
            <div style="padding:10px 14px; background:#faf8f2; border-radius:10px; border-left:3px solid #2563eb;">
              <strong>1. Automated Diagnostic Pull:</strong> Learner completes BKSB / OneAdvanced Initial Assessment or Skill Check.
            </div>
            <div style="padding:10px 14px; background:#faf8f2; border-radius:10px; border-left:3px solid var(--accent);">
              <strong>2. Competency Code Mapping:</strong> System maps wrong question tags directly to Pearson Edexcel & Ofqual standards.
            </div>
            <div style="padding:10px 14px; background:#faf8f2; border-radius:10px; border-left:3px solid #f59e0b;">
              <strong>3. Two-Stage Delivery:</strong> Generates independent "Retry Questions" first, followed by worked step-by-step diagnostic solutions.
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 3 STEP PROCESS SECTION -->
  <section style="padding: 64px 0; background: var(--bg-page);">
    <div class="mfs-container">
      <div style="text-align:center; max-width:760px; margin:0 auto 48px;">
        <h2 style="font-size:2rem; color:var(--navy); margin-bottom:12px;">Why Automated Integration Replaces Manual Screenshots</h2>
        <p style="color:var(--text-muted); font-size:0.95rem; line-height:1.6;">
          Asking apprentices and healthcare learners to capture and upload screenshots of BKSB / OneAdvanced question screens is error-prone, insecure, and frustrating. Our automated bridge modernises the entire diagnostic workflow.
        </p>
      </div>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:24px;">
        <div class="flow-card">
          <div class="flow-step-num">1</div>
          <h3 style="font-size:1.2rem; color:var(--navy); margin-bottom:8px;">Instant Ingestion via API</h3>
          <p style="color:var(--text-muted); font-size:0.9rem; line-height:1.6;">
            With institutional API credentials, learner assessment scores and specific missed question areas are synchronized securely into their learning plan.
          </p>
        </div>
        <div class="flow-card">
          <div class="flow-step-num">2</div>
          <h3 style="font-size:1.2rem; color:var(--navy); margin-bottom:8px;">Stage 1: Retry Sheets</h3>
          <p style="color:var(--text-muted); font-size:0.9rem; line-height:1.6;">
            Learners receive clean, dyslexia-friendly retry worksheets containing only the questions they struggled with, allowing them to re-attempt independently.
          </p>
        </div>
        <div class="flow-card">
          <div class="flow-step-num">3</div>
          <h3 style="font-size:1.2rem; color:var(--navy); margin-bottom:8px;">Stage 2: Tutor Solutions</h3>
          <p style="color:var(--text-muted); font-size:0.9rem; line-height:1.6;">
            For persistent gaps, learners unlock step-by-step diagnostic explanations, golden rules, and video walkthroughs prepared by specialist functional skills tutors.
          </p>
        </div>
      </div>

      <!-- PARTNER INQUIRY FORM -->
      <div id="partner-form" style="margin-top:64px; background:#ffffff; border-radius:20px; border:1px solid var(--border); padding:36px; box-shadow:0 8px 30px rgba(7,13,30,0.06); max-width:800px; margin-left:auto; margin-right:auto;">
        <h3 style="font-size:1.45rem; color:var(--navy); margin-bottom:8px; text-align:center;">Register Interest for BKSB / OneAdvanced Bridge Pilot</h3>
        <p style="color:var(--text-muted); font-size:0.9rem; text-align:center; margin-bottom:28px;">
          For Colleges, Apprenticeship Training Providers, and NHS Trusts seeking automated learner diagnostics.
        </p>

        <form onsubmit="handlePartnerSubmit(event)" style="display:flex; flex-direction:column; gap:16px;">
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">
            <div>
              <label style="display:block; font-size:0.88rem; font-weight:700; color:var(--navy); margin-bottom:6px;">Your Name *</label>
              <input type="text" required style="width:100%; padding:11px 14px; border-radius:10px; border:1px solid var(--border); font-size:0.92rem; background:#faf8f2;">
            </div>
            <div>
              <label style="display:block; font-size:0.88rem; font-weight:700; color:var(--navy); margin-bottom:6px;">Work Email *</label>
              <input type="email" required style="width:100%; padding:11px 14px; border-radius:10px; border:1px solid var(--border); font-size:0.92rem; background:#faf8f2;">
            </div>
          </div>

          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">
            <div>
              <label style="display:block; font-size:0.88rem; font-weight:700; color:var(--navy); margin-bottom:6px;">Organisation / College / NHS Trust *</label>
              <input type="text" required style="width:100%; padding:11px 14px; border-radius:10px; border:1px solid var(--border); font-size:0.92rem; background:#faf8f2;">
            </div>
            <div>
              <label style="display:block; font-size:0.88rem; font-weight:700; color:var(--navy); margin-bottom:6px;">Diagnostic Platform Used</label>
              <select style="width:100%; padding:11px 14px; border-radius:10px; border:1px solid var(--border); font-size:0.92rem; background:#faf8f2;">
                <option>BKSB / OneAdvanced</option>
                <option>OneAdvanced (Skills Forward)</option>
                <option>Century Tech</option>
                <option>Other / Multiple</option>
              </select>
            </div>
          </div>

          <div>
            <label style="display:block; font-size:0.88rem; font-weight:700; color:var(--navy); margin-bottom:6px;">Learner Cohort Size</label>
            <select style="width:100%; padding:11px 14px; border-radius:10px; border:1px solid var(--border); font-size:0.92rem; background:#faf8f2;">
              <option>Under 50 learners / year</option>
              <option>50 – 250 learners / year</option>
              <option>250 – 1,000 learners / year</option>
              <option>1,000+ enterprise / college-wide</option>
            </select>
          </div>

          <div>
            <label style="display:block; font-size:0.88rem; font-weight:700; color:var(--navy); margin-bottom:6px;">Message or Specific Integration Requirements</label>
            <textarea rows="3" placeholder="Tell us about your functional skills cohort, typical failure points, or software bridge requirements..." style="width:100%; padding:11px 14px; border-radius:10px; border:1px solid var(--border); font-size:0.92rem; background:#faf8f2; font-family:inherit;"></textarea>
          </div>

          <button type="submit" class="btn-hero-accent" style="padding:14px; justify-content:center; font-size:1rem; cursor:pointer; margin-top:8px;">
            <i class="fa-solid fa-paper-plane"></i> Submit Partnership Inquiry
          </button>
          <div id="partnerSuccessMsg" style="display:none; text-align:center; padding:12px; background:rgba(0,184,124,0.12); color:#00b87c; border-radius:10px; font-weight:700;">
            Thank you! Your institutional partnership inquiry has been received. Our lead academic consultant will be in touch within 24 hours.
          </div>
        </form>
      </div>

    </div>
  </section>

  <script>
    function handlePartnerSubmit(ev) {{
      ev.preventDefault();
      document.getElementById('partnerSuccessMsg').style.display = 'block';
    }}
  </script>

{FOOTER}
</body>
</html>
"""

target = os.path.join(PROJECT_DIR, "bksb-remediation.html")
with open(target, "w", encoding="utf-8") as f:
    f.write(page_html)

print(f"[OK] Generated {target}")
