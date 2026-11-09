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
<iframe id="jamfor" src="https://iths-hemsida.github.io/jamfor-utbildningar/" title="Jämför utbildningar" style="width:100%; height:1600px; border:0;"></iframe>
<script>
  if (location.search) document.getElementById("jamfor").src = "https://iths-hemsida.github.io/jamfor-utbildningar/" + location.search;
</script>
```

## Koppling till quizet

Quizet på iths.se/vilken-utbildning-passar-mig har en knapp på resultatsidan, "Jämför dina tre bästa sida vid sida". Den länkar hit med två parametrar:

```
/jamfor-utbildningar/?valda=mjukvarutestare,javautvecklare,net&match=mjukvarutestare:50,javautvecklare:43,net:36,frontend:33,...
```

- `valda` (valfri): upp till tre utbildningar, kommaseparerade. Om den saknas väljs de tre med högst matchning.
- `match`: quizets matchning i procent per utbildning. När den finns visas raden "Matchning med dina svar".

Giltiga utbildningar: `frontend`, `javautvecklare`, `ux-designer`, `it-sakerhetsspecialist`, `fullstack`, `net`, `net-cloud`, `mjukvarutestare`, `it-projektledare`, `account-manager`, `it-sakerhetstestare`.

Utan parametrar visar sidan en knapp till quizet. Knappen "Simulera quizresultat" visas bara utanför GitHub Pages, eller med `?demo` i adressen.
