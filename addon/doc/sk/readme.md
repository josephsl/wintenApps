# Vylepšenia prístupnosti pre Windows 10 #

* Autory: Joseph Lee, Derek Riemer a ďalší používatelia Windowsu 10
* Stiahnuť [stabilnú verziu][1]
* Stiahnuť [vývojovú verziu][2]
* NVDA compatibility: 2020.2 to 2020.4

Obsahuje aplikačné moduly pre rôzne aplikácie systému Windows 10, ako aj
vylepšenia a opravy určitých ovládacích prvkov systému Windows 10.

Zahrnuté sú nasledujúce moduly (podrobný popis nájdete nižšie):

* Kalkulačka (moderná)
* Kalendár
* Cortana (konverzácia)
* Pošta
* Mapy
* Microsoft Solitaire Collection
* Obchod microsoft
* Podpora pre vstupy (zahŕňa panel emoji, diktovanie, návrhy pri písaní,
  schránka a moderné spôsoby písania)
* Ľudia
* Nastavenia (systémové nastavenia, Win+I)
* Počasie.
* Rôzne moduly pre ovládacie prvky, napríklad dlaždice ponuky Štart.

Poznámky:

* This add-on requires Windows 10 Version 1909 (build 18363) or later. For
  best results, use the add-on with latest Windows 10 stable release
  (20H2/build 19042).
* Niektoré doplnkové funkcie sú alebo časom budú súčasťou NVDA.
* V prípade položiek, ktoré nie sú uvedené nižšie, môžete predpokladať, že
  funkcie sú súčasťou NVDA, alebo už nie sú relevantné, pretože doplnok
  nepodporuje staré vydania systému Windows 10 alebo boli vykonané zmeny v
  systéme Windows 10 a úpravy viac nie sú potrebné.

Podrobné úpravy medzi jednotlivými verziami nájdete v [Zozname zmien
(anglicky)][3].

## Všeobecné

* NVDA neprehráva chybové tóny a jednoducho nerobí nič, ak bude tento
  doplnok aktívny v systéme Windows 7, Windows 8.1 a nepodporovaných
  vydaniach systému Windows 10.
* Okrem dialógov rozpoznaných programom NVDA je teraz zlepšená orientácia vo
  viacerých dialógoch, vrátane časti Windows insider program.
* NVDA vo väčšine prípadov dokáže oznámiť počet návrhov pri
  vyhľadávaní. Oznamovanie môžete zapnúť a vypnúť v strome nastavení NVDA,
  časť prezentácia objektov, položka Oznamovať pozíciu objektu.
* NVDA viac neoznamuje dvakrát výsledky hľadania pri vyhľadávaní v ponuke
  štart alebo prieskumníkovi (Windows od verzie 1909 (November 2019)). Toto
  tiež zlepšuje oznamovanie výsledkov na braillovskom riadku.
* NVDA rozpoznáva nasledujúce udalosti UIA: controller for, drag start, drag
  cancel, drag complete, drag target enter, drag target leave, drag target
  dropped, element selected, item status, live region change, notification,
  system alert, text change, tooltip opened, window opened. Informácie o
  prvkoch sa zapisujú do záznamu (pri nastavenej úrovni debug). Ak príde
  udalosť z inej aplikácie, udalosť sa rovnako zapíše a vývojové verzie NVDA
  ohlásia zápis charakteristickým zvukom chyby. Pri niektorých prvkoch je
  tiež doplnená informácia o počte položiek, stav alebo text.
* Je možné sledovať iba konkrétne udalosti a udalosti pochádzajúce z
  konkrétnych aplikácií.
* NVDA viac neupozorňuje zvukom na situácie, keď nie je možné zistiť ID
  prvku.
* Pri otváraní, zatváraní alebo prepínaní medzi virtuálnymi pracovnými
  plochami NVDA oznámi aktuálny názov pracovnej plochy (napríklad pracovná
  plocha 2).
* NVDA will no longer announce Start menu size text when changing screen
  resolution or orientation.
* Pri presúvaní dlaždíc alebo položiek v centre akcií (skratky
  alt+shift+šípky), NVDA oznamuje nové umiestnenie položiek.
* NVDA viac neoznamuje správu "zmazať slovo" pri mazaní skratkou
  ctrl+backspace vo Worde 365.
* Oznamovanie zmeny hlasitosti a jasu v okne pracovnej plochy a iných oknách
  Explorera a tiež upozornení z obchodu Microsoft store je možné pozastaviť
  odčiarknutím možnosti Oznamovať notifikácie v nastaveniach > prezentácia
  objektov.
* Okno otvoriť v programe je správne oznamované od verzie 2004 (Máj 2020).

## Kalkulačka

* Keď stlačíte ENTER alebo Escape, NVDA oznámi výsledky výpočtu.
* Pri výpočtoch, ako sú prevodník jednotiek a prevodník mien, NVDA oznámi
  výsledky hneď po zadaní príkladu.
* NVDA neoznamuje pri výsledkoch úroveň nadpisu.
* NVDA upozorní, ak pri zadávaní výrazu dosiahnete maximálny počet číslic.
* Pridaná podpora pre režim vždy zapnuté v kalkulačke od verzie 10.1908.

## Kalendár

* NVDA neoznamuje v tele správy a iných prvkoch nadbitočné informácie, ako
  editačné pole alebo iba na čítanie.

## Cortana

Väčšina položiek už nie je aktuálnych od verzie 1903 ak nepoužívate Cortana
Conversations (od verzie 2004).

* Väčšinou sú oznamované textové odpovede z Cortany.
* NVDA nevyrušuje, keď komunikujete s Cortanou.
* Podporované vyhľadávanie v prieskumníkovi, predstavené od verzie 1909
  (November 2019).

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
* Pri sťahovaní obsahu, ako sú aplikácie a filmy, NVDA oznámi názov produktu
  a priebeh sťahovania.

## Moderná klávesnica

Zahŕňa podporu pre panel emoji, históriu schránky, diktovanie, návrhy pri
písaní a podporu pre moderné editory pre rôzne jazyky. Pri používaní panelu
emoji odporúčame aktivovať v nastaveniach reči použitie databázy unicode
konzorcia a nastaviť úroveň interpunkcie na väčšina alebo všetka.

* Pri otvorení histórie schránky, NVDA viac neoznamuje slovo "schránka" pri
  niektorých položkách.
* Na niektorých systémoch s verziou 1903 (aktualizácia z mája 2019) je
  oznamované otvorenie panela emoji.
* pridaná podpora pre metódy písania v Čínštine, Japončine a Kórejčine,
  predstavené od verzie 2004 (zostava 18965)
* Ak je vybratá skupina emoji(alebo symbolov a kaomoji od verzie 1903), NVDA
  nepresúva navigačný objekt automaticky na prvú položku.
* NVDA will announce selected emoji if emoji panel is opened more than once
  in build 20226.

## Ľudia

* Pri hľadaní kontaktov bude oznámený prvý návrh, najmä ak používate
  najnovšie vydania aplikácie.

## Nastavenia

* NVDA automaticky oznamuje priebeh prípadne chyby aktualizácie Windows a
  priebeh a dokončenie čistenia disku.
* NVDA dvojnásobne neopakuje hodnoty indikátorov priebehu a ďalšie
  informácie.
* NVDA dokáže vo väčšine prípadov rozpoznať názvy a hodnoty pri zoznamových
  rámikoch a prepínačoch.
* NVDA správne funguje pri použití objektovej navigácie.
* Dialóg s pripomenutím aktualizácie Windows je rozpoznaný ako štandardný
  dialóg.
* Opravené nesprávne popisky prvkov v niektorých verziách Windows 10.
* V novších verziách verzie 1803 a novších, bol do dialógu aktualizácie
  Windows pridaný odkaz stiahnuť a nainštalovať teraz. NVDA teraz oznámi
  názov novej aktualizácie, ak je k dispozícii.

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
