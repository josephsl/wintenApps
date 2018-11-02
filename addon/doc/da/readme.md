# Windows 10 App Essentials (Vigtige forbedringer til Windows 10-apps) #

* Forfattere: Joseph Lee, Derek Riemer og andre brugere af Windows 10
* Download [stabil version][1]
* Download [udviklingsversion][2]

Denne tilføjelse er en samling af app-moduler til forskellige Windows 10
apps, samt forbedringer og rettelser for visse windows 10 kontrolelementer.

Følgende app moduler eller støttemoduler for nogle apps er inkluderet (Se
hver appsektion for detaljer om, hvad der er inkluderet):

* Action center
* Alarmer og ur.
* Kalender
* Lommeregner (moderne).
* Cortana
* Feedback Hub
* Spillinje
* Mail
* Kort
* Microsoft Edge
* Moderne tastatur (emoji-panel, hardware-indtastningsforslag Cloud-emner i
  udklipsholderen i version 1709 og nyere)
* Personer
* Indstillinger (systemindstillinger, Windows+I)
* Skype (Universal App)
* Store
* Vejr
* Diverse moduler til betjeninger som Start Menu-felter.

Bemærkninger:

* This add-on requires Windows 10 Version 1709 (build 16299) or later and
  NVDA 2018.3 or later. For best results, use the add-on with latest Windows
  10 stable release (build 17134) and latest stable version of NVDA. Note
  that until further notice, Version 1809 (build 17763) is not available
  from Microsoft.
* Nogle funktioner tilføjelsespakken indeholder er eller bliver en del af
  NVDA skærmlæser.
* For emner, der ikke er anført nedenfor, kan du antage, at funktionerne er
  en del af NVDA, ikke længere gældende som tilføjelsesprogrammet ikke
  understøtter ældre Windows 10 udgivelser, eller ændringer til apps, der
  gør disse emner ugyldige.

For en liste over ændringer, der er fremstillet mellem hver udgivelse af
tilføjelsen, henvises til [ændringslog for tilføjelsen][3].

## Generelt

* If Add-on Updater add-on is installed, that add-on will check for Windows
  10 App Essentials updates.
* Default update check interval has changed to weekly checks for both stable
  and development releases. This is applicable if the add-on itself checks
  for updates.
* Undermenupunkter er korrekt genkendt i forskellige apps, herunder
  kontekstmenu til Start-menufliser og Microsoft Edge-appmenuen (Redstone
  5).
* Certain dialogs are now recognized as proper dialogs and reported as such,
  including Insider Preview dialog (settings app). This is now part of NVDA
  2018.3.
* NVDA kan annoncere nummeret af forslag, når du udfører en søgning i de
  fleste tilfælde. Denne indstilling styres af "Oplys information om
  objektets placering" i objektet præsentation dialog/panel.
* I visse kontekstmenuer (f.eks. i Microsoft Edge), er positionssoplysninger
  (f.eks. 1 af 2) ikke længere annonceret.
* The following UIA events are recognized: active text position change,
  controller for, drag start, drag cancel, drag complete, element selected,
  item status, live region change, notification, system alert, tooltip
  opened, window opened. With NVDA set to run with debug logging enabled,
  these events will be tracked, and for UIA notification event, a debug tone
  will be heard if notifications come from somewhere other than the
  currently active app.
* Notifications from newer app releases on Windows 10 Version 1709 (build
  16299) and later are announced. NVDA 2018.2 and later supports this, with
  2018.3 adding support for more notifications.
* Værktøjstips fra Edge og universale apps er genkendte og vil blive
  annonceret.
* Når åbning, lukning, eller Skift mellem virtuelle skrivebord forekommer,
  vil NVDA annoncere nuværende desktop ID (skrivebord 2, for eksempel).
* NVDA vil ikke længere annoncere størrelsen af punkter på startmenuen, når
  du ændrer skærmopløsning eller orientering.

## Action center

* Brightness quick action is now a button instead of a toggle button.
* Various status changes such as Focus Assist and Brightness will be
  reported.

## Alarmer og ur

* Tidvælgerværdier er nu annonceret, mærkbart, når du flytter fokus til
  vælgekontroller. Dette påvirker også den kontrol, der bliver brugt til at
  vælge, hvornår du vil genstart for at afslutte installationen af
  Windows-opdateringer.

## Lommeregner

* Når enter eller Esc trykkes, vil NVDA nu annoncerer resultatet
* For beregninger som enhedsberegninger og valutaberegninger, vil NVDA
  annoncere resultater så snart beregningerne er indtastet.
* NVDA vil ikke længere meddele "Overskriftsniveau", når resultater i
  Lommeregner annonceres.

## kalender

* NVDA annoncerer ikke længere "Edit" eller "skrivebeskyttet" i
  meddelelsesfelter og andre felter.

## Cortana

* Tekstmæssige svar fra Cortana er annonceret i de fleste situationer (hvis
  det ikke sker, åbne Start-menuen og prøv at udføre søgningen igen).
* NVDA vil forblive tavs, når du taler til Cortana med stemmen.
* NVDA vil nu meddele bekræftelsen, når du tilføjer en påmindelse

## Feedback Hub

* For nyere app-udgivelser, vil NVDA ikke længere meddele feedback
  kategorier to gange.

## Spillinje

* NVDA vil annoncere udseende af vinduet Spillinje. På grund af tekniske
  begrænsninger, kan NVDA ikke fuldt interagere med Spillinje før build
  17723.

## Mail

* When reviewing items in messages list, you can now use table navigation
  commands to review message headers. Note that navigating between rows
  (messages) is not supported.
* Når du skriver en besked, vil @omtale forslag indikeres med lyd, når de
  vises.

## Kort

* NVDA spiller placeringsbip for kortlokationer.
* Når du bruger side street view, og hvis indstillingen "Brug tastaturet" er
  aktiveret, annoncere NVDA gadenavne, som du bruger piletasterne til at
  navigere kortet.

## Microsoft Edge

* Meddelelser som fil-downloads og forskellige websideindberetninger, samt
  tilgængeligheden af læsevisning er (hvis du bruger Version 1709 og senere)
  annonceret.
* Text auto-complete will be tracked and announced in address omnibar.

## Moderne tastatur

Note: most features below are now part of NVDA 2018.3.

* Support for Emoji input panel in Version 1709 (Fall Creators Update) and
  later, including the redesigned panel in Version 1809 (build 17661 and
  later) and changes made in 19H1 (build 18262). For best experience when
  reading emojis, use Windows OneCore speech synthesizer.
* Understøttelse af hardware tastatur input forslag i Version 1803 (April
  2018 opdatering) og senere.
* In post-1709 builds, NVDA will announce the first selected emoji when
  emoji panel opens. This is more noticeable in build 18262 and later where
  emoji panel may open to last browsed category, such as displaying skin
  tone modifier when opened to People category.
* Support for announcing cloud clipboard items in Version 1809 (build 17666
  and later).
* Reduceret unødvendige udtale, når du arbejder med det moderne tastatur og
  dens funktioner. Disse omfatter ikke længere annonceringer "Microsoft
  kandidat UI", når du åbner hardware tastatur input forslag og NVDA
  forbliver tavse, når visse touch-tastaturkommandoer omfatter change name
  event på nogle systemer.
* NVDA will no longer play error tones or do nothing when closing emoji
  panel in more recent Insider Preview builds.

## Personer

* Når du søger efter kontakter, vil forslag blive annoncerede, særligt hvis
  du kører de seneste app-udgivelser.

## indstillinger

* Certain information such as Windows Update progress is reported
  automatically, including Storage sense/disk cleanup widget.
* Værdier på behandlingslinjer og andre oplysninger er ikke længere
  annonceret to gange.
* Indstillingsgrupper genkendes, når du bruger objektnavigation til at
  navigere mellem kontrolelementer.
* For some combo boxes and radio buttons, NVDA will no longer fail to
  recognize labels and/or announce value changes.
* Bip for behandlingslinjer for lydstyrke høres nu ikke længere i version
  1803 og nyere.
* Flere meddelelser om Windows Update status er annonceret, især hvis
  Windows Update fejler.

## Skype

Note: the below entries won't work properly in Skype 14 universal app.

* Indtastningsindikator annonceres nu igen, ligesom Skype for Desktop
* Kommandoer til at læse seneste meddelelser (navnlig Ctrl+1 til 0,
  understøttes nu i Skype for UWP.
* Du kan trykke på Alt + nummer rækken til at finde og flytte til samtaler
  (1), kontakter liste (2), bots (3) og chat-editfeltet hvis synlige
  (4). Bemærk, at disse kommandoer vil fungere korrekt, hvis
  Skype-opdateringen frigivet i marts 2017 er installeret.
* NVDA vil ikke længere meddele "Skype besked", når du gennemgår meddelelser
  i de fleste tilfælde.
* Fra listen over beskeder, vil et tryk på NVDA+D på et meddelelseselement
  tillade NVDA at annoncere detaljerede oplysninger om en besked såsom
  kanaltype, sendte dato og tid, osv.

## Store

* Efter kontrol for app opdateringer, app navne i listen af apps der skal
  opdateres er korrekt navngivet.
* Når du henter indhold som apps og film, vil NVDA annoncere produktnavn og
  fremskridt af tilsvarende handling.

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
