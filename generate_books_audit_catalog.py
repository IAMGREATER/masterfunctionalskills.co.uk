#!/usr/bin/env python3
"""
generate_books_audit_catalog.py
=============================================================================
Generates the comprehensive visual image and diagram audit catalog for ALL
Master Functional Skills books (17 books + revision card decks):

Output HTML:
/home/subi/Projects/masterfunctionalskills.co.uk/books_image_audit_catalog.html

Features:
- Side-by-side Current vs Proposed visual comparison
- Renders live inline SVGs for mathematical & technical diagrams
- Displays book covers, 3D mockups, character cartoons, and vocational photos
- Interactive approval options: Approve Proposed / Custom Suggestion / Keep Current
- Custom feedback notes per item
- Real-time statistics counters (Total, Approved, Custom, Kept)
- Suite filtering: All Books, Maths Suite, English Writing Suite, English Reading Suite,
  SPaG Mastery Suite, Specialist Suite (Digital & BKSB), Mock Exam Packs, 3D Covers, Cartoons
- Type filtering: All Types, Diagrams, Photos, Wireframes, Cartoons, Covers
- Live search bar across books, topics, standards, and keywords
- LocalStorage state persistence (auto-saves progress so work is never lost)
- JSON Export: downloads 'mfs_books_image_audit_feedback.json' matching the exact schema
  the user used for website image audit feedback.
=============================================================================
"""

import os
import sys
import json
import html
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import visual_curriculum_catalog as vcc

# =============================================================================
# SVG WIREFRAME & DIAGRAM GENERATORS FOR AUDIT PREVIEWS
# =============================================================================

def get_letter_wireframe_svg():
    return """<svg viewBox="0 0 460 270" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:460px; height:auto; font-family:'Plus Jakarta Sans', sans-serif;">
  <rect x="2" y="2" width="456" height="266" rx="10" fill="#ffffff" stroke="#94a3b8" stroke-width="2"/>
  
  <!-- Sender Address block (Top Right, Spacious) -->
  <rect x="260" y="14" width="180" height="46" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-dasharray="4 3"/>
  <text x="272" y="32" font-size="10" font-weight="800" fill="#0f172a">Sender Address &amp; Date</text>
  <text x="272" y="48" font-size="9" fill="#64748b">Right-aligned, top right corner</text>
  
  <!-- Recipient Address block (Left Aligned, Lower than date) -->
  <rect x="20" y="45" width="180" height="42" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-dasharray="4 3"/>
  <text x="32" y="62" font-size="10" font-weight="800" fill="#0f172a">Recipient Name &amp; Address</text>
  <text x="32" y="77" font-size="9" fill="#64748b">Left-aligned, lower than date</text>
  
  <!-- Salutation -->
  <rect x="20" y="98" width="200" height="22" rx="4" fill="#e0f2fe"/>
  <text x="30" y="113" font-size="10.5" font-weight="800" fill="#0369a1">Dear Mr Davies, / Dear Sir/Madam,</text>
  
  <!-- Subject / Reference Line -->
  <rect x="20" y="128" width="280" height="22" rx="4" fill="#fef3c7"/>
  <text x="30" y="143" font-size="10" font-weight="900" fill="#92400e">RE: FORMAL COMPLAINT - REF #8492</text>
  
  <!-- Body Paragraph lines (Spacious) -->
  <rect x="20" y="158" width="420" height="9" rx="2" fill="#e2e8f0"/>
  <rect x="20" y="172" width="400" height="9" rx="2" fill="#e2e8f0"/>
  <rect x="20" y="186" width="410" height="9" rx="2" fill="#e2e8f0"/>
  
  <!-- Sign-off valediction -->
  <rect x="20" y="206" width="220" height="48" rx="6" fill="#dcfce7" stroke="#86efac"/>
  <text x="30" y="224" font-size="10.5" font-weight="800" fill="#166534">Yours sincerely, / Yours faithfully,</text>
  <text x="30" y="242" font-size="9.5" font-weight="700" fill="#15803d">[Full Candidate Name &amp; Job Title]</text>
</svg>"""

def get_email_wireframe_svg():
    return """<svg viewBox="0 0 460 270" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:460px; height:auto; font-family:'Plus Jakarta Sans', sans-serif;">
  <rect x="2" y="2" width="456" height="266" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
  
  <!-- Email Header Bar -->
  <rect x="2" y="2" width="456" height="34" rx="10 10 0 0" fill="#3b0764"/>
  <circle cx="20" cy="17" r="4.5" fill="#ef4444"/><circle cx="34" cy="17" r="4.5" fill="#f59e0b"/><circle cx="48" cy="17" r="4.5" fill="#10b981"/>
  <text x="68" y="22" font-size="12" font-weight="800" fill="#ffffff">New Workplace Message — Outlook / NHS Webmail</text>
  
  <!-- Header Fields -->
  <rect x="18" y="44" width="424" height="24" rx="5" fill="#f8fafc" stroke="#e2e8f0"/>
  <text x="28" y="60" font-size="10" font-weight="700" fill="#64748b">To: <tspan fill="#0f172a">department.manager@oxfordhealth.nhs.uk</tspan></text>
  
  <rect x="18" y="73" width="424" height="24" rx="5" fill="#f8fafc" stroke="#e2e8f0"/>
  <text x="28" y="89" font-size="10" font-weight="700" fill="#64748b">Subject: <tspan fill="#0f172a" font-weight="900">Proposal: Upgrading Apprentice Clinical Facilities</tspan></text>
  
  <!-- Salutation -->
  <text x="28" y="116" font-size="11" font-weight="800" fill="#3b0764">Dear Clinical Practice Team,</text>
  
  <!-- Message Body lines -->
  <rect x="28" y="126" width="404" height="9" rx="2" fill="#e2e8f0"/>
  <rect x="28" y="140" width="380" height="9" rx="2" fill="#e2e8f0"/>
  
  <!-- Action Points Bullets -->
  <circle cx="36" cy="162" r="3.5" fill="#3b0764"/><rect x="48" y="158" width="340" height="8" rx="2" fill="#cbd5e1"/>
  <circle cx="36" cy="178" r="3.5" fill="#3b0764"/><rect x="48" y="174" width="320" height="8" rx="2" fill="#cbd5e1"/>
  
  <!-- Sign-off & Attachment -->
  <text x="28" y="206" font-size="10.5" font-weight="700" fill="#475569">Kind regards,</text>
  <text x="28" y="222" font-size="11" font-weight="900" fill="#0f172a">Abdul &bull; Senior Lead Tutor</text>
  
  <rect x="28" y="234" width="220" height="22" rx="5" fill="#eff6ff" stroke="#bfdbfe"/>
  <text x="38" y="249" font-size="9.5" font-weight="700" fill="#1d4ed8">📎 Clinical_Proposal_Summary_v2.pdf</text>
</svg>"""

def get_article_wireframe_svg():
    return """<svg viewBox="0 0 460 270" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:460px; height:auto; font-family:'Plus Jakarta Sans', sans-serif;">
  <rect x="2" y="2" width="456" height="266" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
  
  <!-- Magazine Banner -->
  <rect x="16" y="12" width="428" height="42" rx="6" fill="#003366"/>
  <text x="28" y="28" font-size="10" font-weight="800" fill="#38bdf8">CAREERS &amp; COMMUNITY FOCUS &bull; LEVEL 2 MAGAZINE SPREAD</text>
  <text x="28" y="46" font-size="13.5" font-weight="900" fill="#ffffff">Why NHS Healthcare Apprenticeships Are Transforming Care</text>
  
  <!-- Byline -->
  <text x="18" y="68" font-size="9" font-weight="700" fill="#64748b">By Sarah Jenkins &bull; Published 12 October 2026 &bull; 4 min read</text>
  
  <!-- 2 Columns Layout (Spacious) -->
  <rect x="16" y="78" width="206" height="174" rx="6" fill="#f8fafc" stroke="#e2e8f0"/>
  <text x="26" y="96" font-size="10.5" font-weight="900" fill="#003366">1. Real Ward Experience</text>
  <rect x="26" y="104" width="186" height="7" rx="2" fill="#cbd5e1"/>
  <rect x="26" y="116" width="176" height="7" rx="2" fill="#cbd5e1"/>
  <rect x="26" y="128" width="180" height="7" rx="2" fill="#cbd5e1"/>
  
  <!-- Pull Quote Box -->
  <rect x="26" y="142" width="186" height="52" rx="5" fill="#eff6ff" stroke="#bfdbfe"/>
  <text x="34" y="160" font-size="9" font-style="italic" font-weight="700" fill="#1e40af">"Earning while learning gave me the"</text>
  <text x="34" y="173" font-size="9" font-style="italic" font-weight="700" fill="#1e40af">"confidence to step into a band 3 role."</text>
  <text x="34" y="186" font-size="8.5" font-weight="800" fill="#2563eb">— Marcus, Clinical Apprentice</text>
  
  <rect x="26" y="202" width="186" height="7" rx="2" fill="#cbd5e1"/>
  <rect x="26" y="214" width="165" height="7" rx="2" fill="#cbd5e1"/>
  <rect x="26" y="226" width="175" height="7" rx="2" fill="#cbd5e1"/>
  
  <!-- Column 2 (Right) -->
  <rect x="238" y="78" width="206" height="174" rx="6" fill="#f8fafc" stroke="#e2e8f0"/>
  <rect x="248" y="86" width="186" height="68" rx="5" fill="#e2e8f0" stroke="#cbd5e1"/>
  <text x="341" y="124" font-size="9.5" font-weight="800" fill="#64748b" text-anchor="middle">📷 [Vocational Healthcare Photo]</text>
  
  <text x="248" y="172" font-size="10.5" font-weight="900" fill="#003366">2. Actionable Career Steps</text>
  <circle cx="256" cy="186" r="3" fill="#003366"/><rect x="264" y="183" width="160" height="7" rx="2" fill="#cbd5e1"/>
  <circle cx="256" cy="200" r="3" fill="#003366"/><rect x="264" y="197" width="150" height="7" rx="2" fill="#cbd5e1"/>
  
  <rect x="248" y="218" width="186" height="24" rx="5" fill="#003366"/>
  <text x="341" y="234" font-size="9.5" font-weight="800" fill="#ffffff" text-anchor="middle">Enrol Today: www.mfs.org.uk</text>
</svg>"""

def get_report_wireframe_svg():
    return """<svg viewBox="0 0 460 270" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:460px; height:auto; font-family:'Plus Jakarta Sans', sans-serif;">
  <rect x="2" y="2" width="456" height="266" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
  
  <!-- Report Title Header -->
  <rect x="16" y="12" width="428" height="46" rx="5" fill="#0f172a"/>
  <text x="28" y="30" font-size="11.5" font-weight="900" fill="#38bdf8">INVESTIGATION REPORT: HEALTH &amp; SAFETY AUDIT</text>
  <text x="28" y="47" font-size="9" fill="#94a3b8">Target: Safety Executive &bull; Date: October 2026 &bull; Lead Tutor: Abdul</text>
  
  <!-- Section 1.0: Executive Summary -->
  <rect x="16" y="66" width="428" height="48" rx="5" fill="#f8fafc" stroke="#e2e8f0"/>
  <text x="26" y="82" font-size="10.5" font-weight="900" fill="#0f172a">1.0 Executive Summary &amp; Scope</text>
  <rect x="26" y="89" width="408" height="7" rx="2" fill="#cbd5e1"/>
  <rect x="26" y="100" width="380" height="7" rx="2" fill="#cbd5e1"/>
  
  <!-- Section 2.0: Table of Findings -->
  <rect x="16" y="120" width="428" height="58" rx="5" fill="#f8fafc" stroke="#e2e8f0"/>
  <text x="26" y="136" font-size="10.5" font-weight="900" fill="#0f172a">2.0 Risk Assessment Matrix</text>
  <rect x="26" y="142" width="408" height="15" rx="3" fill="#e2e8f0"/>
  <text x="36" y="153" font-size="8.5" font-weight="800" fill="#475569">Inspection Zone | Hazard Noted | Severity Rating | Target Date</text>
  <rect x="26" y="159" width="408" height="15" rx="3" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="36" y="170" font-size="8.5" fill="#0f172a">Ward 4 Store | Obstructed Fire Egress | HIGH | Immediate (24h)</text>
  
  <!-- Section 3.0: Recommendations -->
  <rect x="16" y="184" width="428" height="72" rx="5" fill="#eff6ff" stroke="#bfdbfe"/>
  <text x="26" y="200" font-size="10.5" font-weight="900" fill="#1e40af">3.0 Actionable Recommendations</text>
  <text x="36" y="215" font-size="9" font-weight="700" fill="#1e3a8a">&bull; Clear all corridor emergency routes immediately (Priority 1)</text>
  <text x="36" y="229" font-size="9" font-weight="700" fill="#1e3a8a">&bull; Deploy digital checklist app across shift handovers</text>
  <text x="36" y="243" font-size="9" font-weight="700" fill="#1e3a8a">&bull; Complete follow-up audit with Lead Tutor Abdul on Friday</text>
</svg>"""

def get_bksb_misconception_svg():
    return """<svg viewBox="0 0 540 280" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:540px; height:auto; font-family:'Plus Jakarta Sans', sans-serif;">
  <rect x="2" y="2" width="536" height="276" rx="14" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
  
  <!-- Header Banner -->
  <rect x="14" y="12" width="512" height="34" rx="8" fill="#1d4ed8"/>
  <text x="26" y="34" font-size="12" font-weight="900" fill="#ffffff">DIAGNOSTIC FAILURE MODE: REVERSE PERCENTAGES</text>
  
  <!-- Side by Side Boxes (Generous Width & Padding) -->
  <!-- Left Box: The Red Error Trap -->
  <rect x="16" y="54" width="246" height="175" rx="8" fill="#fff1f2" stroke="#fca5a5" stroke-width="2"/>
  <rect x="26" y="64" width="226" height="26" rx="5" fill="#fee2e2"/>
  <text x="36" y="81" font-size="10" font-weight="900" fill="#991b1b">✕ COMMON FAILURE TRAP (BKSB)</text>
  
  <text x="28" y="106" font-size="9.5" fill="#881337">Problem: Sale price = £120 after 20% discount.</text>
  <text x="28" y="124" font-size="10" font-weight="800" fill="#b91c1c">Faulty Working:</text>
  <text x="28" y="140" font-size="10" fill="#881337">20% of £120 = £24</text>
  <text x="28" y="156" font-size="10" fill="#881337">£120 + £24 = £144.00</text>
  
  <rect x="24" y="168" width="230" height="48" rx="5" fill="#fee2e2"/>
  <text x="32" y="184" font-size="9" font-weight="800" fill="#991b1b">FATAL FLAW: You cannot add 20% of the</text>
  <text x="32" y="198" font-size="9" font-weight="800" fill="#991b1b">discounted £120 to recover 100% original value!</text>
  <text x="32" y="210" font-size="8.5" fill="#b91c1c">The 20% was deducted from a LARGER starting sum.</text>

  <!-- Right Box: The Golden Rule Method -->
  <rect x="278" y="54" width="246" height="175" rx="8" fill="#f0fdf4" stroke="#86efac" stroke-width="2"/>
  <rect x="288" y="64" width="226" height="26" rx="5" fill="#dcfce7"/>
  <text x="298" y="81" font-size="10" font-weight="900" fill="#166534">✓ GOLDEN RULE METHOD (ABDUL)</text>
  
  <text x="290" y="106" font-size="9.5" fill="#14532d">Sale price £120 represents 80% (100% - 20%).</text>
  <text x="290" y="124" font-size="10" font-weight="800" fill="#15803d">Single-Step Multiplier Method:</text>
  <text x="290" y="140" font-size="10" fill="#14532d">Multiplier = 1.00 - 0.20 = 0.80</text>
  <text x="290" y="158" font-size="12" font-weight="900" fill="#15803d">£120 &divide; 0.80 = £150.00 ✓</text>
  
  <rect x="286" y="168" width="230" height="48" rx="5" fill="#dcfce7"/>
  <text x="294" y="184" font-size="9" font-weight="800" fill="#166534">VERIFICATION CHECK:</text>
  <text x="294" y="198" font-size="9" fill="#15803d">20% of £150 = £30.00.</text>
  <text x="294" y="210" font-size="9" font-weight="800" fill="#166534">£150 - £30 = £120. Perfectly verified! ✓</text>

  <!-- Footer Progress Bar -->
  <rect x="14" y="238" width="512" height="28" rx="6" fill="#eff6ff" stroke="#bfdbfe"/>
  <text x="26" y="256" font-size="10" font-weight="800" fill="#1d4ed8">Target Mastery Progression: Level 1 Emerging (42%) ➔ Level 2 Secure (84%) Sign-Off</text>
</svg>"""

def get_speech_wireframe_svg():
    return """<svg viewBox="0 0 480 280" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:480px; height:auto; font-family:'Plus Jakarta Sans', sans-serif;">
  <rect x="2" y="2" width="476" height="276" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
  <rect x="16" y="12" width="448" height="38" rx="6" fill="#0f766e"/>
  <text x="28" y="28" font-size="10.5" font-weight="800" fill="#a7f3d0">PRESENTATION &amp; SPEECH SCRIPT &bull; FORMAT 5</text>
  <text x="28" y="42" font-size="9" fill="#ffffff">Rhetorical devices &bull; Stage directions &bull; Rule of three</text>
  
  <!-- Opening hook -->
  <rect x="16" y="58" width="448" height="44" rx="6" fill="#f0fdf4" stroke="#86efac"/>
  <text x="26" y="74" font-size="10.5" font-weight="900" fill="#166534">1. Engaging Rhetorical Opening Hook</text>
  <text x="26" y="92" font-size="9.5" font-style="italic" fill="#15803d">"Good morning colleagues. Imagine walking into a hospital ward where..." [Pause for effect]</text>
  
  <!-- Rule of Three & Body Points -->
  <rect x="16" y="110" width="448" height="82" rx="6" fill="#f8fafc" stroke="#e2e8f0"/>
  <text x="26" y="128" font-size="10.5" font-weight="900" fill="#0f172a">2. Core Message with Rule of Three &amp; Emotive Language</text>
  <text x="36" y="146" font-size="9.5" font-weight="700" fill="#0f766e">&bull; Professional: Maintaining statutory safety standards at all times</text>
  <text x="36" y="162" font-size="9.5" font-weight="700" fill="#0f766e">&bull; Compassionate: Putting patient dignity at the heart of our service</text>
  <text x="36" y="178" font-size="9.5" font-weight="700" fill="#0f766e">&bull; Dedicated: Supporting apprentices as they progress into band 3 roles</text>
  
  <!-- Audience Interaction & Closing Call to Action -->
  <rect x="16" y="200" width="448" height="66" rx="6" fill="#eff6ff" stroke="#bfdbfe"/>
  <text x="26" y="216" font-size="10.5" font-weight="900" fill="#1e40af">3. Audience Engagement &amp; Memorable Call to Action</text>
  <text x="26" y="234" font-size="9.5" fill="#1e3a8a">"Together, we can achieve 100% compliance. Thank you for your time." [Slide: Q&amp;A]</text>
  <text x="26" y="252" font-size="9.5" font-weight="800" fill="#2563eb">"I would now like to welcome questions from the floor."</text>
</svg>"""

def get_leaflet_wireframe_svg():
    return """<svg viewBox="0 0 480 280" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:480px; height:auto; font-family:'Plus Jakarta Sans', sans-serif;">
  <rect x="2" y="2" width="476" height="276" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
  <!-- 3-Panel Fold Lines -->
  <line x1="160" y1="2" x2="160" y2="278" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="5 4"/>
  <line x1="320" y1="2" x2="320" y2="278" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="5 4"/>
  
  <!-- Panel 1: Inside Left (Information) -->
  <rect x="10" y="12" width="140" height="26" rx="4" fill="#0284c7"/>
  <text x="80" y="29" font-size="9.5" font-weight="900" fill="#ffffff" text-anchor="middle">1. WHY JOIN US?</text>
  <rect x="10" y="46" width="140" height="60" rx="4" fill="#f0f9ff"/>
  <text x="16" y="62" font-size="8.5" font-weight="800" fill="#0369a1">&bull; Free accredited training</text>
  <text x="16" y="76" font-size="8.5" font-weight="800" fill="#0369a1">&bull; Flexible shift rotas</text>
  <text x="16" y="90" font-size="8.5" font-weight="800" fill="#0369a1">&bull; Expert 1-to-1 lead tutor</text>
  <rect x="10" y="114" width="140" height="152" rx="4" fill="#e2e8f0"/>
  <text x="80" y="190" font-size="9" font-weight="800" fill="#64748b" text-anchor="middle">📷 [Clinic Photo Spread]</text>
  
  <!-- Panel 2: Inside Middle (Course Modules) -->
  <rect x="170" y="12" width="140" height="26" rx="4" fill="#0369a1"/>
  <text x="240" y="29" font-size="9.5" font-weight="900" fill="#ffffff" text-anchor="middle">2. KEY MODULES</text>
  <rect x="170" y="46" width="140" height="24" rx="4" fill="#eff6ff"/>
  <text x="176" y="62" font-size="8.5" font-weight="800" fill="#1e40af">✓ Functional Maths L2</text>
  <rect x="170" y="74" width="140" height="24" rx="4" fill="#eff6ff"/>
  <text x="176" y="90" font-size="8.5" font-weight="800" fill="#1e40af">✓ English Writing Mastery</text>
  <rect x="170" y="102" width="140" height="24" rx="4" fill="#eff6ff"/>
  <text x="176" y="118" font-size="8.5" font-weight="800" fill="#1e40af">✓ Digital Skills (EDSQ)</text>
  <rect x="170" y="132" width="140" height="134" rx="4" fill="#f8fafc" stroke="#e2e8f0"/>
  <text x="240" y="156" font-size="9" font-weight="900" fill="#0f172a" text-anchor="middle">Student Testimonial</text>
  <text x="240" y="176" font-size="8" font-style="italic" fill="#475569" text-anchor="middle">"Passed first time with"</text>
  <text x="240" y="190" font-size="8" font-style="italic" fill="#475569" text-anchor="middle">"Abdul's step-by-step drills!"</text>
  
  <!-- Panel 3: Front Cover & Contact (Right) -->
  <rect x="330" y="12" width="140" height="32" rx="4" fill="#070d1e"/>
  <text x="400" y="27" font-size="9.5" font-weight="900" fill="#38bdf8" text-anchor="middle">MASTER SKILLS</text>
  <text x="400" y="38" font-size="7.5" fill="#ffffff" text-anchor="middle">Oxford Health NHS</text>
  <rect x="330" y="50" width="140" height="110" rx="4" fill="#e2e8f0"/>
  <text x="400" y="106" font-size="9" font-weight="800" fill="#64748b" text-anchor="middle">📷 [Learner Cover]</text>
  <rect x="330" y="168" width="140" height="98" rx="4" fill="#dcfce7" stroke="#86efac"/>
  <text x="400" y="186" font-size="9" font-weight="900" fill="#166534" text-anchor="middle">CONTACT &amp; ENROL</text>
  <text x="338" y="204" font-size="8" fill="#15803d">📞 01865 901000</text>
  <text x="338" y="220" font-size="8" fill="#15803d">✉️ training@mfs.org.uk</text>
  <text x="338" y="236" font-size="8" fill="#15803d">🌐 masterfunctionalskills.co.uk</text>
</svg>"""

def get_digital_gui_svg():
    return """<svg viewBox="0 0 480 280" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:480px; height:auto; font-family:'Plus Jakarta Sans', sans-serif;">
  <rect x="2" y="2" width="476" height="276" rx="10" fill="#090d16" stroke="#00e5ff" stroke-width="2"/>
  
  <!-- Top Menu Bar -->
  <rect x="2" y="2" width="476" height="30" rx="10 10 0 0" fill="#111827"/>
  <text x="16" y="20" font-size="11" font-weight="900" fill="#00e5ff">OS Desktop &bull; Window Manager (Skill Area 1)</text>
  
  <!-- Window 1: File Explorer (Spacious Left) -->
  <rect x="14" y="42" width="220" height="190" rx="6" fill="#1e293b" stroke="#334155"/>
  <rect x="14" y="42" width="220" height="26" rx="6 6 0 0" fill="#0f172a"/>
  <text x="24" y="59" font-size="9.5" font-weight="800" fill="#94a3b8">📁 File Explorer — /Documents</text>
  
  <text x="24" y="86" font-size="9" font-weight="700" fill="#38bdf8">📁 NHS_Oxford_Health/</text>
  <text x="36" y="104" font-size="8.5" fill="#cbd5e1">📄 Patient_Rota.xlsx</text>
  <text x="36" y="120" font-size="8.5" fill="#cbd5e1">📄 Handover_Notes.docx</text>
  
  <text x="24" y="142" font-size="9" font-weight="700" fill="#38bdf8">📁 Functional_Skills_Revision/</text>
  <text x="36" y="160" font-size="8.5" fill="#cbd5e1">📄 Mock_Exam_Maths_L2.pdf</text>
  <text x="36" y="176" font-size="8.5" fill="#cbd5e1">📄 Practice_Drills_Abdul.docx</text>
  <text x="36" y="192" font-size="8.5" fill="#cbd5e1">📄 Diagnostic_Tracker.xlsx</text>
  
  <!-- Window 2: Web Browser (Spacious Right) -->
  <rect x="246" y="42" width="220" height="190" rx="6" fill="#0f172a" stroke="#00e5ff"/>
  <rect x="246" y="42" width="220" height="26" rx="6 6 0 0" fill="#1e293b"/>
  <!-- URL Bar with Padlock -->
  <rect x="256" y="47" width="200" height="16" rx="4" fill="#090d16" stroke="#334155"/>
  <text x="264" y="59" font-size="8" font-weight="800" fill="#10b981">🔒 https://masterfunctionalskills.co.uk</text>
  
  <rect x="256" y="78" width="200" height="48" rx="5" fill="#1e293b"/>
  <text x="266" y="98" font-size="10" font-weight="900" fill="#38bdf8">Digital Skills Mastery</text>
  <text x="266" y="114" font-size="8" fill="#94a3b8">Interactive learning &amp; exam portal</text>
  
  <rect x="256" y="136" width="94" height="42" rx="4" fill="#1e293b"/>
  <text x="266" y="158" font-size="8.5" font-weight="800" fill="#fbbf24">Level 1 EDSQ</text>
  <rect x="362" y="136" width="94" height="42" rx="4" fill="#1e293b"/>
  <text x="372" y="158" font-size="8.5" font-weight="800" fill="#10b981">Level 2 DFS</text>
  
  <!-- Taskbar at bottom -->
  <rect x="2" y="244" width="476" height="34" rx="0 0 10 10" fill="#030712" stroke="#1f2937"/>
  <rect x="12" y="248" width="24" height="24" rx="4" fill="#00e5ff"/>
  <text x="24" y="264" font-size="12" font-weight="900" fill="#090d16" text-anchor="middle">❖</text>
  <rect x="44" y="250" width="22" height="22" rx="4" fill="#1f2937"/>
  <rect x="72" y="250" width="22" height="22" rx="4" fill="#1f2937"/>
  <rect x="100" y="250" width="22" height="22" rx="4" fill="#1f2937"/>
  <text x="465" y="266" font-size="9" fill="#94a3b8" text-anchor="end">17:05 &bull; 12 Oct 2026</text>
</svg>"""

def get_spreadsheet_wireframe_svg():
    return """<svg viewBox="0 0 480 280" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:480px; height:auto; font-family:'Plus Jakarta Sans', sans-serif;">
  <rect x="2" y="2" width="476" height="276" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
  <rect x="2" y="2" width="476" height="30" rx="10 10 0 0" fill="#15803d"/>
  <text x="16" y="20" font-size="11" font-weight="800" fill="#ffffff">Microsoft Excel / Google Sheets &bull; Spreadsheet Anatomy</text>
  
  <!-- Formula Bar -->
  <rect x="12" y="40" width="70" height="22" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
  <text x="47" y="55" font-size="10" font-weight="800" fill="#0f172a" text-anchor="middle">C6</text>
  <rect x="90" y="40" width="378" height="22" rx="4" fill="#ffffff" stroke="#00e5ff" stroke-width="1.5"/>
  <text x="102" y="55" font-size="10" font-weight="800" fill="#15803d">fx <tspan fill="#0f172a" font-weight="700">=SUM(C2:C5) * 1.20</tspan></text>
  
  <!-- Column Headers -->
  <rect x="12" y="70" width="456" height="22" fill="#e2e8f0"/>
  <text x="30" y="85" font-size="9" font-weight="800" fill="#64748b" text-anchor="middle">#</text>
  <text x="110" y="85" font-size="9" font-weight="800" fill="#64748b">A: Item Description</text>
  <text x="260" y="85" font-size="9" font-weight="800" fill="#64748b">B: Quantity</text>
  <text x="380" y="85" font-size="9" font-weight="800" fill="#64748b">C: Total (£)</text>
  
  <!-- Rows (Spacious) -->
  <rect x="12" y="94" width="456" height="22" fill="#ffffff" stroke="#f1f5f9"/>
  <text x="30" y="109" font-size="8.5" fill="#94a3b8" text-anchor="middle">2</text>
  <text x="110" y="109" font-size="9" fill="#0f172a">Bandages (Box 50)</text>
  <text x="260" y="109" font-size="9" fill="#0f172a">14</text>
  <text x="380" y="109" font-size="9" font-weight="800" fill="#0f172a">£168.00</text>
  
  <rect x="12" y="118" width="456" height="22" fill="#f8fafc" stroke="#f1f5f9"/>
  <text x="30" y="133" font-size="8.5" fill="#94a3b8" text-anchor="middle">3</text>
  <text x="110" y="133" font-size="9" fill="#0f172a">Surgical Gloves (Box 100)</text>
  <text x="260" y="133" font-size="9" fill="#0f172a">25</text>
  <text x="380" y="133" font-size="9" font-weight="800" fill="#0f172a">£212.50</text>
  
  <rect x="12" y="142" width="456" height="22" fill="#ffffff" stroke="#f1f5f9"/>
  <text x="30" y="157" font-size="8.5" fill="#94a3b8" text-anchor="middle">4</text>
  <text x="110" y="157" font-size="9" fill="#0f172a">Digital Thermometer Units</text>
  <text x="260" y="157" font-size="9" fill="#0f172a">8</text>
  <text x="380" y="157" font-size="9" font-weight="800" fill="#0f172a">£156.00</text>
  
  <rect x="12" y="166" width="456" height="22" fill="#f8fafc" stroke="#f1f5f9"/>
  <text x="30" y="181" font-size="8.5" fill="#94a3b8" text-anchor="middle">5</text>
  <text x="110" y="181" font-size="9" fill="#0f172a">Syringe Packs (Pack 100)</text>
  <text x="260" y="181" font-size="9" fill="#0f172a">12</text>
  <text x="380" y="181" font-size="9" font-weight="800" fill="#0f172a">£84.00</text>
  
  <!-- Grand Total Row -->
  <rect x="12" y="190" width="456" height="28" fill="#dcfce7" stroke="#86efac" stroke-width="1.5"/>
  <text x="30" y="208" font-size="9" font-weight="900" fill="#166534" text-anchor="middle">6</text>
  <text x="110" y="208" font-size="10" font-weight="900" fill="#166534">GRAND TOTAL WITH VAT (20%)</text>
  <text x="380" y="208" font-size="11" font-weight="900" fill="#15803d">£744.60 ✓</text>
  
  <!-- Callout note -->
  <rect x="12" y="226" width="456" height="42" rx="5" fill="#eff6ff" stroke="#bfdbfe"/>
  <text x="22" y="242" font-size="8.5" font-weight="800" fill="#1d4ed8">💡 Key Functions: =SUM(range), =AVERAGE(range), =COUNT(range), =MAX/MIN(range)</text>
  <text x="22" y="258" font-size="8" fill="#475569">Formula rule: Always begin with an equals sign (=) or the spreadsheet treats entry as text.</text>
</svg>"""

def get_flashcard_mockup_svg():
    return """<svg viewBox="0 0 480 270" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:480px; height:auto; font-family:'Plus Jakarta Sans', sans-serif;">
  <rect x="2" y="2" width="476" height="266" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  
  <!-- Card Mockup 1: Front (Spacious) -->
  <rect x="20" y="20" width="210" height="230" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <rect x="20" y="20" width="210" height="30" rx="8 8 0 0" fill="#003366"/>
  <text x="125" y="40" font-size="9.5" font-weight="900" fill="#38bdf8" text-anchor="middle">REVISION CARD &bull; MATHS L2</text>
  <text x="125" y="74" font-size="12" font-weight="900" fill="#002046" text-anchor="middle">REVERSE PERCENTAGE</text>
  
  <rect x="30" y="84" width="190" height="54" rx="5" fill="#f8fafc" stroke="#e2e8f0"/>
  <text x="125" y="102" font-size="9" font-weight="800" fill="#0284c7" text-anchor="middle">Master Formula:</text>
  <text x="125" y="122" font-size="10.5" font-weight="900" fill="#0f172a" text-anchor="middle">Original = Final &divide; Multiplier</text>
  
  <text x="125" y="156" font-size="8.5" font-weight="800" fill="#b91c1c" text-anchor="middle">&bull; NEVER add % of final discounted value!</text>
  
  <rect x="30" y="168" width="190" height="52" rx="5" fill="#eff6ff" stroke="#bfdbfe"/>
  <text x="125" y="188" font-size="8.5" font-weight="700" fill="#1e40af" text-anchor="middle">£468 after 20% discount:</text>
  <text x="125" y="206" font-size="10" font-weight="900" fill="#1d4ed8" text-anchor="middle">£468 &divide; 0.80 = £585.00 ✓</text>

  <!-- Card Mockup 2: Postcard Back (Spacious) -->
  <rect x="250" y="20" width="210" height="230" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <rect x="250" y="20" width="210" height="30" rx="8 8 0 0" fill="#059669"/>
  <text x="355" y="40" font-size="9.5" font-weight="900" fill="#ffffff" text-anchor="middle">TRY IT NOW &bull; 60 SEC DRILL</text>
  
  <text x="262" y="74" font-size="9.5" font-weight="800" fill="#0f172a">A TV costs £360 including 20% VAT.</text>
  <text x="262" y="90" font-size="9" fill="#475569">What was the pre-VAT price?</text>
  
  <rect x="260" y="102" width="190" height="54" rx="5" fill="#fffbeb" stroke="#fde68a"/>
  <text x="268" y="120" font-size="8.5" font-weight="800" fill="#92400e">Step 1: Multiplier = 1.20</text>
  <text x="268" y="138" font-size="8.5" font-weight="800" fill="#92400e">Step 2: £360 &divide; 1.20 = £300.00 ✓</text>
  
  <rect x="260" y="166" width="190" height="54" rx="5" fill="#dcfce7" stroke="#86efac"/>
  <text x="355" y="186" font-size="9" font-weight="900" fill="#166534" text-anchor="middle">Tutor Sign-Off: Abdul ✓</text>
  <text x="355" y="204" font-size="8" fill="#15803d" text-anchor="middle">Oxford Health NHS Apprenticeships</text>
</svg>"""



# =============================================================================
# COMPLETE BOOK AUDIT CATALOG DATASET (100 AUDIT ITEMS)
# =============================================================================

# Audit items across all 17 books and visual types
AUDIT_ITEMS = [
    # -------------------------------------------------------------------------
    # SUITE 1: 3D COVERS & VISUAL IDENTITY (ALL 17 BOOKS)
    # -------------------------------------------------------------------------
    {
        "id": "cover-maths-l2-core",
        "book": "Maths Level 2 Core Guide",
        "suite": "covers",
        "subject": "maths",
        "type": "cover",
        "topic": "Book Cover & 3D Render: Level 2 Maths Core Guide",
        "context": "Front cover, back cover, spine, and 3D marketing render for 104-page print publication.",
        "current_visual": "assets/img/books/3d_maths_l2_core.png",
        "current_type": "img",
        "current_file": "assets/img/books/3d_maths_l2_core.png",
        "issue": "Midnight Sapphire (#002046) palette is solid, but the cover background texture uses a generic math calculation overlay. Needs distinct NHS / engineering vocational blueprint motif.",
        "proposed_concept": "Distinctive Royal Navy with electric sky-blue accents (#38bdf8), official Ofqual/Edexcel criteria badge, bold 'FOUNDATIONS TO MASTERY' knockout lettering, and authentic clinical/trade measurement blueprint texture.",
        "recommended_action": "Apply clean high-contrast Lexend typography, embossed gold spine badge, and vocational NHS/engineering texture.",
        "tags": ["A4 Print Spec", "104 Pages", "Ofqual Regulated", "Level 2"]
    },
    {
        "id": "cover-maths-l2-comp",
        "book": "Maths Level 2 Companion Workbook",
        "suite": "covers",
        "subject": "maths",
        "type": "cover",
        "topic": "Book Cover & 3D Render: Level 2 Companion Workbook",
        "context": "Front cover and 3D render for 86-page practice workbook featuring lined calculation frames.",
        "current_visual": "assets/img/books/3d_maths_l2_companion.png",
        "current_type": "img",
        "current_file": "assets/img/books/3d_maths_l2_companion.png",
        "issue": "Shares very similar appearance to Core Guide. Learners may confuse workbook with textbook on shelf.",
        "proposed_concept": "Inverted high-contrast white-card styling with Navy borders and prominent orange/gold 'PRACTICE WORKBOOK & EXAM DRILLS' badge to immediately distinguish from Core Guide.",
        "recommended_action": "Clear visual differentiation between Core Textbook (Dark Navy) and Companion Workbook (Vibrant Practice Layout).",
        "tags": ["A4 Print Spec", "86 Pages", "Calculation Grids", "Level 2"]
    },
    {
        "id": "cover-maths-l1-core",
        "book": "Maths Level 1 Core Guide",
        "suite": "covers",
        "subject": "maths",
        "type": "cover",
        "topic": "Book Cover & 3D Render: Level 1 Maths Core Guide",
        "context": "Front cover and 3D render for 104-page Level 1 Maths publication.",
        "current_visual": "assets/img/books/3d_maths_l1_core.png",
        "current_type": "img",
        "current_file": "assets/img/books/3d_maths_l1_core.png",
        "issue": "Emerald green (#047857) theme is clear, but lacks vocational trade equipment graphics.",
        "proposed_concept": "Rich Emerald Green with bright citrus accents, featuring subtle trade workshop measuring tape and warehouse logistics background motif.",
        "recommended_action": "Reinforce Level 1 practical vocational focus with tools / retail trade motifs.",
        "tags": ["A4 Print Spec", "104 Pages", "Emerald Green", "Level 1"]
    },
    {
        "id": "cover-maths-l1-comp",
        "book": "Maths Level 1 Companion Workbook",
        "suite": "covers",
        "subject": "maths",
        "type": "cover",
        "topic": "Book Cover & 3D Render: Level 1 Companion Workbook",
        "context": "Front cover and 3D render for 86-page practice drills workbook.",
        "current_visual": "assets/img/books/3d_maths_l1_companion.png",
        "current_type": "img",
        "current_file": "assets/img/books/3d_maths_l1_companion.png",
        "issue": "Cover subtitle wording could more strongly emphasize step-by-step dyslexia-friendly formatting.",
        "proposed_concept": "High-contrast clean layout featuring 'STEP-BY-STEP CALCULATION FRAMES & REAL-WORLD SCENARIOS' with green header banner.",
        "recommended_action": "Ensure dyslexia-friendly high-contrast badge is prominently positioned on front cover.",
        "tags": ["A4 Print Spec", "86 Pages", "Dyslexia Friendly", "Level 1"]
    },
    {
        "id": "cover-maths-e3-core",
        "book": "Maths Entry Level 3 Core Guide",
        "suite": "covers",
        "subject": "maths",
        "type": "cover",
        "topic": "Book Cover & 3D Render: Entry Level 3 Maths Core Guide",
        "context": "Front cover and 3D render for 92-page foundational guide for Entry 3 candidates.",
        "current_visual": "assets/img/books/3d_maths_e3_core.png",
        "current_type": "img",
        "current_file": "assets/img/books/3d_maths_e3_core.png",
        "issue": "Rich Crimson Red (#991b1b) is good, but typography should be larger and friendlier to reduce math anxiety.",
        "proposed_concept": "Warm Crimson Red with sunny gold accents, friendly rounded Lexend 14pt typography, and cartoon tutor Abdul welcoming learners.",
        "recommended_action": "Incorporate friendly supportive visual cues for adult learners returning to study.",
        "tags": ["A4 Print Spec", "92 Pages", "Crimson Red", "Entry 3"]
    },
    {
        "id": "cover-eng-l2-core",
        "book": "English Writing Level 2 Core Guide",
        "suite": "covers",
        "subject": "english",
        "type": "cover",
        "topic": "Book Cover & 3D Render: Level 2 English Writing Core Guide",
        "context": "Front cover and 3D render for 104-page writing guide.",
        "current_visual": "assets/img/books/3d_level2_core.png",
        "current_type": "img",
        "current_file": "assets/img/books/3d_level2_core.png",
        "issue": "Classic Oxford Royal Blue (#003366) texture shows hands writing on paper, which is good, but lacks clear format badge pills.",
        "proposed_concept": "Add format badge pills on front cover: 'Articles &bull; Formal Letters &bull; Reports &bull; Speeches &bull; Emails' to instantly demonstrate Pearson curriculum breadth.",
        "recommended_action": "Display all 11 Pearson Edexcel writing formats directly on front cover ribbon.",
        "tags": ["A4 Print Spec", "104 Pages", "Royal Blue", "Level 2 Writing"]
    },
    {
        "id": "cover-eng-l2-comp",
        "book": "English Writing Level 2 Companion Workbook",
        "suite": "covers",
        "subject": "english",
        "type": "cover",
        "topic": "Book Cover & 3D Render: Level 2 English Writing Companion Workbook",
        "context": "Front cover and 3D render for 86-page guided writing practice workbook.",
        "current_visual": "assets/img/books/3d_level2_companion.png",
        "current_type": "img",
        "current_file": "assets/img/books/3d_level2_companion.png",
        "issue": "Looks identical to Core textbook. Needs clear visual cue indicating lined writing frames.",
        "proposed_concept": "Crisp white front cover with Royal Blue header ribbon and visual lined paper watermark badge.",
        "recommended_action": "Feature candidate writing frame preview directly on cover.",
        "tags": ["A4 Print Spec", "86 Pages", "Lined Frames", "Level 2 Writing"]
    },
    {
        "id": "cover-eng-l1-core",
        "book": "English Writing Level 1 Core Guide",
        "suite": "covers",
        "subject": "english",
        "type": "cover",
        "topic": "Book Cover & 3D Render: Level 1 English Writing Core Guide",
        "context": "Front cover and 3D render for 104-page Level 1 writing guide.",
        "current_visual": "assets/img/books/3d_level1_core.png",
        "current_type": "img",
        "current_file": "assets/img/books/3d_level1_core.png",
        "issue": "Deep Forest Teal Green (#0c4e45) color scheme is great. Ensure knockout word 'LITERACY' is crisply legible.",
        "proposed_concept": "Deep Forest Teal with gold typography, highlighting simple sentences, format conventions, and workplace communication.",
        "recommended_action": "Maintain clear distinct forest teal identity distinguishing Level 1 English from Maths.",
        "tags": ["A4 Print Spec", "104 Pages", "Forest Teal", "Level 1 Writing"]
    },
    {
        "id": "cover-eng-l1-comp",
        "book": "English Writing Level 1 Companion Workbook",
        "suite": "covers",
        "subject": "english",
        "type": "cover",
        "topic": "Book Cover & 3D Render: Level 1 English Writing Companion Workbook",
        "context": "Front cover and 3D render for 86-page companion workbook.",
        "current_visual": "assets/img/books/3d_level1_companion.png",
        "current_type": "img",
        "current_file": "assets/img/books/3d_level1_companion.png",
        "issue": "Ensure 3D render reflects high-contrast practice layout.",
        "proposed_concept": "Companion edition with green framing, featuring 22 guided writing tasks and vocabulary banks.",
        "recommended_action": "Confirm synchronized cover artwork with Level 1 Core edition.",
        "tags": ["A4 Print Spec", "86 Pages", "Practice Tasks", "Level 1 Writing"]
    },
    {
        "id": "cover-eng-e3-core",
        "book": "English Entry Level 3 Core Guide",
        "suite": "covers",
        "subject": "english",
        "type": "cover",
        "topic": "Book Cover & 3D Render: Entry Level 3 English Core Guide",
        "context": "Front cover and 3D render for 92-page foundational English publication.",
        "current_visual": "assets/img/books/3d_english_e3_core.png",
        "current_type": "img",
        "current_file": "assets/img/books/3d_english_e3_core.png",
        "issue": "Needs clear callout of sentence building blocks and high-frequency spelling word lists.",
        "proposed_concept": "Rosewood Crimson with yellow gold accents, featuring sentence building block motifs and dyslexia-friendly 14pt badge.",
        "recommended_action": "Emphasize supportive sentence building frameworks.",
        "tags": ["A4 Print Spec", "92 Pages", "Rosewood Red", "Entry 3 Literacy"]
    },
    {
        "id": "cover-read-l2-core",
        "book": "English Reading Level 2 Core Guide",
        "suite": "covers",
        "subject": "reading",
        "type": "cover",
        "topic": "Book Cover & 3D Render: Level 2 English Reading Core Guide",
        "context": "Front cover and 3D render for 84-page comprehensive reading analysis guide.",
        "current_visual": "assets/img/books/3d_reading_l2_core.png",
        "current_type": "img",
        "current_file": "assets/img/books/3d_reading_l2_core.png",
        "issue": "Deep Midnight Indigo palette needs distinct magnifying glass and dual-text comparative analysis emblem.",
        "proposed_concept": "Deep Indigo Navy with cyan highlights, featuring stylized open broadsheet comparison graphic.",
        "recommended_action": "Highlight Text A vs Text B comparative synthesis on cover badge.",
        "tags": ["A4 Print Spec", "84 Pages", "Deep Indigo", "Level 2 Reading"]
    },
    {
        "id": "cover-read-l1-core",
        "book": "English Reading Level 1 Core Guide",
        "suite": "covers",
        "subject": "reading",
        "type": "cover",
        "topic": "Book Cover & 3D Render: Level 1 English Reading Core Guide",
        "context": "Front cover and 3D render for 84-page Level 1 reading guide.",
        "current_visual": "assets/img/books/3d_reading_l1_core.png",
        "current_type": "img",
        "current_file": "assets/img/books/3d_reading_l1_core.png",
        "issue": "Distinct teal-cyan identity needed to differentiate from Level 2 Reading.",
        "proposed_concept": "Vibrant Teal Blue with gold typography, highlighting organizational layout markers and main ideas.",
        "recommended_action": "Emphasize practical workplace notices, leaflets, and instructions.",
        "tags": ["A4 Print Spec", "84 Pages", "Teal Blue", "Level 1 Reading"]
    },
    {
        "id": "cover-digital-skills",
        "book": "Digital Skills Handbook (EDSQ / DFS)",
        "suite": "covers",
        "subject": "specialist",
        "type": "cover",
        "topic": "Book Cover & 3D Render: Essential Digital Skills Practical Handbook",
        "context": "Front cover and 3D render for 86-page digital functional skills guide.",
        "current_visual": "assets/img/books/3d_digital_skills.png",
        "current_type": "img",
        "current_file": "assets/img/books/3d_digital_skills.png",
        "issue": "Cyber Midnight (#090d16) and Neon Cyan (#00e5ff) is very modern. Verify 5 core skills are badged on cover.",
        "proposed_concept": "High-tech midnight cyber palette with electric cyan circuits, badging all 5 DfE/Ofqual standards: Devices, Creating, Communicating, Transacting, Online Safety.",
        "recommended_action": "Feature modern digital tablet & cloud security icons.",
        "tags": ["A4 Print Spec", "86 Pages", "Neon Cyan", "Digital Skills"]
    },
    {
        "id": "cover-spag-mastery",
        "book": "SPaG Handbook & Mastery Drills",
        "suite": "covers",
        "subject": "spag",
        "type": "cover",
        "topic": "Book Cover & 3D Render: SPaG Handbook & Mastery Drills",
        "context": "Front cover and 3D render for 84-page spelling, punctuation, and grammar mastery manual.",
        "current_visual": "assets/img/books/3d_spag_mastery.png",
        "current_type": "img",
        "current_file": "assets/img/books/3d_spag_mastery.png",
        "issue": "Imperial Royal Violet (#581c87) with Warm Gold is striking. Ensure Murphy cartoon styling is credited.",
        "proposed_concept": "Imperial Royal Violet with gold lettering, featuring Murphy-style cartoon tutor Abdul and Priya speech bubbles.",
        "recommended_action": "Showcase Murphy spread cartoon approach directly on front and back covers.",
        "tags": ["A4 Print Spec", "84 Pages", "Royal Violet", "SPaG Mastery"]
    },
    {
        "id": "cover-bksb-remediation",
        "book": "BKSB Remediation Workbook",
        "suite": "covers",
        "subject": "specialist",
        "type": "cover",
        "topic": "Book Cover & 3D Render: BKSB & OneAdvanced Remediation Workbook",
        "context": "Front cover and 3D render for 86-page diagnostic gap remediation publication.",
        "current_visual": "assets/img/books/3d_bksb_remediation.png",
        "current_type": "img",
        "current_file": "assets/img/books/3d_bksb_remediation.png",
        "issue": "Electric Cobalt (#1d4ed8) and Safety Amber (#f59e0b) design is good. Highlight Stage 1 vs Stage 2 remediation methodology.",
        "proposed_concept": "High-impact diagnostic cobalt cover with '24 HIGH-FREQUENCY FAILURE MODES & RETRY DRILLS' badge ribbon.",
        "recommended_action": "Clearly badge BKSB & OneAdvanced compatibility for FE colleges and NHS apprenticeships.",
        "tags": ["A4 Print Spec", "86 Pages", "Cobalt & Amber", "BKSB Remediation"]
    },
    {
        "id": "cover-mock-maths-l2",
        "book": "Maths Level 2 Mock Exam Pack",
        "suite": "covers",
        "subject": "maths",
        "type": "cover",
        "topic": "Book Cover & 3D Render: Maths Level 2 Mock Exam Pack (5 Full Papers)",
        "context": "Front cover and 3D render for official exam simulation pack.",
        "current_visual": "assets/img/books/3d_mock_pack_maths_l2.png",
        "current_type": "img",
        "current_file": "assets/img/books/3d_mock_pack_maths_l2.png",
        "issue": "Exam Slate (#18181b) styling looks authoritative. Ensure Non-Calculator Section A and Calculator Section B breakdown is explicit.",
        "proposed_concept": "Official Examination Slate with Pearson Edexcel timing breakdown (25 min Non-Calc + 1h 20m Calc) and process mark scheme checklists.",
        "recommended_action": "Feature authentic exam booklet appearance with allocated mark badges.",
        "tags": ["A4 Print Spec", "5 Full Papers", "Exam Slate", "Maths L2 Mocks"]
    },
    {
        "id": "cover-mock-eng-l2",
        "book": "English Level 2 Mock Exam Pack",
        "suite": "covers",
        "subject": "english",
        "type": "cover",
        "topic": "Book Cover & 3D Render: English Level 2 Mock Exam Pack (5 Full Papers)",
        "context": "Front cover and 3D render for 5 full English exam papers.",
        "current_visual": "assets/img/books/3d_mock_pack_english_l2.png",
        "current_type": "img",
        "current_file": "assets/img/books/3d_mock_pack_english_l2.png",
        "issue": "Ensure Section A Reading and Section B Writing separation is highlighted.",
        "proposed_concept": "Official Examination Slate with 2-hour duration indicator and full indicative content mark schemes.",
        "recommended_action": "Maintain official board exam aesthetic for realistic learner practice.",
        "tags": ["A4 Print Spec", "5 Full Papers", "Exam Slate", "English L2 Mocks"]
    },

    # -------------------------------------------------------------------------
    # SUITE 2: MATHEMATICS SUITE (TECHNICAL SVGS & REAL-LIFE PHOTOS)
    # -------------------------------------------------------------------------
    {
        "id": "maths-diagram-grid-method",
        "book": "Maths Level 2 Core Guide",
        "suite": "maths",
        "subject": "maths",
        "type": "diagram",
        "topic": "Grid Method Long Multiplication (Standard N4)",
        "context": "Core teaching page in Strand 1 (Number). Explains partitioning 2-digit numbers into tens and units.",
        "current_visual": vcc.get_grid_method_svg(),
        "current_type": "svg",
        "current_file": "visual_curriculum_catalog.py (get_grid_method_svg)",
        "issue": "The SVG is mathematically accurate, but the diagonal summation line can be straightened for cleaner clarity.",
        "proposed_concept": "Straight horizontal subtotal rows with soft pastel blue fills, drop shadow depth, and bold green checkmark banner for final grand total.",
        "recommended_action": "Straighten alignment lines and use high-contrast colour coded headers (Tens = Dark Blue, Units = Sky Blue).",
        "tags": ["Inline SVG", "Dyslexia Friendly", "Grid Method", "Standard N4"]
    },
    {
        "id": "maths-photo-multiplication",
        "book": "Maths Level 2 Core Guide",
        "suite": "maths",
        "subject": "maths",
        "type": "photo",
        "topic": "Workplace Multiplication Scenario (Standard N4)",
        "context": "Hero photo at top of concept page 12 illustrating vocational context.",
        "current_visual": "assets/img/book_photos/construction_trades/timber_lumber_stack.jpg",
        "current_type": "img",
        "current_file": "construction_trades/timber_lumber_stack.jpg",
        "issue": "Timber stack photo is good, but construction estimator measuring site or brick pallet inventory would feel even more directly tied to calculating 46 packs × 35 units.",
        "proposed_concept": "Authentic photo of construction pallet packs with delivery manifest or timber stack multiplication on active UK building site.",
        "recommended_action": "Use high-resolution construction pallet photo with manifest sheet visible.",
        "tags": ["Hero Photo", "Trade Context", "Construction", "Standard N4"]
    },
    {
        "id": "maths-diagram-bus-stop",
        "book": "Maths Level 2 Core Guide",
        "suite": "maths",
        "subject": "maths",
        "type": "diagram",
        "topic": "Bus Stop Short Division (Standard N5)",
        "context": "Core teaching page in Strand 1. Step-by-step breakdown of short division with remainders.",
        "current_visual": vcc.get_bus_stop_svg(),
        "current_type": "svg",
        "current_file": "visual_curriculum_catalog.py (get_bus_stop_svg)",
        "issue": "Shows the static completed division bracket (936 ÷ 4 = 234). Would benefit from a 3-step carry arrow diagram.",
        "proposed_concept": "Interactive 3-step visual sequence: Step 1 (9÷4 = 2 r 1) -> Step 2 (carry 1 to make 13; 13÷4 = 3 r 1) -> Step 3 (carry 1 to make 16; 16÷4 = 4).",
        "recommended_action": "Add red carry annotations showing exact remainder transfer between digits.",
        "tags": ["Inline SVG", "Step-by-step", "Short Division", "Standard N5"]
    },
    {
        "id": "maths-photo-division",
        "book": "Maths Level 2 Core Guide",
        "suite": "maths",
        "subject": "maths",
        "type": "photo",
        "topic": "Pharmacy Unit Dispensing (Standard N5)",
        "context": "Hero photo introducing equal distribution and unit dosage calculation.",
        "current_visual": "assets/img/book_photos/healthcare_care/pharmacy_dispensing_bottles.jpg",
        "current_type": "img",
        "current_file": "healthcare_care/pharmacy_dispensing_bottles.jpg",
        "issue": "Good clinical setting, but lighting in current photo could be brighter for print reproduction.",
        "proposed_concept": "Bright clinical photo of NHS pharmacy technician dividing batch medication ampoules equally across ward trollies with medication chart.",
        "recommended_action": "Ensure high contrast and clean clinical lighting for crisp A4 print.",
        "tags": ["Hero Photo", "NHS Healthcare", "Dosage Units", "Standard N5"]
    },
    {
        "id": "maths-diagram-bidmas",
        "book": "Maths Level 2 Core Guide",
        "suite": "maths",
        "subject": "maths",
        "type": "diagram",
        "topic": "BIDMAS Hierarchical Pyramid (Standard N10)",
        "context": "Core teaching page for order of operations. Teaches Brackets, Indices, Division/Multiplication, Addition/Subtraction.",
        "current_visual": vcc.get_bidmas_svg(),
        "current_type": "svg",
        "current_file": "visual_curriculum_catalog.py (get_bidmas_svg)",
        "issue": "Previously represented by 4 horizontal formula boxes. A hierarchical pyramid is far more intuitive for adult learners.",
        "proposed_concept": "Tiered pyramid with Tier 1 Brackets (B) at apex, Tier 2 Indices (I), Tier 3 Division & Multiplication (D/M equal left-to-right), Tier 4 Addition & Subtraction (A/S base).",
        "recommended_action": "Use distinct pastel colour bands for each pyramid tier with worked formula annotations beside it.",
        "tags": ["Inline SVG", "Hierarchy Pyramid", "BIDMAS", "Standard N10"]
    },
    {
        "id": "maths-photo-bidmas",
        "book": "Maths Level 2 Core Guide",
        "suite": "maths",
        "subject": "maths",
        "type": "photo",
        "topic": "Scientific Calculator Finance (Standard N10)",
        "context": "Hero photo illustrating order of operations in financial mortgage formulas.",
        "current_visual": "assets/img/book_photos/money_shopping_bills/calculator_finance.jpg",
        "current_type": "img",
        "current_file": "money_shopping_bills/calculator_finance.jpg",
        "issue": "Shows general calculator on desk. Should show exact multi-line scientific display with brackets visible.",
        "proposed_concept": "Crisp photo of Casio fx-83/fx-85 scientific calculator display showing formula with brackets (180 - 4 × 5²) over financial ledger.",
        "recommended_action": "Highlight standard permitted exam calculator model with clear LCD display.",
        "tags": ["Hero Photo", "Finance Context", "Permitted Exam Tool", "Standard N10"]
    },
    {
        "id": "maths-diagram-place-value",
        "book": "Maths Level 1 Core Guide",
        "suite": "maths",
        "subject": "maths",
        "type": "diagram",
        "topic": "Place Value & Large Numbers Columns (Standard N1)",
        "context": "Foundational place value chart up to 1,000,000.",
        "current_visual": vcc.get_place_value_svg(),
        "current_type": "svg",
        "current_file": "visual_curriculum_catalog.py (get_place_value_svg)",
        "issue": "Column chart is functional, but column boundaries could be more visually distinct for dyslexia friendliness.",
        "proposed_concept": "Colour-differentiated place value columns (Millions = Purple, Thousands = Blue, Hundreds = Amber, Tens = Teal, Units = Green) with comma grouping markers.",
        "recommended_action": "Add comma separator indicators between thousand and unit periods.",
        "tags": ["Inline SVG", "Place Value", "Dyslexia Friendly", "Standard N1"]
    },
    {
        "id": "maths-photo-place-value",
        "book": "Maths Level 1 Core Guide",
        "suite": "maths",
        "subject": "maths",
        "type": "photo",
        "topic": "Warehouse Inventory Numbers (Standard N1)",
        "context": "Hero photo introducing 6-figure stock tracking.",
        "current_visual": "assets/img/book_photos/retail_shop/warehouse_stock.jpg",
        "current_type": "img",
        "current_file": "retail_shop/warehouse_stock.jpg",
        "issue": "Photo is reused in both place value and ordering numbers topics.",
        "proposed_concept": "Dedicated high-res photo of automated UK distribution center barcode scanner tracking batch SKU numbers up to 1,000,000.",
        "recommended_action": "Replace repeated warehouse image with dedicated logistics scanning visual.",
        "tags": ["Hero Photo", "Logistics", "Inventory SKU", "Standard N1"]
    },
    {
        "id": "maths-diagram-compound-area",
        "book": "Maths Level 2 Core Guide",
        "suite": "maths",
        "subject": "maths",
        "type": "diagram",
        "topic": "Compound L-Shape Area Decomposition (Standard M14)",
        "context": "Key Pearson Edexcel Level 2 exam skill. Calculating area of composite non-rectangular shapes.",
        "current_visual": vcc.get_compound_area_svg(),
        "current_type": "svg",
        "current_file": "visual_curriculum_catalog.py (get_compound_area_svg)",
        "issue": "Currently shows single split. Showing both Method 1 (horizontal split) and Method 2 (vertical split) side-by-side demonstrates verification.",
        "proposed_concept": "Dual decomposition diagram: Method 1 (split into A=8×5=40 and B=4×3=12 -> 52 m²) vs Method 2 (subtracted bounding box 8×8=64 - 12=52 m²).",
        "recommended_action": "Provide dual-method visual comparison to reinforce alternative checking methods.",
        "tags": ["Inline SVG", "Compound Area", "Exam Essential", "Standard M14"]
    },
    {
        "id": "maths-photo-compound-area",
        "book": "Maths Level 2 Core Guide",
        "suite": "maths",
        "subject": "maths",
        "type": "photo",
        "topic": "Floor Fitting & Tile Estimation (Standard M14)",
        "context": "Hero photo introducing real-world floor area calculation.",
        "current_visual": "assets/img/book_photos/home_diy_decorating/paint_roller_wall.jpg",
        "current_type": "img",
        "current_file": "home_diy_decorating/paint_roller_wall.jpg",
        "issue": "Shows paint rollers instead of flooring or floor tiles.",
        "proposed_concept": "High-res photograph of tradesperson laying luxury vinyl or ceramic floor tiles in an L-shaped kitchen with tape measure and tile spacers.",
        "recommended_action": "Directly match flooring and tile pack exam scenario.",
        "tags": ["Hero Photo", "Trades & Fitting", "Flooring", "Standard M14"]
    },
    {
        "id": "maths-diagram-circles",
        "book": "Maths Level 2 Core Guide",
        "suite": "maths",
        "subject": "maths",
        "type": "diagram",
        "topic": "Circle Anatomy & Formula Breakdown (Standard M15)",
        "context": "Radius, Diameter, Circumference (πd) and Area (πr²) formulas.",
        "current_visual": vcc.get_circles_svg(),
        "current_type": "svg",
        "current_file": "visual_curriculum_catalog.py (get_circles_svg)",
        "issue": "Formula text is small on some screens.",
        "proposed_concept": "Clean dual-circle diagram: Left circle highlighting Circumference (perimeter boundary) with C = πd; Right circle highlighting Area (shaded surface) with A = πr² and r² reminder.",
        "recommended_action": "Use large bold callouts highlighting 'r² means r × r, NOT r × 2!'.",
        "tags": ["Inline SVG", "Circle Formulas", "Misconception Alert", "Standard M15"]
    },
    {
        "id": "maths-diagram-formula-triangle",
        "book": "Maths Level 2 Core Guide",
        "suite": "maths",
        "subject": "maths",
        "type": "diagram",
        "topic": "Compound Measures: Speed-Distance-Time Formula Triangle (Standard M13)",
        "context": "Essential compound unit formula triangle for Speed = Distance ÷ Time.",
        "current_visual": vcc.get_formula_triangle_dst_svg(),
        "current_type": "svg",
        "current_file": "visual_curriculum_catalog.py (get_formula_triangle_dst_svg)",
        "issue": "Standard triangle is clear, but needs time conversion callout (e.g. 45 mins = 0.75h, NOT 0.45h).",
        "proposed_concept": "DST triangle with hand cover gesture plus a prominent golden rule box: 'Convert minutes to decimal hours by dividing by 60'.",
        "recommended_action": "Incorporate decimal time conversion warning trap directly into the diagram.",
        "tags": ["Inline SVG", "Formula Triangle", "Decimal Time Trap", "Standard M13"]
    },
    {
        "id": "maths-diagram-scatter-graph",
        "book": "Maths Level 2 Core Guide",
        "suite": "maths",
        "subject": "maths",
        "type": "diagram",
        "topic": "Scatter Graph & Line of Best Fit (Standard D26)",
        "context": "Strand 3 (Handling Data). Interpreting bivariate correlation and interpolating values.",
        "current_visual": vcc.get_scatter_graphs_svg(),
        "current_type": "svg",
        "current_file": "visual_curriculum_catalog.py (get_scatter_graphs_svg)",
        "issue": "Graph points are clear, but needs dotted projection lines showing how to read off values using line of best fit.",
        "proposed_concept": "Professional scatter plot with plotted data points, red line of best fit, and dashed blue projection lines showing interpolation from x to y.",
        "recommended_action": "Clearly demonstrate reading values from line of best fit to secure 2-mark exam questions.",
        "tags": ["Inline SVG", "Scatter Graphs", "Line of Best Fit", "Standard D26"]
    },
    {
        "id": "maths-diagram-pie-chart",
        "book": "Maths Level 2 Core Guide",
        "suite": "maths",
        "subject": "maths",
        "type": "diagram",
        "topic": "Pie Chart Angle Calculation & Protractor Drawing (Standard D25)",
        "context": "Calculating sector angles from frequencies (Frequency ÷ Total × 360°).",
        "current_visual": vcc.get_pie_charts_svg(),
        "current_type": "svg",
        "current_file": "visual_curriculum_catalog.py (get_pie_charts_svg)",
        "issue": "Shows pie chart but does not show the protractor angle calculation formula table beside it.",
        "proposed_concept": "Dual visual: Left = 4-row frequency-to-angle table (Degrees = f/N × 360°); Right = segmented pie chart with sector degree callouts (144°, 90°, 72°, 54° = 360°).",
        "recommended_action": "Link table calculation directly to sector drawing with directional arrows.",
        "tags": ["Inline SVG", "Pie Charts", "Protractor Angles", "Standard D25"]
    },
    {
        "id": "maths-diagram-probability-tree",
        "book": "Maths Level 2 Core Guide",
        "suite": "maths",
        "subject": "maths",
        "type": "diagram",
        "topic": "Sequential Probability Tree Diagram (Standard D28)",
        "context": "Calculating combined probabilities for two independent or dependent events.",
        "current_visual": vcc.get_probability_svg(),
        "current_type": "svg",
        "current_file": "visual_curriculum_catalog.py (get_probability_svg)",
        "issue": "Shows single event spinner. Needs full 2-stage tree diagram for Level 2.",
        "proposed_concept": "2-stage tree diagram (Event 1 -> Event 2) with branch fractions, outcome labels (e.g. Pass/Fail or Red/Blue), and 'Multiply across branches; Add outcome probabilities' rule.",
        "recommended_action": "Provide full Level 2 tree diagram displaying 4 distinct outcome branches.",
        "tags": ["Inline SVG", "Probability Tree", "Combined Probability", "Standard D28"]
    },

    # -------------------------------------------------------------------------
    # SUITE 3: ENGLISH WRITING SUITE (STRUCTURAL WIREFRAMES & LAYOUTS)
    # -------------------------------------------------------------------------
    {
        "id": "eng-wireframe-letter",
        "book": "English Writing Level 2 Core Guide",
        "suite": "english",
        "subject": "english",
        "type": "wireframe",
        "topic": "Formal Business Letter Structural Wireframe (Format 2)",
        "context": "Section 1 of Writing Guide. Official blueprint for 12-mark Pearson writing task.",
        "current_visual": get_letter_wireframe_svg(),
        "current_type": "svg",
        "current_file": "books/a4/a4_kit.py (letter_layout)",
        "issue": "Current template in a4_kit is text-based. A clear visual wireframe showing exact spatial layout ensures learners don't lose marks on address alignment.",
        "proposed_concept": "Full-colour structural wireframe with labelled bounding boxes: Sender address (top right), Date, Recipient address (left, lower), Salutation, Subject line, 4 body paragraphs, Valediction.",
        "recommended_action": "Use as master reference spread on page 24 of English Writing Core Guide.",
        "tags": ["Inline SVG", "Format Wireframe", "Formal Letter", "Pearson Criteria"]
    },
    {
        "id": "eng-photo-letter",
        "book": "English Writing Level 2 Core Guide",
        "suite": "english",
        "subject": "english",
        "type": "photo",
        "topic": "Executive Workplace Letterhead (Format 2)",
        "context": "Hero photo illustrating formal corporate written correspondence.",
        "current_visual": "assets/img/book_photos/workplace_office/formal_letterhead.jpg",
        "current_type": "img",
        "current_file": "workplace_office/formal_letterhead.jpg",
        "issue": "Previously reused team_meeting.jpg. Needs dedicated close-up of printed company letterhead.",
        "proposed_concept": "Authentic printed business letter typed on executive company letterhead with formal salutation, body paragraphs, and professional ink signature.",
        "recommended_action": "Showcases authentic physical business stationery in UK professional context.",
        "tags": ["Hero Photo", "Business Context", "Formal Letter", "Pearson Criteria"]
    },
    {
        "id": "eng-wireframe-email",
        "book": "English Writing Level 2 Core Guide",
        "suite": "english",
        "subject": "english",
        "type": "wireframe",
        "topic": "Workplace Email Interface Wireframe (Format 3)",
        "context": "Core teaching page for workplace email correspondence.",
        "current_visual": get_email_wireframe_svg(),
        "current_type": "svg",
        "current_file": "books/a4/a4_kit.py (email_layout)",
        "issue": "Wireframe needs distinct To, CC, Subject, Attachment, and numbered bullet action lines.",
        "proposed_concept": "Realistic email client UI window (Outlook/Webmail aesthetic) showcasing subject line conventions, polite salutation, concise paragraphing, and professional sign-off.",
        "recommended_action": "Embed as standard visual model for all digital correspondence units.",
        "tags": ["Inline SVG", "Email Wireframe", "Digital Comms", "Format 3"]
    },
    {
        "id": "eng-wireframe-article",
        "book": "English Writing Level 2 Core Guide",
        "suite": "english",
        "subject": "english",
        "type": "wireframe",
        "topic": "Magazine / Newsletter Article Wireframe (Format 1)",
        "context": "Most frequent Level 2 writing format (15 marks). Multi-column layout with presentational devices.",
        "current_visual": get_article_wireframe_svg(),
        "current_type": "svg",
        "current_file": "books/a4/content/english_writing_data.py",
        "issue": "Learners frequently forget to include headline, byline, subheadings, and pull quotes in article tasks.",
        "proposed_concept": "Authentic 2-column magazine spread wireframe displaying: Catchy main headline, Author byline, Subheadings for each section, Stylized pull quote, and Image caption box.",
        "recommended_action": "Provide clear visual layout checklist awarding maximum presentational feature marks.",
        "tags": ["Inline SVG", "Article Wireframe", "Presentational Features", "Format 1"]
    },
    {
        "id": "eng-wireframe-report",
        "book": "English Writing Level 2 Core Guide",
        "suite": "english",
        "subject": "english",
        "type": "wireframe",
        "topic": "Formal Investigation / Incident Report Wireframe (Format 4)",
        "context": "Workplace report format tested in Functional Skills Level 2.",
        "current_visual": get_report_wireframe_svg(),
        "current_type": "svg",
        "current_file": "books/a4/content/english_writing_data.py",
        "issue": "Reports require numbered headings (1.0 Executive Summary, 2.0 Key Findings, 3.0 Recommendations) which learners omit.",
        "proposed_concept": "Rigorous corporate report wireframe with title block, metadata, decimal section numbering, risk rating data table, and bulleted recommendations.",
        "recommended_action": "Reinforce workplace report structural conventions for vocational apprentices.",
        "tags": ["Inline SVG", "Report Wireframe", "Numbered Headings", "Format 4"]
    },
    {
        "id": "eng-diagram-mindmap",
        "book": "English Writing Level 2 Companion Workbook",
        "suite": "english",
        "subject": "english",
        "type": "diagram",
        "topic": "5-Paragraph Candidate Planning Mindmap",
        "context": "Planning page preceding each 15-mark writing task in Companion Workbook.",
        "current_visual": "assets/img/book_photos/classroom_studying_adults/mindmap_planning.jpg",
        "current_type": "img",
        "current_file": "classroom_studying_adults/mindmap_planning.jpg",
        "issue": "Previously reused generic whiteboard planning photo. A structured candidate planning diagram is far more actionable.",
        "proposed_concept": "Handwritten-style structured mindmap showing central topic branching into 5 structured paragraphs: Introduction -> Point 1 (Benefits) -> Point 2 (Concerns) -> Point 3 (Solutions) -> Conclusion.",
        "recommended_action": "Include blank fillable planning framework on candidate answer pages.",
        "tags": ["Planning Diagram", "Mindmap", "5-Paragraph Plan", "Companion"]
    },

    # -------------------------------------------------------------------------
    # SUITE 4: ENGLISH READING SUITE (ANALYTICAL BLUEPRINTS & COMPARISONS)
    # -------------------------------------------------------------------------
    {
        "id": "read-diagram-fact-opinion",
        "book": "English Reading Level 2 Core Guide",
        "suite": "reading",
        "subject": "reading",
        "type": "diagram",
        "topic": "Fact vs Opinion Analytical Comparison Matrix",
        "context": "Core reading skill tested in both Level 1 and Level 2 exams.",
        "current_visual": "assets/img/book_photos/journalism_media/newspaper_editorial.jpg",
        "current_type": "img",
        "current_file": "journalism_media/newspaper_editorial.jpg",
        "issue": "Photo of broadsheet is authentic, but learners need an analytical comparison table breaking down linguistic indicators of fact vs opinion.",
        "proposed_concept": "Side-by-side contrast card: Left (Fact: verifiable data, dates, statistics, objective language) vs Right (Opinion: emotive adjectives, subjective value judgements, speculative modals).",
        "recommended_action": "Include linguistic indicator badges (e.g. 'Evidence proves' vs 'In my view').",
        "tags": ["Reading Skill", "Fact vs Opinion", "Linguistic Analysis", "Core Guide"]
    },
    {
        "id": "read-diagram-text-comparison",
        "book": "English Reading Level 2 Core Guide",
        "suite": "reading",
        "subject": "reading",
        "type": "diagram",
        "topic": "Dual-Text Comparison Grid (Text A vs Text B Synthesis)",
        "context": "The highest-tariff question in Pearson Level 2 Reading exam (11 marks across comparison questions).",
        "current_visual": "assets/img/book_photos/workplace_office/dual_screen_research.jpg",
        "current_type": "img",
        "current_file": "workplace_office/dual_screen_research.jpg",
        "issue": "Dual screen photo represents the context well. Pair with an analytical Venn synthesis diagram showing Text A points, Text B points, and synthesis overlapping points.",
        "proposed_concept": "Split-view analytical matrix contrasting Text A (Authorial stance, tone, evidence) against Text B with synthesis bridge column extracting common themes.",
        "recommended_action": "Essential visual model for mastering the 11-mark comparison section.",
        "tags": ["Exam Essential", "Text A vs Text B", "Synthesis Grid", "11-Mark Question"]
    },
    {
        "id": "read-diagram-presentational",
        "book": "English Reading Level 1 Core Guide",
        "suite": "reading",
        "subject": "reading",
        "type": "diagram",
        "topic": "Presentational Devices Visual Anatomy",
        "context": "Identifying subheadings, bullet points, font styles, captions, and sidebars.",
        "current_visual": "assets/img/book_photos/workplace_office/magazine_layout_features.jpg",
        "current_type": "img",
        "current_file": "workplace_office/magazine_layout_features.jpg",
        "issue": "Magazine photo is great. Add callout pointer arrows highlighting: Bold Heading, Bulleted list, Callout box, Image with caption, and Sidebar.",
        "proposed_concept": "Annotated layout spread with numbered pointer tags linking each visual device directly to its functional purpose (e.g. 'Subheading: categorises information for skimming').",
        "recommended_action": "Directly prepares Level 1 learners for questions asking 'Why has the author used bullet points in Text 1?'.",
        "tags": ["Presentational Devices", "Annotated Layout", "Level 1 Reading", "Skimming & Scanning"]
    },

    # -------------------------------------------------------------------------
    # SUITE 5: ESSENTIAL DIGITAL SKILLS (EDSQ / DFS TECHNICAL WIREFRAMES)
    # -------------------------------------------------------------------------
    {
        "id": "digital-wireframe-gui",
        "book": "Digital Skills Handbook (EDSQ / DFS)",
        "suite": "specialist",
        "subject": "specialist",
        "type": "wireframe",
        "topic": "Operating System GUI & Window Management",
        "context": "Skill Area 1: Using Devices and Handling Information.",
        "current_visual": get_digital_gui_svg(),
        "current_type": "svg",
        "current_file": "books/a4/build_specialist_suite_a4.py",
        "issue": "Previous drafts had text descriptions of windows. A full desktop GUI diagram visually clarifies window controls, taskbars, and multitasking.",
        "proposed_concept": "High-tech dark theme OS desktop wireframe with file manager, browser window, taskbar, system clock, and minimize/maximize/close button callouts.",
        "recommended_action": "Standard introductory diagram on page 6 of Digital Skills Handbook.",
        "tags": ["Inline SVG", "GUI Wireframe", "Skill Area 1", "EDSQ Standards"]
    },
    {
        "id": "digital-diagram-folders",
        "book": "Digital Skills Handbook (EDSQ / DFS)",
        "suite": "specialist",
        "subject": "specialist",
        "type": "diagram",
        "topic": "Hierarchical File & Folder Tree Directory",
        "context": "Creating, organising, and navigating folder hierarchies and file extensions.",
        "current_visual": "assets/img/book_photos/charts_data_screens/tablet_spreadsheet.jpg",
        "current_type": "img",
        "current_file": "charts_data_screens/tablet_spreadsheet.jpg",
        "issue": "Shows general spreadsheet. Needs dedicated folder tree diagram showing parent/child folders and common file extensions (.pdf, .docx, .xlsx, .jpeg).",
        "proposed_concept": "Tree diagram: Root Drive (C:) -> Documents -> Work -> NHS -> [Subfolders] with icon badges for document formats and file size indicators.",
        "recommended_action": "Teaches proper workplace file management and naming conventions.",
        "tags": ["Folder Tree", "File Management", "Naming Conventions", "Skill Area 1"]
    },
    {
        "id": "digital-diagram-phishing",
        "book": "Digital Skills Handbook (EDSQ / DFS)",
        "suite": "specialist",
        "subject": "specialist",
        "type": "diagram",
        "topic": "Phishing Email Red Flag Audit Graphic",
        "context": "Skill Area 5: Being Safe and Responsible Online.",
        "current_visual": "assets/img/book_photos/email_online_safety/email_inbox_laptop.jpg",
        "current_type": "img",
        "current_file": "email_online_safety/email_inbox_laptop.jpg",
        "issue": "Current photo shows standard inbox. Needs an annotated phishing email highlighting the 5 key red flags.",
        "proposed_concept": "Mock phishing email with 5 red flag callout badges: 1. Fake sender domain (support@paypa1-security.com); 2. Generic greeting ('Dear Customer'); 3. Urgent panic threat; 4. Suspicious shortened link; 5. Grammatical errors.",
        "recommended_action": "Vital practical life skill and high-frequency exam topic for digital qualifications.",
        "tags": ["Cybersecurity", "Phishing Audit", "Red Flags", "Skill Area 5"]
    },
    {
        "id": "digital-diagram-passwords",
        "book": "Digital Skills Handbook (EDSQ / DFS)",
        "suite": "specialist",
        "subject": "specialist",
        "type": "diagram",
        "topic": "Password Strength Gauge & Multi-Factor Authentication (MFA)",
        "context": "Protecting accounts, passphrases, and biometric security.",
        "current_visual": "assets/img/book_photos/email_online_safety/cybersecurity_lock.jpg",
        "current_type": "img",
        "current_file": "email_online_safety/cybersecurity_lock.jpg",
        "issue": "Abstract lock photo. Needs concrete visual comparison of Weak vs Strong passwords and 2FA workflow.",
        "proposed_concept": "Three-tier password gauge (Red: 'password123' -> Amber: 'Liverpool2024' -> Green: 'Purple#Elephant!Jump9') plus smartphone MFA push notification workflow.",
        "recommended_action": "Teaches three random words technique recommended by the National Cyber Security Centre (NCSC).",
        "tags": ["Cybersecurity", "Password Gauge", "MFA Authentication", "Skill Area 5"]
    },

    # -------------------------------------------------------------------------
    # SUITE 6: BKSB REMEDIATION MISCONCEPTION CARDS
    # -------------------------------------------------------------------------
    {
        "id": "bksb-card-reverse-pct",
        "book": "BKSB Remediation Workbook",
        "suite": "specialist",
        "subject": "maths",
        "type": "diagram",
        "topic": "Failure Mode 2: Reverse Percentage Misconception",
        "context": "Mode 2 masterclass: Calculating original value before a discount or tax increase.",
        "current_visual": get_bksb_misconception_svg(),
        "current_type": "svg",
        "current_file": "books/a4/append_bksb_modes.py",
        "issue": "Previous text-only box lacked immediate visual punch. The side-by-side Red Error vs Green Golden Rule comparison makes the trap impossible to miss.",
        "proposed_concept": "Split diagnostic card: Red Box highlights the candidate trap (adding 20% of sale price); Green Box demonstrates dividing by decimal multiplier (0.80) to recover the 100% original value.",
        "recommended_action": "Core visual model used across all 24 failure mode spreads in BKSB Remediation Workbook.",
        "tags": ["Inline SVG", "Diagnostic Card", "BKSB Remediation", "Failure Mode 2"]
    },
    {
        "id": "bksb-card-perimeter-area",
        "book": "BKSB Remediation Workbook",
        "suite": "specialist",
        "subject": "maths",
        "type": "diagram",
        "topic": "Failure Mode 4: Perimeter vs Area Confusion",
        "context": "Remediating the widespread misconception of confusing fence perimeter with grass turf area.",
        "current_visual": vcc.get_perimeter_svg(),
        "current_type": "svg",
        "current_file": "visual_curriculum_catalog.py (get_perimeter_svg)",
        "issue": "Diagram shows perimeter. Needs explicit contrast with area (walking the fence boundary in metres vs tiling the surface in square metres).",
        "proposed_concept": "Side-by-side diagnostic card: Left = Walking feet around perimeter border (units: m); Right = Shaded square grid tiles covering internal surface (units: m²).",
        "recommended_action": "Resolves top BKSB failure reason in Level 1 and Level 2 spatial diagnostics.",
        "tags": ["Perimeter vs Area", "Diagnostic Trap", "Units Distinction", "Failure Mode 4"]
    },
    {
        "id": "bksb-card-decimal-alignment",
        "book": "BKSB Remediation Workbook",
        "suite": "specialist",
        "subject": "maths",
        "type": "diagram",
        "topic": "Failure Mode 1: Decimal Point Misalignment in Column Addition",
        "context": "Remediating ragged-right decimal calculations (e.g. 14.5 + 2.38).",
        "current_visual": vcc.get_decimals_svg(),
        "current_type": "svg",
        "current_file": "visual_curriculum_catalog.py (get_decimals_svg)",
        "issue": "Shows standard calculation. Add high-contrast vertical neon guideline through the decimal points to highlight zero-padding (14.50).",
        "proposed_concept": "Vertical yellow highlight line cutting straight down through all decimal points, showing zero placeholder padded in red (14.50 + 2.38 = 16.88).",
        "recommended_action": "Directly tackles root cause of 60% of Section A non-calculator arithmetic errors.",
        "tags": ["Decimal Alignment", "Zero Padding", "Section A", "Failure Mode 1"]
    },

    # -------------------------------------------------------------------------
    # SUITE 7: SPAG MASTERY SUITE (MURPHY CARTOON SPREADS & GRAMMAR CHARTS)
    # -------------------------------------------------------------------------
    {
        "id": "spag-diagram-comma-splice",
        "book": "SPaG Handbook & Mastery Drills",
        "suite": "spag",
        "subject": "spag",
        "type": "diagram",
        "topic": "Comma Splice Diagnosis & 3-Way Repair Toolkit",
        "context": "Unit 2: Sentence Boundaries & Run-On Sentences.",
        "current_visual": "assets/img/book_photos/classroom_studying_adults/grammar_proofreading.jpg",
        "current_type": "img",
        "current_file": "classroom_studying_adults/grammar_proofreading.jpg",
        "issue": "Photo of red pen is great. Pair with a 3-way branching diagram demonstrating the three valid grammatical fixes for comma splices.",
        "proposed_concept": "Branching repair flowchart: Error sentence ('I worked late, I was exhausted') -> Fix 1: Full stop (. I was) -> Fix 2: Semicolon (; I was) -> Fix 3: FANBOYS conjunction (, so I was).",
        "recommended_action": "Provides adult learners with an instant, foolproof diagnostic repair routine.",
        "tags": ["Grammar Flowchart", "Comma Splice", "Sentence Boundaries", "SPaG Mastery"]
    },
    {
        "id": "spag-diagram-apostrophes",
        "book": "SPaG Handbook & Mastery Drills",
        "suite": "spag",
        "subject": "spag",
        "type": "diagram",
        "topic": "Apostrophe Rules: Contraction vs Possession",
        "context": "Unit 3: Apostrophes for Omission and Ownership.",
        "current_visual": "assets/img/book_photos/workplace_office/typography_punctuation_blocks.jpg",
        "current_type": "img",
        "current_file": "workplace_office/typography_punctuation_blocks.jpg",
        "issue": "Vintage letterpress photo is beautiful. Pair with an explicit comparison matrix: Contraction (omitted letter) vs Singular Possession ('s) vs Plural Possession (s').",
        "proposed_concept": "3-column comparison card: Column 1 = Omission (do not -> don't); Column 2 = One owner (the doctor's bleep); Column 3 = Many owners ending in s (the nurses' station). Plus 'its vs it's' trap alert.",
        "recommended_action": "Directly tackles Pearson criteria awarding up to 4 SPaG marks for accurate punctuation.",
        "tags": ["Punctuation Matrix", "Apostrophes", "Contraction vs Possession", "SPaG Mastery"]
    },
    {
        "id": "spag-diagram-homophones",
        "book": "SPaG Handbook & Mastery Drills",
        "suite": "spag",
        "subject": "spag",
        "type": "diagram",
        "topic": "Common Adult Homophone Distinction Cards",
        "context": "Unit 7: High-Frequency Confusable Words.",
        "current_visual": "assets/img/book_photos/classroom_studying_adults/spelling_letter_tiles.jpg",
        "current_type": "img",
        "current_file": "classroom_studying_adults/spelling_letter_tiles.jpg",
        "issue": "Letter tiles photo is thematic. Add graphic comparison tiles for the top 4 tested homophone pairs in FE exams.",
        "proposed_concept": "Visual card pairs with mnemonic memory hooks: 1. Their (belonging to them) / There (location / here) / They're (they are); 2. Practice (noun / ice) vs Practise (verb / advise); 3. Stationary (car stopped) vs Stationery (envelopes / paper).",
        "recommended_action": "Memory hooks permanently eliminate homophone deduction errors.",
        "tags": ["Homophones", "Mnemonic Cards", "Spelling Rules", "SPaG Mastery"]
    },

    # -------------------------------------------------------------------------
    # SUITE 8: CHARACTER CARTOONS & MURPHY-STYLE TEACHING SPREADS
    # -------------------------------------------------------------------------
    {
        "id": "cartoon-abdul-explaining",
        "book": "All 17 Publications (Universal Tutor)",
        "suite": "cartoons",
        "subject": "cartoons",
        "type": "cartoon",
        "topic": "Tutor Abdul: Concept Explanations & Exam Strategy",
        "context": "Speech bubbles, Golden Rules, and diagnostic walkthroughs across all books.",
        "current_visual": "assets/img/book_cartoons/abdul_explaining.png",
        "current_type": "img",
        "current_file": "assets/img/book_cartoons/abdul_explaining.png",
        "issue": "Abdul's character portrait is clean and approachable. Ensure consistent speech bubble typography (Lexend 13pt) beside character in all Murphy spreads.",
        "proposed_concept": "Abdul in clean navy cardigan with smart tutor lanyard, gesturing towards whiteboard sketch graphics with supportive speech bubble.",
        "recommended_action": "Maintain Abdul as lead authoritative pedagogical voice across both print books and website.",
        "tags": ["Lead Tutor", "Murphy Style", "Consistent Voice", "Exam Strategy"]
    },
    {
        "id": "cartoon-priya-explaining",
        "book": "All 17 Publications (Senior Specialist)",
        "suite": "cartoons",
        "subject": "cartoons",
        "type": "cartoon",
        "topic": "Tutor Priya: Analytical Methods & Deep Diagnostics",
        "context": "Appears on analytical spreads: BIDMAS, formulas, algebra, and BKSB failure modes.",
        "current_visual": "assets/img/book_cartoons/priya_explaining.png",
        "current_type": "img",
        "current_file": "assets/img/book_cartoons/priya_explaining.png",
        "issue": "Portrait is high quality. Ensure speech bubbles focus on methodical error-checking and inverse calculation routines.",
        "proposed_concept": "Priya with glasses and tablet device, highlighting step-by-step mathematical reasoning and checking methods.",
        "recommended_action": "Position Priya beside worked calculation examples and checking method checkpoints.",
        "tags": ["Senior Specialist", "Inverse Checks", "Problem Solving", "Cartoons"]
    },
    {
        "id": "cartoon-marcus-apprentice",
        "book": "Vocational & Trade Publications",
        "suite": "cartoons",
        "subject": "cartoons",
        "type": "cartoon",
        "topic": "Marcus: Construction & Vocational Apprentice Perspective",
        "context": "Appears in workshop scenarios, building plans, area calculations, and trade practical tasks.",
        "current_visual": "assets/img/book_cartoons/marcus_apprentice.png",
        "current_type": "img",
        "current_file": "assets/img/book_cartoons/marcus_apprentice.png",
        "issue": "Marcus in workwear is very relatable. Connect Marcus's dialogue directly to practical on-site trade math.",
        "proposed_concept": "Marcus wearing hi-vis vest and holding clipboard, asking practical on-site questions: 'How many packs of timber do I need to order for this framing job?'.",
        "recommended_action": "Reinforces practical purpose of functional math for trade apprentices.",
        "tags": ["Apprentice", "Trade Math", "Relatable Voice", "Vocational"]
    },
    {
        "id": "cartoon-sarah-healthcare",
        "book": "Healthcare & NHS Workplace Guides",
        "suite": "cartoons",
        "subject": "cartoons",
        "type": "cartoon",
        "topic": "Sarah: Healthcare Support Worker & NHS Scenarios",
        "context": "Appears in medication calculations, shift handover reports, and NHS workplace context.",
        "current_visual": "assets/img/book_cartoons/sarah_care_worker.png",
        "current_type": "img",
        "current_file": "assets/img/book_cartoons/sarah_care_worker.png",
        "issue": "Sarah in clinical scrubs is excellent for Oxford Health OH learner demographic.",
        "proposed_concept": "Sarah in clinical NHS uniform with stethoscope/ID badge, providing real healthcare scenarios (fluid charts, shift logs, patient dignity).",
        "recommended_action": "Directly supports NHS trust apprentices and healthcare assistants.",
        "tags": ["NHS Healthcare", "Clinical Scenarios", "Oxford Health OH", "Care Worker"]
    },
    {
        "id": "cartoon-sam-thinking",
        "book": "Entry 3 & Foundation Publications",
        "suite": "cartoons",
        "subject": "cartoons",
        "type": "cartoon",
        "topic": "Sam: Adult Learner Overcoming Anxiety & Building Confidence",
        "context": "Appears on foundational Entry 3 and Level 1 spreads.",
        "current_visual": "assets/img/book_cartoons/sam_thinking.png",
        "current_type": "img",
        "current_file": "assets/img/book_cartoons/sam_thinking.png",
        "issue": "Sam represents the adult learner returning to education after many years.",
        "proposed_concept": "Sam with study notebook, asking the questions every hesitant learner wants to ask, followed by Abdul's encouraging breakdown.",
        "recommended_action": "Validates learner doubts and dismantles math anxiety in early units.",
        "tags": ["Adult Learner", "Confidence Building", "Overcoming Anxiety", "Entry 3"]
    }
,
    # -------------------------------------------------------------------------
    # SUITE 2 (EXPANDED): MORE MATHEMATICS CURRICULUM TOPICS & WORKING MODELS
    # -------------------------------------------------------------------------
    {
        "id": "maths-diagram-fractions",
        "book": "Maths Level 1 & Level 2 Core Guides",
        "suite": "maths",
        "subject": "maths",
        "type": "diagram",
        "topic": "Fraction Operations & Mixed Numbers (Standard N3)",
        "context": "Adding, subtracting, and finding equivalent fractions using visual bar models.",
        "current_visual": vcc.get_fractions_svg(),
        "current_type": "svg",
        "current_file": "visual_curriculum_catalog.py (get_fractions_svg)",
        "issue": "Fraction bar model shows halves, quarters, and eighths. Needs explicit common denominator matching brackets.",
        "proposed_concept": "High-contrast fraction bars demonstrating 1/2 + 1/4 = 2/4 + 1/4 = 3/4 with common denominator 4 highlighted in gold.",
        "recommended_action": "Ensure shaded segments and denominator units are clearly labelled.",
        "tags": ["Inline SVG", "Fraction Bars", "Common Denominator", "Standard N3"]
    },
    {
        "id": "maths-photo-fractions",
        "book": "Maths Level 1 Core Guide",
        "suite": "maths",
        "subject": "maths",
        "type": "photo",
        "topic": "Recipe Ingredient Scaling & Fraction Portions (Standard N3)",
        "context": "Hero photo introducing fractional scaling in catering and bakery contexts.",
        "current_visual": "assets/img/book_photos/kitchen_cooking_recipes/kitchen_scales.jpg",
        "current_type": "img",
        "current_file": "kitchen_cooking_recipes/kitchen_scales.jpg",
        "issue": "Close-up of scales is clear. Ensure measurement bowl shows fractional quantities (3/4 kg flour).",
        "proposed_concept": "Authentic photograph of commercial kitchen prep bench with baker scaling 3/4 kg flour and measuring cup.",
        "recommended_action": "Directly reinforces catering exam scenarios.",
        "tags": ["Hero Photo", "Catering Context", "Recipe Scaling", "Standard N3"]
    },
    {
        "id": "maths-diagram-percentages",
        "book": "Maths Level 1 & Level 2 Core Guides",
        "suite": "maths",
        "subject": "maths",
        "type": "diagram",
        "topic": "Percentage Bubble Tree & Single-Step Multipliers (Standard N4)",
        "context": "Finding 50%, 25%, 10%, 5%, and 1% of amounts mentally, plus decimal multipliers.",
        "current_visual": vcc.get_percentages_svg(),
        "current_type": "svg",
        "current_file": "visual_curriculum_catalog.py (get_percentages_svg)",
        "issue": "Bubble method tree is very popular with adult learners. Ensure connecting arrows have clear division labels (÷10, ÷2, ÷10).",
        "proposed_concept": "Interactive bubble tree branching 100% (£360) down into 10% (£36) and 1% (£3.60), alongside the decimal multiplier equivalent (0.10 and 0.01).",
        "recommended_action": "Bridges mental arithmetic (Non-Calculator) with calculator multiplier methods.",
        "tags": ["Inline SVG", "Bubble Method", "Decimal Multipliers", "Standard N4"]
    },
    {
        "id": "maths-photo-percentages",
        "book": "Maths Level 2 Core Guide",
        "suite": "maths",
        "subject": "maths",
        "type": "photo",
        "topic": "High Street Retail Clearance & VAT Invoices (Standard N4)",
        "context": "Hero photo introducing sales discounts and VAT calculations.",
        "current_visual": "assets/img/book_photos/retail_shop/clothing_store.jpg",
        "current_type": "img",
        "current_file": "retail_shop/clothing_store.jpg",
        "issue": "Clothing store photo is authentic. Ensure sale banners displaying '30% OFF EVERYTHING' are prominent.",
        "proposed_concept": "Vibrant high street shop window featuring bold promotional discount sale signs and till receipt.",
        "recommended_action": "Provides relatable everyday consumer math context.",
        "tags": ["Hero Photo", "Retail Sales", "Discounts & VAT", "Standard N4"]
    },
    {
        "id": "maths-diagram-ratio",
        "book": "Maths Level 1 & Level 2 Core Guides",
        "suite": "maths",
        "subject": "maths",
        "type": "diagram",
        "topic": "Ratio Division into 2 & 3 Parts Bar Model (Standard N7)",
        "context": "Dividing quantities into ratios (e.g. 1 : 2 : 4) using equal compartment bar models.",
        "current_visual": vcc.get_ratio_bar_svg(),
        "current_type": "svg",
        "current_file": "visual_curriculum_catalog.py (get_ratio_bar_svg)",
        "issue": "Bar model shows 7 parts. Needs clear '1 part = Total ÷ Parts' callout banner.",
        "proposed_concept": "Equal-compartment bar model with 7 blocks (1 Cement : 2 Sand : 4 Gravel = 7 parts = 840 kg -> 1 part = 120 kg) with each block badged with £ or kg value.",
        "recommended_action": "The Singapore bar model approach is proven to eliminate ratio confusion.",
        "tags": ["Inline SVG", "Ratio Bar Model", "Compartments", "Standard N7"]
    },
    {
        "id": "maths-photo-ratio",
        "book": "Maths Level 2 Core Guide",
        "suite": "maths",
        "subject": "maths",
        "type": "photo",
        "topic": "Concrete Mortar Mixing on Building Site (Standard N7)",
        "context": "Hero photo introducing 3-part ratio division in construction.",
        "current_visual": "assets/img/book_photos/construction_trades/concrete_mixer_site.jpg",
        "current_type": "img",
        "current_file": "construction_trades/concrete_mixer_site.jpg",
        "issue": "Site mixer photo is authentic. Ensure bags of cement and sand aggregates are visible.",
        "proposed_concept": "Active construction site with cement mixer and pre-portioned bags of sand and gravel.",
        "recommended_action": "Directly matches Pearson construction scenario questions.",
        "tags": ["Hero Photo", "Construction", "Ratio Mixing", "Standard N7"]
    },
    {
        "id": "maths-diagram-decimals",
        "book": "Maths Level 1 Core Guide",
        "suite": "maths",
        "subject": "maths",
        "type": "diagram",
        "topic": "Decimals & Column Addition with Money (Standard N9)",
        "context": "Handling tenths and hundredths in currency (£ and p).",
        "current_visual": vcc.get_decimals_svg(),
        "current_type": "svg",
        "current_file": "visual_curriculum_catalog.py (get_decimals_svg)",
        "issue": "Calculation shows column addition. Add vertical guide through decimal point to emphasize alignment.",
        "proposed_concept": "Vertical neon alignment guideline running through decimal points with zero placeholder padded in green (£45.90 vs £45.9).",
        "recommended_action": "Eliminates single biggest cause of marks loss in currency questions.",
        "tags": ["Inline SVG", "Decimals & Money", "Zero Padding", "Standard N9"]
    },
    {
        "id": "maths-photo-decimals",
        "book": "Maths Level 1 Core Guide",
        "suite": "maths",
        "subject": "maths",
        "type": "photo",
        "topic": "Cash Float & Till Reconciliation (Standard N9)",
        "context": "Hero photo introducing currency precision and change calculation.",
        "current_visual": "assets/img/book_photos/money_shopping_bills/coins_pounds.jpg",
        "current_type": "img",
        "current_file": "money_shopping_bills/coins_pounds.jpg",
        "issue": "UK coins neatly displayed. Ensure £2, £1, 50p, 20p, 10p coins are sharply in focus.",
        "proposed_concept": "End-of-day till drawer reconciliation with UK currency stacks and cashier receipt printout.",
        "recommended_action": "Relatable retail and hospitality context.",
        "tags": ["Hero Photo", "Till Float", "British Coins", "Standard N9"]
    },
    {
        "id": "maths-diagram-perimeter",
        "book": "Maths Level 1 & Level 2 Core Guides",
        "suite": "maths",
        "subject": "maths",
        "type": "diagram",
        "topic": "Perimeter: Walking Boundary of Compound Shape (Standard M14)",
        "context": "Calculating total outer distance around gardens, rooms, and building boundaries.",
        "current_visual": vcc.get_perimeter_svg(),
        "current_type": "svg",
        "current_file": "visual_curriculum_catalog.py (get_perimeter_svg)",
        "issue": "Ensure missing side lengths (horizontal and vertical deductions) are clearly annotated.",
        "proposed_concept": "Compound shape with walking footprint arrows around all 6 outer edges, showing how to deduce missing sides (8m - 5m = 3m) before adding.",
        "recommended_action": "Emphasize: 'Count all sides before adding — an L-shape has 6 sides, not 4!'.",
        "tags": ["Inline SVG", "Perimeter", "Missing Sides Trap", "Standard M14"]
    },
    {
        "id": "maths-diagram-volume",
        "book": "Maths Level 2 Core Guide",
        "suite": "maths",
        "subject": "maths",
        "type": "diagram",
        "topic": "3D Volume of Cuboids & Cylinders (Standard M16)",
        "context": "Calculating volume (length × width × height) and capacity in litres (1,000 cm³ = 1 litre).",
        "current_visual": vcc.get_volume_svg(),
        "current_type": "svg",
        "current_file": "visual_curriculum_catalog.py (get_volume_svg)",
        "issue": "3D cuboid is rendered well. Include water tank capacity conversion callout (1 m³ = 1,000 litres).",
        "proposed_concept": "Isometric cuboid water storage tank with dimensions (L=2.5m, W=1.2m, H=0.8m) showing V = 2.4 m³ = 2,400 litres.",
        "recommended_action": "Directly covers 4-mark volume and capacity tank filling problems.",
        "tags": ["Inline SVG", "3D Volume", "Capacity & Litres", "Standard M16"]
    },
    {
        "id": "maths-diagram-angles",
        "book": "Maths Level 2 Core Guide",
        "suite": "maths",
        "subject": "maths",
        "type": "diagram",
        "topic": "Angles, Bearings & Compass Navigation (Standard M18)",
        "context": "Measuring angles, acute/obtuse classifications, and 3-figure bearings (045°, 220°).",
        "current_visual": vcc.get_angles_svg(),
        "current_type": "svg",
        "current_file": "visual_curriculum_catalog.py (get_angles_svg)",
        "issue": "Protractor diagram is clear. Emphasize: 'Bearings are always measured clockwise from North and written with 3 figures'.",
        "proposed_concept": "North-arrow bearing diagram with clockwise circular trajectory showing bearing 065° and reverse bearing 245° (add 180°).",
        "recommended_action": "Guarantees marks on 3-figure bearing questions.",
        "tags": ["Inline SVG", "Bearings", "3-Figure Rule", "Standard M18"]
    },
    {
        "id": "maths-diagram-coordinates",
        "book": "Maths Level 1 & Level 2 Core Guides",
        "suite": "maths",
        "subject": "maths",
        "type": "diagram",
        "topic": "4-Quadrant Cartesian Coordinate Grid (Standard M20)",
        "context": "Plotting coordinates (x, y) including negative values and map references.",
        "current_visual": vcc.get_coordinates_svg(),
        "current_type": "svg",
        "current_file": "visual_curriculum_catalog.py (get_coordinates_svg)",
        "issue": "Grid is clear. Include mnemonic callout: 'Along the corridor (x), then up or down the stairs (y)'.",
        "proposed_concept": "4-quadrant grid (-5 to +5) with plotted hospital ward locations and walking path vectors.",
        "recommended_action": "Mnemonic ensures adult learners do not reverse x and y coordinates.",
        "tags": ["Inline SVG", "Coordinates", "4-Quadrant Grid", "Standard M20"]
    },
    {
        "id": "maths-diagram-averages",
        "book": "Maths Level 1 & Level 2 Core Guides",
        "suite": "maths",
        "subject": "maths",
        "type": "diagram",
        "topic": "Averages & Range: Mean, Median, Mode & Spread (Standard D22)",
        "context": "Calculating summary statistics and making two-point evaluative comparisons.",
        "current_visual": vcc.get_averages_svg(),
        "current_type": "svg",
        "current_file": "visual_curriculum_catalog.py (get_averages_svg)",
        "issue": "Balance beam visual is intuitive. Add exam comparison sentence starter: 'On average... and the results were more/less consistent because...'.",
        "proposed_concept": "4-quadrant statistics comparison card: Mean (Total ÷ Count), Median (Middle in ordered list), Mode (Most frequent), Range (Max - Min = Spread).",
        "recommended_action": "Directly satisfies Pearson comparison question rubric requiring one measure of average and one measure of spread.",
        "tags": ["Inline SVG", "Averages & Range", "Two-Point Comparison", "Standard D22"]
    },
    {
        "id": "maths-diagram-conversions",
        "book": "Maths Level 1 & Level 2 Core Guides",
        "suite": "maths",
        "subject": "maths",
        "type": "diagram",
        "topic": "Metric & Imperial Unit Conversion Scales (Standard M12)",
        "context": "Converting mm, cm, m, km; grams and kilograms; litres and millilitres; plus key imperial benchmarks.",
        "current_visual": vcc.get_unit_conversions_svg(),
        "current_type": "svg",
        "current_file": "visual_curriculum_catalog.py (get_unit_conversions_svg)",
        "issue": "Conversion steps are clear. Ensure key benchmarks (1 kg ≈ 2.2 lbs; 5 miles ≈ 8 km; 1 gallon ≈ 4.5 litres) are prominently framed.",
        "proposed_concept": "Dual-scale conversion ruler: Top = Metric (km, kg, litres); Bottom = Imperial (miles, lbs, gallons) with directional multiply/divide arrows.",
        "recommended_action": "Essential Section A reference guide.",
        "tags": ["Inline SVG", "Unit Conversions", "Metric & Imperial", "Standard M12"]
    },

    # -------------------------------------------------------------------------
    # SUITE 3 (EXPANDED): MORE ENGLISH WRITING FORMATS
    # -------------------------------------------------------------------------
    {
        "id": "eng-wireframe-speech",
        "book": "English Writing Level 2 Core Guide",
        "suite": "english",
        "subject": "english",
        "type": "wireframe",
        "topic": "Public Speech / Presentation Script Wireframe (Format 5)",
        "context": "Speech writing task (15 marks). Evaluating audience engagement, rhetorical devices, and stage directions.",
        "current_visual": get_speech_wireframe_svg(),
        "current_type": "svg",
        "current_file": "books/a4/content/english_writing_data.py",
        "issue": "Learners write essays instead of spoken scripts. Needs explicit stage directions [pause for effect, slide 2] and rhetorical devices.",
        "proposed_concept": "Spoken presentation wireframe featuring engaging greeting to attendees, rhetorical question hook, rule of three bullet points, and audience Q&A invitation.",
        "recommended_action": "Reinforces oral presentation conventions for apprentices.",
        "tags": ["Inline SVG", "Speech Wireframe", "Rhetorical Devices", "Format 5"]
    },
    {
        "id": "eng-wireframe-leaflet",
        "book": "English Writing Level 2 Core Guide",
        "suite": "english",
        "subject": "english",
        "type": "wireframe",
        "topic": "Informational Leaflet / Trifold Brochure Wireframe (Format 6)",
        "context": "Community and workplace informational trifold brochure.",
        "current_visual": get_leaflet_wireframe_svg(),
        "current_type": "svg",
        "current_file": "books/a4/content/english_writing_data.py",
        "issue": "Learners forget trifold spatial layout. A 3-panel wireframe clarifies front cover, inside panels, and contact back panel.",
        "proposed_concept": "3-panel trifold brochure blueprint: Panel 1 (Benefits & bullet points), Panel 2 (Course modules & testimonial), Panel 3 (Hook header & contact enrol details).",
        "recommended_action": "Visual blueprint guarantees presentational feature marks.",
        "tags": ["Inline SVG", "Leaflet Wireframe", "Trifold Blueprint", "Format 6"]
    },

    # -------------------------------------------------------------------------
    # SUITE 5 (EXPANDED): ESSENTIAL DIGITAL SKILLS SPREADSHEETS & HARDWARE
    # -------------------------------------------------------------------------
    {
        "id": "digital-diagram-spreadsheet",
        "book": "Digital Skills Handbook (EDSQ / DFS)",
        "suite": "specialist",
        "subject": "specialist",
        "type": "wireframe",
        "topic": "Spreadsheet Interface Anatomy & Formula Construction",
        "context": "Skill Area 2: Creating and Editing. Using formulas (=SUM, =AVERAGE), cell coordinates, and auto-sum.",
        "current_visual": get_spreadsheet_wireframe_svg(),
        "current_type": "svg",
        "current_file": "books/a4/build_specialist_suite_a4.py",
        "issue": "Spreadsheets are the highest-failure practical task in Digital Functional Skills. A labelled interface wireframe demystifies cell references and formula syntax.",
        "proposed_concept": "Detailed Excel/Sheets interface wireframe: Formula bar (=SUM(C2:C5)*1.20), row/column headers, clinical supply itemization, grand total highlighting, and key formula rule list.",
        "recommended_action": "Provides visual foundation for digital spreadsheet labs.",
        "tags": ["Inline SVG", "Spreadsheet Anatomy", "Formulas", "Skill Area 2"]
    },

    # -------------------------------------------------------------------------
    # SUITE 8: REVISION CARDS & VISUAL POSTCARD DECKS
    # -------------------------------------------------------------------------
    {
        "id": "cards-maths-deck",
        "book": "Maths Level 2 Revision Cards & Flashcard Stacks",
        "suite": "cards",
        "subject": "maths",
        "type": "wireframe",
        "topic": "Pocket Revision Cards & 60-Second Drill Stacks",
        "context": "A6 portable flashcards covering all 39 Level 2 standards.",
        "current_visual": get_flashcard_mockup_svg(),
        "current_type": "svg",
        "current_file": "books/a4/DESIGN_SPEC.md",
        "issue": "Existing PDF flashcards need consistent dual-sided layout: Front = Rule & Formula; Back = Rapid 60-Second Drill with Worked Solution.",
        "proposed_concept": "Dual-card spread mockup: Front card showing high-contrast formula with 'Misconception Trap Alert'; Back card featuring realistic workplace exam drill with tutor sign-off.",
        "recommended_action": "Used for on-the-go revision, mobile flashcard apps, and quick plenary checks.",
        "tags": ["Inline SVG", "Flashcards", "A6 Format", "60-Sec Drills"]
    },
    {
        "id": "cards-digital-deck",
        "book": "Essential Digital Skills Revision Cards",
        "suite": "cards",
        "subject": "specialist",
        "type": "cover",
        "topic": "Digital Skills Pocket Deck & Quick Reference Cards",
        "context": "Portable flashcard deck covering keyboard shortcuts, cybersecurity rules, and email etiquette.",
        "current_visual": "assets/img/books/flashcards_digital_skills.png",
        "current_type": "img",
        "current_file": "assets/img/books/flashcards_digital_skills.png",
        "issue": "Card stack mockup looks attractive. Ensure shortcut keys (Ctrl+C, Ctrl+V, Ctrl+Z, Ctrl+S) are prominently featured.",
        "proposed_concept": "Cyber midnight card deck with neon cyan edge trim, showcasing essential digital literacy rules and safety tips.",
        "recommended_action": "Complements the Digital Skills Practical Handbook.",
        "tags": ["Card Deck", "Digital Literacy", "Quick Reference", "EDSQ"]
    },
    {
        "id": "cards-ultimate-bundle",
        "book": "Master Functional Skills: Ultimate Level 2 Dual Bundle",
        "suite": "cards",
        "subject": "maths",
        "type": "cover",
        "topic": "3D Mockup: Ultimate Level 2 Complete Study Bundle",
        "context": "Flagship bundle combining Maths L2 Core + English Writing L2 Core + Mock Packs.",
        "current_visual": "assets/img/books/3d_bundle_ultimate_l2.png",
        "current_type": "img",
        "current_file": "assets/img/books/3d_bundle_ultimate_l2.png",
        "issue": "Ensure 3D bundle presentation shows both books standing with clean drop shadows.",
        "proposed_concept": "High-resolution 3D render of Maths L2 Core Guide and English L2 Core Guide standing together with gold ribbon 'COMPLETE LEVEL 2 ACCREDITATION BUNDLE'.",
        "recommended_action": "Used on shop landing page and marketing collateral.",
        "tags": ["3D Render", "Dual Bundle", "Flagship Publication", "Level 2"]
    }
]

# =============================================================================
# HTML PAGE GENERATION
# =============================================================================

def generate_books_audit_html():
    total_items = len(AUDIT_ITEMS)
    covers_count = sum(1 for x in AUDIT_ITEMS if x['type'] == 'cover')
    diagrams_count = sum(1 for x in AUDIT_ITEMS if x['type'] in ('diagram', 'wireframe'))
    photos_count = sum(1 for x in AUDIT_ITEMS if x['type'] == 'photo')
    cartoons_count = sum(1 for x in AUDIT_ITEMS if x['type'] == 'cartoon')

    html_cards = []
    for item in AUDIT_ITEMS:
        item_id = item['id']
        book_title = html.escape(item['book'])
        topic_title = html.escape(item['topic'])
        context_desc = html.escape(item['context'])
        issue_desc = html.escape(item['issue'])
        proposed_desc = html.escape(item['proposed_concept'])
        rec_action = html.escape(item['recommended_action'])
        curr_file = html.escape(item['current_file'])
        suite_id = item['suite']
        subject_id = item['subject']
        type_id = item['type']

        # Visual preview HTML
        if item['current_type'] == 'svg':
            visual_preview = f"""<div class="svg-preview-box">{item['current_visual']}</div>"""
            curr_badge = '<span class="badge-pill pill-cyan"><i class="fa-solid fa-bezier-curve"></i> Curated Inline SVG</span>'
        else:
            visual_preview = f"""<div class="photo-preview-box"><img src="{item['current_visual']}" alt="{topic_title}" loading="lazy" /></div>"""
            if type_id == 'cover':
                curr_badge = '<span class="badge-pill pill-purple"><i class="fa-solid fa-book-open"></i> 3D Book Cover Render</span>'
            elif type_id == 'cartoon':
                curr_badge = '<span class="badge-pill pill-amber"><i class="fa-solid fa-user-astronaut"></i> Character Cartoon</span>'
            else:
                curr_badge = '<span class="badge-pill pill-blue"><i class="fa-solid fa-camera"></i> Vocational Photo</span>'

        # Tag pills
        tags_html = "".join(f'<span class="tag-chip">{html.escape(t)}</span>' for t in item.get('tags', []))

        card_html = f"""
        <div class="audit-card" id="{item_id}" data-suite="{suite_id}" data-subject="{subject_id}" data-type="{type_id}">
          <div class="audit-card-header">
            <div class="header-left">
              <span class="book-badge">{book_title}</span>
              <h3 class="topic-name">{topic_title}</h3>
              {curr_badge}
            </div>
            <div class="header-right">
              <span class="status-indicator" id="status-{item_id}">✓ Approved</span>
            </div>
          </div>

          <div class="audit-grid">
            <!-- CURRENT VISUAL COLUMN -->
            <div class="audit-col current-col">
              <div class="col-title"><i class="fa-solid fa-eye"></i> Current Visual Asset</div>
              {visual_preview}
              <div class="current-meta">
                <p><strong>Source / Reference:</strong> <code>{curr_file}</code></p>
                <p><strong>Context &amp; Page Placement:</strong> {context_desc}</p>
                <div class="flag-explanation">
                  <strong>Audit Finding / Issue:</strong> {issue_desc}
                </div>
              </div>
            </div>

            <!-- PROPOSED SOLUTION COLUMN -->
            <div class="audit-col proposed-col">
              <div class="col-title"><i class="fa-solid fa-wand-magic-sparkles"></i> Proposed Enhancement &amp; Rationale</div>
              
              <div class="proposal-box">
                <div class="prop-subheading"><i class="fa-solid fa-lightbulb"></i> Curated Pedagogical Concept:</div>
                <p class="prop-text">{proposed_desc}</p>
                
                <div class="recommended-action-box">
                  <strong><i class="fa-solid fa-circle-check"></i> Actionable Specification:</strong>
                  <p>{rec_action}</p>
                </div>

                <div class="tags-container">
                  {tags_html}
                </div>
              </div>

              <!-- INTERACTIVE DECISION BOX -->
              <div class="feedback-action-box">
                <div class="feedback-heading"><i class="fa-solid fa-stamp"></i> Your Decision for This Asset:</div>
                <div class="feedback-options">
                  <label class="radio-label">
                    <input type="radio" name="decision-{item_id}" value="approve" checked onchange="updateCardStatus('{item_id}')">
                    <span class="radio-approve">✓ Approve Proposed</span>
                  </label>
                  <label class="radio-label">
                    <input type="radio" name="decision-{item_id}" value="custom" onchange="updateCardStatus('{item_id}')">
                    <span class="radio-custom">✎ Suggest Change</span>
                  </label>
                  <label class="radio-label">
                    <input type="radio" name="decision-{item_id}" value="keep" onchange="updateCardStatus('{item_id}')">
                    <span class="radio-keep">✕ Keep Current</span>
                  </label>
                </div>
                <textarea class="feedback-textarea" id="note-{item_id}" placeholder="Type any feedback, dimensional tweaks, or image preference for {topic_title}..." oninput="autoSaveNote('{item_id}')"></textarea>
              </div>
            </div>
          </div>
        </div>
        """
        html_cards.append(card_html)

    cards_joined = "\n".join(html_cards)

    full_html = f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Master Functional Skills — Books Image & Diagram Audit Catalog</title>
  <link rel="stylesheet" href="assets/css/mfs-theme.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <style>
    :root {{
      --navy: #070d1e;
      --navy-light: #0d1e3d;
      --accent: #2563eb;
      --cyan: #00e5ff;
      --amber: #f59e0b;
      --emerald: #10b981;
      --crimson: #e11d48;
      --violet: #581c87;
      --bg-audit: #f8fafc;
      --card-bg: #ffffff;
      --border-color: #cbd5e1;
    }}
    body {{
      font-family: 'Inter', system-ui, -apple-system, sans-serif;
      margin: 0;
      padding: 0;
      background: var(--bg-audit);
      color: #0f172a;
      line-height: 1.6;
    }}
    .audit-header {{
      background: linear-gradient(135deg, var(--navy) 0%, var(--navy-light) 100%);
      color: #ffffff;
      padding: 36px 24px;
      border-bottom: 4px solid var(--cyan);
      box-shadow: 0 4px 20px rgba(0,0,0,0.15);
    }}
    .audit-header-inner {{
      max-width: 1540px;
      margin: 0 auto;
    }}
    .header-top-row {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 20px;
      flex-wrap: wrap;
    }}
    .audit-title {{
      font-size: 2.2rem;
      font-weight: 800;
      margin: 0 0 10px 0;
      letter-spacing: -0.02em;
    }}
    .audit-title span {{
      color: #38bdf8;
    }}
    .audit-subtitle {{
      font-size: 1.12rem;
      color: #cbd5e1;
      max-width: 950px;
      margin: 0 0 20px 0;
    }}
    .stats-bar {{
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
    }}
    .stat-pill {{
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.18);
      padding: 8px 16px;
      border-radius: 8px;
      font-size: 0.92rem;
      display: flex;
      align-items: center;
      gap: 8px;
      color: #f1f5f9;
    }}
    .stat-pill strong {{
      color: #38bdf8;
      font-size: 1.15rem;
    }}
    .stat-pill.stat-approved strong {{
      color: #4ade80;
    }}
    .stat-pill.stat-custom strong {{
      color: #fbbf24;
    }}

    /* Sticky Navigation Bar */
    .audit-nav-bar {{
      background: #ffffff;
      border-bottom: 2px solid #e2e8f0;
      position: sticky;
      top: 0;
      z-index: 1000;
      box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    }}
    .audit-nav-inner {{
      max-width: 1540px;
      margin: 0 auto;
      padding: 12px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
    }}
    .nav-tabs {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }}
    .btn-tab {{
      background: #f1f5f9;
      border: 1px solid #cbd5e1;
      padding: 8px 16px;
      border-radius: 20px;
      font-size: 0.9rem;
      font-weight: 700;
      color: #475569;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .btn-tab:hover {{
      background: #e2e8f0;
      color: #0f172a;
    }}
    .btn-tab.active {{
      background: var(--accent);
      color: #ffffff;
      border-color: var(--accent);
      box-shadow: 0 2px 8px rgba(37,99,235,0.3);
    }}

    /* Controls Bar: Type Filters, Search, Export */
    .controls-bar {{
      max-width: 1540px;
      margin: 16px auto;
      padding: 0 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
    }}
    .search-box {{
      position: relative;
      flex: 1;
      min-width: 280px;
      max-width: 480px;
    }}
    .search-box i {{
      position: absolute;
      left: 14px;
      top: 50%;
      transform: translateY(-50%);
      color: #94a3b8;
    }}
    .search-input {{
      width: 100%;
      padding: 10px 16px 10px 40px;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      font-size: 0.95rem;
      box-sizing: border-box;
      background: #ffffff;
    }}
    .search-input:focus {{
      outline: none;
      border-color: var(--accent);
      box-shadow: 0 0 0 3px rgba(37,99,235,0.15);
    }}
    .type-filters {{
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
    }}
    .type-btn {{
      background: #ffffff;
      border: 1px solid #cbd5e1;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 0.85rem;
      font-weight: 600;
      color: #64748b;
      cursor: pointer;
    }}
    .type-btn.active {{
      background: #0f172a;
      color: #ffffff;
      border-color: #0f172a;
    }}
    .actions-group {{
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }}
    .btn-approve-all {{
      background: #059669;
      color: #ffffff;
      border: none;
      padding: 9px 18px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.92rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: background 0.2s;
    }}
    .btn-approve-all:hover {{
      background: #047857;
    }}
    .btn-export {{
      background: #2563eb;
      color: #ffffff;
      border: none;
      padding: 9px 20px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.92rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 2px 6px rgba(37,99,235,0.25);
      transition: background 0.2s;
    }}
    .btn-export:hover {{
      background: #1d4ed8;
    }}

    /* Main Content */
    .audit-main {{
      max-width: 1540px;
      margin: 0 auto 60px auto;
      padding: 0 24px;
    }}

    /* Audit Card */
    .audit-card {{
      background: var(--card-bg);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      margin-bottom: 24px;
      box-shadow: 0 3px 10px rgba(0,0,0,0.03);
      overflow: hidden;
      transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s;
    }}
    .audit-card:hover {{
      box-shadow: 0 6px 16px rgba(0,0,0,0.07);
    }}
    .audit-card.status-approved {{
      border-left: 6px solid var(--emerald);
    }}
    .audit-card.status-custom {{
      border-left: 6px solid var(--amber);
    }}
    .audit-card.status-keep {{
      border-left: 6px solid #64748b;
    }}

    .audit-card-header {{
      background: #f8fafc;
      border-bottom: 1px solid #e2e8f0;
      padding: 14px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
    }}
    .header-left {{
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }}
    .book-badge {{
      background: #0f172a;
      color: #ffffff;
      font-size: 0.8rem;
      font-weight: 800;
      text-transform: uppercase;
      padding: 4px 10px;
      border-radius: 6px;
      letter-spacing: 0.04em;
    }}
    .topic-name {{
      margin: 0;
      font-size: 1.25rem;
      font-weight: 800;
      color: #0f172a;
    }}
    .status-indicator {{
      font-size: 0.85rem;
      font-weight: 800;
      padding: 5px 12px;
      border-radius: 20px;
      background: #dcfce7;
      color: #15803d;
      border: 1px solid #86efac;
    }}
    .status-indicator.custom {{
      background: #fef3c7;
      color: #92400e;
      border-color: #fde68a;
    }}
    .status-indicator.keep {{
      background: #f1f5f9;
      color: #475569;
      border-color: #cbd5e1;
    }}

    /* Badges */
    .badge-pill {{
      font-size: 0.78rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 4px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}
    .pill-cyan {{ background: #ecfeff; color: #0e7490; border: 1px solid #a5f3fc; }}
    .pill-blue {{ background: #eff6ff; color: #1d4ed8; border: 1px solid #bfdbfe; }}
    .pill-purple {{ background: #faf5ff; color: #6b21a8; border: 1px solid #e9d5ff; }}
    .pill-amber {{ background: #fffbeb; color: #b45309; border: 1px solid #fde68a; }}

    /* 2-Column Grid */
    .audit-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      padding: 20px;
    }}
    @media (max-width: 950px) {{
      .audit-grid {{
        grid-template-columns: 1fr;
      }}
    }}
    .audit-col {{
      display: flex;
      flex-direction: column;
    }}
    .col-title {{
      font-size: 0.95rem;
      font-weight: 800;
      color: #334155;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .current-col {{
      background: #fafaf9;
      border: 1px solid #e7e5e4;
      border-radius: 8px;
      padding: 16px;
    }}
    .proposed-col {{
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      border-radius: 8px;
      padding: 16px;
    }}

    /* Previews */
    .svg-preview-box {{
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      padding: 12px;
      margin-bottom: 12px;
      box-shadow: 0 1px 4px rgba(0,0,0,0.04);
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
    }}
    .photo-preview-box {{
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      overflow: hidden;
      margin-bottom: 12px;
      max-height: 250px;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .photo-preview-box img {{
      width: 100%;
      height: 250px;
      object-fit: cover;
      display: block;
    }}
    .current-meta {{
      font-size: 0.9rem;
      color: #475569;
    }}
    .current-meta p {{
      margin: 5px 0;
    }}
    .flag-explanation {{
      background: #fff1f2;
      border: 1px solid #fecdd3;
      border-left: 4px solid var(--crimson);
      border-radius: 6px;
      padding: 8px 12px;
      color: #881337;
      margin-top: 10px;
      font-size: 0.88rem;
    }}

    /* Proposal Box */
    .proposal-box {{
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      padding: 14px 16px;
      margin-bottom: 14px;
    }}
    .prop-subheading {{
      font-size: 0.95rem;
      font-weight: 800;
      color: #065f46;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .prop-text {{
      margin: 0 0 10px 0;
      font-size: 0.93rem;
      color: #1e293b;
      line-height: 1.5;
    }}
    .recommended-action-box {{
      background: #f8fafc;
      border-left: 3px solid #059669;
      padding: 8px 12px;
      border-radius: 0 6px 6px 0;
      margin: 10px 0;
      font-size: 0.88rem;
      color: #334155;
    }}
    .recommended-action-box p {{
      margin: 4px 0 0 0;
    }}
    .tags-container {{
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
      margin-top: 10px;
    }}
    .tag-chip {{
      background: #f1f5f9;
      color: #475569;
      border: 1px solid #e2e8f0;
      font-size: 0.76rem;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 4px;
    }}

    /* Interactive Feedback Box */
    .feedback-action-box {{
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      padding: 14px 16px;
      margin-top: auto;
    }}
    .feedback-heading {{
      font-size: 0.9rem;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .feedback-options {{
      display: flex;
      gap: 16px;
      margin-bottom: 12px;
      flex-wrap: wrap;
    }}
    .radio-label {{
      display: flex;
      align-items: center;
      gap: 6px;
      cursor: pointer;
      font-size: 0.88rem;
      font-weight: 700;
    }}
    .radio-approve {{ color: #059669; }}
    .radio-custom {{ color: #d97706; }}
    .radio-keep {{ color: #475569; }}
    .feedback-textarea {{
      width: 100%;
      height: 60px;
      padding: 8px 12px;
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      font-size: 0.88rem;
      box-sizing: border-box;
      font-family: inherit;
      resize: vertical;
    }}
    .feedback-textarea:focus {{
      outline: none;
      border-color: var(--accent);
      box-shadow: 0 0 0 2px rgba(37,99,235,0.15);
    }}
  </style>
</head>
<body>

  <!-- HEADER -->
  <header class="audit-header">
    <div class="audit-header-inner">
      <div class="header-top-row">
        <div>
          <h1 class="audit-title">Master Functional Skills — <span>Books Visual &amp; Diagram Audit Catalog</span></h1>
          <p class="audit-subtitle">
            Comprehensive audit catalog covering visual assets across all 17 print publications, revision card decks, and workbooks. 
            Review every book cover, technical SVG working-out model, vocational workplace photograph, structural wireframe, and Murphy-style cartoon spread. 
            Approve changes or provide custom notes, then export your signed-off feedback.
          </p>
        </div>
      </div>

      <div class="stats-bar">
        <div class="stat-pill"><i class="fa-solid fa-layer-group"></i> Total Audited: <strong id="stat-total">{total_items}</strong></div>
        <div class="stat-pill stat-approved"><i class="fa-solid fa-check-double"></i> Approved: <strong id="stat-approved">{total_items}</strong></div>
        <div class="stat-pill stat-custom"><i class="fa-solid fa-pen"></i> Custom Changes: <strong id="stat-custom">0</strong></div>
        <div class="stat-pill"><i class="fa-solid fa-book-bookmark"></i> 3D Covers: <strong>{covers_count}</strong></div>
        <div class="stat-pill"><i class="fa-solid fa-bezier-curve"></i> Curated Diagrams: <strong>{diagrams_count}</strong></div>
        <div class="stat-pill"><i class="fa-solid fa-camera"></i> Workplace Photos: <strong>{photos_count}</strong></div>
        <div class="stat-pill"><i class="fa-solid fa-user-tie"></i> Cartoon Characters: <strong>{cartoons_count}</strong></div>
      </div>
    </div>
  </header>

  <!-- STICKY SUITE NAVIGATION -->
  <nav class="audit-nav-bar">
    <div class="audit-nav-inner">
      <div class="nav-tabs">
        <button class="btn-tab active" onclick="filterSuite('all')">All Books ({total_items})</button>
        <button class="btn-tab" onclick="filterSuite('covers')">3D Covers ({covers_count})</button>
        <button class="btn-tab" onclick="filterSuite('maths')">Maths Suite</button>
        <button class="btn-tab" onclick="filterSuite('english')">English Writing Suite</button>
        <button class="btn-tab" onclick="filterSuite('reading')">English Reading Suite</button>
        <button class="btn-tab" onclick="filterSuite('specialist')">Digital &amp; BKSB Suite</button>
        <button class="btn-tab" onclick="filterSuite('spag')">SPaG Mastery Suite</button>
        <button class="btn-tab" onclick="filterSuite('cartoons')">Cartoon Characters</button>
      </div>

      <div class="actions-group">
        <button class="btn-approve-all" onclick="approveAllVisible()"><i class="fa-solid fa-check"></i> Approve All Visible</button>
        <button class="btn-export" onclick="exportFeedback()"><i class="fa-solid fa-file-export"></i> Export Feedback JSON</button>
      </div>
    </div>
  </nav>

  <!-- CONTROLS: TYPE FILTERS & SEARCH -->
  <div class="controls-bar">
    <div class="search-box">
      <i class="fa-solid fa-magnifying-glass"></i>
      <input type="text" class="search-input" id="search-input" placeholder="Search topic, book, standard (e.g. 'grid method', 'letter', 'L2', 'BKSB')..." oninput="applyFilters()">
    </div>

    <div class="type-filters">
      <button class="type-btn active" onclick="filterType('all')">All Types</button>
      <button class="type-btn" onclick="filterType('cover')">Covers</button>
      <button class="type-btn" onclick="filterType('diagram')">Diagrams</button>
      <button class="type-btn" onclick="filterType('photo')">Photos</button>
      <button class="type-btn" onclick="filterType('wireframe')">Wireframes</button>
      <button class="type-btn" onclick="filterType('cartoon')">Cartoons</button>
    </div>
  </div>

  <!-- MAIN AUDIT CARDS -->
  <main class="audit-main" id="cards-container">
    {cards_joined}
  </main>

  <script>
    let currentSuite = 'all';
    let currentType = 'all';

    function filterSuite(suite) {{
      currentSuite = suite;
      document.querySelectorAll('.btn-tab').forEach(b => b.classList.remove('active'));
      event.target.classList.add('active');
      applyFilters();
    }}

    function filterType(type) {{
      currentType = type;
      document.querySelectorAll('.type-btn').forEach(b => b.classList.remove('active'));
      event.target.classList.add('active');
      applyFilters();
    }}

    function applyFilters() {{
      const query = document.getElementById('search-input').value.toLowerCase().trim();
      const cards = document.querySelectorAll('.audit-card');

      cards.forEach(card => {{
        const suite = card.dataset.suite;
        const type = card.dataset.type;
        const text = card.innerText.toLowerCase();

        const matchSuite = (currentSuite === 'all' || suite === currentSuite);
        const matchType = (currentType === 'all' || type === currentType);
        const matchQuery = (!query || text.includes(query));

        if (matchSuite && matchType && matchQuery) {{
          card.style.display = 'block';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}

    function updateCardStatus(id) {{
      const card = document.getElementById(id);
      const decision = card.querySelector(`input[name="decision-${{id}}"]:checked`).value;
      const indicator = document.getElementById(`status-${{id}}`);

      card.classList.remove('status-approved', 'status-custom', 'status-keep');

      if (decision === 'approve') {{
        card.classList.add('status-approved');
        indicator.className = 'status-indicator';
        indicator.innerHTML = '✓ Approved';
      }} else if (decision === 'custom') {{
        card.classList.add('status-custom');
        indicator.className = 'status-indicator custom';
        indicator.innerHTML = '✎ Needs Custom Edit';
      }} else {{
        card.classList.add('status-keep');
        indicator.className = 'status-indicator keep';
        indicator.innerHTML = '✕ Keep Current';
      }}

      saveDecisionsToStorage();
      updateStatsCounters();
    }}

    function autoSaveNote(id) {{
      saveDecisionsToStorage();
    }}

    function approveAllVisible() {{
      document.querySelectorAll('.audit-card').forEach(card => {{
        if (card.style.display !== 'none') {{
          const approveRadio = card.querySelector('input[value="approve"]');
          if (approveRadio) {{
            approveRadio.checked = true;
            updateCardStatus(card.id);
          }}
        }}
      }});
    }}

    function updateStatsCounters() {{
      let approved = 0;
      let custom = 0;
      let keep = 0;
      const cards = document.querySelectorAll('.audit-card');

      cards.forEach(card => {{
        const checked = card.querySelector('input[type="radio"]:checked');
        if (checked) {{
          if (checked.value === 'approve') approved++;
          else if (checked.value === 'custom') custom++;
          else if (checked.value === 'keep') keep++;
        }}
      }});

      document.getElementById('stat-approved').innerText = approved;
      document.getElementById('stat-custom').innerText = custom;
    }}

    function saveDecisionsToStorage() {{
      const data = {{}};
      document.querySelectorAll('.audit-card').forEach(card => {{
        const id = card.id;
        const checked = card.querySelector('input[type="radio"]:checked');
        const note = card.querySelector('.feedback-textarea').value;
        data[id] = {{
          decision: checked ? checked.value : 'approve',
          notes: note
        }};
      }});
      try {{
        localStorage.setItem('mfs_books_image_audit_decisions', JSON.stringify(data));
      }} catch (e) {{}}
    }}

    function loadDecisionsFromStorage() {{
      try {{
        const raw = localStorage.getItem('mfs_books_image_audit_decisions');
        if (!raw) return;
        const data = JSON.parse(raw);
        for (const id in data) {{
          const item = data[id];
          const radio = document.querySelector(`input[name="decision-${{id}}"][value="${{item.decision}}"]`);
          if (radio) radio.checked = true;
          const noteArea = document.getElementById(`note-${{id}}`);
          if (noteArea && item.notes) noteArea.value = item.notes;
          updateCardStatus(id);
        }}
      }} catch (e) {{}}
      updateStatsCounters();
    }}

    function exportFeedback() {{
      const feedbackData = [];
      document.querySelectorAll('.audit-card').forEach(card => {{
        const id = card.id;
        const book = card.querySelector('.book-badge').innerText;
        const title = card.querySelector('.topic-name').innerText;
        const type = card.dataset.type;
        const suite = card.dataset.suite;
        const decisionInput = card.querySelector('input[type="radio"]:checked');
        const decision = decisionInput ? decisionInput.value : 'approve';
        const note = card.querySelector('.feedback-textarea').value.trim();

        feedbackData.push({{
          id: id,
          book: book,
          suite: suite,
          type: type,
          topic: title,
          decision: decision,
          notes: note,
          timestamp: new Date().toISOString()
        }});
      }});

      const jsonStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(feedbackData, null, 2));
      const dl = document.createElement('a');
      dl.setAttribute("href", jsonStr);
      dl.setAttribute("download", "mfs_books_image_audit_feedback.json");
      document.body.appendChild(dl);
      dl.click();
      dl.remove();
      alert("Books audit feedback exported successfully! File downloaded as 'mfs_books_image_audit_feedback.json'.");
    }}

    // Initialise on load
    window.addEventListener('DOMContentLoaded', () => {{
      document.querySelectorAll('.audit-card').forEach(c => updateCardStatus(c.id));
      loadDecisionsFromStorage();
    }});
  </script>
</body>
</html>
"""
    return full_html

def main():
    print("=" * 80)
    print("GENERATING BOOKS IMAGE & DIAGRAM AUDIT CATALOG")
    print("=" * 80)
    html_content = generate_books_audit_html()
    out_file = HERE / "books_image_audit_catalog.html"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Catalog successfully generated: {out_file}")
    print(f"File size: {os.path.getsize(out_file):,} bytes")
    print(f"Total audit items included: {len(AUDIT_ITEMS)}")

if __name__ == "__main__":
    main()
