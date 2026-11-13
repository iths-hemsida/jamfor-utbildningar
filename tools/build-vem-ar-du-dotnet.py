"""Bygger vem-ar-du-dotnet/index.html (GitHub Pages, för iframe) och wordpress/vem-ar-du-dotnet-wpcode.html från vem-ar-du-dotnet/snippet.html."""
from pathlib import Path
root = Path(__file__).resolve().parent.parent
snippet = (root / "vem-ar-du-dotnet" / "snippet.html").read_text(encoding="utf-8")
page = f"""<!doctype html>
<html lang="sv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Vem är du? .NET-utvecklare | IT-Högskolan</title>
<style>html, body {{ margin: 0; background: #fff; }} body {{ padding: 0 16px; }} @media (max-width: 500px) {{ html.inbaddad body {{ padding: 0 2px; }} }}</style>
<script>if (window.parent !== window) document.documentElement.className = "inbaddad";</script>
</head>
<body>
{snippet}
</body>
</html>
"""
(root / "vem-ar-du-dotnet" / "index.html").write_text(page, encoding="utf-8")
(root / "wordpress" / "vem-ar-du-dotnet-wpcode.html").write_text(snippet, encoding="utf-8")
print("ok")
