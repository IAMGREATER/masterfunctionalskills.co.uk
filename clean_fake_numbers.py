#!/usr/bin/env python3
"""
clean_fake_numbers.py
Replaces fake '020 XXXX XXXX' phone numbers with direct WhatsApp (+44 7564 525425) or Contact Us links.
"""

import os
import glob
import re

TARGET_DIRS = [
    "/home/subi/Projects/masterfunctionalskills.co.uk",
    "/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk"
]

def clean_file(fpath):
    with open(fpath, "r", encoding="utf-8") as fp:
        c = fp.read()
    
    orig = c
    
    # 1. Clean tel: links
    c = re.sub(r'href=[\'"]tel:020[X0-9\s]*[\'"]', 'href="https://wa.me/447564525425" target="_blank" rel="noopener"', c)
    
    # 2. Clean phone icon + 020 XXXX XXXX
    c = re.sub(r'<i class=[\'"]fa-solid fa-phone[\'"]></i>\s*(?:Call\s*)?020\s*XXXX\s*XXXX', '<i class="fa-brands fa-whatsapp"></i> WhatsApp Tutor', c)
    
    # 3. Clean any remaining 020 XXXX XXXX
    c = c.replace("020 XXXX XXXX", "+44 (0)7564 525425")
    
    if c != orig:
        with open(fpath, "w", encoding="utf-8") as fp:
            fp.write(c)
        return True
    return False

def main():
    for d in TARGET_DIRS:
        if not os.path.exists(d):
            continue
        count = 0
        for f in glob.glob(os.path.join(d, "*.html")):
            if clean_file(f):
                count += 1
        print(f"Cleaned {count} files in {d}")

if __name__ == "__main__":
    main()
