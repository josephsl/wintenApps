# Windows App Essentials #

* Authors: Joseph Lee, Derek Riemer and others
* Stiahnuť [stabilnú verziu][1]
* Stiahnuť [vývojovú verziu][2]
* NVDA compatibility: 2022.2 and later

Note: Originally called Windows 10 App Essentials, it was renamed to Windows
App Essentials in 2021 to support Windows 10 and future releases such as
Windows 11. Parts of this add-on will still refer to the original add-on
name.

This add-on is a collection of app modules for various modern Windows apps,
as well as enhancements and fixes for certain controls found in Windows 10
and later.

Zahrnuté sú nasledujúce moduly (podrobný popis nájdete nižšie):

* Cortana
* Mapy
* Modern keyboard (emoji panel/dictation/voice typing/hardware input
  suggestions/clipboard history/Suggested Actions/modern input method
  editors)
* Ľudia
* Nastavenia (systémové nastavenia, Win+I)
* Voice access (Windows 11 22H2)
* Počasie
* Miscellaneous modules for controls such as Start Menu tiles

Poznámky:

* This add-on requires Windows 10 21H2 (build 19044), 11 21H2 (build 22000),
  or later releases.
* Although installation is possible, this add-on does not support Windows
  Enterprise LTSC (Long-Term Servicing Channel) and Windows Server releases.
* If Add-on Updater 22.08 or later is installed and background add-on
  updates is enabled, Windows App Essentials will not install at all on
  unsupported Windows releases.
* Not all features from Windows Insider Preview builds will be supported.
* Niektoré doplnkové funkcie sú alebo časom budú súčasťou NVDA.
* For entries not listed below, you can assume that features are part of
  NVDA, no longer applicable as the add-on does not support unsupported
  Windows releases such as old Windows 10 versions, or changes were made to
  Windows, apps, and NVDA that makes entries no longer applicable.
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
  opens.

## Cortana

* Väčšinou sú oznamované textové odpovede z Cortany.
* NVDA nevyrušuje, keď komunikujete s Cortanou.

## Mapy

* NVDA zvukom indikuje polohu na mape.

## Moderná klávesnica

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
* In Windows 11 clipboard history, browse mode will be turned off by
  default, designed to let NVDA announce clipboard history entry menu items.
* In Windows 11 22H2 Moment 1 and later, NVDA will announce suggested
  actions when compatible data such as phone numbers is copied to the
  clipboard.

## Ľudia

* When searching for contacts, first suggestion will be announced.

## Nastavenia

* NVDA will announce the name of the optional quality update control if
  present (download and install now link in Windows 10, download button in
  Windows 11).
* In Windows 11, breadcrumb bar items are properly recognized.
* In Windows 10 and 11 22H2 and later, NVDA will interupt speech and report
  updates to Windows Update status as download and install progresses. This
  may result in speech interruption when navigating Settings app while
  updates are being downloaded and installed. If using Windows 11 22H2 and
  later, if selective UIA event registration is on, you must move focus to
  updates list as soon as they appear so NVDA can announce update progress.

## Voice access

This refers to Voice access feature introduced in Windows 11 22H2.

* NVDA will announce microphone status when toggling microphone from Voice
  access interface.

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
