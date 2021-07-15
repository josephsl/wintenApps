# Windows App Essentials #

* Autory: Joseph Lee, Derek Riemer a ďalší používatelia Windowsu 10
* Stiahnuť [stabilnú verziu][1]
* Stiahnuť [vývojovú verziu][2]
* NVDA compatibility: 2020.4 and beyond

Note: Originally called Windows 10 App Essentials, it was renamed to Windows
App Essentials in 2021 to support Windows 10 and future releases such as
Windows 11. Parts of this add-on will still refer to the original add-on
name.

This add-on is a collection of app modules for various modern Windows apps,
as well as enhancements and fixes for certain controls found in Windows 10
and later.

Zahrnuté sú nasledujúce moduly (podrobný popis nájdete nižšie):

* Calculator (modern)
* Kalendár
* Cortana (konverzácia)
* Pošta
* Mapy
* Microsoft Solitaire Collection
* Obchod microsoft
* Modern keyboard (emoji panel/dictation/hardware input
  suggestions/clipboard history/modern input method editors)
* Ľudia
* Nastavenia (systémové nastavenia, Win+I)
* Počasie
* Miscellaneous modules for controls such as Start Menu tiles

Poznámky:

* This add-on requires Windows 10 20H2 (build 19042) or later. For best
  results, use the add-on with latest Windows release (Windows 10 21H1/build
  19043).
* Although installation is possible, this add-on does not support Windows
  Enterprise LTSC (Long-Term Servicing Channel) and Windows Server releases.
* Support for Windows 11 is experimental, and some features will not work
  (see relevant entries for details).
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

* NVDA vo väčšine prípadov dokáže oznámiť počet návrhov pri
  vyhľadávaní. Oznamovanie môžete zapnúť a vypnúť v strome nastavení NVDA,
  časť prezentácia objektov, položka Oznamovať pozíciu objektu.
* When searching in Start menu or File Explorer in Windows 10 1909 (November
  2019 Update) and later, instances of NVDA announcing search results twice
  when reviewing results are less noticeable, which also makes braille
  output more consistent when reviewing items.
* In addition to UIA event handlers provided by NVDA, the following UIA
  events are recognized: drag start, drag cancel, drag complete, drop target
  drag enter, drop target drag leave, drop target dropped. With NVDA's log
  level set to debug, these events will be tracked, and for UIA notification
  event, a debug tone will be heard if notifications come from somewhere
  other than the currently active app. Some events will provide additional
  information such as element count in controller for event, state of the
  element for state change event, and item text for item status event.
* Je možné sledovať iba konkrétne udalosti a udalosti pochádzajúce z
  konkrétnych aplikácií.
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

## Kalendár

* NVDA neoznamuje v tele správy a iných prvkoch nadbitočné informácie, ako
  editačné pole alebo iba na čítanie.

## Cortana

Most items are applicable when using Cortana Conversations (Windows 10 2004
and later).

* Väčšinou sú oznamované textové odpovede z Cortany.
* NVDA nevyrušuje, keď komunikujete s Cortanou.
* In Windows 10 1909 (November 2019 Update) and later, modern search
  experience in File Explorer powered by Windows Search user interface is
  supported.

## Pošta

* Pri prezeraní položiek v zozname správ môžete teraz použiť príkazy
  navigácie v tabuľke na kontrolu hlavičiek správ. Upozorňujeme, že
  navigácia medzi riadkami (správami) nie je podporovaná.
* NVDA zvukom upozorní, ak pri písaní správy spomeniete niekoho z kontaktov.

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
  product name and download progress (does not work properly in updated
  Microsoft Store in Windows 11).

## Moderná klávesnica

This includes emoji panel, clipboard history, dictation, hardware input
suggestions, and modern input method editors for certain languages. When
viewing emojis, for best experience, enable Unicode Consortium setting from
NVDA's speech settings and set symbol level to "some" or higher. Also, NVDA
supports updated input experience panel in Windows 11.

* Pri otvorení histórie schránky, NVDA viac neoznamuje slovo "schránka" pri
  niektorých položkách.
* On some systems running Windows 10 1903 (May 2019 Update) and later, NVDA
  will no longer appear to do nothing when emoji panel opens.
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
* Dialóg s pripomenutím aktualizácie Windows je rozpoznaný ako štandardný
  dialóg.
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
