# Osnovne Windows aplikacije (Windows App Essentials) #

* Autori: Joseph Lee, Derek Riemer i drugi
* Preuzmi [stabilnu verziju][1]
* Preuzmi [razvojnu verziju][2]
* NVDA kompatibilnost: 2022.2 i novije verzije

Napomena: Izvorno ime „Osnovni moduli za Windows 10 aplikacije”, preimenovan
je 2021. godine u „Osnovni moduli za Windows aplikacije” kako bi podržao
Windows 10 i buduća izdanja poput Windows 11. Dijelovi ovog dodatka će se i
nadalje odnositi na izvorno ime dodatka.

Ovaj NVDA dodatak je zbirka aplikacijskih modula za razne Windows
aplikacije, kao i poboljšanja i ispravci određenih kontrola u sustavu
Windows 10 i novijim.

Uključeni su sljedeći moduli (za svaku aplikaciju postoji odlomak, gdje piše
što je uključeno):

* Cortana
* Karte
* Moderna tipkovnica (ploča emojija, diktatiranje, tipkanje glasom,
  prijedlozi hardvera unosa, povijest međuspremnika, predložene radnje,
  moderni uređivači za unos)
* Osobe
* Postavke (postavke sustava, Windows+I)
* Pristup glasu (Windows 11 22H2)
* Vrijeme
* Dodatni moduli za kontrole kao što su pločice izbornika Start

Napomene:

* This add-on requires Windows 10 21H2 (build 19044), 11 21H2 (build 22000),
  or later releases.
* Mada je instalacija moguća, ovaj dodatak ne podržava izdanja Windows
  Enterprise LTSC (Long-Term Servicing Channel) i Windows Server.
* If Add-on Updater 22.08 or later is installed and background add-on
  updates is enabled, Windows App Essentials will not install at all on
  unsupported Windows releases.
* Not all features from Windows Insider Preview builds will be supported.
* Neke funkcije dodatka već jesu ili će postati dio NVDA čitača ekrana.
* Za unose koji niže dolje nisu navedeni, može se pretpostaviti da su te
  funkcije dio NVDA čitača. Više nisu primjenjive jer dodatak ne podržava
  stara izdanja sustava poput stare Windows 10 verzije ili su napravljene
  promjene u Windows sustavu i aplikacijama, zbog čega unosi više nisu
  primjenjivi.
* Neke aplikacije podržavaju način kompaktnog preklapanja (na primjer,
  uvijek na vrhu u Kalkulatoru) i ovaj modus neće ispravno raditi s
  prijenosnom verzijom NVDA čitača.
* For best experience with apps that embed web technologies and content such
  as Start menu and its context menu, enable "Automatic focus mode for focus
  changes" setting from NVDA's browse mode settings panel.

Za popis promjena izvršenih između svakog izdanja dodatka, pogledaj
[dokument s izmjenama izdanja dodatka][3].

## Opće

* In addition to UIA event handlers provided by NVDA, the following UIA
  events and properties are recognized: drag complete, drag drop effect,
  drop target dropped. With NVDA's log level set to debug, these events will
  be tracked and logged.
* Prilikom otvaranja, zatvaranja, preraspoređivanja (Windows 11) ili
  prebacivanja između virtualnih radnih površina, NVDA će najaviti
  trenutačno ime radne površine (na primjer, desktop 2).
* When dragging and dropping items such as arranging pinned entries (tiles
  in Windows 10) in Start menu or Action Center quick actions with
  Alt+Shift+arrow keys, NVDA will announce "dragging" and/or drag and drop
  effects before and while dragging items, respectively. NVDA announcing
  "dragging" is now part of NVDA 2022.4.
* Najave kao što su promjena glasnoće/svjetline u File Explorereru i
  obavijesti aktualiziranja programa s Microsoft Store stranica, mogu se
  potisnuti isključivanjem opcije „Izvijesti o obavijestima” u NVDA
  postavkama prikaza objekata.
* In Windows 11 22H2 and later, microphone mute toggle status
  (Windows+Alt+K) is announced from everywhere.
* Item status changes are announced in more apps including Visual Studio
  Community 2022. This is now part of NVDA 2022.4.

## Cortana

* Tekstualni odgovori Cortane najavljuju se u većini slučajeva.
* NVDA neće govoriti kad pričaš sa Cortanom.

## Karte

* NVDA svira zvuk za lokacije za lokacije na karti.

## Moderna tipkovnica

This includes emoji panel, clipboard history, dictation/voice typing,
hardware input suggestions, suggested actions (preview), and modern input
method editors for certain languages across Windows 10 and 11. When viewing
emojis, for best experience, enable Unicode Consortium setting from NVDA's
speech settings and set symbol level to "some" or higher. When pasting from
clipboard history in Windows 10, press Space key instead of Enter key to
paste the selected item.

* U sustavu Windows 10, kad je odabrana grupa emojija (uključujući kaomoji i
  grupu simbola), NVDA više neće pomicati navigacijski objekt na određene
  emojije.
* U sustavu Windows 11 ponovo je moguće koristiti tipke sa strelicama za
  pregled emojija kad se otvori ploča s emojijima. Ovo je sada dio u NVDA
  2022.1.
* In Windows 11 clipboard history, browse mode will be turned off by
  default, designed to let NVDA announce clipboard history entry menu items.
* In Insider Preview build 25115 and later (backported to Windows 11 beta
  build 22622), NVDA will announce suggested actions when compatible data
  such as phone numbers is copied to the clipboard.

## Osobe

* Prilikom pretraživanja kontakata najavit će se prvi prijedlog, posebice,
  ako se koriste nedavna izdanja aplikacija.

## Postavke

* Čudne kontrolne oznake viđene u određenim Windows instalacijama su
  ispravljene.
* NVDA će najaviti naziv opcionalne kontrole kvalitete aktualiziranja ako
  postoji (preuzimi i instaliraj poveznicu sada u Windows 10, gumb za
  preuzimanje u Windows 11).
* U sustavu Windows 11 elementi trake navigacije se ispravno prepoznaju.
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

## Vrijeme

* Kartice poput „prognoza” i „karte” prepoznaju se kao ispravne kartice
  (zakrpu je napravio Derek Riemer).
* Prilikom čitanja prognoze, pritišćite strelice kako biste se kretali
  između stavaka. Pritišćite gornju ili donju strelicu kako biste se
  premještali između individualnih stavaka. Na primjer, pritiskom desne
  strelice čitač izgovara „Ponedjeljak: 79 stupnjeva, djelomično oblačno,
  …”, pritiskom na strelicu dolje izgovara „Ponedjeljak”. Ponovnim pritiskom
  čita sljedeću stavku (poput temperature). Ovo trenutačno radi za dnevnu i
  svakosatnu vremensku prognozu.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
