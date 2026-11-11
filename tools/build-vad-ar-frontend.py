"""Bygger vad-ar-frontend/index.html (GitHub Pages, för iframe) och wordpress/vad-ar-frontend-wpcode.html från vad-ar-frontend/snippet.html."""
from pathlib import Path
root = Path(__file__).resolve().parent.parent
snippet = (root / "vad-ar-frontend" / "snippet.html").read_text(encoding="utf-8")
page = f"""<!doctype html>
<html lang="sv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Vad är frontend? | IT-Högskolan</title>
<style>html, body {{ margin: 0; background: #fff; }} body {{ padding: 0 16px; }}</style>
</head>
<body>
{snippet}
</body>
</html>
"""
(root / "vad-ar-frontend" / "index.html").write_text(page, encoding="utf-8")
(root / "wordpress" / "vad-ar-frontend-wpcode.html").write_text(snippet, encoding="utf-8")
print("ok")
