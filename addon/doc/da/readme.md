# Vigtige forbedringer til Windows apps (Windows App Essentials) #

* Forfattere: Joseph Lee, Derek Riemer og andre
* Download [stabil version][1]
* Download [udviklingsversion][2]
* NVDA-kompatibilitet: 2022.4 og nyere

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
* Modern keyboard (emoji panel/touch keyboard/dictation/voice
  typing/hardware input suggestions/clipboard history/Suggested
  Actions/modern input method editors)
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
* Not all features from Windows Insider Preview builds will be supported,
  more so for features introduced to a subset of Windows Insiders in dev
  channel.
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

* Når åbning, lukning eller Skift mellem virtuelle skrivebord forekommer,
  vil NVDA annoncere det aktuelle navn for det virtuelle skrivebord
  (f.eks. "Skrivebord 2").
* I Windows 11 vil NVDA annoncere søgehøjdepunkter i Start-menuen, når den
  åbnes. Dette er nu en del af NVDA 2023.1.
* In Windows 11 22H2 and later, mouse and/or touch interaction can be used
  to interact with redesigned system tray overflow window and Open With
  dialog. This is now part of NVDA 2023.1.
* NVDA will record processor architecture for the current Windows
  installation (x86/32-bit, AMD64, ARM64) when it starts. This is now part
  of NVDA 2023.1.
* Improved Windows 10 and 11 taskbar experience, including announcing
  results of rearranging icons when pressing Alt+Shift+left/right arrow keys
  (Windows 11 prior to build 25267) and reporting item position when moving
  through taskbar icons (Windows 10 and 11 prior to build 25281).
* NVDA will announce empty folder text inside an empty folder in File
  Explorer.
* In aps such as File Explorer and Notepad where tabbed windows are
  supported, NVDA will announce the name and the position of tabs when
  switching between them.

## Cortana

* Tekstlige svar fra Cortana annonceres i de fleste tilfælde.

## Kort

* NVDA spiller placeringsbip for kortlokationer.
* NVDA will no longer interrupt speech when focused on items other than the
  map control in some cases.

## Moderne tastatur

This includes emoji panel, clipboard history, touch keyboard,
dictation/voice typing, hardware input suggestions, suggested actions, and
modern input method editors for certain languages across Windows 10 and
11. When viewing emojis, for best experience, enable Unicode Consortium
setting from NVDA's speech settings and set symbol level to "some" or
higher. When pasting from clipboard history in Windows 10, press Space key
instead of Enter key to paste the selected item.

* Når en emoji-gruppe (inklusive kaomoji og symbolgrupper er valgt i Windows
  10, vil NVDA ikke længere flytte navigatorobjektet til bestemte emoji.
* In Windows 11 clipboard history, browse mode will be turned off by
  default, designed to let NVDA announce clipboard history entry menu
  items. This is now part of NVDA 2023.1.
* In Windows 11 22H2 and later, NVDA will announce suggested actions when
  compatible data such as phone numbers is copied to the clipboard.

## Indstillinger

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

[1]: https://addons.nvda-project.org/files/get.php?file=wintenApps

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
