"""Bygger java-fakta/index.html (GitHub Pages, för iframe) och wordpress/java-fakta-wpcode.html från java-fakta/snippet.html."""
from pathlib import Path
root = Path(__file__).resolve().parent.parent
snippet = (root / "java-fakta" / "snippet.html").read_text(encoding="utf-8")
page = f"""<!doctype html>
<html lang="sv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Javautvecklare i korthet | IT-Högskolan</title>
<style>html, body {{ margin: 0; background: #fff; }} body {{ padding: 0 16px; }} @media (max-width: 500px) {{ html.inbaddad body {{ padding: 0 2px; }} }}</style>
<script>if (window.parent !== window) document.documentElement.className = "inbaddad";</script>
</head>
<body>
{snippet}
</body>
</html>
"""
(root / "java-fakta" / "index.html").write_text(page, encoding="utf-8")
(root / "wordpress" / "java-fakta-wpcode.html").write_text(snippet, encoding="utf-8")
print("ok")
