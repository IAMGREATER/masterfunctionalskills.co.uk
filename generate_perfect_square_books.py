import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

BOOKS_DIR = "/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk/assets/img/books"
PROJECT_BOOKS_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk/assets/img/books"

def find_perspective_coeffs(source_coords, target_coords):
    matrix = []
    for (s_x, s_y), (t_x, t_y) in zip(source_coords, target_coords):
        matrix.append([s_x, s_y, 1, 0, 0, 0, -t_x * s_x, -t_x * s_y])
        matrix.append([0, 0, 0, s_x, s_y, 1, -t_y * s_x, -t_y * s_y])
    A = np.matrix(matrix, dtype=float)
    B = np.array(target_coords).reshape(8)
    res = np.dot(np.linalg.inv(A.T * A) * A.T, B)
    return np.array(res).reshape(8)

def render_almost_square_book(cover_filename, out_filename, base_rgb=(2, 34, 76), accent_rgb=(245, 158, 11)):
    cover_path = os.path.join(BOOKS_DIR, cover_filename)
    if not os.path.exists(cover_path):
        print(f"Error: {cover_path} not found")
        return
        
    cover_img = Image.open(cover_path).convert("RGBA")
    cw, ch = cover_img.size

    canvas_w, canvas_h = 800, 800
    canvas = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))

    # Coordinates: Almost square-on, subtle standing 3D angle
    # Slim spine on the left (width 19px)
    s_tl = (196, 64)
    s_tr = (215, 58)
    s_br = (215, 742)
    s_bl = (196, 736)

    # Front cover: 98% rectangular, completely readable and crisp
    c_tl = s_tr # (215, 58)
    c_tr = (704, 70)
    c_br = (704, 730)
    c_bl = s_br # (215, 742)

    # Multi-layer Drop Shadow
    # 1. Ambient body shadow
    body_sh_mask = Image.new("L", (canvas_w, canvas_h), 0)
    b_draw = ImageDraw.Draw(body_sh_mask)
    b_draw.polygon([(s_tl[0]-8, s_tl[1]+10), (c_tr[0]+14, c_tr[1]+10), (c_br[0]+14, c_br[1]+16), (s_bl[0]-8, s_bl[1]+16)], fill=130)
    body_sh_mask = body_sh_mask.filter(ImageFilter.GaussianBlur(22))

    # 2. Floor contact shadow under base
    floor_sh_mask = Image.new("L", (canvas_w, canvas_h), 0)
    f_draw = ImageDraw.Draw(floor_sh_mask)
    f_draw.ellipse([180, 728, 725, 764], fill=160)
    f_draw.line([(200, 738), (704, 731)], fill=210, width=5)
    floor_sh_mask = floor_sh_mask.filter(ImageFilter.GaussianBlur(12))

    canvas.paste(Image.new("RGBA", (canvas_w, canvas_h), (7, 13, 30, 65)), mask=body_sh_mask)
    canvas.paste(Image.new("RGBA", (canvas_w, canvas_h), (7, 13, 30, 95)), mask=floor_sh_mask)

    # 3. Slim 3D Spine (19px wide)
    spine_canvas_w = 100
    spine_canvas_h = 1000
    spine_raw = Image.new("RGBA", (spine_canvas_w, spine_canvas_h), (0, 0, 0, 0))
    sp_draw = ImageDraw.Draw(spine_raw)

    for x in range(spine_canvas_w):
        ratio = x / float(spine_canvas_w)
        light_factor = 0.65 + 0.35 * np.sin(ratio * np.pi)
        r = int(base_rgb[0] * light_factor)
        g = int(base_rgb[1] * light_factor)
        b = int(base_rgb[2] * light_factor)
        sp_draw.line([(x, 0), (x, spine_canvas_h)], fill=(r, g, b, 255))

    if accent_rgb:
        sp_draw.rectangle([0, 30, spine_canvas_w, 70], fill=accent_rgb + (255,))

    s_coeffs = find_perspective_coeffs([s_tl, s_tr, s_br, s_bl], [(0,0), (spine_canvas_w,0), (spine_canvas_w,spine_canvas_h), (0,spine_canvas_h)])
    warped_spine = spine_raw.transform((canvas_w, canvas_h), Image.PERSPECTIVE, s_coeffs, Image.BICUBIC)
    canvas.alpha_composite(warped_spine)

    # 4. Front Cover
    c_coeffs = find_perspective_coeffs([c_tl, c_tr, c_br, c_bl], [(0,0), (cw,0), (cw,ch), (0,ch)])
    warped_cover = cover_img.transform((canvas_w, canvas_h), Image.PERSPECTIVE, c_coeffs, Image.BICUBIC)
    canvas.alpha_composite(warped_cover)

    # 5. Inner Crease & Highlight Line
    cr_layer = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    cr_draw = ImageDraw.Draw(cr_layer)
    cr_draw.line([(c_tl[0], c_tl[1]), (c_bl[0], c_bl[1])], fill=(255, 255, 255, 120), width=1)
    cr_draw.line([(c_tl[0]-1, c_tl[1]), (c_bl[0]-1, c_bl[1])], fill=(0, 0, 0, 70), width=1)
    canvas.alpha_composite(cr_layer)

    # Save to both directories
    p1 = os.path.join(BOOKS_DIR, out_filename)
    p2 = os.path.join(PROJECT_BOOKS_DIR, out_filename)
    canvas.save(p1, "PNG")
    canvas.save(p2, "PNG")
    print(f"Rendered: {out_filename}")

def render_double_bundle(cover1_fn, cover2_fn, out_filename):
    cover1 = Image.open(os.path.join(BOOKS_DIR, cover1_fn)).convert("RGBA")
    cover2 = Image.open(os.path.join(BOOKS_DIR, cover2_fn)).convert("RGBA")

    def render_sub_book(c_img, base_rgb, accent_rgb):
        canvas = Image.new("RGBA", (800, 800), (0, 0, 0, 0))
        cw, ch = c_img.size
        s_tl = (40, 50)
        s_tr = (55, 45)
        s_br = (55, 595)
        s_bl = (40, 590)

        c_tl = s_tr
        c_tr = (445, 55)
        c_br = (445, 585)
        c_bl = s_br

        spine_w = 100
        spine_h = 1000
        spine_raw = Image.new("RGBA", (spine_w, spine_h), (0, 0, 0, 0))
        sp_draw = ImageDraw.Draw(spine_raw)
        for x in range(spine_w):
            ratio = x / float(spine_w)
            light_factor = 0.65 + 0.35 * np.sin(ratio * np.pi)
            r = int(base_rgb[0] * light_factor)
            g = int(base_rgb[1] * light_factor)
            b = int(base_rgb[2] * light_factor)
            sp_draw.line([(x, 0), (x, spine_h)], fill=(r, g, b, 255))
        if accent_rgb:
            sp_draw.rectangle([0, 30, spine_w, 70], fill=accent_rgb + (255,))

        s_coeffs = find_perspective_coeffs([s_tl, s_tr, s_br, s_bl], [(0,0), (spine_w,0), (spine_w,spine_h), (0,spine_h)])
        warped_spine = spine_raw.transform((800, 800), Image.PERSPECTIVE, s_coeffs, Image.BICUBIC)
        canvas.alpha_composite(warped_spine)

        c_coeffs = find_perspective_coeffs([c_tl, c_tr, c_br, c_bl], [(0,0), (cw,0), (cw,ch), (0,ch)])
        warped_cover = c_img.transform((800, 800), Image.PERSPECTIVE, c_coeffs, Image.BICUBIC)
        canvas.alpha_composite(warped_cover)

        cr_draw = ImageDraw.Draw(canvas)
        cr_draw.line([(c_tl[0], c_tl[1]), (c_bl[0], c_bl[1])], fill=(255, 255, 255, 120), width=1)
        cr_draw.line([(c_tl[0]-1, c_tl[1]), (c_bl[0]-1, c_bl[1])], fill=(0, 0, 0, 70), width=1)

        return canvas.crop((35, 40, 455, 605))

    b_comp = render_sub_book(cover1, base_rgb=(235, 235, 235), accent_rgb=(2, 34, 76))
    b_core = render_sub_book(cover2, base_rgb=(2, 34, 76), accent_rgb=(245, 158, 11))

    canvas = Image.new("RGBA", (800, 800), (0, 0, 0, 0))

    pos_comp = (60, 110)
    pos_core = (320, 125)

    # Shadow for companion
    sh1 = Image.new("L", (800, 800), 0)
    ImageDraw.Draw(sh1).ellipse([pos_comp[0]-10, pos_comp[1]+b_comp.height-20, pos_comp[0]+b_comp.width+20, pos_comp[1]+b_comp.height+25], fill=140)
    sh1 = sh1.filter(ImageFilter.GaussianBlur(16))
    canvas.paste(Image.new("RGBA", (800, 800), (7, 13, 30, 70)), mask=sh1)
    canvas.paste(b_comp, pos_comp, b_comp)

    # Shadow for core book
    sh2 = Image.new("L", (800, 800), 0)
    s2_d = ImageDraw.Draw(sh2)
    s2_d.rounded_rectangle([pos_core[0]-10, pos_core[1]+10, pos_core[0]+b_core.width+15, pos_core[1]+b_core.height+15], radius=10, fill=130)
    s2_d.ellipse([pos_core[0]-15, pos_core[1]+b_core.height-20, pos_core[0]+b_core.width+25, pos_core[1]+b_core.height+25], fill=160)
    sh2 = sh2.filter(ImageFilter.GaussianBlur(16))
    canvas.paste(Image.new("RGBA", (800, 800), (7, 13, 30, 85)), mask=sh2)
    canvas.paste(b_core, pos_core, b_core)

    # Pill badge
    font_badge = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 16)
    badge_w, badge_h = 320, 42
    bx = (800 - badge_w) // 2
    by = 705

    b_draw = ImageDraw.Draw(canvas)
    b_draw.rounded_rectangle([bx, by, bx + badge_w, by + badge_h], radius=21, fill=(245, 158, 11, 255), outline=(255, 255, 255, 200), width=2)
    b_draw.text((bx + 26, by + 11), "COMPLETE 2-BOOK BUNDLE", fill=(7, 13, 30, 255), font=font_badge)

    p1 = os.path.join(BOOKS_DIR, out_filename)
    p2 = os.path.join(PROJECT_BOOKS_DIR, out_filename)
    canvas.save(p1, "PNG")
    canvas.save(p2, "PNG")
    print(f"Rendered Bundle: {out_filename}")

# Run generation for all 13 books
books_to_render = [
    # filename_cover, filename_out, base_rgb, accent_rgb
    ("level2_core_cover_page-1.png", "3d_level2_core.png", (2, 34, 76), (245, 158, 11)),
    ("level2_companion_cover_page-1.png", "3d_level2_companion.png", (230, 230, 230), (2, 34, 76)),
    ("level1_core_cover_page-1.png", "3d_level1_core.png", (4, 78, 56), (245, 158, 11)),
    ("level1_companion_cover_page-1.png", "3d_level1_companion.png", (230, 230, 230), (4, 78, 56)),
    ("spag_mastery_cover_page-1.png", "3d_spag_mastery.png", (65, 18, 92), (245, 158, 11)),
    ("maths_l2_core_cover_page-1.png", "3d_maths_l2_core.png", (2, 34, 76), (245, 158, 11)),
    ("maths_l2_companion_cover_page-1.png", "3d_maths_l2_companion.png", (230, 230, 230), (2, 34, 76)),
    ("maths_l1_core_cover_page-1.png", "3d_maths_l1_core.png", (4, 78, 56), (245, 158, 11)),
    ("maths_l1_companion_cover_page-1.png", "3d_maths_l1_companion.png", (230, 230, 230), (4, 78, 56)),
    ("maths_e3_core_cover_page-1.png", "3d_maths_e3_core.png", (140, 22, 22), (245, 158, 11)),
    ("english_e3_core_cover_page-1.png", "3d_english_e3_core.png", (140, 22, 22), (245, 158, 11)),
    ("digital_skills_cover_page-1.png", "3d_digital_skills.png", (15, 30, 50), (14, 165, 233)),
    ("bksb_remediation_cover_page-1.png", "3d_bksb_remediation.png", (18, 55, 120), (245, 158, 11)),
    ("mock_pack_maths_l2_cover_page-1.png", "3d_mock_pack_maths_l2.png", (30, 41, 59), (245, 158, 11)),
    ("mock_pack_english_l2_cover_page-1.png", "3d_mock_pack_english_l2.png", (30, 41, 59), (245, 158, 11)),
    ("spag_l2_mastery_cover-01.png", "3d_spag_l2_mastery.png", (0, 32, 70), (37, 99, 235)),
    ("spag_l1_mastery_cover-01.png", "3d_spag_l1_mastery.png", (12, 78, 69), (20, 184, 166)),
    ("spag_e3_mastery_cover-01.png", "3d_spag_e3_mastery.png", (136, 19, 55), (225, 29, 72)),
]

for c_fn, o_fn, brgb, argb in books_to_render:
    render_almost_square_book(c_fn, o_fn, brgb, argb)

# Double book bundle
render_double_bundle("level2_companion_cover_page-1.png", "level2_core_cover_page-1.png", "3d_bundle_writing_l2.png")

# Quad book ultimate bundle (square-on stacked)
def render_quad_bundle(out_filename):
    canvas = Image.new("RGBA", (1100, 800), (0, 0, 0, 0))
    books = [
        "3d_maths_l2_companion.png",
        "3d_maths_l2_core.png",
        "3d_level2_companion.png",
        "3d_level2_core.png"
    ]
    start_x = 30
    spacing = 140
    for i, b_fn in enumerate(books):
        b_path = os.path.join(BOOKS_DIR, b_fn)
        if not os.path.exists(b_path):
            continue
        b_img = Image.open(b_path).convert("RGBA")
        target_h = 700
        target_w = int(b_img.width * (target_h / b_img.height))
        b_resized = b_img.resize((target_w, target_h), Image.Resampling.LANCZOS)
        pos_x = start_x + (i * spacing)
        pos_y = 50 + (i * 10)
        
        # Shadow for each book
        sh = Image.new("L", (1100, 800), 0)
        ImageDraw.Draw(sh).ellipse([pos_x + 30, pos_y + target_h - 40, pos_x + target_w - 20, pos_y + target_h + 10], fill=120)
        sh = sh.filter(ImageFilter.GaussianBlur(16))
        canvas.paste(Image.new("RGBA", (1100, 800), (7, 13, 30, 60)), mask=sh)
        
        canvas.paste(b_resized, (pos_x, pos_y), b_resized)
        
    p1 = os.path.join(BOOKS_DIR, out_filename)
    p2 = os.path.join(PROJECT_BOOKS_DIR, out_filename)
    canvas.save(p1, "PNG")
    canvas.save(p2, "PNG")
    print(f"Rendered Quad Bundle: {out_filename}")

render_quad_bundle("3d_bundle_ultimate_l2.png")

print("ALL BOOKS RE-RENDERED ALMOST SQUARE-ON WITH SLIM SPINES!")
