# Vigtige forbedringer til Windows apps (Windows App Essentials) #

* Forfattere: Joseph Lee, Derek Riemer og andre
* Download [stabil version][1]
* Download [beta version][2]
* Download [udviklingsversion][3]
* NVDA-kompatibilitet: 2023.1 og nyere

Bemærk: Denne tilføjelse hed Windows 10 App Essentials, men er blevet omdøbt
til Windows App Essentials i 2021 for at understøtte Windows 10 og
fremtidige udgivelser som Windows 11. Dele af dette tilføjelsesprogram vil
stadig henvise til det originale navn for tilføjelsen.

Denne tilføjelse er en samling af app-moduler til forskellige Windows-apps,
samt forbedringer og rettelser for visse windows 10 kontrolelementer.

Følgende app moduler eller støttemoduler for nogle apps er inkluderet (Se
hver appsektion for detaljer om, hvad der er inkluderet):

* Cortana
* Modern keyboard (emoji panel/touch keyboard/dictation/voice
  typing/hardware input suggestions/clipboard history/Suggested
  Actions/modern input method editors)
* Indstillinger (systemindstillinger, Windows+I)
* Stemmeadgang (Windows 11 22H2)
* Vejr
* Diverse moduler til kontrolelementer og funktioner som annoncering af
  virtuelle skriveborde.

Bemærkninger:

* Denne tilføjelse kræver Windows 10 22H2 (build 19045), 11 21H2 (build
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
  more so for features introduced to a subset of Windows Insiders in canary
  and dev channels.
* The add-on may emulate fixes included in Insider Preview builds which are
  subsequently removed, and for these changes, the add-on may remove them in
  future releases.
* Add-on dev channel will include changes including experimental content
  that may or may not be included in beta and stable releases, and beta
  channel will come with changes planned for future stable releases.
* Nogle funktioner tilføjelsespakken indeholder er eller bliver en del af
  NVDA skærmlæser.
* For at få den bedste oplevelse med apps, der integrerer webteknologier og
  indhold som f.eks. Start-menuen og dens kontekstmenu, skal du aktivere
  indstillingen "Automatisk fokustilstand ved ændring af fokus" fra NVDAs
  indstillingspanel under "Gennemsynstilstand".

For en liste over ændringer, der er fremstillet mellem hver udgivelse af
tilføjelsen, henvises til [ændringslog for tilføjelsen][4].

## Generelt

* When opening, closing, or switching between virtual desktops, NVDA will
  announce active virtual desktop name (desktop 2, for example). This is now
  part of NVDA 2023.2.
* Improved Windows 10 and 11 taskbar experience, including announcing
  results of rearranging icons when pressing Alt+Shift+left/right arrow keys
  (Windows 11) and reporting item position when moving through taskbar icons
  (Windows 10 and 11). Note that these are emulated workarounds for features
  introduced and then subsequently removed in Insider Preview builds and may
  be removed from the add-on in the future.
* In aps such as Windows 11 22H2 File Explorer and Notepad where tabbed
  windows are supported, NVDA will announce the name and the position of
  tabs when switching between them. This is now part of NVDA 2023.2.

## Cortana

* Tekstlige svar fra Cortana annonceres i de fleste tilfælde.

## Moderne tastatur

This includes emoji panel, clipboard history, touch keyboard,
dictation/voice typing, hardware input suggestions, suggested actions, and
modern input method editors for certain languages across Windows 10 and
11. When viewing emojis, for best experience, enable Unicode Consortium
setting from NVDA's speech settings and set symbol level to "some" or
higher. When pasting from clipboard history in Windows 10, press Space key
instead of Enter key to paste the selected item.

* In Windows 11 22H2 and later, NVDA will announce suggested actions when
  compatible data such as phone numbers is copied to the clipboard.

## Indstillinger

* NVDA vil annoncere navnet på den valgfrie kvalitetsopdateringskontrol,
  hvis den findes (download og installer nu-link i Windows 10, download-knap
  i Windows 11).
* I Windows 11 genkendes brødkrumme-elementer korrekt.
* NVDA will report updates to Windows Update status as download and install
  progresses. This may result in speech interruption when navigating
  Settings app while updates are being downloaded and installed. If using
  Windows 11 and UIA event registration is set to selective from NVDA
  advanced settings panel, you must move focus to updates list as soon as
  they appear so NVDA can announce update progress.

## Stemmeadgang

Dette henviser til stemmeadgangsfunktionen introduceret i Windows 11 22H2.

* NVDA vil annoncere mikrofonstatus, når mikrofonen skiftes fra
  brugergrænsefladen i Stemmeadgang.

## Vejr

* Faner som "Vejrudsigt" og "Kort" er nu genkendt korrekt som faner (patch
  af Derek Riemer).

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps

[2]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-dev

[4]: https://github.com/josephsl/wintenapps/wiki/w10changelog
