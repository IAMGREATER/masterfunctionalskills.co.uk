#!/usr/bin/env python3
"""
Digital Functional Skills Deck (50 Cards)
Levels: Entry 3 / Level 1 / Level 2
Skill Areas:
  Area 1: Using Devices & Handling Information (Cards 1-10)
  Area 2: Creating and Editing Digital Content (Cards 11-24)
  Area 3: Communicating Online (Cards 25-32)
  Area 4: Transacting Online (Cards 33-40)
  Area 5: Being Safe and Responsible Online (Cards 41-50)
"""
import xml.etree.ElementTree as ET

from .area_1 import CARDS as C1
from .area_2 import CARDS as C2
from .area_3 import CARDS as C3
from .area_4 import CARDS as C4
from .area_5 import CARDS as C5

CARDS = C1 + C2 + C3 + C4 + C5

# Validate all cards
for i, card in enumerate(CARDS):
    assert card["number"] == i + 1, f"Expected card number {i+1}, got {card['number']}"
    ET.fromstring(card["svg_html"])

print(f"Successfully loaded and validated {len(CARDS)} Digital Functional Skills cards.")
