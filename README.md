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

Koden ovan räcker om sidan inte ska kopplas till quizet. För quizkopplingen, använd i stället den här varianten, som skickar vidare parametrarna i adressen till iframen:

```html
<iframe id="jamfor" title="Jämför utbildningar" style="width:100%; height:1600px; border:0;" loading="lazy"></iframe>
<script>
  document.getElementById("jamfor").src = "https://iths-hemsida.github.io/jamfor-utbildningar/" + location.search;
</script>
```

## Koppling till quizet

Quizets resultatsida länkar till jämförelsesidan med två parametrar:

```
/jamfor-utbildningar/?valda=frontend,ux-designer,fullstack&svar=visuellt:0.9,logik:0.5,sakerhet:0.1,data:0.2,webb:0.9,manniskor:0.4
```

- `valda` (valfri): upp till tre utbildningar, kommaseparerade. Om den saknas väljs de tre som matchar svaren bäst.
- `svar`: alla sex dimensionerna med ett värde mellan 0 och 1. När den finns visas raden "Matchning med dina svar".

Giltiga utbildningar: `frontend`, `javautvecklare`, `ux-designer`, `it-sakerhetsspecialist`, `fullstack`, `net`, `net-cloud`, `mjukvarutestare`, `it-projektledare`, `account-manager`, `it-sakerhetstestare`.

Dimensioner: `visuellt` (design och det visuella), `logik` (logik och problemlösning), `sakerhet` (IT-säkerhet), `data` (data och system), `webb` (webb), `manniskor` (leda, samarbeta och prata med kunder).
