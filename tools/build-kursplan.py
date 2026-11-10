#!/usr/bin/env python3
"""Kopierar kursbeskrivningarna (COURSE_INFO) och AI-sammanfattningarna (AI_INFO)
från jämförelsen (index.html) till kursplansutforskaren (kursplan/index.html),
så att båda visar samma texter.

Kör från repots rot efter att COURSE_INFO eller AI_INFO har ändrats i index.html:
    python3 tools/build-kursplan.py
"""
import pathlib, re

root = pathlib.Path(__file__).resolve().parent.parent
src = (root / "index.html").read_text(encoding="utf-8")
target = root / "kursplan" / "index.html"
page = target.read_text(encoding="utf-8")

for name in ("COURSE_INFO", "AI_INFO"):
    m = re.search(rf"^const {name} = .*;$", src, re.M)
    if not m:
        raise SystemExit(f"Hittade inte {name} i index.html")
    start, end = f"// BEGIN {name}\n", f"// END {name}"
    a, b = page.index(start) + len(start), page.index(end)
    page = page[:a] + m.group(0) + "\n" + page[b:]

target.write_text(page, encoding="utf-8")
print("Uppdaterade", target.relative_to(root))
