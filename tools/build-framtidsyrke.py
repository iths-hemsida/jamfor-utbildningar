"""Bygger framtidsyrke/index.html (GitHub Pages, för iframe) och wordpress/framtidsyrke-wpcode.html från framtidsyrke/snippet.html."""
from pathlib import Path
root = Path(__file__).resolve().parent.parent
snippet = (root / "framtidsyrke" / "snippet.html").read_text(encoding="utf-8")
page = f"""<!doctype html>
<html lang="sv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Därför är frontend ett framtidsyrke | IT-Högskolan</title>
<style>html, body {{ margin: 0; background: #fff; }} body {{ padding: 0 16px; }} @media (max-width: 500px) {{ html.inbaddad body {{ padding: 0 2px; }} }}</style>
<script>if (window.parent !== window) document.documentElement.className = "inbaddad";</script>
</head>
<body>
{snippet}
</body>
</html>
"""
(root / "framtidsyrke" / "index.html").write_text(page, encoding="utf-8")
# I WPCode ska huvudrubriken ärva temats rubriktypsnitt, så raden märkt FRISTÅENDE tas bort där.
wp = "\n".join(l for l in snippet.split("\n") if "/* FRISTÅENDE */" not in l)
(root / "wordpress" / "framtidsyrke-wpcode.html").write_text(wp, encoding="utf-8")
print("ok")
