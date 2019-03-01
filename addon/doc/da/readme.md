# Windows 10 App Essentials (Vigtige forbedringer til Windows 10-apps) #

* Forfattere: Joseph Lee, Derek Riemer og andre brugere af Windows 10
* Download [stabil version][1]
* Download [udviklingsversion][2]
* NVDA-kompatibilitet: 2018.3 til 2019.1

Denne tilføjelse er en samling af app-moduler til forskellige Windows 10
apps, samt forbedringer og rettelser for visse windows 10 kontrolelementer.

Følgende app moduler eller støttemoduler for nogle apps er inkluderet (Se
hver appsektion for detaljer om, hvad der er inkluderet):

* Handlingscenter
* Alarmer og ur.
* Kalender
* Lommeregner (moderne).
* Cortana
* Feedback Hub
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

* Denne tilføjelse kræver Windows 10 Version 1803 (build 17134) eller senere
  og NVDA 2018.3 eller nyere. For de bedste resultater skal du bruge
  tilføjelsen med den nyeste Windows 10-stabile udgivelse (build 17763) og
  den seneste stabile version af NVDA.
* Nogle funktioner tilføjelsespakken indeholder er eller bliver en del af
  NVDA skærmlæser.
* For emner, der ikke er anført nedenfor, kan du antage, at funktionerne er
  en del af NVDA, ikke længere gældende som tilføjelsesprogrammet ikke
  understøtter ældre Windows 10 udgivelser, eller ændringer til apps, der
  gør disse emner ugyldige.

For en liste over ændringer, der er fremstillet mellem hver udgivelse af
tilføjelsen, henvises til [ændringslog for tilføjelsen][3].

## Generelt

* NVDA will no longer play error tones or do nothing if this add-on becomes
  active from Windows 7 and 8.1.
* Undermenupunkter er korrekt genkendt i forskellige apps, herunder
  kontekstmenu til Start-menufliser og Microsoft Edge-appmenuen (Redstone
  5).
* In addition to dialogs recognized by NVDA, more dialogs are now recognized
  as proper dialogs and reported as such, including Insider Preview dialog
  (settings app).
* NVDA can announce suggestion count when performing a search in majority of
  cases. This option is controlled by "Report object position information"
  in Object presentation panel found in NVDA settings.
* I visse kontekstmenuer (f.eks. i Microsoft Edge), er positionssoplysninger
  (f.eks. 1 af 2) ikke længere annonceret.
* De følgende UIA begivenheder er anerkendt: active text position change,
  controller for, drag start, drag cancel, drag complete, element selected,
  live region change, notification, system alert, tooltip opened, window
  opened. Med NVDA indstillet til at køre med logføring aktiveret, spores
  disse begivenheder, og for UIA notification event, vil en fejltone blive
  hørt, hvis notifikationer kommer fra en anden app en den aktuelle.
* Værktøjstips fra Edge og universale apps er genkendte og vil blive
  annonceret.
* Når åbning, lukning, eller Skift mellem virtuelle skrivebord forekommer,
  vil NVDA annoncere nuværende desktop ID (skrivebord 2, for eksempel).
* NVDA vil ikke længere annoncere størrelsen af punkter på startmenuen, når
  du ændrer skærmopløsning eller orientering.
* In build 18323 and later, NVDA will now announce audio volume and
  brightness changes.

## Handlingscenter

* Den hurtige handling til at ændre lysstyrke er nu en knap i stedet for en
  skiftknap.
* Forskellige statusændringer som Fokushjælp og Lysstyrke vil blive
  rapporteret. Denne forbedring vil være en del af NVDA 2019.1.

## Alarmer og ur

* Tidvælgerværdier er nu annonceret, mærkbart, når du flytter fokus til
  vælgekontroller. Dette påvirker også den kontrol, der bliver brugt til at
  vælge, hvornår du vil genstart for at afslutte installationen af
  Windows-opdateringer. Denne forbedring vil være en del af NVDA 2019.1.

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

* Autofuldførelse af tekst vil blive sporet og annonceret i adressse
  omnibar.
* NVDA vil ikke længere afspille lyden for forslag, når du trykker på F11
  for at ændre indstillingen for fuld skærm.

## Moderne tastatur

Note: most features below are now part of NVDA 2018.3 or later.

* Støtte til Emoji inputpanelet i Version 1709 (Fall Creators Update) og
  senere, herunder det redesignet panel i build version 1809 17661 og
  senere, samt ændringer i 19H1 (build 18262). Du vil få den bedste
  oplevelse, når du læser emojis, hvis du benytter talesyntesen Windows
  OneCore. Hvis du benytter 2018.4 eller senere, skal du aktivér
  indstillingen der benytter Unicode Consortium data til emojis via NVDAs
  taleindstillinger. Derefter skal tegnsætningsniveauet indstilles til
  "nogle" eller højere.
* Understøttelse af hardware tastatur input forslag i Version 1803 (April
  2018 opdatering) og senere.
* I versioner af Windows 10 efter 1709 vil NVDA læse den første valgte
  emoji, når emoji-panelet åbnes. Dette er mere mærkbart i version 18262 og
  senere, hvor emoji-panelet åbner til den sidst gennemsete kategori, som
  f.eks. Visning af hudtone, når den åbnes til Personer-kategorien.
* Understøtter annoncering af Cloud Udklipsholder i version 1809 (build
  17666) og senere.
* Reduceret unødvendige udtale, når du arbejder med det moderne tastatur og
  dens funktioner. Disse omfatter ikke længere annonceringer "Microsoft
  kandidat UI", når du åbner hardware tastatur input forslag og NVDA
  forbliver tavse, når visse touch-tastaturkommandoer omfatter change name
  event på nogle systemer.
* NVDA will no longer play error tones or do nothing when closing emoji
  panel in more recent 19H1 Insider Preview builds. This will be part of
  NVDA 2019.1.
* In Version 1809 (October 2018 Update) and later, NVDA will announce search
  results for emojis if possible. This will be part of NVDA 2019.1.

## Personer

* Når du søger efter kontakter, vil forslag blive annoncerede, særligt hvis
  du kører de seneste app-udgivelser.

## indstillinger

* Visse oplysninger såsom fremdskridt af Windows-opdateringer rapporteres
  automatisk, herunder ved brug af Storage sense/disk cleanup widget..
* Værdier på behandlingslinjer og andre oplysninger er ikke længere
  annonceret to gange.
* For nogle combo boxe, vil NVDA ikke længere undlade at rapportere
  etiketter- og- eller annoncere værdiændringer.
* Bip for behandlingslinjer for lydstyrke høres nu ikke længere i version
  1803 og nyere.
* Flere meddelelser om Windows Update status er annonceret, især hvis
  Windows Update fejler.
* NVDA ser ikke længere ud til at gøre ingenting eller afspille fejltoner,
  hvis du bruger objektnavigeringskommandoer under visse omstændigheder.
* Dialogboksen Windows Update-påmindelse genkendes som en korrekt dialog.

## Skype

Bemærk: nedenstående funktioner  virker ikke korrekt i Skype 14 Universal
App.

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
