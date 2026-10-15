import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

BOOKS_DIR = "/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk/assets/img/books"
PROJECT_BOOKS_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk/assets/img/books"

# Load the newly rendered 3d_level2_core (almost square-on, slim spine)
book_img = Image.open(os.path.join(BOOKS_DIR, "3d_level2_core.png")).convert("RGBA")
# Load the fanned revision cards
cards_img = Image.open(os.path.join(BOOKS_DIR, "flashcards_maths_l2.png")).convert("RGBA")

# Let's crop tight around non-empty pixels of book and cards so we have full control over sizing
def get_tight_bbox(img):
    alpha = img.split()[-1]
    # threshold
    bbox = alpha.getbbox()
    return img.crop(bbox)

book_tight = get_tight_bbox(book_img)
cards_tight = get_tight_bbox(cards_img)

print(f"Book tight size: {book_tight.size}")
print(f"Cards tight size: {cards_tight.size}")

# Target canvas: 920 x 700 (standard product image wrap ratio)
canvas_w, canvas_h = 920, 700
canvas = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))

# Make the book BIGGER like in the other book images:
# In standard book images, book height is ~680px.
# Here on 700px canvas, let book height be 620px! (Fills ~89% of height, standing tall and proud)
target_book_h = 620
target_book_w = int(book_tight.width * (target_book_h / float(book_tight.height)))
book_large = book_tight.resize((target_book_w, target_book_h), Image.Resampling.LANCZOS)

# Cards size:
# Cards should be nicely proportioned alongside the big book:
target_cards_w = 460
target_cards_h = int(cards_tight.height * (target_cards_w / float(cards_tight.width)))
cards_scaled = cards_tight.resize((target_cards_w, target_cards_h), Image.Resampling.LANCZOS)

# Position Book on the right, standing tall:
bx = canvas_w - target_book_w - 40 # ~440
by = (canvas_h - target_book_h) // 2 # ~40

# Position Cards on the left, slightly overlapping the bottom-left of the book:
cx = 30
cy = canvas_h - target_cards_h - 40 # ~250

# 1. Soft Floor Shadow beneath the entire group
shadow_mask = Image.new("L", (canvas_w, canvas_h), 0)
s_draw = ImageDraw.Draw(shadow_mask)
# Under book base
s_draw.ellipse([bx + 40, by + target_book_h - 25, bx + target_book_w + 20, by + target_book_h + 30], fill=160)
# Under cards base
s_draw.ellipse([cx + 30, cy + target_cards_h - 30, cx + target_cards_w - 20, cy + target_cards_h + 25], fill=150)
shadow_mask = shadow_mask.filter(ImageFilter.GaussianBlur(24))

canvas.paste(Image.new("RGBA", (canvas_w, canvas_h), (7, 13, 30, 85)), mask=shadow_mask)

# 2. Paste the BIG book
canvas.paste(book_large, (bx, by), book_large)

# 3. Soft cast shadow from cards onto the book
cards_cast_sh = Image.new("L", (canvas_w, canvas_h), 0)
cc_draw = ImageDraw.Draw(cards_cast_sh)
cc_draw.rounded_rectangle([cx + 40, cy + 30, cx + target_cards_w, cy + target_cards_h], radius=16, fill=130)
cards_cast_sh = cards_cast_sh.filter(ImageFilter.GaussianBlur(16))
canvas.paste(Image.new("RGBA", (canvas_w, canvas_h), (7, 13, 30, 75)), mask=cards_cast_sh)

# 4. Paste the cards in front
canvas.paste(cards_scaled, (cx, cy), cards_scaled)

out_nc = os.path.join(BOOKS_DIR, "flashcards_hero_stack.png")
out_pr = os.path.join(PROJECT_BOOKS_DIR, "flashcards_hero_stack.png")
canvas.save(out_nc, "PNG", optimize=True)
canvas.save(out_pr, "PNG", optimize=True)
print(f"Saved {out_nc} and synced to {out_pr}!")
