"""
a4_kit.py — Master Functional Skills A4 "Fill the Page" layout kit
===================================================================
Implements books/a4/DESIGN_SPEC.md (binding).

Every page is 210 x 297 mm:  header (fixed) -> body (flex column, flex:1) -> footer (fixed).
The LAST block of a page body should be a *fill* block (fill_lines / fill_grid / fill_notes /
hero_image(fill=True) / working_box(fill=True) / photo_grid(fill=True) / practice_stack ...)
so it stretches down to the footer.  Content that does not fit must move to a new page —
never shrink the font.

Typography floor: body 13pt (Entry 3 variant 14pt); nothing under 12pt except the running
header/footer (10pt).

Quick start
-----------
    import a4_kit as K
    pages = [K.front_cover(img),
             K.page(K.page_title("Percentages", kicker="Unit 4") +
                    K.hero_image(photo, "Sale signs use percentages", 80) +
                    K.rule_box("The rule", "...") +
                    K.fill_notes(),
                    header=("Maths Level 2", "Unit 4"), footer="Maths L2 Core", page_no=3),
             K.back_cover(img)]
    K.render_pdf(pages, "out.pdf", theme="maths")
    K.qa_report("out.pdf")
"""

from __future__ import annotations

import html as _html
import json
import math
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
KIT_DIR = Path(__file__).resolve().parent
SITE_ROOT = KIT_DIR.parent.parent                      # masterfunctionalskills.co.uk/
FONT_DIR = KIT_DIR / "fonts"
COVER_DIR = SITE_ROOT / "assets" / "img" / "books"
PHOTO_DIR = SITE_ROOT / "assets" / "img" / "book_photos"
CARTOON_DIR = SITE_ROOT / "assets" / "img" / "book_cartoons"
CHROMIUM = "/usr/lib/chromium/chromium"

# ---------------------------------------------------------------------------
# Themes — colours only differ
# ---------------------------------------------------------------------------
THEMES = {
    #           primary    accent     light      soft-border
    "maths":   ("#0c4a6e", "#0284c7", "#e0f2fe", "#7dd3fc"),
    "english": ("#831843", "#db2777", "#fce7f3", "#f9a8d4"),
    "spag":    ("#3b0764", "#7c3aed", "#ede9fe", "#c4b5fd"),
    "digital": ("#134e4a", "#0d9488", "#ccfbf1", "#5eead4"),
    "bksb":    ("#7c2d12", "#ea580c", "#ffedd5", "#fdba74"),
    "mock":    ("#1e293b", "#dc2626", "#fee2e2", "#fca5a5"),
}

# Manual overrides (cover filename -> (primary, accent, light, soft)) when auto-extraction
# picks the wrong colour.  Leave empty unless a cover needs correcting.
COVER_THEME_OVERRIDES: dict[str, tuple[str, str, str, str]] = {
    "maths_l2_core_cover_page-1.png":        ("#002040", "#0077a8", "#e5ecf3", "#8aa6c1"),
    "maths_l2_companion_cover_page-1.png":   ("#0c4a6e", "#0284c7", "#e0f2fe", "#7dd3fc"),
    "mock_pack_maths_l2_cover_page-1.png":   ("#182028", "#0a7ea8", "#e6f3f8", "#9cc9db"),
    "mock_pack_english_l2_cover_page-1.png": ("#2a1840", "#7c3aed", "#f1eafc", "#c4a8f0"),
    "digital_skills_cover_page-1.png":       ("#3b0764", "#7c3aed", "#ede9fe", "#c4b5fd"),
    "spag_l2_mastery_cover-01.png":          ("#3b0764", "#7c3aed", "#f1eaf8", "#b99bd3"),
    "spag_l1_mastery_cover-01.png":          ("#064e3b", "#047857", "#ecfdf5", "#a7f3d0"),
    "spag_e3_mastery_cover-01.png":          ("#7c2d12", "#a16207", "#fbeee6", "#d9a68e"),
    "reading_l1_core_cover_page-1.png":      ("#064e3b", "#047857", "#ecfdf5", "#a7f3d0"),
    "reading_l2_core_cover_page-1.png":      ("#3b0764", "#7c3aed", "#ede9fe", "#c4b5fd"),
}


def _hex(rgb) -> str:
    return "#%02x%02x%02x" % tuple(max(0, min(255, int(round(c)))) for c in rgb)


def _mix(rgb, other, t: float):
    return tuple(a + (b - a) * t for a, b in zip(rgb, other))


def _lum(rgb) -> float:
    def ch(c):
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def _contrast(a, b) -> float:
    la, lb = sorted((_lum(a), _lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def theme_from_cover(cover_path) -> tuple[str, str, str, str]:
    """Derive (primary, accent, light, soft) from a front-cover image.

    primary : the cover's dominant saturated dark colour (background or title/badge ink)
    accent  : the cover's highlight colour (e.g. gold badge), darkened until it reads on cream
    light   : primary tinted ~90% towards white (panel fills)
    soft    : primary tinted ~55% towards white (borders)
    Samples only the top 28% and bottom 30% bands so photo-knockout lettering is ignored."""
    import colorsys
    from collections import Counter
    from PIL import Image
    name = Path(str(cover_path)).name
    if name in COVER_THEME_OVERRIDES:
        return COVER_THEME_OVERRIDES[name]
    im = Image.open(cover_path).convert("RGB").resize((124, 175))
    w, h = im.size
    px = im.load()
    rows = list(range(0, int(h * 0.28))) + list(range(int(h * 0.70), h))
    cnt = Counter()
    for y in rows:
        for x in range(w):
            r, g, b = px[x, y]
            cnt[(r // 8 * 8, g // 8 * 8, b // 8 * 8)] += 1

    def hsv(c):
        return colorsys.rgb_to_hsv(*(v / 255 for v in c))

    darks = [(c, n) for c, n in cnt.items() if hsv(c)[1] > 0.35 and 0.10 < hsv(c)[2] < 0.75]
    if not darks:
        return THEMES["maths"]
    primary = max(darks, key=lambda cn: cn[1])[0]
    ph = hsv(primary)[0]
    brights = [(c, n) for c, n in cnt.items()
               if hsv(c)[1] > 0.45 and hsv(c)[2] > 0.70
               and min(abs(hsv(c)[0] - ph), 1 - abs(hsv(c)[0] - ph)) > 0.08]
    if brights and max(n for _, n in brights) >= 12:
        accent = max(brights, key=lambda cn: cn[1])[0]
    else:  # no distinct highlight: use a brighter version of primary
        hh, ss, vv = hsv(primary)
        accent = tuple(v * 255 for v in colorsys.hsv_to_rgb(hh, min(1, ss * 1.05), min(1, vv * 1.6 + 0.15)))
    # primary must read as heading ink on cream (>= 7:1); accent must read as text/border (>= 3.2:1)
    cream = (253, 251, 247)
    while _contrast(primary, cream) < 7:
        primary = _mix(primary, (0, 0, 0), 0.12)
    while _contrast(accent, cream) < 3.2:
        accent = _mix(accent, (0, 0, 0), 0.08)
    light = _mix(primary, (255, 255, 255), 0.90)
    soft = _mix(primary, (255, 255, 255), 0.55)
    return (_hex(primary), _hex(accent), _hex(light), _hex(soft))

E = _html.escape


def _uri(path) -> str:
    """file:// URI for an absolute (or site-relative) path."""
    if path is None:
        return ""
    s = str(path)
    if s.startswith(("file://", "http://", "https://", "data:")):
        return s
    p = Path(s)
    if not p.is_absolute():
        p = SITE_ROOT / p
    return p.resolve().as_uri()


def _exists(path) -> bool:
    if not path:
        return False
    s = str(path)
    if s.startswith(("http://", "https://", "data:")):
        return True
    if s.startswith("file://"):
        s = s[7:]
    p = Path(s)
    if not p.is_absolute():
        p = SITE_ROOT / p
    return p.exists()


# ---------------------------------------------------------------------------
# CSS
# ---------------------------------------------------------------------------
def get_css(theme: str = "maths", entry3: bool = False) -> str:
    """Return the full <style> block for a subject theme.

    theme  : maths | english | spag | digital | bksb | mock
    entry3 : True -> 14pt body / 1.6 line-height (Entry Level 3 books)
    """
    primary, accent, light, soft = (tuple(theme) if isinstance(theme, (tuple, list))
                                    else THEMES.get(theme, THEMES["maths"]))
    body_pt, lh = (14, 1.6) if entry3 else (13, 1.5)
    f = FONT_DIR
    return f"""
<style>
@font-face {{ font-family:'Lexend'; src:url('{(f / "Lexend.ttf").as_uri()}') format('truetype'); font-weight:100 900; }}
@font-face {{ font-family:'Open Sans'; src:url('{(f / "OpenSans.ttf").as_uri()}') format('truetype'); font-weight:300 800; }}
@font-face {{ font-family:'Montserrat'; src:url('{(f / "Montserrat.ttf").as_uri()}') format('truetype'); font-weight:100 900; }}
@font-face {{ font-family:'RefSerif'; src:url('{(f / "LiberationSerif-Regular.ttf").as_uri()}'); font-weight:400; font-style:normal; }}
@font-face {{ font-family:'RefSerif'; src:url('{(f / "LiberationSerif-Bold.ttf").as_uri()}'); font-weight:700; font-style:normal; }}
@font-face {{ font-family:'RefSerif'; src:url('{(f / "LiberationSerif-Italic.ttf").as_uri()}'); font-weight:400; font-style:italic; }}
@font-face {{ font-family:'RefSerif'; src:url('{(f / "LiberationSerif-BoldItalic.ttf").as_uri()}'); font-weight:700; font-style:italic; }}
@font-face {{ font-family:'RefNarrow'; src:url('{(f / "NimbusSansNarrow-Regular.otf").as_uri()}'); font-weight:400; }}
@font-face {{ font-family:'RefNarrow'; src:url('{(f / "NimbusSansNarrow-Bold.otf").as_uri()}'); font-weight:700; }}
@page {{ size:210mm 297mm; margin:0; }}
* {{ box-sizing:border-box; -webkit-print-color-adjust:exact !important; print-color-adjust:exact !important; }}
:root {{
  --primary:{primary}; --accent:{accent}; --light:{light}; --soft:{soft};
  --cream:#FDFBF7; --ink:#1e293b; --muted:#475569; --line:#94a3b8;
  --gold:#b45309; --gold-bg:#fef3c7; --gold-bd:#f59e0b;
  --red:#b91c1c; --red-bg:#fee2e2; --red-bd:#ef4444;
  --green:#15803d; --green-bg:#dcfce7; --green-bd:#22c55e;
}}
html, body {{ margin:0; padding:0; background:#FDFBF7; }}
body {{ font-family:'Lexend','Open Sans',Arial,sans-serif; font-size:{body_pt}pt; line-height:{lh};
        color:var(--ink); text-align:left; -webkit-font-smoothing:antialiased; }}
p {{ margin:0 0 2.5mm 0; }}
ul, ol {{ margin:1mm 0 2mm 0; padding-left:7mm; }}
li {{ margin-bottom:1mm; }}
strong {{ font-weight:700; }}

/* ---------- page shell ---------- */
.page {{ width:210mm; height:297mm; overflow:hidden; position:relative; background:var(--cream);
         page-break-after:always; break-after:page; padding:12mm 14mm 12mm 14mm;
         display:flex; flex-direction:column; }}
.page:last-child {{ page-break-after:auto; break-after:auto; }}
.run-head {{ flex:0 0 auto; display:flex; justify-content:space-between; align-items:center;
             font-family:'Montserrat',sans-serif; font-size:10pt; /* hf-ok */ font-weight:700;
             color:var(--primary); letter-spacing:.4px; border-bottom:2px solid var(--primary);
             padding-bottom:2mm; margin-bottom:4mm; text-transform:uppercase; }}
.run-head .rh-right {{ background:var(--primary); color:#fff; border-radius:20px; padding:.6mm 3.5mm; }}
.run-foot {{ flex:0 0 auto; display:flex; justify-content:space-between; align-items:center;
             font-size:10pt; /* hf-ok */ color:var(--muted); border-top:1.5px solid var(--soft);
             padding-top:2mm; margin-top:3.5mm; }}
.run-foot .pg {{ font-family:'Montserrat',sans-serif; font-weight:800; color:#fff; background:var(--primary);
                min-width:9mm; height:7mm; border-radius:4mm; display:flex; align-items:center;
                justify-content:center; font-size:11pt; /* hf-ok */ padding:0 2mm; }}
.body {{ flex:1 1 auto; min-height:0; display:flex; flex-direction:column; gap:3mm; }}
.body > * {{ flex:0 0 auto; }}
.body > .fill, .fill {{ flex:1 1 0; min-height:22mm; }}

/* ---------- covers ---------- */
.page.cover {{ padding:0; background:#0b1220; }}
.page.cover img.full {{ width:210mm; height:297mm; object-fit:cover; display:block; }}

/* ---------- headings ---------- */
.ptitle {{ display:flex; align-items:center; gap:5mm; }}
.ptitle .badge {{ flex:0 0 auto; min-width:20mm; width:auto; height:20mm; padding:0 4mm; box-sizing:border-box;
                  border-radius:5mm; background:var(--primary); color:#fff;
                  font-family:'Montserrat',sans-serif; font-weight:900; font-size:22pt;
                  display:inline-flex; align-items:center; justify-content:center; white-space:nowrap;
                  line-height:1; text-align:center; }}
.ptitle .kicker {{ font-family:'Montserrat',sans-serif; font-weight:800; font-size:12pt; color:var(--accent);
                   text-transform:uppercase; letter-spacing:1px; }}
h1 {{ font-family:'Lexend',sans-serif; font-weight:800; font-size:28pt; line-height:1.12; margin:0;
      color:var(--primary); }}
h2 {{ font-family:'Lexend',sans-serif; font-weight:700; font-size:19pt; line-height:1.2; margin:0 0 2mm 0;
      color:var(--primary); }}
h3 {{ font-family:'Lexend',sans-serif; font-weight:700; font-size:15pt; margin:0 0 1.5mm 0; color:var(--ink); }}
.sec {{ display:flex; align-items:center; gap:3mm; font-family:'Lexend',sans-serif; font-weight:700;
        font-size:18pt; color:var(--primary); margin:0; }}
.sec .tag {{ width:10mm; height:10mm; border-radius:50%; background:var(--accent); color:#fff;
             display:flex; align-items:center; justify-content:center; font-size:15pt; font-weight:800; }}
.lead {{ font-size:14pt; color:var(--muted); margin:0; }}

/* ---------- images ---------- */
.hero {{ position:relative; border-radius:8px; overflow:hidden; background:var(--light);
         border:1.5px solid var(--soft); display:flex; flex-direction:column; }}
.hero .imgwrap {{ position:relative; flex:1 1 auto; min-height:0; }}
.hero img {{ position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:center top; display:block; }}
.hero .cap {{ flex:0 0 auto; font-size:12pt; color:var(--ink); background:#fff; padding:2mm 4mm;
              border-top:1.5px solid var(--soft); }}
.ph {{ position:absolute; inset:0; display:flex; flex-direction:column; align-items:center; justify-content:center;
       gap:2mm; color:var(--primary); font-weight:700; font-size:14pt; text-align:center; padding:4mm;
       background:repeating-linear-gradient(135deg, var(--light) 0 14px, #ffffff 14px 28px); }}
.ph svg {{ width:22mm; height:22mm; opacity:.55; }}
.ph small {{ font-size:12pt; font-weight:400; color:var(--muted); }}

/* photo tiles */
.pgrid {{ display:grid; gap:4mm; }}
.pgrid.fill {{ grid-auto-rows:1fr; }}
.tile {{ background:#fff; border:1.5px solid var(--soft); border-radius:8px; overflow:hidden;
         display:flex; flex-direction:column; min-height:0; }}
.tile .imgwrap {{ position:relative; flex:1 1 auto; min-height:38mm; }}
.tile img {{ position:absolute; inset:0; width:100%; height:100%; object-fit:cover; }}
.tile .word {{ font-family:'Lexend',sans-serif; font-weight:800; font-size:16pt; color:var(--primary);
               padding:2mm 3.5mm 0 3.5mm; line-height:1.2; }}
.tile .ex {{ font-size:12.5pt; line-height:1.35; padding:1mm 3.5mm 3mm 3.5mm; color:var(--ink); }}

/* character + bubble */
.charrow {{ display:flex; align-items:center; gap:4.5mm; }}
.charrow.right {{ flex-direction:row-reverse; }}
.charrow .who {{ flex:0 0 auto; display:flex; flex-direction:column; align-items:center; }}
.charrow .who img, .charrow .who svg {{ height:var(--ch, 48mm); width:auto; max-width:55mm; object-fit:contain; display:block; }}
.charrow .who .nm {{ font-family:'Montserrat',sans-serif; font-weight:800; font-size:11.5pt; /* hf-ok */ color:var(--primary);
                     margin-top:1mm; }}
.bubble {{ position:relative; flex:1 1 auto; background:#fff; border:2.5px solid var(--primary);
           border-radius:8mm; padding:3.5mm 5.5mm; font-size:12.5pt; line-height:1.42; }}
.bubble:before {{ content:''; position:absolute; top:50%; left:-7mm; margin-top:-5mm; border:5mm solid transparent;
                  border-right:7mm solid var(--primary); border-left:0; }}
.bubble:after {{ content:''; position:absolute; top:50%; left:-3.6mm; margin-top:-3.4mm; border:3.4mm solid transparent;
                 border-right:4.6mm solid #fff; border-left:0; }}
.charrow.right .bubble:before {{ left:auto; right:-7mm; border-right:0; border-left:7mm solid var(--primary); }}
.charrow.right .bubble:after {{ left:auto; right:-3.6mm; border-right:0; border-left:4.6mm solid #fff; }}

/* ---------- boxes ---------- */
.box {{ border-radius:8px; padding:3mm 4.5mm; font-size:12.5pt; line-height:1.42; }}
.box .bt {{ font-family:'Lexend',sans-serif; font-weight:800; font-size:13.5pt; margin-bottom:1.2mm;
            display:flex; align-items:center; gap:2.5mm; }}
.box .bt .ico {{ width:7mm; height:7mm; border-radius:50%; display:inline-flex; align-items:center;
                 justify-content:center; color:#fff; font-size:12pt; flex:0 0 auto; }}
.box p:last-child, .box ul:last-child {{ margin-bottom:0; }}
.rule {{ background:var(--light); border:2px solid var(--accent); border-left:9px solid var(--primary); padding:2.5mm 4mm; font-size:12pt; line-height:1.38; }}
.rule .bt {{ color:var(--primary); }} .rule .ico {{ background:var(--primary); }}
.golden {{ background:var(--gold-bg); border:2px solid var(--gold-bd); }}
.golden .bt {{ color:var(--gold); }} .golden .ico {{ background:var(--gold-bd); }}
.watch {{ background:var(--red-bg); border:2px solid var(--red-bd); }}
.watch .bt {{ color:var(--red); }} .watch .ico {{ background:var(--red-bd); }}
.pair {{ display:grid; grid-template-columns:1fr 1fr; gap:4mm; }}
.worked {{ background:#fff; border:2px solid var(--soft); }}
.worked .bt {{ color:var(--primary); }} .worked .ico {{ background:var(--accent); }}
.worked .q {{ font-weight:600; margin-bottom:2mm; }}
.worked ol.steps {{ margin:0; padding-left:0; list-style:none; counter-reset:st; }}
.worked ol.steps li {{ counter-increment:st; position:relative; padding-left:10mm; margin-bottom:1.5mm; }}
.worked ol.steps li:before {{ content:counter(st); position:absolute; left:0; top:.3mm; width:7mm; height:7mm;
                               border-radius:50%; background:var(--light); color:var(--primary); font-weight:800;
                               font-size:12pt; display:flex; align-items:center; justify-content:center;
                               border:1.5px solid var(--accent); }}
.worked .ans {{ margin-top:2mm; background:var(--green-bg); border:1.5px solid var(--green-bd); border-radius:6px;
                padding:2mm 4mm; font-weight:700; color:var(--green); }}
.compare {{ display:grid; grid-template-columns:1fr 1fr; gap:3mm; }}
.compare .bad, .compare .good {{ border-radius:8px; padding:2mm 3.5mm; font-size:11pt; line-height:1.25; }}
.compare .bad {{ background:var(--red-bg); border:1.5px solid var(--red-bd); }}
.compare .good {{ background:var(--green-bg); border:1.5px solid var(--green-bd); }}
.compare .lab {{ font-weight:800; font-size:11pt; margin-bottom:0.6mm; }}
.compare .bad .lab {{ color:var(--red); }} .compare .good .lab {{ color:var(--green); }}
.formula-strip {{ display:flex; flex-wrap:wrap; gap:1.5mm; align-items:center; margin:1.5mm 0 2mm 0; font-weight:700; }}
.fpill {{ display:inline-block; border-radius:5mm; padding:0.6mm 3mm; background:#fff; border:1.5px solid var(--accent);
          color:var(--primary); font-size:10pt; line-height:1.2; }}
.box.rule .formula-strip {{ margin:1mm 0 1.5mm 0; gap:1.2mm; }}
.box.rule .fpill {{ font-size:9pt; padding:0.4mm 2.2mm; border-width:1.2px; }}
.box.rule ul {{ margin:1mm 0 0 14px; line-height:1.24; }}
.box.rule + .compare {{ gap:2.5mm; margin-top:0.5mm; }}
.box.rule + .compare .bad, .box.rule + .compare .good {{ padding:1.5mm 3mm; font-size:9.5pt; line-height:1.2; }}
.box.rule + .compare .lab {{ font-size:10pt; margin-bottom:0.4mm; }}

/* ---------- exercises ---------- */
.exlist {{ margin:0; padding:0; list-style:none; counter-reset:ex var(--start, 0); display:flex; flex-direction:column; gap:3mm; }}
.exlist > li {{ counter-increment:ex; position:relative; padding-left:11mm; margin:0; font-size:13pt; }}
.exlist > li:before {{ content:counter(ex); position:absolute; left:0; top:0; width:8mm; height:8mm; border-radius:2mm;
                       background:var(--primary); color:#fff; font-weight:800; font-size:12.5pt;
                       display:flex; align-items:center; justify-content:center; }}
.opts {{ list-style:none; margin:1.5mm 0 0 0; padding:0; display:flex; flex-direction:column; gap:1mm; }}
.opts.inline {{ flex-direction:row; flex-wrap:wrap; gap:2mm 9mm; }}
.opts li {{ margin:0; display:flex; gap:2.5mm; align-items:flex-start; }}
.opts .ck {{ flex:0 0 auto; width:6mm; height:6mm; border:2px solid var(--line); border-radius:1.5mm; margin-top:.8mm; background:#fff; }}
.aline {{ height:10mm; border-bottom:1.6px solid var(--line); }}
.marks {{ float:right; font-size:12pt; font-weight:700; color:var(--muted); margin-left:3mm; }}

/* working boxes */
.wbox {{ border:2px solid var(--soft); border-radius:8px; background:#fff; display:flex; flex-direction:column;
         min-height:var(--h, 30mm); overflow:hidden; }}
.wbox .wl {{ flex:0 0 auto; font-size:12pt; font-weight:700; color:var(--primary); background:var(--light);
             padding:1.2mm 4mm; border-bottom:1.5px solid var(--soft); }}
.wbox .wa {{ flex:1 1 auto; }}
.wbox .wa.grid {{ background-color:#fff; background-image:
     linear-gradient(to right, #cdd8e6 1px, transparent 1px), linear-gradient(to bottom, #cdd8e6 1px, transparent 1px);
     background-size:5mm 5mm; }}
.wbox .wans {{ flex:0 0 auto; display:flex; justify-content:flex-end; align-items:center; gap:3mm; padding:2mm 4mm;
               border-top:1.5px dashed var(--soft); font-weight:700; font-size:12.5pt; color:var(--primary); }}
.wbox .wans span.blank {{ display:inline-block; width:45mm; border-bottom:2px solid var(--ink); height:7mm; }}
.qstack {{ display:flex; flex-direction:column; gap:4mm; }}
.qstack > .qitem {{ flex:1 1 0; display:flex; flex-direction:column; gap:2mm; min-height:0; }}
.qstack > .qitem > .wbox {{ flex:1 1 0; }}
.qitem .qtext {{ display:flex; gap:3mm; font-size:13pt; }}
.qitem .qn {{ flex:0 0 auto; width:9mm; height:9mm; border-radius:2.2mm; background:var(--primary); color:#fff;
              font-weight:800; display:flex; align-items:center; justify-content:center; font-size:13pt; }}
.qitem .qbody {{ flex:1 1 auto; }}

/* fill blocks */
.flines {{ border-radius:6px; background-color:#fff; border:1.5px solid var(--soft);
           display:flex; flex-direction:column; overflow:hidden; }}
.flines .fl-head, .flines .fl {{ flex:0 0 auto; background:#fff; padding:2.5mm 5mm 1mm 5mm;
                                font-weight:700; color:var(--primary); font-size:11.5pt; /* hf-ok */ }}
.flines .fl-lines {{ flex:1 1 auto; margin:2.5mm 5mm 3mm 5mm;
                     background-image:repeating-linear-gradient(to bottom, transparent 0,
                     transparent calc(var(--gap, 11mm) - 1.6px), #9fb0c4 calc(var(--gap, 11mm) - 1.6px),
                     #9fb0c4 var(--gap, 11mm)); }}
.flines .fl-head + .fl-lines, .flines .fl + .fl-lines {{ margin-top:0; }}

.fgrid {{ border:2px solid var(--soft); border-radius:6px; background-color:#fff;
          display:flex; flex-direction:column; overflow:hidden; }}
.fgrid .fg-head, .fgrid .fl-head, .fgrid .fl {{ flex:0 0 auto; background:#fff; padding:2.5mm 5mm 1mm 5mm;
                                               font-weight:700; color:var(--primary); font-size:11.5pt; /* hf-ok */ }}
.fgrid .fg-grid {{ flex:1 1 auto; margin:2.5mm 3mm 3mm 3mm;
                   background-image:
                     linear-gradient(to right, #cdd8e6 1px, transparent 1px),
                     linear-gradient(to bottom, #cdd8e6 1px, transparent 1px),
                     linear-gradient(to right, #aebdd1 1px, transparent 1px),
                     linear-gradient(to bottom, #aebdd1 1px, transparent 1px);
                   background-size:5mm 5mm, 5mm 5mm, 25mm 25mm, 25mm 25mm; }}
.fgrid .fg-head + .fg-grid, .fgrid .fl-head + .fg-grid, .fgrid .fl + .fg-grid {{ margin-top:0; }}

.fnotes {{ border:2px dashed var(--soft); border-radius:8px; background:#fff; display:flex; flex-direction:column; }}
.fnotes .nt {{ flex:0 0 auto; font-family:'Lexend',sans-serif; font-weight:800; font-size:13.5pt; color:var(--primary);
               padding:2.5mm 5mm 0 5mm; }}
.fnotes .nl {{ flex:1 1 auto; margin:2.5mm 5mm 3mm 5mm; background-image:repeating-linear-gradient(to bottom,
              transparent 0, transparent calc(10mm - 1.4px), #b6c3d3 calc(10mm - 1.4px), #b6c3d3 10mm); }}
.fnotes .nt + .nl {{ margin-top:0; }}

/* layout */
.cols {{ display:grid; gap:5mm; align-items:stretch; }}
.cols > div {{ min-width:0; display:flex; flex-direction:column; gap:4mm; }}
.cols > div > .fill {{ flex:1 1 0; }}
.fillcol {{ display:flex; flex-direction:column; }}
table.t {{ width:100%; border-collapse:separate; border-spacing:0; font-size:12pt; border:2px solid var(--soft);
           border-radius:8px; overflow:hidden; background:#fff; }}
table.t th {{ background:var(--primary); color:#fff; text-align:left; padding:2.2mm 3.5mm; font-size:12.5pt; }}
table.t td {{ padding:2.2mm 3.5mm; border-top:1px solid #e2e8f0; vertical-align:top; }}
table.t tr:nth-child(even) td {{ background:var(--light); }}
.diag {{ display:flex; flex-direction:column; align-items:center; background:#fff; border:1.5px solid var(--soft);
         border-radius:8px; padding:3mm; }}
.diag .cap {{ font-size:12pt; color:var(--muted); margin-top:1.5mm; text-align:center; }}
.diag svg {{ display:block; }}
.anscols {{ column-count:2; column-gap:8mm; column-rule:1.5px solid var(--soft); font-size:12.5pt; line-height:1.45; }}
.anscols .ak {{ break-inside:avoid; margin-bottom:3mm; }}
.anscols .ak h3 {{ font-size:14pt; color:var(--primary); margin-bottom:1mm; }}
.chip {{ display:inline-block; background:var(--light); color:var(--primary); border:1.5px solid var(--soft);
         border-radius:5mm; padding:.5mm 3.5mm; font-weight:700; font-size:12pt; }}
.overflow-flag {{ position:absolute; top:0; left:0; right:0; background:#dc2626; color:#fff; font-size:14pt;
                  font-weight:800; text-align:center; padding:2mm; z-index:99; }}

/* ---------- reference back matter (answers / mark schemes / glossary / index) ---------- */
.page.ref {{ background:#fff; }}
.page.ref .run-head {{ font-family:'RefNarrow',sans-serif; color:#000; border-bottom:1px solid #000; letter-spacing:.2px; }}
.page.ref .run-head .rh-right {{ background:none; color:#000; padding:0; border-radius:0; }}
.page.ref .run-foot {{ font-family:'RefNarrow',sans-serif; color:#000; border-top:.75px solid #000; }}
.page.ref .run-foot .pg {{ background:none; color:#000; font-family:'RefNarrow',sans-serif; font-weight:700; }}
.page.ref .body {{ gap:2mm; }}
.ref-title {{ flex:0 0 auto; font-family:'RefNarrow',sans-serif; font-weight:700; font-size:17pt; /* ref-ok */ color:#000;
              text-transform:uppercase; letter-spacing:.4px; border-bottom:2px solid #000; padding-bottom:1mm; }}
.ref-title small {{ display:block; font-size:9.5pt; /* ref-ok */ font-weight:400; text-transform:none; letter-spacing:0; }}
.ref-body {{ flex:1 1 0; min-height:0; column-count:var(--cols,2); column-gap:6mm; column-rule:.5px solid #000;
             column-fill:auto; font-family:'RefSerif',serif; font-size:9.6pt; /* ref-ok */ line-height:1.27; color:#000; }}
.ref-body * {{ color:#000 !important; }}
.ref-blk {{ break-inside:avoid; margin:0 0 1.6mm 0; }}
.ref-blk.split {{ break-inside:auto; }}
.ref-body h3 {{ font-family:'RefNarrow',sans-serif; font-weight:700; font-size:10.6pt; /* ref-ok */ margin:0 0 .8mm 0;
                padding-bottom:.3mm; border-bottom:.5px solid #000; break-after:avoid; text-transform:uppercase; }}
.ref-body h4 {{ font-family:'RefNarrow',sans-serif; font-weight:700; font-size:9.8pt; /* ref-ok */ margin:1mm 0 .4mm 0; }}
.ref-body p {{ margin:0 0 .9mm 0; }}
.ref-body .qa {{ margin:0 0 .9mm 0; padding-left:7mm; text-indent:-7mm; }}
.ref-body .qa b.qn {{ display:inline-block; width:7mm; text-indent:0; }}
.ref-body .mk {{ font-weight:700; white-space:nowrap; }}
.ref-body .wk {{ display:block; padding-left:7mm; text-indent:0; font-style:italic; }}
.ref-body ul, .ref-body ol {{ margin:.4mm 0 .9mm 0; padding-left:5mm; }}
.ref-body li {{ margin:0 0 .3mm 0; }}
.ref-body table {{ width:100%; border-collapse:collapse; font-size:9pt; /* ref-ok */ margin:.5mm 0 1mm 0; }}
.ref-body td, .ref-body th {{ border:.5px solid #000; padding:.6mm 1mm; vertical-align:top; text-align:left; }}
.ref-body dl {{ margin:0; }} .ref-body dt {{ font-weight:700; }} .ref-body dd {{ margin:0 0 .8mm 4mm; }}
.ref-body .ix {{ display:flex; justify-content:space-between; gap:2mm; }}
.ref-body .ix span:last-child {{ white-space:nowrap; }}
.ref-body .ix-letter {{ font-family:'RefNarrow',sans-serif; font-weight:700; font-size:11pt; /* ref-ok */ margin:1.4mm 0 .3mm 0; break-after:avoid; }}
.ref-notes {{ border-top:1px solid #000; display:flex; flex-direction:column; min-height:18mm; }}
.ref-notes .nt {{ font-family:'RefNarrow',sans-serif; font-weight:700; font-size:10pt; /* ref-ok */ color:#000; padding-top:1mm; }}
.ref-notes .nl {{ flex:1 1 auto; background-image:repeating-linear-gradient(to bottom, transparent 0,
                  transparent calc(8mm - 1px), #9ca3af calc(8mm - 1px), #9ca3af 8mm); }}
</style>
"""


# ---------------------------------------------------------------------------
# Page shell
# ---------------------------------------------------------------------------
def page(body_html: str, header=None, footer: str | None = None, page_no=None, extra_class: str = "") -> str:
    """One A4 page.  header = "Left" or ("Left", "Right pill");  footer = left footer text.

    The page body is a flex column; give the last child the class `fill` (all fill_* helpers
    do this) so it grows to the footer.
    """
    head = ""
    if header:
        if isinstance(header, (tuple, list)):
            l, r = (list(header) + [""])[:2]
        else:
            l, r = header, ""
        head = (f'<div class="run-head"><span>{l}</span>'
                + (f'<span class="rh-right">{r}</span>' if r else "") + "</div>")
    foot = ""
    if footer is not None or page_no is not None:
        foot = (f'<div class="run-foot"><span>{footer or ""}</span><span>masterfunctionalskills.co.uk</span>'
                f'<span class="pg">{page_no if page_no is not None else ""}</span></div>')
    return f'<section class="page {extra_class}">{head}<div class="body">{body_html}</div>{foot}</section>'


def page_title(title: str, kicker: str | None = None, badge=None, lead: str | None = None) -> str:
    """Big page heading (28pt) with optional unit badge and kicker line."""
    if badge is not None and str(badge).strip():
        badge_str = str(badge).strip()
        raw_text = re.sub(r"<[^>]+>", "", badge_str)
        char_len = len(raw_text)
        if char_len <= 2:
            badge_style = "font-size:22pt; min-width:20mm;"
        elif char_len <= 4:
            badge_style = "font-size:13pt; min-width:22mm; padding:0 3mm;"
        else:
            badge_style = "font-size:11pt; min-width:26mm; padding:0 4mm;"
        b = f'<div class="badge" style="{badge_style}">{badge}</div>'
    else:
        b = ""
    k = f'<div class="kicker">{kicker}</div>' if kicker else ""
    ld = f'<p class="lead">{lead}</p>' if lead else ""
    return f'<div class="ptitle">{b}<div>{k}<h1>{title}</h1>{ld}</div></div>'


def section(label: str, title: str) -> str:
    """Section heading with a round letter tag (A/B/C)."""
    return f'<div class="sec"><span class="tag">{label}</span>{title}</div>'


def h2(text: str) -> str:
    return f"<h2>{text}</h2>"


def para(html: str, cls: str = "") -> str:
    return f'<p class="{cls}">{html}</p>'


def bullets(items, ordered=False) -> str:
    tag = "ol" if ordered else "ul"
    return f"<{tag}>" + "".join(f"<li>{i}</li>" for i in items) + f"</{tag}>"


# ---------------------------------------------------------------------------
# Images
# ---------------------------------------------------------------------------
_CAMERA_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6">'
               '<rect x="2" y="6" width="20" height="14" rx="2"/><circle cx="12" cy="13" r="4"/>'
               '<path d="M8 6l1.5-2.5h5L16 6"/></svg>')


def _img_or_placeholder(path, label: str = "") -> str:
    label = re.sub(r"<[^>]+>", "", label or "").strip()
    label = _html.unescape(label)
    if _exists(path):
        return f'<img src="{_uri(path)}" alt="{E(label)}">'
    return f'<div class="ph">{_CAMERA_SVG}<div>{E(label) or "Photo"}</div><small>photo coming soon</small></div>'


def hero_image(path, caption: str = "", height_mm: float | None = 80, fill: bool = False) -> str:
    """Full-width photo (object-fit:cover, rounded).  fill=True -> grows to fill the page
    (height_mm then acts as the minimum height)."""
    cls = "hero fill" if fill else "hero"
    h = height_mm or 70
    style = f"min-height:{h}mm;" if fill else f"height:{h}mm;"
    cap = f'<div class="cap">{caption}</div>' if caption else ""
    return f'<div class="{cls}" style="{style}"><div class="imgwrap">{_img_or_placeholder(path, "" if caption else "Photo")}</div>{cap}</div>'


def photo_grid(items, cols: int = 3, fill: bool = True, min_tile_mm: float = 55) -> str:
    """Visual-dictionary tiles.  items = [(photo_path, word, example_sentence), ...].
    fill=True -> the grid stretches to the footer with equal-height rows."""
    tiles = []
    for it in items:
        path, word, ex = (list(it) + ["", ""])[:3]
        tiles.append(f'<div class="tile"><div class="imgwrap">{_img_or_placeholder(path, word)}</div>'
                     f'<div class="word">{word}</div><div class="ex">{ex}</div></div>')
    rows = math.ceil(len(items) / cols)
    style = f"grid-template-columns:repeat({cols},1fr);"
    if fill:
        style += f"min-height:{rows * min_tile_mm}mm;"
    else:
        style += f"grid-auto-rows:{min_tile_mm}mm;"
    return f'<div class="pgrid{" fill" if fill else ""}" style="{style}">{"".join(tiles)}</div>'


def silhouette_svg(colour: str = "#7c3aed", height_mm: float = 55) -> str:
    """Friendly inline-SVG character used when no cartoon image is available."""
    return (f'<svg viewBox="0 0 100 150" style="height:{height_mm}mm;width:auto">'
            f'<ellipse cx="50" cy="146" rx="34" ry="4" fill="#00000018"/>'
            f'<path d="M14 146 C14 104 28 88 50 88 C72 88 86 104 86 146 Z" fill="{colour}"/>'
            f'<rect x="43" y="74" width="14" height="18" rx="6" fill="#f2c9a0"/>'
            f'<circle cx="50" cy="50" r="30" fill="#f6d2ae"/>'
            f'<path d="M20 48 C20 20 80 18 80 46 C72 36 58 30 44 34 C34 37 26 42 20 48Z" fill="#3f2a1d"/>'
            f'<circle cx="39" cy="54" r="3.6" fill="#1e293b"/><circle cx="61" cy="54" r="3.6" fill="#1e293b"/>'
            f'<path d="M38 66 Q50 76 62 66" stroke="#1e293b" stroke-width="3" fill="none" stroke-linecap="round"/>'
            f'<circle cx="31" cy="63" r="4" fill="#f4a3a3" opacity=".6"/><circle cx="69" cy="63" r="4" fill="#f4a3a3" opacity=".6"/>'
            f'</svg>')


def character_bubble(cartoon_path, name: str, text: str, side: str = "left",
                     height_mm: float = 48, colour: str | None = None) -> str:
    """Cartoon character (45–70 mm tall) with a speech bubble beside it.
    side='left' -> character on the left; 'right' -> character on the right.
    Works with any image path; falls back to an inline SVG character."""
    if _exists(cartoon_path):
        fig = f'<img src="{_uri(cartoon_path)}" alt="{E(name)}">'
    else:
        fig = silhouette_svg(colour or "var(--accent)", height_mm)
    cls = "charrow right" if side == "right" else "charrow"
    nm = f'<div class="nm">{name}</div>' if name else ""
    return (f'<div class="{cls}" style="--ch:{height_mm}mm"><div class="who">{fig}{nm}</div>'
            f'<div class="bubble">{text}</div></div>')


# ---------------------------------------------------------------------------
# Teaching boxes
# ---------------------------------------------------------------------------
def _box(kind: str, title: str, body: str, icon: str, extra_cls="") -> str:
    bt = f'<div class="bt"><span class="ico">{icon}</span>{title}</div>' if title else ""
    return f'<div class="box {kind} {extra_cls}">{bt}<div>{body}</div></div>'


def rule_box(title: str, body_html: str, fill: bool = False) -> str:
    return _box("rule", title, body_html, "&#9733;", "fill" if fill else "")


def golden_rule(text: str, title: str = "Golden Rule") -> str:
    return _box("golden", title, text, "&#10003;")


def watch_out(text: str, title: str = "Watch Out!") -> str:
    return _box("watch", title, text, "!")


def tip_pair(golden: str, watch: str, golden_title="Golden Rule", watch_title="Watch Out!") -> str:
    """Golden Rule + Watch Out side by side."""
    return f'<div class="pair">{golden_rule(golden, golden_title)}{watch_out(watch, watch_title)}</div>'


def box_html(body_html: str, title: str = "", fill: bool = False) -> str:
    """Plain white task/info box (e.g. an exam task or a text extract)."""
    return _box("worked", title, body_html, "&#9654;", "fill" if fill else "")


def checklist_box(title: str, items: list[str]) -> str:
    """Box containing a formatted checklist for candidate task requirements."""
    items_html = "".join(f"<li style='margin-bottom:4px;'>{item}</li>" for item in items)
    return box_html(f"<ul style='margin:0; padding-left:20px; font-size:10pt; line-height:1.4;'>{items_html}</ul>", title=title)


def worked_example(question: str, steps, answer: str | None = None, title: str = "Worked Example") -> str:
    st = "".join(f"<li>{s}</li>" for s in steps)
    ans = f'<div class="ans">{answer}</div>' if answer else ""
    return _box("worked", title, f'<div class="q">{question}</div><ol class="steps">{st}</ol>{ans}', "&#9998;")


def compare(bad: str, good: str, bad_label="&#10007; Wrong", good_label="&#10003; Right", stacked: bool = False) -> str:
    """Wrong vs right side-by-side (red / green).  stacked=True puts them one above the other."""
    st = ' style="grid-template-columns:1fr"' if stacked else ""
    return (f'<div class="compare"{st}><div class="bad"><div class="lab">{bad_label}</div>{bad}</div>'
            f'<div class="good"><div class="lab">{good_label}</div>{good}</div></div>')


# ---------------------------------------------------------------------------
# Exercises & fill blocks
# ---------------------------------------------------------------------------
def answer_lines(n: int = 2) -> str:
    return "".join('<div class="aline"></div>' for _ in range(n))


def exercise_list(items, lines: int = 2, start: int = 1, options_key: str = "options") -> str:
    """Numbered exercise list.
    items: str  |  (question, n_lines)  |  {"q":..., "options":[...], "lines":n, "marks":m}
    Multiple-choice options get tick boxes; otherwise ruled answer lines follow each question."""
    out = []
    for it in items:
        n = lines
        opts = None
        marks = ""
        if isinstance(it, dict):
            q = it.get("q", "")
            n = it.get("lines", 0 if it.get(options_key) else lines)
            opts = it.get(options_key)
            if it.get("marks"):
                marks = f'<span class="marks">({it["marks"]} mark{"s" if it["marks"] != 1 else ""})</span>'
        elif isinstance(it, (tuple, list)):
            q, n = it[0], it[1]
        else:
            q = it
        o = ""
        if opts:
            short = max(len(re.sub(r"<[^>]+>", "", x)) for x in opts) <= 28
            o = f'<ul class="opts{" inline" if short else ""}">' + "".join(f'<li><span class="ck"></span><span>{x}</span></li>' for x in opts) + "</ul>"
        out.append(f"<li>{marks}{q}{o}{answer_lines(n)}</li>")
    return f'<ol class="exlist" style="--start:{start - 1}">{"".join(out)}</ol>'


def working_box(label: str = "Working", height_mm: float | None = 35, fill: bool = False,
                grid: bool = True, answer_label: str | None = "Answer:") -> str:
    """Bordered working-out box (5 mm grid inside by default) with an answer blank."""
    cls = "wbox fill" if fill else "wbox"
    style = f"--h:{height_mm or 30}mm;" + ("" if fill else f"height:{height_mm}mm;")
    ans = (f'<div class="wans">{answer_label} <span class="blank"></span></div>' if answer_label else "")
    return (f'<div class="{cls}" style="{style}"><div class="wl">{label}</div>'
            f'<div class="wa{" grid" if grid else ""}"></div>{ans}</div>')


def practice_stack(questions, start: int = 1, grid: bool = True, fill: bool = True) -> str:
    """Practice page core: each question gets its own working box; the boxes share the remaining
    page height equally (so the last one always reaches the footer).
    questions: [str | (text, weight) | {"q":..., "weight":1.5, "marks":2, "answer":"Answer:"}]"""
    items = []
    for i, q in enumerate(questions):
        w, marks, al = 1, None, "Answer:"
        if isinstance(q, dict):
            text, w, marks, al = q.get("q"), q.get("weight", 1), q.get("marks"), q.get("answer", "Answer:")
        elif isinstance(q, (tuple, list)):
            text, w = q[0], q[1]
        else:
            text = q
        mk = f'<span class="marks">({marks} mark{"s" if marks != 1 else ""})</span>' if marks else ""
        items.append(f'<div class="qitem" style="flex-grow:{w}"><div class="qtext"><span class="qn">{start + i}</span>'
                     f'<div class="qbody">{mk}{text}</div></div>{working_box("Show your working", 22, grid=grid, answer_label=al, fill=True)}</div>')
    return f'<div class="qstack{" fill" if fill else ""}">{"".join(items)}</div>'


def fill_lines(label: str = "", gap_mm: float = 11, min_mm: float = 30) -> str:
    """Ruled writing lines that stretch to the footer."""
    head = ""
    if label:
        ico = "" if label.startswith(("<span", "&#")) else "&#9998; "
        head = f'<div class="fl-head">{ico}{label}</div>'
    return f'<div class="flines fill" style="min-height:{min_mm}mm">{head}<div class="fl-lines" style="--gap:{gap_mm}mm;"></div></div>'


def fill_grid(label: str = "", min_mm: float = 30) -> str:
    """5 mm maths grid (bold every 25 mm) that stretches to the footer."""
    head = ""
    if label:
        ico = "" if label.startswith(("<span", "&#")) else "&#9998; "
        head = f'<div class="fg-head">{ico}{label}</div>'
    return f'<div class="fgrid fill" style="min-height:{min_mm}mm">{head}<div class="fg-grid"></div></div>'


def fill_notes(title: str = "My Notes", min_mm: float = 30) -> str:
    """Dashed 'Notes' panel with faint lines that stretches to the footer."""
    return f'<div class="fnotes fill" style="min-height:{min_mm}mm"><div class="nt">&#9998; {title}</div><div class="nl"></div></div>'


# ---------------------------------------------------------------------------
# Reference back matter (answers, mark schemes, glossary, index)
# ---------------------------------------------------------------------------
def ref_qa(num, answer_html: str, marks=None, working: str | None = None) -> str:
    """One answer line:  '3  £42.50 [2]'  with optional italic working line underneath."""
    mk = f' <span class="mk">[{marks}]</span>' if marks not in (None, "") else ""
    wk = f'<span class="wk">{working}</span>' if working else ""
    return f'<div class="qa"><b class="qn">{num}</b>{answer_html}{mk}{wk}</div>'


def ref_block(heading: str, inner_html: str) -> str:
    return f'<div class="ref-blk"><h3>{heading}</h3>{inner_html}</div>' if heading else f'<div class="ref-blk">{inner_html}</div>'


def _measure_blocks(blocks, col_width_mm: float, theme="maths") -> list[float]:
    """Return rendered height (mm) of each block at the given column width."""
    items = "".join(f'<div class="mb" data-i="{i}">{b}</div>' for i, b in enumerate(blocks))
    js = """<script>window.addEventListener('load',function(){var o=[];
document.querySelectorAll('.mb').forEach(function(e){var b=e.firstElementChild||e;
var cs=getComputedStyle(b);o.push((e.getBoundingClientRect().height+parseFloat(cs.marginBottom||0))/3.7795);});
var d=document.createElement('pre');d.id='mout';d.textContent=JSON.stringify(o);document.body.appendChild(d);});</script>"""
    html_s = (f'<!DOCTYPE html><html><head><meta charset="utf-8">{get_css(theme)}</head><body>'
              f'<div class="ref-body" style="column-count:1;width:{col_width_mm}mm;flex:none;">{items}</div>{js}</body></html>')
    tmp = Path(tempfile.mkdtemp(prefix="refm_")) / "m.html"
    tmp.write_text(html_s, encoding="utf-8")
    r = _chromium(["--virtual-time-budget=5000", "--dump-dom", tmp.as_uri()])
    m = re.search(r'<pre id="mout">(.*?)</pre>', r.stdout, re.S)
    shutil.rmtree(tmp.parent, ignore_errors=True)
    if not m:
        raise RuntimeError("block measurement failed")
    return json.loads(_html.unescape(m.group(1)))


def ref_pages(title: str, blocks, book: str, start_page: int, header_right: str = "",
              cols: int = 2, subtitle: str = "", theme="maths", notes_title: str = "Notes") -> list[str]:
    """Paginate reference blocks (from ref_block) into black, condensed, ruled-column pages.
    Each block stays whole.  The last page balances its columns and ends with a ruled Notes area."""
    blocks = list(blocks)
    if not blocks:
        return []
    usable_w = 182.0
    col_w = (usable_w - 6.0 * (cols - 1)) / cols
    heights = _measure_blocks(blocks, col_w, theme)
    title_mm = 13.5 if subtitle else 10.5
    cap = (253.0 - title_mm - 2.0) * 0.985           # per column, safety margin
    pages_cols: list[list[list[int]]] = []
    cur, col = [[]], 0
    used = 0.0
    for i, hgt in enumerate(heights):
        if used + hgt > cap and cur[col]:
            col += 1
            used = 0.0
            if col == cols:
                pages_cols.append(cur)
                cur, col = [[]], 0
            else:
                cur.append([])
        cur[col].append(i)
        used += hgt
    pages_cols.append(cur)

    out = []
    sub = f"<small>{subtitle}</small>" if subtitle else ""
    for pi, pcols in enumerate(pages_cols):
        last = pi == len(pages_cols) - 1
        cont = "" if pi == 0 else " (continued)"
        head = f'<div class="ref-title">{title}{cont}{sub if pi == 0 else ""}</div>'
        if not last:
            # explicit column breaks so each column holds exactly the packed blocks
            inner = '<div style="break-after:column;height:0"></div>'.join(
                "".join(blocks[i] for i in c) for c in pcols)
            body = head + f'<div class="ref-body" style="--cols:{cols}">{inner}</div>'
        else:
            idx = [i for c in pcols for i in c]
            tot = sum(heights[i] for i in idx)
            need = max(tot / cols * 1.10 + 4, max(heights[i] for i in idx) + 3)
            inner = "".join(blocks[i] for i in idx)
            full_h = cap / 0.985
            if need + 22 <= full_h:
                body = (head + f'<div class="ref-body" style="--cols:{cols};flex:0 0 auto;column-fill:balance;'
                        f'height:{need:.1f}mm">{inner}</div>'
                        f'<div class="ref-notes fill"><div class="nt">{notes_title}</div><div class="nl"></div></div>')
            else:  # page is (nearly) full: keep greedy packing, no notes
                inner = '<div style="break-after:column;height:0"></div>'.join(
                    "".join(blocks[i] for i in c) for c in pcols)
                body = head + f'<div class="ref-body" style="--cols:{cols}">{inner}</div>'
        out.append(page(body, header=(book, header_right or title), footer=book,
                        page_no=start_page + pi, extra_class="ref"))
    return out


def two_col(left: str, right: str, ratio=(1, 1), fill: bool = False, gap_mm: float = 5) -> str:
    """Two columns.  Put a fill block last in a column to stretch that column."""
    cls = "cols fill" if fill else "cols"
    return (f'<div class="{cls}" style="grid-template-columns:{ratio[0]}fr {ratio[1]}fr;gap:{gap_mm}mm">'
            f'<div>{left}</div><div>{right}</div></div>')


def table(headers, rows, col_widths=None) -> str:
    cg = ""
    if col_widths:
        cg = "<colgroup>" + "".join(f'<col style="width:{w}">' for w in col_widths) + "</colgroup>"
    th = "".join(f"<th>{h}</th>" for h in headers)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="t">{cg}<thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'


def diagram(svg: str, caption: str = "", fill: bool = False) -> str:
    """Wrap an SVG in a white rounded panel with caption."""
    cap = f'<div class="cap">{caption}</div>' if caption else ""
    style = "justify-content:center;" if fill else ""
    return f'<div class="diag{" fill" if fill else ""}" style="{style}">{svg}{cap}</div>'


def answer_columns(blocks, fill: bool = False) -> str:
    """Answer page: blocks = [(heading, html), ...] in two 12.5pt columns.
    Columns balance; follow with fill_notes("Corrections") unless fill=True."""
    return f'<div class="anscols{" fill" if fill else ""}">' + "".join(f'<div class="ak"><h3>{h}</h3>{b}</div>' for h, b in blocks) + "</div>"


# ---------------------------------------------------------------------------
# SVG diagram helpers  (viewBox in millimetres -> font-size 5 = 14pt, 4.3 = 12pt)
# ---------------------------------------------------------------------------
_SVGF = "font-family:Lexend,Arial,sans-serif"


def _svg(w, h, inner) -> str:
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'style="width:{w}mm;height:{h}mm;{_SVGF}">{inner}</svg>')


def _fmt(v) -> str:
    return f"{v:g}" if isinstance(v, (int, float)) else str(v)


def number_line(start, end, step=1, marks=None, width_mm=170, height_mm=34, label_every=1,
                colour="#0284c7", jumps=None) -> str:
    """Number line.  marks = {value: "label"} shown as coloured dots with labels above.
    jumps = [(from, to, "label")] drawn as arcs."""
    marks = marks or {}
    pad = 8
    y = height_mm * 0.62
    n = int(round((end - start) / step))
    xw = width_mm - 2 * pad
    X = lambda v: pad + (v - start) / (end - start) * xw
    s = [f'<line x1="{pad - 4}" y1="{y}" x2="{width_mm - pad + 4}" y2="{y}" stroke="#1e293b" stroke-width="0.8"/>',
         f'<path d="M{width_mm - pad + 5} {y} l-3 -1.8 v3.6z" fill="#1e293b"/>',
         f'<path d="M{pad - 5} {y} l3 -1.8 v3.6z" fill="#1e293b"/>']
    for i in range(n + 1):
        v = start + i * step
        x = X(v)
        major = i % label_every == 0
        s.append(f'<line x1="{x:.2f}" y1="{y - (3 if major else 1.8)}" x2="{x:.2f}" y2="{y + (3 if major else 1.8)}" stroke="#1e293b" stroke-width="0.6"/>')
        if major:
            s.append(f'<text x="{x:.2f}" y="{y + 9}" font-size="4.6" text-anchor="middle" fill="#1e293b">{_fmt(round(v, 6))}</text>')
    for a, b, lab in (jumps or []):
        xa, xb = X(a), X(b)
        mid = (xa + xb) / 2
        s.append(f'<path d="M{xa:.2f} {y - 1} Q{mid:.2f} {y - 16} {xb:.2f} {y - 1}" fill="none" stroke="{colour}" stroke-width="0.8"/>')
        s.append(f'<text x="{mid:.2f}" y="{y - 10}" font-size="4.4" text-anchor="middle" fill="{colour}" font-weight="700">{lab}</text>')
    for v, lab in marks.items():
        x = X(v)
        s.append(f'<circle cx="{x:.2f}" cy="{y}" r="2" fill="{colour}"/>')
        if lab:
            s.append(f'<text x="{x:.2f}" y="{y - 5}" font-size="4.6" text-anchor="middle" fill="{colour}" font-weight="700">{lab}</text>')
    return _svg(width_mm, height_mm, "".join(s))


def bar_chart(data, title="", ylabel="", width_mm=170, height_mm=95, ymax=None, ystep=None,
              colour="#0284c7", value_labels=True) -> str:
    """Vertical bar chart.  data = [(label, value), ...]."""
    left, right, top, bottom = 22, 6, 12 if title else 6, 16
    pw, ph = width_mm - left - right, height_mm - top - bottom
    vmax = ymax or max(v for _, v in data) * 1.15
    if not ystep:
        raw = vmax / 5
        mag = 10 ** math.floor(math.log10(raw))
        ystep = min((m * mag for m in (1, 2, 2.5, 5, 10) if m * mag >= raw), default=raw)
        vmax = math.ceil(vmax / ystep) * ystep
    s = []
    if title:
        s.append(f'<text x="{width_mm / 2}" y="7" font-size="5.2" font-weight="700" text-anchor="middle" fill="#1e293b">{title}</text>')
    v = 0
    while v <= vmax + 1e-9:
        yy = top + ph - v / vmax * ph
        s.append(f'<line x1="{left}" y1="{yy:.2f}" x2="{left + pw}" y2="{yy:.2f}" stroke="#cbd5e1" stroke-width="0.35"/>')
        s.append(f'<text x="{left - 2}" y="{yy + 1.6:.2f}" font-size="4.3" text-anchor="end" fill="#334155">{_fmt(round(v, 6))}</text>')
        v += ystep
    s.append(f'<line x1="{left}" y1="{top}" x2="{left}" y2="{top + ph}" stroke="#1e293b" stroke-width="0.7"/>')
    s.append(f'<line x1="{left}" y1="{top + ph}" x2="{left + pw}" y2="{top + ph}" stroke="#1e293b" stroke-width="0.7"/>')
    if ylabel:
        s.append(f'<text transform="translate(5 {top + ph / 2}) rotate(-90)" font-size="4.3" text-anchor="middle" fill="#334155">{ylabel}</text>')
    n = len(data)
    slot = pw / n
    bw = slot * 0.62
    for i, (lab, val) in enumerate(data):
        x = left + i * slot + (slot - bw) / 2
        h = val / vmax * ph
        c = colour[i % len(colour)] if isinstance(colour, (list, tuple)) else colour
        s.append(f'<rect x="{x:.2f}" y="{top + ph - h:.2f}" width="{bw:.2f}" height="{h:.2f}" rx="1" fill="{c}"/>')
        s.append(f'<text x="{x + bw / 2:.2f}" y="{top + ph + 6.5}" font-size="4.4" text-anchor="middle" fill="#1e293b">{lab}</text>')
        if value_labels:
            s.append(f'<text x="{x + bw / 2:.2f}" y="{top + ph - h - 1.8:.2f}" font-size="4.3" font-weight="700" text-anchor="middle" fill="#1e293b">{_fmt(val)}</text>')
    return _svg(width_mm, height_mm, "".join(s))


_PIE_COLS = ["#0284c7", "#f59e0b", "#10b981", "#ef4444", "#8b5cf6", "#ec4899", "#14b8a6", "#64748b"]


def pie_chart(data, title="", width_mm=170, height_mm=90, show_percent=True, colours=None) -> str:
    """Pie chart with legend.  data = [(label, value), ...]."""
    cols = colours or _PIE_COLS
    total = sum(v for _, v in data)
    r = min(height_mm - (16 if title else 8), width_mm * 0.5) / 2
    legend_w = 12 + max(len(f"{lab} ({_fmt(v)})") for lab, v in data) * 2.7
    r = max(12, min(r, (width_mm - legend_w - 8) / 2))
    cx, cy = r + 6, (12 if title else 4) + r
    s = []
    if title:
        s.append(f'<text x="{width_mm / 2}" y="7" font-size="5.2" font-weight="700" text-anchor="middle" fill="#1e293b">{title}</text>')
    a0 = -math.pi / 2
    for i, (lab, v) in enumerate(data):
        a1 = a0 + v / total * 2 * math.pi
        large = 1 if a1 - a0 > math.pi else 0
        x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        c = cols[i % len(cols)]
        if len(data) == 1:
            s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}"/>')
        else:
            s.append(f'<path d="M{cx},{cy} L{x0:.2f},{y0:.2f} A{r},{r} 0 {large} 1 {x1:.2f},{y1:.2f} Z" fill="{c}" stroke="#fff" stroke-width="0.8"/>')
        if show_percent and v / total >= 0.06:
            am = (a0 + a1) / 2
            tx, ty = cx + r * 0.62 * math.cos(am), cy + r * 0.62 * math.sin(am)
            s.append(f'<text x="{tx:.2f}" y="{ty + 1.7:.2f}" font-size="4.6" font-weight="700" text-anchor="middle" fill="#fff">{round(v / total * 100)}%</text>')
        a0 = a1
    lx = cx + r + 12
    ly = cy - len(data) * 4.5
    for i, (lab, v) in enumerate(data):
        yy = ly + i * 9
        s.append(f'<rect x="{lx}" y="{yy}" width="6" height="6" rx="1" fill="{cols[i % len(cols)]}"/>')
        s.append(f'<text x="{lx + 9}" y="{yy + 4.8}" font-size="4.6" fill="#1e293b">{lab} ({_fmt(v)})</text>')
    return _svg(width_mm, height_mm, "".join(s))


def shape(kind="rect", dims=None, width_mm=120, height_mm=80, units="m", fill="#e0f2fe", stroke="#0c4a6e") -> str:
    """Labelled shape diagram.
    kind: rect (w,h) | triangle (base,height) | circle (r) | lshape (W,H,w_cut,h_cut) | cuboid (l,w,h)
    dims: dict of numbers, e.g. {"w":8, "h":5}.  Labels drawn at >= 12pt."""
    d = dims or {}
    s = []
    fs = 5
    lab = lambda x, y, t, anchor="middle": (f'<text x="{x:.2f}" y="{y:.2f}" font-size="{fs}" font-weight="700" '
                                            f'text-anchor="{anchor}" fill="{stroke}">{t}</text>')
    m = 14
    W, H = width_mm - 2 * m, height_mm - 2 * m
    if kind == "rect":
        w, h = d.get("w", 8), d.get("h", 5)
        sc = min(W / w, H / h)
        pw, ph = w * sc, h * sc
        x0, y0 = (width_mm - pw) / 2, (height_mm - ph) / 2
        s.append(f'<rect x="{x0:.2f}" y="{y0:.2f}" width="{pw:.2f}" height="{ph:.2f}" fill="{fill}" stroke="{stroke}" stroke-width="0.9"/>')
        s.append(lab(x0 + pw / 2, y0 + ph + 7, f"{_fmt(w)} {units}"))
        s.append(lab(x0 - 3, y0 + ph / 2 + 1.7, f"{_fmt(h)} {units}", "end"))
    elif kind == "triangle":
        b, h = d.get("base", 10), d.get("height", 6)
        sc = min(W / b, H / h)
        pb, ph = b * sc, h * sc
        x0, y0 = (width_mm - pb) / 2, (height_mm + ph) / 2
        apex = x0 + pb * d.get("apex", 0.35)
        s.append(f'<path d="M{x0:.2f},{y0:.2f} L{x0 + pb:.2f},{y0:.2f} L{apex:.2f},{y0 - ph:.2f} Z" fill="{fill}" stroke="{stroke}" stroke-width="0.9"/>')
        s.append(f'<line x1="{apex:.2f}" y1="{y0 - ph:.2f}" x2="{apex:.2f}" y2="{y0:.2f}" stroke="{stroke}" stroke-width="0.6" stroke-dasharray="2 1.5"/>')
        s.append(f'<rect x="{apex:.2f}" y="{y0 - 3:.2f}" width="3" height="3" fill="none" stroke="{stroke}" stroke-width="0.5"/>')
        s.append(lab(x0 + pb / 2, y0 + 7, f"base {_fmt(b)} {units}"))
        s.append(lab(apex + 3, y0 - ph / 2, f"height {_fmt(h)} {units}", "start"))
    elif kind == "circle":
        r = d.get("r", 4)
        pr = min(W, H) / 2
        cx, cy = width_mm / 2, height_mm / 2
        s.append(f'<circle cx="{cx}" cy="{cy}" r="{pr:.2f}" fill="{fill}" stroke="{stroke}" stroke-width="0.9"/>')
        s.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + pr:.2f}" y2="{cy}" stroke="{stroke}" stroke-width="0.8"/>')
        s.append(f'<circle cx="{cx}" cy="{cy}" r="1" fill="{stroke}"/>')
        s.append(lab(cx + pr / 2, cy - 2.5, f"r = {_fmt(r)} {units}"))
    elif kind == "lshape":
        Wt, Ht, wc, hc = d.get("W", 10), d.get("H", 8), d.get("w_cut", 4), d.get("h_cut", 3)
        sc = min(W / Wt, H / Ht)
        pw, ph, cw, chh = Wt * sc, Ht * sc, wc * sc, hc * sc
        x0, y0 = (width_mm - pw) / 2, (height_mm - ph) / 2
        pts = [(x0, y0), (x0 + pw - cw, y0), (x0 + pw - cw, y0 + chh), (x0 + pw, y0 + chh), (x0 + pw, y0 + ph), (x0, y0 + ph)]
        s.append('<path d="M' + " L".join(f"{x:.2f},{y:.2f}" for x, y in pts) + f' Z" fill="{fill}" stroke="{stroke}" stroke-width="0.9"/>')
        s.append(f'<line x1="{x0 + pw - cw:.2f}" y1="{y0 + chh:.2f}" x2="{x0 + pw - cw:.2f}" y2="{y0 + ph:.2f}" stroke="{stroke}" stroke-width="0.5" stroke-dasharray="2 1.5"/>')
        s.append(lab(x0 + pw / 2, y0 + ph + 7, f"{_fmt(Wt)} {units}"))
        s.append(lab(x0 - 3, y0 + ph / 2 + 1.7, f"{_fmt(Ht)} {units}", "end"))
        s.append(lab(x0 + (pw - cw) / 2, y0 - 3, f"{_fmt(Wt - wc)} {units}"))
        s.append(lab(x0 + pw + 3, y0 + chh + (ph - chh) / 2 + 1.7, f"{_fmt(Ht - hc)} {units}", "start"))
        s.append(f'<text x="{x0 + (pw - cw) / 2:.2f}" y="{y0 + ph * 0.6:.2f}" font-size="6" font-weight="800" text-anchor="middle" fill="{stroke}" opacity=".55">A</text>')
        s.append(f'<text x="{x0 + pw - cw / 2:.2f}" y="{y0 + chh + (ph - chh) * 0.6:.2f}" font-size="6" font-weight="800" text-anchor="middle" fill="{stroke}" opacity=".55">B</text>')
    elif kind == "cuboid":
        l, w, h = d.get("l", 6), d.get("w", 3), d.get("h", 4)
        dx, dy = 0.5, -0.35
        sc = min(W / (l + w * dx), H / (h - w * dy))
        pl, pw_, ph = l * sc, w * sc, h * sc
        ox, oy = (width_mm - (pl + pw_ * dx)) / 2, (height_mm + (ph - pw_ * dy)) / 2
        F = lambda a, b, c: (ox + a * sc + b * sc * dx, oy - c * sc + b * sc * dy)
        def poly(pts, f):
            return '<path d="M' + " L".join(f"{x:.2f},{y:.2f}" for x, y in pts) + f' Z" fill="{f}" stroke="{stroke}" stroke-width="0.8"/>'
        s.append(poly([F(0, 0, 0), F(l, 0, 0), F(l, 0, h), F(0, 0, h)], fill))
        s.append(poly([F(0, 0, h), F(l, 0, h), F(l, w, h), F(0, w, h)], "#bae6fd"))
        s.append(poly([F(l, 0, 0), F(l, w, 0), F(l, w, h), F(l, 0, h)], "#7dd3fc"))
        a, b = F(0, 0, 0), F(l, 0, 0)
        s.append(lab((a[0] + b[0]) / 2, a[1] + 7, f"{_fmt(l)} {units}"))
        c = F(l, w / 2, 0)
        s.append(lab(c[0] + 3, c[1] + 4, f"{_fmt(w)} {units}", "start"))
        e = F(0, 0, h / 2)
        s.append(lab(e[0] - 3, e[1] + 1.7, f"{_fmt(h)} {units}", "end"))
    return _svg(width_mm, height_mm, "".join(s))


def clock_face(hour=3, minute=0, size_mm=70, colour="#0c4a6e") -> str:
    """Analogue clock showing hour:minute."""
    r = size_mm / 2 - 2
    c = size_mm / 2
    s = [f'<circle cx="{c}" cy="{c}" r="{r}" fill="#fff" stroke="{colour}" stroke-width="1.6"/>']
    for i in range(60):
        a = math.radians(i * 6 - 90)
        r1 = r - (4 if i % 5 == 0 else 2)
        s.append(f'<line x1="{c + r1 * math.cos(a):.2f}" y1="{c + r1 * math.sin(a):.2f}" x2="{c + (r - 0.8) * math.cos(a):.2f}" '
                 f'y2="{c + (r - 0.8) * math.sin(a):.2f}" stroke="#1e293b" stroke-width="{0.7 if i % 5 == 0 else 0.3}"/>')
    for n in range(1, 13):
        a = math.radians(n * 30 - 90)
        rr = r - 10
        s.append(f'<text x="{c + rr * math.cos(a):.2f}" y="{c + rr * math.sin(a) + 2:.2f}" font-size="5.6" font-weight="700" text-anchor="middle" fill="#1e293b">{n}</text>')
    ha = math.radians((hour % 12 + minute / 60) * 30 - 90)
    ma = math.radians(minute * 6 - 90)
    s.append(f'<line x1="{c}" y1="{c}" x2="{c + r * 0.5 * math.cos(ha):.2f}" y2="{c + r * 0.5 * math.sin(ha):.2f}" stroke="{colour}" stroke-width="2.4" stroke-linecap="round"/>')
    s.append(f'<line x1="{c}" y1="{c}" x2="{c + r * 0.78 * math.cos(ma):.2f}" y2="{c + r * 0.78 * math.sin(ma):.2f}" stroke="#ef4444" stroke-width="1.4" stroke-linecap="round"/>')
    s.append(f'<circle cx="{c}" cy="{c}" r="1.8" fill="{colour}"/>')
    return _svg(size_mm, size_mm, "".join(s))


def thermometer(value=18, vmin=-10, vmax=40, step=5, height_mm=110, width_mm=46, unit="°C", colour="#ef4444") -> str:
    """Vertical thermometer scale with a reading."""
    tx = 14
    top, bulb = 8, height_mm - 10
    bottom = bulb - 7
    Y = lambda v: bottom - (v - vmin) / (vmax - vmin) * (bottom - top)
    s = [f'<rect x="{tx - 3.5}" y="{top - 3}" width="7" height="{bottom - top + 6}" rx="3.5" fill="#fff" stroke="#1e293b" stroke-width="0.7"/>',
         f'<circle cx="{tx}" cy="{bulb}" r="7" fill="{colour}" stroke="#1e293b" stroke-width="0.7"/>',
         f'<rect x="{tx - 2}" y="{Y(value):.2f}" width="4" height="{bulb - Y(value):.2f}" fill="{colour}"/>']
    v = vmin
    while v <= vmax + 1e-9:
        y = Y(v)
        s.append(f'<line x1="{tx + 3.5}" y1="{y:.2f}" x2="{tx + 8}" y2="{y:.2f}" stroke="#1e293b" stroke-width="0.5"/>')
        s.append(f'<text x="{tx + 10}" y="{y + 1.6:.2f}" font-size="4.4" fill="#1e293b">{_fmt(v)}{unit}</text>')
        v += step
    return _svg(width_mm, height_mm, "".join(s))


def letter_layout(kind="letter", width_mm=120, height_mm=150, labels=True, colour="#831843") -> str:
    """Skeleton of a formal letter or email with labelled parts (for writing pages)."""
    s = [f'<rect x="1" y="1" width="{width_mm - 2}" height="{height_mm - 2}" rx="3" fill="#fff" stroke="#94a3b8" stroke-width="0.6"/>']
    bar = lambda x, y, w, h=2.6, c="#cbd5e1": f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="1.2" fill="{c}"/>'
    L = lambda x, y, t, a="start": (f'<text x="{x}" y="{y}" font-size="4.4" font-weight="700" fill="{colour}" text-anchor="{a}">{t}</text>' if labels else "")
    W = width_mm
    if kind == "email":
        s.append(f'<rect x="1" y="1" width="{W - 2}" height="12" rx="3" fill="{colour}"/>')
        s.append(f'<text x="7" y="9" font-size="4.6" fill="#fff" font-weight="700">New message</text>')
        rows = [("To:", 20), ("Cc:", 31), ("Subject:", 42)]
        for t, y in rows:
            s.append(f'<text x="7" y="{y}" font-size="4.4" fill="#334155">{t}</text>')
            s.append(f'<line x1="26" y1="{y + 1.5}" x2="{W - 6}" y2="{y + 1.5}" stroke="#cbd5e1" stroke-width="0.5"/>')
        y = 56
        s.append(bar(7, y, 30, c="#94a3b8")); s.append(L(W - 6, y + 2.5, "Greeting", "end"))
        for i in range(5):
            s.append(bar(7, y + 10 + i * 6, W - 16 - (i == 4) * 30))
        s.append(L(W - 6, y + 22, "Opening paragraph", "end"))
        for i in range(5):
            s.append(bar(7, y + 46 + i * 6, W - 16 - (i == 4) * 20))
        s.append(L(W - 6, y + 58, "Main points", "end"))
        s.append(bar(7, height_mm - 26, 34, c="#94a3b8")); s.append(bar(7, height_mm - 18, 24, c="#94a3b8"))
        s.append(L(W - 6, height_mm - 20, "Sign-off", "end"))
    else:
        s.append(bar(W - 46, 8, 40)); s.append(bar(W - 46, 13, 34)); s.append(bar(W - 46, 18, 28))
        s.append(L(W - 48, 15, "Your address", "end"))
        s.append(bar(W - 46, 26, 24, c="#94a3b8")); s.append(L(W - 48, 28.5, "Date", "end"))
        s.append(bar(7, 36, 36)); s.append(bar(7, 41, 30)); s.append(bar(7, 46, 26))
        s.append(L(46, 43, "Their address"))
        s.append(bar(7, 56, 34, c="#94a3b8")); s.append(L(46, 58.5, "Dear Mr / Ms ..."))
        s.append(bar(7, 64, 50, c="#64748b")); s.append(L(60, 66.5, "Subject line"))
        y = 74
        for blk, lab in ((4, "Opening"), (5, "Main point 1"), (5, "Main point 2"), (3, "Closing")):
            for i in range(blk):
                s.append(bar(7, y + i * 5, W - 14 - (i == blk - 1) * 30))
            s.append(L(W - 8, y + (blk - 1) * 5 + 2.5, lab, "end"))
            y += blk * 5 + 4
        s.append(bar(7, y + 2, 30, c="#94a3b8")); s.append(bar(7, y + 9, 26, c="#94a3b8"))
        s.append(L(42, y + 6, "Yours sincerely / faithfully"))
    return _svg(width_mm, height_mm, "".join(s))


# ---------------------------------------------------------------------------
# Image libraries (photos / cartoons) — manifest-aware lookup
# ---------------------------------------------------------------------------
def _load_manifest(folder: Path):
    mf = folder / "manifest.json"
    entries = []
    if mf.exists():
        try:
            data = json.loads(mf.read_text())
        except Exception:
            data = None
        def walk(obj, ctx=""):
            if isinstance(obj, dict):
                pathlike = next((obj[k] for k in ("path", "file", "filename", "src", "image", "local_path")
                                 if k in obj and isinstance(obj[k], str)), None)
                if pathlike:
                    entries.append((pathlike, json.dumps(obj).lower() + " " + ctx.lower()))
                else:
                    for k, v in obj.items():
                        if isinstance(v, str) and v.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
                            entries.append((v, (k + " " + ctx).lower()))
                        else:
                            walk(v, ctx + " " + str(k))
            elif isinstance(obj, list):
                for v in obj:
                    walk(v, ctx)
        walk(data)
    resolved = []
    for p, text in entries:
        cands = [Path(p), folder / p, SITE_ROOT / p]
        cands += [d / Path(p).name for d in [folder] + [x for x in folder.glob("*") if x.is_dir()]]
        hit = next((c for c in cands if c.is_absolute() and c.exists() or (not c.is_absolute() and (SITE_ROOT / c).exists())), None)
        if hit:
            hit = hit if hit.is_absolute() else SITE_ROOT / hit
            resolved.append((str(hit), text + " " + str(hit).lower()))
    # also any image files not in manifest
    seen = {r[0] for r in resolved}
    if folder.exists():
        for f in folder.rglob("*"):
            if f.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp") and str(f) not in seen:
                resolved.append((str(f), str(f.relative_to(folder)).lower().replace("_", " ").replace("-", " ")))
    return resolved


def find_image(library: str, keywords, theme: str | None = None, exclude=()):
    """Best-matching image path from book_photos ('photo') or book_cartoons ('cartoon').
    keywords: str or list.  Returns None if nothing matches (callers then get a placeholder)."""
    folder = PHOTO_DIR if library.startswith("photo") else CARTOON_DIR
    entries = _load_manifest(folder)
    if isinstance(keywords, str):
        keywords = keywords.split()
    kws = [k.lower() for k in keywords]
    best, best_score = None, 0
    for path, text in entries:
        if path in exclude:
            continue
        score = sum(2 if re.search(r"\b" + re.escape(k) + r"\b", text) else (1 if k in text else 0) for k in kws)
        if theme and f"/{theme}/" in path:
            score += 0.5
        if score > best_score:
            best, best_score = path, score
    return best if best_score >= 1 else None


def photo(keywords, theme=None, exclude=()):
    return find_image("photo", keywords, theme, exclude)


def cartoon(keywords, exclude=()):
    return find_image("cartoon", keywords, None, exclude)


# ---------------------------------------------------------------------------
# Covers
# ---------------------------------------------------------------------------
def front_cover(img) -> str:
    return f'<section class="page cover"><img class="full" src="{_uri(img)}" alt="Front cover"></section>'


def back_cover(img) -> str:
    return f'<section class="page cover"><img class="full" src="{_uri(img)}" alt="Back cover"></section>'


def inside_cover(title: str, subtitle: str, level: str, contents, how_to_use=None,
                 footer: str = "", extra_html: str = "") -> str:
    """Page 2: book identity, 'this book belongs to', contents and how-to-use, filled cleanly within 240mm."""
    how = how_to_use or [
        ("&#128214;", "Read", "Read the rule. Study the picture."),
        ("&#9998;", "Try", "Write your answers on the lines."),
        ("&#10003;", "Check", "Mark it with the answers at the back."),
        ("&#9733;", "Remember", "Learn the Golden Rule by heart."),
    ]
    con = "".join(
        f'<tr><td style="width:26mm; min-width:26mm; padding:1.8mm 3mm; white-space:nowrap;"><span class="chip" style="font-size:9.5pt; /* hf-ok */ padding:0.5mm 2.8mm; font-weight:700; white-space:nowrap; display:inline-block; text-align:center; min-width:18mm;">{n}</span></td>'
        f'<td style="padding:1.8mm 3mm; font-size:10.5pt; /* hf-ok */ line-height:1.25; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">{t}</td>'
        f'<td style="text-align:right; width:18mm; min-width:18mm; font-weight:700; padding:1.8mm 3mm; font-size:10.5pt; /* hf-ok */ color:var(--primary); white-space:nowrap;">p. {p}</td></tr>'
        for n, t, p in contents
    )
    hw = "".join(
        f'<div style="background:#fff; border:1.5px solid var(--soft); border-top:3.5px solid var(--accent); '
        f'border-radius:6px; padding:2mm 2.5mm; display:flex; flex-direction:column; gap:1mm; min-width:0;">'
        f'<div style="display:flex; align-items:center; gap:1.5mm; font-weight:800; font-size:11pt; /* hf-ok */ color:var(--primary);">'
        f'<span style="width:5mm; height:5mm; border-radius:50%; background:var(--light); border:1px solid var(--accent); color:var(--primary); '
        f'display:inline-flex; align-items:center; justify-content:center; font-size:8.5pt; /* hf-ok */ flex:0 0 auto;">{i}</span>'
        f'<span>{h}</span></div>'
        f'<div style="font-size:9.5pt; /* hf-ok */ line-height:1.25; color:var(--muted);">{t}</div>'
        f'</div>'
        for i, h, t in how
    )
    body = (
        page_title(title, kicker=level)
        + f'<p class="lead" style="margin-top:-2mm; font-size:12.5pt; color:var(--muted);">{subtitle}</p>'
        + '<div class="box worked" style="padding:2.5mm 4mm; display:grid; grid-template-columns:1.4fr 1fr 1fr; gap:2mm 5mm; font-size:11.5pt; /* hf-ok */">'
          '<div><span style="font-weight:700; color:var(--primary); font-size:10.5pt; /* hf-ok */">This book belongs to:</span><div class="aline" style="height:6.5mm;"></div></div>'
          '<div><span style="font-weight:700; color:var(--primary); font-size:10.5pt; /* hf-ok */">Exam date:</span><div class="aline" style="height:6.5mm;"></div></div>'
          '<div><span style="font-weight:700; color:var(--primary); font-size:10.5pt; /* hf-ok */">Target level:</span><div class="aline" style="height:6.5mm;"></div></div></div>'
        + '<h2 style="font-size:15pt; margin:1mm 0 1mm 0;">What is inside</h2>'
        + f'<table class="t" style="font-size:11pt; /* hf-ok */ width:100%; border-collapse:separate;"><tbody>{con}</tbody></table>'
        + '<h2 style="font-size:15pt; margin:1mm 0 1mm 0;">How to use this book</h2>'
        + extra_html
        + f'<div style="display:grid; grid-template-columns:repeat({len(how)}, 1fr); gap:2.5mm;">{hw}</div>'
    )
    return page(body, header=("Master Functional Skills", level), footer=footer, page_no=2)


# ---------------------------------------------------------------------------
# Legacy content cleaner (re-use old 7–8pt data modules safely)
# ---------------------------------------------------------------------------
def clean_legacy(html_s: str) -> str:
    """Strip inline font-size / line-height / tight margins from legacy HTML snippets so the
    kit typography (13pt floor) applies."""
    if not html_s:
        return ""
    s = re.sub(r"font-size\s*:\s*[\d.]+\s*(pt|px|em|rem|%)\s*;?", "", html_s)
    s = re.sub(r"line-height\s*:\s*[\d.]+\s*;?", "", s)
    s = re.sub(r"margin\s*:\s*[^;\"]+;?", "", s)
    s = re.sub(r"padding\s*:\s*[^;\"]+;?", "", s)
    s = re.sub(r'\sstyle="\s*"', "", s)
    return s


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------
_OVERFLOW_JS = """
<script>
window.addEventListener('load', function(){
  var bad=[];
  document.querySelectorAll('section.page').forEach(function(p,i){
    var b=p.querySelector('.body'); if(!b) return;
    var extra = b.scrollHeight - b.clientHeight;
    b.querySelectorAll('.fill').forEach(function(f){
      var cs = getComputedStyle(f), mh = parseFloat(cs.minHeight)||0;
      if (f.getBoundingClientRect().height <= mh + 1 && extra > 2) {}
    });
    if (extra > 2) bad.push((i+1) + ':' + (extra/3.7795).toFixed(0));
  });
  document.body.setAttribute('data-overflow', bad.join(','));
});
</script>
"""


def build_html(pages, theme="maths", entry3=False, title="Master Functional Skills") -> str:
    return (f'<!DOCTYPE html><html lang="en-GB"><head><meta charset="utf-8"><title>{E(title)}</title>'
            f'{get_css(theme, entry3)}{_OVERFLOW_JS}</head><body>{"".join(pages)}</body></html>')


def _chromium(args, timeout=180):
    cmd = [CHROMIUM, "--headless=new", "--disable-gpu", "--no-sandbox", "--disable-dev-shm-usage",
           "--allow-file-access-from-files", "--hide-scrollbars"] + args
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)


def check_overflow(html_path) -> list[int]:
    """Return [(page_no, overflow_mm), ...] for pages whose body content overflows (gets clipped)."""
    r = _chromium(["--virtual-time-budget=8000", "--window-size=794,1123", "--dump-dom", Path(html_path).as_uri()])
    m = re.search(r'data-overflow="([\d,:]*)"', r.stdout)
    return [tuple(int(v) for v in x.split(":")) for x in m.group(1).split(",") if x] if m else []


def render_pdf(pages, out_path, theme="maths", entry3=False, title="Master Functional Skills",
               keep_html=True) -> dict:
    """Write HTML next to the PDF (…/build/<name>.html) and print it to PDF with headless Chromium.
    Returns {"pdf":..., "html":..., "overflow":[pages]}."""
    out = Path(out_path).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    build = out.parent / "build"
    build.mkdir(exist_ok=True)
    html_path = build / (out.stem + ".html")
    html_path.write_text(build_html(pages, theme, entry3, title), encoding="utf-8")
    r = _chromium(["--no-pdf-header-footer", "--virtual-time-budget=10000",
                   f"--print-to-pdf={out}", html_path.as_uri()])
    if not out.exists():
        raise RuntimeError(f"Chromium failed: {r.stderr[-2000:]}")
    overflow = check_overflow(html_path)
    if not keep_html:
        html_path.unlink(missing_ok=True)
    return {"pdf": str(out), "html": str(html_path), "overflow": overflow}


# ---------------------------------------------------------------------------
# QA
# ---------------------------------------------------------------------------
def font_audit(html_path) -> list[str]:
    """List every font-size below 12pt in the HTML (except lines marked hf-ok = header/footer)."""
    bad = []
    txt = Path(html_path).read_text(encoding="utf-8")
    for m in re.finditer(r"font-size\s*:\s*([\d.]+)\s*(pt|px)", txt):
        v = float(m.group(1)) * (0.75 if m.group(2) == "px" else 1)
        ctx = txt[max(0, m.start() - 120): m.end() + 30]
        if v < 12 and "hf-ok" not in ctx:
            bad.append(f"{v:g}pt …{ctx[-80:]!r}")
    return bad


def _inspect_page_pixels(img, is_cover: bool = False) -> tuple[float, float, bool, bool, int | None]:
    """(bottom_blank_frac, largest_internal_blank_frac, margin_overflow, edge_cutoff, foot_line_y)
    for one rendered page (PIL image)."""
    im = img.convert("RGB")
    w, h = im.size
    px = im.load()
    from collections import Counter
    margin_samples = (
        [px[2, 2], px[w - 3, 2], px[2, h - 3], px[w - 3, h - 3]] +
        [px[x, 2] for x in range(10, w - 10, max(1, (w - 20) // 10))] +
        [px[x, h - 3] for x in range(10, w - 10, max(1, (w - 20) // 10))]
    )
    bg = Counter(margin_samples).most_common(1)[0][0]
    x0, x1 = int(w * 0.04), int(w * 0.96)
    span = x1 - x0

    def count(y):
        n = 0
        for x in range(x0, x1):
            p = px[x, y]
            if abs(p[0] - bg[0]) + abs(p[1] - bg[1]) + abs(p[2] - bg[2]) > 30:
                n += 1
        return n

    counts = [count(y) for y in range(h)]
    rows = [c < 2 for c in counts]
    foot_line = next((y for y in range(h - 1, int(h * 0.85), -1) if counts[y] > 0.6 * span), None)

    margin_overflow = False
    edge_cutoff = False
    if not is_cover:
        margin_overflow = any(counts[y] >= 2 for y in range(int(h * 0.968), h))
        edge_cutoff = counts[h - 1] >= 2 or counts[h - 2] >= 2
        if foot_line and (foot_line / h > 0.955):
            margin_overflow = True

    if foot_line is None:
        y = h - 1
        while y > 0 and not rows[y]:
            y -= 1
        margin = 0
    else:
        y = foot_line - 1
        margin = round(3.5 / 297 * h)
    run = 0
    while y > 0 and rows[y]:
        run += 1
        y -= 1
    bottom = max(0, run - margin) / h

    best = cur = 0
    for yy in range(int(h * 0.06), int(h * 0.92)):
        cur = cur + 1 if rows[yy] else 0
        best = max(best, cur)
    return bottom, best / h, margin_overflow, edge_cutoff, foot_line


def _blank_bottom_fraction(img) -> tuple[float, float]:
    b, internal, _, _, _ = _inspect_page_pixels(img)
    return b, internal


def qa_report(pdf_path, dpi: int = 30, threshold: float = 0.15, skip_pages=None,
              contact_sheet: str | None = None, html_path=None) -> dict:
    """pdfinfo size/count + per-page empty-bottom measurement + overflow detection + contact sheet PNG.
    skip_pages: 1-based pages to ignore for blank-bottom check (defaults to covers: 1, 2, pages)."""
    from PIL import Image
    pdf = Path(pdf_path).resolve()
    info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
    pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
    size = re.search(r"Page size:\s+(.+)", info).group(1).strip()
    m = re.match(r"([\d.]+) x ([\d.]+) pts", size)
    a4 = bool(m and abs(float(m.group(1)) - 595.28) < 2 and abs(float(m.group(2)) - 841.89) < 2)

    skip = set(skip_pages if skip_pages is not None else ([1, pages] + ([2] if pages >= 2 else [])))

    dom_overflow = {}
    html_target = html_path
    if not html_target:
        cand = pdf.parent / "build" / (pdf.stem + ".html")
        if cand.exists():
            html_target = cand
    if html_target and Path(html_target).exists():
        try:
            dom_overflow = dict(check_overflow(html_target))
        except Exception:
            pass

    tmp = Path(tempfile.mkdtemp(prefix="a4qa_"))
    subprocess.run(["pdftoppm", "-r", str(dpi), "-png", str(pdf), str(tmp / "p")], check=True)
    files = sorted(tmp.glob("p-*.png"), key=lambda p: int(p.stem.split("-")[-1]))
    results, flagged = [], []
    for i, f in enumerate(files, 1):
        is_cover = (i in (1, pages))
        b, internal, margin_overflow, edge_cutoff, foot_y = _inspect_page_pixels(Image.open(f), is_cover=is_cover)
        over_mm = dom_overflow.get(i, 0)
        has_overflow = margin_overflow or edge_cutoff or (over_mm > 0)

        is_blank_flag = False
        if i not in skip:
            is_blank_flag = (b > threshold or internal > threshold)

        flag = has_overflow or is_blank_flag
        res_entry = {
            "page": i,
            "bottom_blank": round(b, 3),
            "largest_gap": round(internal, 3),
            "overflow_mm": over_mm,
            "margin_overflow": margin_overflow,
            "edge_cutoff": edge_cutoff,
            "flag": flag,
        }
        if i in skip and not has_overflow:
            res_entry["skipped"] = True
        results.append(res_entry)
        if flag:
            flagged.append(i)

    sheet = Path(contact_sheet) if contact_sheet else pdf.with_name(pdf.stem + "_contact.png")
    labels = []
    for f in files:
        labels += ["-label", f"p{int(f.stem.split('-')[-1])}", str(f)]
    subprocess.run(["magick", "montage", *labels, "-tile", "6x", "-geometry", "+6+6",
                    "-background", "#d4d4d8", "-pointsize", "14", str(sheet)], check=True)
    fonts = font_audit(html_target) if html_target else None
    shutil.rmtree(tmp, ignore_errors=True)
    rep = {"pdf": str(pdf), "pages": pages, "page_size": size, "a4": a4, "even": pages % 2 == 0,
           "flagged": flagged, "per_page": results, "contact_sheet": str(sheet),
           "small_fonts": fonts}
    return rep


def print_report(rep: dict):
    print(f"PDF: {rep['pdf']}")
    print(f"  pages={rep['pages']} even={rep['even']} size={rep['page_size']} A4={rep['a4']}")
    for r in rep["per_page"]:
        if r.get("skipped"):
            print(f"  p{r['page']:>2}: cover/inside (skipped)")
        else:
            issues = []
            if r.get("margin_overflow") or r.get("overflow_mm", 0) > 0 or r.get("edge_cutoff"):
                mm = r.get("overflow_mm", 0)
                issues.append(f"OVERFLOW ({mm}mm)" if mm else "MARGIN OVERFLOW")
            if r.get("bottom_blank", 0) > 0.15:
                issues.append(f"bottom blank {r['bottom_blank'] * 100:5.1f}%")
            if r.get("largest_gap", 0) > 0.15:
                issues.append(f"gap {r['largest_gap'] * 100:5.1f}%")
            status_desc = " | ".join(issues) if issues else "ok"
            print(f"  p{r['page']:>2}: bottom blank {r['bottom_blank'] * 100:5.1f}%  largest gap {r['largest_gap'] * 100:5.1f}%  {'FLAG' if r['flag'] else 'ok'} ({status_desc})")
    print(f"  flagged: {rep['flagged'] or 'none'}")
    if rep.get("small_fonts") is not None:
        print(f"  fonts < 12pt (excluding header/footer): {len(rep['small_fonts'])}")
        for s in rep["small_fonts"][:10]:
            print("    ", s)
    print(f"  contact sheet: {rep['contact_sheet']}")
