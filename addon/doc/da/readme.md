# Vigtige forbedringer til Windows apps (Windows App Essentials) #

* Forfattere: Joseph Lee, Derek Riemer og andre
* Download [stabil version][1]
* Download [udviklingsversion][2]
* NVDA compatibility: 2022.2 and later

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
* Modern keyboard (emoji panel/dictation/voice typing/hardware input
  suggestions/clipboard history/Suggested Actions/modern input method
  editors)
* Personer
* Indstillinger (systemindstillinger, Windows+I)
* Voice access (Windows 11 22H2)
* Vejr
* Diverse moduler til kontrolelementer som Start Menu-felter.

Bemærkninger:

* This add-on requires Windows 10 21H2 (build 19044), 11 21H2 (build 22000),
  or later releases.
* Feature update support duration is tied to consumer support duration
  (Home, Pro, Pro Education, Pro for Workstations editions) and the add-on
  may end support for a feature update prior to end of consumer support. See
  aka.ms/WindowsTargetVersioninfo for more information and support dates.
* Selvom installation er mulig, understøtter denne tilføjelse ikke Windows
  Enterprise LTSC (Long-Term Servicing Channel) og Windows
  Server-udgivelser.
* If Add-on Updater is installed and background add-on updates is enabled,
  Windows App Essentials will not install at all on unsupported Windows
  releases.
* Not all features from Windows Insider Preview builds will be supported,
  more so for features introduced to a subset of Windows Insiders in dev
  channel.
* Nogle funktioner tilføjelsespakken indeholder er eller bliver en del af
  NVDA skærmlæser.
* Some apps support compact overlay mode (always on top in Calculator, for
  example), and this mode will not work properly with the portable version
  of NVDA.
* For at få den bedste oplevelse med apps, der integrerer webteknologier og
  indhold som f.eks. Start-menuen og dens kontekstmenu, skal du aktivere
  indstillingen "Automatisk fokustilstand ved ændring af fokus" fra NVDAs
  indstillingspanel under "Gennemsynstilstand".

For en liste over ændringer, der er fremstillet mellem hver udgivelse af
tilføjelsen, henvises til [ændringslog for tilføjelsen][3].

## Generelt

* In addition to UIA event handlers provided by NVDA, the following UIA
  events and properties are recognized: drag start/cancel/complete
  (recognized as state change event), drag drop effect, drag item is
  grabbed, drop target effect.
* When opening, closing, or switching between virtual desktops, NVDA will
  announce active virtual desktop name (desktop 2, for example).
* When dragging and dropping items such as arranging pinned entries (tiles
  in Windows 10) in Start menu or Action Center quick actions with
  Alt+Shift+arrow keys, NVDA will announce "dragging" and/or drag and drop
  effects before and while dragging items, respectively. This is now part of
  NVDA 2022.4.
* Announcements such as volume/brightness/microphone mute (Windows 11 22H2
  and later) changes in File Explorer and app update notifications from
  Microsoft Store can be suppressed by turning off Report Notifications in
  NVDA's object presentation settings.
* In Windows 11, NVDA will announce search highlights in Start menu when it
  opens. This is now part of NVDA 2023.1.

## Cortana

* Tekstlige svar fra Cortana annonceres i de fleste tilfælde.
* NVDA vil forblive tavs, når du taler til Cortana med stemmen.

## Kort

* NVDA spiller placeringsbip for kortlokationer.

## Moderne tastatur

This includes emoji panel, clipboard history, dictation/voice typing,
hardware input suggestions, suggested actions, and modern input method
editors for certain languages across Windows 10 and 11. When viewing emojis,
for best experience, enable Unicode Consortium setting from NVDA's speech
settings and set symbol level to "some" or higher. When pasting from
clipboard history in Windows 10, press Space key instead of Enter key to
paste the selected item.

* In Windows 10 emoji panel, when an emoji group (including kaomoji and
  symbols group) is selected, NVDA will no longer move navigator object to
  certain emojis.
* I Windows 11 udklipsholderhistorik er gennemsynstilstand slået fra som
  standard, således NVDA kan annoncere menupunkter i
  udklipsholderhistorikken.
* In Windows 11 22H2 Moment 1 and later, NVDA will announce suggested
  actions when compatible data such as phone numbers is copied to the
  clipboard.

## Personer

* When searching for contacts, first suggestion will be announced.

## indstillinger

* NVDA vil annoncere navnet på den valgfrie kvalitetsopdateringskontrol,
  hvis den findes (download og installer nu-link i Windows 10, download-knap
  i Windows 11).
* I Windows 11 genkendes brødkrumme-elementer korrekt.
* In Windows 10 and 11 22H2 and later, NVDA will interupt speech and report
  updates to Windows Update status as download and install progresses. This
  may result in speech interruption when navigating Settings app while
  updates are being downloaded and installed. If using Windows 11 22H2 and
  later, if selective UIA event registration is on, you must move focus to
  updates list as soon as they appear so NVDA can announce update progress.

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
