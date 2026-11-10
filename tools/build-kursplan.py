#!/usr/bin/env python3
"""Kopierar kursbeskrivningarna (COURSE_INFO) från jämförelsen (index.html)
till kursplansutforskaren (kursplan/index.html), så att båda visar samma texter.

Kör från repots rot efter att COURSE_INFO har ändrats i index.html:
    python3 tools/build-kursplan.py
"""
import pathlib, re

root = pathlib.Path(__file__).resolve().parent.parent
src = (root / "index.html").read_text(encoding="utf-8")
m = re.search(r"^const COURSE_INFO = .*;$", src, re.M)
if not m:
    raise SystemExit("Hittade inte COURSE_INFO i index.html")

target = root / "kursplan" / "index.html"
page = target.read_text(encoding="utf-8")
start, end = "// BEGIN COURSE_INFO\n", "// END COURSE_INFO"
a, b = page.index(start) + len(start), page.index(end)
target.write_text(page[:a] + m.group(0) + "\n" + page[b:], encoding="utf-8")
print("Uppdaterade", target.relative_to(root))
