#!/usr/bin/env python3
"""
render_all_pfs_3d_books.py
Generates angled 3D standing book and deck mockups matching the exact 3/4 perspective
and visual layout of Pass Functional Skills shop.
"""

import os
import glob
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

BOOKS_DIR = "/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk/assets/img/books"

def find_perspective_coeffs(dst_pts, src_pts):
    """Calculates perspective transformation coefficients for PIL transform."""
    matrix = []
    for (x, y), (u, v) in zip(dst_pts, src_pts):
        matrix.append([x, y, 1, 0, 0, 0, -u*x, -u*y])
        matrix.append([0, 0, 0, x, y, 1, -v*x, -v*y])
    A = np.matrix(matrix, dtype=float)
    B = np.array(src_pts).reshape(8)
    res = np.dot(np.linalg.inv(A.T * A) * A.T, B)
    return np.array(res).reshape(8)

def render_3d_book_pfs(front_png_path, output_png_path):
    """
    Renders an upright, 3/4 angled standing 3D book mockup.
    Matches the Pass Functional Skills shop geometry:
    - Visible left spine in 3D perspective
    - Tilted front cover angled rightward
    - Visible top page edge
    - Soft ambient floor drop-shadow
    """
    if not os.path.exists(front_png_path):
        print(f"Warning: {front_png_path} not found.")
        return

    front = Image.open(front_png_path).convert("RGBA")
    fw, fh = front.size

    canvas_w, canvas_h = 600, 600
    canvas = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))

    # Coordinates calibrated from PFS shop book references:
    spine_top_left = (145, 115)
    spine_top_right = (182, 100)
    spine_bottom_left = (145, 480)
    spine_bottom_right = (182, 495)

    cover_top_left = spine_top_right
    cover_top_right = (490, 155)
    cover_bottom_left = spine_bottom_right
    cover_bottom_right = (490, 520)

    # 1. Floor Drop-Shadow
    shadow = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow)
    s_draw.polygon([
        (120, 485),
        (182, 502),
        (515, 528),
        (480, 560),
        (150, 535)
    ], fill=(15, 23, 42, 140))
    s_draw.ellipse([130, 500, 500, 550], fill=(15, 23, 42, 110))
    shadow = shadow.filter(ImageFilter.GaussianBlur(16))
    canvas.paste(shadow, (0, 0), shadow)

    # 2. Render Front Cover in Perspective
    dst_cover = [cover_top_left, cover_top_right, cover_bottom_right, cover_bottom_left]
    src_cover = [(0, 0), (fw, 0), (fw, fh), (0, fh)]
    coeffs_cover = find_perspective_coeffs(dst_cover, src_cover)
    cover_persp = front.transform((canvas_w, canvas_h), Image.Transform.PERSPECTIVE, coeffs_cover, Image.Resampling.BICUBIC)

    # 3. Soft Cover Sheen & Lighting Hinge
    sheen = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    sh_draw = ImageDraw.Draw(sheen)
    # Hinge shadow & highlight
    sh_draw.line([cover_top_left, cover_bottom_left], fill=(0, 0, 0, 85), width=3)
    sh_draw.line([(cover_top_left[0] + 3, cover_top_left[1] + 2), (cover_bottom_left[0] + 3, cover_bottom_left[1] + 2)], fill=(255, 255, 255, 75), width=2)
    # Subtle soft diagonal gradient gloss
    for i in range(15):
        alpha = int(35 * (1 - i / 15))
        p1 = (cover_top_left[0] + 20 + i*8, cover_top_left[1] + 8)
        p2 = (cover_bottom_left[0] + 20 + i*8, cover_bottom_left[1] + 8)
        sh_draw.line([p1, p2], fill=(255, 255, 255, alpha), width=3)

    # 4. Book Spine with Vertical Shading Gradient
    edge_sample = front.crop((0, 0, 10, fh)).resize((1, 1)).getpixel((0, 0))
    base_r, base_g, base_b = edge_sample[:3]

    spine_canvas = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    sp_strip_w = 60
    sp_strip = Image.new("RGBA", (sp_strip_w, fh), (base_r, base_g, base_b, 255))
    sp_draw = ImageDraw.Draw(sp_strip)
    for x in range(sp_strip_w):
        factor = 0.50 + 0.50 * (x / sp_strip_w)
        sp_draw.line([(x, 0), (x, fh)], fill=(int(base_r * factor), int(base_g * factor), int(base_b * factor), 255))
    sp_draw.line([(0, 0), (0, fh)], fill=(0, 0, 0, 110), width=2)
    sp_draw.line([(sp_strip_w - 1, 0), (sp_strip_w - 1, fh)], fill=(255, 255, 255, 60), width=1)

    dst_spine = [spine_top_left, spine_top_right, spine_bottom_right, spine_bottom_left]
    src_spine = [(0, 0), (sp_strip_w, 0), (sp_strip_w, fh), (0, fh)]
    coeffs_spine = find_perspective_coeffs(dst_spine, src_spine)
    spine_persp = sp_strip.transform((canvas_w, canvas_h), Image.Transform.PERSPECTIVE, coeffs_spine, Image.Resampling.BICUBIC)

    # 5. Top Page Ridge
    pages_top = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    pt_draw = ImageDraw.Draw(pages_top)
    pt_draw.polygon([
        spine_top_right,
        (spine_top_right[0] + 16, spine_top_right[1] - 8),
        (cover_top_right[0] - 8, cover_top_right[1] - 8),
        cover_top_right
    ], fill=(235, 235, 235, 245), outline=(190, 190, 190, 200))
    # Fine page line grooves
    for y_off in range(-7, -1, 2):
        pt_draw.line([
            (spine_top_right[0] + 16, spine_top_right[1] + y_off),
            (cover_top_right[0] - 8, cover_top_right[1] + y_off)
        ], fill=(215, 215, 215, 180))

    # Composite Layers
    canvas.paste(pages_top, (0, 0), pages_top)
    canvas.paste(spine_persp, (0, 0), spine_persp)
    canvas.paste(cover_persp, (0, 0), cover_persp)
    canvas.paste(sheen, (0, 0), sheen)

    canvas.save(output_png_path, "PNG", optimize=True)
    print(f"Generated PFS-Style 3D Book Mockup -> {output_png_path}")

def render_3d_deck_pfs(front_png_path, output_png_path):
    """
    Renders an angled stacked revision card deck (A6 cards in a 3D box stack).
    """
    if not os.path.exists(front_png_path):
        return

    front = Image.open(front_png_path).convert("RGBA")
    fw, fh = front.size

    canvas_w, canvas_h = 600, 600
    canvas = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))

    # Stack of cards: 4 stacked cards underneath + top hero card
    stack_count = 5
    card_w, card_h = 380, int(380 * (fh / fw))
    
    # Floor shadow
    shadow = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow)
    s_draw.ellipse([90, 480, 520, 540], fill=(15, 23, 42, 130))
    shadow = shadow.filter(ImageFilter.GaussianBlur(18))
    canvas.paste(shadow, (0, 0), shadow)

    # Render card stack
    front_resized = front.resize((card_w, card_h), Image.Resampling.LANCZOS)
    for i in range(stack_count - 1, -1, -1):
        offset_x = 100 + i * 8
        offset_y = 120 + (stack_count - 1 - i) * 12
        card_copy = front_resized.copy()
        if i > 0:
            # Darken under-cards
            dark = Image.new("RGBA", (card_w, card_h), (0, 0, 0, 40 + i * 15))
            card_copy = Image.alpha_composite(card_copy, dark)
        canvas.paste(card_copy, (offset_x, offset_y), card_copy)

    canvas.save(output_png_path, "PNG", optimize=True)
    print(f"Generated Deck Mockup -> {output_png_path}")

def main():
    print("=== Re-rendering All Shop Book Mockups into Pass Functional Skills 3D Style ===")
    
    # Book IDs
    book_ids = [
        "maths_e3_core",
        "english_e3_core",
        "maths_l1_core",
        "maths_l1_companion",
        "level1_core",
        "level1_companion",
        "maths_l2_core",
        "maths_l2_companion",
        "level2_core",
        "level2_companion",
        "digital_skills",
        "spag_mastery",
        "bksb_remediation",
        "mock_pack_maths_l2",
        "mock_pack_english_l2"
    ]

    for b_id in book_ids:
        front_png = os.path.join(BOOKS_DIR, f"{b_id}_cover_page-1.png")
        if not os.path.exists(front_png):
            # Try alternate naming
            matches = glob.glob(os.path.join(BOOKS_DIR, f"*{b_id}*page-1.png"))
            if matches:
                front_png = matches[0]

        output_png = os.path.join(BOOKS_DIR, f"3d_{b_id}.png")
        render_3d_book_pfs(front_png, output_png)

    # Multi-book bundles
    from PIL import Image
    bundles = [
        ("3d_bundle_writing_l2.png", ["3d_level2_core.png", "3d_level2_companion.png", "3d_spag_mastery.png"]),
        ("3d_bundle_ultimate_l2.png", ["3d_maths_l2_core.png", "3d_maths_l2_companion.png", "3d_level2_core.png", "3d_level2_companion.png"])
    ]
    for b_name, books in bundles:
        canvas_w, canvas_h = 1000, 750
        b_canvas = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
        spacing = 150
        for i, b in enumerate(books):
            b_path = os.path.join(BOOKS_DIR, b)
            if os.path.exists(b_path):
                im = Image.open(b_path).convert("RGBA")
                target_h = 580
                target_w = int(im.width * (target_h / im.height))
                im_res = im.resize((target_w, target_h), Image.Resampling.LANCZOS)
                b_canvas.paste(im_res, (70 + i * spacing, 80 + i * 10), im_res)
        out_b = os.path.join(BOOKS_DIR, b_name)
        b_canvas.save(out_b, "PNG", optimize=True)
        print(f"Generated Bundle Mockup -> {out_b}")

    print("\nALL 3D SHOP MOCKUPS SUCCESSFULLY RE-RENDERED IN PFS STYLE!")

if __name__ == "__main__":
    main()
