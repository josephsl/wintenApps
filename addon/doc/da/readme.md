# Windows 10 App Essentials (Vigtige forbedringer til Windows 10-apps) #

* Forfattere: Joseph Lee, Derek Riemer og andre brugere af Windows 10
* Download [stabil version][1]
* Download [udviklingsversion][2]
* NVDA compatibility: 2019.3 and beyond

Denne tilføjelse er en samling af app-moduler til forskellige Windows 10
apps, samt forbedringer og rettelser for visse windows 10 kontrolelementer.

Følgende app moduler eller støttemoduler for nogle apps er inkluderet (Se
hver appsektion for detaljer om, hvad der er inkluderet):

* Lommeregner (moderne).
* Kalender
* Cortana (Conversations)
* Mail
* Kort
* Microsoft store
* Modern keyboard (emoji panel/dictation/hardware input suggestions/cloud
  clipboard history/modern input method editors)
* Personer
* Indstillinger (systemindstillinger, Windows+I)
* Vejr
* Diverse moduler til betjeninger som Start Menu-felter.

Bemærkninger:

* This add-on requires Windows 10 Version 1903 (build 18362) or later. For
  best results, use the add-on with latest Windows 10 stable release (build
  18363).
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
* When searching in Start menu or File Explorer in Version 1909 (November
  2019 Update) and later, instances of NVDA announcing search results twice
  when reviewing results are less noticeable, which also makes braille
  output more consistent when reviewing items.
* The following UIA events are recognized: controller for, drag start, drag
  cancel, drag complete, drag target enter, drag target leave, drag target
  dropped, element selected, item status, live region change, notification,
  system alert, text change, tooltip opened, window opened. With NVDA set to
  run with debug logging enabled, these events will be tracked, and for UIA
  notification event, a debug tone will be heard if notifications come from
  somewhere other than the currently active app.
* Det er muligt at overvåge specifikke hændelser og/eller hændelser, der
  kommer fra specifikke apps.
* Når åbning, lukning, eller Skift mellem virtuelle skrivebord forekommer,
  vil NVDA annoncere nuværende desktop ID (f.eks. "Skrivebord 2").
* NVDA vil ikke længere annoncere størrelsen af punkter på startmenuen, når
  du ændrer skærmopløsning eller orientering.
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

Most items are no longer applicable on Version 1903 and later unless Cortana
Conversations (Version 2004 and later) is in use.

* Textual responses from Cortana are announced in most situations.
* NVDA vil forblive tavs, når du taler til Cortana med stemmen.
* In Version 1909 (November 2019 Update) and later, modern search experience
  in File Explorer powered by Windows Search user interface is supported.

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

## Microsoft store

* Efter kontrol for app opdateringer, app navne i listen af apps der skal
  opdateres er korrekt navngivet.
* Når du henter indhold som apps og film, vil NVDA annoncere produktnavn og
  fremskridt af tilsvarende handling.

## Moderne tastatur

This includes emoji panel, clipboard history, dictation, hardware input
suggestions, and modern input method editors for certain languages. When
viewing emojis, for best experience, enable Unicode Consortium setting from
NVDA's speech settings and set symbol level to "Some" or higher.

* When opening clipboard history, NVDA will no longer announce "clipboard"
  when there are items in the clipboard under some circumstances.
* På nogle systemer, der kører version 1903 (May 2019 Update) og senere, vil
  NVDA ikke længere foretage sig ingenting, når Emoji panel åbnes.
* Added support for modern Chinese, Japanese, and Korean (CJK) IME
  candidates interface introduced in Version 2004 (build 18965 and later).

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
