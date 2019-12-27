# Windows 10 App Essentials #

* Autory: Joseph Lee, Derek Riemer a ďalší používatelia Windowsu 10
* Stiahnúť [stabilnú verziu][1]
* Stiahnúť [vývojovú verziu][2]
* NVDA compatibility: 2019.3 and beyond
* Download [older version][4] compatible with NVDA 2019.2.1 and earlier

Tento doplnok je zbierka aplikačných modulov pre rôzne aplikácie systému
Windows 10, ako aj vylepšenia a opravy určitých ovládacích prvkov systému
Windows 10.

Zahrnuté sú nasledujúce aplikačné moduly alebo podporné moduly pre niektoré
aplikácie (podrobnosti o obsahu nájdete v každej časti aplikácie):

* Kalkulačka (moderná).
* Kalendár
* Cortana (klasická  a konzerzácia)
* Spätná väzba
* Pošta
* Mapy
* Microsoft Edge
* Microsoft Obchod
* Modern keyboard (emoji panel/dictation/hardware input suggestions/cloud
  clipboard history/modern input method editors)
* Ľudia
* Nastavenia (systémové nastavenia, Win+I)
* Počasie
* Rôzne moduly pre ovládacie prvky, napríklad dlaždice ponuky Štart.

Poznámky:

* This add-on requires Windows 10 Version 1809 (build 17763) or later and
  NVDA 2019.3 or later. For best results, use the add-on with latest Windows
  10 stable release (build 18363) and latest stable version of NVDA.
* Niektoré doplnkové funkcie sú alebo budú súčasťou čítačky obrazovky NVDA.
* V prípade položiek, ktoré nie sú uvedené nižšie, môžete predpokladať, že
  funkcie sú súčasťou NVDA, ktoré už nie sú použiteľné, pretože doplnok
  nepodporuje staré vydania systému Windows 10 alebo boli vykonané zmeny v
  systéme Windows 10 a v aplikáciách, vďaka ktorým položky už nie sú
  použiteľné.

Zoznam zmien vykonaných medzi jednotlivými vydaniami doplnkov nájdete v
dokumente [changelogs for add-on release][3].

## Všeobecné

* NVDA už nebude prehrávať chybové tóny alebo nebude robiť nič, ak bude
  tento doplnok aktívny v systéme Windows 7, Windows 8.1 a nepodporovaných
  vydaniach systému Windows 10.
* Submenu items are properly recognized in various apps, including context
  menu for Start menu tiles and microsoft Edge's app menu in Version 1809
  (October 2018 Update).
* Okrem dialógov rozpoznaných programom NVDA je teraz viac dialógov
  rozpoznaných ako správne dialógy a ako také, sú hlásené vrátane dialógov
  Insider Preview (app settings).
* NVDA môže vo väčšine prípadov oznámiť počet návrhov pri vyhľadávaní. Táto
  voľba je riadená pomocou "Informácie o polohe objektu" v paneli
  Prezentácia objektu nájdené v nastaveniach NVDA.
* NVDA will no longer announce "blank" when pressing up or down arrow to
  open all apps views in Start menu. This is now part of NVDA 2019.3.
* When searching in Start menu or File Explorer in Version 1909 (November
  2019 Update) and later, instances of NVDA announcing search results twice
  when reviewing results are less noticeable, which also makes braille
  output more consistent when reviewing items.
* V určitých kontextových ponukách (napríklad v Edge) sa už informácie o
  polohe (napríklad 1 z 2) už neoznamujú.
* The following UIA events are recognized: controller for, drag start, drag
  cancel, drag complete, drag target enter, drag target leave, drag target
  dropped, element selected, item status, live region change, notification,
  system alert, text change, tooltip opened, window opened. With NVDA set to
  run with debug logging enabled, these events will be tracked, and for UIA
  notification event, a debug tone will be heard if notifications come from
  somewhere other than the currently active app.
* Je možné sledovať iba konkrétne udalosti a / alebo udalosti pochádzajúce z
  konkrétnych aplikácií.
* Tooltips from Edge and universal apps are recognized and will be
  announced. This is now part of NVDA 2019.3.
* Pri otváraní, zatváraní alebo prepínaní medzi virtuálnymi pracovnými
  plochami NVDA oznámi aktuálny názov pracovnej plochy (napríklad desktop
  2).
* NVDA už nebude oznamovať veľkosť textu ponuky Štart pri zmene rozlíšenia
  alebo orientácie obrazovky.
* App name and version for various Microsoft Store apps are now shown
  correctly. This is now part of NVDA 2019.3.
* When arranging Start menu tiles or Action Center quick actions with
  Alt+Shift+arrow keys, NVDA will announce information on dragged items or
  new position of the dragged item.

## Kalkulačka

* Keď stlačíte ENTER alebo Escape, NVDA oznámi výsledky výpočtu.
* Pri výpočtoch, ako sú prevodník jednotiek a prevodník mien, NVDA oznámi
  výsledky hneď po zadaní výpočtov.
* NVDA už nebude oznamovať „úroveň nadpisu“ pre výsledky kalkulačky.
* NVDA upozorní, ak sa pri zadávaní výrazu dosiahne maximálny počet číslic.
* Added support for always on mode in Calculator version 10.1908 and later.

## Kalendár

* NVDA už neoznámi v tele správy a ďalších poliach „upraviť“ alebo „iba na
  čítanie“.

## Cortana

Väčšina položiek už nie je použiteľná vo verzii 1903 a novšej. Classic
Cortana označuje staršie rozhranie Cortana, ktoré bolo súčasťou ponuky
Štart.

* Textové odpovede od Cortany (UI Classic aj Conversations UI) sa oznamujú
  vo väčšine situácií (ak používate Classic Cortana, znova otvorte ponuku
  Štart a skúste znova hľadať, ak odpovede nie sú oznámené).
* NVDA bude mlčať, keď bude hovoriť s Cortanou hlasom.
* V Classic Cortana NVDA po nastavení nastaví upomienku.
* In Version 1909 (November 2019 Update) and later, modern search experience
  in File Explorer powered by Windows Search user interface is supported.

## Spätná väzba

* V prípade novších vydaní aplikácií už NVDA nebude oznamovať kategórie
  spätnej väzby dvakrát.

## Pošta

* Pri prezeraní položiek v zozname správ môžete teraz použiť príkazy
  navigácie v tabuľke na kontrolu hlavičiek správ. Upozorňujeme, že
  navigácia medzi riadkami (správami) nie je podporovaná.
* Pri písaní správy je vzhľad zmienených návrhov oznamovaný zvukom.

## Mapy

* NVDA prehrá pípnutie polohy pre umiestnenie na mape.
* Ak používate bočný pohľad na ulicu a ak je povolená možnosť „použiť
  klávesnicu“, NVDA oznámi pri navigácii na mape adresy ulíc pomocou
  klávesov so šípkami.

## Microsoft Edge

Toto sa týka klasickej EdgeHTML založenej aplikácie Microsoft Edge.

* Text auto-complete will be tracked and announced in address omnibar. This
  is now part of NVDA 2019.3.
* NVDA will no longer play suggestion sound when pressing F11 to toggle full
  screen. This is now part of NVDA 2019.3.
* Removed suggestions sound playback for address omnibar. This is now part
  of NVDA 2019.3.

## Microsoft Obchod

* Po kontrole aktualizácií aplikácií sú názvy aplikácií v zozname
  aktualizovaných aplikácií správne oznamované.
* Pri sťahovaní obsahu, ako sú aplikácie a filmy, NVDA oznámi názov produktu
  a postup sťahovania.

## Moderná klávesnica

This includes emoji panel, clipboard history, dictation, hardware input
suggestions, and modern input method editors for certain languages. When
viewing emojis, for best experience, enable Unicode Consortium setting from
NvDA's speech settings and set symbol level to "some" or higher.

* Support for Emoji input panel in Version 1709 (Fall Creators Update) and
  later, including redesigned panel in Version 1809 (build 17661 and later)
  and changes made in Version 1903 (build 18262 and later, including kaomoji
  and symbols categories in build 18305). This is also applicable in Version
  2004 (build 18963 and later) as the app has been renamed. All of these
  changes are now part of NVDA 2019.3.
* When opening clipboard history, NVDA will no longer announce "clipboard"
  when there are items in the clipboard under some circumstances.
* On some systems running Version 1903 (May 2019 Update) and later, NVDA
  will no longer appear to do nothing when emoji panel opens.
* Added support for modern Chinese, Japanese, and Korean (CJK) IME
  candidates interface introduced in Version 2004 (build 18965 and later).

## Ľudia

* Pri hľadaní kontaktov bude oznámený prvý návrh, najmä ak používate
  najnovšie vydania aplikácií.

## Nastavenia

* Niektoré informácie, ako napríklad Priebeh Windows Update, sa hlásia
  automaticky, vrátane widgetu Storage sense / vyčistenie disku a chýb z
  Windows Update.
* Hodnoty indikátora priebehu a ďalšie informácie sa už neoznamujú dvakrát.
* Pre niektoré rozbaľovacie zoznamy a prepínacie tlačidlá  nebude NVDA
  naďalej rozpoznávať štítky a / alebo oznamovať zmeny hodnoty.
* Audio Volume progress bar beeps are no longer heard in Version 1803 and
  later. This is now part of NVDA 2019.3.
* Ak sa za určitých okolností používajú príkazy navigácie objektov, NVDA už
  nebude robiť nič alebo nebude prehrávať chybové tóny.
* Dialógové okno pripomenutia služby Windows Update sa považuje za správne
  dialógové okno.
* Menovky lichých kontrol zobrazené v niektorých inštaláciách systému
  Windows 10 boli opravené.
* V novších verziách verzie 1803 a novších, z dôvodu zmien v postupe Windows
  Update pre aktualizácie funkcií, bol pridaný odkaz „stiahnuť a
  nainštalovať teraz“. NVDA teraz oznámi názov novej aktualizácie, ak je k
  dispozícii.

## Počasie

* Tabs such as "forecast" and "maps" are recognized as proper tabs (patch by
  Derek Riemer).
* When reading a forecast, use the left and right arrows to move between
  items. Use the up and down arrows to read the individual items. For
  example, pressing the right arrow might report "Monday: 79 degrees, partly
  cloudy, ..." pressing the down arrow will say "Monday" Then pressing it
  again will read the next item (Like the temperature). This currently works
  for daily and hourly forecasts.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog

[4]: https://addons.nvda-project.org/files/get.php?file=w10-2019
