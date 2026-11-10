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
<iframe id="jamfor" src="https://iths-hemsida.github.io/jamfor-utbildningar/" title="Jämför utbildningar" style="width:100%; height:1600px; border:0; scroll-margin-top:120px;"></iframe>
<script>
  if (location.search) document.getElementById("jamfor").src = "https://iths-hemsida.github.io/jamfor-utbildningar/" + location.search;
</script>
```

## Koppling till quizet

Quizet på iths.se/vilken-utbildning-passar-mig har en knapp på resultatsidan, "Jämför dina tre bästa sida vid sida". Den länkar hit med två parametrar:

```
/jamfor-utbildningar/?valda=mjukvarutestare,javautvecklare,net&match=mjukvarutestare:50,javautvecklare:43,net:36,frontend:33,...#jamfor
```

- `valda` (valfri): upp till tre utbildningar, kommaseparerade. Om den saknas väljs de tre med högst matchning.
- `match`: quizets matchning i procent per utbildning. När den finns visas raden "Matchning med dina svar".

Giltiga utbildningar: `frontend`, `javautvecklare`, `ux-designer`, `it-sakerhetsspecialist`, `fullstack`, `net`, `net-cloud`, `mjukvarutestare`, `it-projektledare`, `account-manager`, `it-sakerhetstestare`.

Utan parametrar visar sidan en knapp till quizet. Knappen "Simulera quizresultat" visas bara utanför GitHub Pages, eller med `?demo` i adressen.

## Direkt på sidan med WPCode (utan iframe)

`wordpress/jamfor-utbildningar-wpcode.html` är samma sida som en WPCode-snutt, på samma sätt som quizet. All CSS är avgränsad till `#iths-jamfor` så att den inte påverkar resten av iths.se. Bygg om snutten efter ändringar i `index.html`:

```
python3 tools/build-wpcode.py
```

## Quizet inbyggt på sidan

Knappen "Gör quizet" öppnar quizet direkt i jämförelsesidan, så att besökaren stannar kvar. Frågorna och poängen (`QZ` i `index.html`) är kopierade från quizets WPCode-snutt och behöver ändras på båda ställena om quizet ändras.

`#jamfor` i slutet gör att iths.se hoppar direkt ner till iframen (som har `id="jamfor"`), så att besökaren slipper sidans header.

## Kursplansutforskaren

`kursplan/index.html` visar en utbildnings kurser, LIA och examensarbete som en klickbar tidslinje över läsåren. Den publiceras på https://iths-hemsida.github.io/jamfor-utbildningar/kursplan/.

- Kursordningen och poängen kommer från kursplanerna på utbildningssidorna på iths.se (hämtade 10 november 2026), i `PROGRAMS` i filen. Veckorna räknas på 5 YH-poäng per vecka, och läsårens längd kommer från tabellen "Terminstider".
- Mjukvarutestare, IT-projektledare och Account Manager listar kurserna i bokstavsordning på iths.se. För dem är ordningen en bedömning (`guessed: true`), och sidan säger det.
- AI i kurserna står i `COURSE_AI`, bara för de moment där ansökan till MYH eller kursplanen nämner AI, med källa. Saknas ett moment där står det inget om AI i underlaget.
- Kursbeskrivningarna och AI-sammanfattningen per utbildning (`AI_INFO`) är samma som i jämförelsen. Kopiera dem efter ändringar i `index.html`:

```
python3 tools/build-kursplan.py
```

- `?program=frontend` öppnar en viss utbildning (samma id:n som i jämförelsen).

Bädda in med ett block av typen Anpassad HTML. Iframen växer med innehållet:

```html
<iframe id="kursplan" src="https://iths-hemsida.github.io/jamfor-utbildningar/kursplan/" title="Utforska kursplanen" style="width:100%; height:1500px; border:0;" loading="lazy"></iframe>
<script>
  window.addEventListener("message", function(e){
    var fr = document.getElementById("kursplan");
    if (e.origin === "https://iths-hemsida.github.io" && e.source === fr.contentWindow && e.data && e.data.type === "kursplan-height") fr.style.height = e.data.h + "px";
  });
</script>
```

På en programsida kan iframen få `data-program="frontend"` för att visa just den utbildningen; den fullständiga koden finns i projektmappen (`kursplan/iframe-kod.txt`).
