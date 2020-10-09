# Vigtige forbedringer til Windows 10-apps (Windows 10 App Essentials) #

* Forfattere: Joseph Lee, Derek Riemer og andre brugere af Windows 10
* Download [stabil version][1]
* Download [udviklingsversion][2]
* NVDA compatibility: 2020.1 to 2020.3

Denne tilføjelse er en samling af app-moduler til forskellige Windows 10
apps, samt forbedringer og rettelser for visse windows 10 kontrolelementer.

Følgende app moduler eller støttemoduler for nogle apps er inkluderet (Se
hver appsektion for detaljer om, hvad der er inkluderet):

* Lommeregner (moderne).
* Kalender
* Cortana (samtaler)
* Mail
* Kort
* Microsoft Kabale Samling
* Microsoft store
* Moderne tastatur (Emoji-panel, diktering, forslag til hardwareinput,
  historik for udklipsholder i skyen og Input Method Editor)
* Personer
* Indstillinger (systemindstillinger, Windows+I)
* Vejr
* Diverse moduler til betjeninger som Start Menu-felter.

Bemærkninger:

* This add-on requires Windows 10 Version 1909 (build 18363) or later. For
  best results, use the add-on with latest Windows 10 stable release (build
  19041).
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
* Visse dialogbokse er nu anerkendt som ordentlige dialoger og rapporteret
  som sådan, herunder Insider Preview dialog (indstillinger app).
* NVDA kan annoncere nummeret af forslag, når du udfører en søgning i de
  fleste tilfælde. Denne indstilling styres af "Oplys information om
  objektets placering" i indstillingspanelet "Objektpræsentation".
* Når du søger i menuen Start eller Stifinder i version 1909 (november 2019
  Update) og senere, vil NVDA ikke længere annoncere søgeresultater to
  gange, når du gennemser resultater, hvilket også gør punktoutput mere
  ensartet, når du gennemgår elementer.
* The following UIA events are recognized: controller for, drag start, drag
  cancel, drag complete, drag target enter, drag target leave, drag target
  dropped, element selected, item status, live region change, notification,
  system alert, text change, tooltip opened, window opened. With NVDA set to
  run with debug logging enabled, these events will be tracked, and for UIA
  notification event, a debug tone will be heard if notifications come from
  somewhere other than the currently active app. Some events will provide
  additional information such as element count in controller for event,
  state of the element for state change event, and item text for item status
  event.
* Det er muligt at overvåge specifikke hændelser og/eller hændelser, der
  kommer fra specifikke apps.
* NVDA will no longer appear to do nothing or play error tones if UIA
  Automation Id for an element could not be recorded when tracking events.
* Når åbning, lukning, eller Skift mellem virtuelle skrivebord forekommer,
  vil NVDA annoncere nuværende desktop ID (f.eks. "Skrivebord 2").
* NVDA will no longer announce Start menu size text when changing screen
  resolution or orientation.
* Når du arrangerer fliser på start-menuen eller hurtige handlinger i
  Handlingscenter med Alt+Shift+piletasterne, vil NVDA oplyse informationer
  om emner, når disse flyttes.
* I de seneste udgivelser af Word 365 vil NVDA ikke længere meddele "slet
  ord bagud", når du trykker på Control+Backspace.
* Announcements such as volume/brightness changes in File Explorer and app
  update notifications from Microsoft Store can be suppressed by turning off
  Report Notifications in NVDA's object presentation settings.
* Open With dialog in Version 2004 (May 2020 Update) and later is announced
  when opened.

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

De fleste punkter er ikke længere gældende i version 1903 og senere,
medmindre Cortana Samtaler (version 2004 og nyere) er i brug.

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
  fremskridt af tilsvarende handling.

## Moderne tastatur

This includes emoji panel, clipboard history, dictation, hardware input
suggestions, and modern input method editors for certain languages. When
viewing emojis, for best experience, enable Unicode Consortium setting from
NVDA's speech settings and set symbol level to "some" or higher.

* NVDA vil ikke længere annoncere "Udklipsholder", når der er elementer i
  udklipsholderen under nogle omstændigheder.
* På nogle systemer, der kører version 1903 (May 2019 Update) og senere, vil
  NVDA ikke længere foretage sig ingenting, når Emoji panel åbnes.
* Tilføjet understøttelse af moderne kinesisk, japansk og koreansk (CJK)
  IME-kandidater interface introduceret i version 2004 (build 18965 og
  senere).
* When an emoji group (including kaomoji and symbols group in Version 1903
  or later) is selected, NVDA will no longer move navigator object to
  certain emojis.
* NVDA will announce selected emoji if emoji panel is opened more than once
  in build 20226.

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
