# Vigtige forbedringer til Windows apps (Windows App Essentials) #

* Authors: Joseph Lee, Derek Riemer and others
* Download [stabil version][1]
* Download [udviklingsversion][2]
* NVDA compatibility: 2021.3 and later

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
  suggestions/clipboard history/modern input method editors)
* Notepad (Windows 11)
* Personer
* Indstillinger (systemindstillinger, Windows+I)
* Vejr
* Diverse moduler til kontrolelementer som Start Menu-felter.

Bemærkninger:

* This add-on requires Windows 10 21H1 (build 19043) or later and is
  compatible with Windows 11.
* Selvom installation er mulig, understøtter denne tilføjelse ikke Windows
  Enterprise LTSC (Long-Term Servicing Channel) og Windows
  Server-udgivelser.
* Not all features from Windows Insider Preview builds will be supported.
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
* For best experience with apps that embed web technologies and content such
  as Start menu and its context menu, enable "Automatic focus mode for focus
  changes" setting from NVDA's browse mode settings panel.

For en liste over ændringer, der er fremstillet mellem hver udgivelse af
tilføjelsen, henvises til [ændringslog for tilføjelsen][3].

## Generelt

* In addition to UIA event handlers provided by NVDA, the following UIA
  events and properties are recognized: drag complete, drag drop effect,
  drop target dropped. With NVDA's log level set to debug, these events will
  be tracked and logged.
* Når åbning, lukning, ændring af rækkefølge (Windows 11) eller Skift mellem
  virtuelle skrivebord forekommer, vil NVDA annoncere det aktuelle navn for
  det virtuelle skrivebord (f.eks. "Skrivebord 2").
* When arranging pinned entries (tiles in Windows 10) in Start menu or
  Action Center quick actions with Alt+Shift+arrow keys, NVDA will announce
  information on dragged items or new position of the dragged item.
* Meddelelser, som ændringer i lydstyrke/lysstyrke i Stifinder og
  appopdateringsmeddelelser fra Microsoft Store, kan deaktiveres ved at
  deaktivere rapportering af meddelelserne i NVDAs
  objektpræsentationsindstillinger.
* In Windows 11 Insider Preview builds, microphone mute toggle status
  (Windows+Alt+K) is announced from everywhere.

## Lommeregner

* NVDA annoncerer ikke længere en meddelelse om grafregnerens skærmbillede
  to gange.
* In Windows 10, history and memory list items are properly labeled. This is
  now part of NVDA 2022.1.
* NVDA will now announce calculator display content when performing
  scientific mode commands such as trigonometry operations.

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

Dette inkluderer emoji-panelet, historik for udklipsholderen, diktering,
forslag i forhold til hardwareinput og moderne Input Methodf Editor for
visse sprog. Når du ser emojier, skal du for at få den bedste oplevelse
aktivere Unicode Consortium-indstillingen fra NvDAs taleindstillinger og
indstille tegnsætningsniveauet til "nogle" eller højere. Når du skal
indstille fra historikken i Windows 10, skal du bruge mellemrumstasten i
stedet for enter. NVDA understøtter også det opdaterede inputoplevelsespanel
i Windows 11.

* In Windows 10, when an emoji group (including kaomoji and symbols group)
  is selected, NVDA will no longer move navigator object to certain emojis.
* Understøtter nu opdateret input-oplevelsespanel (kombineret emoji-panel og
  udklipsholderhistorik) i Windows 11.
* In Windows 11, it is again possible to use the arrow keys to review emojis
  when emoji panel opens. This is now part of NVDA 2022.1.
* In Windows 11 clipboard history, browse mode will be turned off by
  default, designed to let NVDA announce clipboard history entry menu items.

## Notepad

This refers to Windows 11 Notepad version 11 or later.

* NVDA will announce status items such as line and column information when
  report status bar command (NVDA+End in desktop layout, NvDA+Shift+End in
  laptop layout) is performed.
* NVDA will no longer announce entered text when pressing Enter key from the
  document.

## Personer

* Når du søger efter kontakter, vil forslag blive annoncerede, særligt hvis
  du kører de seneste app-udgivelser.

## indstillinger

* Bemærkelsesværdige kontroletiketter set i visse Windows-installationer er
  blevet løst.
* NVDA will announce the name of the optional quality update control if
  present (download and install now link in Windows 10, download button in
  Windows 11).
* In Windows 11, breadcrumb bar items are properly recognized.

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
