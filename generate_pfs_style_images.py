#!/usr/bin/env python3
"""
generate_pfs_style_images.py
Generates all Master Functional Skills Shop images in the exact signature positional format
of Pass Functional Skills (PFS):
1. 3D Isometric Angled Books (with spine, page block, and perspective tilt matching PFS)
2. Fanned Pocket Revision Card Decks (tilted front card + fanned topic cards with badges and traps)
3. Fanned 5-Mock Exam Paper Packs (5 booklets spread in symmetrical semi-circle arc)
4. Multi-Volume Bundles and Hero Showcase
"""

import os
import sys
import math
import subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import generate_overhauled_cards as goc

BOOKS_DIR = "/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk/assets/img/books"
PROJECT_BOOKS_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk/assets/img/books"
COVERS_DIR = "/tmp/card_covers"
os.makedirs(BOOKS_DIR, exist_ok=True)
os.makedirs(PROJECT_BOOKS_DIR, exist_ok=True)
os.makedirs(COVERS_DIR, exist_ok=True)

FONT_BOLD = "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf"
FONT_REGULAR = "/usr/share/fonts/TTF/DejaVuSans.ttf"

def get_font(bold=False, size=14):
    font_path = FONT_BOLD if bold else FONT_REGULAR
    try:
        return ImageFont.truetype(font_path, size)
    except Exception:
        return ImageFont.load_default()

def find_perspective_coeffs(dst_pts, src_pts):
    matrix = []
    for (x, y), (u, v) in zip(dst_pts, src_pts):
        matrix.append([x, y, 1, 0, 0, 0, -u*x, -u*y])
        matrix.append([0, 0, 0, x, y, 1, -v*x, -v*y])
    A = np.matrix(matrix, dtype=float)
    B = np.array(src_pts).reshape(8)
    res = np.dot(np.linalg.inv(A.T * A) * A.T, B)
    return np.array(res).reshape(8)

def add_card_shadow(img, offset=(2, 8), blur=10, opacity=100):
    w, h = img.size
    pad = blur * 3
    shadow = Image.new("RGBA", (w + pad * 2, h + pad * 2), (0, 0, 0, 0))
    alpha = img.split()[3]
    black = Image.new("L", img.size, 0)
    shadow_mask = Image.merge("RGBA", (black, black, black, alpha))
    r, g, b, a = shadow_mask.split()
    a = a.point(lambda p: int(p * (opacity / 255.0)))
    shadow_mask = Image.merge("RGBA", (r, g, b, a))
    shadow.paste(shadow_mask, (pad + offset[0], pad + offset[1]))
    shadow = shadow.filter(ImageFilter.GaussianBlur(blur))
    shadow.paste(img, (pad, pad), img)
    return shadow

# ==============================================================================
# 1. 3D ISOMETRIC BOOK GENERATOR (Matches PFS Book Mockups)
# ==============================================================================
def render_3d_isometric_book(cover_path, output_path, spine_title, spine_color, is_white=False):
    if not os.path.exists(cover_path):
        print(f"Warning: Cover not found: {cover_path}")
        return
        
    cover = Image.open(cover_path).convert("RGBA")
    cw, ch = cover.size
    
    canvas_w, canvas_h = 760, 900
    canvas = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    
    # Precise 3D isometric coordinates calibrated to PFS reference
    c_tl = (175, 305)   # Spine top
    c_tr = (455, 125)   # Top corner
    c_br = (715, 435)   # Right corner
    c_bl = (435, 655)   # Spine bottom
    
    # Spine thickness vector (down-left)
    th_dx, th_dy = -48, 30
    s_tr = c_tl
    s_br = c_bl
    s_tl = (c_tl[0] + th_dx, c_tl[1] + th_dy)
    s_bl = (c_bl[0] + th_dx, c_bl[1] + th_dy)
    
    # Pages thickness vector (downward)
    pg_dx, pg_dy = 0, 44
    p_tl = c_bl
    p_tr = c_br
    p_br = (c_br[0] + pg_dx, c_br[1] + pg_dy)
    p_bl = (c_bl[0] + pg_dx, c_bl[1] + pg_dy)

    # 1. Soft Floor Shadow
    shadow_layer = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow_layer)
    s_poly = [
        (s_bl[0] - 30, s_bl[1] + 40),
        (s_tl[0] - 20, s_tl[1] + 50),
        (c_tr[0] + 60, c_tr[1] + 70),
        (p_br[0] + 50, p_br[1] + 50),
        (p_bl[0] + 20, p_bl[1] + 40)
    ]
    s_draw.polygon(s_poly, fill=(7, 13, 30, 150))
    s_draw.ellipse([80, canvas_h - 220, canvas_w - 60, canvas_h - 40], fill=(7, 13, 30, 130))
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(34))
    canvas.paste(shadow_layer, (0, 0), shadow_layer)
    
    # 2. Pages Block (bottom edge)
    pages_layer = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    p_draw = ImageDraw.Draw(pages_layer)
    p_draw.polygon([p_tl, p_tr, p_br, p_bl], fill=(244, 244, 242, 255), outline=(205, 205, 205, 255))
    for t in np.linspace(0.1, 0.9, 14):
        l_start = (int(p_tl[0] + (p_bl[0] - p_tl[0]) * t), int(p_tl[1] + (p_bl[1] - p_tl[1]) * t))
        l_end = (int(p_tr[0] + (p_br[0] - p_tr[0]) * t), int(p_tr[1] + (p_br[1] - p_tr[1]) * t))
        p_draw.line([l_start, l_end], fill=(225, 225, 222, 170), width=1)
        
    corner_poly = [s_bl, c_bl, p_bl, (s_bl[0] + pg_dx, s_bl[1] + pg_dy)]
    p_draw.polygon(corner_poly, fill=(230, 230, 228, 255))
    canvas.paste(pages_layer, (0, 0), pages_layer)

    # 3. Spine
    spine_w_base = 100
    spine_h_base = 800
    spine_img = Image.new("RGBA", (spine_w_base, spine_h_base), (0, 0, 0, 0))
    sp_draw = ImageDraw.Draw(spine_img)
    
    for x in range(spine_w_base):
        factor = 0.5 + 0.5 * (x / float(spine_w_base))
        col = tuple(int(c * factor) for c in spine_color) + (255,)
        sp_draw.line([(x, 0), (x, spine_h_base)], fill=col)
    
    # Spine text
    sp_text = Image.new("RGBA", (spine_h_base, spine_w_base), (0, 0, 0, 0))
    st_draw = ImageDraw.Draw(sp_text)
    text_color = (15, 23, 42, 240) if is_white else (255, 255, 255, 240)
    st_draw.text((120, 32), spine_title.upper(), fill=text_color, font=get_font(bold=True, size=24))
    sp_text_rot = sp_text.rotate(-90, expand=True)
    spine_img.paste(sp_text_rot, (0, 0), sp_text_rot)

    src_spine = [(0, 0), (spine_w_base, 0), (spine_w_base, spine_h_base), (0, spine_h_base)]
    dst_spine = [s_tl, s_tr, s_br, s_bl]
    spine_coeffs = find_perspective_coeffs(dst_spine, src_spine)
    transformed_spine = spine_img.transform((canvas_w, canvas_h), Image.Transform.PERSPECTIVE, spine_coeffs, Image.Resampling.BICUBIC)
    canvas.paste(transformed_spine, (0, 0), transformed_spine)

    # 4. Front Cover Transform
    src_cover = [(0, 0), (cw, 0), (cw, ch), (0, ch)]
    dst_cover = [c_tl, c_tr, c_br, c_bl]
    coeffs = find_perspective_coeffs(dst_cover, src_cover)
    transformed_cover = cover.transform((canvas_w, canvas_h), Image.Transform.PERSPECTIVE, coeffs, Image.Resampling.BICUBIC)

    # Spine fold sheen
    sheen = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    sh_draw = ImageDraw.Draw(sheen)
    sh_draw.line([c_tl, c_bl], fill=(0, 0, 0, 110), width=3)
    sh_draw.line([(c_tl[0]+3, c_tl[1]), (c_bl[0]+3, c_bl[1])], fill=(255, 255, 255, 70), width=2)

    canvas.paste(transformed_cover, (0, 0), transformed_cover)
    canvas.paste(sheen, (0, 0), sheen)

    canvas.save(output_path, "PNG", optimize=True)
    proj_out = os.path.join(PROJECT_BOOKS_DIR, os.path.basename(output_path))
    canvas.save(proj_out, "PNG", optimize=True)
    print(f"Generated 3D Isometric Book: {output_path}")

# ==============================================================================
# 2. DOUBLE BOOK BUNDLE GENERATOR
# ==============================================================================
def render_double_book_bundle(book1_path, book2_path, output_path):
    if not os.path.exists(book1_path) or not os.path.exists(book2_path):
        return
    b1 = Image.open(book1_path).convert("RGBA")
    b2 = Image.open(book2_path).convert("RGBA")
    
    canvas_w, canvas_h = 860, 920
    canvas = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    
    # Back book (b2) offset up-left
    b2_scaled = b2.resize((int(b2.width * 0.94), int(b2.height * 0.94)), Image.Resampling.LANCZOS)
    canvas.paste(b2_scaled, (40, 20), b2_scaled)
    
    # Front book (b1) placed forward
    canvas.paste(b1, (110, 50), b1)
    
    canvas.save(output_path, "PNG", optimize=True)
    proj_out = os.path.join(PROJECT_BOOKS_DIR, os.path.basename(output_path))
    canvas.save(proj_out, "PNG", optimize=True)
    print(f"Generated Double Book Bundle: {output_path}")

# ==============================================================================
# 3. FANNED REVISION CARDS GENERATOR (Matches PFS Cards Mockups)
# ==============================================================================
def render_cover_card_to_png(deck_key):
    png_path = os.path.join(COVERS_DIR, f"{deck_key}.png")
    html_path = os.path.join(COVERS_DIR, f"{deck_key}.html")
    
    meta = goc.DECK_METADATA[deck_key]
    inner = goc.render_cover_card_front_html(meta, is_quadrant=False)
    
    html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      width: 740px;
      height: 525px;
      background: transparent;
      overflow: hidden;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }}
    .a6-card {{
      width: 740px !important;
      height: 525px !important;
      border-radius: 20px !important;
      border: 2px solid rgba(255, 255, 255, 0.45) !important;
      box-shadow: none !important;
      overflow: hidden;
      padding: 24px 30px 18px !important;
    }}
  </style>
</head>
<body>
  {inner}
</body>
</html>"""
    
    with open(html_path, "w") as f:
        f.write(html)
        
    subprocess.run([
        "/usr/lib/chromium/chromium",
        "--headless=new",
        "--disable-gpu",
        "--user-data-dir=/tmp/test_chrome_profile",
        "--window-size=740,525",
        "--default-background-color=00000000",
        f"--screenshot={png_path}",
        html_path
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    return png_path

def create_card_topic(width=470, height=335, strand_code="N1", strand_name="NUMBERS",
                      topic="Ordering Numbers & Decimals", q_title="Ascending & Descending Decimal Order",
                      c_bg=(225, 29, 72), card_num=18, card_total=50,
                      example_text="Example: Arrange 0.45, 0.405, 0.54 in ascending order.",
                      method_text="Step: Equalize decimal places: 0.450, 0.405, 0.540 -> 0.405, 0.45, 0.54",
                      trap_text="Never assume longer digits mean bigger numbers! 0.405 is LESS than 0.45."):
    card = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(card)
    
    draw.rounded_rectangle([0, 0, width-1, height-1], radius=18, fill=(255, 255, 255, 255), outline=(205, 210, 222, 255), width=2)
    
    draw.rounded_rectangle([4, 4, width-5, 46], radius=14, fill=(245, 247, 250, 255))
    draw.rectangle([4, 22, width-5, 46], fill=(245, 247, 250, 255))
    
    draw.rounded_rectangle([14, 10, 52, 38], radius=5, fill=c_bg)
    draw.text((20, 15), strand_code, fill=(255, 255, 255), font=get_font(bold=True, size=14))
    
    draw.text((60, 15), f"{strand_name}  •  {topic}", fill=(30, 41, 59), font=get_font(bold=True, size=13))
    draw.text((width - 105, 15), f"Card {card_num} of {card_total}", fill=(100, 116, 139), font=get_font(bold=False, size=11))
    draw.line([(4, 47), (width-5, 47)], fill=(226, 232, 240), width=1)
    
    draw.text((20, 60), q_title, fill=(15, 23, 42), font=get_font(bold=True, size=17))
    
    draw.rounded_rectangle([20, 92, width - 20, 218], radius=8, fill=(248, 250, 252), outline=(226, 232, 240), width=1)
    draw.text((32, 104), example_text, fill=(51, 65, 85), font=get_font(bold=False, size=12))
    draw.text((32, 132), method_text, fill=(2, 132, 199), font=get_font(bold=True, size=12))
    
    draw.rounded_rectangle([20, 232, width - 20, 296], radius=8, fill=(254, 242, 242), outline=(252, 165, 165), width=1)
    draw.text((32, 241), "⚠ EXAM TRAP WARNING:", fill=(185, 28, 28), font=get_font(bold=True, size=11))
    draw.text((32, 261), trap_text, fill=(153, 27, 27), font=get_font(bold=False, size=10))
    
    draw.text((20, 310), "Master Functional Skills — Official Curriculum Spec", fill=(148, 163, 184), font=get_font(bold=False, size=10))
    draw.rounded_rectangle([width - 155, 303, width - 20, 331], radius=5, fill=(238, 242, 255))
    draw.text((width - 144, 311), "Turn over for question ➔", fill=(67, 56, 202), font=get_font(bold=True, size=9))

    return card

def render_fanned_cards_deck(deck_key, topic_data, output_path, card_count):
    cover_png = render_cover_card_to_png(deck_key)
    cover_img = Image.open(cover_png).convert("RGBA")
    
    canvas_w, canvas_h = 760, 620
    canvas = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    
    floor_shadow = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    fs_draw = ImageDraw.Draw(floor_shadow)
    fs_draw.ellipse([60, canvas_h - 130, canvas_w - 60, canvas_h - 25], fill=(7, 13, 30, 100))
    floor_shadow = floor_shadow.filter(ImageFilter.GaussianBlur(26))
    canvas.paste(floor_shadow, (0, 0), floor_shadow)
    
    deck_angles = [-18, -10, 4, 14]
    deck_offsets = [(74, 110), (109, 90), (149, 80), (184, 85)]
    
    for i in range(len(topic_data[:4])):
        t = topic_data[i]
        card = create_card_topic(
            width=470, height=335,
            strand_code=t["code"], strand_name=t["strand"],
            topic=t["topic"], q_title=t["q_title"],
            c_bg=t["color"], card_num=t["num"], card_total=card_count,
            example_text=t["example"], method_text=t["method"], trap_text=t["trap"]
        )
        card_sh = add_card_shadow(card, offset=(3, 8), blur=8, opacity=85)
        rotated = card_sh.rotate(deck_angles[i], resample=Image.Resampling.BICUBIC, expand=True)
        canvas.paste(rotated, deck_offsets[i], rotated)
        
    front = cover_img.resize((508, 360), Image.Resampling.LANCZOS)
    front_sh = add_card_shadow(front, offset=(4, 14), blur=14, opacity=120)
    front_rot = front_sh.rotate(-7.0, resample=Image.Resampling.BICUBIC, expand=True)
    canvas.paste(front_rot, (89, 115), front_rot)
    
    canvas.save(output_path, "PNG", optimize=True)
    proj_out = os.path.join(PROJECT_BOOKS_DIR, os.path.basename(output_path))
    canvas.save(proj_out, "PNG", optimize=True)
    print(f"Generated Fanned Revision Cards: {output_path}")

# ==============================================================================
# 4. FANNED 5-MOCK EXAM PAPERS GENERATOR (Symmetrical Arc Pivot)
# ==============================================================================
def create_mock_booklet(booklet_num=1, title="Numbers & Calculation", topics=None, subject="MATHEMATICS", level="Level 2"):
    w, h = 480, 680
    page = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(page)
    
    draw.rounded_rectangle([0, 0, w-1, h-1], radius=6, fill=(255, 255, 255, 255), outline=(200, 205, 215, 255), width=1)
    draw.line([(18, 0), (18, h)], fill=(230, 233, 240, 255), width=2)
    draw.rounded_rectangle([15, 70, 21, 100], radius=2, fill=(148, 163, 184))
    draw.rounded_rectangle([15, h-100, 21, h-70], radius=2, fill=(148, 163, 184))
    
    draw.rounded_rectangle([36, 24, 180, 64], radius=6, fill=(248, 250, 252), outline=(226, 232, 240), width=1)
    draw.polygon([(46, 44), (56, 38), (66, 44), (56, 50)], fill=(0, 40, 85))
    draw.text((72, 34), "MASTER", fill=(0, 40, 85), font=get_font(bold=True, size=11))
    draw.text((72, 47), "FUNCTIONAL SKILLS", fill=(2, 132, 199), font=get_font(bold=True, size=7))
    
    draw.text((w - 240, 26), f"FUNCTIONAL SKILLS {subject.upper()}", fill=(15, 23, 42), font=get_font(bold=True, size=10))
    draw.text((w - 240, 40), "Pearson Edexcel • C&G • Open Awards Aligned", fill=(100, 116, 139), font=get_font(bold=False, size=8))
    draw.text((w - 240, 52), f"{level} • Official 5-Mock Exam Series", fill=(2, 132, 199), font=get_font(bold=True, size=9))
    draw.line([(36, 74), (w - 24, 74)], fill=(15, 23, 42), width=2)
    
    draw.text((36, 88), f"Booklet {booklet_num}: {title}", fill=(15, 23, 42), font=get_font(bold=True, size=18))
    
    draw.rounded_rectangle([36, 120, w - 24, 155], radius=4, fill=(255, 255, 255), outline=(148, 163, 184), width=1)
    draw.text((44, 125), "Candidate Forename:", fill=(71, 85, 105), font=get_font(bold=False, size=9))
    draw.line([(150, 140), (280, 140)], fill=(203, 213, 225), width=1)
    draw.text((290, 125), "Surname:", fill=(71, 85, 105), font=get_font(bold=False, size=9))
    draw.line([(340, 140), (w - 32, 140)], fill=(203, 213, 225), width=1)
    
    draw.text((36, 172), f"Topics Covered in Booklet {booklet_num}:", fill=(30, 41, 59), font=get_font(bold=True, size=11))
    if topics is None:
        topics = ["Topic 1 Coverage", "Topic 2 Methods", "Topic 3 Problem Solving"]
    y_pos = 196
    for t in topics[:5]:
        draw.text((44, y_pos), f"• {t}", fill=(71, 85, 105), font=get_font(bold=False, size=10))
        y_pos += 20
        
    draw.rounded_rectangle([36, 310, w - 24, 440], radius=6, fill=(248, 250, 252), outline=(226, 232, 240), width=1)
    draw.text((48, 322), "Instructions & Examination Rules:", fill=(15, 23, 42), font=get_font(bold=True, size=10))
    draw.text((48, 344), "• Use black ink or ball-point pen. Show all method working.", fill=(100, 116, 139), font=get_font(bold=False, size=9))
    draw.text((48, 362), "• Answer all questions in the spaces provided.", fill=(100, 116, 139), font=get_font(bold=False, size=9))
    draw.text((48, 380), "• Marks are awarded for clear stepped calculations.", fill=(100, 116, 139), font=get_font(bold=False, size=9))
    draw.text((48, 398), "• Total Marks: 64 Marks | Time Allowed: 1 Hour 30 Minutes", fill=(2, 132, 199), font=get_font(bold=True, size=9))

    draw.rounded_rectangle([w - 140, h - 85, w - 30, h - 35], radius=6, fill=(0, 40, 85))
    draw.text((w - 128, h - 75), f"SET {booklet_num}", fill=(255, 255, 255), font=get_font(bold=True, size=14))
    draw.text((w - 128, h - 55), "OFFICIAL MOCK", fill=(245, 158, 11), font=get_font(bold=True, size=8))
    
    draw.text((36, h - 45), "Master Functional Skills — Copyright © All Rights Reserved", fill=(148, 163, 184), font=get_font(bold=False, size=9))
    return page

def render_fanned_mock_pack(subject, level, booklet_topics, output_path):
    canvas_w, canvas_h = 760, 720
    canvas = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))

    floor_shadow = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    fs_draw = ImageDraw.Draw(floor_shadow)
    fs_draw.ellipse([80, canvas_h - 130, canvas_w - 80, canvas_h - 20], fill=(7, 13, 30, 120))
    floor_shadow = floor_shadow.filter(ImageFilter.GaussianBlur(30))
    canvas.paste(floor_shadow, (0, 0), floor_shadow)

    angles = [-22, -11, 0, 11, 22]
    pivot = (canvas_w // 2, canvas_h - 80)
    bw, bh = 360, 510

    for i in range(5):
        b_num = 5 - i # Symmetrical layering
        title, topics = booklet_topics[b_num - 1]
        booklet = create_mock_booklet(b_num, title, topics, subject=subject, level=level)
        booklet = booklet.resize((bw, bh), Image.Resampling.LANCZOS)
        booklet_sh = add_card_shadow(booklet, blur=10, opacity=85, offset=(2, 6))
        
        layer = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
        bx = pivot[0] - booklet_sh.width // 2
        by = pivot[1] - booklet_sh.height + 40
        layer.paste(booklet_sh, (bx, by), booklet_sh)
        
        rotated = layer.rotate(angles[i], resample=Image.Resampling.BICUBIC, center=pivot)
        canvas.paste(rotated, (0, 0), rotated)

    canvas.save(output_path, "PNG", optimize=True)
    proj_out = os.path.join(PROJECT_BOOKS_DIR, os.path.basename(output_path))
    canvas.save(proj_out, "PNG", optimize=True)
    print(f"Generated Symmetrical 5-Mock Exam Fan: {output_path}")

# ==============================================================================
# 5. TWIN PACK CARDS BUNDLE & HERO SHOWCASE
# ==============================================================================
def render_twin_pack_cards(maths_cards_path, english_cards_path, output_path):
    if not os.path.exists(maths_cards_path) or not os.path.exists(english_cards_path):
        return
    c_m = Image.open(maths_cards_path).convert("RGBA")
    c_e = Image.open(english_cards_path).convert("RGBA")
    
    canvas_w, canvas_h = 860, 640
    canvas = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    
    c_m_scaled = c_m.resize((int(c_m.width * 0.88), int(c_m.height * 0.88)), Image.Resampling.LANCZOS)
    canvas.paste(c_m_scaled, (20, 40), c_m_scaled)
    
    c_e_scaled = c_e.resize((int(c_e.width * 0.88), int(c_e.height * 0.88)), Image.Resampling.LANCZOS)
    canvas.paste(c_e_scaled, (200, 30), c_e_scaled)
    
    badge = Image.new("RGBA", (320, 56), (0, 0, 0, 0))
    b_draw = ImageDraw.Draw(badge)
    b_draw.rounded_rectangle([0, 0, 319, 55], radius=28, fill=(245, 158, 11), outline=(255, 255, 255), width=2)
    b_draw.text((32, 16), "LEVEL 2 TWIN PACK • 98 CARDS", fill=(7, 13, 30), font=get_font(bold=True, size=14))
    badge_sh = add_card_shadow(badge, offset=(2, 6), blur=8, opacity=120)
    canvas.paste(badge_sh, (270, 490), badge_sh)
    
    canvas.save(output_path, "PNG", optimize=True)
    proj_out = os.path.join(PROJECT_BOOKS_DIR, os.path.basename(output_path))
    canvas.save(proj_out, "PNG", optimize=True)
    print(f"Generated Twin Pack Cards Bundle: {output_path}")

def render_hero_showcase(output_path):
    canvas_w, canvas_h = 760, 550
    canvas = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    
    floor_shadow = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    fs_draw = ImageDraw.Draw(floor_shadow)
    fs_draw.ellipse([50, canvas_h - 100, canvas_w - 50, canvas_h - 15], fill=(7, 13, 30, 100))
    floor_shadow = floor_shadow.filter(ImageFilter.GaussianBlur(26))
    canvas.paste(floor_shadow, (0, 0), floor_shadow)
    
    # All 6 Front Cover Cards cascading down-right:
    # 0: Master All-Cards Deck (Navy) - Top Left, in front
    # 1: Maths Level 2 (Emerald Green) - Underneath, down & right
    # 2: English Level 2 (Indigo) - Underneath, down & right
    # 3: Maths Level 1 (Ocean Blue) - Underneath, down & right
    # 4: English Level 1 (Teal) - Underneath, down & right
    # 5: Digital Skills (Deep Orange) - Underneath, down & right
    deck_keys = ["all_cards", "maths_l2", "english_l2", "maths_l1", "english_l1", "digital_skills"]
    card_w, card_h = 490, 348
    start_x, start_y = 35, 35
    dx, dy = 42, 26
    
    for i in reversed(range(len(deck_keys))):
        k = deck_keys[i]
        png = render_cover_card_to_png(k)
        card = Image.open(png).convert("RGBA").resize((card_w, card_h), Image.Resampling.LANCZOS)
        
        opacity = 75 + (5 - i) * 10
        card_sh = add_card_shadow(card, offset=(3, 8), blur=10, opacity=opacity)
        
        pos_x = start_x + i * dx
        pos_y = start_y + i * dy
        pad = 10 * 3
        canvas.paste(card_sh, (pos_x - pad, pos_y - pad), card_sh)
        
    canvas.save(output_path, "PNG", optimize=True)
    proj_out = os.path.join(PROJECT_BOOKS_DIR, os.path.basename(output_path))
    canvas.save(proj_out, "PNG", optimize=True)
    print(f"Generated Cascading Hero Showcase: {output_path}")


# ==============================================================================
# MAIN EXECUTION
# ==============================================================================
def main():
    print("=== Generating Master Functional Skills PFS-Format Visuals ===")
    
    # 1. 3D ISOMETRIC BOOKS (all 13 subjects and levels)
    book_configs = [
        ("level2_core_cover_page-1.png", "3d_level2_core.png", "WRITING SKILLS LEVEL 2", (0, 40, 85), False),
        ("level2_companion_cover_page-1.png", "3d_level2_companion.png", "WRITING COMPANION L2", (0, 51, 102), False),
        ("level1_core_cover_page-1.png", "3d_level1_core.png", "WRITING SKILLS LEVEL 1", (12, 78, 69), False),
        ("level1_companion_cover_page-1.png", "3d_level1_companion.png", "WRITING COMPANION L1", (13, 148, 136), False),
        ("spag_mastery_cover_page-1.png", "3d_spag_mastery.png", "SPAG MASTERY HANDBOOK", (15, 23, 42), False),
        ("maths_l2_core_cover_page-1.png", "3d_maths_l2_core.png", "MATHS LEVEL 2 STUDY GUIDE", (2, 132, 199), False),
        ("maths_l2_companion_cover_page-1.png", "3d_maths_l2_companion.png", "MATHS L2 WORKBOOK", (0, 40, 85), False),
        ("maths_l1_core_cover_page-1.png", "3d_maths_l1_core.png", "MATHS LEVEL 1 STUDY GUIDE", (37, 99, 235), False),
        ("maths_l1_companion_cover_page-1.png", "3d_maths_l1_companion.png", "MATHS L1 WORKBOOK", (2, 132, 199), False),
        ("maths_e3_core_cover_page-1.png", "3d_maths_e3_core.png", "MATHS ENTRY 3 GUIDE", (37, 99, 235), False),
        ("english_e3_core_cover_page-1.png", "3d_english_e3_core.png", "ENGLISH ENTRY 3 GUIDE", (12, 78, 69), False),
        ("digital_skills_cover_page-1.png", "3d_digital_skills.png", "DIGITAL SKILLS PRACTICAL", (109, 40, 217), False),
        ("bksb_remediation_cover_page-1.png", "3d_bksb_remediation.png", "BKSB REMEDIATION GUIDE", (30, 58, 138), False),
    ]
    
    for cover_fn, out_fn, spine_title, spine_color, is_white in book_configs:
        cover_p = os.path.join(BOOKS_DIR, cover_fn)
        out_p = os.path.join(BOOKS_DIR, out_fn)
        render_3d_isometric_book(cover_p, out_p, spine_title, spine_color, is_white)

    # 2. DOUBLE BOOK BUNDLE
    render_double_book_bundle(
        os.path.join(BOOKS_DIR, "3d_level2_core.png"),
        os.path.join(BOOKS_DIR, "3d_level2_companion.png"),
        os.path.join(BOOKS_DIR, "3d_bundle_writing_l2.png")
    )

    # 3. FANNED REVISION CARDS DECKS
    maths_l2_topics = [
        {"code": "N1", "strand": "NUMBERS", "topic": "Ordering Decimals", "q_title": "Ascending & Descending Decimal Order", "color": (225, 29, 72), "num": 12, "example": "Order: 0.45, 0.405, 0.54 -> 0.405, 0.45, 0.54", "method": "Rule: Equalize digits with trailing zeros to compare.", "trap": "0.405 is NOT larger than 0.45 just because it has more digits!"},
        {"code": "M2", "strand": "MEASURES", "topic": "Compound Area & Perimeter", "q_title": "Area of L-Shapes & Trapeziums", "color": (2, 132, 199), "num": 24, "example": "Split compound shape into rectangles A and B.", "method": "Area = (a + b)/2 × h for trapezium. Add components.", "trap": "Never count interior joining lines when calculating perimeter!"},
        {"code": "S1", "strand": "STATISTICS", "topic": "Averages & Frequency", "q_title": "Estimated Mean from Grouped Tables", "color": (147, 51, 234), "num": 38, "example": "Estimated Mean = Total (Midpoint × Freq) ÷ Total Freq", "method": "Find midpoints, multiply by frequency, sum and divide.", "trap": "Never divide by the number of rows! Always divide by total frequency."},
        {"code": "R1", "strand": "RATIO", "topic": "Direct Proportion Multipliers", "q_title": "Dividing into 3-Part Ratio", "color": (234, 88, 12), "num": 46, "example": "Divide £240 in ratio 3:4:5. Total parts = 12.", "method": "1 Part = £240 ÷ 12 = £20. Multiply by each part: £60, £80, £100.", "trap": "Check your answers sum back to the original total (£240)."}
    ]
    render_fanned_cards_deck("maths_l2", maths_l2_topics, os.path.join(BOOKS_DIR, "flashcards_maths_l2.png"), card_count=50)

    english_l2_topics = [
        {"code": "W1", "strand": "WRITING", "topic": "Formal Letter Format", "q_title": "Address Layout & Salutation Rules", "color": (22, 163, 74), "num": 8, "example": "Sender address top right, Recipient left. Date below.", "method": "Dear Sir/Madam -> Yours faithfully. Dear Name -> Yours sincerely.", "trap": "Never write 'Yours faithfully' if you know the person's name!"},
        {"code": "R2", "strand": "READING", "topic": "DAFOREST Devices", "q_title": "Identifying Rhetoric & Persuasion", "color": (234, 88, 12), "num": 19, "example": "Direct address, Alliteration, Facts, Opinions, Rhetorical Q.", "method": "Quote the device and explain the direct effect on the reader.", "trap": "Don't just feature-spot! You MUST explain the effect on the reader."},
        {"code": "G1", "strand": "SPAG", "topic": "Comma Splices & Run-Ons", "q_title": "Eliminating Comma Splice Errors", "color": (225, 29, 72), "num": 31, "example": "Incorrect: I studied hard, I passed the exam.", "method": "Fix with semicolon, period, or coordinating conjunction (and/so).", "trap": "A comma alone CANNOT join two complete independent sentences!"},
        {"code": "W3", "strand": "FORMATS", "topic": "Persuasive Articles & Blogs", "q_title": "Headlines, Subheadings & Hooks", "color": (147, 51, 234), "num": 42, "example": "Catchy headline, rhetorical hook intro, structured paragraphs.", "method": "Use organizational markers: bullet lists, bold subheaders.", "trap": "Always adapt tone to target audience (formal vs informal register)."}
    ]
    render_fanned_cards_deck("english_l2", english_l2_topics, os.path.join(BOOKS_DIR, "flashcards_english_l2.png"), card_count=48)

    maths_l1_topics = [
        {"code": "N1", "strand": "NUMBER", "topic": "Whole Numbers & Place Value", "q_title": "Writing Large Numbers in Words", "color": (37, 99, 235), "num": 6, "example": "Write 45,208 in words: Forty-five thousand, two hundred and eight.", "method": "Separate into periods: Thousands, Hundreds, Tens, Units.", "trap": "Watch out for zero placeholders! (208 is not 28)."},
        {"code": "M1", "strand": "MEASURE", "topic": "Metric Unit Conversions", "q_title": "Converting mm, cm, m and km", "color": (2, 132, 199), "num": 15, "example": "Convert 2.5 metres to centimetres: 2.5 × 100 = 250 cm.", "method": "Multiply to go smaller (m -> cm ×100). Divide to go larger.", "trap": "Do not mix up ×10, ×100, and ×1000 multipliers!"},
        {"code": "F1", "strand": "FRACTIONS", "topic": "Fraction of an Amount", "q_title": "Calculating Simple Fractions Non-Calc", "color": (234, 88, 12), "num": 22, "example": "Find 3/4 of £60: £60 ÷ 4 = £15, then £15 × 3 = £45.", "method": "Divide by the denominator, multiply by the numerator.", "trap": "Always complete the division first to keep numbers manageable."},
        {"code": "S1", "strand": "DATA", "topic": "Bar Charts & Tally Tables", "q_title": "Extracting Values from Scales", "color": (22, 163, 74), "num": 32, "example": "Identify scale intervals on vertical axis (intervals of 2, 5 or 10).", "method": "Count grid divisions to verify step increments before reading.", "trap": "Double check axis labels to see if units are in thousands or hundreds."}
    ]
    render_fanned_cards_deck("maths_l1", maths_l1_topics, os.path.join(BOOKS_DIR, "flashcards_maths_l1.png"), card_count=38)

    english_l1_topics = [
        {"code": "W1", "strand": "WRITING", "topic": "Informal Email Structure", "q_title": "Subject Line & Email Etiquette", "color": (15, 118, 110), "num": 6, "example": "Clear subject line, friendly greeting (Hi/Hello), clear purpose.", "method": "Use short paragraphs or bullet points. Sign off with Kind regards.", "trap": "Never send an email without a subject line or clear purpose!"},
        {"code": "R1", "strand": "READING", "topic": "Fact vs Opinion", "q_title": "Distinguishing Facts from Views", "color": (2, 132, 199), "num": 14, "example": "Fact: The store opens at 9am. Opinion: It is the best shop in town.", "method": "Facts can be proven true; opinions express beliefs or feelings.", "trap": "Words like 'best', 'worst', 'should' signal opinions, not facts."},
        {"code": "G1", "strand": "SPAG", "topic": "Apostrophes (Contraction & Possession)", "q_title": "Correct Use of 's and s'", "color": (225, 29, 72), "num": 25, "example": "Contraction: don't = do not. Possession: the doctor's coat.", "method": "Singular owner -> 's. Plural ending in s -> s'. It's = it is only!", "trap": "Never use an apostrophe for simple plurals (apples, NOT apple's)!"},
        {"code": "W2", "strand": "FORMATS", "topic": "Leaflets & Information Guides", "q_title": "Visual Headings & Bullet Points", "color": (147, 51, 234), "num": 36, "example": "Engaging title, bold subheadings, bullet points, and contact info.", "method": "Keep language direct (imperative verbs) and easy to read quickly.", "trap": "Always include every key contact or venue detail required in the task."}
    ]
    render_fanned_cards_deck("english_l1", english_l1_topics, os.path.join(BOOKS_DIR, "flashcards_english_l1.png"), card_count=42)

    digital_skills_topics = [
        {"code": "S1", "strand": "SPREADSHEET", "topic": "Core Formulas (=SUM, =AVERAGE)", "q_title": "Basic Spreadsheet Calculations", "color": (194, 65, 12), "num": 8, "example": "=SUM(B2:B10) calculates total; =AVERAGE(B2:B10) calculates mean.", "method": "Always start every spreadsheet formula with an equals sign (=).", "trap": "Do not type numbers manually into formulas; always reference cell ranges!"},
        {"code": "SEC", "strand": "SECURITY", "topic": "Strong Passwords & 2FA", "q_title": "Protecting Accounts & Data", "color": (225, 29, 72), "num": 18, "example": "Combine 3 random words, numbers, symbols + enable SMS/App 2FA.", "method": "2FA requires 2 separate pieces of evidence (Password + Phone OTP).", "trap": "Never reuse the same password across multiple online accounts."},
        {"code": "C1", "strand": "COMMUNICATION", "topic": "Professional Workplace Email", "q_title": "Netiquette & Digital Etiquette", "color": (2, 132, 199), "num": 28, "example": "Use clear subject lines, correct salutation, and professional tone.", "method": "Proofread before sending and double-check recipient addresses.", "trap": "Never reply-all to company-wide messages unless strictly necessary!"},
        {"code": "F1", "strand": "FILES", "topic": "File Types & Cloud Storage", "q_title": "Organizing .xlsx, .pdf & .docx", "color": (22, 163, 74), "num": 40, "example": ".docx for documents, .xlsx for spreadsheets, .pdf for read-only.", "method": "Save files with descriptive names and version numbers in cloud folders.", "trap": "Remember that CSV files store raw text data and cannot save formulas!"}
    ]
    render_fanned_cards_deck("digital_skills", digital_skills_topics, os.path.join(BOOKS_DIR, "flashcards_digital_skills.png"), card_count=50)

    # 4. TWIN PACK CARDS BUNDLE
    render_twin_pack_cards(
        os.path.join(BOOKS_DIR, "flashcards_maths_l2.png"),
        os.path.join(BOOKS_DIR, "flashcards_english_l2.png"),
        os.path.join(BOOKS_DIR, "bundle_ultimate_l2.png")
    )

    # 5. SYMMETRICAL 5-MOCK EXAM FANS
    maths_mock_topics = [
        ("Numbers & Calculations", ["Place Value & Ordering", "Four Operations & Negatives", "Fractions of Amounts", "Percentages & Multipliers", "Ratio & Proportion"]),
        ("Measures, Shape & Space", ["Perimeter & Circumference", "Compound Area (Rectangles & Triangles)", "Prism & Cylinder Volume", "Metric & Imperial Conversions", "Scale Drawings & Plans"]),
        ("Handling Data & Probability", ["Mean, Median, Mode & Range", "Grouped Frequency Tables", "Scatter Graphs & Correlation", "Probability Scale & Trees", "Comparing Data Sets"]),
        ("Core Practice Exam (Non-Calc)", ["25% Non-Calculator Section A", "Rapid Mental Arithmetic", "Estimation & Rounding", "Units of Measure Checks", "Exam Trap Checkpoints"]),
        ("Full Practice Exam (Calculator)", ["75% Calculator Section B", "Multi-Step Real Life Problems", "Finances, Best Buys & Wages", "Check Answers & Inverse Ops", "Full Mark Scheme Rubrics"])
    ]
    render_fanned_mock_pack("Mathematics", "Level 2", maths_mock_topics, os.path.join(BOOKS_DIR, "3d_mock_pack_maths_l2.png"))

    english_mock_topics = [
        ("Reading Source Insert Booklet", ["Text A: Workplace Report & Policy", "Text B: Persuasive Campaign Article", "Text C: Online Public Review Forum", "Comparative Vocabulary", "Fact vs Opinion Contrasts"]),
        ("Reading Comprehension Exam", ["Retrieval & Direct Information", "Specialist Language & Vocabulary", "Organizational & Presentational Markers", "Author's Tone, Voice & Bias", "Cross-Text Comparative Matrix"]),
        ("Writing Task 1: Formal Letter", ["Formal Workplace Correspondence", "Sender & Recipient Address Formats", "Salutation & Sign-Off Conventions", "Purpose, Context & Professional Tone", "Logical Paragraph Sequencing"]),
        ("Writing Task 2: Persuasive Article", ["Engaging Headline & Strapline", "DAFOREST Rhetorical Devices", "Subheadings & Bulleted Structures", "Complex Sentence Formats", "Spelling, Punctuation & Grammar Check"]),
        ("Full Mark Scheme & Rubrics", ["11 Exemplar Benchmark Model Answers", "Examiner SPaG Grading Matrices", "Formatting Criteria Checklists", "Pass Mark Boundaries & Scaling", "Self-Assessment Diagnostic Review"])
    ]
    render_fanned_mock_pack("English", "Level 2", english_mock_topics, os.path.join(BOOKS_DIR, "3d_mock_pack_english_l2.png"))

    # 6. HERO SHOWCASE
    render_hero_showcase(os.path.join(BOOKS_DIR, "flashcards_hero_stack.png"))

    print("\nALL PFS-STYLE 3D IMAGES SUCCESSFULLY GENERATED AND SYNCED!")

if __name__ == "__main__":
    main()
