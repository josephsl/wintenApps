# Vigtige forbedringer til Windows apps (Windows App Essentials) #

* Forfattere: Joseph Lee, Derek Riemer og andre
* Download [stabil version][1]
* Download [udviklingsversion][2]
* NVDA compatibility: 2022.3 and later

Bemærk: Denne tilføjelse hed Windows 10 App Essentials, men er blevet omdøbt
til Windows App Essentials i 2021 for at understøtte Windows 10 og
fremtidige udgivelser som Windows 11. Dele af dette tilføjelsesprogram vil
stadig henvise til det originale navn for tilføjelsen.

Denne tilføjelse er en samling af app-moduler til forskellige Windows-apps,
samt forbedringer og rettelser for visse windows 10 kontrolelementer.

Følgende app moduler eller støttemoduler for nogle apps er inkluderet (Se
hver appsektion for detaljer om, hvad der er inkluderet):

* Cortana
* Kort
* Moderne tastatur (Emoji-panel, diktering, stemmeskrivning, forslag til
  hardwareinput, udklipshistorik og Editor til inputmetode)
* Indstillinger (systemindstillinger, Windows+I)
* Stemmeadgang (Windows 11 22H2)
* Vejr
* Diverse moduler til kontrolelementer og funktioner som annoncering af
  virtuelle skriveborde.

Bemærkninger:

* Denne tilføjelse kræver Windows 10 21H2 (build 19044), 11 21H2 (build
  22000) eller nyere udgivelser.
* Varigheden af understøttelse af funktionsopdateringer er bundet til
  varigheden af forbrugersupport (Home, Pro, Pro Education, Pro for
  Workstations-udgaver), og tilføjelsen kan afslutte understøttelsen af en
  funktionsopdatering, før forbrugersupporten ophører. Se
  aka.ms/WindowsTargetVersioninfo for mere information og supportdatoer.
* Selvom installation er mulig, understøtter denne tilføjelse ikke Windows
  Enterprise LTSC (Long-Term Servicing Channel) og Windows
  Server-udgivelser.
* Hvis Opdateringsværktøj til Tilføjelsespakker er installeret, og
  opdatering af tilføjelser i baggrunden er aktiveret, installeres Vigtige
  Forbedringer til Windows Apps slet ikke på ikke-understøttede
  Windows-udgivelser.
* Ikke alle funktioner fra Windows Insider Preview-builds vil blive
  understøttet. Dette er yderligere tilfældet for funktioner introduceret i
  en undergruppe af Windows Insiders i udviklerkanalen. For betakanaler er
  kun den seneste build (22623) understøttet.
* Nogle funktioner tilføjelsespakken indeholder er eller bliver en del af
  NVDA skærmlæser.
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
  UIA-hændelser og egenskaber blive genkendt: drag start/cancel/complete
  (genkendt som state change event), drag drop effect, drag item is grabbed,
  drop target effect. Disse hændelser er nu en del af NVDA 2022.4.
* Når åbning, lukning eller Skift mellem virtuelle skrivebord forekommer,
  vil NVDA annoncere det aktuelle navn for det virtuelle skrivebord
  (f.eks. "Skrivebord 2").
* Når du arrangerer fastgjorte elementer (fliser i Windows 10) på
  start-menuen eller hurtige handlinger i Handlingscenter med
  Alt+Shift+piletasterne, vil NVDA oplyse informationer om emner, når disse
  flyttes. Dette er nu en del af NVDA 2022.4.
* I Windows 11 vil NVDA annoncere søgehøjdepunkter i Start-menuen, når den
  åbnes. Dette er nu en del af NVDA 2023.1.
* In Windows 11 22H2 Moment 2, redesigned system tray overflow area can be
  detected properly when using mouse and/or touch interaction.

## Cortana

* Tekstlige svar fra Cortana annonceres i de fleste tilfælde.
* NVDA vil forblive tavs, når du taler til Cortana med stemmen.

## Kort

* NVDA spiller placeringsbip for kortlokationer.
* NVDA will no longer interupt speech when focused on items other than the
  map control in some cases.

## Moderne tastatur

Dette inkluderer emoji-panelet, historik for udklipsholderen, diktering,
forslag i forhold til hardwareinput og moderne Input Methodf Editor for
visse sprog. Når du ser emojier, skal du for at få den bedste oplevelse
aktivere Unicode Consortium-indstillingen fra NvDAs taleindstillinger og
indstille tegnsætningsniveauet til "nogle" eller højere. Når du skal
indstille fra historikken i Windows 10, skal du bruge mellemrumstasten i
stedet for enter.

* Når en emoji-gruppe (inklusive kaomoji og symbolgrupper er valgt i Windows
  10, vil NVDA ikke længere flytte navigatorobjektet til bestemte emoji.
* I Windows 11 udklipsholderhistorik er gennemsynstilstand slået fra som
  standard, således NVDA kan annoncere menupunkter i
  udklipsholderhistorikken.
* I Windows 11 22H2 Moment 1 og senere vil NVDA annoncere foreslåede
  handlinger, når kompatible data såsom telefonnumre kopieres til
  udklipsholderen.

## indstillinger

* NVDA vil annoncere navnet på den valgfrie kvalitetsopdateringskontrol,
  hvis den findes (download og installer nu-link i Windows 10, download-knap
  i Windows 11).
* I Windows 11 genkendes brødkrumme-elementer korrekt.
* I Windows 10 og 11 22H2 og nyere vil NVDA afbryde talen og oplyse status
  for opdateringer til Windows Update, efterhånden som download og
  installation skrider frem. Dette kan resultere i afbrydelse af talen, når
  du navigerer i appen Indstillinger, mens opdateringer downloades og
  installeres. Hvis du bruger Windows 11 22H2 og nyere med indstillingen
  "Registrer hændelser fra UI Automation samt egenskabsændringer" slået til,
  skal du flytte fokus til listen opdateringer, så NVDA kan oplyse status
  for opdateringerne.

## Stemmeadgang

Dette henviser til stemmeadgangsfunktionen introduceret i Windows 11 22H2.

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
