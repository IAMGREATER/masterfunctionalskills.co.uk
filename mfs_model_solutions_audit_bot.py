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

# Gold-Standard Edexcel Maths L2 Color Palette (STRICT)
GOLD_NAVY = 0x0F47AD
GOLD_EMERALD = 0x14843D
GOLD_EMERALD_ALT = 0x14853D
GOLD_CRIMSON = 0xD11F26
GOLD_ACCENT = 0xF59E0B
GOLD_COLOR_SET = {GOLD_NAVY, GOLD_EMERALD, GOLD_EMERALD_ALT, GOLD_CRIMSON, GOLD_ACCENT}

# Deprecated PFS / wrong ink colours (FAIL if used for handwriting)
WRONG_PFS_COLORS = {0x0F172A, 0x0F766E, 0xDC2626}


def _is_chromatic_color(color: int) -> bool:
    r, g, b = (color >> 16) & 0xFF, (color >> 8) & 0xFF, color & 0xFF
    return (max(r, g, b) - min(r, g, b)) >= 25

# Right margin threshold for exam working boxes (legacy constant kept for summary print)
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
    ('dfs', 'e3'): ['Digital Functional Skills Entry 3', 'Entry 3', 'Digital Functional Skills'],
    ('dfs', '1'): ['Digital Functional Skills Level 1', 'Level 1', 'Digital Functional Skills'],
}


class ModelSolutionAuditor:
    def __init__(self, pdf_path, orig_qp_path=None, orig_qp_paths=None):
        self.pdf_path = Path(pdf_path)
        if orig_qp_paths is not None:
            qps = [Path(p) for p in orig_qp_paths if Path(p).exists()]
        elif orig_qp_path:
            qps = [Path(orig_qp_path)] if Path(orig_qp_path).exists() else []
        else:
            qps = self._find_matching_qps()
        self.orig_qp_path = qps[0] if qps else None
        self.doc = pymupdf.open(str(self.pdf_path))
        if len(qps) == 1:
            self.orig_doc = pymupdf.open(str(qps[0]))
        elif len(qps) > 1:
            comb = pymupdf.open()
            for qp_p in qps:
                d_tmp = pymupdf.open(str(qp_p))
                comb.insert_pdf(d_tmp)
                d_tmp.close()
            self.orig_doc = comb
        else:
            self.orig_doc = None
        
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

    def _find_matching_qps(self):
        """Auto-detect all un-annotated QPs (1 or 2 files) via manifest.json or sibling directories."""
        name = self.pdf_path.name
        manifest_file = Path("/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk/mfs_model_engine/data/manifest.json")
        if manifest_file.exists():
            try:
                mdata = json.loads(manifest_file.read_text(encoding="utf-8"))
                entries = mdata if isinstance(mdata, list) else next((v for v in mdata.values() if isinstance(v, list)), [])
                target_norm = str(self.pdf_path.resolve())
                for ent in entries:
                    for cand_key in ("target_model_path", "existing_model_path"):
                        rel = ent.get(cand_key)
                        if rel:
                            cp = (Path("/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk") / rel).resolve()
                            if str(cp) == target_norm and ent.get("qp_paths"):
                                spec_f = Path("/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk/mfs_model_engine/data/specs") / ent["board"] / f"{ent['paper_id']}.json"
                                if spec_f.exists():
                                    try:
                                        if json.loads(spec_f.read_text(encoding="utf-8")).get("typeset_online_mock"):
                                            return []
                                    except Exception:
                                        pass
                                found = [
                                    Path("/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk") / rp
                                    for rp in ent["qp_paths"]
                                    if (Path("/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk") / rp).exists()
                                ]
                                if found:
                                    return found
            except Exception:
                pass
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
            if c.exists() and c.resolve() != self.pdf_path.resolve():
                return [c]
        return []

    def _detect_subject_and_level(self):
        """Detect subject (maths, english_writing, english_reading, dfs) and level (1, 2, e3) from path/cover text."""
        fname = self.pdf_path.name.lower()
        full_path = str(self.pdf_path).lower()
        subject = 'maths'
        if 'digital' in full_path or '/dfs/' in full_path or 'dfsq' in full_path:
            subject = 'dfs'
        elif 'writing' in full_path:
            subject = 'english_writing'
        elif 'reading' in full_path:
            subject = 'english_reading'
        elif 'maths' in full_path:
            subject = 'maths'
        elif 'english' in full_path:
            subject = 'english_writing'

        if any(k in full_path for k in ('entry_level_3', 'entry-level-3', 'entry_3', 'entry 3', '_e3_', '/e3/')):
            level = 'e3'
        elif any(k in full_path for k in ('level_2', 'level-2', 'level 2', '/l2/', '_l2_', '-l2-', 'l2_')) or 'l2' in fname:
            level = '2'
        else:
            p0_txt = self.doc[0].get_text('text').lower() if self.total_pages > 0 else ''
            if 'level 2' in p0_txt and 'level 1' not in p0_txt:
                level = '2'
            elif 'entry 3' in p0_txt or 'entry level 3' in p0_txt:
                level = 'e3'
            else:
                level = '1'
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
        elif 'nocn' in fname:
            return 'nocn'
        return 'edexcel'

    def _has_native_right_markers(self, page, scale: float) -> bool:
        thresh = 492.0 * scale
        for blk in page.get_text("dict").get("blocks", []):
            for line in blk.get("lines", []):
                for sp in line.get("spans", []):
                    font = sp.get("font", "").lower()
                    if "kalam" in font or "caveat" in font:
                        continue
                    bbox = sp.get("bbox", [0, 0, 0, 0])
                    if bbox[0] >= thresh:
                        low = sp.get("text", "").lower()
                        if "marker" in low or "examiner" in low or "for markers" in low:
                            return True
        return False

    def check_right_margin_overflow(self):
        """Rule 1: Right-margin boundary check for handwriting & annotations (strict x <= max_x)."""
        rule_res = {'status': 'PASS', 'max_x': 0.0, 'violations': []}
        board = self._detect_board()
        
        # Subject-aware base limits for standard A4 (595.28 pt):
        if self.subject == 'english_writing':
            board_limits = {
                'edexcel': (545.0, 562.0),
                'aqa': (542.0, 560.0),
                'city-and-guilds': (545.0, 565.0),
                'ncfe': (542.0, 560.0),
                'nocn': (545.0, 562.0),
                'open-awards': (545.0, 562.0),
                'tquk': (498.0, 502.5),
            }
        elif self.subject == 'english_reading':
            board_limits = {
                'edexcel': (544.0, 562.0),
                'aqa': (485.0, 535.0),
                'city-and-guilds': (548.0, 568.0),
                'ncfe': (542.0, 560.0),
                'nocn': (545.0, 565.0),
                'open-awards': (545.0, 562.0),
                'tquk': (542.0, 560.0),
            }
        elif self.subject == 'dfs':
            board_limits = {
                'edexcel': (542.0, 560.0),
                'aqa': (542.0, 560.0),
                'city-and-guilds': (545.0, 565.0),
                'ncfe': (542.0, 560.0),
                'nocn': (545.0, 562.0),
                'open-awards': (545.0, 562.0),
                'tquk': (542.0, 560.0),
            }
        else:
            board_limits = {
                'edexcel': (485.0, 518.2),
                'aqa': (485.0, 535.0),
                'city-and-guilds': (540.0, 565.0),
                'ncfe': (520.0, 545.0),
                'nocn': (535.0, 560.0),
                'open-awards': (495.0, 515.0),
                'tquk': (535.0, 558.0),
            }
        base_max_limit, base_border_limit = board_limits.get(board, (525.0, 550.0))
        
        # Check interior pages (ignore cover, service promo, and final merch page)
        for page_idx in range(self.total_pages):
            if page_idx in (0, 1, self.total_pages - 1):
                continue
            
            page = self.doc[page_idx]
            page_text = page.get_text('text').lower()
            if ('section b' in page_text or 'section 2' in page_text or 'part b' in page_text or 'part 2' in page_text) and ('calculator' in page_text or 'pmat' in page_text or 'candidate' in page_text or 'check that you have' in page_text or 'solutions' in page_text or 'prac' in page_text):
                continue

            # Scale boundaries proportionally to page width (e.g. 652 pt Crown Quarto vs 595.3 pt A4)
            scale = page.rect.width / 595.28
            eff_max, eff_border = base_max_limit, base_border_limit
            if self.subject in ('english_reading', 'english_writing', 'dfs') and board in ('open-awards', 'aqa'):
                if self._has_native_right_markers(page, scale):
                    if board == 'open-awards':
                        eff_max, eff_border = min(eff_max, 495.0), min(eff_border, 515.0)
                    elif board == 'aqa':
                        eff_max, eff_border = min(eff_max, 485.0), min(eff_border, 535.0)
            max_limit = eff_max * scale
            border_limit = eff_border * scale
            if any(k in page_text for k in ('mfs active reading guide', 'mfs active reading source guide', 'annotated source', 'exam board source booklet')):
                is_full_sheet = (max(page.rect.width, page.rect.height) >= 760.0 and min(page.rect.width, page.rect.height) >= 580.0)
                max_limit = (576.0 if is_full_sheet else 538.0) * scale
                border_limit = (590.0 if is_full_sheet else 544.0) * scale

            text_dict = page.get_text('dict')
            for block in text_dict.get('blocks', []):
                for line in block.get('lines', []):
                    for span in line.get('spans', []):
                        font = span.get('font', '').lower()
                        txt = span.get('text', '').strip()
                        if not txt:
                            continue
                        
                        # Identify whether span is an injected handwriting/annotation (exclude pure-black original QP fonts like MaturaMTScriptCapitals)
                        color = span.get('color', 0)
                        is_annot_font = any(f in font for f in ['kalam', 'caveat']) or (_is_chromatic_color(color) and any(f in font for f in ['script', 'hand']))
                        is_pedagogical_color = color in GOLD_COLOR_SET or color in WRONG_PFS_COLORS
                        
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
            m = re.search(r'\*[A-Za-z0-9_]+\*', p.get_text('text'))
            if m:
                orig_map[m.group(0).lower()] = i

        for p_idx in range(self.total_pages):
            if p_idx in (0, 1, self.total_pages - 1):
                continue
            annot_page = self.doc[p_idx]
            page_text = annot_page.get_text('text').lower()
            if ('section b' in page_text or 'section 2' in page_text or 'part b' in page_text or 'part 2' in page_text) and ('calculator' in page_text or 'candidate' in page_text or 'pmat' in page_text or 'check that you have' in page_text):
                continue
            if ('annotated source insert' in page_text or 'mfs active reading source guide' in page_text
                    or 'examiner assessment' in page_text or 'additional writing space' in page_text):
                continue

            is_insert_page = ('mfs active reading guide' in page_text)
            orig_page = None
            if not is_insert_page:
                m = re.search(r'\*[A-Za-z0-9_]+\*', annot_page.get_text('text'))
                if m and m.group(0).lower() in orig_map:
                    orig_page = self.orig_doc[orig_map[m.group(0).lower()]]
                else:
                    # Global max-overlap match using ONLY underlying printed QP spans (ignores our handwritten essays/solutions!)
                    cand_idx = p_idx - 1 if (p_idx - 1 < len(self.orig_doc)) else None
                    annot_word_set = set()
                    for blk in annot_page.get_text('dict').get('blocks', []):
                        for ln in blk.get('lines', []):
                            for sp in ln.get('spans', []):
                                fn = sp.get('font', '').lower()
                                col = sp.get('color', 0)
                                is_ann = any(f in fn for f in ['kalam', 'caveat']) or (_is_chromatic_color(col) and any(f in fn for f in ['script', 'hand'])) or col in GOLD_COLOR_SET or col in WRONG_PFS_COLORS
                                if not is_ann:
                                    for tok in sp.get('text', '').lower().split():
                                        if len(tok) >= 2:
                                            annot_word_set.add(tok)
                    best_idx, best_overlap = -1, 0
                    for o_idx, o_page in enumerate(self.orig_doc):
                        o_word_set = set(w[4].lower() for w in o_page.get_text('words') if len(w[4]) >= 2)
                        overlap = len(annot_word_set & o_word_set)
                        # Small tie-breaker (+0.5) if candidate offset aligns directly
                        score = overlap + (0.5 if o_idx == cand_idx else 0.0)
                        if score > best_overlap:
                            best_overlap = score
                            best_idx = o_idx
                    if best_idx >= 0 and best_overlap >= 3:
                        orig_page = self.orig_doc[best_idx]
                    elif cand_idx is not None and len(self.orig_doc[cand_idx].get_text('words')) <= 15:
                        orig_page = self.orig_doc[cand_idx]
                    elif best_idx >= 0:
                        orig_page = self.orig_doc[best_idx]
                    else:
                        continue

            # 1. Collect original words (ignore underlines and barcodes)
            orig_words = []
            if is_insert_page:
                for block in annot_page.get_text('dict').get('blocks', []):
                    for line in block.get('lines', []):
                        for span in line.get('spans', []):
                            f = span.get('font', '').lower()
                            c = span.get('color', 0)
                            t = span.get('text', '').strip()
                            if not t or any(k in f for k in ['kalam', 'caveat', 'helvetica']) or c in GOLD_COLOR_SET or c in WRONG_PFS_COLORS or c == 0xffffff:
                                continue
                            orig_words.append((pymupdf.Rect(span['bbox']), t))
            else:
                for w in orig_page.get_text('words'):
                    txt = w[4].strip()
                    if not txt or '*P' in txt or txt.startswith('*') or '....' in txt or re.fullmatch(r'[\s._\-–—…\.]+', txt):
                        continue
                    if '____' in txt:
                        # Keep printed prefix box (e.g. 'Answer' in 'Answer_______', '1)' in '1)_____')
                        pref = txt.split('____')[0].strip()
                        if pref:
                            r_full = pymupdf.Rect(w[:4])
                            frac = len(pref) / max(1, len(txt))
                            r_pref = pymupdf.Rect(r_full.x0, r_full.y0, r_full.x0 + r_full.width * frac, r_full.y1)
                            orig_words.append((r_pref, pref))
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
                        is_annot = any(f in font for f in ['kalam', 'caveat']) or (_is_chromatic_color(color) and any(f in font for f in ['script', 'hand'])) or color in GOLD_COLOR_SET or color in WRONG_PFS_COLORS
                        if is_annot:
                            annot_words.append((pymupdf.Rect(span['bbox']), txt))

            # 3. Check for physical bounding box collisions
            for ar, atxt in annot_words:
                for ow_r, ow_txt in orig_words:
                    # Skip if the span in annot_page is an original QP word printed in a script/hand font colliding with itself
                    if (atxt.strip('\x08 ') == ow_txt.strip('\x08 ') or ow_txt.strip('\x08 ') in atxt.strip('\x08 ')) and (abs(ar.x0 - ow_r.x0) < 5.0 or abs(ar.x1 - ow_r.x1) < 5.0) and abs(ar.y0 - ow_r.y0) < 4.5:
                        continue
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
                        
                        is_annot_font = any(f in font for f in ['kalam', 'caveat']) or (_is_chromatic_color(color) and any(f in font for f in ['script', 'hand']))
                        is_pedagogical_color = color in GOLD_COLOR_SET or color in WRONG_PFS_COLORS
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
        if self.level in ('1', '2'):
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

    def check_pedagogical_authenticity(self):
        """Rule 7: Verify presence of genuine MFS pedagogical ink layers and absence of competitor raw handwriting."""
        rule_res = {
            'status': 'PASS',
            'mfs_font_spans': 0,
            'pedagogical_color_spans': 0,
            'gold_palette_spans': 0,
            'wrong_pfs_palette_spans': 0,
            'caveat_spans': 0,
            'median_font_size': 0.0,
            'self_collisions': 0,
            'missing_diagram_pages': [],
            'mupdf_warnings': [],
            'competitor_ink_annots': 0,
            'competitor_drawings': 0,
            'mark_tags_found': 0,
            'annotated_question_pages': 0,
            'total_question_pages': 0,
            'blank_page_violations': [],
            'violations': []
        }

        # Check MuPDF syntax/pattern errors cleanly
        pymupdf.TOOLS.mupdf_warnings(reset=True)
        for p in self.doc:
            _ = p.get_text("words")
        mwarn = pymupdf.TOOLS.mupdf_warnings()
        if "cannot find Pattern" in mwarn or "syntax error" in mwarn:
            rule_res['mupdf_warnings'].append(mwarn.strip()[:240])

        # Scan interior pages (exclude cover p0, service promo p1, and final merch promo)
        interior_start = min(2, self.total_pages - 1)
        interior_end = max(interior_start, self.total_pages - 1)

        total_interior_pages = max(1, interior_end - interior_start)
        hand_sizes = []

        for p_idx in range(interior_start, interior_end):
            page = self.doc[p_idx]
            page_text = page.get_text('text').lower()

            # Identify if page is intentionally blank, end-of-assessment filler, or a standalone synthetic assessment card
            is_intentionally_blank = 'intentionally blank' in page_text or 'blank page' in page_text
            has_kalam_or_caveat = any(
                any(f in s.get('font', '').lower() for f in ('kalam', 'caveat'))
                for b in page.get_text('dict').get('blocks', [])
                for ln in b.get('lines', [])
                for s in ln.get('spans', [])
            )
            if self.subject == 'english_writing' and 'examiner assessment' in page_text and not has_kalam_or_caveat:
                continue
            if self.subject == 'english_writing':
                if 'end of assessment' in page_text and not has_kalam_or_caveat:
                    is_question_page = False
                else:
                    # Stimulus/prompt-only pages (e.g. AQA 'Remember to:', Edexcel 'Information', C&G 'You will be assessed on:')
                    has_wide_rules = any(dr.get('rect') and dr['rect'].width > 250 and dr['rect'].height < 4 for dr in page.get_drawings())
                    has_dots = any('....' in ln or '____' in ln for ln in page_text.splitlines())
                    is_stimulus_only = (
                        not has_kalam_or_caveat
                        and (
                            ('begins on the next page' in page_text)
                            or ('information' in page_text and not has_dots)
                            or (
                                any(k in page_text for k in ('remember to:', 'make notes', 'assessment task sheet', 'you must', 'you will be assessed on', 'sample paper'))
                                and not has_wide_rules and not has_dots
                                and ('write the ' not in page_text and 'write your ' not in page_text and 'email here' not in page_text and 'letter here' not in page_text and 'article here' not in page_text and 'report here' not in page_text and 'continued' not in page_text)
                            )
                        )
                    )
                    is_question_page = has_kalam_or_caveat or (
                        not is_stimulus_only and (
                            has_dots or any(w in page_text for w in ['write the ', 'write your ', 'write an ', 'task 1', 'task 2', 'question', 'email here', 'letter here', 'article here', 'report here', 'continued'])
                        )
                    )
            elif self.subject == 'english_reading':
                is_source_or_decl = any(k in page_text for k in (
                    'mfs active reading', 'use this document to answer',
                    'do not write your answers', 'source overview',
                    'prior knowledge', 'candidate name',
                ))
                if is_source_or_decl:
                    is_question_page = False
                else:
                    is_question_page = has_kalam_or_caveat or any(w in page_text for w in ['question', 'marks)', 'mark)', 'what is', 'identify', 'explain'])
            else:
                is_question_page = any(w in page_text for w in ['question', 'task', 'calculate', 'what is', 'show your', 'answer'])

            if is_question_page:
                rule_res['total_question_pages'] += 1

            page_mfs_spans = 0
            page_annot_boxes = []

            # 1. Detect competitor Ink annotations
            for annot in page.annots():
                if annot.type[1] == 'Ink':
                    rule_res['competitor_ink_annots'] += 1
                    rule_res['violations'].append({
                        'page': p_idx + 1,
                        'issue': 'Competitor Ink annotation detected (raw scanned/vector handwriting)'
                    })

            # 2. Detect competitor vector drawings & count MFS diagram vector items
            drawings = page.get_drawings()
            mfs_colored_items = 0
            for d in drawings:
                items_list = d.get('items', [])
                item_cnt = sum(4 if it[0] in ('re', 'qu') else 1 for it in items_list) if items_list else 1
                matched_mfs = False
                for ck in ('color', 'fill'):
                    c = d.get(ck)
                    if c and len(c) >= 3:
                        if ck == 'color' and c[0] == 0.0 and c[1] == 0.0 and c[2] == 1.0:
                            rule_res['competitor_drawings'] += 1
                        elif ck == 'color' and 0.85 < c[0] < 0.95 and c[1] < 0.2 and 0.18 < c[2] < 0.25:
                            rule_res['competitor_drawings'] += 1
                        elif max(c) - min(c) > 0.15:
                            matched_mfs = True
                if matched_mfs:
                    mfs_colored_items += item_cnt

            # Diagram-question verification (Maths only: trigger only on active draw/plot/complete imperatives)
            if self.subject == 'maths' and ('section' not in page_text or 'question' in page_text or 'marks)' in page_text or 'mark)' in page_text):
                if any(kw in page_text for kw in ['draw a ', 'draw the ', 'plot this', 'plot the', 'complete the graph', 'complete the bar', 'complete the pie', 'complete the chart', 'line of best fit', 'draw a scale']):
                    eff_items = mfs_colored_items
                    if ('page opposite' in page_text or 'opposite page' in page_text or 'next page' in page_text or 'use the grid' in page_text or 'grid on' in page_text) and p_idx + 1 < interior_end:
                        for d2 in self.doc[p_idx + 1].get_drawings():
                            if any(d2.get(ck) and len(d2[ck]) >= 3 and max(d2[ck]) - min(d2[ck]) > 0.15 for ck in ('color', 'fill')):
                                il2 = d2.get('items', [])
                                eff_items += sum(4 if it[0] in ('re', 'qu') else 1 for it in il2) if il2 else 1
                    if eff_items < 1:
                        rule_res['missing_diagram_pages'].append(p_idx + 1)

            # 3. Detect authentic MFS pedagogical text layers & fonts
            text_dict = page.get_text('dict')
            for block in text_dict.get('blocks', []):
                for line in block.get('lines', []):
                    for span in line.get('spans', []):
                        font = span.get('font', '').lower()
                        color = span.get('color', 0)
                        txt = span.get('text', '').strip()
                        if not txt:
                            continue
                        bbox = pymupdf.Rect(span['bbox'])
                        if bbox.y0 < 34.0:
                            continue  # skip optional compact running header

                        if any(f in font for f in ['kalam', 'caveat']):
                            rule_res['mfs_font_spans'] += 1
                            page_mfs_spans += 1
                            hand_sizes.append(round(span.get('size', 0), 1))
                            page_annot_boxes.append((bbox, txt))
                            if 'caveat' in font:
                                rule_res['caveat_spans'] += 1
                            if color in WRONG_PFS_COLORS:
                                rule_res['wrong_pfs_palette_spans'] += 1

                        if color in GOLD_COLOR_SET:
                            rule_res['pedagogical_color_spans'] += 1
                            rule_res['gold_palette_spans'] += 1
                        elif color in WRONG_PFS_COLORS:
                            rule_res['pedagogical_color_spans'] += 1

                        if re.search(r'\[(?:M\d|A\d|B\d|P\d|R\d|W\d|\d+\s*marks?|1\s*mark)\]', txt, re.IGNORECASE):
                            rule_res['mark_tags_found'] += 1

            # Self-collision check using core ink height (trimmed for Kalam/Caveat ascender/descender padding)
            def _core_ink(rect):
                h = rect.height
                return pymupdf.Rect(rect.x0, rect.y0 + 0.24 * h, rect.x1, rect.y1 - 0.22 * h)

            for i in range(len(page_annot_boxes)):
                for j in range(i + 1, len(page_annot_boxes)):
                    r1, t1 = page_annot_boxes[i]
                    r2, t2 = page_annot_boxes[j]
                    c1, c2 = _core_ink(r1), _core_ink(r2)
                    inter = c1 & c2
                    if inter.is_valid and inter.width > 5.0 and inter.height > 3.5:
                        # Ignore tiny adjacent tokens or stacked numerator/denominator digits
                        if len(t1) <= 4 and len(t2) <= 4 and t1.replace('.','').isdigit() and t2.replace('.','').isdigit():
                            continue
                        rule_res['self_collisions'] += 1

            if page_mfs_spans > 0:
                if is_question_page:
                    rule_res['annotated_question_pages'] += 1
                if is_intentionally_blank:
                    rule_res['blank_page_violations'].append({
                        'page': p_idx + 1,
                        'spans': page_mfs_spans,
                        'issue': 'Handwritten solution spans detected on page marked "Intentionally Blank"'
                    })

        if hand_sizes:
            hand_sizes.sort()
            rule_res['median_font_size'] = hand_sizes[len(hand_sizes) // 2]

        # Evaluate violations
        if rule_res['mupdf_warnings']:
            rule_res['status'] = 'FAIL'
            self.results['errors'].append(f"PDF Integrity Failure: MuPDF warnings detected ({rule_res['mupdf_warnings'][0][:80]})")
        elif rule_res['competitor_ink_annots'] > 0:
            rule_res['status'] = 'FAIL'
            self.results['errors'].append(f"Authenticity Failure: Found {rule_res['competitor_ink_annots']} raw competitor Ink annotation(s) inside paper.")
        elif rule_res['competitor_drawings'] > 10:
            rule_res['status'] = 'FAIL'
            self.results['errors'].append(f"Authenticity Failure: Found {rule_res['competitor_drawings']} raw competitor vector handwriting stroke(s) inside paper.")
        elif rule_res['wrong_pfs_palette_spans'] > 8 and rule_res['gold_palette_spans'] < 15:
            rule_res['status'] = 'FAIL'
            self.results['errors'].append(f"Style Drift Failure: Found {rule_res['wrong_pfs_palette_spans']} PFS/wrong-palette spans (#0f172a/#0f766e/#dc2626) instead of Edexcel L2 Gold palette (#0f47ad/#14843d/#d11f26).")
        elif rule_res['self_collisions'] > 0:
            rule_res['status'] = 'FAIL'
            self.results['errors'].append(f"Self-Collision Failure: {rule_res['self_collisions']} overlapping annotation span(s) detected.")
        elif rule_res['missing_diagram_pages']:
            rule_res['status'] = 'FAIL'
            self.results['errors'].append(f"Diagram Missing: Graph/chart/scale question page(s) {rule_res['missing_diagram_pages']} lack vector diagram drawings.")
        elif rule_res['blank_page_violations']:
            rule_res['status'] = 'FAIL'
            self.results['errors'].append(f"Layout Failure: {len(rule_res['blank_page_violations'])} page(s) have handwriting written on blank/overflow pages instead of designated answer areas.")
        elif rule_res['mfs_font_spans'] < 10 and rule_res['pedagogical_color_spans'] < 10:
            rule_res['status'] = 'FAIL'
            self.results['errors'].append("Authenticity Failure: Insufficient MFS pedagogical ink layers detected on interior pages (wrapper-only document).")
        elif self.subject == 'maths' and rule_res['median_font_size'] < 11.5:
            rule_res['status'] = 'FAIL'
            self.results['errors'].append(f"Font Size Too Small: Maths median font size is {rule_res['median_font_size']}pt (expected >= 12.0pt per Edexcel L2 Gold Template).")
        elif self.subject == 'maths' and rule_res['caveat_spans'] < 3:
            rule_res['status'] = 'WARNING'
            self.results['warnings'].append("Low Tutor Feedback: Fewer than 3 Caveat Emerald tutor feedback spans detected.")
        elif rule_res['total_question_pages'] > 5 and (rule_res['annotated_question_pages'] / max(1, rule_res['total_question_pages'])) < 0.5:
            rule_res['status'] = 'FAIL'
            cov_pct = round((rule_res['annotated_question_pages'] / max(1, rule_res['total_question_pages'])) * 100, 1)
            self.results['errors'].append(f"Incomplete Paper: Only {rule_res['annotated_question_pages']} of {rule_res['total_question_pages']} question pages ({cov_pct}%) have worked solutions.")

        # Subject-specific English checks (Reading source highlights; Writing word count badge)
        full_doc_txt = "\n".join(p.get_text("text") for p in self.doc)
        if self.subject == 'english_reading':
            has_guide = ("ACTIVE READING" in full_doc_txt.upper() or "MFS ACTIVE READING GUIDE" in full_doc_txt.upper())
            # Also count translucent highlight fills on interior pages
            hl_rects = 0
            for p_idx in range(interior_start, interior_end):
                for dr in self.doc[p_idx].get_drawings():
                    fo = dr.get("fill_opacity")
                    if fo is not None and 0.05 < fo < 0.5 and dr.get("fill"):
                        hl_rects += 1
            if not has_guide or hl_rects < 3:
                rule_res['status'] = 'FAIL'
                self.results['errors'].append(f"Reading Guidance Missing: has_guide={has_guide}, highlight_rects={hl_rects} (requires Active Reading guidance + source text highlights).")
        elif self.subject == 'english_writing':
            if "Verified Word Count:" not in full_doc_txt:
                rule_res['status'] = 'WARNING'
                self.results['warnings'].append("Writing Word Count Card missing 'Verified Word Count:' examiner badge.")

        self.results['rules']['authenticity'] = rule_res
        return rule_res

    def _is_special_non_working_page(self, page_text: str) -> bool:
        low = page_text.lower()
        if ('section b' in low or 'section 2' in low or 'part b' in low or 'part 2' in low) and (
            'calculator' in low or 'pmat' in low or 'candidate' in low or 'check that you have' in low or 'instructions to learners' in low
        ):
            return True
        if any(k in low for k in (
            'annotated source insert',
            'mfs active reading guide',
            'mfs active reading source guide',
            'annotated source',
            'exam board source booklet',
        )):
            return True
        return False

    def _assess_card_top_y(self, page) -> float:
        top = 9999.0
        for blk in page.get_text('dict').get('blocks', []):
            for line in blk.get('lines', []):
                txt = "".join(s.get('text', '') for s in line.get('spans', [])).lower()
                if 'examiner assessment' in txt or 'verified word count' in txt:
                    for s in line.get('spans', []):
                        top = min(top, float(s.get('bbox', [0, 9999])[1]))
        return top

    def check_typography_standards(self):
        """Rule 8: Full-size Edexcel Gold font standards (Kalam median >= 13.2 Maths/DFS, >= 12.8 Reading/Writing)."""
        rule_res = {'status': 'PASS', 'median_kalam': None, 'min_long_kalam': None, 'violations': []}
        kalam_weights: list[tuple[float, int]] = []
        long_violations: list[dict] = []
        body_violations: list[dict] = []
        long_char_total = 0
        long_char_ok = 0
        min_long = 99.0

        for page_idx in range(2, max(2, self.total_pages - 1)):
            page = self.doc[page_idx]
            ptxt = page.get_text('text')
            if self._is_special_non_working_page(ptxt):
                continue
            assess_y = self._assess_card_top_y(page)
            diag_boxes = []
            if self.subject in ('maths', 'dfs'):
                for dr in page.get_drawings():
                    dr_r = dr.get('rect')
                    if dr_r and dr_r.width >= 20.0 and 15.0 <= dr_r.height <= 260.0:
                        if any(dr.get(ck) and len(dr[ck]) >= 3 and max(dr[ck][:3]) - min(dr[ck][:3]) > 0.12 for ck in ('color', 'fill')):
                            diag_boxes.append(dr_r)
            for blk in page.get_text('dict').get('blocks', []):
                for line in blk.get('lines', []):
                    for sp in line.get('spans', []):
                        font = sp.get('font', '').lower()
                        txt = sp.get('text', '').strip()
                        bbox = sp.get('bbox', [0, 0, 0, 0])
                        if not txt or bbox[1] <= 26.0 or bbox[1] >= assess_y - 4.0:
                            continue
                        sz = round(float(sp.get('size', 0.0)), 1)
                        if 'kalam' in font:
                            kalam_weights.append((sz, len(txt)))
                            if len(txt) >= 14:
                                sp_rect = pymupdf.Rect(bbox)
                                in_diag = bool(diag_boxes) and any(
                                    db.contains(sp_rect)
                                    or ((db & sp_rect).is_valid and (
                                        (db & sp_rect).get_area() >= 0.7 * max(1.0, sp_rect.get_area())
                                        or (db & sp_rect).get_area() >= 0.15 * max(1.0, db.get_area())
                                        or (db.y0 - 2.0 <= sp_rect.y0 and sp_rect.y1 <= db.y1 + 2.0 and (db & sp_rect).width >= 15.0)
                                    ))
                                    for db in diag_boxes
                                )
                                if in_diag:
                                    continue
                                long_char_total += len(txt)
                                if sz < min_long:
                                    min_long = sz
                                min_req = 11.8 if self.subject in ('maths', 'dfs') else 11.6
                                if sz >= min_req:
                                    long_char_ok += len(txt)
                                else:
                                    info = {'page': page_idx + 1, 'size': sz, 'text': txt[:36]}
                                    long_violations.append(info)
                                    if len(txt) >= 28 or self.subject in ('english_reading', 'english_writing'):
                                        body_violations.append(info)

        if kalam_weights:
            kalam_weights.sort(key=lambda t: t[0])
            total_w = sum(w for _, w in kalam_weights)
            acc = 0
            med = kalam_weights[0][0]
            for sz, w in kalam_weights:
                acc += w
                if acc >= total_w * 0.5:
                    med = sz
                    break
            rule_res['median_kalam'] = med
            rule_res['min_long_kalam'] = min_long if min_long < 99.0 else med

            target_med = 13.2 if self.subject in ('maths', 'dfs') else 12.8
            if med < target_med:
                rule_res['status'] = 'FAIL'
                self.results['errors'].append(
                    f"Typography Size Too Small: char-weighted median Kalam is {med}pt (requires >= {target_med}pt for {self.subject})."
                )
        pct_ok = (long_char_ok / long_char_total) if long_char_total > 0 else 1.0
        fail_spans = body_violations if (self.subject in ('maths', 'dfs') and pct_ok >= 0.85) else long_violations
        if fail_spans:
            rule_res['violations'] = fail_spans[:10]
            if rule_res['status'] == 'PASS':
                rule_res['status'] = 'FAIL'
            self.results['errors'].append(
                f"Small Long Kalam Spans ({len(fail_spans)}): e.g. p.{fail_spans[0]['page']} {fail_spans[0]['size']}pt '{fail_spans[0]['text']}'."
            )

        self.results['rules']['typography_standards'] = rule_res
        return rule_res

    def check_line_alignment_and_fill(self):
        """Rule 9: Printed-line baseline snapping & full-width paragraph line fill check."""
        rule_res = {'status': 'PASS', 'misaligned': [], 'underfilled': []}
        if self.subject not in ('english_writing', 'english_reading', 'maths'):
            self.results['rules']['line_alignment_fill'] = rule_res
            return rule_res

        board = self._detect_board()
        try:
            from mfs_model_engine.core.geometry_detector import inspect_page, detect_raster_ruled_lines
            from mfs_model_engine.core.style_template import get_font_objs
            kreg_font = get_font_objs().get('kalam-reg')
        except Exception:
            inspect_page = None
            detect_raster_ruled_lines = None
            kreg_font = None

        if inspect_page is None:
            self.results['rules']['line_alignment_fill'] = rule_res
            return rule_res

        for page_idx in range(2, max(2, self.total_pages - 1)):
            page = self.doc[page_idx]
            ptxt = page.get_text('text')
            if self._is_special_non_working_page(ptxt):
                continue
            assess_y = self._assess_card_top_y(page)
            geom = inspect_page(page, board=board, subject=self.subject)
            vert_xs = []
            colored_boxes = []
            for dr in page.get_drawings():
                r = dr.get('rect')
                if not r:
                    continue
                if r.width <= 2.0 and r.height >= 24.0:
                    vert_xs.append((r.x0, r.y0, r.y1))
                elif self.subject == 'maths' and r.height >= 14.0 and r.width >= 15.0:
                    if any(dr.get(ck) and len(dr[ck]) >= 3 and max(dr[ck][:3]) - min(dr[ck][:3]) > 0.12 for ck in ('color', 'fill')):
                        colored_boxes.append(r)
                for it in dr.get('items', []):
                    if it[0] == 'l':
                        p1, p2 = it[1], it[2]
                        if abs(p1.x - p2.x) <= 1.5 and abs(p1.y - p2.y) >= 24.0:
                            vert_xs.append((p1.x, min(p1.y, p2.y), max(p1.y, p2.y)))
                    elif it[0] == 're' and it[1].height >= 24.0 and it[1].width >= 15.0:
                        rr = it[1]
                        vert_xs.append((rr.x0, rr.y0, rr.y1))
                        vert_xs.append((rr.x1, rr.y0, rr.y1))
            min_rw = 270.0 if self.subject == 'maths' else 85.0
            rules = [
                (ln[0], ln[1], min(ln[2], geom.right_margin_limit))
                for ln in geom.ruled_lines
                if (ln[2] - ln[0]) >= min_rw and 65.0 <= ln[1] <= 775.0
                and not any(ln[0] + 12.0 <= vx <= ln[2] - 12.0 and vy0 <= ln[1] - 4.0 and vy1 >= ln[1] + 4.0 for vx, vy0, vy1 in vert_xs)
                and not any((abs(ln[1] - br.y0) <= 3.0 or abs(ln[1] - br.y1) <= 3.0) and ln[2] >= br.x0 - 8.0 and ln[0] <= br.x1 + 8.0 for br in colored_boxes)
            ]
            if self.subject == 'english_writing' and len(rules) < 4 and detect_raster_ruled_lines is not None:
                r_cands = detect_raster_ruled_lines(page, min_y=70.0)
                # Filter out unequal email input box header edges at y <= 220 (e.g. 36pt To/Subject boxes)
                for ri, rln in enumerate(r_cands):
                    if rln[1] <= 220.0:
                        gaps = [abs(r_cands[j][1] - rln[1]) for j in (ri - 1, ri + 1) if 0 <= j < len(r_cands)]
                        if gaps and (max(gaps) > 32.0 or min(gaps) < 16.0):
                            continue
                    rules.append((rln[0], rln[1], min(rln[2], geom.right_margin_limit)))
            # Deduplicate vertical rule y within 3pt keeping widest x-span
            rules.sort(key=lambda t: (t[1], -(t[2] - t[0])))
            dedup_rules: list[tuple[float, float, float]] = []
            for ln in rules:
                if not dedup_rules or abs(ln[1] - dedup_rules[-1][1]) >= 3.5:
                    dedup_rules.append(ln)
            ys_sorted = [r[1] for r in dedup_rules]

            # Identify whether page uses a regular ruled sequence
            ruled_block_ys: set[float] = set()
            if self.subject == 'maths':
                gaps = [ys_sorted[k + 1] - ys_sorted[k] for k in range(len(ys_sorted) - 1)]
                for i in range(len(gaps)):
                    if not (18.0 <= gaps[i] <= 38.0):
                        continue
                    g_min = g_max = gaps[i]
                    j = i + 1
                    while j < len(gaps) and (18.0 <= gaps[j] <= 38.0):
                        cand_min = min(g_min, gaps[j])
                        cand_max = max(g_max, gaps[j])
                        if cand_max - cand_min > 4.0:
                            break
                        g_min, g_max = cand_min, cand_max
                        j += 1
                    if (j - i) >= 2:  # >= 3 uniformly spaced rules
                        for k in range(i, j + 1):
                            ruled_block_ys.add(ys_sorted[k])
            else:
                for a, b in zip(ys_sorted, ys_sorted[1:]):
                    if 14.0 <= (b - a) <= 42.0:
                        ruled_block_ys.add(a)
                        ruled_block_ys.add(b)

            if self.subject == 'maths' and len(ruled_block_ys) < 3:
                continue

            body_lines: list[dict] = []
            for blk in page.get_text('dict').get('blocks', []):
                for line in blk.get('lines', []):
                    for sp in line.get('spans', []):
                        font = sp.get('font', '').lower()
                        txt = sp.get('text', '').strip()
                        bbox = sp.get('bbox', [0, 0, 0, 0])
                        orig = sp.get('origin', (bbox[0], bbox[3]))
                        by = float(orig[1])
                        if not txt or 'kalam' not in font or by <= 28.0 or by >= assess_y - 4.0:
                            continue

                        if self.subject == 'maths' and colored_boxes:
                            sp_r = pymupdf.Rect(bbox)
                            if any(
                                br.contains(sp_r)
                                or (
                                    (br.y0 - 4.0 <= sp_r.y0 <= br.y1 + 4.0 or br.y0 - 4.0 <= sp_r.y1 <= br.y1 + 4.0)
                                    and sp_r.x0 >= br.x0 - 150.0 and sp_r.x1 <= br.x1 + 25.0
                                    and br.height >= 16.0
                                )
                                for br in colored_boxes
                            ):
                                continue

                        # Alignment against regular ruled block lines (len >= 6 skips fraction digits)
                        if len(txt) >= 6 and len(ruled_block_ys) >= 2:
                            over = [
                                ln for ln in dedup_rules
                                if ln[1] in ruled_block_ys
                                and bbox[2] > ln[0] + 6.0 and bbox[0] < ln[2] - 6.0
                                and -13.0 <= (by - ln[1]) <= 4.0
                            ]
                            if over:
                                nearest = min(over, key=lambda ln: abs(ln[1] - by))
                                above = nearest[1] - by
                                # Only flag floating-in-middle when an upper neighbour rule sits 14..42pt above nearest
                                has_upper = any(14.0 <= (nearest[1] - uy) <= 42.0 for uy in ruled_block_ys)
                                max_above = 7.8 if self.subject == 'maths' else 7.4
                                if (above > max_above and has_upper) or above < -2.2:
                                    rule_res['misaligned'].append({
                                        'page': page_idx + 1,
                                        'rule_y': nearest[1],
                                        'base_y': round(by, 1),
                                        'above_pt': round(above, 1),
                                        'text': txt[:32],
                                    })

                        if self.subject == 'english_writing' and 'regular' in font:
                            body_lines.append({
                                'y': by,
                                'x0': float(bbox[0]),
                                'x1': float(bbox[2]),
                                'text': txt,
                                'fs': float(sp.get('size', 13.5)),
                            })

            # Writing full-width wrap check on consecutive body lines
            if self.subject == 'english_writing' and len(body_lines) >= 2 and kreg_font is not None:
                body_lines.sort(key=lambda d: (d['y'], d['x0']))
                merged_lines: list[dict] = []
                for seg in body_lines:
                    if merged_lines and abs(seg['y'] - merged_lines[-1]['y']) <= 3.0:
                        m = merged_lines[-1]
                        m['x0'] = min(m['x0'], seg['x0'])
                        m['x1'] = max(m['x1'], seg['x1'])
                        m['text'] = (m['text'] + ' ' + seg['text']).strip()
                    else:
                        merged_lines.append(dict(seg))

                for cur, nxt in zip(merged_lines, merged_lines[1:]):
                    dy = nxt['y'] - cur['y']
                    if not (13.5 <= dy <= 34.0) or abs(nxt['x0'] - cur['x0']) > 14.0:
                        continue
                    ct = cur['text'].lstrip()
                    nt = nxt['text'].lstrip()
                    if not ct or not nt or ct[0] in '*-•' or nt[0] in '*-•' or re.match(r'^\d+[.)]', nt):
                        continue
                    if ct.endswith(('.', '!', '?', ':', ',')):
                        continue
                    if cur['y'] < 325.0 and len(ct) <= 52:
                        continue
                    c_low, n_low = ct.lower(), nt.lower()
                    fmt_keys = (
                        'yours faithfully', 'yours sincerely', 'kind regards', 'best wishes',
                        'speak soon', 'dear ', 'many thanks', 'from:', 'to:', 'subject:', 'date:', 're:'
                    )
                    if any(k in c_low or k in n_low for k in fmt_keys):
                        continue
                    matched_r = [
                        ln for ln in dedup_rules
                        if abs(ln[1] - cur['y']) <= 8.0 and cur['x0'] >= ln[0] - 8.0
                    ]
                    eff_end = min(matched_r[0][2] - 2.0, geom.right_margin_limit - 2.0) if matched_r else (geom.right_margin_limit - 4.0)
                    line_span = max(1.0, eff_end - cur['x0'])
                    fill_ratio = (cur['x1'] - cur['x0']) / line_span
                    remaining = eff_end - cur['x1']
                    first_w = nt.split()[0]
                    fw_px = kreg_font.text_length(first_w, fontsize=cur['fs'])
                    if remaining > fw_px + 20.0 and fill_ratio < 0.72:
                        rule_res['underfilled'].append({
                            'page': page_idx + 1,
                            'y': round(cur['y'], 1),
                            'fill_pct': round(fill_ratio * 100.0, 1),
                            'remaining_pt': round(remaining, 1),
                            'next_word_pt': round(fw_px, 1),
                            'text': ct[-32:],
                        })

        if rule_res['misaligned']:
            rule_res['status'] = 'FAIL'
            m0 = rule_res['misaligned'][0]
            self.results['errors'].append(
                f"Off-Line Baseline ({len(rule_res['misaligned'])} spans): p.{m0['page']} base_y={m0['base_y']} vs rule_y={m0['rule_y']} (above={m0['above_pt']}pt)."
            )
            rule_res['misaligned'] = rule_res['misaligned'][:10]
        if rule_res['underfilled']:
            rule_res['status'] = 'FAIL'
            u0 = rule_res['underfilled'][0]
            self.results['errors'].append(
                f"Underfilled Writing Line ({len(rule_res['underfilled'])}): p.{u0['page']} fill={u0['fill_pct']}% rem={u0['remaining_pt']}pt > next '{u0['next_word_pt']}pt'."
            )
            rule_res['underfilled'] = rule_res['underfilled'][:10]

        self.results['rules']['line_alignment_fill'] = rule_res
        return rule_res

    def check_math_notation(self):
        """Rule 10: Maths & DFS notation quality (obelus ÷, × multiplication, vertical stacked fractions)."""
        rule_res = {'status': 'PASS', 'violations': []}
        if self.subject not in ('maths', 'dfs'):
            self.results['rules']['math_notation'] = rule_res
            return rule_res

        date_mark_re = re.compile(
            r"(?:\b\d{1,2}\s*/\s*\d{1,2}\s*/\s*\d{2,4}\b"
            r"|\b\d+/\d+(?=\s*(?:marks?|pts?|points?|total)\b)"
            r"|(?<=\bscore\s)\d+/\d+|(?<=\bScore\s)\d+/\d+|[\[\(]\d+/\d+[\]\)])"
        )
        unstacked_frac_re = re.compile(r"(?<![\d./£$€A-Za-z_])\b(\d{1,3})/(\d{1,3})\b(?![\d./A-Za-z_])")

        for page_idx in range(2, max(2, self.total_pages - 1)):
            page = self.doc[page_idx]
            ptxt = page.get_text('text')
            if self._is_special_non_working_page(ptxt):
                continue
            for blk in page.get_text('dict').get('blocks', []):
                for line in blk.get('lines', []):
                    for sp in line.get('spans', []):
                        font = sp.get('font', '').lower()
                        txt = sp.get('text', '').strip()
                        bbox = sp.get('bbox', [0, 0, 0, 0])
                        if not txt or bbox[1] <= 26.0:
                            continue
                        if not any(f in font for f in ('kalam', 'caveat')):
                            continue
                        if txt.lstrip().startswith('='):
                            continue
                        cleaned = date_mark_re.sub(' ', txt)
                        bad_reason = None
                        if re.search(r'\b\d[\d.,%]*\s+/\s+\d', cleaned):
                            bad_reason = 'ascii_spaced_division'
                        elif re.search(r'[£$€]\d[\d,]*(?:\.\d+)?/\d|\d+\.\d+/\d', cleaned):
                            bad_reason = 'ascii_decimal_currency_division'
                        elif re.search(r'(?<=\d)\s*\*\s*(?=\d)|(?<=\d)\s+[xX]\s+(?=\d)', cleaned):
                            bad_reason = 'ascii_multiplication'
                        else:
                            for fm in unstacked_frac_re.finditer(cleaned):
                                n_s, d_s = fm.group(1), fm.group(2)
                                if d_s != '0' and n_s != d_s and not (len(d_s) > 1 and d_s.startswith('0')) and not (len(n_s) > 1 and n_s.startswith('0')):
                                    bad_reason = f'unstacked_fraction:{n_s}/{d_s}'
                                    break
                        if bad_reason:
                            rule_res['violations'].append({
                                'page': page_idx + 1,
                                'reason': bad_reason,
                                'text': txt[:45],
                            })

        if rule_res['violations']:
            rule_res['status'] = 'FAIL'
            v0 = rule_res['violations'][0]
            self.results['errors'].append(
                f"Legacy Math Notation ({len(rule_res['violations'])} spans): p.{v0['page']} {v0['reason']} in '{v0['text']}'."
            )
            rule_res['violations'] = rule_res['violations'][:10]

        self.results['rules']['math_notation'] = rule_res
        return rule_res

    def run_all_checks(self):
        """Execute full audit suite across all rules."""
        self.check_right_margin_overflow()
        self.check_text_collisions()
        self.check_red_grid_watermarks()
        self.check_typography_glyphs()
        self.check_merchandise_promo_page()
        self.check_booklet_assembly()
        self.check_pedagogical_authenticity()
        self.check_typography_standards()
        self.check_line_alignment_and_fill()
        self.check_math_notation()

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
    parser.add_argument("--render-qa", help="Optional directory to dump 150 DPI PNG page previews for visual inspection")
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

        if args.render_qa:
            qa_dir = Path(args.render_qa) / pdf_path.stem
            qa_dir.mkdir(parents=True, exist_ok=True)
            doc_qa = pymupdf.open(str(pdf_path))
            # Render cover (0), first content page (2), middle page, and any page with diagrams/last content page
            idxs = sorted(set([0, min(2, len(doc_qa)-1), len(doc_qa)//2, max(0, len(doc_qa)-2), max(0, len(doc_qa)-1)]))
            for p_i in idxs:
                pix = doc_qa[p_i].get_pixmap(dpi=150)
                pix.save(str(qa_dir / f"page_{p_i+1:02d}.png"))
            doc_qa.close()

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
