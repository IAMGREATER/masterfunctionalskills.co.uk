# generate_spag_visuals.py
# Bespoke visual diagrams, document containers, and graphical elements for the 11 SPaG units.

def get_unit_diagram_html(unit_num, level):
    theme_color = "#0f766e" if level == 1 else "#1e3a8a"
    theme_accent = "#0d9488" if level == 1 else "#2563eb"
    theme_light = "#f0fdfa" if level == 1 else "#eff6ff"
    badge_bg = "#ccfbf1" if level == 1 else "#dbeafe"
    
    if unit_num == 1:
        # Unit 1: Sentence Boundaries
        return f"""
<div style="background:{theme_light}; border:1px solid {theme_color}30; border-radius:5px; padding:6px 10px; margin:5px 0; font-size:8.3pt;">
  <div style="font-weight:700; color:{theme_color}; margin-bottom:3px; display:flex; align-items:center; gap:6px;">
    <span>⚡ Visual Anchor: The Anatomy of a Complete Sentence</span>
  </div>
  <div style="display:flex; align-items:center; justify-content:center; gap:6px; flex-wrap:wrap; margin:3px 0;">
    <span style="background:#ffffff; border:1.5px solid {theme_color}; color:{theme_color}; padding:3px 10px; border-radius:15px; font-weight:700;">👤 Subject</span>
    <span style="color:{theme_accent}; font-weight:800;">+</span>
    <span style="background:#ffffff; border:1.5px solid {theme_color}; color:{theme_color}; padding:3px 10px; border-radius:15px; font-weight:700;">⚡ Main Verb</span>
    <span style="color:{theme_accent}; font-weight:800;">+</span>
    <span style="background:#ffffff; border:1.5px solid {theme_color}; color:{theme_color}; padding:3px 10px; border-radius:15px; font-weight:700;">💡 Complete Thought</span>
    <span style="color:{theme_accent}; font-weight:800;">=</span>
    <span style="background:{theme_color}; color:#ffffff; padding:3px 12px; border-radius:15px; font-weight:800;">✓ Complete Sentence</span>
  </div>
</div>"""

    elif unit_num == 2:
        # Unit 2: Subject-Verb Agreement
        return f"""
<div style="background:{theme_light}; border:1px solid {theme_color}30; border-radius:5px; padding:6px 10px; margin:5px 0; font-size:8.3pt;">
  <div style="font-weight:700; color:{theme_color}; margin-bottom:3px; display:flex; align-items:center; gap:6px;">
    <span>⚖️ Visual Anchor: Subject-Verb Agreement Concord</span>
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; margin:2px 0;">
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-left:3px solid {theme_color}; padding:3px 8px; border-radius:3px;">
      <strong>Singular Subject:</strong> <em>The supervisor</em> ➔ <strong>is / walks / has</strong>
    </div>
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-left:3px solid {theme_accent}; padding:3px 8px; border-radius:3px;">
      <strong>Plural Subject:</strong> <em>The supervisors</em> ➔ <strong>are / walk / have</strong>
    </div>
  </div>
</div>"""

    elif unit_num == 3:
        # Unit 3: Formal Register & Politeness
        return f"""
<div style="background:{theme_light}; border:1px solid {theme_color}30; border-radius:5px; padding:6px 10px; margin:5px 0; font-size:8.3pt;">
  <div style="font-weight:700; color:{theme_color}; margin-bottom:3px; display:flex; align-items:center; gap:6px;">
    <span>📈 Visual Anchor: The Formal Letter Register Meter</span>
  </div>
  <div style="display:flex; align-items:center; justify-content:space-between; gap:4px; margin:2px 0; font-size:7.8pt;">
    <div style="background:#fee2e2; border:1px solid #fca5a5; color:#991b1b; padding:3px 6px; border-radius:3px; flex:1; text-align:center;">
      <strong>Informal:</strong> "Give me my money back"
    </div>
    <span style="color:#94a3b8;">&rarr;</span>
    <div style="background:#fef3c7; border:1px solid #fcd34d; color:#92400e; padding:3px 6px; border-radius:3px; flex:1; text-align:center;">
      <strong>Neutral:</strong> "Please send a refund"
    </div>
    <span style="color:#94a3b8;">&rarr;</span>
    <div style="background:#dcfce7; border:1px solid #86efac; color:#166534; padding:3px 6px; border-radius:3px; flex:1.2; text-align:center;">
      <strong>Exam Formal:</strong> "I request a full refund"
    </div>
  </div>
</div>"""

    elif unit_num == 4:
        # Unit 4: Report Capitalisation & Bullet Lists
        return f"""
<div style="background:{theme_light}; border:1px solid {theme_color}30; border-radius:5px; padding:6px 10px; margin:5px 0; font-size:8.3pt;">
  <div style="font-weight:700; color:{theme_color}; margin-bottom:3px; display:flex; align-items:center; gap:6px;">
    <span>🧭 Visual Anchor: The P.A.T.H. Capitalisation Compass for Reports</span>
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:6px; margin:2px 0; text-align:center; font-size:7.6pt;">
    <div style="background:#ffffff; border:1px solid #cbd5e1; padding:3px; border-radius:3px;">
      <strong style="color:{theme_color};">P</strong>: People &amp; Places
    </div>
    <div style="background:#ffffff; border:1px solid #cbd5e1; padding:3px; border-radius:3px;">
      <strong style="color:{theme_color};">A</strong>: Acronyms (NHS)
    </div>
    <div style="background:#ffffff; border:1px solid #cbd5e1; padding:3px; border-radius:3px;">
      <strong style="color:{theme_color};">T</strong>: Titles &amp; Headings
    </div>
    <div style="background:#ffffff; border:1px solid #cbd5e1; padding:3px; border-radius:3px;">
      <strong style="color:{theme_color};">H</strong>: Days &amp; Months
    </div>
  </div>
</div>"""

    elif unit_num == 5:
        # Unit 5: Incident Report Chronology
        return f"""
<div style="background:{theme_light}; border:1px solid {theme_color}30; border-radius:5px; padding:6px 10px; margin:5px 0; font-size:8.3pt;">
  <div style="font-weight:700; color:{theme_color}; margin-bottom:3px; display:flex; align-items:center; gap:6px;">
    <span>⏱️ Visual Anchor: Incident Chronology &amp; Tense Consistency</span>
  </div>
  <div style="display:flex; align-items:center; justify-content:space-between; gap:4px; margin:2px 0; font-size:7.6pt;">
    <div style="background:#ffffff; border:1px solid #cbd5e1; padding:3px 6px; border-radius:3px; text-align:center; flex:1;">
      <strong>1. Exact Time:</strong><br><em>At 10:15 AM</em>
    </div>
    <span style="color:#94a3b8;">&rarr;</span>
    <div style="background:#ffffff; border:1px solid #cbd5e1; padding:3px 6px; border-radius:3px; text-align:center; flex:1.2;">
      <strong>2. Continuous Action:</strong><br><em>was inspecting equipment</em>
    </div>
    <span style="color:#94a3b8;">&rarr;</span>
    <div style="background:#ffffff; border:1px solid #cbd5e1; padding:3px 6px; border-radius:3px; text-align:center; flex:1.2;">
      <strong>3. Sudden Event:</strong><br><em>cable ruptured</em>
    </div>
    <span style="color:#94a3b8;">&rarr;</span>
    <div style="background:#ffffff; border:1px solid #cbd5e1; padding:3px 6px; border-radius:3px; text-align:center; flex:1;">
      <strong>4. Action Taken:</strong><br><em>isolated power</em>
    </div>
  </div>
</div>"""

    elif unit_num == 6:
        # Unit 6: Imperative Command Verbs
        return f"""
<div style="background:{theme_light}; border:1px solid {theme_color}30; border-radius:5px; padding:6px 10px; margin:5px 0; font-size:8.3pt;">
  <div style="font-weight:700; color:{theme_color}; margin-bottom:3px; display:flex; align-items:center; gap:6px;">
    <span>📋 Visual Anchor: Strong Imperative Command Verbs for Leaflets</span>
  </div>
  <div style="display:flex; justify-content:space-around; gap:6px; margin:2px 0; font-size:7.8pt;">
    <span style="background:#ffffff; border:1px solid {theme_color}60; color:{theme_color}; padding:2px 8px; border-radius:3px; font-weight:700;">🔍 Inspect</span>
    <span style="background:#ffffff; border:1px solid {theme_color}60; color:{theme_color}; padding:2px 8px; border-radius:3px; font-weight:700;">⚠️ Avoid</span>
    <span style="background:#ffffff; border:1px solid {theme_color}60; color:{theme_color}; padding:2px 8px; border-radius:3px; font-weight:700;">💧 Wash</span>
    <span style="background:#ffffff; border:1px solid {theme_color}60; color:{theme_color}; padding:2px 8px; border-radius:3px; font-weight:700;">📞 Contact</span>
    <span style="background:#ffffff; border:1px solid {theme_color}60; color:{theme_color}; padding:2px 8px; border-radius:3px; font-weight:700;">📦 Store</span>
  </div>
</div>"""

    elif unit_num == 7:
        # Unit 7: Degrees of Comparison
        return f"""
<div style="background:{theme_light}; border:1px solid {theme_color}30; border-radius:5px; padding:6px 10px; margin:5px 0; font-size:8.3pt;">
  <div style="font-weight:700; color:{theme_color}; margin-bottom:3px; display:flex; align-items:center; gap:6px;">
    <span>⭐ Visual Anchor: The 3-Tier Comparison Ladder in Reviews</span>
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:6px; margin:2px 0; text-align:center; font-size:7.8pt;">
    <div style="background:#ffffff; border:1px solid #cbd5e1; padding:3px; border-radius:3px;">
      <strong>Positive:</strong><br><em>reliable / durable</em>
    </div>
    <div style="background:#ffffff; border:1px solid #cbd5e1; padding:3px; border-radius:3px;">
      <strong style="color:{theme_accent};">Comparative:</strong><br><em>more reliable / faster</em>
    </div>
    <div style="background:#ffffff; border:1.5px solid {theme_color}; padding:3px; border-radius:3px; background:{badge_bg};">
      <strong style="color:{theme_color};">Superlative:</strong><br><em>most reliable / fastest</em>
    </div>
  </div>
</div>"""

    elif unit_num == 8:
        # Unit 8: Apostrophe Matrix
        return f"""
<div style="background:{theme_light}; border:1px solid {theme_color}30; border-radius:5px; padding:6px 10px; margin:5px 0; font-size:8.3pt;">
  <div style="font-weight:700; color:{theme_color}; margin-bottom:3px; display:flex; align-items:center; gap:6px;">
    <span>🎯 Visual Anchor: Apostrophe Decision Matrix</span>
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; margin:2px 0; font-size:7.8pt;">
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-left:3px solid #3b82f6; padding:3px 7px; border-radius:3px;">
      <strong>Contraction (Omission):</strong><br><em>it is</em> ➔ <strong>it's</strong> | <em>cannot</em> ➔ <strong>can't</strong>
    </div>
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-left:3px solid #10b981; padding:3px 7px; border-radius:3px;">
      <strong>Possession (Belonging):</strong><br><em>user + account</em> ➔ <strong>user's account</strong>
    </div>
  </div>
</div>"""

    elif unit_num == 9:
        # Unit 9: Discourse Markers Toolbox
        return f"""
<div style="background:{theme_light}; border:1px solid {theme_color}30; border-radius:5px; padding:6px 10px; margin:5px 0; font-size:8.3pt;">
  <div style="font-weight:700; color:{theme_color}; margin-bottom:3px; display:flex; align-items:center; gap:6px;">
    <span>🧰 Visual Anchor: The Discourse Marker Toolbox for Blogs &amp; Forums</span>
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:6px; margin:2px 0; font-size:7.6pt;">
    <div style="background:#ffffff; border:1px solid #cbd5e1; padding:3px 6px; border-radius:3px;">
      <strong style="color:{theme_color};">➕ Addition:</strong><br>Furthermore, In addition
    </div>
    <div style="background:#ffffff; border:1px solid #cbd5e1; padding:3px 6px; border-radius:3px;">
      <strong style="color:{theme_accent};">⚖️ Contrast:</strong><br>However, On the other hand
    </div>
    <div style="background:#ffffff; border:1px solid #cbd5e1; padding:3px 6px; border-radius:3px;">
      <strong style="color:#d97706;">🎯 Result:</strong><br>Consequently, Therefore
    </div>
  </div>
</div>"""

    elif unit_num == 10:
        # Unit 10: Commas in Clauses
        return f"""
<div style="background:{theme_light}; border:1px solid {theme_color}30; border-radius:5px; padding:6px 10px; margin:5px 0; font-size:8.3pt;">
  <div style="font-weight:700; color:{theme_color}; margin-bottom:3px; display:flex; align-items:center; gap:6px;">
    <span>🥪 Visual Anchor: The Embedded Clause Punctuation Sandwich</span>
  </div>
  <div style="display:flex; align-items:center; justify-content:center; gap:5px; margin:2px 0; font-size:7.8pt;">
    <span style="background:#ffffff; border:1px solid #cbd5e1; padding:3px 7px; border-radius:3px;">[ Main Clause Start ]</span>
    <span style="background:{theme_color}; color:#ffffff; font-weight:800; padding:3px 8px; border-radius:3px;">, [ Clause ] ,</span>
    <span style="background:#ffffff; border:1px solid #cbd5e1; padding:3px 7px; border-radius:3px;">[ Main Clause End ]</span>
  </div>
</div>"""

    elif unit_num == 11:
        # Unit 11: Reflective Learning Cycle
        return f"""
<div style="background:{theme_light}; border:1px solid {theme_color}30; border-radius:5px; padding:6px 10px; margin:5px 0; font-size:8.3pt;">
  <div style="font-weight:700; color:{theme_color}; margin-bottom:3px; display:flex; align-items:center; gap:6px;">
    <span>🔄 Visual Anchor: The Gibbs Reflective Learning Cycle</span>
  </div>
  <div style="display:flex; align-items:center; justify-content:space-between; gap:4px; margin:2px 0; font-size:7.6pt;">
    <div style="background:#ffffff; border:1px solid #cbd5e1; padding:3px 5px; border-radius:3px; flex:1; text-align:center;">
      <strong>1. Description:</strong><br><em>What happened</em>
    </div>
    <span style="color:#94a3b8;">&rarr;</span>
    <div style="background:#ffffff; border:1px solid #cbd5e1; padding:3px 5px; border-radius:3px; flex:1; text-align:center;">
      <strong>2. Feelings:</strong><br><em>How I reacted</em>
    </div>
    <span style="color:#94a3b8;">&rarr;</span>
    <div style="background:#ffffff; border:1px solid #cbd5e1; padding:3px 5px; border-radius:3px; flex:1; text-align:center;">
      <strong>3. Evaluation:</strong><br><em>What worked well</em>
    </div>
    <span style="color:#94a3b8;">&rarr;</span>
    <div style="background:#ffffff; border:1px solid #cbd5e1; padding:3px 5px; border-radius:3px; flex:1; text-align:center;">
      <strong>4. Action Plan:</strong><br><em>Future improvement</em>
    </div>
  </div>
</div>"""

    return ""


def get_formatted_proofread_box(unit_num, level, scenario, text):
    theme_color = "#0f766e" if level == 1 else "#1e3a8a"
    theme_accent = "#0d9488" if level == 1 else "#2563eb"
    theme_light = "#f0fdfa" if level == 1 else "#eff6ff"
    
    # Custom headers and styling for authentic format representation
    if unit_num == 1:
        # Article: News masthead
        header_bar = f"""
      <div style="background:#1e293b; color:#ffffff; padding:4px 10px; border-radius:4px 4px 0 0; display:flex; justify-content:space-between; align-items:center; font-family:'Montserrat', sans-serif; font-size:7.5pt;">
        <span>📰 <strong>THE COMMUNITY OBSERVER</strong> &bull; LOCAL NEWS DESK</span>
        <span style="color:#cbd5e1;">ISSUE 42 &bull; BYLINE DRAFT</span>
      </div>"""
    elif unit_num == 2:
        # Workplace Email: Email window header
        header_bar = f"""
      <div style="background:#f1f5f9; border-bottom:1.5px solid #cbd5e1; padding:4px 10px; border-radius:4px 4px 0 0; font-size:7.6pt; color:#334155;">
        <div style="display:flex; justify-content:space-between; margin-bottom:2px;">
          <span>✉️ <strong>Webmail Client:</strong> [ Inbox &gt; Compose Draft ]</span>
          <span style="background:#22c55e; color:#ffffff; padding:1px 6px; border-radius:3px; font-weight:700; font-size:6.8pt;">SEND READY</span>
        </div>
        <div style="display:grid; grid-template-columns:50px 1fr; row-gap:1px; color:#475569;">
          <span><strong>To:</strong></span><span>department.manager@workplace.co.uk</span>
          <span><strong>Subject:</strong></span><span style="color:{theme_color}; font-weight:600;">Training Course Approval &amp; Shift Cover</span>
        </div>
      </div>"""
    elif unit_num == 3:
        # Formal Letter: Official letterhead
        header_bar = f"""
      <div style="background:#f8fafc; border-bottom:2px solid {theme_color}; padding:5px 10px; border-radius:4px 4px 0 0; display:flex; justify-content:space-between; align-items:center; font-size:7.5pt;">
        <div>
          <div style="font-family:'Montserrat', sans-serif; font-weight:800; color:{theme_color};">CIVIC APPOINTMENTS &amp; CUSTOMER RELATIONS</div>
          <div style="color:#64748b; font-size:6.8pt;">14 Station Approach, Riverside, RS2 4TY</div>
        </div>
        <div style="text-align:right; color:#475569;">
          <strong>Date:</strong> 18 September<br>
          <span style="color:#64748b; font-size:6.8pt;">REF: FORMAL-REG/2026</span>
        </div>
      </div>"""
    elif unit_num == 4:
        # Report: Corporate memorandum header
        header_bar = f"""
      <div style="background:{theme_color}; color:#ffffff; padding:5px 10px; border-radius:4px 4px 0 0; display:flex; justify-content:space-between; align-items:center; font-family:'Montserrat', sans-serif; font-size:7.6pt;">
        <span>📊 <strong>INTERNAL MANAGEMENT AUDIT REPORT</strong></span>
        <span style="background:rgba(255,255,255,0.2); padding:1px 6px; border-radius:3px; font-size:6.8pt;">OFFICIAL DRAFT</span>
      </div>"""
    elif unit_num == 5:
        # Incident Report: HSE safety header
        header_bar = f"""
      <div style="background:#dc2626; color:#ffffff; padding:4px 10px; border-radius:4px 4px 0 0; display:flex; justify-content:space-between; align-items:center; font-family:'Montserrat', sans-serif; font-size:7.5pt;">
        <span>⚠️ <strong>HEALTH &amp; SAFETY EXECUTIVE (HSE) INCIDENT LOG</strong></span>
        <span style="background:#ffffff; color:#dc2626; padding:1px 6px; border-radius:3px; font-weight:800; font-size:6.8pt;">LOG REF: #4092</span>
      </div>"""
    elif unit_num == 6:
        # Advice Leaflet: Tri-fold header
        header_bar = f"""
      <div style="background:#0284c7; color:#ffffff; padding:4px 10px; border-radius:4px 4px 0 0; display:flex; justify-content:space-between; align-items:center; font-family:'Montserrat', sans-serif; font-size:7.5pt;">
        <span>💡 <strong>PUBLIC HEALTH &amp; WELLBEING ADVICE LEAFLET</strong></span>
        <span style="color:#e0f2fe; font-size:6.8pt;">COMMUNITY GUIDANCE PANEL</span>
      </div>"""
    elif unit_num == 7:
        # Review: Star rating header
        header_bar = f"""
      <div style="background:#f8fafc; border-bottom:1.5px solid #cbd5e1; padding:4px 10px; border-radius:4px 4px 0 0; display:flex; justify-content:space-between; align-items:center; font-size:7.6pt;">
        <div>
          <span style="color:#f59e0b; font-size:9pt;">★★★★☆</span>
          <strong style="margin-left:6px; color:#1e293b;">Verified Consumer Product Review</strong>
        </div>
        <span style="background:#ecfdf5; color:#065f46; border:1px solid #a7f3d0; padding:1px 6px; border-radius:3px; font-size:6.8pt; font-weight:700;">VERIFIED BUYER</span>
      </div>"""
    elif unit_num == 8:
        # Feedback Form: Web form header
        header_bar = f"""
      <div style="background:#475569; color:#ffffff; padding:4px 10px; border-radius:4px 4px 0 0; display:flex; justify-content:space-between; align-items:center; font-family:'Montserrat', sans-serif; font-size:7.5pt;">
        <span>📋 <strong>ONLINE SERVICE EVALUATION &amp; FEEDBACK FORM</strong></span>
        <span style="color:#cbd5e1; font-size:6.8pt;">CUSTOMER SUBMISSION #882</span>
      </div>"""
    elif unit_num == 9:
        # Online Forum: Forum thread header
        header_bar = f"""
      <div style="background:#f1f5f9; border-bottom:1.5px solid #cbd5e1; padding:4px 10px; border-radius:4px 4px 0 0; display:flex; justify-content:space-between; align-items:center; font-size:7.6pt;">
        <div style="display:flex; align-items:center; gap:6px;">
          <span style="background:{theme_color}; color:#ffffff; width:18px; height:18px; border-radius:50%; display:inline-flex; align-items:center; justify-content:center; font-size:7pt; font-weight:700;">U</span>
          <strong>Forum Thread:</strong> <span style="color:#64748b;">Posted by User_2026</span>
        </div>
        <span style="color:#f97316; font-weight:700; font-size:7.2pt;">▲ +24 Upvotes</span>
      </div>"""
    elif unit_num == 10:
        # Newsletter: Community masthead
        header_bar = f"""
      <div style="background:{theme_color}; color:#ffffff; padding:4px 10px; border-radius:4px 4px 0 0; display:flex; justify-content:space-between; align-items:center; font-family:'Montserrat', sans-serif; font-size:7.5pt;">
        <span>🗞️ <strong>COMMUNITY DISPATCH NEWSLETTER</strong></span>
        <span style="color:#ffffff; font-size:6.8pt;">VOLUME 18 &bull; ISSUE 3</span>
      </div>"""
    elif unit_num == 11:
        # Learning Log: Journal notebook header
        header_bar = f"""
      <div style="background:#f8fafc; border-bottom:2px dashed {theme_color}; padding:4px 10px; border-radius:4px 4px 0 0; display:flex; justify-content:space-between; align-items:center; font-size:7.6pt;">
        <div>📓 <strong>REFLECTIVE VOCATIONAL LEARNING LOG</strong></div>
        <div style="color:#64748b;"><strong>ENTRY DATE:</strong> Week 6 &bull; Practical Placement</div>
      </div>"""
    else:
        header_bar = ""

    return f"""
    <div style="border:1.5px solid #cbd5e1; border-radius:5px; margin-bottom:6px; box-shadow:0 1px 3px rgba(0,0,0,0.04); background:#ffffff;">
      {header_bar}
      <div style="padding:8px 12px; font-size:9.2pt; line-height:1.44; color:#1e293b;">
        {text}
      </div>
    </div>"""
