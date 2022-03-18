# Windows App Essentials #

* Authors: Joseph Lee, Derek Riemer and others
* Stiahnuť [stabilnú verziu][1]
* Stiahnuť [vývojovú verziu][2]
* NVDA compatibility: 2021.3 and later

Note: Originally called Windows 10 App Essentials, it was renamed to Windows
App Essentials in 2021 to support Windows 10 and future releases such as
Windows 11. Parts of this add-on will still refer to the original add-on
name.

This add-on is a collection of app modules for various modern Windows apps,
as well as enhancements and fixes for certain controls found in Windows 10
and later.

Zahrnuté sú nasledujúce moduly (podrobný popis nájdete nižšie):

* Kalkulačka
* Cortana
* Pošta
* Mapy
* Microsoft Solitaire Collection
* Modern keyboard (emoji panel/dictation/voice typing/hardware input
  suggestions/clipboard history/modern input method editors)
* Notepad (Windows 11)
* Ľudia
* Nastavenia (systémové nastavenia, Win+I)
* Počasie
* Miscellaneous modules for controls such as Start Menu tiles

Poznámky:

* This add-on requires Windows 10 21H1 (build 19043) or later and is
  compatible with Windows 11.
* Although installation is possible, this add-on does not support Windows
  Enterprise LTSC (Long-Term Servicing Channel) and Windows Server releases.
* Not all features from Windows Insider Preview builds will be supported.
* Niektoré doplnkové funkcie sú alebo časom budú súčasťou NVDA.
* For entries not listed below, you can assume that features are part of
  NVDA, no longer applicable as the add-on does not support unsupported
  Windows releases such as old Windows 10 versions, or changes were made to
  Windows and apps that makes entries no longer applicable.
* Some apps support compact overlay mode (always on top in Calculator, for
  example), and this mode will not work properly with portable version of
  NVDA.
* For best experience with apps that embed web technologies and content such
  as Start menu and its context menu, enable "Automatic focus mode for focus
  changes" setting from NVDA's browse mode settings panel.

Podrobné úpravy medzi jednotlivými verziami nájdete v [Zozname zmien
(anglicky)][3].

## Všeobecné

* In addition to UIA event handlers provided by NVDA, the following UIA
  events and properties are recognized: drag complete, drag drop effect,
  drop target dropped. With NVDA's log level set to debug, these events will
  be tracked and logged.
* When opening, closing, reordering (Windows 11), or switching between
  virtual desktops, NVDA will announce active virtual desktop name (desktop
  2, for example).
* When arranging pinned entries (tiles in Windows 10) in Start menu or
  Action Center quick actions with Alt+Shift+arrow keys, NVDA will announce
  information on dragged items or new position of the dragged item.
* Oznamovanie zmeny hlasitosti a jasu v okne pracovnej plochy a iných oknách
  Explorera a tiež upozornení z obchodu Microsoft store je možné pozastaviť
  odčiarknutím možnosti Oznamovať notifikácie v nastaveniach > prezentácia
  objektov.
* In Windows 11 Insider Preview builds, microphone mute toggle status
  (Windows+Alt+K) is announced from everywhere.

## Kalkulačka

* NVDA will no longer announce graphing calculator screen message twice.
* In Windows 10, history and memory list items are properly labeled. This is
  now part of NVDA 2022.1.
* NVDA will now announce calculator display content when performing
  scientific mode commands such as trigonometry operations.

## Cortana

* Väčšinou sú oznamované textové odpovede z Cortany.
* NVDA nevyrušuje, keď komunikujete s Cortanou.

## Pošta

* Pri prezeraní položiek v zozname správ môžete teraz použiť príkazy
  navigácie v tabuľke na kontrolu hlavičiek správ. Upozorňujeme, že
  navigácia medzi riadkami (správami) nie je podporovaná.

## Mapy

* NVDA zvukom indikuje polohu na mape.

## Microsoft Solitaire Collection

* NVDA oznamuje karty a kombinácie kariet.

## Moderná klávesnica

This includes emoji panel, clipboard history, dictation/voice typing,
hardware input suggestions, and modern input method editors for certain
languages. When viewing emojis, for best experience, enable Unicode
Consortium setting from NVDA's speech settings and set symbol level to
"some" or higher. When pasting from clipboard history in Windows 10, press
Space key instead of Enter key to paste the selected item. NVDA also
supports updated input experience panel in Windows 11.

* In Windows 10, when an emoji group (including kaomoji and symbols group)
  is selected, NVDA will no longer move navigator object to certain emojis.
* Added support for updated input experience panel (combined emoji panel and
  clipboard history) in Windows 11.
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

## Ľudia

* Pri hľadaní kontaktov bude oznámený prvý návrh, najmä ak používate
  najnovšie vydania aplikácie.

## Nastavenia

* Odd control labels seen in certain Windows installations has been
  corrected.
* NVDA will announce the name of the optional quality update control if
  present (download and install now link in Windows 10, download button in
  Windows 11).
* In Windows 11, breadcrumb bar items are properly recognized.

## Počasie

* Správne sú rozpoznané záložky ako mapy a počasie (opravil Derek Riemer).
* pri čítaní predpovede sa môžete medzi položkami pohybovať pomocou ľavej a
  pravej šípky. Na čítanie jednotlivých položiek použite šípky nahor a
  nadol. Napríklad pri stlačení pravej šípky sa môže zobraziť správa
  "Pondelok: 15 stupňov, polojasno, ...". Po stlačení šípky nadol sa zobrazí
  "pondelok". Po opätovnom stlačení sa načíta ďalšia položka (napríklad
  teplota). V súčasnosti to funguje na denné a hodinové predpovede.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
