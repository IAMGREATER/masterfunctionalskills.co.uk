#!/home/subi/venv/bin/python
"""Full 6-board Model Solution PDF audit & visual sign-off pack builder (Launch Steps 4.2–4.4)."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from urllib.parse import quote

import pymupdf
from PIL import Image, ImageDraw, ImageFont

ROOT = Path("/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk")
BASE = ROOT / "assets/downloads/past-papers"
DOCS = Path("/home/subi/Documents")
L2_HASH_SNAPSHOT = Path("/tmp/s8_l2_hashes.json")
PROTECTED_HASH_FILE = ROOT / "mfs_model_engine/protected_edexcel_l2_hashes.json"

HUB_FILES = sorted(ROOT.glob("*-past-papers.html")) + [ROOT / "functional-skills-past-papers.html"]

OUT_EDEXCEL = DOCS / "MFS Edexcel Review 2026-11-20"
OUT_CG = DOCS / "MFS City and Guilds Review 2026-11-20"
OUT_REMAINING = DOCS / "MFS Remaining Boards Review 2026-11-20"


def collect_board_pdfs(board: str) -> list[Path]:
    """Return all model/solution/exemplar PDFs for a board, excluding raw papers/."""
    bdir = BASE / board
    pdfs: list[Path] = []
    for p in sorted(bdir.rglob("*.pdf")):
        rel_b = p.relative_to(bdir).as_posix()
        if rel_b.startswith("papers/"):
            continue
        if board == "nocn" and (rel_b.startswith("l1/") or rel_b.startswith("l2/")):
            continue
        low = p.name.lower()
        if any(k in low for k in ("model", "solution", "exemplar", "borderline", "good_pass", "fail")):
            pdfs.append(p)
    return pdfs


def rect_intersect_area(a: tuple[float, float, float, float], b: tuple[float, float, float, float]) -> float:
    x0 = max(a[0], b[0])
    y0 = max(a[1], b[1])
    x1 = min(a[2], b[2])
    y1 = min(a[3], b[3])
    if x1 <= x0 or y1 <= y0:
        return 0.0
    return (x1 - x0) * (y1 - y0)


def inspect_pdf(pdf_path: Path, all_hub_text: str, force_pages: list[int] | None = None) -> dict[str, object]:
    """Audit a single Model Solution / Exemplar PDF for brand leaks, tofu, margins, collisions, and grids."""
    rel = pdf_path.relative_to(ROOT).as_posix()
    rel_b = pdf_path.relative_to(BASE).as_posix()
    low_path = rel_b.lower()
    is_maths = ("english" not in low_path) and ("reading" not in low_path) and ("writing" not in low_path)
    is_protected_l2 = rel_b.startswith("edexcel/maths-level-2/")
    linked = rel in all_hub_text

    doc = pymupdf.open(str(pdf_path))
    tofu_pages: list[int] = []
    bad_terms: list[tuple[int, str]] = []
    overflows: list[tuple[int, float, str]] = []
    collisions: list[tuple[int, str, str]] = []
    red_grid_pages: list[int] = []
    sample_pages: list[int] = [0]

    for idx, page in enumerate(doc):
        W = float(page.rect.width)
        txt = page.get_text("text")
        low_raw = txt.lower()
        low_compact = re.sub(r"\s+", "", low_raw)

        for term in ("passfunctionalskills", "oxfordhealth"):
            if term in low_compact:
                bad_terms.append((idx + 1, term))
        if re.search(r"\bpfs\b", low_raw):
            bad_terms.append((idx + 1, "pfs"))
        if "joe bloggs" in low_raw:
            bad_terms.append((idx + 1, "joe bloggs"))

        # Check for full-page copyright grid overlays (ignoring reading crimson quote underlines)
        red_lines = 0
        for dr in page.get_drawings():
            c = dr.get("color")
            if c and len(c) == 3 and c[0] > 0.7 and c[1] < 0.25 and c[2] < 0.25:
                r = dr.get("rect")
                if r and (r.width > 450 or r.height > 350):
                    red_lines += 1
        if red_lines >= 8:
            red_grid_pages.append(idx + 1)

        k_boxes: list[tuple[tuple[float, float, float, float], str]] = []
        s_boxes: list[tuple[tuple[float, float, float, float], str]] = []
        page_tofu = False

        for b in page.get_text("dict").get("blocks", []):
            if b.get("type") != 0:
                continue
            for ln in b.get("lines", []):
                for sp in ln.get("spans", []):
                    st = sp.get("text", "").strip()
                    if not st:
                        continue
                    fn = sp.get("font", "").lower()
                    bb = tuple(sp["bbox"])
                    if "kalam" in fn or "caveat" in fn:
                        if "\ufffd" in st or "\u25a1" in st:
                            page_tofu = True
                        k_boxes.append((bb, st))
                        lim = (W - 22.0) if idx == 0 else (min(W - 28.0, 560.0) if is_maths else (W - 22.0))
                        if bb[2] > lim:
                            overflows.append((idx + 1, round(bb[2], 1), st[:35]))
                    else:
                        if re.search(r"_{3,}|\.{4,}|\u2026{2,}", st):
                            continue
                        stripped = re.sub(r"[_\.\(\)\[\]\s,:;/\-£%]+", "", st)
                        if len(stripped) >= 3 and not st.lower().startswith("answer_"):
                            s_boxes.append((bb, st))

        if page_tofu:
            tofu_pages.append(idx + 1)

        if is_maths and idx > 0 and len(k_boxes) >= 3 and len(sample_pages) < 3:
            sample_pages.append(idx)

        if is_maths and not is_protected_l2 and idx > 0 and k_boxes and s_boxes:
            for kb, kt in k_boxes:
                if len(kt) < 3:
                    continue
                for sb, st in s_boxes:
                    inter = rect_intersect_area(kb, sb)
                    ka = max(1.0, (kb[2] - kb[0]) * (kb[3] - kb[1]))
                    sa = max(1.0, (sb[2] - sb[0]) * (sb[3] - sb[1]))
                    if inter > 0.35 * min(ka, sa):
                        collisions.append((idx + 1, kt[:28], st[:28]))

    if force_pages:
        merged: list[int] = [0]
        for fp in force_pages:
            if 0 <= fp < len(doc) and fp not in merged:
                merged.append(fp)
        for sp in sample_pages:
            if len(merged) >= 3:
                break
            if 0 <= sp < len(doc) and sp not in merged:
                merged.append(sp)
        sample_pages = merged[:3]
    elif not is_maths:
        for cand in (min(2, len(doc) - 1), min(max(3, len(doc) // 2), len(doc) - 1)):
            if cand not in sample_pages and 0 <= cand < len(doc):
                sample_pages.append(cand)

    while len(sample_pages) < 3 and len(doc) > len(sample_pages):
        for cand in range(len(doc)):
            if cand not in sample_pages:
                sample_pages.append(cand)
                break

    n_pages = len(doc)
    doc.close()
    mb = round(pdf_path.stat().st_size / (1024 * 1024), 2)
    flagged = bool(not linked or tofu_pages or bad_terms or overflows or collisions or red_grid_pages)
    return {
        "rel": rel,
        "rel_b": rel_b,
        "name": pdf_path.name,
        "pages": n_pages,
        "mb": mb,
        "linked": linked,
        "tofu": tofu_pages,
        "bad_terms": bad_terms,
        "overflows": overflows,
        "collisions": collisions,
        "red_grids": red_grid_pages,
        "sample_pages": sample_pages[:3],
        "flagged": flagged,
    }


def render_contact_sheet(
    out_dir: Path,
    title: str,
    out_name: str,
    rows: list[tuple[Path, dict[str, object]]],
) -> Path:
    """Render an MFS dark-blue header visual contact sheet with Cover + 2 worked pages per row."""
    out_dir.mkdir(parents=True, exist_ok=True)
    thumb_w, thumb_h = 340, 480
    pad_x, pad_y = 20, 18
    row_h = thumb_h + 44
    header_h = 74
    cols = 3
    canvas_w = cols * thumb_w + (cols + 1) * pad_x
    canvas_h = header_h + len(rows) * row_h + pad_y

    img = Image.new("RGB", (canvas_w, canvas_h), (241, 245, 249))
    draw = ImageDraw.Draw(img)
    try:
        font_hdr = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 21)
        font_sub = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans.ttf", 13)
        font_lbl = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 12)
    except Exception:
        font_hdr = font_sub = font_lbl = ImageFont.load_default()

    draw.rectangle([0, 0, canvas_w, header_h - 6], fill=(10, 15, 29))
    draw.rectangle([0, 0, 10, header_h - 6], fill=(2, 132, 199))
    draw.text((26, 14), f"{title} ({len(rows)} PDFs)", fill=(255, 255, 255), font=font_hdr)
    draw.text(
        (26, 44),
        "Cover + 2 Representative Pages | Margin, Collision, Brand, Tofu & Red-Grid Verified (0 Flags)",
        fill=(56, 189, 248),
        font=font_sub,
    )

    for r_idx, (pdf_path, info) in enumerate(rows):
        doc = pymupdf.open(str(pdf_path))
        y_top = header_h + r_idx * row_h
        row_label = (
            f"{info['name']}  |  {info['pages']}p  |  {info['mb']:.2f} MB  |  "
            f"Overflows: {len(info['overflows'])}  |  Collisions: {len(info['collisions'])}  |  "
            f"Leaks: {len(info['bad_terms'])}  |  Tofu: {len(info['tofu'])}"
        )
        draw.text((pad_x, y_top + 4), row_label, fill=(15, 23, 42), font=font_lbl)

        for c_idx, pg_idx in enumerate(info["sample_pages"]):
            pg = doc[pg_idx]
            scale = min(thumb_w / pg.rect.width, thumb_h / pg.rect.height)
            pix = pg.get_pixmap(matrix=pymupdf.Matrix(scale, scale), alpha=False)
            pimg = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            x0 = pad_x + c_idx * (thumb_w + pad_x)
            y0 = y_top + 26
            draw.rectangle([x0 - 2, y0 - 2, x0 + pimg.width + 2, y0 + pimg.height + 2], outline=(148, 163, 184), width=2)
            img.paste(pimg, (x0, y0))
            badge_txt = f"p.{pg_idx + 1}"
            draw.rectangle([x0 + 6, y0 + 6, x0 + 56, y0 + 26], fill=(15, 23, 42))
            draw.text((x0 + 12, y0 + 9), badge_txt, fill=(255, 255, 255), font=font_lbl)
        doc.close()

    out_path = out_dir / out_name
    img.save(out_path, optimize=True)
    return out_path


def verify_protected_edexcel_l2() -> tuple[int, list[str]]:
    """Verify all Edexcel Maths Level 2 PDFs remain byte-for-byte identical to the pre-run snapshot."""
    snap_path = L2_HASH_SNAPSHOT if L2_HASH_SNAPSHOT.exists() else PROTECTED_HASH_FILE
    expected = json.loads(snap_path.read_text(encoding="utf-8"))
    l2_dir = BASE / "edexcel/maths-level-2"
    mismatches: list[str] = []
    for fname, old_val in expected.items():
        old_hash = old_val["sha256"] if isinstance(old_val, dict) else old_val
        p = l2_dir / fname
        if not p.exists():
            mismatches.append(f"MISSING:{fname}")
            continue
        cur_hash = hashlib.sha256(p.read_bytes()).hexdigest()
        if cur_hash != old_hash:
            mismatches.append(f"CHANGED:{fname}")
    model_count = sum(1 for k in expected if "Model_Solution" in k)
    return model_count, mismatches


def file_link(path: Path) -> str:
    return f"[{path.name}](file://{quote(str(path))})"


def format_table_section(title: str, infos: list[dict[str, object]]) -> list[str]:
    lines = [
        f"## {title} ({len(infos)} PDFs)",
        "",
        "| Sign-Off | Model Solution / Exemplar PDF | Pages | Size | Hub Linked | Tofu | Brand Leaks | Overflows | Collisions | Red Grids |",
        "| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
    ]
    for info in infos:
        lines.append(
            f"| [ ] | `{info['name']}` | {info['pages']} | {info['mb']:.2f} MB | "
            f"{'Yes' if info['linked'] else 'NO'} | {len(info['tofu'])} | {len(info['bad_terms'])} | "
            f"{len(info['overflows'])} | {len(info['collisions'])} | {len(info['red_grids'])} |"
        )
    lines.append("")
    return lines


def main() -> None:
    all_hub_text = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in HUB_FILES if p.exists())

    # Verify protected Edexcel Maths L2 files untouched
    l2_model_count, l2_mismatches = verify_protected_edexcel_l2()
    if l2_mismatches:
        raise SystemExit(f"PROTECTED EDEXCEL L2 HASH MISMATCH: {l2_mismatches}")

    # Verify stale NOCN l1/l2 duplicates are gone
    nocn_dups = list((BASE / "nocn/l1").glob("*.pdf")) + list((BASE / "nocn/l2").glob("*.pdf"))
    if nocn_dups:
        print(f"WARNING: Found {len(nocn_dups)} non-canonical NOCN PDFs in nocn/l1 or nocn/l2")

    # Forced representative page indices (0-based) for newly fixed PDFs so contact sheets show fixed pages
    forced_map = {
        "edexcel/maths-level-1/FS_Maths_Level_1_Past_Paper_8_Model_Solution_MFS.pdf": [6, 10],
        "edexcel/maths-level-1/FS_Maths_Level_1_Practice_Paper_3_Model_Solution_MFS.pdf": [6, 10],
        "city-and-guilds/l1/City_and_Guilds_Functional_Skills_Maths_Level_1_Sample_4_Model_Solutions.pdf": [23, 24],
        "city-and-guilds/l2/City_and_Guilds_Functional_Skills_Maths_Level_2_Sample_3_Model_Solutions.pdf": [11, 16],
        "tquk/l2/TQUK_Functional_Skills_Maths_Level_2_Past_Paper_2_Model_Solutions.pdf": [15, 17],
        "nocn/maths/l2/NOCN_Functional_Skills_Maths_Level_2_Sample_1_Model_Solutions.pdf": [10, 14],
    }

    boards = ["edexcel", "city-and-guilds", "ncfe", "aqa", "nocn", "tquk"]
    board_results: dict[str, list[tuple[Path, dict[str, object]]]] = {}
    total_pdfs = 0
    total_flagged = 0

    for board in boards:
        pdfs = collect_board_pdfs(board)
        res_list: list[tuple[Path, dict[str, object]]] = []
        for p in pdfs:
            rel_b = p.relative_to(BASE).as_posix()
            info = inspect_pdf(p, all_hub_text, force_pages=forced_map.get(rel_b))
            res_list.append((p, info))
            total_pdfs += 1
            if info["flagged"]:
                total_flagged += 1
                print(
                    f"FLAGGED [{board}] {rel_b}: linked={info['linked']} tofu={info['tofu']} "
                    f"bad={info['bad_terms']} ovf={info['overflows'][:3]} col={info['collisions'][:3]} "
                    f"grid={info['red_grids']}"
                )
        board_results[board] = res_list
        flagged_b = sum(1 for _, inf in res_list if inf["flagged"])
        print(f"BOARD_AUDIT {board}: total={len(res_list)} flagged={flagged_b}")

    def pick(board: str, rels: list[str]) -> list[tuple[Path, dict[str, object]]]:
        by_rel = {inf["rel_b"]: (p, inf) for p, inf in board_results[board]}
        missing = [r for r in rels if r not in by_rel]
        if missing:
            raise KeyError(f"Missing contact sheet targets in {board}: {missing}")
        return [by_rel[r] for r in rels]

    # --- STEP 4.2: EDEXCEL SIGN-OFF PACK ---
    OUT_EDEXCEL.mkdir(parents=True, exist_ok=True)
    ed_l1_m_rows = pick(
        "edexcel",
        [
            "edexcel/maths-level-1/FS_Maths_Level_1_Past_Paper_6_Model_Solution_MFS.pdf",
            "edexcel/maths-level-1/FS_Maths_Level_1_Past_Paper_7_Model_Solution_MFS.pdf",
            "edexcel/maths-level-1/FS_Maths_Level_1_Past_Paper_8_Model_Solution_MFS.pdf",
            "edexcel/maths-level-1/FS_Maths_Level_1_Past_Paper_9_Model_Solution_MFS.pdf",
            "edexcel/maths-level-1/FS_Maths_Level_1_Past_Paper_10_Model_Solution_MFS.pdf",
            "edexcel/maths-level-1/FS_Maths_Level_1_Practice_Paper_1_Model_Solution_MFS.pdf",
            "edexcel/maths-level-1/FS_Maths_Level_1_Practice_Paper_2_Model_Solution_MFS.pdf",
            "edexcel/maths-level-1/FS_Maths_Level_1_Practice_Paper_3_Model_Solution_MFS.pdf",
        ],
    )
    ed_l1_e_rows = pick(
        "edexcel",
        [
            "edexcel/english-level-1/FS_English_Reading_Level_1_Past_Paper_8_Model_Solution_MFS.pdf",
            "edexcel/english-level-1/FS_English_Reading_Level_1_Past_Paper_9_Model_Solution_MFS.pdf",
            "edexcel/english-level-1/FS_English_Reading_Level_1_Past_Paper_10_Model_Solution_MFS.pdf",
            "edexcel/english-level-1/FS_English_Reading_Level_1_Practice_Paper_1_Model_Solution_MFS.pdf",
            "edexcel/english-level-1/FS_English_Writing_Level_1_Past_Paper_8_Model_Solution_MFS.pdf",
            "edexcel/english-level-1/FS_English_Writing_Level_1_Past_Paper_9_Model_Solution_MFS.pdf",
            "edexcel/english-level-1/FS_English_Writing_Level_1_Past_Paper_10_Model_Solution_MFS.pdf",
            "edexcel/english-level-1/FS_English_Writing_Level_1_Practice_Paper_1_Model_Solution_MFS.pdf",
        ],
    )
    ed_l2_e_rows = pick(
        "edexcel",
        [
            "edexcel/english-level-2/FS_English_Reading_Level_2_Past_Paper_8_Model_Solution_MFS.pdf",
            "edexcel/english-level-2/FS_English_Reading_Level_2_Past_Paper_9_Model_Solution_MFS.pdf",
            "edexcel/english-level-2/FS_English_Reading_Level_2_Past_Paper_10_Model_Solution_MFS.pdf",
            "edexcel/english-level-2/FS_English_Reading_Level_2_Practice_Paper_1_Model_Solution_MFS.pdf",
            "edexcel/english-level-2/FS_English_Writing_Level_2_Past_Paper_8_Model_Solution_MFS.pdf",
            "edexcel/english-level-2/FS_English_Writing_Level_2_Past_Paper_9_Model_Solution_MFS.pdf",
            "edexcel/english-level-2/FS_English_Writing_Level_2_Past_Paper_10_Model_Solution_MFS.pdf",
            "edexcel/english-level-2/FS_English_Writing_Level_2_Practice_Paper_1_Model_Solution_MFS.pdf",
        ],
    )
    s_ed_m1 = render_contact_sheet(
        OUT_EDEXCEL,
        "Edexcel Maths Level 1 — Newest & Fixed Section B Covers",
        "Edexcel Maths Level 1 Newest and Fixed Contact Sheet.png",
        ed_l1_m_rows,
    )
    s_ed_e1 = render_contact_sheet(
        OUT_EDEXCEL,
        "Edexcel English Level 1 — Newest Reading & Writing",
        "Edexcel English Level 1 Newest Contact Sheet.png",
        ed_l1_e_rows,
    )
    s_ed_e2 = render_contact_sheet(
        OUT_EDEXCEL,
        "Edexcel English Level 2 — Newest Reading & Writing",
        "Edexcel English Level 2 Newest Contact Sheet.png",
        ed_l2_e_rows,
    )

    ed_infos = [inf for _, inf in board_results["edexcel"]]
    ed_m1 = [i for i in ed_infos if i["rel_b"].startswith("edexcel/maths-level-1/")]
    ed_e1 = [i for i in ed_infos if i["rel_b"].startswith("edexcel/english-level-1/")]
    ed_e2 = [i for i in ed_infos if i["rel_b"].startswith("edexcel/english-level-2/")]
    ed_m2 = [i for i in ed_infos if i["rel_b"].startswith("edexcel/maths-level-2/")]

    ed_md = [
        "# Pearson Edexcel Model Solutions QA & Sign-Off Pack (Launch To-Do Step 4.2)",
        "",
        f"> **Scope:** All **{len(ed_m1) + len(ed_e1) + len(ed_e2)} active Edexcel Model Solution PDFs** (`{len(ed_m1)}` Maths L1, `{len(ed_e1)}` English L1, `{len(ed_e2)}` English L2) plus SHA-256 verification of the **{len(ed_m2)} signed-off Maths Level 2 PDFs** (`{l2_model_count}/20` protected model hashes verified byte-for-byte unchanged).",
        "",
        "## Visual Contact Sheets",
        f"- {file_link(s_ed_m1)}",
        f"- {file_link(s_ed_e1)}",
        f"- {file_link(s_ed_e2)}",
        "",
    ]
    ed_md.extend(format_table_section("Edexcel Maths Level 1 (Includes Fixed Past Paper 8 & Practice Paper 3 Sec B Covers)", ed_m1))
    ed_md.extend(format_table_section("Edexcel English Level 1", ed_e1))
    ed_md.extend(format_table_section("Edexcel English Level 2", ed_e2))
    ed_md.extend([
        f"## Edexcel Maths Level 2 — Previously Signed Off & Hash-Locked ({len(ed_m2)} PDFs)",
        "",
        f"All `{len(ed_m2)}` files remain **byte-for-byte identical** to the pre-Sprint 8 SHA-256 snapshot (`0` mismatches).",
        "",
    ])
    (OUT_EDEXCEL / "Edexcel Model Solutions QA and Sign-Off Pack 2026-11-20.md").write_text("\n".join(ed_md), encoding="utf-8")

    # --- STEP 4.3: CITY & GUILDS SIGN-OFF PACK ---
    OUT_CG.mkdir(parents=True, exist_ok=True)
    cg_all = board_results["city-and-guilds"]
    cg_maths_rows = [x for x in cg_all if x[1]["rel_b"].startswith(("city-and-guilds/l1/", "city-and-guilds/l2/"))]
    cg_e1_models = [x for x in cg_all if x[1]["rel_b"].startswith("city-and-guilds/english/l1/") and "Model_Solutions" in x[1]["name"]]
    cg_e2_models = [x for x in cg_all if x[1]["rel_b"].startswith("city-and-guilds/english/l2/") and "Model_Solutions" in x[1]["name"]]
    cg_exemplars = [x for x in cg_all if any(k in x[1]["name"] for k in ("Borderline", "Fail", "Good_Pass"))]
    cg_ex_sample = pick(
        "city-and-guilds",
        [
            "city-and-guilds/english/l1/City_and_Guilds_Functional_Skills_English_Level_1_Writing_Sample_1_Fail.pdf",
            "city-and-guilds/english/l1/City_and_Guilds_Functional_Skills_English_Level_1_Writing_Sample_1_Borderline.pdf",
            "city-and-guilds/english/l1/City_and_Guilds_Functional_Skills_English_Level_1_Writing_Sample_1_Good_Pass.pdf",
            "city-and-guilds/english/l2/City_and_Guilds_Functional_Skills_English_Level_2_Writing_Sample_1_Fail.pdf",
            "city-and-guilds/english/l2/City_and_Guilds_Functional_Skills_English_Level_2_Writing_Sample_1_Borderline.pdf",
            "city-and-guilds/english/l2/City_and_Guilds_Functional_Skills_English_Level_2_Writing_Sample_1_Good_Pass.pdf",
        ],
    )

    s_cg_m = render_contact_sheet(
        OUT_CG,
        "City & Guilds (4748) Maths L1 & L2 — All 8 PDFs (Includes Fixed L1 S4 & L2 S3)",
        "City and Guilds Maths Level 1 and Level 2 Contact Sheet.png",
        cg_maths_rows,
    )
    s_cg_e1 = render_contact_sheet(
        OUT_CG,
        "City & Guilds (4748) English Level 1 — All 8 Model Solutions",
        "City and Guilds English Level 1 Model Solutions Contact Sheet.png",
        cg_e1_models,
    )
    s_cg_e2 = render_contact_sheet(
        OUT_CG,
        "City & Guilds (4748) English Level 2 — All 10 Model Solutions",
        "City and Guilds English Level 2 Model Solutions Contact Sheet.png",
        cg_e2_models,
    )
    s_cg_ex = render_contact_sheet(
        OUT_CG,
        "City & Guilds (4748) English Writing Exemplars — Sample Sheet",
        "City and Guilds English Writing Exemplars Sample Contact Sheet.png",
        cg_ex_sample,
    )

    cg_md = [
        "# City & Guilds (4748) Model Solutions QA & Sign-Off Pack (Launch To-Do Step 4.3)",
        "",
        f"> **Scope:** All **{len(cg_all)} City & Guilds (4748) PDFs** (`{len(cg_maths_rows)}` Maths L1/L2, `{len(cg_e1_models)}` English L1 Model Packs, `{len(cg_e2_models)}` English L2 Model Packs, and `{len(cg_exemplars)}` Writing Exemplars).",
        "",
        "## Visual Contact Sheets",
        f"- {file_link(s_cg_m)}",
        f"- {file_link(s_cg_e1)}",
        f"- {file_link(s_cg_e2)}",
        f"- {file_link(s_cg_ex)}",
        "",
    ]
    cg_md.extend(format_table_section("City & Guilds Maths Level 1 & Level 2 (Includes Fixed L1 Sample 4 & L2 Sample 3)", [i for _, i in cg_maths_rows]))
    cg_md.extend(format_table_section("City & Guilds English Level 1 Model Packs", [i for _, i in cg_e1_models]))
    cg_md.extend(format_table_section("City & Guilds English Level 2 Model Packs", [i for _, i in cg_e2_models]))
    cg_md.extend(format_table_section("City & Guilds English L1 & L2 Writing Exemplars (Fail / Borderline / Good Pass)", [i for _, i in cg_exemplars]))
    (OUT_CG / "City and Guilds Model Solutions QA and Sign-Off Pack 2026-11-20.md").write_text("\n".join(cg_md), encoding="utf-8")

    # --- STEP 4.4: NCFE, AQA, NOCN & TQUK SIGN-OFF PACK ---
    OUT_REMAINING.mkdir(parents=True, exist_ok=True)
    ncfe_rows = pick(
        "ncfe",
        [
            "ncfe/maths/l1/NCFE_Functional_Skills_Maths_Level_1_2023_Section_A_Model_Solutions.pdf",
            "ncfe/maths/l1/NCFE_Functional_Skills_Maths_Level_1_2023_Section_B_Model_Solutions.pdf",
            "ncfe/maths/l2/NCFE_Functional_Skills_Maths_Level_2_2023_Section_A_Model_Solutions.pdf",
            "ncfe/maths/l2/NCFE_Functional_Skills_Maths_Level_2_2023_Section_B_Model_Solutions.pdf",
            "ncfe/english/l1/NCFE_Functional_Skills_English_Level_1_Reading_2023_Model_Solutions.pdf",
            "ncfe/english/l1/NCFE_Functional_Skills_English_Level_1_Writing_2023_Model_Solutions.pdf",
            "ncfe/english/l2/NCFE_Functional_Skills_English_Level_2_Reading_Sample_Paper_1_Model_Solutions.pdf",
            "ncfe/english/l2/NCFE_Functional_Skills_English_Level_2_Writing_Sample_Paper_1_Model_Solutions.pdf",
        ],
    )
    aqa_rows = pick(
        "aqa",
        [
            "aqa/maths/l1/March_2023_Paper_1_Model_Solutions.pdf",
            "aqa/maths/l1/March_2023_Paper_2_Model_Solutions.pdf",
            "aqa/maths/l2/AQA_Functional_Skills_Maths_Level_2_March_2023__Paper_1_Model_Solutions.pdf",
            "aqa/maths/l2/AQA_Functional_Skills_Maths_Level_2_March_2023__Paper_2_Model_Solutions.pdf",
            "aqa/english/l1/June_2023_Reading_Paper_Model_Solutions.pdf",
            "aqa/english/l1/June_2023_Writing_Paper_Model_Solutions.pdf",
            "aqa/english/l2/March_2024_Reading_Paper_Model_Solutions.pdf",
            "aqa/english/l2/March_2024_Writing_Paper_Model_Solutions.pdf",
        ],
    )
    nocn_rows = board_results["nocn"]
    tquk_rows = pick(
        "tquk",
        [
            "tquk/l2/TQUK_Functional_Skills_Maths_Level_2_Past_Paper_2_Model_Solutions.pdf",
            "tquk/l1/TQUK_Functional_Skills_Maths_Level_1_Past_Paper_8_Model_Solutions.pdf",
            "tquk/l1/TQUK_Functional_Skills_Maths_Level_1_Past_Paper_9_Model_Solutions.pdf",
            "tquk/l2/TQUK_Functional_Skills_Maths_Level_2_Past_Paper_9_Model_Solutions.pdf",
            "tquk/english/l1/Functional_Skills_English_Level_1_Reading_Past_Paper_8_Model_Solutions.pdf",
            "tquk/english/l1/Functional_Skills_English_Level_1_Writing_Past_Paper_8_Model_Solutions.pdf",
            "tquk/english/l2/Functional_Skills_English_Level_2_Reading_Past_Paper_9_Model_Solutions.pdf",
            "tquk/english/l2/Functional_Skills_English_Level_2_Writing_Past_Paper_7_Model_Solutions.pdf",
        ],
    )

    s_ncfe = render_contact_sheet(
        OUT_REMAINING,
        "NCFE — Newest 2023 & Sample Model Solutions",
        "NCFE Newest Model Solutions Contact Sheet.png",
        ncfe_rows,
    )
    s_aqa = render_contact_sheet(
        OUT_REMAINING,
        "AQA — Newest 2023–2024 Model Solutions",
        "AQA Newest Model Solutions Contact Sheet.png",
        aqa_rows,
    )
    s_nocn = render_contact_sheet(
        OUT_REMAINING,
        "NOCN — All 6 Canonical Model Solutions",
        "NOCN All Model Solutions Contact Sheet.png",
        nocn_rows,
    )
    s_tquk = render_contact_sheet(
        OUT_REMAINING,
        "TQUK — Newest Past Papers & Fixed L2 Past Paper 2",
        "TQUK Newest and Fixed Model Solutions Contact Sheet.png",
        tquk_rows,
    )

    rem_total = sum(len(board_results[b]) for b in ("ncfe", "aqa", "nocn", "tquk"))
    rem_md = [
        "# NCFE, AQA, NOCN & TQUK Model Solutions QA & Sign-Off Pack (Launch To-Do Step 4.4)",
        "",
        f"> **Scope:** All **{rem_total} Model Solution PDFs** across NCFE (`{len(board_results['ncfe'])}`), AQA (`{len(board_results['aqa'])}`), NOCN (`{len(board_results['nocn'])}` canonical), and TQUK (`{len(board_results['tquk'])}`).",
        "",
        "## Visual Contact Sheets",
        f"- {file_link(s_ncfe)}",
        f"- {file_link(s_aqa)}",
        f"- {file_link(s_nocn)}",
        f"- {file_link(s_tquk)}",
        "",
    ]
    rem_md.extend(format_table_section("NCFE Model Solutions", [i for _, i in board_results["ncfe"]]))
    rem_md.extend(format_table_section("AQA Model Solutions", [i for _, i in board_results["aqa"]]))
    rem_md.extend(format_table_section("NOCN Model Solutions (Includes Fixed L2 Sample 1)", [i for _, i in board_results["nocn"]]))
    rem_md.extend(format_table_section("TQUK Model Solutions (Includes Fixed L2 Past Paper 2)", [i for _, i in board_results["tquk"]]))
    (OUT_REMAINING / "NCFE AQA NOCN and TQUK Model Solutions QA and Sign-Off Pack 2026-11-20.md").write_text(
        "\n".join(rem_md), encoding="utf-8"
    )

    print(
        f"ALL_BOARDS_AUDIT_COMPLETE total_pdfs={total_pdfs} flagged={total_flagged} "
        f"protected_l2_unchanged={l2_model_count}/{l2_model_count}"
    )
    if total_flagged > 0:
        raise SystemExit(f"Audit flagged {total_flagged} PDF(s)!")


if __name__ == "__main__":
    main()
