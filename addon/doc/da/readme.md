# Vigtige forbedringer til Windows apps (Windows App Essentials) #

* Forfattere: Joseph Lee, Derek Riemer og andre brugere af Windows 10
* Download [stabil version][1]
* Download [udviklingsversion][2]
* NVDA-kompatibilitet: 2020.4 og derover

Bemærk: Denne tilføjelse hed Windows 10 App Essentials, men er blevet omdøbt
til Windows App Essentials i 2021 for at understøtte Windows 10 og
fremtidige udgivelser som Windows 11. Dele af dette tilføjelsesprogram vil
stadig henvise til det originale navn for tilføjelsen.

Denne tilføjelse er en samling af app-moduler til forskellige Windows-apps,
samt forbedringer og rettelser for visse windows 10 kontrolelementer.

Følgende app moduler eller støttemoduler for nogle apps er inkluderet (Se
hver appsektion for detaljer om, hvad der er inkluderet):

* Lommeregner (moderne)
* Kalender
* Cortana (samtaler)
* Mail
* Kort
* Microsoft Kabale Samling
* Microsoft store
* Moderne tastatur (Emoji-panel, diktering, forslag til hardwareinput,
  historik for udklipsholder og Editor til inputmetode)
* Personer
* Indstillinger (systemindstillinger, Windows+I)
* Vejr
* Diverse moduler til kontrolelementer som Start Menu-felter.

Bemærkninger:

* Denne tilføjelse kræver Windows 10 20H2 (build 19042) eller nyere. For at
  få de bedste resultater skal du bruge tilføjelsen med den nyeste
  Windows-udgivelse (Windows 10 21H1/build 19043).
* Selvom installation er mulig, understøtter denne tilføjelse ikke Windows
  Enterprise LTSC (Long-Term Servicing Channel) og Windows
  Server-udgivelser.
* Understøttelse for Windows 11 er eksperimentel, og nogle funktioner
  fungerer ikke (se relevante afsnit for detaljer).
* Nogle funktioner tilføjelsespakken indeholder er eller bliver en del af
  NVDA skærmlæser.
* For funktioner, der ikke er anført nedenfor, kan du antage, at funktioner
  er en del af NVDA, ikke længere kan anvendes, da tilføjelsesprogrammet
  ikke understøtter udgåede Windows-udgivelser såsom gamle Windows
  10-versioner, eller der blev foretaget ændringer i Windows og apps, der
  gør at disse ikke længere er aktuelle.
* Nogle apps understøtter kompakt overlejring (for eksempel Bevar Øverst i
  lommeregner), og denne tilstand fungerer ikke korrekt med flytbare kopier
  af NVDA.

For en liste over ændringer, der er fremstillet mellem hver udgivelse af
tilføjelsen, henvises til [ændringslog for tilføjelsen][3].

## Generelt

* NVDA kan annoncere nummeret af forslag, når du udfører en søgning i de
  fleste tilfælde. Denne indstilling styres af "Oplys information om
  objektets placering" i indstillingspanelet "Objektpræsentation".
* Når du søger i startmenuen eller Stifinder i version 1909 (november 2019
  Update) og senere, vil NVDA ikke længere annoncere søgeresultater to
  gange, når du gennemser resultater, hvilket også gør punktoutput mere
  ensartet, når du gennemgår elementer.
* Udover de UIA-håndteringsmuligheder, som NVDA leverer, vil følgende
  UIA-hændelser blive opfanget af skærmlæseren: drag start, drag cancel,
  drag complete, drop target drag enter, drop target drag leave, drop target
  dropped. Hvis NVDAs logningsniveau er indstillet til "Fejlfinding", vil
  disse hændelser blive sporet, og en tone vil blive hørt, hvis en
  UIA-hændelse stammer fra andet end den aktuelt fokuserede app. Nogle
  hændelser angiver yderligere oplysninger, såsom antal af elementer i
  kontrolhændelsen, status for elementet ved en hændelse, hvor status
  ændres, samt emnetekst for hændelser, hvor der anmodes om emnestatus.
* Det er muligt at overvåge specifikke hændelser og/eller hændelser, der
  kommer fra specifikke apps.
* Når åbning, lukning, ændring af rækkefølge (Windows 11) eller Skift mellem
  virtuelle skrivebord forekommer, vil NVDA annoncere det aktuelle navn for
  det virtuelle skrivebord (f.eks. "Skrivebord 2").
* NVDA vil ikke længere annoncere størrelsen af punkter på startmenuen, når
  du ændrer skærmopløsning eller orientering.
* Når du arrangerer fliser på start-menuen eller hurtige handlinger i
  Handlingscenter med Alt+Shift+piletasterne, vil NVDA oplyse informationer
  om emner, når disse flyttes.
* Meddelelser, som ændringer i lydstyrke/lysstyrke i Stifinder og
  appopdateringsmeddelelser fra Microsoft Store, kan deaktiveres ved at
  deaktivere rapportering af meddelelserne i NVDAs
  objektpræsentationsindstillinger.

## Lommeregner

* NVDA annoncerer ikke længere en meddelelse om grafregnerens skærmbillede
  to gange.

## Kalender

* NVDA annoncerer ikke længere "Edit" eller "skrivebeskyttet" i
  meddelelsesfelter og andre felter.

## Cortana

De fleste funktioner er anvendelige, når du bruger Cortana-samtaler (Windows
10 2004 og nyere).

* Tekstlige svar fra Cortana annonceres i de fleste tilfælde.
* NVDA vil forblive tavs, når du taler til Cortana med stemmen.
* I version 1909 (november 2019-opdatering) og senere understøttes den
  moderne søgeoplevelse i Stifinder drevet af brugergrænseflade til Windows
  Søg.

## Mail

* Når du gennemgår emner i meddelelseslisten, kan du nu bruge
  tabelnavigationskommandoer til at gennemgå
  meddelelsesoverskrifter. Bemærk, at navigering mellem rækker (meddelelser)
  ikke understøttes.
* Når du skriver en besked, vil @omtale forslag indikeres med lyd, når de
  vises.

## Kort

* NVDA spiller placeringsbip for kortlokationer.
* Når du bruger side street view, og hvis indstillingen "Brug tastaturet" er
  aktiveret, annoncere NVDA gadenavne, som du bruger piletasterne til at
  navigere kortet.

## Microsoft Kabale Samling

* NVDA vil annoncere navnene på kort og kortdæk.

## Microsoft store

* Efter kontrol for app opdateringer, app navne i listen af apps der skal
  opdateres er korrekt navngivet.
* Når du henter indhold som apps og film, vil NVDA annoncere produktnavn og
  fremskridt af tilsvarende handling (virker ikke i øjeblikket som forventet
  i den nyere Microsoft Store til Windows 11).

## Moderne tastatur

Dette inkluderer emoji-panelet, historik for udklipsholderen, diktering,
forslag i forhold til hardwareinput og moderne Input Methodf Editor for
visse sprog. Når du ser emojier, skal du for at få den bedste oplevelse
aktivere Unicode Consortium-indstillingen fra NvDAs taleindstillinger og
indstille tegnsætningsniveauet til "nogle" eller højere. NVDA understøtter
også det opdaterede inputoplevelsespanel i Windows 11.

* NVDA vil ikke længere annoncere "Udklipsholder", når der er elementer i
  udklipsholderen under nogle omstændigheder.
* På nogle systemer, der kører version 1903 (May 2019 Update) og senere, vil
  NVDA ikke længere foretage sig ingenting, når Emoji panel åbnes.
* Når en emoji-gruppe (inklusive kaomoji og symbolgrupper i version 1903
  eller nyere) er valgt, vil NVDA ikke længere flytte navigatorobjektet til
  bestemte emojis.
* Understøtter nu opdateret input-oplevelsespanel (kombineret emoji-panel og
  udklipsholderhistorik) i Windows 11.

## Personer

* Når du søger efter kontakter, vil forslag blive annoncerede, særligt hvis
  du kører de seneste app-udgivelser.

## indstillinger

* Visse oplysninger såsom fremdskridt af Windows-opdateringer rapporteres
  automatisk, herunder ved brug af Storage sense/disk cleanup widget.
* Værdier på behandlingslinjer og andre oplysninger er ikke længere
  annonceret to gange.
* Dialogboksen Windows Update-påmindelse genkendes som en korrekt dialog.
* Bemærkelsesværdige kontroletiketter set i visse Windows-installationer er
  blevet løst.
* NVDA annoncerer navnet på linket for den valgfrie kvalitetsopdatering,
  hvis det findes, typisk kaldet "Hent og installer nu".

## Vejr

* Faner som "Vejrudsigt" og "Kort" er nu genkendt korrekt som faner (patch
  af Derek Riemer).
* Når du læser en vejrudsigt, skal du bruge venstre og højre pil til at
  flytte mellem emner. Brug pilene op og ned for at læse de enkelte
  elementer. For eksempel, ved at trykke på højre pil vil du måske høre
  "mandag: 79 grader, delvist skyet,..." ved at trykke på pil ned vil NVDA
  sige "Mandag". Ved et yderligere tryk vil du gå videre til næste element
  (som temperatur). Dette virker i øjeblikket for daglig og vejrudsigt for
  hver time.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
