#!/usr/bin/env python3
"""Kopierar kursbeskrivningarna (COURSE_INFO) och AI-sammanfattningarna (AI_INFO)
från jämförelsen (index.html) till kursplansutforskaren (kursplan/index.html),
och sedan alla data från kursplansutforskaren till version B (kursplan/b/index.html),
så att alla sidor visar samma texter.

Kör från repots rot efter att data har ändrats i index.html eller kursplan/index.html:
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

# Version B delar data och hjälpfunktioner med kursplan/index.html.
shared = page[page.index("// Kursplanerna i den ordning"):page.index("const params = ")].rstrip() + "\n"
b_page = root / "kursplan" / "b" / "index.html"
text = b_page.read_text(encoding="utf-8")
start, end = "// BEGIN SHARED (kopieras från ../index.html med tools/build-kursplan.py, ändra där)\n", "// END SHARED"
a, b = text.index(start) + len(start), text.index(end)
b_page.write_text(text[:a] + shared + "\n" + text[b:], encoding="utf-8")
print("Uppdaterade", b_page.relative_to(root))
