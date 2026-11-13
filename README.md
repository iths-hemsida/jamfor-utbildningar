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
- Där det finns ett nyare underlag för samma utbildning och ort gäller det i stället för iths.se (`src` i `PROGRAMS`): ansökan till MYH 2026 för Javautvecklare, IT-säkerhetsspecialist, .NET-utvecklare och IT-projektledare (`src: "app"`), och kursplanerna 2026 för IT-säkerhetstestare (`src: "kp"`). Nya kurser utan text i jämförelsen står i `EXTRA_INFO`, och kurser som bytt namn pekar på sin gamla beskrivning via `INFO_ALIAS`.
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

## Vad är frontend? (levande demo)

Mappen `vad-ar-frontend/` innehåller en demo för avsnittet "Vad är frontend?" på utbildningssidan för Frontend-utvecklare. Ett produktkort byggs upp i fyra lager: HTML, CSS, JavaScript och AI & UX.

- Källan är `vad-ar-frontend/snippet.html`. Kör `python3 tools/build-vad-ar-frontend.py` efter ändringar, så byggs `vad-ar-frontend/index.html` (GitHub Pages) och `wordpress/vad-ar-frontend-wpcode.html` (WPCode).
- WPCode: klistra in hela `wordpress/vad-ar-frontend-wpcode.html` i ett HTML-snippet. All CSS är avgränsad till `#iths-fe-demo`.
- Iframe: demon skickar sin höjd med `postMessage` (`type: "fe-demo-height"`), så iframen kan växa med innehållet.

## Javautvecklare i korthet (faktatabell)

Mappen `java-fakta/` innehåller en klickbar faktatabell för utbildningssidan Javautvecklare: start, studieort, längd, LIA, kostnad, CSN, behörighet, antagningsprov, dator och yrkesroller. Varje rad går att öppna för en kort förklaring. Fakta hämtades från iths.se/utbildningar/javautvecklare/ den 12 november 2026.

- Källan är `java-fakta/snippet.html` (raderna står i `RADER`). Kör `python3 tools/build-java-fakta.py` efter ändringar, så byggs `java-fakta/index.html` (GitHub Pages) och `wordpress/java-fakta-wpcode.html` (WPCode).
- All CSS är avgränsad till `#iths-java-fakta`.
- Iframe: tabellen skickar sin höjd med `postMessage` (`type: "java-fakta-height"`), så iframen växer och krymper när rader öppnas.

## Vad är Java? (levande demo)

Mappen `vad-ar-java/` innehåller en demo för utbildningssidan Javautvecklare: "Vad händer när du klickar på Köp?". Samma webbshop som i "Vad är frontend?", men nu syns servern bakom i fyra steg: API, logik (lagerkoll), databas och AI & kvalitet.

- Källan är `vad-ar-java/snippet.html`. Kör `python3 tools/build-vad-ar-java.py` efter ändringar, så byggs `vad-ar-java/index.html` (GitHub Pages) och `wordpress/vad-ar-java-wpcode.html` (WPCode).
- All CSS är avgränsad till `#iths-java-demo`.
- Iframe: demon skickar sin höjd med `postMessage` (`type: "java-demo-height"`).

## Vad är mjukvarutest? (levande demo)

Mappen `vad-ar-mjukvarutest/` innehåller en demo för utbildningssidan Mjukvarutestare med testautomation: "Hitta felen innan kunderna gör det". Samma webbshop som i "Vad är frontend?" och "Vad är Java?", men nu testas den i fyra steg: testfall (besökaren hittar en bugg i antalsväljaren), buggrapport, testautomation (Selenium klickar själv och Cucumber-testerna stoppar en trasig kodändring) och AI & kvalitet (godkänn eller avvisa AI:s förslag på testfall). Innehållet bygger på iths.se/utbildningar/mjukvarutestare/ (hämtad 12 november 2026), som nämner Selenium, Cucumber, JIRA, continuous testing och AI i testarbetet.

- Källan är `vad-ar-mjukvarutest/snippet.html`. Kör `python3 tools/build-vad-ar-mjukvarutest.py` efter ändringar, så byggs `vad-ar-mjukvarutest/index.html` (GitHub Pages) och `wordpress/vad-ar-mjukvarutest-wpcode.html` (WPCode).
- All CSS är avgränsad till `#iths-test-demo`.
- Iframe: demon skickar sin höjd med `postMessage` (`type: "test-demo-height"`).

## Vad är fullstack? (levande demo)

Mappen `vad-ar-fullstack/` innehåller en demo för utbildningssidan Fullstackutvecklare: "Bygg en funktion från knapp till databas". Samma webbshop som i de andra demona, men nu bygger besökaren recensioner genom hela kedjan i fyra steg: gränssnitt (React, recensionen försvinner när sidan laddas om), API (Node.js och Express, recensionen försvinner när servern startas om), databas (allt finns kvar och betyget räknas ut) och AI & kvalitet (godkänn AI:s förslag: stoppa tomma recensioner, ta bort kod ur texten och skriv tester). Innehållet bygger på iths.se/utbildningar/fullstackutvecklare/ (hämtad 12 november 2026), som nämner JavaScript, React, Node.js, Express, databaser och AI för kodning, felsökning och kvalitetssäkring.

- Källan är `vad-ar-fullstack/snippet.html`. Kör `python3 tools/build-vad-ar-fullstack.py` efter ändringar, så byggs `vad-ar-fullstack/index.html` (GitHub Pages) och `wordpress/vad-ar-fullstack-wpcode.html` (WPCode).
- All CSS är avgränsad till `#iths-fs-demo`.
- Iframe: demon skickar sin höjd med `postMessage` (`type: "fullstack-demo-height"`).

## Vad är UX? (levande demo)

Mappen `vad-ar-ux/` innehåller en demo för utbildningssidan UX-designer: "Design som människor vill använda". Samma webbshop som i de andra demona, men nu görs den lätt att använda i fyra steg: research (spela upp ett användartest där Sara inte lyckas köpa), prototyp (fixa pris, färgval och köpknapp och låt Sara testa igen: från inget köp till klart på 8 sekunder), tillgänglighet (välj en färg på köpknappen som klarar kontrastkravet 4,5:1, och se butiken med nedsatt syn) och AI & UX (godkänn eller avvisa AI:s designförslag, där ett av dem är ett mörkt mönster). Innehållet bygger på iths.se/utbildningar/ux-designer/ (hämtad 12 november 2026), som nämner research, användarcentrerad design, prototyper, tillgänglighetslagen och AI som verktyg i designprocessen.

- Källan är `vad-ar-ux/snippet.html`. Kör `python3 tools/build-vad-ar-ux.py` efter ändringar, så byggs `vad-ar-ux/index.html` (GitHub Pages) och `wordpress/vad-ar-ux-wpcode.html` (WPCode).
- All CSS är avgränsad till `#iths-ux-demo`.
- Iframe: demon skickar sin höjd med `postMessage` (`type: "ux-demo-height"`).

## Vad är .NET? (levande demo)

Mappen `vad-ar-dotnet/` innehåller en demo för utbildningssidan .NET-utvecklare: "Bygg en rabattkod med C# och .NET". Samma webbshop som i de andra demona, men nu byggs en rabattkod i fyra steg: C# (bygget stoppas av ett typfel, "10%" är text och inte ett tal, och besökaren rättar raden), webb-API (servern räknar ut priset, så det går inte att fuska med priset i webbläsaren), databas (rabattkoderna ligger i en tabell, besökaren lägger till en ny kod utan att bygga om och ser att en utgången kod stoppas) och AI & kvalitet (låt AI granska koden: godkänn tre förslag och avvisa ett som tar bort datumkollen, och se enhetstesterna slå larm). Innehållet bygger på iths.se/utbildningar/netutvecklare/ (hämtad 12 november 2026), som nämner C#, Visual Studio, webbapplikationer och API:er, databaser, clean code, testbar kod och "Låt AI granska din kod".

- Källan är `vad-ar-dotnet/snippet.html`. Kör `python3 tools/build-vad-ar-dotnet.py` efter ändringar, så byggs `vad-ar-dotnet/index.html` (GitHub Pages) och `wordpress/vad-ar-dotnet-wpcode.html` (WPCode).
- All CSS är avgränsad till `#iths-net-demo`.
- Datumen i rabattabellen räknas från dagens datum, så att demon fungerar oavsett när den visas.
- Iframe: demon skickar sin höjd med `postMessage` (`type: "net-demo-height"`).

## Vad är Cloud? (levande demo)

Mappen `vad-ar-cloud/` innehåller en demo för utbildningssidan .NET Cloud Developer: "Ta butiken ut i molnet". Samma webbshop som i de andra demona, men nu flyttas den från din dator till Microsoft Azure i fyra steg: driftsätt (paketera i en Docker-container, skapa en webbapp i Azure och driftsätt, och testa att butiken nu nås från mobilen), skala (välj 1 server, 5 servrar hela tiden eller autoskalning och kör Black Friday: en server ger 503, fem kostar mest, autoskalning klarar rusningen och skalar ner efteråt), säkerhet (skanna och fixa en öppen databas, ett lösenord i koden och för breda behörigheter) och AI & moln (godkänn eller avvisa AI:s förslag, där ett av dem öppnar databasen för alla). Innehållet bygger på iths.se/utbildningar/net-cloud-developer/ (hämtad 12 november 2026), som nämner C#, .NET, Azure, molnarkitektur, IT-säkerhet, automatisering, Docker, skalbarhet, kostnader och AI-verktyg. Priserna i demon är exempel.

- Källan är `vad-ar-cloud/snippet.html`. Kör `python3 tools/build-vad-ar-cloud.py` efter ändringar, så byggs `vad-ar-cloud/index.html` (GitHub Pages) och `wordpress/vad-ar-cloud-wpcode.html` (WPCode).
- All CSS är avgränsad till `#iths-cloud-demo`.
- Iframe: demon skickar sin höjd med `postMessage` (`type: "cloud-demo-height"`).

## Vad är IT-säkerhet? (levande demo)

Mappen `vad-ar-it-sakerhet/` innehåller en demo för utbildningssidan IT-säkerhetsspecialist: "Skydda butiken mot angrepp". Samma webbshop som i de andra demona, men nu ska den skyddas i fyra steg: kryptering (Anna loggar in från ett café och angriparen på samma wifi läser lösenordet, tills besökaren skaffar ett certifikat och slår på HTTPS), loggar (läs inloggningsloggen, hitta adressen som provar lösenord mot många konton och blockera den i brandväggen, utan att blockera en kund eller butikens egen server), incident (ransomware har krypterat butiken: isolera servern, täpp till hålet, återställ från backup och skriv en incidentrapport i rätt ordning, och betala aldrig lösensumman) och AI & säkerhet (godkänn eller avvisa AI:s förslag, där ett av dem stänger av loggningen). Innehållet bygger på iths.se/utbildningar/it-sakerhetsspecialist/ (hämtad 12 november 2026), som nämner hot som virus, ransomware och nätverksintrång, logganalys, incidenthantering, spårbarhet, återställning efter attacker, kryptering, nätverkssäkerhet och AI för att förutse attacker. IP-adresser, lösenord och belopp i demon är påhittade exempel.

- Källan är `vad-ar-it-sakerhet/snippet.html`. Kör `python3 tools/build-vad-ar-it-sakerhet.py` efter ändringar, så byggs `vad-ar-it-sakerhet/index.html` (GitHub Pages) och `wordpress/vad-ar-it-sakerhet-wpcode.html` (WPCode).
- All CSS är avgränsad till `#iths-sak-demo`.
- Iframe: demon skickar sin höjd med `postMessage` (`type: "sakerhet-demo-height"`).

## Vad är IT-säkerhetstest? (levande demo)

Mappen `vad-ar-it-sakerhetstest/` innehåller en demo för utbildningssidan IT-säkerhetstestare: "Hacka butiken innan någon annan gör det". Samma webbshop som i de andra demona, men nu penetrationstestas den i fyra steg: kartlägg (skanna butiken.se med Nmap och hitta en adminsida på port 8080, men stoppas om du försöker skanna betaltjänsten som inte ingår i uppdraget), hitta hålet (fånga köpet i Burp Suite, ändra priset till 1 kr och se servern godta det), rapport (bedöm risken Hög, Medel eller Låg för tre fynd, skicka rapporten och gör ett omtest som visar att hålet är tätat) och AI & pentest (godkänn AI-agentens Python-skript och kodgranskning, men avvisa förslaget att attackera betala.se). Innehållet bygger på IT-Högskolans kursplaner 2026 för IT-säkerhetstestare (samma underlag som i jämförelsen och kursplansutforskaren), som nämner pentestrapporter, NIS2 och GDPR, Nmap och Wireshark, Nessus, OWASP, Burp Suite, Python och AI-agenter för att skriva kod och automatisera penetrationstester.

- Källan är `vad-ar-it-sakerhetstest/snippet.html`. Kör `python3 tools/build-vad-ar-it-sakerhetstest.py` efter ändringar, så byggs `vad-ar-it-sakerhetstest/index.html` (GitHub Pages) och `wordpress/vad-ar-it-sakerhetstest-wpcode.html` (WPCode).
- All CSS är avgränsad till `#iths-pen-demo`.
- Iframe: demon skickar sin höjd med `postMessage` (`type: "pentest-demo-height"`).

## Vad är Account Manager inom IT? (levande demo)

Mappen `vad-ar-account-manager/` innehåller en demo för utbildningssidan Account Manager inom IT: "Vinn kunden och behåll den". Samma webbshop som i de andra demona, men nu är butiken kunden och besökaren säljer en IT-lösning till den i fyra steg: behov (ställ frågor till butikens ägare Sara och fyll i kundkortet i CRM, men gå inte rakt på försäljningen), erbjudande (välj de delar som löser butikens tre problem och ryms i budgeten, se business caset och presentera, utan appen för smartklockor som ingen bett om), förhandling (svara på ekonomichefens invändningar med värde, ett SLA och lägre pris mot längre avtal, i stället för att ge bort marginalen) och AI & relation (godkänn AI:s mötessammanfattning och kvartalsunderlag, men avvisa förslaget att låta AI svara en irriterad kund med ett standardmejl). Innehållet bygger på iths.se/utbildningar/account-manager-inom-it/ (hämtad 12 november 2026), som beskriver rollen i gränslandet mellan kund, affär och teknik: hela säljprocessen från prospektering till avslut, kundbehov och värdebaserade IT-lösningar, CRM, förhandling och avtal, business case och ROI, och AI för att effektivisera säljet medan relationer och förtroende förblir mänskligt arbete. Namn, priser och siffror i demon är påhittade exempel.

- Källan är `vad-ar-account-manager/snippet.html`. Kör `python3 tools/build-vad-ar-account-manager.py` efter ändringar, så byggs `vad-ar-account-manager/index.html` (GitHub Pages) och `wordpress/vad-ar-account-manager-wpcode.html` (WPCode).
- All CSS är avgränsad till `#iths-am-demo`.
- På mobil (när demon är högst 600 px bred) är butiken ihopfälld bakom "Visa butiken" (det som ändrats i butiken syns ändå som gröna och röda etiketter), anteckningarna visar de tre senaste raderna med "Hela loggen", svaren på frågorna och de lösta invändningarna visas bara i kundkortet och anteckningarna, och AI-korten i steg 4 öppnas ett i taget och fälls ihop till en svarsrad. På dator är allt utfällt.
- Iframe: demon skickar sin höjd med `postMessage` (`type: "am-demo-height"`).

## Vad är IT-projektledare? (levande demo)

Mappen `vad-ar-it-projektledare/` innehåller en demo för utbildningssidan IT-projektledare: "Led projektet hela vägen till lansering". Samma webbshop som i de andra demona, men nu ska den lanseras till Black Friday i fyra steg: planera (kunden vill ha sex funktioner på 31 poäng men teamet hinner 20, så besökaren prioriterar och ser att produktsida, varukorg och betalning måste vara med), sprint (spela upp en Scrum-sprint där betalningen blockeras på daily standup dag 4, och bara om du som Scrum Master tar bort hindret blir allt klart i tid), risker (hantera en risk och två intressenter, VD:n som vill ha en chattbot i sista stund och kundtjänst som inte vet vad som lanseras, och se lamporna för tid, kvalitet och kund) och AI & projekt (godkänn AI:s statusrapport och riskanalys av tidplanen, men avvisa förslaget att lägga kundregistret i en gratis AI-tjänst). Innehållet bygger på iths.se/utbildningar/it-projektledare/ (hämtad 12 november 2026), som nämner Scrum, Agile och Lean, att planera och driva IT-projekt från behovsanalys till leverans, kommunikation med kunder, intressenter och utvecklingsteam, resurser, risker och deadlines samt rollen som Scrum Master, och på kursen Projektverktyg och dokumentation i ansökan till MYH 2026, som tar upp AI-verktyg för analys, planering och riskidentifiering.

- Källan är `vad-ar-it-projektledare/snippet.html`. Kör `python3 tools/build-vad-ar-it-projektledare.py` efter ändringar, så byggs `vad-ar-it-projektledare/index.html` (GitHub Pages) och `wordpress/vad-ar-it-projektledare-wpcode.html` (WPCode).
- All CSS är avgränsad till `#iths-pl-demo`.
- På mobil (när demon är högst 600 px bred) är butiken ihopfälld bakom "Visa butiken", loggen visar de tre senaste raderna, user stories visas på begäran och korten i steg 3 och 4 öppnas ett i taget. På dator är allt utfällt.
- Iframe: demon skickar sin höjd med `postMessage` (`type: "projektledare-demo-height"`).

## Därför är frontend-utvecklare ett framtidsyrke

Mappen `framtidsyrke/` innehåller fyra kort för avsnittet med samma namn på utbildningssidan för Frontend-utvecklare. Varje kort har en liten interaktiv illustration: enheter, AI-förslag, ett reglage mellan kod och design, och yrkesroller.

- Källan är `framtidsyrke/snippet.html`. Kör `python3 tools/build-framtidsyrke.py` efter ändringar.
- WPCode: `wordpress/framtidsyrke-wpcode.html`. All CSS är avgränsad till `#iths-fe-framtid`.
- Iframe: höjden skickas med `postMessage` (`type: "fe-framtid-height"`).

## Vem är du? (vem-ar-du/)

Självkoll för Frontend-sidan: fem påståenden, en mätare och ett nästa steg (4–5 → "Det låter som du!", 0–3 → quizet). Redigera `vem-ar-du/snippet.html` och kör `python3 tools/build-vem-ar-du.py`. Länkarna ställs in i `LANKAR` i skriptet. WPCode-version: `wordpress/vem-ar-du-wpcode.html`.

## Därför är mjukvarutestare ett framtidsyrke (framtidsyrke-mjukvarutest/)

Fem enkla kort (bock, rubrik och text) för Mjukvarutestare-sidan, under en kort ingress. Redigera `framtidsyrke-mjukvarutest/snippet.html` och kör `python3 tools/build-framtidsyrke-mjukvarutest.py`. WPCode-version: `wordpress/framtidsyrke-mjukvarutest-wpcode.html`.

## Vem är du? Mjukvarutestare (vem-ar-du-mjukvarutest/)

Samma självkoll som för Frontend, med fem av punkterna från Mjukvarutestare-sidan. Redigera `vem-ar-du-mjukvarutest/snippet.html` och kör `python3 tools/build-vem-ar-du-mjukvarutest.py`. WPCode-version: `wordpress/vem-ar-du-mjukvarutest-wpcode.html`.

## LIA-praktik (lia-mjukvarutest/)

Snyggare LIA-avsnitt för Mjukvarutestare-sidan: punkterna som ikonrutor och nyckeltalen 16 veckor (med en veckostapel som fylls i när blocket syns) och 100 %. Redigera `lia-mjukvarutest/snippet.html` och kör `python3 tools/build-lia-mjukvarutest.py`. WPCode-version: `wordpress/lia-mjukvarutest-wpcode.html`.

## Därför är frontend-utvecklare ett framtidsyrke, enkla kort (framtidsyrke/enkla-kort-snippet.html)

Alternativ till de levande korten: samma ingress och fyra enkla kort med bock, rubrik och text. Kör `python3 tools/build-framtidsyrke-enkla-kort.py`. WPCode-version: `wordpress/framtidsyrke-enkla-kort-wpcode.html`.

## Därför är fullstackutvecklare ett framtidsyrke (framtidsyrke-fullstack/)

Ingress och fem enkla kort med bock, rubrik och text. Redigera `framtidsyrke-fullstack/snippet.html` och kör `python3 tools/build-framtidsyrke-fullstack.py`. WPCode-version: `wordpress/framtidsyrke-fullstack-wpcode.html`.

## Vem är du? UX-designer (vem-ar-du-ux/)

Samma självkoll som för Frontend och Mjukvarutestare, med fem av punkterna från UX-designer-sidan. Kör `python3 tools/build-vem-ar-du-ux.py`. WPCode-version: `wordpress/vem-ar-du-ux-wpcode.html`.

## Därför är javautvecklare ett framtidsyrke (framtidsyrke-java/)

Ingress och fem enkla kort med bock, rubrik och text. Redigera `framtidsyrke-java/snippet.html` och kör `python3 tools/build-framtidsyrke-java.py`. WPCode-version: `wordpress/framtidsyrke-java-wpcode.html`.

## Vem är du? Javautvecklare (vem-ar-du-java/)

Samma självkoll som de andra, med fem av punkterna för Java. Kör `python3 tools/build-vem-ar-du-java.py`. WPCode-version: `wordpress/vem-ar-du-java-wpcode.html`.

## Därför är .NET ett framtidsyrke (framtidsyrke-dotnet/)

Ingress och fem enkla kort med bock, rubrik och text. Redigera `framtidsyrke-dotnet/snippet.html` och kör `python3 tools/build-framtidsyrke-dotnet.py`. WPCode-version: `wordpress/framtidsyrke-dotnet-wpcode.html`.

## Vem är du? .NET-utvecklare (vem-ar-du-dotnet/)

Samma självkoll som de andra, med fem av punkterna för .NET. Kör `python3 tools/build-vem-ar-du-dotnet.py`. WPCode-version: `wordpress/vem-ar-du-dotnet-wpcode.html`.

## Därför är .NET Cloud ett framtidsyrke (framtidsyrke-dotnet-cloud/)

Ingress och fyra enkla kort med bock, rubrik och text. Redigera `framtidsyrke-dotnet-cloud/snippet.html` och kör `python3 tools/build-framtidsyrke-dotnet-cloud.py`. WPCode-version: `wordpress/framtidsyrke-dotnet-cloud-wpcode.html`.

## Vem är du? .NET Cloud (vem-ar-du-dotnet-cloud/)

Samma självkoll som de andra, med fem av punkterna för .NET Cloud. Kör `python3 tools/build-vem-ar-du-dotnet-cloud.py`. WPCode-version: `wordpress/vem-ar-du-dotnet-cloud-wpcode.html`.
