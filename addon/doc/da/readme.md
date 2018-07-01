# Windows 10 App Essentials (Vigtige forbedringer til Windows 10-apps) #

* Forfattere: Joseph Lee, Derek Riemer og andre brugere af Windows 10
* Download [stabil version][1]
* Download [udviklingsversion][2]

Denne tilføjelse er en samling af app-moduler til forskellige Windows 10
apps, samt forbedringer og rettelser for visse windows 10 kontrolelementer.

Følgende app moduler eller støttemoduler for nogle apps er inkluderet (Se
hver appsektion for detaljer om, hvad der er inkluderet):

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

* Denne tilføjelse kræver Windows 10 Version 1709 (build 16299) eller nyere
  og NVDA 2018.2 eller nyere. For de bedste resultater skal du bruge
  tilføjelsen med den nyeste Windows 10-stabile udgivelse (build 17134) og
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

* I kontesktmenuer, der vises i felterne i menuen start, genkendes
  undermenuer nu korrekt.
* Visse dialogbokse er nu anerkendt som ordentlige dialoger og rapporteret
  som sådan, herunder Insider Preview dialog (indstillinger app).
* NVDA kan annoncere nummeret af forslag, når du udfører en søgning i de
  fleste tilfælde. Denne indstilling styres af "Oplys information om
  objektets placering" i objektet præsentation dialog/panel.
* I visse kontekstmenuer (f.eks. i Microsoft Edge), er positionssoplysninger
  (f.eks. 1 af 2) ikke længere annonceret.
* De følgende UIA begivenheder er anerkendt: active text position change
  (Redstone 5), controller for, drag start, drag cancel, drag complete,
  element selected, live region change, notification, system alert, tooltip
  opened, window opened. Med NVDA indstillet til at køre med logføring
  aktiveret, spores disse begivenheder, og for UIA notification event, en
  fejltone vil blive hørt.
* Tilføjet mulighed for at søge efter tilføjelse opdateringer (automatisk
  eller manuel) via dialogboksen Windows 10 App Essentials fundet i
  NvDA-menuen under Præferencer. Som standard, vil stabil og
  udviklingsversioner kontrollere for nye opdateringer automatisk på et
  ugentligt eller dagligt tidspunkt.
* Nogle apps, live region tekst er annonceret. Dette omfatter advarsler i
  Edge, resultater i Lommeregner m.fl. Bemærk, at dette kan betyde, at nogle
  beskeder gentages i nogle tilfæld.
* Meddelelser fra nyere app-udgivelser o Windows 10 Version 1709 (build
  16299) og senere bliver annonceret.
* Værktøjstips fra Edge og universale apps er genkendte og vil blive
  annonceret.
* I Build 17627 og senere, når du åbner et nyt sæt af faner (CTRL + Windows
  + T), vil NVDA annoncerer søgeresultater, når du søger efter elementer i
  det integrerede Cortana vindue.
* Når du skifter mellem Sæt af faner, annoncerer NvDA navn og position på
  fanen, du skifter til.
* Når åbning, lukning, eller Skift mellem virtuelle skrivebord forekommer,
  vil NVDA annoncere nuværende desktop ID (skrivebord 2, for eksempel).
* NVDA vil ikke længere annoncere størrelsen af punkter på startmenuen, når
  du ændrer skærmopløsning eller orientering.

## Alarmer og ur

* Tidvælgerværdier er nu annonceret, mærkbart, når du flytter fokus til
  vælgekontroller. Dette påvirker også den kontrol, der bliver brugt til at
  vælge, hvornår du vil genstart for at afslutte installationen af
  Windows-opdateringer.

## Lommeregner

* Når enter eller Esc trykkes, vil NVDA nu annoncerer resultatet
* For beregninger som enhedsberegninger og valutaberegninger, vil NVDA
  annoncere resultater så snart beregningerne er indtastet.

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
  begrænsninger, kan NVDA ikke fuldt interagere med Spillinje.

## Mail

* Når du gennemgår emner i listen meddelelser, kan du nu bruge
  tabelnavigationskommandoer til at gennemse brevhovederne.
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

## Moderne tastatur

* Støtte til Emoji inputpanelet i Version 1709 (Fall Creators Update) og
  senere, herunder det redesignet panel i build 17661 og senere. Du vil få
  den bedste oplevelse, når du læser emojis, hvis du benytter talesyntesen
  Windows OneCore.
* Understøttelse af hardware tastatur input forslag i Version 1803 (April
  2018 opdatering) og senere.
* I builds efter 1709, vil NVDA annoncere den første valgte emoji når
  emoji-panelet åbner.
* Understøtter annoncering af Cloud Udklipsholder i build 17666 (Redstone 5)
  og senere.
* Reduceret unødvendige udtale, når du arbejder med det moderne tastatur og
  dens funktioner. Disse omfatter ikke længere annonceringer "Microsoft
  kandidat UI", når du åbner hardware tastatur input forslag og NVDA
  forbliver tavse, når visse touch-tastaturkommandoer omfatter change name
  event på nogle systemer.

## Personer

* Når du søger efter kontakter, afspilles en lyd, hvis der er
  søgeresultater.

## indstillinger

* Visse oplysninger såsom fremdskridt af Windows-opdateringer rapporteres
  automatisk.
* Værdier på behandlingslinjer og andre oplysninger er ikke længere
  annonceret to gange.
* Indstillingsgrupper genkendes, når du bruger objektnavigation til at
  navigere mellem kontrolelementer.
* For nogle combo boxe, vil NVDA ikke længere undlade at rapportere
  etiketter- og- eller annoncere værdiændringer.
* Bip for behandlingslinjer for lydstyrke høres nu ikke længere i version
  1803 og nyere.
* Flere meddelelser om Windows Update status er annonceret, især hvis
  Windows Update fejler.

## Skype

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
