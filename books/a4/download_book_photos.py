#!/usr/bin/env python3
"""
download_book_photos.py
Downloads a curated library of high-resolution, royalty-free stock photos from Unsplash
for the Master Functional Skills A4 publications.
"""

import os
import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from PIL import Image

SITE_ROOT = Path("/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk")
PHOTO_DIR = SITE_ROOT / "assets" / "img" / "book_photos"

# Curated high-res Unsplash photos across 14 practical adult learning themes
PHOTO_CATALOG = [
    # 1. workplace_office
    ("workplace_office", "team_meeting", "photo-1522071820081-009f0129c71c", "Colleagues in an office meeting collaborating around a laptop", ["office", "team", "meeting", "workplace", "discussion"]),
    ("workplace_office", "desk_laptop", "photo-1497215728101-856f4ea42174", "Modern office desk with open laptop and paperwork", ["desk", "laptop", "office", "work", "computer"]),
    ("workplace_office", "woman_manager", "photo-1573496359142-b8d87734a5a2", "Professional woman manager smiling in modern workplace", ["manager", "professional", "office", "woman", "worker"]),
    ("workplace_office", "whiteboard_planning", "photo-1531403009284-440f080d1e12", "Team planning workflow with sticky notes on whiteboard", ["whiteboard", "planning", "strategy", "project", "notes"]),
    ("workplace_office", "writing_notes", "photo-1455390582262-044cdead277a", "Hands writing a report in a notebook with fountain pen", ["writing", "notebook", "pen", "report", "notes"]),
    ("workplace_office", "presentation", "photo-1557804506-669a67965ba0", "Colleague giving a presentation to team with screen", ["presentation", "meeting", "colleagues", "screen"]),
    ("workplace_office", "typing_keyboard", "photo-1587829741301-dc798b83add3", "Hands typing on keyboard in modern bright workspace", ["typing", "keyboard", "computer", "desk"]),

    # 2. retail_shop
    ("retail_shop", "cashier_till", "photo-1556742049-0a67c5574f73", "Customer paying contactless by card at shop counter till", ["shop", "till", "cashier", "payment", "card", "contactless"]),
    ("retail_shop", "supermarket_aisle", "photo-1578916171728-46686eac8d58", "Organised supermarket shelves with groceries and price tags", ["supermarket", "groceries", "shelves", "price", "shopping"]),
    ("retail_shop", "customer_service", "photo-1556740758-90de374c12ad", "Friendly shop assistant helping customer at checkout", ["customer service", "retail", "shop", "assistant", "helping"]),
    ("retail_shop", "clothing_store", "photo-1441986300917-64674bd600d8", "Retail clothing store with sale items and neat displays", ["retail", "clothing", "store", "sale", "display"]),
    ("retail_shop", "warehouse_stock", "photo-1586528116311-ad8dd3c8310d", "Warehouse worker checking inventory boxes on metal shelves", ["warehouse", "stock", "inventory", "boxes", "worker"]),

    # 3. healthcare_care
    ("healthcare_care", "nurse_patient", "photo-1576765608535-5f04d1e3f289", "Friendly nurse caring for an elderly resident in care home", ["nurse", "care", "patient", "elderly", "healthcare"]),
    ("healthcare_care", "doctor_stethoscope", "photo-1582750433449-648ed127bb54", "Healthcare practitioner with stethoscope in medical clinic", ["doctor", "stethoscope", "clinic", "hospital", "medical"]),
    ("healthcare_care", "medicine_tablets", "photo-1584308666744-24d5c474f2ae", "Prescription medicine bottles and blister packs on tray", ["medicine", "tablets", "prescription", "pharmacy", "dosage"]),
    ("healthcare_care", "blood_pressure", "photo-1628771065518-0d82f1938462", "Medical professional measuring blood pressure with monitor", ["blood pressure", "monitor", "healthcare", "checkup"]),
    ("healthcare_care", "care_worker_smiling", "photo-1584515979956-d9f6e5d09982", "Care worker supporting resident in hospital community room", ["care", "worker", "support", "community", "hospital"]),

    # 4. construction_trades
    ("construction_trades", "builder_measuring", "photo-1504307651254-35680f356dfd", "Construction worker measuring wooden frame on site", ["builder", "construction", "measuring", "wood", "tape measure"]),
    ("construction_trades", "blueprints_plans", "photo-1503387762-592deb58ef4e", "Architectural blueprints and technical drawings with hardhat", ["blueprints", "plans", "architecture", "scale", "drawings"]),
    ("construction_trades", "electrician_tools", "photo-1621905251189-08b45d6a269e", "Electrician installing wiring with safety tools and multimeter", ["electrician", "wiring", "tools", "safety", "trade"]),
    ("construction_trades", "spirit_level", "photo-1581092335397-9583fe92d232", "Construction engineer using spirit level on brickwork", ["level", "construction", "masonry", "brick", "trade"]),
    ("construction_trades", "safety_hardhat", "photo-1578575437130-527eed3abbec", "Personal protective equipment hardhat and high-visibility vest", ["ppe", "hardhat", "hivis", "safety", "site"]),

    # 5. kitchen_cooking_recipes
    ("kitchen_cooking_recipes", "kitchen_scales", "photo-1556911220-e15b29be8c8f", "Baking ingredients being weighed on kitchen scales with bowl", ["scales", "baking", "ingredients", "weighing", "grams"]),
    ("kitchen_cooking_recipes", "chopping_vegetables", "photo-1540420773420-3366772f4999", "Fresh vegetables being chopped on wooden cutting board", ["vegetables", "chopping", "cooking", "fresh", "nutrition"]),
    ("kitchen_cooking_recipes", "measuring_jug", "photo-1556909114-f6e7ad7d3136", "Baker measuring liquid milk in glass measuring jug", ["measuring jug", "liquid", "milk", "recipe", "volume"]),
    ("kitchen_cooking_recipes", "oven_baking", "photo-1509440159596-0249088772ff", "Fresh bread rolls baking in oven on metal baking sheet", ["bread", "baking", "oven", "temperature", "food"]),

    # 6. money_shopping_bills
    ("money_shopping_bills", "calculator_finance", "photo-1554224155-6726b3ff858f", "Desk with electronic calculator, financial bills and pencil", ["calculator", "bills", "finance", "budget", "maths"]),
    ("money_shopping_bills", "coins_pounds", "photo-1526304640581-d334cdbbf45e", "Coins and currency arranged on wooden table", ["coins", "money", "currency", "cash", "pounds"]),
    ("money_shopping_bills", "paying_card", "photo-1563013544-824ae1b704d3", "Contactless card chip payment at modern terminal", ["payment", "card", "contactless", "banking", "money"]),
    ("money_shopping_bills", "receipt_checking", "photo-1586769852044-692d6e3703f0", "Auditor checking printed receipts and invoices with pen", ["receipts", "invoice", "checking", "audit", "expenses"]),

    # 7. travel_transport_timetables
    ("travel_transport_timetables", "train_departures", "photo-1517649763962-0c623266ddc0", "Railway station electronic departures board with train times", ["train", "departures", "timetable", "station", "schedule"]),
    ("travel_transport_timetables", "bus_stop", "photo-1544620347-c4fd4a3d5957", "City bus waiting at designated roadside bus stop", ["bus", "transport", "travel", "commute", "timetable"]),
    ("travel_transport_timetables", "tube_underground", "photo-1513635269975-59663e0ac1ad", "London underground transit train arriving at station", ["tube", "train", "metro", "london", "transit"]),

    # 8. measuring_tools
    ("measuring_tools", "tape_measure", "photo-1586864387967-d02ef85d93e8", "Yellow metal tape measure pulled out showing metric centimetres", ["tape measure", "centimetres", "metric", "measuring", "length"]),
    ("measuring_tools", "ruler_geometry", "photo-1618005182384-a83a8bd57fbe", "Clear plastic ruler and geometric protractor on grid paper", ["ruler", "geometry", "protractor", "measurement", "maths"]),
    ("measuring_tools", "digital_scales", "photo-1518770660439-4636190af475", "Digital precision electronic scale on workshop bench", ["scale", "digital", "weight", "grams", "measurement"]),

    # 9. maps_directions
    ("maps_directions", "smartphone_navigation", "photo-1524661135-423995f22d0b", "Hand holding smartphone showing live GPS street map route", ["map", "gps", "navigation", "directions", "route"]),
    ("maps_directions", "paper_map_route", "photo-1526778548025-fa2f459cd5c1", "Unfolded topographical road map with planned route markers", ["paper map", "route", "roads", "directions", "journey"]),
    ("maps_directions", "compass_direction", "photo-1516738901171-8eb4fc13bd20", "Classic brass compass pointing north on nautical chart", ["compass", "direction", "north", "bearings", "navigation"]),

    # 10. charts_data_screens
    ("charts_data_screens", "analytics_dashboard", "photo-1460925895917-afdab827c52f", "Computer monitor displaying colourful bar charts and statistics", ["charts", "graphs", "statistics", "data", "dashboard"]),
    ("charts_data_screens", "tablet_spreadsheet", "photo-1551288049-bebda4e38f71", "Business tablet showing spreadsheet columns and data table", ["spreadsheet", "table", "data", "tablet", "columns"]),
    ("charts_data_screens", "pie_chart_analysis", "photo-1543286386-713bdd548da4", "Printed document with colourful segmented pie chart", ["pie chart", "percentages", "analysis", "data", "report"]),

    # 11. home_diy_decorating
    ("home_diy_decorating", "paint_roller_wall", "photo-1589939705384-5185137a7f0f", "Paint roller applying clean fresh paint onto interior wall", ["paint", "roller", "decorating", "wall", "diy", "area"]),
    ("home_diy_decorating", "measuring_floor", "photo-1505798577917-a65157d3320a", "Floor installer measuring room dimensions for new flooring", ["flooring", "measuring", "dimensions", "area", "perimeter"]),
    ("home_diy_decorating", "diy_tools_box", "photo-1530124566582-a618bc2615dc", "Well-stocked homeowner toolbox with hammer, pliers and screws", ["tools", "toolbox", "diy", "repairs", "home"]),

    # 12. email_online_safety
    ("email_online_safety", "email_inbox_laptop", "photo-1596526131083-e8c633c948d2", "Close-up of laptop screen displaying corporate email inbox", ["email", "inbox", "laptop", "communication", "message"]),
    ("email_online_safety", "cybersecurity_lock", "photo-1563986768609-322da13575f3", "Secure digital lock graphic representing cybersecurity protection", ["security", "cybersecurity", "safety", "password", "lock"]),
    ("email_online_safety", "phone_login", "photo-1512941937669-90a1b58e7e9c", "User entering two-step verification code on smartphone", ["phone", "login", "verification", "security", "digital"]),

    # 13. classroom_studying_adults
    ("classroom_studying_adults", "adult_learners_class", "photo-1517245386807-bb43f82c33c4", "Adult students in college seminar classroom discussing project", ["adult learners", "classroom", "college", "students", "studying"]),
    ("classroom_studying_adults", "student_studying_laptop", "photo-1434030216411-0b793f4b4173", "Focused adult learner taking notes from online course on laptop", ["studying", "online learning", "notes", "learner", "exam"]),
    ("classroom_studying_adults", "library_books", "photo-1457369804613-52c61a468e7d", "Study desk in library with open reference textbooks and highlighter", ["library", "books", "reference", "study", "reading"]),

    # 14. everyday_objects
    ("everyday_objects", "wall_clock", "photo-1508057198894-247b23fe5ade", "Classic round analogue wall clock showing clear hours and minutes", ["clock", "time", "analogue", "hours", "minutes"]),
    ("everyday_objects", "calendar_schedule", "photo-1506784983877-45594efa4cbe", "Monthly wall calendar planner with highlighted target dates", ["calendar", "dates", "schedule", "planner", "month"]),
    ("everyday_objects", "delivery_parcel", "photo-1549465220-1a8b9238cd48", "Cardboard delivery package box with barcode shipping label", ["parcel", "package", "delivery", "box", "shipping"]),
    ("everyday_objects", "coffee_break", "photo-1514432324607-a09d9b4aefdd", "Ceramic coffee cup next to open planner on wooden café table", ["coffee", "café", "break", "planner", "lifestyle"])
]


def download_one(item):
    theme, slug, photo_id, desc, tags = item
    target_dir = PHOTO_DIR / theme
    target_dir.mkdir(parents=True, exist_ok=True)
    target_path = target_dir / f"{slug}.jpg"

    if target_path.exists() and target_path.stat().st_size > 10000:
        return {"status": "exists", "path": str(target_path.relative_to(PHOTO_DIR)), "theme": theme, "desc": desc, "tags": tags, "full_path": str(target_path)}

    url = f"https://images.unsplash.com/{photo_id}?w=1200&q=80&fm=jpg"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = resp.read()
        target_path.write_bytes(data)

        # Validate with PIL
        with Image.open(target_path) as img:
            w, h = img.size

        return {
            "status": "downloaded",
            "path": str(target_path.relative_to(PHOTO_DIR)),
            "theme": theme,
            "description": desc,
            "tags": tags,
            "source_url": url,
            "license": "Unsplash License (free commercial use)",
            "width": w,
            "height": h,
            "full_path": str(target_path)
        }
    except Exception as e:
        print(f"Error downloading {slug}: {e}")
        return None


def main():
    print(f"Downloading {len(PHOTO_CATALOG)} curated stock photos to {PHOTO_DIR}...")
    manifest_entries = []

    with ThreadPoolExecutor(max_workers=8) as executor:
        results = list(executor.map(download_one, PHOTO_CATALOG))

    for r in results:
        if r:
            manifest_entries.append(r)

    manifest_file = PHOTO_DIR / "manifest.json"
    manifest_file.write_text(json.dumps(manifest_entries, indent=2), encoding="utf-8")
    print(f"Successfully processed {len(manifest_entries)} photos! Manifest written to {manifest_file}")


if __name__ == "__main__":
    main()
