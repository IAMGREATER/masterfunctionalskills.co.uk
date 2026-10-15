#!/usr/bin/env python3
"""
Master Functional Skills - Automated YouTube Video Solution Generator
Generates high-definition (1080p 16:9) video walkthroughs with British Neural Voice narration,
step-by-step Pearson Edexcel method marks [M1/A1], examiner trap alerts, and final answer reveals.
"""

import os
import subprocess
import json
import time
from PIL import Image, ImageDraw, ImageFont

VID_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk/videos"
os.makedirs(VID_DIR, exist_ok=True)

FONT_BOLD = "/usr/share/fonts/liberation/LiberationSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/liberation/LiberationSans-Regular.ttf"
FONT_ITALIC = "/usr/share/fonts/liberation/LiberationSans-Italic.ttf"

W, H = 1920, 1080

def get_font(path, size):
    return ImageFont.truetype(path, size)

def generate_voiceover(text, output_path, voice="bm_george"):
    print(f"Generating Kokoro Neural narration ({voice}) for {os.path.basename(output_path)}...")
    if os.path.exists(output_path):
        os.remove(output_path)
    wav_tmp = output_path.replace(".mp3", ".wav")
    if os.path.exists(wav_tmp):
        os.remove(wav_tmp)

    cmd_kokoro = [
        "uvx", "kokoro",
        "-m", voice,
        "-l", "b",
        "-o", wav_tmp,
        "-t", text
    ]
    subprocess.run(cmd_kokoro, check=True)

    # Broadcast standard EBU R128 loudness normalization
    cmd_ffmpeg = [
        "ffmpeg", "-y",
        "-i", wav_tmp,
        "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
        "-c:a", "libmp3lame", "-b:a", "192k",
        output_path
    ]
    subprocess.run(cmd_ffmpeg, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

    if os.path.exists(wav_tmp):
        os.remove(wav_tmp)
    return True

def draw_header_and_footer(draw, topic_name="Numbers & Place Value"):
    # Header Background
    draw.rectangle([0, 0, W, 100], fill="#070e1e")
    draw.line([0, 100, W, 100], fill="#2563eb", width=3)
    
    # Logo
    f_logo_m = get_font(FONT_BOLD, 30)
    f_logo_fs = get_font(FONT_BOLD, 30)
    draw.text((60, 32), "MASTER ", font=f_logo_m, fill="#ffffff")
    draw.text((200, 32), "FUNCTIONAL SKILLS", font=f_logo_fs, fill="#38bdf8")
    
    # Qualification Pill
    f_pill = get_font(FONT_BOLD, 16)
    draw.rounded_rectangle([1380, 28, 1860, 72], radius=12, fill="#1e293b", outline="#3b82f6", width=2)
    draw.text((1405, 38), "PEARSON EDEXCEL • LEVEL 1 & LEVEL 2", font=f_pill, fill="#93c5fd")
    
    # Footer Background
    draw.rectangle([0, H - 70, W, H], fill="#070e1e")
    draw.line([0, H - 70, W, H - 70], fill="#1e293b", width=2)
    
    f_foot = get_font(FONT_REG, 20)
    f_foot_b = get_font(FONT_BOLD, 20)
    draw.text((60, H - 48), "Your Functional Skills Tutor", font=f_foot_b, fill="#38bdf8")
    
    draw.text((760, H - 48), f"Topic: {topic_name} • Full Worked Solutions", font=f_foot, fill="#cbd5e1")
    
    draw.text((1540, H - 48), "masterfunctionalskills.co.uk", font=f_foot_b, fill="#38bdf8")

# -------------------------------------------------------------
# SLIDE 1: TITLE SLIDE
# -------------------------------------------------------------
def make_slide_title(filename):
    img = Image.new("RGB", (W, H), color="#091124")
    draw = ImageDraw.Draw(img)
    draw_header_and_footer(draw)
    
    draw.rounded_rectangle([160, 150, W - 160, H - 120], radius=24, fill="#0f172a", outline="#1e3a8a", width=3)
    
    f_badge = get_font(FONT_BOLD, 22)
    draw.rounded_rectangle([720, 200, 1200, 250], radius=15, fill="#1e3a8a", outline="#60a5fa", width=2)
    draw.text((750, 212), "OFFICIAL VIDEO SOLUTION", font=f_badge, fill="#60a5fa")
    
    f_main = get_font(FONT_BOLD, 68)
    f_sub = get_font(FONT_REG, 32)
    draw.text((540, 290), "Numbers & Place Value", font=f_main, fill="#ffffff")
    draw.text((460, 390), "Pearson Edexcel Functional Skills Mathematics (Level 1 & Level 2)", font=f_sub, fill="#93c5fd")
    
    # 3 Features Cards
    f_card_t = get_font(FONT_BOLD, 24)
    f_card_b = get_font(FONT_REG, 20)
    
    draw.rounded_rectangle([220, 480, 680, 750], radius=16, fill="#1e293b", outline="#334155", width=2)
    draw.text((250, 510), "🎯 Method Mark Breakdown", font=f_card_t, fill="#38bdf8")
    draw.text((250, 560), "Every step tagged with M1\nand A1 mark allocations\naccording to Pearson criteria.", font=f_card_b, fill="#cbd5e1")
    
    draw.rounded_rectangle([730, 480, 1190, 750], radius=16, fill="#1e293b", outline="#334155", width=2)
    draw.text((760, 510), "⚠️ Examiner Trap Alerts", font=f_card_t, fill="#f59e0b")
    draw.text((760, 560), "Highlight common pitfalls\nincluding placeholder zeros\nand column misalignment.", font=f_card_b, fill="#cbd5e1")
    
    draw.rounded_rectangle([1240, 480, 1700, 750], radius=16, fill="#1e293b", outline="#334155", width=2)
    draw.text((1270, 510), "🔄 Reverse Sanity Checks", font=f_card_t, fill="#10b981")
    draw.text((1270, 560), "Tutor proofing methods\nto verify calculation accuracy\nand guarantee exam marks.", font=f_card_b, fill="#cbd5e1")
    
    f_pres = get_font(FONT_BOLD, 26)
    draw.text((740, 810), "Official Step-by-Step Model Solutions", font=f_pres, fill="#f8fafc")
    
    img.save(filename)
    print(f"Generated {filename}")

# -------------------------------------------------------------
# SLIDE 2: EXAMINER GOLDEN RULE
# -------------------------------------------------------------
def make_slide_rule(filename):
    img = Image.new("RGB", (W, H), color="#091124")
    draw = ImageDraw.Draw(img)
    draw_header_and_footer(draw)
    
    draw.rounded_rectangle([120, 130, W - 120, H - 100], radius=20, fill="#0f172a", outline="#d97706", width=3)
    
    f_sec = get_font(FONT_BOLD, 20)
    draw.rounded_rectangle([160, 160, 480, 205], radius=10, fill="#78350f", outline="#f59e0b", width=2)
    draw.text((180, 172), "EXAMINER GOLDEN RULE", font=f_sec, fill="#fde68a")
    
    f_h1 = get_font(FONT_BOLD, 42)
    draw.text((160, 225), "Place Value Columns & Placeholder Zeros", font=f_h1, fill="#ffffff")
    
    columns = [
        ("M", "Millions", "1,000,000"),
        ("HTh", "Hundred Th", "100,000"),
        ("TTh", "Ten Th", "10,000"),
        ("Th", "Thousands", "1,000"),
        ("H", "Hundreds", "100"),
        ("T", "Tens", "10"),
        ("U", "Units", "1"),
        ("t", "tenths", "0.1"),
        ("h", "hundredths", "0.01"),
    ]
    
    start_x = 160
    col_w = 175
    y_top = 300
    
    f_c_abbr = get_font(FONT_BOLD, 28)
    f_c_name = get_font(FONT_BOLD, 17)
    f_c_val = get_font(FONT_REG, 15)
    
    for i, (abbr, name, val) in enumerate(columns):
        cx = start_x + i * col_w
        bg = "#1e3a8a" if "Th" in abbr or abbr == "M" else "#1e293b" if abbr in ["H","T","U"] else "#374151"
        draw.rounded_rectangle([cx, y_top, cx + col_w - 10, y_top + 150], radius=10, fill=bg, outline="#475569", width=2)
        draw.text((cx + 15, y_top + 15), abbr, font=f_c_abbr, fill="#38bdf8")
        draw.text((cx + 15, y_top + 60), name, font=f_c_name, fill="#ffffff")
        draw.text((cx + 15, y_top + 105), val, font=f_c_val, fill="#94a3b8")
        
    f_rule_t = get_font(FONT_BOLD, 24)
    f_rule_b = get_font(FONT_REG, 21)
    
    draw.rounded_rectangle([160, 490, 930, 720], radius=14, fill="#1e293b", outline="#2563eb", width=2)
    draw.text((190, 520), "1. Grouping Digits by Threes", font=f_rule_t, fill="#60a5fa")
    draw.text((190, 570), "• Count 3 digits from right to left before comma.\n• Example: 2,045,608 (never 20,45608).\n• Spaces or commas are accepted by Pearson.", font=f_rule_b, fill="#e2e8f0")
    
    draw.rounded_rectangle([970, 490, 1740, 720], radius=14, fill="#1e293b", outline="#f59e0b", width=2)
    draw.text((1000, 520), "2. The Zero Placeholder Trap", font=f_rule_t, fill="#fbbf24")
    draw.text((1000, 570), "• If a place value column is empty, write 0.\n• 'Forty-five thousand' means ZERO hundred-thousands:\n  045,000 (Omission turns 2,045,608 into 245,608!).", font=f_rule_b, fill="#e2e8f0")
    
    draw.rounded_rectangle([160, 755, 1740, 835], radius=12, fill="#14532d", outline="#22c55e", width=2)
    f_tip = get_font(FONT_BOLD, 21)
    draw.text((190, 780), "💡 Examiner Pro Tip: Always state the actual value for digit value questions (e.g. 30,000), not just the column name.", font=f_tip, fill="#bbf7d0")

    img.save(filename)
    print(f"Generated {filename}")

# -------------------------------------------------------------
# SLIDE 3: QUESTION 1
# -------------------------------------------------------------
def make_slide_q1(filename):
    img = Image.new("RGB", (W, H), color="#091124")
    draw = ImageDraw.Draw(img)
    draw_header_and_footer(draw)
    
    draw.rounded_rectangle([120, 130, W - 120, H - 100], radius=20, fill="#0f172a", outline="#2563eb", width=3)
    
    f_qhead = get_font(FONT_BOLD, 28)
    draw.text((160, 160), "Question 1 • Procedural Fluency Check", font=f_qhead, fill="#38bdf8")
    
    draw.rounded_rectangle([1620, 155, 1740, 200], radius=10, fill="#1e3a8a", outline="#60a5fa", width=2)
    f_marks = get_font(FONT_BOLD, 22)
    draw.text((1635, 165), "[2 Marks]", font=f_marks, fill="#93c5fd")
    
    draw.rounded_rectangle([160, 220, 1740, 310], radius=12, fill="#1e293b", outline="#334155", width=2)
    f_stem = get_font(FONT_REG, 25)
    draw.text((185, 245), "Write the number two million, forty-five thousand, six hundred and eight in figures.", font=f_stem, fill="#ffffff")
    
    draw.rounded_rectangle([160, 335, 1740, 440], radius=12, fill="#111827", outline="#3b82f6", width=2)
    f_step_num = get_font(FONT_BOLD, 22)
    f_step_txt = get_font(FONT_REG, 21)
    draw.text((185, 355), "Step 1: Partition into Period Columns", font=f_step_num, fill="#60a5fa")
    draw.text((185, 390), "• Millions period: 2 million = 2,000,000\n• Thousands period: 'forty-five thousand' = 045,000 (0 in Hundred-Thousands column)", font=f_step_txt, fill="#e2e8f0")
    
    draw.rounded_rectangle([1620, 360, 1715, 410], radius=8, fill="#1e3a8a", outline="#38bdf8", width=2)
    f_badge = get_font(FONT_BOLD, 20)
    draw.text((1640, 373), "[M1]", font=f_badge, fill="#38bdf8")
    
    draw.rounded_rectangle([160, 465, 1740, 570], radius=12, fill="#111827", outline="#10b981", width=2)
    draw.text((185, 485), "Step 2: Append Units Period & Combine", font=f_step_num, fill="#34d399")
    draw.text((185, 520), "• Units period: 'six hundred and eight' = 608 (0 in Tens column)\n• Combined: 2,000,000 + 45,000 + 608 = 2,045,608", font=f_step_txt, fill="#e2e8f0")
    
    draw.rounded_rectangle([1620, 490, 1715, 540], radius=8, fill="#065f46", outline="#10b981", width=2)
    draw.text((1640, 503), "[A1]", font=f_badge, fill="#34d399")
    
    draw.rounded_rectangle([160, 595, 1050, 695], radius=12, fill="#422006", outline="#eab308", width=3)
    f_ans_lbl = get_font(FONT_BOLD, 24)
    f_ans_val = get_font(FONT_BOLD, 42)
    draw.text((190, 625), "Final Award Answer:", font=f_ans_lbl, fill="#fde047")
    draw.text((500, 615), "2,045,608", font=f_ans_val, fill="#ffffff")
    
    draw.rounded_rectangle([160, 720, 1740, 835], radius=12, fill="#450a0a", outline="#ef4444", width=2)
    f_trap_h = get_font(FONT_BOLD, 22)
    f_trap_b = get_font(FONT_REG, 20)
    draw.text((185, 740), "⚠️ EXAMINER TRAP ALERT:", font=f_trap_h, fill="#fca5a5")
    draw.text((185, 775), "Candidates frequently omit the placeholder zero in hundred-thousands, incorrectly writing 2,45,608 or 245,608.\nAlways verify that there are exactly 6 digits following the millions digit!", font=f_trap_b, fill="#fecaca")

    img.save(filename)
    print(f"Generated {filename}")

# -------------------------------------------------------------
# SLIDE 4: QUESTION 2
# -------------------------------------------------------------
def make_slide_q2(filename):
    img = Image.new("RGB", (W, H), color="#091124")
    draw = ImageDraw.Draw(img)
    draw_header_and_footer(draw)
    
    draw.rounded_rectangle([120, 130, W - 120, H - 100], radius=20, fill="#0f172a", outline="#2563eb", width=3)
    
    f_qhead = get_font(FONT_BOLD, 28)
    draw.text((160, 160), "Question 2 • Digit Value Identification", font=f_qhead, fill="#38bdf8")
    
    draw.rounded_rectangle([1620, 155, 1740, 200], radius=10, fill="#1e3a8a", outline="#60a5fa", width=2)
    f_marks = get_font(FONT_BOLD, 22)
    draw.text((1635, 165), "[2 Marks]", font=f_marks, fill="#93c5fd")
    
    draw.rounded_rectangle([160, 220, 1740, 310], radius=12, fill="#1e293b", outline="#334155", width=2)
    f_stem = get_font(FONT_REG, 25)
    draw.text((185, 245), "In the number 4,839,271, state the value of the digit 3 both in words and as a number.", font=f_stem, fill="#ffffff")
    
    draw.rounded_rectangle([160, 335, 1740, 440], radius=12, fill="#111827", outline="#3b82f6", width=2)
    f_step_num = get_font(FONT_BOLD, 22)
    f_step_txt = get_font(FONT_REG, 21)
    draw.text((185, 355), "Step 1: Column Analysis for Digit 3", font=f_step_num, fill="#60a5fa")
    draw.text((185, 390), "• 4 [M] , 8 [HTh] , 3 [TTh] , 9 [Th] , 2 [H] , 7 [T] , 1 [U]\n• Digit 3 is located in the Ten-Thousands column.", font=f_step_txt, fill="#e2e8f0")
    
    draw.rounded_rectangle([1620, 360, 1715, 410], radius=8, fill="#1e3a8a", outline="#38bdf8", width=2)
    f_badge = get_font(FONT_BOLD, 20)
    draw.text((1640, 373), "[M1]", font=f_badge, fill="#38bdf8")
    
    draw.rounded_rectangle([160, 465, 1740, 570], radius=12, fill="#111827", outline="#10b981", width=2)
    draw.text((185, 485), "Step 2: Express Value in Figures and Words", font=f_step_num, fill="#34d399")
    draw.text((185, 520), "• As a number: 3 × 10,000 = 30,000\n• In words: Thirty Thousand (Both formats required by question).", font=f_step_txt, fill="#e2e8f0")
    
    draw.rounded_rectangle([1620, 490, 1715, 540], radius=8, fill="#065f46", outline="#10b981", width=2)
    draw.text((1640, 503), "[A1]", font=f_badge, fill="#34d399")
    
    draw.rounded_rectangle([160, 595, 1150, 695], radius=12, fill="#422006", outline="#eab308", width=3)
    f_ans_lbl = get_font(FONT_BOLD, 24)
    f_ans_val = get_font(FONT_BOLD, 36)
    draw.text((190, 627), "Award Final Answer:", font=f_ans_lbl, fill="#fde047")
    draw.text((500, 623), "30,000 (Thirty Thousand)", font=f_ans_val, fill="#ffffff")
    
    draw.rounded_rectangle([160, 720, 1740, 835], radius=12, fill="#064e3b", outline="#10b981", width=2)
    f_chk_h = get_font(FONT_BOLD, 22)
    f_chk_b = get_font(FONT_REG, 20)
    draw.text((185, 740), "🔄 REVERSE SANITY CHECK & CRITERIA WARNING:", font=f_chk_h, fill="#a7f3d0")
    draw.text((185, 775), "• Writing just 'ten-thousands' identifies the position, NOT the value (Scores 0 for A1).\n• Check: 30,000 + 4,800,000 + 9,000 + 200 + 70 + 1 = 4,839,271. Confirmed!", font=f_chk_b, fill="#d1fae5")

    img.save(filename)
    print(f"Generated {filename}")

# -------------------------------------------------------------
# SLIDE 5: QUESTION 3 WORKPLACE SCENARIO
# -------------------------------------------------------------
def make_slide_q3(filename):
    img = Image.new("RGB", (W, H), color="#091124")
    draw = ImageDraw.Draw(img)
    draw_header_and_footer(draw)
    
    draw.rounded_rectangle([120, 130, W - 120, H - 100], radius=20, fill="#0f172a", outline="#2563eb", width=3)
    
    f_qhead = get_font(FONT_BOLD, 28)
    draw.text((160, 160), "Question 3 • NHS Workplace Stock Audit (Ordering Numbers)", font=f_qhead, fill="#38bdf8")
    
    draw.rounded_rectangle([1620, 155, 1740, 200], radius=10, fill="#1e3a8a", outline="#60a5fa", width=2)
    f_marks = get_font(FONT_BOLD, 22)
    draw.text((1635, 165), "[3 Marks]", font=f_marks, fill="#93c5fd")
    
    draw.rounded_rectangle([160, 220, 1740, 325], radius=12, fill="#1e293b", outline="#334155", width=2)
    f_stem = get_font(FONT_REG, 23)
    stem_txt = ("An NHS central distribution warehouse holds regional medical mask stocks:\n"
                "• Depot A: 340,500    • Depot B: 304,850    • Depot C: 345,000    • Depot D: 340,095\n"
                "Write these depot stock figures in order of size, starting with the smallest stock quantity.")
    draw.text((185, 235), stem_txt, font=f_stem, fill="#ffffff")
    
    draw.rounded_rectangle([160, 350, 1740, 450], radius=12, fill="#111827", outline="#3b82f6", width=2)
    f_step_num = get_font(FONT_BOLD, 22)
    f_step_txt = get_font(FONT_REG, 21)
    draw.text((185, 370), "Step 1: Compare Highest Columns (Hundred-Thousands & Ten-Thousands)", font=f_step_num, fill="#60a5fa")
    draw.text((185, 403), "• All depots begin with 3 in Hundred-Thousands (300,000).\n• Compare Ten-Thousands: Depot B has 0 in Ten-Thousands (304,850) -> Smallest!", font=f_step_txt, fill="#e2e8f0")
    
    draw.rounded_rectangle([1620, 375, 1715, 425], radius=8, fill="#1e3a8a", outline="#38bdf8", width=2)
    f_badge = get_font(FONT_BOLD, 20)
    draw.text((1640, 388), "[P1]", font=f_badge, fill="#38bdf8")
    
    draw.rounded_rectangle([160, 475, 1740, 580], radius=12, fill="#111827", outline="#3b82f6", width=2)
    draw.text((185, 495), "Step 2: Compare Remaining Depots (Depots A, C, and D)", font=f_step_num, fill="#60a5fa")
    draw.text((185, 530), "• Depot C has 5 in Thousands (345,000) -> Largest of all.\n• Compare Depot D (340,095) vs Depot A (340,500): 0 hundreds < 5 hundreds.", font=f_step_txt, fill="#e2e8f0")
    
    draw.rounded_rectangle([1620, 500, 1715, 550], radius=8, fill="#1e3a8a", outline="#38bdf8", width=2)
    draw.text((1640, 513), "[P1]", font=f_badge, fill="#38bdf8")
    
    draw.rounded_rectangle([160, 605, 1550, 710], radius=12, fill="#422006", outline="#eab308", width=3)
    f_ans_lbl = get_font(FONT_BOLD, 24)
    f_ans_val = get_font(FONT_BOLD, 36)
    draw.text((190, 640), "Ordered Figures:", font=f_ans_lbl, fill="#fde047")
    draw.text((430, 635), "304,850  <  340,095  <  340,500  <  345,000", font=f_ans_val, fill="#ffffff")
    
    draw.rounded_rectangle([1620, 630, 1715, 680], radius=8, fill="#065f46", outline="#10b981", width=2)
    draw.text((1640, 643), "[A1]", font=f_badge, fill="#34d399")
    
    draw.rounded_rectangle([160, 735, 1740, 835], radius=12, fill="#064e3b", outline="#10b981", width=2)
    f_chk_h = get_font(FONT_BOLD, 22)
    f_chk_b = get_font(FONT_REG, 20)
    draw.text((185, 755), "🔄 REVERSE DESCENDING CHECK:", font=f_chk_h, fill="#a7f3d0")
    draw.text((185, 790), "• Check largest to smallest: 345,000 > 340,500 > 340,095 > 304,850.\n• All inequalities hold true across every regional depot. 3/3 Marks secured!", font=f_chk_b, fill="#d1fae5")

    img.save(filename)
    print(f"Generated {filename}")

# -------------------------------------------------------------
# SLIDE 6: OUTRO
# -------------------------------------------------------------
def make_slide_outro(filename):
    img = Image.new("RGB", (W, H), color="#091124")
    draw = ImageDraw.Draw(img)
    draw_header_and_footer(draw)
    
    draw.rounded_rectangle([160, 150, W - 160, H - 120], radius=24, fill="#0f172a", outline="#1e3a8a", width=3)
    
    f_badge = get_font(FONT_BOLD, 22)
    draw.rounded_rectangle([700, 200, 1220, 250], radius=15, fill="#166534", outline="#22c55e", width=2)
    draw.text((730, 212), "FREE REVISION RESOURCES", font=f_badge, fill="#86efac")
    
    f_main = get_font(FONT_BOLD, 54)
    draw.text((450, 290), "Practice Makes Perfect in Functional Skills", font=f_main, fill="#ffffff")
    
    f_sub = get_font(FONT_REG, 28)
    draw.text((360, 380), "Download the free practice worksheet and official tutor mark scheme for this topic:", font=f_sub, fill="#93c5fd")
    
    draw.rounded_rectangle([320, 460, 1600, 580], radius=18, fill="#1e293b", outline="#38bdf8", width=3)
    f_url = get_font(FONT_BOLD, 46)
    draw.text((500, 495), "🌐 masterfunctionalskills.co.uk", font=f_url, fill="#38bdf8")
    
    f_b_txt = get_font(FONT_BOLD, 22)
    draw.rounded_rectangle([250, 630, 680, 710], radius=12, fill="#1e293b", outline="#3b82f6", width=2)
    draw.text((280, 655), "✓ Printable A4 Worksheets", font=f_b_txt, fill="#ffffff")
    
    draw.rounded_rectangle([740, 630, 1180, 710], radius=12, fill="#1e293b", outline="#10b981", width=2)
    draw.text((770, 655), "✓ Complete Worked Schemes", font=f_b_txt, fill="#ffffff")
    
    draw.rounded_rectangle([1240, 630, 1670, 710], radius=12, fill="#1e293b", outline="#f59e0b", width=2)
    draw.text((1270, 655), "✓ 100% Original Curriculum", font=f_b_txt, fill="#ffffff")
    
    f_sub_cta = get_font(FONT_BOLD, 30)
    draw.text((640, 780), "🔔 Like & Subscribe for Full Topic Walkthroughs!", font=f_sub_cta, fill="#f59e0b")

    img.save(filename)
    print(f"Generated {filename}")

# -------------------------------------------------------------
# YOUTUBE THUMBNAIL (1280x720)
# -------------------------------------------------------------
def make_thumbnail(filename):
    TW, TH = 1280, 720
    img = Image.new("RGB", (TW, TH), color="#070e1e")
    draw = ImageDraw.Draw(img)
    
    # Outer Border Glow
    draw.rectangle([0, 0, TW, TH], outline="#2563eb", width=6)
    
    # Header Mini
    draw.rectangle([0, 0, TW, 70], fill="#0b172d")
    draw.line([0, 70, TW, 70], fill="#3b82f6", width=2)
    f_t_logo = get_font(FONT_BOLD, 24)
    draw.text((40, 20), "MASTER FUNCTIONAL SKILLS", font=f_t_logo, fill="#38bdf8")
    
    # Pill
    f_t_pill = get_font(FONT_BOLD, 18)
    draw.rounded_rectangle([880, 15, 1240, 55], radius=10, fill="#1e293b", outline="#60a5fa", width=2)
    draw.text((900, 24), "EDEXCEL LEVEL 1 & 2", font=f_t_pill, fill="#93c5fd")
    
    # Big Title
    f_t_h1 = get_font(FONT_BOLD, 64)
    draw.text((50, 120), "NUMBERS &", font=f_t_h1, fill="#ffffff")
    draw.text((50, 200), "PLACE VALUE", font=f_t_h1, fill="#38bdf8")
    
    # Walkthrough Banner
    f_t_ban = get_font(FONT_BOLD, 36)
    draw.rounded_rectangle([50, 310, 720, 385], radius=12, fill="#dc2626", outline="#ef4444", width=2)
    draw.text((75, 328), "▶ FULL WORKED SOLUTIONS", font=f_t_ban, fill="#ffffff")
    
    # Right Side Graphic Box (Problem & Answer)
    draw.rounded_rectangle([750, 110, 1230, 660], radius=18, fill="#0f172a", outline="#3b82f6", width=3)
    
    f_box_t = get_font(FONT_BOLD, 22)
    draw.text((780, 140), "Avoid The #1 Zero Trap!", font=f_box_t, fill="#f59e0b")
    
    f_box_q = get_font(FONT_REG, 20)
    draw.text((780, 185), "'Two million, forty-five\nthousand, six hundred & eight'", font=f_box_q, fill="#cbd5e1")
    
    # Big Answer Badge
    draw.rounded_rectangle([780, 270, 1200, 380], radius=12, fill="#422006", outline="#eab308", width=3)
    f_ans_l = get_font(FONT_BOLD, 18)
    f_ans_v = get_font(FONT_BOLD, 46)
    draw.text((800, 285), "CORRECT FINAL ANSWER:", font=f_ans_l, fill="#fde047")
    draw.text((830, 315), "2,045,608", font=f_ans_v, fill="#ffffff")
    
    # Badges
    f_b_sub = get_font(FONT_BOLD, 18)
    draw.rounded_rectangle([780, 410, 1200, 465], radius=8, fill="#1e293b", outline="#10b981", width=2)
    draw.text((800, 425), "✓ Full Method Marks [M1 / A1]", font=f_b_sub, fill="#a7f3d0")
    
    draw.rounded_rectangle([780, 485, 1200, 540], radius=8, fill="#1e293b", outline="#3b82f6", width=2)
    draw.text((800, 500), "✓ Workplace Scenario Solved", font=f_b_sub, fill="#93c5fd")
    
    draw.rounded_rectangle([780, 560, 1200, 615], radius=8, fill="#1e293b", outline="#f59e0b", width=2)
    draw.text((800, 575), "✓ Step-by-Step Examiner Guide", font=f_b_sub, fill="#fde68a")
    
    # Left Bottom Badges
    f_lb = get_font(FONT_BOLD, 26)
    draw.text((50, 430), "• Step-by-Step Mark Breakdown", font=f_lb, fill="#ffffff")
    draw.text((50, 480), "• Examiner Pitfalls & Traps", font=f_lb, fill="#ffffff")
    draw.text((50, 530), "• Reverse Sanity Checks", font=f_lb, fill="#ffffff")
    
    # Tutor Badge
    draw.rounded_rectangle([50, 600, 460, 665], radius=14, fill="#1e293b", outline="#38bdf8", width=2)
    f_tut = get_font(FONT_BOLD, 22)
    draw.text((70, 620), "Your Functional Skills Tutor", font=f_tut, fill="#38bdf8")
    
    img.save(filename)
    print(f"Generated YouTube Thumbnail: {filename}")

# -------------------------------------------------------------
# MAIN PIPELINE
# -------------------------------------------------------------
def build_video():
    scenes = [
        {
            "id": "scene_01_intro",
            "img": os.path.join(VID_DIR, "scene_01_intro.png"),
            "audio": os.path.join(VID_DIR, "scene_01_intro.mp3"),
            "video": os.path.join(VID_DIR, "scene_01_intro.mp4"),
            "render_func": make_slide_title,
            "text": ("Welcome to Master Functional Skills. I am your tutor. In this video walkthrough, "
                     "we are going through the complete step-by-step model solutions and examiner mark schemes "
                     "for our Numbers and Place Value worksheet, aligned to Pearson Edexcel Level 1 and Level 2 exams. "
                     "Let us get straight into the questions.")
        },
        {
            "id": "scene_02_rule",
            "img": os.path.join(VID_DIR, "scene_02_rule.png"),
            "audio": os.path.join(VID_DIR, "scene_02_rule.mp3"),
            "video": os.path.join(VID_DIR, "scene_02_rule.mp4"),
            "render_func": make_slide_rule,
            "text": ("Before solving, let us review the Examiner Golden Rule. Place value determines the exact value "
                     "of each digit by its column, from millions down to units and decimals. Always group digits by threes "
                     "from right to left using commas. Most importantly, never drop placeholder zeros when converting words into figures. "
                     "And when an examiner asks for the value of a digit, write the actual numerical value, not just the column name.")
        },
        {
            "id": "scene_03_q1",
            "img": os.path.join(VID_DIR, "scene_03_q1.png"),
            "audio": os.path.join(VID_DIR, "scene_03_q1.mp3"),
            "video": os.path.join(VID_DIR, "scene_03_q1.mp4"),
            "render_func": make_slide_q1,
            "text": ("Question one asks us to write two million, forty-five thousand, six hundred and eight in figures for two marks. "
                     "First, identify the millions period: that gives two in the millions column. "
                     "Next, forty-five thousand has zero hundred-thousands, giving zero four five in the thousands period, securing our first method mark. "
                     "Finally, six hundred and eight gives six zero eight. "
                     "Combining these gives our final answer: two million, forty-five thousand, six hundred and eight. "
                     "Watch out for the examiner trap: never write two, forty-five, six hundred and eight, omitting that vital placeholder zero!")
        },
        {
            "id": "scene_04_q2",
            "img": os.path.join(VID_DIR, "scene_04_q2.png"),
            "audio": os.path.join(VID_DIR, "scene_04_q2.mp3"),
            "video": os.path.join(VID_DIR, "scene_04_q2.mp4"),
            "render_func": make_slide_q2,
            "text": ("In question two, we look at the number four million, eight hundred and thirty-nine thousand, two hundred and seventy-one. "
                     "We need the value of digit three both in words and as a number. "
                     "Digit three sits in the ten-thousands column for our method mark. "
                     "Its numerical value is three times ten thousand, which is thirty thousand, written as three zero comma zero zero zero. "
                     "In words, that is Thirty Thousand. "
                     "Remember the examiner warning: writing just ten-thousands names the place, not the value, and forfeits the accuracy mark.")
        },
        {
            "id": "scene_05_q3",
            "img": os.path.join(VID_DIR, "scene_05_q3.png"),
            "audio": os.path.join(VID_DIR, "scene_05_q3.mp3"),
            "video": os.path.join(VID_DIR, "scene_05_q3.mp4"),
            "render_func": make_slide_q3,
            "text": ("Question three is an NHS workplace scenario worth three marks. "
                     "We need to arrange four depot stock quantities in ascending order. "
                     "First, compare the ten-thousands digits: Depot B has zero ten-thousands, making 304,850 the smallest for our first process mark. "
                     "For the remaining three depots in the three-hundred-and-forty-thousand range, compare the hundreds column: "
                     "Depot D has zero hundreds, Depot A has five hundreds, and Depot C has five thousands. "
                     "Our complete ascending order is 304,850, followed by 340,095, then 340,500, and finally 345,000.")
        },
        {
            "id": "scene_06_outro",
            "img": os.path.join(VID_DIR, "scene_06_outro.png"),
            "audio": os.path.join(VID_DIR, "scene_06_outro.mp3"),
            "video": os.path.join(VID_DIR, "scene_06_outro.mp4"),
            "render_func": make_slide_outro,
            "text": ("That concludes our worked video solution for Numbers and Place Value. "
                     "You can download the free printable worksheet along with the full examiner mark scheme directly on masterfunctionalskills.co.uk. "
                     "Be sure to subscribe for more complete video solutions across the entire Functional Skills Maths and English syllabus. "
                     "Keep practicing, and I will see you in the next walkthrough.")
        }
    ]

    print("=== Step 1: Generating 1080p Image Slides ===")
    for sc in scenes:
        sc["render_func"](sc["img"])

    make_thumbnail(os.path.join(VID_DIR, "thumbnail_numbers_and_place_value.png"))

    print("\n=== Step 2: Generating Audio Voiceover Tracks ===")
    for sc in scenes:
        generate_voiceover(sc["text"], sc["audio"])

    print("\n=== Step 3: Encoding Video Clips with ffmpeg ===")
    for sc in scenes:
        res = subprocess.run([
            "ffprobe", "-i", sc["audio"],
            "-show_entries", "format=duration",
            "-v", "quiet", "-of", "csv=p=0"
        ], capture_output=True, text=True, check=True)
        duration = float(res.stdout.strip())
        total_dur = duration + 0.6
        
        cmd_enc = [
            "ffmpeg", "-y",
            "-loop", "1", "-i", sc["img"],
            "-i", sc["audio"],
            "-c:v", "libx264", "-tune", "stillimage",
            "-c:a", "aac", "-b:a", "192k",
            "-pix_fmt", "yuv420p",
            "-t", str(total_dur),
            sc["video"]
        ]
        subprocess.run(cmd_enc, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        print(f"Rendered clip: {os.path.basename(sc['video'])} ({total_dur:.1f}s)")

    print("\n=== Step 4: Concatenating Master YouTube Video ===")
    concat_list_path = os.path.join(VID_DIR, "concat_list.txt")
    with open(concat_list_path, "w") as f:
        for sc in scenes:
            f.write(f"file '{sc['video']}'\n")

    master_output = os.path.join(VID_DIR, "Numbers_and_Place_Value_Video_Solution.mp4")
    cmd_concat = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", concat_list_path,
        "-c", "copy",
        master_output
    ]
    subprocess.run(cmd_concat, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    print(f"\n🎉 MASTER VIDEO CREATED: {master_output}")

    res = subprocess.run([
        "ffprobe", "-i", master_output,
        "-show_entries", "format=duration,size",
        "-v", "quiet", "-of", "json"
    ], capture_output=True, text=True, check=True)
    data = json.loads(res.stdout)
    dur = float(data['format']['duration'])
    size_mb = int(data['format']['size']) / (1024 * 1024)
    print(f"Master Video Specs: 1920x1080 Full HD | Duration: {dur:.1f}s (~{dur/60:.1f} mins) | Size: {size_mb:.2f} MB")

if __name__ == "__main__":
    build_video()
