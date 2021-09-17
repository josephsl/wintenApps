# Windows App Essentials #

* Authors: Joseph Lee, Derek Riemer and others
* Stiahnuť [stabilnú verziu][1]
* Stiahnuť [vývojovú verziu][2]
* NVDA compatibility: 2021.2 and beyond

Note: Originally called Windows 10 App Essentials, it was renamed to Windows
App Essentials in 2021 to support Windows 10 and future releases such as
Windows 11. Parts of this add-on will still refer to the original add-on
name.

This add-on is a collection of app modules for various modern Windows apps,
as well as enhancements and fixes for certain controls found in Windows 10
and later.

Zahrnuté sú nasledujúce moduly (podrobný popis nájdete nižšie):

* Calculator (modern)
* Cortana (konverzácia)
* Pošta
* Mapy
* Microsoft Solitaire Collection
* Obchod microsoft
* Modern keyboard (emoji panel/dictation/voice typing/hardware input
  suggestions/clipboard history/modern input method editors)
* Ľudia
* Nastavenia (systémové nastavenia, Win+I)
* Počasie
* Miscellaneous modules for controls such as Start Menu tiles

Poznámky:

* This add-on requires Windows 10 20H2 (build 19042) or later and is
  compatible with Windows 11.
* Although installation is possible, this add-on does not support Windows
  Enterprise LTSC (Long-Term Servicing Channel) and Windows Server releases.
* Niektoré doplnkové funkcie sú alebo časom budú súčasťou NVDA.
* For entries not listed below, you can assume that features are part of
  NVDA, no longer applicable as the add-on does not support unsupported
  Windows releases such as old Windows 10 versions, or changes were made to
  Windows and apps that makes entries no longer applicable.
* Some apps support compact overlay mode (always on top in Calculator, for
  example), and this mode will not work properly with portable version of
  NVDA.

Podrobné úpravy medzi jednotlivými verziami nájdete v [Zozname zmien
(anglicky)][3].

## Všeobecné

* NVDA can announce suggestion count when performing a search in majority of
  cases, including when suggestion count changes as search progresses. This
  option is controlled by "Report object position information" in Object
  presentation panel found in NVDA settings.
* In addition to UIA event handlers provided by NVDA, the following UIA
  events are recognized: drag start, drag cancel, drag complete, drop target
  drag enter, drop target drag leave, drop target dropped, layout
  invalidated. With NVDA's log level set to debug, these events will be
  tracked, and for UIA notification event, a debug tone will be heard if
  notifications come from somewhere other than the currently active
  app. Events built into NVDA such as name change and controller for events
  will be tracked from an add-on called Event Tracker.
* When opening, closing, reordering (Windows 11), or switching between
  virtual desktops, NVDA will announce active virtual desktop name (desktop
  2, for example).
* NVDA will no longer announce Start menu size text when changing screen
  resolutions or orientation.
* Pri presúvaní dlaždíc alebo položiek v centre akcií (skratky
  alt+shift+šípky), NVDA oznamuje nové umiestnenie položiek.
* Oznamovanie zmeny hlasitosti a jasu v okne pracovnej plochy a iných oknách
  Explorera a tiež upozornení z obchodu Microsoft store je možné pozastaviť
  odčiarknutím možnosti Oznamovať notifikácie v nastaveniach > prezentácia
  objektov.

## Kalkulačka

* NVDA will no longer announce graphing calculator screen message twice.

## Cortana

Most items are applicable when using Cortana Conversations (Windows 10 2004
and later).

* Väčšinou sú oznamované textové odpovede z Cortany.
* NVDA nevyrušuje, keď komunikujete s Cortanou.

## Pošta

* Pri prezeraní položiek v zozname správ môžete teraz použiť príkazy
  navigácie v tabuľke na kontrolu hlavičiek správ. Upozorňujeme, že
  navigácia medzi riadkami (správami) nie je podporovaná.

## Mapy

* NVDA zvukom indikuje polohu na mape.
* Ak používate zobrazenie s pohľadom na ulicu, a ak je povolená možnosť
  použiť klávesnicu, NVDA pri pohybe šípkami oznamuje názvy ulíc.

## Microsoft Solitaire Collection

* NVDA oznamuje karty a kombinácie kariet.

## Obchod microsoft

* Po kontrole aktualizácií je možné prezerať zoznam s aktualizovanými
  aplikáciami.
* When downloading content such as apps and movies, NVDA will announce
  product name and download progress.

## Moderná klávesnica

This includes emoji panel, clipboard history, dictation/voice typing,
hardware input suggestions, and modern input method editors for certain
languages. When viewing emojis, for best experience, enable Unicode
Consortium setting from NVDA's speech settings and set symbol level to
"some" or higher. When pasting from clipboard history in Windows 10, press
Space key instead of Enter key to paste the selected item. NVDA also
supports updated input experience panel in Windows 11.

* When an emoji group (including kaomoji and symbols group in Windows 10
  1903 or later) is selected, NVDA will no longer move navigator object to
  certain emojis.
* Added support for updated input experience panel (combined emoji panel and
  clipboard history) in Windows 11.

## Ľudia

* Pri hľadaní kontaktov bude oznámený prvý návrh, najmä ak používate
  najnovšie vydania aplikácie.

## Nastavenia

* NVDA automaticky oznamuje priebeh prípadne chyby aktualizácie Windows a
  priebeh a dokončenie čistenia disku.
* NVDA dvojnásobne neopakuje hodnoty indikátorov priebehu a ďalšie
  informácie.
* Odd control labels seen in certain Windows installations has been
  corrected.
* NVDA will announce the name of the optional quality update link if
  present, typically named "download and install now".

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
