#!/usr/bin/env python3
"""Content audit for Master Functional Skills PDFs (complements the pixel/layout qa_report).

Usage:  python3 content_audit.py BOOK.pdf [BOOK2.pdf ...]
Flags per page:
  FILLER    loop/boilerplate phrases ("Part 3 of 8", "Option B is correct", "workplace problem for", ...)
  DUP       page text (numbers stripped) near-identical to an earlier page
  THIN      a non-cover, non-writing-frame page with < 45 words of real text
  NO_NUM    a maths question line that contains no digit at all
  REPEAT    the same sentence appears on >= 4 different pages
Exit code 1 if any FILLER / DUP flags are found.
"""
import re, subprocess, sys
from collections import defaultdict
from difflib import SequenceMatcher

FILLER = [
    r"\bPart \d+ of \d+\b", r"Option [A-D] is (the )?correct", r"\bplaceholder\b", r"lorem ipsum",
    r"Solve the initial workplace problem", r"multi-step calculation involving",
    r"Complete the full contextual scenario", r"Multi-step problem assessing core standard",
    r"Extended workplace scenario requiring", r"Mental arithmetic or fraction operation in workplace context",
    r"Written long multiplication or division calculation\. Show all working\.$",
    r"Format \d+: Practical Writing Format", r"\bTBC\b", r"\bTODO\b", r"\bXXX\b",
    r"Answer to question \d+", r"Sample answer goes here", r"Insert (answer|text|image)",
    r"Award marks for correct (method|answer)\.?$", r"See mark scheme", r"Refer to the model answer",
]
FRAME_HINTS = re.compile(r"(write your .*?(answer|response)|candidate response|planning|notes|working|draft|my notes|plan your|lined response)", re.I)


def pages_text(pdf):
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout).group(1))
    out = []
    for i in range(1, n + 1):
        t = subprocess.run(["pdftotext", "-layout", "-f", str(i), "-l", str(i), pdf, "-"],
                           capture_output=True, text=True).stdout
        out.append(t)
    return out


def norm(t):
    t = re.sub(r"\d+", "#", t.lower())
    return re.sub(r"\s+", " ", t).strip()


def audit(pdf):
    txt = pages_text(pdf)
    n = len(txt)
    flags = defaultdict(list)
    seen = []
    sent_pages = defaultdict(set)
    for i, t in enumerate(txt, 1):
        if i in (1, 2, n):
            continue
        body_lines = [l for l in t.splitlines() if l.strip()]
        body = "\n".join(body_lines[1:-1]) if len(body_lines) > 2 else t  # drop running head/foot
        for pat in FILLER:
            for l in body.splitlines():
                if re.search(pat, l.strip(), re.I):
                    flags[i].append(f"FILLER: {l.strip()[:110]}")
        words = re.findall(r"[A-Za-z']{2,}", body)
        if len(words) < 45 and not FRAME_HINTS.search(body):
            flags[i].append(f"THIN: only {len(words)} words")
        nb = norm(body)
        if len(nb) > 200:
            for j, prev in seen:
                if abs(len(prev) - len(nb)) < 0.1 * len(nb) and SequenceMatcher(None, prev, nb).quick_ratio() > 0.95 \
                        and SequenceMatcher(None, prev, nb).ratio() > 0.93:
                    flags[i].append(f"DUP: ~same as page {j}")
                    break
            seen.append((i, nb))
        for s in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", body)):
            s = s.strip()
            if len(s) > 60:
                sent_pages[norm(s)].add(i)
        if "maths" in pdf.lower() or "mock_pack_maths" in pdf.lower():
            for l in body.splitlines():
                m = re.match(r"\s*(Q(uestion)?\s*\d+[a-z]?[.:)]|\d+[a-z]?[.)])\s+(.{25,})", l)
                if m and not re.search(r"\d", m.group(3)) and "?" in l:
                    flags[i].append(f"NO_NUM: {l.strip()[:100]}")
    for s, ps in sent_pages.items():
        if len(ps) >= 4:
            flags[min(ps)].append(f"REPEAT x{len(ps)} pages {sorted(ps)[:8]}: {s[:90]}")
    return n, flags


def main():
    bad = False
    for pdf in sys.argv[1:]:
        n, flags = audit(pdf)
        hard = sum(1 for v in flags.values() for f in v if f.startswith(("FILLER", "DUP")))
        soft = sum(1 for v in flags.values() for f in v if not f.startswith(("FILLER", "DUP")))
        print(f"\n=== {pdf}  ({n} pages)  hard={hard} soft={soft}")
        for p in sorted(flags):
            for f in flags[p]:
                print(f"  p{p}: {f}")
        bad |= hard > 0
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
