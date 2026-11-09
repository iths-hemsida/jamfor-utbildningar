# Jämför utbildningar

Prototyp för iths.se där besökare kan välja upp till tre YH-utbildningar och jämföra dem sida vid sida.

- All kod ligger i `index.html` (HTML, CSS och JavaScript utan beroenden).
- Datan ligger i filen: `PROGRAMS` (utbildningarna), `COURSE_INFO` (kursbeskrivningar), `AI_INFO` (AI-raden) och `QUIZ_ANSWERS` (simulerade quizsvar).
- Datan hämtades från iths.se den 6 november 2026. Kursbeskrivningar och AI-texter kommer från IT-Högskolans ansökningar till MYH och kursplaner.

## Bädda in på iths.se

Lägg ett block av typen Anpassad HTML på en WordPress-sida:

```html
<iframe src="https://iths-hemsida.github.io/jamfor-utbildningar/"
  title="Jämför utbildningar" style="width:100%; height:1600px; border:0;" loading="lazy"></iframe>
```
