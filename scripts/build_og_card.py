#!/usr/bin/env python3
"""Generate the 1200x630 Master Functional Skills Open Graph social card."""

from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT_PATH = ROOT / "assets" / "img" / "mfs-og-card.png"
EMBLEM_PATH = ROOT / "assets" / "img" / "favicon-512x512.png"

FONT_TITLE = ROOT / "a4" / "fonts" / "Montserrat.ttf"
FONT_HEAD = ROOT / "a4" / "fonts" / "Lexend.ttf"
FONT_BODY = ROOT / "a4" / "fonts" / "OpenSans.ttf"

WIDTH = 1200
HEIGHT = 630


def load_font(path: Path, size: int, weight: str | None = None) -> ImageFont.FreeTypeFont:
    font = ImageFont.truetype(str(path), size=size)
    if weight:
        try:
            font.set_variation_by_name(weight)
        except Exception:
            pass
    return font


def draw_gradient_bg(img: Image.Image) -> None:
    """Paint the unified Dark Blue (#0a0f1d -> #0f172a) studio gradient with subtle sky glow."""
    px = img.load()
    r1, g1, b1 = 0x0A, 0x0F, 0x1D
    r2, g2, b2 = 0x0F, 0x17, 0x2A
    for y in range(HEIGHT):
        ty = y / (HEIGHT - 1)
        for x in range(WIDTH):
            tx = x / (WIDTH - 1)
            t = 0.55 * ty + 0.45 * tx
            r = r1 + (r2 - r1) * t
            g = g1 + (g2 - g1) * t
            b = b1 + (b2 - b1) * t

            # Soft radial sky-blue glow behind the emblem on the right
            dx = (x - 980) / 360.0
            dy = (y - 290) / 300.0
            dist2 = dx * dx + dy * dy
            if dist2 < 1.0:
                glow = (1.0 - dist2) ** 2
                r += 14 * glow
                g += 54 * glow
                b += 96 * glow

            px[x, y] = (
                max(0, min(255, int(r))),
                max(0, min(255, int(g))),
                max(0, min(255, int(b))),
            )


def wrap_lines(
    draw: ImageDraw.ImageDraw,
    text: str,
    font: ImageFont.FreeTypeFont,
    max_width: int,
) -> list[str]:
    words = text.split()
    lines: list[str] = []
    cur = ""
    for w in words:
        test = f"{cur} {w}".strip()
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] <= max_width or not cur:
            cur = test
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def check_bounds(
    bboxes: list[tuple[str, tuple[int, int, int, int]]],
    max_x: int = 1140,
    max_y: int = 600,
) -> None:
    for label, (x0, y0, x1, y1) in bboxes:
        if x0 < 0 or y0 < 0 or x1 > max_x or y1 > max_y:
            raise AssertionError(
                f"Text bounds overflow for '{label}': ({x0}, {y0}, {x1}, {y1}) exceeds (0, 0, {max_x}, {max_y})"
            )


def main() -> None:
    img = Image.new("RGB", (WIDTH, HEIGHT), "#0a0f1d")
    draw_gradient_bg(img)
    draw = ImageDraw.Draw(img, "RGBA")

    # Subtle grid accents on right half
    for gx in range(740, WIDTH, 48):
        draw.line([(gx, 0), (gx, HEIGHT)], fill=(56, 189, 248, 12), width=1)
    for gy in range(48, HEIGHT, 48):
        draw.line([(720, gy), (WIDTH, gy)], fill=(56, 189, 248, 12), width=1)

    # Crisp left #0284c7 accent bar + subtle top hairline
    draw.rectangle([0, 0, 14, HEIGHT], fill="#0284c7")
    draw.rectangle([14, 0, WIDTH, 4], fill=(56, 189, 248, 90))

    f_eyebrow = load_font(FONT_HEAD, 18, "Bold")
    f_h1 = load_font(FONT_TITLE, 60, "ExtraBold")
    f_sub = load_font(FONT_BODY, 25, "Regular")
    f_pill = load_font(FONT_HEAD, 19, "SemiBold")
    f_trust = load_font(FONT_HEAD, 19, "Medium")
    f_url = load_font(FONT_HEAD, 22, "Bold")
    f_badge = load_font(FONT_HEAD, 16, "SemiBold")

    recorded_bounds: list[tuple[str, tuple[int, int, int, int]]] = []

    left_x = 64
    max_text_w = 720

    # Eyebrow pill
    eyebrow_text = "OFQUAL-ALIGNED UK REVISION & EXAMS"
    eb = draw.textbbox((0, 0), eyebrow_text, font=f_eyebrow)
    eb_w = (eb[2] - eb[0]) + 34
    eb_h = 40
    eyebrow_y = 58
    draw.rounded_rectangle(
        [left_x, eyebrow_y, left_x + eb_w, eyebrow_y + eb_h],
        radius=20,
        fill=(2, 132, 199, 45),
        outline=(56, 189, 248, 180),
        width=2,
    )
    tx = left_x + 17
    ty = eyebrow_y + 9
    draw.text((tx, ty), eyebrow_text, font=f_eyebrow, fill="#38bdf8")
    recorded_bounds.append(("eyebrow", draw.textbbox((tx, ty), eyebrow_text, font=f_eyebrow)))

    # Headline (2 balanced lines so text stays crisp and left of emblem)
    h1_lines = ["Master Functional", "Skills"]
    y_cursor = 122
    for idx, line in enumerate(h1_lines):
        draw.text((left_x, y_cursor), line, font=f_h1, fill="#ffffff")
        recorded_bounds.append((f"h1_{idx}", draw.textbbox((left_x, y_cursor), line, font=f_h1)))
        y_cursor += 68

    # Subheadline
    sub_text = "Free Past Papers, Video Walkthroughs, Visual Revision & Onscreen Simulators"
    sub_lines = wrap_lines(draw, sub_text, f_sub, max_text_w)
    y_cursor += 12
    for idx, line in enumerate(sub_lines):
        draw.text((left_x, y_cursor), line, font=f_sub, fill="#cbd5e1")
        recorded_bounds.append((f"sub_{idx}", draw.textbbox((left_x, y_cursor), line, font=f_sub)))
        y_cursor += 36

    # Tier Pills Row
    tiers = [
        ("Entry Level 3", (13, 148, 136, 55), "#2dd4bf", (45, 212, 191, 180)),
        ("Level 1", (22, 163, 74, 55), "#4ade80", (74, 222, 128, 180)),
        ("Level 2", (217, 119, 6, 55), "#fbbf24", (251, 191, 36, 180)),
        ("Digital Skills", (2, 132, 199, 55), "#38bdf8", (56, 189, 248, 180)),
    ]
    pill_y = y_cursor + 24
    pill_x = left_x
    pill_h = 42
    for label, bg_rgba, text_hex, border_rgba in tiers:
        pb = draw.textbbox((0, 0), label, font=f_pill)
        pw = (pb[2] - pb[0]) + 32
        draw.rounded_rectangle(
            [pill_x, pill_y, pill_x + pw, pill_y + pill_h],
            radius=12,
            fill=bg_rgba,
            outline=border_rgba,
            width=2,
        )
        ptx = pill_x + 16
        pty = pill_y + 9
        draw.text((ptx, pty), label, font=f_pill, fill=text_hex)
        recorded_bounds.append((f"pill_{label}", draw.textbbox((ptx, pty), label, font=f_pill)))
        pill_x += pw + 14

    # Bottom divider + Multi-board trust strip + URL
    div_y = 492
    draw.line([(left_x, div_y), (WIDTH - 64, div_y)], fill=(148, 163, 184, 55), width=2)

    trust_text = "Open Awards  •  Edexcel  •  City & Guilds  •  AQA  •  NCFE  •  TQUK  •  NOCN"
    trust_y = 514
    draw.text((left_x, trust_y), trust_text, font=f_trust, fill="#e2e8f0")
    recorded_bounds.append(("trust_strip", draw.textbbox((left_x, trust_y), trust_text, font=f_trust)))

    url_text = "masterfunctionalskills.co.uk"
    url_y = 550
    draw.text((left_x, url_y), url_text, font=f_url, fill="#38bdf8")
    recorded_bounds.append(("url_footer", draw.textbbox((left_x, url_y), url_text, font=f_url)))

    # Right Emblem Card (cleanly bounded x=836..1136, y=104..444)
    card_x0, card_y0, card_x1, card_y1 = 836, 98, 1136, 444
    draw.rounded_rectangle(
        [card_x0, card_y0, card_x1, card_y1],
        radius=28,
        fill=(15, 23, 42, 235),
        outline=(56, 189, 248, 125),
        width=2,
    )

    emblem = Image.open(EMBLEM_PATH).convert("RGBA")
    emblem = emblem.resize((220, 220), Image.Resampling.LANCZOS)
    emb_x = card_x0 + (card_x1 - card_x0 - 220) // 2
    emb_y = card_y0 + 32
    img.paste(emblem, (emb_x, emb_y), emblem)

    # Re-acquire draw after paste
    draw = ImageDraw.Draw(img, "RGBA")
    cap_text = "MATHS  •  ENGLISH  •  DFS"
    cb = draw.textbbox((0, 0), cap_text, font=f_badge)
    cap_w = cb[2] - cb[0]
    cap_x = card_x0 + (card_x1 - card_x0 - cap_w) // 2
    cap_y = card_y0 + 276
    draw.text((cap_x, cap_y), cap_text, font=f_badge, fill="#94a3b8")
    recorded_bounds.append(("emblem_caption", draw.textbbox((cap_x, cap_y), cap_text, font=f_badge)))

    subcap_text = "332+ Guides  •  161 Videos"
    sb = draw.textbbox((0, 0), subcap_text, font=f_badge)
    subcap_w = sb[2] - sb[0]
    subcap_x = card_x0 + (card_x1 - card_x0 - subcap_w) // 2
    subcap_y = card_y0 + 306
    draw.text((subcap_x, subcap_y), subcap_text, font=f_badge, fill="#38bdf8")
    recorded_bounds.append(("emblem_subcaption", draw.textbbox((subcap_x, subcap_y), subcap_text, font=f_badge)))

    check_bounds(recorded_bounds, max_x=1140, max_y=600)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH, format="PNG", optimize=True)
    print(f"OG_CARD_WRITTEN={OUT_PATH} size={OUT_PATH.stat().st_size} dims={img.size} bounds_checked={len(recorded_bounds)}")


if __name__ == "__main__":
    main()
