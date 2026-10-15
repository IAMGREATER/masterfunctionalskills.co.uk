"""
book_theme.py
Shared styling and helper functions for Master Functional Skills publication books.
Dyslexia-friendly cream background (#FDFBF7), Open Sans & Lexend typography,
crisp borders, clear calculation frames, and full print control.
"""

def get_shared_css(theme_color="#002046", accent_color="#0284c7", light_bg="#f0f7ff"):
    return f"""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@400;500;600;700;800&family=Open+Sans:ital,wght@0,400;0,600;0,700;1,400&family=Montserrat:wght@700;800;900&display=swap');

  @page {{
    size: 210mm 297mm;
    margin: 0;
  }}

  * {{
    box-sizing: border-box;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }}

  body {{
    margin: 0;
    padding: 0;
    background: #fdfbf7;
    color: #1e293b;
    font-family: 'Open Sans', Arial, Helvetica, sans-serif;
    font-size: 8.2pt;
    line-height: 1.48;
    -webkit-font-smoothing: antialiased;
  }}

  :root {{
    --theme: {theme_color};
    --accent: {accent_color};
    --theme-light: {light_bg};
    --bg-cream: #fdfbf7;
    --text-main: #1e293b;
    --border-soft: #cbd5e1;
  }}

  .page {{
    width: 210mm;
    height: 297mm;
    page-break-after: always;
    break-after: page;
    box-sizing: border-box;
    padding: 10mm 13mm 11mm 13mm;
    position: relative;
    background: #fdfbf7;
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }}

  .cover-full-page {{
    padding: 0 !important;
    margin: 0 !important;
  }}

  .cover-full-img {{
    width: 210mm;
    height: 297mm;
    display: block;
    object-fit: cover;
  }}

  .page-header {{
    border-bottom: 2px solid var(--theme);
    padding-bottom: 4px;
    margin-bottom: 7px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-shrink: 0;
  }}

  .page-header-title {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 7.8pt;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    color: var(--theme);
  }}

  .page-header-strand {{
    font-size: 7.2pt;
    font-weight: 700;
    color: #334155;
    background: #e2e8f0;
    padding: 2px 7px;
    border-radius: 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}

  .page-footer {{
    position: absolute;
    bottom: 6mm;
    left: 13mm;
    right: 13mm;
    border-top: 1px solid #cbd5e1;
    padding-top: 4px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 7.2pt;
    color: #64748b;
  }}

  .page-num {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    color: var(--theme);
    font-size: 8pt;
  }}

  .page-body {{
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }}

  h1 {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    color: var(--theme);
    font-size: 13.5pt;
    margin: 0 0 5px 0;
    line-height: 1.2;
  }}

  h2 {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    color: var(--theme);
    font-size: 11pt;
    margin: 0 0 4px 0;
    line-height: 1.25;
  }}

  h3 {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    color: #0f172a;
    font-size: 9pt;
    margin: 4px 0 2px 0;
  }}

  p {{
    margin: 0 0 5px 0;
    line-height: 1.38;
  }}

  /* Visual Boxes */
  .box-concept {{
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-left: 4px solid var(--theme);
    padding: 6px 9px;
    border-radius: 5px;
    margin: 4px 0;
  }}

  .box-formula {{
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    border-left: 4px solid #2563eb;
    padding: 6px 9px;
    border-radius: 5px;
    margin: 4px 0;
  }}

  .box-example {{
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-left: 4px solid #16a34a;
    padding: 6px 9px;
    border-radius: 5px;
    margin: 4px 0;
  }}

  .box-trap {{
    background: #fef2f2;
    border: 1px solid #fecaca;
    border-left: 4px solid #dc2626;
    padding: 6px 9px;
    border-radius: 5px;
    margin: 4px 0;
    color: #991b1b;
  }}

  .box-try {{
    background: #faf5ff;
    border: 1px solid #e9d5ff;
    border-left: 4px solid #9333ea;
    padding: 6px 9px;
    border-radius: 5px;
    margin: 4px 0;
  }}

  .box-exam-tip {{
    background: #fffbeb;
    border: 1px solid #fde68a;
    border-left: 4px solid #d97706;
    padding: 6px 9px;
    border-radius: 5px;
    margin: 4px 0;
    color: #92400e;
  }}

  .tag-label {{
    display: inline-block;
    padding: 1px 6px;
    border-radius: 3px;
    font-size: 6.8pt;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-right: 5px;
  }}

  .tag-blue {{ background: #2563eb; color: #ffffff; }}
  .tag-green {{ background: #16a34a; color: #ffffff; }}
  .tag-red {{ background: #dc2626; color: #ffffff; }}
  .tag-purple {{ background: #9333ea; color: #ffffff; }}
  .tag-amber {{ background: #d97706; color: #ffffff; }}
  .tag-dark {{ background: var(--theme); color: #ffffff; }}

  .step-row {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 2.5px 0;
    border-bottom: 1px dashed #e2e8f0;
    font-size: 7.9pt;
  }}
  .step-row:last-child {{
    border-bottom: none;
  }}

  .mark-badge {{
    background: var(--theme);
    color: #ffffff;
    padding: 1px 5px;
    border-radius: 3px;
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 6.8pt;
    display: inline-block;
  }}

  /* Grids and Workspaces */
  .grid-2col {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    margin: 4px 0;
  }}

  .grid-3col {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 6px;
    margin: 4px 0;
  }}

  .ruled-workspace {{
    height: 60px;
    background: repeating-linear-gradient(
      to bottom,
      transparent,
      transparent 17px,
      #cbd5e1 18px
    );
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    margin: 4px 0;
    position: relative;
  }}

  .grid-workspace {{
    height: 65px;
    background-size: 5mm 5mm;
    background-image:
      linear-gradient(to right, #e2e8f0 1px, transparent 1px),
      linear-gradient(to bottom, #e2e8f0 1px, transparent 1px);
    border: 1px solid #94a3b8;
    border-radius: 4px;
    margin: 4px 0;
    position: relative;
  }}

  .workspace-hint {{
    position: absolute;
    top: 3px;
    right: 6px;
    font-size: 6.5pt;
    color: #94a3b8;
    font-style: italic;
  }}

  .answer-line {{
    display: flex;
    justify-content: flex-end;
    align-items: center;
    gap: 6px;
    font-weight: 700;
    font-size: 8.2pt;
    margin-top: 3px;
  }}

  .answer-blank {{
    display: inline-block;
    min-width: 120px;
    border-bottom: 1.5px solid #1e293b;
    height: 15px;
  }}

  .q-card {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 7px 10px;
    margin: 5px 0;
  }}

  .q-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 3px;
  }}

  .q-num {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 8.5pt;
    color: var(--theme);
  }}

  .q-marks {{
    font-size: 7.2pt;
    font-weight: 800;
    color: #64748b;
  }}

  table.cgp-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 4px 0;
    font-size: 7.8pt;
  }}

  table.cgp-table th, table.cgp-table td {{
    padding: 4px 7px;
    border: 1px solid #cbd5e1;
    text-align: left;
  }}

  table.cgp-table th {{
    background: var(--theme);
    color: #ffffff;
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    font-size: 7.2pt;
    text-transform: uppercase;
  }}

  table.cgp-table tr:nth-child(even) {{
    background: #f8fafc;
  }}

  .key-callout {{
    font-size: 10pt;
    font-weight: 800;
    color: var(--theme);
    text-align: center;
    padding: 3px;
  }}
</style>
"""

def wrap_page(content_html, page_num, header_title, strand_tag, footer_title):
    return f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">{header_title}</div>
    <div class="page-header-strand">{strand_tag}</div>
  </div>
  <div class="page-body">
    {content_html}
  </div>
  <div class="page-footer">
    <div>{footer_title}</div>
    <div class="page-num">Page {page_num}</div>
  </div>
</div>
"""
