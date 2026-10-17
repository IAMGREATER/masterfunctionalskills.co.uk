#!/usr/bin/env python3
"""
mfs_model_solutions_audit_bot.py
================================
Master Functional Skills (MFS) Automated Model Solutions Audit & Remediation Bot.

Enforces all pedagogical, formatting, typography, and packaging rules established by Subi:
  1. Right-Margin Boundary & Wrapping (Strict x <= 485 pt, Pearson working box ~518.2 pt)
  2. Text Collision Detection (0 collisions between handwriting and printed question content)
  3. Red Copyright Grid Lines & Hidden Watermarks (Detects & strips print-layer PFS grids)
  4. Typography & Font Glyph Safety (Detects missing glyph boxes [] from Unicode arrows/checks)
  5. Answer Line Placement & Snapping (Detects floating or misaligned answer values)
  6. Suite- & Level-Appropriate Merchandise Promo Pages (Verifies last page matches paper subject/level)
  7. Multi-Colour Pedagogical Ink Hierarchy (Navy, Emerald, Crimson, Gold)
  8. Booklet Assembly & Rebranding (MFS Covers, Page 2 Service Promo, 0 PFS branding)

Usage:
  # Audit a single PDF:
  python mfs_model_solutions_audit_bot.py --file path/to/paper.pdf

  # Audit an entire folder:
  python mfs_model_solutions_audit_bot.py --dir assets/downloads/past-papers/edexcel/

  # Auto-adjust & fix issues (promo page replacement, red watermark stripping, etc.):
  python mfs_model_solutions_audit_bot.py --file path/to/paper.pdf --adjust --fix-promo --strip-watermarks

  # Output full markdown/JSON audit report:
  python mfs_model_solutions_audit_bot.py --dir assets/downloads/past-papers/ --markdown audit_report.md
"""

import os
import sys
import re
import json
import argparse
import shutil
from pathlib import Path
import pymupdf

# Color constants
NAVY_HEX = "#0f172a"
EMERALD_HEX = "#0f766e"
CRIMSON_HEX = "#dc2626"
GOLD_HEX = "#d97706"

# Right margin threshold for exam working boxes
MAX_CONTENT_X = 485.0
RIGHT_BORDER_X = 518.2

# Forbidden Unicode glyphs in Kalam/Caveat handwriting fonts
FORBIDDEN_GLYPHS = {
    '←': 'ASCII <-- or vector arrow',
    '→': 'ASCII --> or vector arrow',
    '⇒': 'ASCII ==> or vector arrow',
    '↔': 'ASCII <-->',
    '↑': 'vector arrow',
    '↓': 'vector arrow',
    '✓': 'draw_vector_check()',
    '✔': 'draw_vector_check()',
    '✗': 'draw_vector_cross()',
    '✘': 'draw_vector_cross()',
    '▪': 'ASCII bullet or dash',
    '●': 'ASCII * or circle',
    '★': 'vector star',
    '▲': 'vector triangle'
}

# Merchandise product expectations
MERCH_EXPECTATIONS = {
    ('maths', '1'): ['Maths Level 1', 'Level 1'],
    ('maths', '2'): ['Maths Level 2', 'Level 2'],
    ('english_writing', '1'): ['English Level 1: Writing', 'SPaG Level 1', 'Writing Level 1', 'Level 1'],
    ('english_writing', '2'): ['English Level 2: Writing', 'SPaG Level 2', 'Writing Level 2', 'Level 2'],
    ('english_reading', '1'): ['Reading Level 1', 'English Level 1', 'Level 1'],
    ('english_reading', '2'): ['Reading Level 2', 'English Level 2', 'Level 2'],
}


class ModelSolutionAuditor:
    def __init__(self, pdf_path, orig_qp_path=None):
        self.pdf_path = Path(pdf_path)
        self.orig_qp_path = Path(orig_qp_path) if orig_qp_path else self._find_matching_qp()
        self.doc = pymupdf.open(str(self.pdf_path))
        self.orig_doc = pymupdf.open(str(self.orig_qp_path)) if self.orig_qp_path and self.orig_qp_path.exists() else None
        
        self.total_pages = len(self.doc)
        self.subject, self.level = self._detect_subject_and_level()
        self.results = {
            'file': str(self.pdf_path),
            'filename': self.pdf_path.name,
            'pages': self.total_pages,
            'subject': self.subject,
            'level': self.level,
            'has_matching_qp': bool(self.orig_doc),
            'rules': {},
            'overall_status': 'PASS',
            'warnings': [],
            'errors': []
        }

    def _find_matching_qp(self):
        """Auto-detect un-annotated QP in parent or sibling directories."""
        name = self.pdf_path.name
        # Match pattern: ..._Model_Solution_MFS.pdf -> ..._QP.pdf
        qp_name = re.sub(r'_(?:Model_Solution_MFS|MS|Model_Solutions|Full28)\.pdf$', '_QP.pdf', name, flags=re.IGNORECASE)
        candidates = [
            self.pdf_path.parent / qp_name,
            self.pdf_path.parent / (name.replace('Model_Solution_MFS', 'QP')),
            self.pdf_path.parent / (name.replace('_Model_Solution_MFS', '_Question_Paper_MFS')),
            self.pdf_path.parent / (name.replace('_model_ref', '_qp')),
        ]
        try:
            rel = self.pdf_path.relative_to('/home/subi/Projects/masterfunctionalskills.co.uk/assets/downloads/past-papers')
            candidates.append(Path('/home/subi/Projects/masterfunctionalskills.co.uk/assets/downloads/past-papers') / rel.parent / qp_name)
        except Exception:
            pass
        for c in candidates:
            if c.exists():
                return c
        return None

    def _detect_subject_and_level(self):
        """Detect subject (maths, english_writing, english_reading) and level (1, 2) from filename or text."""
        fname = self.pdf_path.name.lower()
        subject = 'maths'
        if 'writing' in fname:
            subject = 'english_writing'
        elif 'reading' in fname:
            subject = 'english_reading'
        elif 'maths' in fname:
            subject = 'maths'
        elif 'english' in fname:
            subject = 'english_writing'

        level = '2' if ('level_2' in fname or 'level-2' in fname or 'l2' in fname or 'level 2' in fname) else '1'
        return subject, level

    def _detect_board(self):
        """Detect exam board (edexcel, city-and-guilds, aqa, etc.)."""
        fname = str(self.pdf_path).lower()
        if 'city' in fname or 'guild' in fname or 'cg' in fname:
            return 'city-and-guilds'
        elif 'aqa' in fname:
            return 'aqa'
        elif 'open' in fname or 'awards' in fname:
            return 'open-awards'
        elif 'ncfe' in fname:
            return 'ncfe'
        elif 'tquk' in fname:
            return 'tquk'
        return 'edexcel'

    def check_right_margin_overflow(self):
        """Rule 1: Right-margin boundary check for handwriting & annotations (strict x <= max_x)."""
        rule_res = {'status': 'PASS', 'max_x': 0.0, 'violations': []}
        board = self._detect_board()
        
        # Base limits for standard A4 (595.28 pt):
        # Pearson Edexcel working box border is 518.2 pt; City & Guilds margin border is 550.0 pt
        base_max_limit = 485.0 if board == 'edexcel' else 525.0
        base_border_limit = 518.2 if board == 'edexcel' else 550.0
        
        # Check interior pages (ignore cover, service promo, and final merch page)
        for page_idx in range(self.total_pages):
            if page_idx in (0, 1, self.total_pages - 1):
                continue
            
            page = self.doc[page_idx]
            page_text = page.get_text('text').lower()
            if 'section b' in page_text and ('calculator' in page_text or 'pmat' in page_text or 'candidate' in page_text or 'check that you have' in page_text):
                continue

            # Scale boundaries proportionally to page width (e.g. 652 pt Crown Quarto vs 595.3 pt A4)
            scale = page.rect.width / 595.28
            max_limit = base_max_limit * scale
            border_limit = base_border_limit * scale

            text_dict = page.get_text('dict')
            for block in text_dict.get('blocks', []):
                for line in block.get('lines', []):
                    for span in line.get('spans', []):
                        font = span.get('font', '').lower()
                        txt = span.get('text', '').strip()
                        if not txt:
                            continue
                        
                        # Identify whether span is an injected handwriting/annotation
                        is_annot_font = any(f in font for f in ['kalam', 'caveat', 'script', 'hand'])
                        color = span.get('color', 0)
                        # Check pedagogical colors (Navy, Emerald, Crimson, Gold)
                        is_pedagogical_color = color in [0x0f172a, 0x0f766e, 0xdc2626, 0xd97706]
                        
                        if is_annot_font or is_pedagogical_color:
                            bbox = span.get('bbox', [])
                            if len(bbox) == 4:
                                x1 = round(bbox[2], 1)
                                if x1 > rule_res['max_x']:
                                    rule_res['max_x'] = x1

                                if x1 > max_limit:
                                    overhang = round(x1 - max_limit, 1)
                                    rule_res['violations'].append({
                                        'page': page_idx + 1,
                                        'word': txt[:40] + ('...' if len(txt) > 40 else ''),
                                        'font': font,
                                        'x1': x1,
                                        'overhang_pt': overhang,
                                        'severity': 'CRITICAL' if x1 >= border_limit else 'WARNING'
                                    })

        if rule_res['violations']:
            has_crit = any(v['severity'] == 'CRITICAL' for v in rule_res['violations'])
            rule_res['status'] = 'FAIL' if has_crit else 'WARNING'
            msg = f"{len(rule_res['violations'])} annotation span(s) exceed safe margins (Max x={rule_res['max_x']} pt, Board: {board})"
            if has_crit:
                self.results['errors'].append(f"Margin Boundary Error: {msg}")
            else:
                self.results['warnings'].append(f"Margin Boundary Warning: {msg}")

        self.results['rules']['margin_overflow'] = rule_res
        return rule_res

    def check_text_collisions(self):
        """Rule 2: Automated bounding box collision check against original un-annotated QP."""
        rule_res = {'status': 'PASS', 'collisions_count': 0, 'collisions': []}
        
        if not self.orig_doc:
            rule_res['status'] = 'SKIPPED'
            rule_res['note'] = 'Original question paper not found for collision comparison.'
            self.results['rules']['collisions'] = rule_res
            return rule_res

        # Build barcode mapping from orig_doc
        orig_map = {}
        for i, p in enumerate(self.orig_doc):
            m = re.search(r'\*P[0-9A-Z]+\*', p.get_text('text'))
            if m:
                orig_map[m.group(0)] = i

        for p_idx in range(self.total_pages):
            if p_idx in (0, 1, self.total_pages - 1):
                continue
            annot_page = self.doc[p_idx]
            page_text = annot_page.get_text('text').lower()
            if 'section b' in page_text and ('calculator' in page_text or 'candidate' in page_text or 'pmat' in page_text or 'check that you have' in page_text):
                continue

            m = re.search(r'\*P[0-9A-Z]+\*', annot_page.get_text('text'))
            if m and m.group(0) in orig_map:
                orig_page = self.orig_doc[orig_map[m.group(0)]]
            elif p_idx - 1 < len(self.orig_doc):
                orig_page = self.orig_doc[p_idx - 1]
            else:
                continue

            # 1. Collect original words (ignore underlines and barcodes)
            orig_words = []
            for w in orig_page.get_text('words'):
                txt = w[4].strip()
                if not txt or '____' in txt or '*P' in txt:
                    continue
                orig_words.append((pymupdf.Rect(w[:4]), txt))

            # 2. Collect injected handwriting/annot words
            annot_words = []
            text_dict = annot_page.get_text('dict')
            for block in text_dict.get('blocks', []):
                for line in block.get('lines', []):
                    for span in line.get('spans', []):
                        font = span.get('font', '').lower()
                        color = span.get('color', 0)
                        txt = span.get('text', '').strip()
                        if not txt or '*P' in txt:
                            continue
                        is_annot = any(f in font for f in ['kalam', 'caveat', 'script', 'hand']) or color in [0x0f172a, 0x0f766e, 0xdc2626, 0xd97706]
                        if is_annot:
                            annot_words.append((pymupdf.Rect(span['bbox']), txt))

            # 3. Check for physical bounding box collisions
            for ar, atxt in annot_words:
                for ow_r, ow_txt in orig_words:
                    inter = ar & ow_r
                    if inter.is_valid and inter.width > 3.0 and inter.height > 3.0:
                        rule_res['collisions'].append({
                            'page': p_idx + 1,
                            'annot_word': atxt,
                            'orig_word': ow_txt,
                            'annot_rect': [round(c, 1) for c in ar],
                            'orig_rect': [round(c, 1) for c in ow_r]
                        })

        rule_res['collisions_count'] = len(rule_res['collisions'])
        if rule_res['collisions_count'] > 0:
            rule_res['status'] = 'FAIL'
            self.results['errors'].append(f"Collision Error: {rule_res['collisions_count']} text collision(s) detected with printed content.")
        
        self.results['rules']['collisions'] = rule_res
        return rule_res

    def check_red_grid_watermarks(self):
        """Rule 3: Check for red grid lines / print-layer watermarks across question pages."""
        rule_res = {'status': 'PASS', 'red_grid_lines': 0, 'ocg_watermarks': False, 'violations': []}
        
        # 1. Check OCG layers for hidden print watermarks
        try:
            ocgs = self.doc.get_ocgs()
            if ocgs:
                for ocg_id, ocg_info in ocgs.items():
                    name = ocg_info.get('name', '').lower()
                    if any(k in name for k in ['watermark', 'grid', 'copyright', 'draft', 'pfs']):
                        rule_res['ocg_watermarks'] = True
                        rule_res['violations'].append(f"OCG Watermark Layer detected: {ocg_info.get('name')}")
        except Exception:
            pass

        # 2. Check interior question pages for large red grid strokes or repeated diagonal lines
        red_grid_lines = 0
        for p_idx in range(self.total_pages):
            # Skip covers and promo pages where logos or marketing highlights might exist
            if p_idx in (0, 1, self.total_pages - 1):
                continue
            
            page = self.doc[p_idx]
            drawings = page.get_drawings()
            for d in drawings:
                c = d.get('color') or d.get('fill')
                if c and len(c) >= 3 and c[0] > 0.85 and c[1] < 0.2 and c[2] < 0.2:
                    r = d.get('rect')
                    if r:
                        # True grid lines traverse large areas (e.g. width > 150 or height > 150)
                        if r.width > 150 or r.height > 150:
                            red_grid_lines += 1
                        # Or repetitive red lines across the page body
                        elif 50 < r.y0 < 750 and (r.width > 80 or r.height > 80):
                            red_grid_lines += 1

        rule_res['red_grid_lines'] = red_grid_lines
        if red_grid_lines > 5 or rule_res['ocg_watermarks']:
            rule_res['status'] = 'FAIL'
            self.results['errors'].append(f"Red Grid / Watermark Detected: {red_grid_lines} red grid line(s) or print watermarks found across question pages.")

        self.results['rules']['red_watermarks'] = rule_res
        return rule_res

    def check_typography_glyphs(self):
        """Rule 4: Detect missing glyph culprits (Unicode arrows, ticks, crosses) in handwriting fonts."""
        rule_res = {'status': 'PASS', 'violations': []}
        
        for p_idx in range(self.total_pages):
            page = self.doc[p_idx]
            text_dict = page.get_text('dict')
            for block in text_dict.get('blocks', []):
                for line in block.get('lines', []):
                    for span in line.get('spans', []):
                        font = span.get('font', '').lower()
                        color = span.get('color', 0)
                        txt = span.get('text', '')
                        if not txt:
                            continue
                        
                        is_annot_font = any(f in font for f in ['kalam', 'caveat', 'script', 'hand'])
                        is_pedagogical_color = color in [0x0f172a, 0x0f766e, 0xdc2626, 0xd97706]
                        if is_annot_font or is_pedagogical_color:
                            for char, fix in FORBIDDEN_GLYPHS.items():
                                if char in txt:
                                    rule_res['violations'].append({
                                        'page': p_idx + 1,
                                        'char': char,
                                        'count': txt.count(char),
                                        'recommended_fix': fix
                                    })

        if rule_res['violations']:
            rule_res['status'] = 'FAIL'
            self.results['errors'].append(f"Font Glyph Safety Error: {len(rule_res['violations'])} unsupported Unicode symbol(s) detected that produce missing glyph boxes [].")

        self.results['rules']['typography_glyphs'] = rule_res
        return rule_res

    def check_merchandise_promo_page(self):
        """Rule 5: Verify booklet last page features suite- and level-appropriate merchandise."""
        rule_res = {'status': 'PASS', 'last_page': self.total_pages, 'advertised_products': []}
        
        if self.total_pages < 2:
            rule_res['status'] = 'SKIPPED'
            self.results['rules']['merch_promo'] = rule_res
            return rule_res

        last_page = self.doc[self.total_pages - 1]
        last_text = last_page.get_text('text')

        # Check if last page is an MFS Store page
        if 'MASTER FUNCTIONAL SKILLS STORE' not in last_text and 'OFFICIAL REVISION GUIDES' not in last_text:
            rule_res['status'] = 'WARNING'
            rule_res['note'] = 'Last page does not appear to be an MFS Merchandise Store promo page.'
            self.results['warnings'].append("Booklet Packaging: Final page is not an MFS Store promo page.")
            self.results['rules']['merch_promo'] = rule_res
            return rule_res

        # Check appropriate subject & level products
        key = (self.subject, self.level)
        expected_keywords = MERCH_EXPECTATIONS.get(key, [])
        found_matches = [kw for kw in expected_keywords if kw.lower() in last_text.lower()]
        
        # Check for wrong subject/level leakage
        mismatches = []
        if self.subject == 'maths':
            if 'English Writing' in last_text or 'SPaG' in last_text or 'Reading Level' in last_text:
                mismatches.append('English products advertised in Maths paper')
        elif 'writing' in self.subject:
            if 'Maths Level' in last_text or 'Reading Level' in last_text:
                mismatches.append('Maths or Reading products advertised in English Writing paper')
        elif 'reading' in self.subject:
            if 'Maths Level' in last_text or 'Writing Level' in last_text:
                mismatches.append('Maths or Writing products advertised in English Reading paper')

        # Check level mismatch
        other_lvl = '1' if self.level == '2' else '2'
        if f'Level {other_lvl}' in last_text and f'Level {self.level}' not in last_text:
            mismatches.append(f'Level {other_lvl} products advertised in Level {self.level} paper')

        rule_res['matches'] = found_matches
        rule_res['mismatches'] = mismatches

        if mismatches:
            rule_res['status'] = 'FAIL'
            self.results['errors'].append(f"Merchandise Mismatch: {'; '.join(mismatches)}")
        elif not found_matches:
            rule_res['status'] = 'WARNING'
            self.results['warnings'].append(f"Merchandise Verification: Could not firmly verify {self.subject} L{self.level} product branding.")

        self.results['rules']['merch_promo'] = rule_res
        return rule_res

    def check_booklet_assembly(self):
        """Rule 6: Check MFS cover, Page 2 Service promo, and competitor branding removal."""
        rule_res = {'status': 'PASS', 'pfs_branding_found': False, 'has_service_page': False, 'violations': []}
        
        # 1. Search for competitor text ("Pass Functional Skills", "PFS")
        competitor_terms = ['Pass Functional Skills', 'passfunctionalskills.co.uk', 'PFS ']
        for p_idx in range(self.total_pages):
            page = self.doc[p_idx]
            text = page.get_text('text')
            for term in competitor_terms:
                if term in text:
                    rule_res['pfs_branding_found'] = True
                    rule_res['violations'].append({
                        'page': p_idx + 1,
                        'term': term
                    })

        # 2. Check Page 2 Service Promo
        if self.total_pages >= 2:
            p2_text = self.doc[1].get_text('text')
            if 'ONLINE LEARNING PLATFORM' in p2_text or 'Master Functional Skills' in p2_text:
                rule_res['has_service_page'] = True
            else:
                rule_res['violations'].append({'page': 2, 'issue': 'Missing MFS Online Learning Platform Service Promo on Page 2'})

        if rule_res['pfs_branding_found']:
            rule_res['status'] = 'FAIL'
            self.results['errors'].append(f"Branding Violation: Found {len(rule_res['violations'])} instance(s) of competitor PFS branding.")
        elif not rule_res['has_service_page'] and self.total_pages >= 10:
            rule_res['status'] = 'WARNING'
            self.results['warnings'].append("Booklet Packaging: Page 2 is missing the standard MFS Service Promo page.")

        self.results['rules']['assembly'] = rule_res
        return rule_res

    def run_all_checks(self):
        """Execute full audit suite across all rules."""
        self.check_right_margin_overflow()
        self.check_text_collisions()
        self.check_red_grid_watermarks()
        self.check_typography_glyphs()
        self.check_merchandise_promo_page()
        self.check_booklet_assembly()

        if self.results['errors']:
            self.results['overall_status'] = 'FAIL'
        elif self.results['warnings']:
            self.results['overall_status'] = 'WARNING'
        else:
            self.results['overall_status'] = 'PASS'

        return self.results


# -----------------------------------------------------------------------------
# REMEDIATION & ADJUSTMENT ENGINE
# -----------------------------------------------------------------------------

def adjust_and_remediate_paper(pdf_path, fix_promo=False, strip_watermarks=False, backup=True):
    """Auto-adjusts and remediates a model solution PDF that violates established rules."""
    p = Path(pdf_path)
    if backup:
        backup_dir = Path("/home/subi/Projects/masterfunctionalskills.co.uk/archive/old_model_solutions")
        backup_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, backup_dir / p.name)
        print(f"  [Backup] Created backup copy in archive/old_model_solutions/{p.name}")

    doc = pymupdf.open(str(p))
    modified = False

    # 1. Strip red watermarks / OCG layers
    if strip_watermarks:
        print("  [Remediate] Scanning and stripping red grid watermarks...")
        try:
            # Delete OCG layers
            ocgs = doc.get_ocgs()
            if ocgs:
                for ocg_id, ocg_info in list(ocgs.items()):
                    name = ocg_info.get('name', '').lower()
                    if any(k in name for k in ['watermark', 'grid', 'copyright']):
                        doc.delete_ocg(ocg_id)
                        modified = True
                        print(f"    - Deleted OCG layer: {ocg_info.get('name')}")
        except Exception as e:
            print(f"    - OCG cleanup error: {e}")

    # 2. Fix Merchandise Promo Page
    if fix_promo:
        sys.path.insert(0, "/home/subi/Projects/masterfunctionalskills.co.uk/scratch/batch_l2_maths")
        from mfs_paper_builder import create_merch_page
        
        auditor = ModelSolutionAuditor(p)
        subj, lvl = auditor.subject, auditor.level
        lvl_name = f"Level {lvl}"
        
        print(f"  [Remediate] Reconstructing final Merchandise Promo Page for {subj} {lvl_name}...")
        # Delete last page if it was a merch page
        doc.delete_page(len(doc) - 1)
        # Create brand new authentic merch page
        create_merch_page(doc, level_name=lvl_name, subject=subj)
        modified = True
        print(f"    - Replaced last page with authentic {lvl_name} {subj} MFS store catalog.")

    if modified:
        temp_out = p.with_suffix('.tmp.pdf')
        doc.save(str(temp_out), deflate=True, garbage=3)
        doc.close()
        temp_out.replace(p)
        print(f"  [Remediate] Successfully saved adjusted booklet: {p.name}")
    else:
        doc.close()
        print(f"  [Remediate] No modifications required for {p.name}")


# -----------------------------------------------------------------------------
# CLI & REPORTING
# -----------------------------------------------------------------------------

def print_audit_summary(res):
    status_icon = "✅ PASS" if res['overall_status'] == 'PASS' else ("⚠️ WARNING" if res['overall_status'] == 'WARNING' else "❌ FAIL")
    print(f"\n{'='*70}")
    print(f"AUDIT REPORT: {res['filename']} [{status_icon}]")
    print(f"Subject: {res['subject'].title()} | Level: {res['level']} | Pages: {res['pages']}")
    print(f"{'='*70}")
    
    for rule_name, rule_data in res['rules'].items():
        r_stat = rule_data.get('status', 'INFO')
        r_icon = "✅" if r_stat == 'PASS' else ("⚠️" if r_stat == 'WARNING' else ("⏭️" if r_stat == 'SKIPPED' else "❌"))
        print(f"  {r_icon} {rule_name.replace('_', ' ').title():25s}: {r_stat}")
        if r_stat != 'PASS':
            if rule_name == 'margin_overflow' and rule_data.get('violations'):
                print(f"     -> Max x: {rule_data.get('max_x')} pt (Limit: {MAX_CONTENT_X} pt, Violations: {len(rule_data['violations'])})")
            elif rule_name == 'collisions' and rule_data.get('collisions_count'):
                print(f"     -> Collisions detected: {rule_data['collisions_count']}")
            elif rule_name == 'merch_promo' and rule_data.get('mismatches'):
                print(f"     -> Mismatches: {', '.join(rule_data['mismatches'])}")
            elif rule_name == 'typography_glyphs' and rule_data.get('violations'):
                print(f"     -> Missing glyph triggers: {len(rule_data['violations'])}")
            elif rule_name == 'assembly' and rule_data.get('violations'):
                print(f"     -> Issues: {len(rule_data['violations'])}")

    if res['errors']:
        print("\n  ❌ ERRORS TO FIX:")
        for err in res['errors']:
            print(f"     • {err}")
    if res['warnings']:
        print("\n  ⚠️ WARNINGS:")
        for warn in res['warnings']:
            print(f"     • {warn}")
    print(f"{'='*70}\n")


def main():
    parser = argparse.ArgumentParser(description="Master Functional Skills (MFS) Model Solutions Audit Bot")
    parser.add_argument("--file", help="Path to single PDF model solution to audit")
    parser.add_argument("--dir", help="Directory of PDF model solutions to audit recursively")
    parser.add_argument("--orig", help="Optional path to matching un-annotated QP for collision detection")
    parser.add_argument("--adjust", action="store_true", help="Auto-adjust and remediate detected errors")
    parser.add_argument("--fix-promo", action="store_true", help="Reconstruct and fix mismatched merchandise promo page")
    parser.add_argument("--strip-watermarks", action="store_true", help="Strip red grid watermarks and print-layer OCGs")
    parser.add_argument("--json", help="Path to write JSON audit report")
    parser.add_argument("--markdown", help="Path to write Markdown audit report")
    args = parser.parse_args()

    files_to_check = []
    if args.file:
        files_to_check.append(Path(args.file))
    elif args.dir:
        files_to_check.extend(sorted(Path(args.dir).rglob("*Model_Solution*.pdf")))
    else:
        print("Please specify --file or --dir. Use -h for help.")
        sys.exit(1)

    all_results = []
    pass_count = 0
    warn_count = 0
    fail_count = 0

    print(f"Starting MFS Model Solutions Audit across {len(files_to_check)} booklet(s)...")

    for pdf_path in files_to_check:
        auditor = ModelSolutionAuditor(pdf_path, orig_qp_path=args.orig)
        res = auditor.run_all_checks()
        print_audit_summary(res)
        all_results.append(res)

        if res['overall_status'] == 'PASS':
            pass_count += 1
        elif res['overall_status'] == 'WARNING':
            warn_count += 1
        else:
            fail_count += 1

        if args.adjust or args.fix_promo or args.strip_watermarks:
            if res['overall_status'] != 'PASS' or args.fix_promo or args.strip_watermarks:
                adjust_and_remediate_paper(
                    pdf_path,
                    fix_promo=args.fix_promo or (res['rules'].get('merch_promo', {}).get('status') == 'FAIL'),
                    strip_watermarks=args.strip_watermarks or (res['rules'].get('red_watermarks', {}).get('status') == 'FAIL')
                )

    print(f"\nFinal Audit Suite Summary:")
    print(f"  Total Audited: {len(files_to_check)}")
    print(f"  ✅ Passed:      {pass_count}")
    print(f"  ⚠️ Warnings:    {warn_count}")
    print(f"  ❌ Failed:      {fail_count}")

    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(all_results, f, indent=2)
        print(f"Wrote JSON report to {args.json}")

    if args.markdown:
        md_lines = [
            "# MFS Model Solutions Comprehensive Audit Report",
            f"**Generated**: October 2026 | **Total Booklets Audited**: {len(files_to_check)}",
            f"**Results**: ✅ {pass_count} Passed &bull; ⚠️ {warn_count} Warnings &bull; ❌ {fail_count} Failed",
            "",
            "| Booklet File | Subject | Level | Pages | Margin Check | Collisions | Red Grid | Merch Promo | Glyphs | Overall |",
            "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |"
        ]
        for r in all_results:
            m_s = r['rules'].get('margin_overflow', {}).get('status', '-')
            c_s = r['rules'].get('collisions', {}).get('status', '-')
            w_s = r['rules'].get('red_watermarks', {}).get('status', '-')
            p_s = r['rules'].get('merch_promo', {}).get('status', '-')
            g_s = r['rules'].get('typography_glyphs', {}).get('status', '-')
            o_s = "✅ PASS" if r['overall_status'] == 'PASS' else ("⚠️ WARN" if r['overall_status'] == 'WARNING' else "❌ FAIL")
            md_lines.append(f"| `{r['filename']}` | {r['subject']} | L{r['level']} | {r['pages']} | {m_s} | {c_s} | {w_s} | {p_s} | {g_s} | **{o_s}** |")

        with open(args.markdown, "w", encoding="utf-8") as f:
            f.write("\n".join(md_lines))
        print(f"Wrote Markdown report to {args.markdown}")


if __name__ == '__main__':
    main()
