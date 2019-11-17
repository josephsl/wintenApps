# Windows 10 App Essentials (Vigtige forbedringer til Windows 10-apps) #

* Forfattere: Joseph Lee, Derek Riemer og andre brugere af Windows 10
* Download [stabil version][1]
* Download [udviklingsversion][2]
* NVDA compatibility: 2019.2 to 2019.3

Denne tilføjelse er en samling af app-moduler til forskellige Windows 10
apps, samt forbedringer og rettelser for visse windows 10 kontrolelementer.

Følgende app moduler eller støttemoduler for nogle apps er inkluderet (Se
hver appsektion for detaljer om, hvad der er inkluderet):

* Lommeregner (moderne).
* Kalender
* Cortana (klassisk og samtaler)
* Feedback Hub
* Mail
* Kort
* Microsoft Edge
* Microsoft store
* Moderne tastatur (Emoji-panel/Diktering/hardware input forslag/Cloud
  Udklipsholder i version 1709 og senere)
* Personer
* Indstillinger (systemindstillinger, Windows+I)
* Vejr
* Diverse moduler til betjeninger som Start Menu-felter.

Bemærkninger:

* This add-on requires Windows 10 Version 1809 (build 17763) or later and
  NVDA 2019.2 or later. For best results, use the add-on with latest Windows
  10 stable release (build 18363) and latest stable version of NVDA.
* Nogle funktioner tilføjelsespakken indeholder er eller bliver en del af
  NVDA skærmlæser.
* For emner, der ikke er anført nedenfor, kan du antage, at funktionerne er
  en del af NVDA, ikke længere gældende som tilføjelsesprogrammet ikke
  understøtter ældre Windows 10 udgivelser, eller ændringer til apps, der
  gør disse emner ugyldige.

For en liste over ændringer, der er fremstillet mellem hver udgivelse af
tilføjelsen, henvises til [ændringslog for tilføjelsen][3].

## Generelt

* NVDA vil ikke længere spille fejltoner eller gøre ingenting, hvis denne
  tilføjelse bliver aktiv fra Windows 7 og 8.1 og andre versioner af
  Windows, der ikke understøttes.
* Undermenupunkter er korrekt genkendt i forskellige apps, herunder
  kontekstmenu til Start-menufliser og Microsoft Edge-appmenuen (Version
  1809 October 2018 Update).
* Visse dialogbokse er nu anerkendt som ordentlige dialoger og rapporteret
  som sådan, herunder Insider Preview dialog (indstillinger app).
* NVDA kan annoncere nummeret af forslag, når du udfører en søgning i de
  fleste tilfælde. Denne indstilling styres af "Oplys information om
  objektets placering" i indstillingspanelet "Objektpræsentation".
* NVDA will no longer announce "blank" when pressing up or down arrow to
  open all apps views in Start menu. This will be part of NVDA 2019.3.
* When searching in Start menu or File Explorer in Version 1909 (November
  2019 Update) and later, instances of NVDA announcing search results twice
  when reviewing results are less noticeable, which also makes braille
  output more consistent when reviewing items.
* I visse kontekstmenuer (f.eks. i Microsoft Edge), er positionssoplysninger
  (f.eks. 1 af 2) ikke længere annonceret.
* The following UIA events are recognized: controller for, drag start, drag
  cancel, drag complete, drag target enter, drag target leave, drag target
  dropped, element selected, item status, live region change, notification,
  system alert, text change, tooltip opened, window opened. With NVDA set to
  run with debug logging enabled, these events will be tracked, and for UIA
  notification event, a debug tone will be heard if notifications come from
  somewhere other than the currently active app.
* Det er muligt at overvåge specifikke hændelser og/eller hændelser, der
  kommer fra specifikke apps.
* Værktøjstips fra Edge og universale apps er genkendte og vil blive
  annonceret. Dette vil være en del af NVDA 2019.3.
* Når åbning, lukning, eller Skift mellem virtuelle skrivebord forekommer,
  vil NVDA annoncere nuværende desktop ID (f.eks. "Skrivebord 2").
* NVDA vil ikke længere annoncere størrelsen af punkter på startmenuen, når
  du ændrer skærmopløsning eller orientering.
* Appnavn og-version for forskellige Microsoft store-apps vises nu
  korrekt. Dette vil være en del af NVDA 2019.3.
* When arranging Start menu tiles or Action Center quick actions with
  Alt+Shift+arrow keys, NVDA will announce information on dragged items or
  new position of the dragged item.

## Lommeregner

* Når der trykkes på ENTER eller Escape, vil NVDA annoncere
  beregningsresultaterne.
* For beregninger som enhedsberegninger og valutaberegninger, vil NVDA
  annoncere resultater så snart beregningerne er indtastet.
* NVDA vil ikke længere meddele "Overskriftsniveau", når resultater i
  Lommeregner annonceres.
* NVDA giver besked, hvis det maksimale antal cifre er nået, mens du
  indtaster udtryk.
* Understøttelse af Always On mode i Lommeregner version 10,1908 og nyere er
  tilføjet.

## Kalender

* NVDA annoncerer ikke længere "Edit" eller "skrivebeskyttet" i
  meddelelsesfelter og andre felter.

## Cortana

De fleste elementer er ikke længere gældende i version 1903 og
nyere. Klassisk Cortana refererer til ældre Cortana interface, som var en
del af start-menuen.

* Tekstmæssige svar fra Cortana (både Classisk og samtaler-UI) annonceres i
  de fleste situationer (hvis du bruger klassisk Cortana, genåbne start
  menuen og prøv at søge igen, hvis svarene ikke er annonceret).
* NVDA vil forblive tavs, når du taler til Cortana med stemmen.
* I klassisk Cortana vil NVDA annoncere bekræftelse af påmindelse, når du
  har angivet en.
* In Version 1909 (November 2019 Update) and 20H1 build 18945 and later,
  modern search experience in File Explorer powered by Windows Search user
  interface is supported.

## Feedback Hub

* For nyere app-udgivelser, vil NVDA ikke længere meddele feedback
  kategorier to gange.

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

## Microsoft Edge

Dette refererer til den klassiske EdgeHTML-baserede Microsoft Edge.

* Autofuldførelse af tekst vil blive sporet og annonceret i adressse
  omnibar. Dette vil være en del af NVDA 2019.3.
* NVDA vil ikke længere afspille lyden for forslag, når du trykker på F11
  for at ændre indstillingen for fuld skærm. Dette vil være en del af NVDA
  2019.3.
* Fjernede lyden for autoforslag for adresse Omnibar. Dette vil være en del
  af NVDA 2019.3.

## Microsoft store

* Efter kontrol for app opdateringer, app navne i listen af apps der skal
  opdateres er korrekt navngivet.
* Når du henter indhold som apps og film, vil NVDA annoncere produktnavn og
  fremskridt af tilsvarende handling.

## Moderne tastatur

Bemærk: De fleste funktioner nedenfor er nu en del af NVDA 2018.3 eller
nyere.

* Understøttelse for Emoji inputpanelet i Version 1709 (Fall Creators
  Update) og senere, herunder det redesignet panel i build version 1809
  17661 og senere, samt ændringer i 19H1 (build 18262). Du vil få den bedste
  oplevelse, når du læser emojis, hvis du benytter talesyntesen Windows
  OneCore. Hvis du benytter 2018.4 eller senere, skal du aktivér
  indstillingen der benytter Unicode Consortium data til emojis via NVDAs
  taleindstillinger. Derefter skal tegnsætningsniveauet indstilles til
  "nogle" eller højere.
* NVDA vil ikke længere annoncere "Udklipsholder", når der er elementer i
  udklipsholderen under nogle omstændigheder.
* På nogle systemer, der kører version 1903 (May 2019 Update) og senere, vil
  NVDA ikke længere foretage sig ingenting, når Emoji panel åbnes.
* Tilføjet understøttelse af moderne kinesisk, japansk og koreansk (CJK)
  IME-kandidater interface introduceret i 20H1 Build 18965 og senere.

## Personer

* Når du søger efter kontakter, vil forslag blive annoncerede, særligt hvis
  du kører de seneste app-udgivelser.

## indstillinger

* Visse oplysninger såsom fremdskridt af Windows-opdateringer rapporteres
  automatisk, herunder ved brug af Storage sense/disk cleanup widget.
* Værdier på behandlingslinjer og andre oplysninger er ikke længere
  annonceret to gange.
* For nogle combo boxe, vil NVDA ikke længere undlade at rapportere
  etiketter- og- eller annoncere værdiændringer.
* Bip for behandlingslinjer for lydstyrke høres nu ikke længere i version
  1803 og nyere. Dette vil være en del af NVDA 2019.3.
* NVDA ser ikke længere ud til at gøre ingenting eller afspille fejltoner,
  hvis du bruger objektnavigeringskommandoer under visse omstændigheder.
* Dialogboksen Windows Update-påmindelse genkendes som en korrekt dialog.
* Bemærkelsesværdige kontroletiketter ses i visse Windowt 10 installationer
  er blevet løst.
* I nyere versioner af version 1803 og nyere, på grund af ændringer i
  Windows Update-proceduren for FUNKTIONSOPDATERINGER, er linket "Hent og
  Installer nu" blevet tilføjet. NVDA vil nu annoncere titlen for den nye
  opdatering, hvis den findes.

## Vejr

* Faner som "Vejrudsigt" og "Kort" er nu genkendt korrekt som faner (patch
  af Derek Riemer).
* When reading a forecast, use the left and right arrows to move between
  items. Use the up and down arrows to read the individual items. For
  example, pressing the right arrow might report "Monday: 79 degrees, partly
  cloudy, ..." pressing the down arrow will say "Monday" Then pressing it
  again will read the next item (Like the temperature). This currently works
  for daily and hourly forecasts.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
