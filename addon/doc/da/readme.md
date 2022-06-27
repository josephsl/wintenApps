# Vigtige forbedringer til Windows apps (Windows App Essentials) #

* Forfattere: Joseph Lee, Derek Riemer og andre
* Download [stabil version][1]
* Download [udviklingsversion][2]
* NVDA-kompatibilitet: 2021.3 og nyere

Bemærk: Denne tilføjelse hed Windows 10 App Essentials, men er blevet omdøbt
til Windows App Essentials i 2021 for at understøtte Windows 10 og
fremtidige udgivelser som Windows 11. Dele af dette tilføjelsesprogram vil
stadig henvise til det originale navn for tilføjelsen.

Denne tilføjelse er en samling af app-moduler til forskellige Windows-apps,
samt forbedringer og rettelser for visse windows 10 kontrolelementer.

Følgende app moduler eller støttemoduler for nogle apps er inkluderet (Se
hver appsektion for detaljer om, hvad der er inkluderet):

* Lommeregner
* Cortana
* Mail
* Kort
* Microsoft Kabale Samling
* Modern keyboard (emoji panel/dictation/voice typing/hardware input
  suggestions/clipboard history/Suggested Actions (preview)/modern input
  method editors)
* Notesblok (Windows 11)
* Personer
* Indstillinger (systemindstillinger, Windows+I)
* Voice access (Windows 11 22H2)
* Vejr
* Diverse moduler til kontrolelementer som Start Menu-felter.

Bemærkninger:

* Denne tilføjelse kræver Windows 10 21H1 (build 19043), Windows 11 21H2
  (build 22000) eller nyere.
* Selvom installation er mulig, understøtter denne tilføjelse ikke Windows
  Enterprise LTSC (Long-Term Servicing Channel) og Windows
  Server-udgivelser.
* Ikke alle funktioner fra Windows Insider Preview-builds vil blive
  understøttet.
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
* For at få den bedste oplevelse med apps, der integrerer webteknologier og
  indhold som f.eks. Start-menuen og dens kontekstmenu, skal du aktivere
  indstillingen "Automatisk fokustilstand ved ændring af fokus" fra NVDAs
  indstillingspanel under "Gennemsynstilstand".

For en liste over ændringer, der er fremstillet mellem hver udgivelse af
tilføjelsen, henvises til [ændringslog for tilføjelsen][3].

## Generelt

* Udover UIA event handlers, der tilbydes af NVDA, vil følgende
  UIA-hændelser og egenskaber blive genkendt: drag complete, drag drop
  effect, drop target dropped. Hvis NVDAs logningsniveau indstilles til
  "Fejlfinding", vil disse hændelser blive sporet og logført.
* Når åbning, lukning, ændring af rækkefølge (Windows 11) eller Skift mellem
  virtuelle skrivebord forekommer, vil NVDA annoncere det aktuelle navn for
  det virtuelle skrivebord (f.eks. "Skrivebord 2").
* Når du arrangerer fastgjorte elementer (fliser i Windows 10) på
  start-menuen eller hurtige handlinger i Handlingscenter med
  Alt+Shift+piletasterne, vil NVDA oplyse informationer om emner, når disse
  flyttes.
* Meddelelser, som ændringer i lydstyrke/lysstyrke i Stifinder og
  appopdateringsmeddelelser fra Microsoft Store, kan deaktiveres ved at
  deaktivere rapportering af meddelelserne i NVDAs
  objektpræsentationsindstillinger.
* In Windows 11 22H2 and later, microphone mute toggle status
  (Windows+Alt+K) is announced from everywhere.
* NVDA vil ikke længere gentage tekstoutput i Windows Terminal 1.12.10733 og
  nyere. Dette er nu en del af NVDA 2022.1.
* NVDA vil igen annoncere søgeresultatdetaljer i Start-menuen. Dette er nu
  en del af NVDA 2022.2.
* In Windows 11, Taskbar items and other shell user interface elements can
  be detected properly when using mouse and/or touch interaction. This is
  now part of NVDA 2022.2.

## Lommeregner

* I Windows 10 er historik- og hukommelseslisteelementer korrekt
  navngivet. Dette er nu en del af NVDA 2022.1.
* NVDA vil annoncere indholdet af lommeregnerens display, når du udfører
  kommandoer i videnskabelig tilstand, såsom trigonometrioperationer. Dette
  er nu en del af NVDA 2022.2.

## Cortana

* Tekstlige svar fra Cortana annonceres i de fleste tilfælde.
* NVDA vil forblive tavs, når du taler til Cortana med stemmen.

## Mail

* Når du gennemgår emner i meddelelseslisten, kan du nu bruge
  tabelnavigationskommandoer til at gennemgå
  meddelelsesoverskrifter. Bemærk, at navigering mellem rækker (meddelelser)
  ikke understøttes.

## Kort

* NVDA spiller placeringsbip for kortlokationer.

## Microsoft Kabale Samling

* NVDA vil annoncere navnene på kort og kortdæk.

## Moderne tastatur

This includes emoji panel, clipboard history, dictation/voice typing,
hardware input suggestions, suggested actions (preview), and modern input
method editors for certain languages across Windows 10 and 11. When viewing
emojis, for best experience, enable Unicode Consortium setting from NVDA's
speech settings and set symbol level to "some" or higher. When pasting from
clipboard history in Windows 10, press Space key instead of Enter key to
paste the selected item.

* Når en emoji-gruppe (inklusive kaomoji og symbolgrupper er valgt, vil NVDA
  ikke længere flytte navigatorobjektet til bestemte emoji.
* I Windows 11 er det igen muligt at bruge piletasterne til at gennemgå
  listen over emoji, når emoji-panelet åbner. Dette er nu en del af NVDA
  2022.1.
* I Windows 11 udklipsholderhistorik er gennemsynstilstand slået fra som
  standard, således NVDA kan annoncere menupunkter i
  udklipsholderhistorikken.
* In Insider Preview build 25115, NVDA will announce suggested actions when
  compatible data such as phone numbers is copied to the clipboard.

## Notesblok

Dette henviser til Windows 11 Notepad version 11 eller nyere.

* NVDA will announce status items such as line and column information when
  report status bar command (NVDA+End in desktop layout, NvDA+Shift+End in
  laptop layout) is performed. This is now part of NVDA 2022.2.

## Personer

* Når du søger efter kontakter, vil forslag blive annoncerede, særligt hvis
  du kører de seneste app-udgivelser.

## indstillinger

* Bemærkelsesværdige kontroletiketter set i visse Windows-installationer er
  blevet løst.
* NVDA vil annoncere navnet på den valgfrie kvalitetsopdateringskontrol,
  hvis den findes (download og installer nu-link i Windows 10, download-knap
  i Windows 11).
* I Windows 11 genkendes brødkrumme-elementer korrekt.
* I Windows 10 vil NVDA afbryde talen og oplyse status for opdateringer til
  Windows Update, efterhånden som download og installation skrider
  frem. Dette kan resultere i afbrydelse af talen, når du navigerer i appen
  Indstillinger, mens opdateringer downloades og installeres.

## Stemmeadgang

This refers to Voice access feature introduced in Windows 11 22H2.

* NVDA vil annoncere mikrofonstatus, når mikrofonen skiftes fra
  brugergrænsefladen i Stemmeadgang.

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
