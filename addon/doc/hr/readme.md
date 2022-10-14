# Osnovni moduli za Windows aplikacije (Windows App Essentials) #

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
  prijedlozi za unos hardverom, povijest međuspremnika, predložene radnje,
  moderni uređivači za unos)
* Osobe
* Postavke (postavke sustava, Windows+I)
* Pristup glasu (Windows 11 22H2)
* Vrijeme
* Dodatni moduli za kontrole kao što su pločice izbornika Start

Napomene:

* Ovaj dodatak zahtijeva Windows 10 21H2 (gradnja 19044), 11 21H2 (gradnja
  22000) ili novija izdanja.
* Mada je instalacija moguća, ovaj dodatak ne podržava izdanja Windows
  Enterprise LTSC (Long-Term Servicing Channel) i Windows Server.
* If Add-on Updater 22.08 or later is installed and background add-on
  updates is enabled, Windows App Essentials will not install at all on
  unsupported Windows releases.
* Not all features from Windows Insider Preview builds will be supported.
* Neke funkcije dodatka već jesu ili će postati dio NVDA čitača ekrana.
* Za unose koji niže dolje nisu navedeni, može se pretpostaviti da su te
  funkcije dio NVDA čitača. Više nisu primjenjive jer dodatak ne podržava
  stara izdanja sustava poput stare Windows 10 verzije ili promjene u
  Windowsu, aplikacijama i NVDA čitaču zbog čega unosi više nisu
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
  events and properties are recognized: drag start/cancel/complete
  (recognized as state change event), drag drop effect, drag item is
  grabbed, drop target effect.
* Prilikom otvaranja, zatvaranja ili prebacivanja između virtualnih radnih
  površina, NVDA će najaviti ime aktivne virtualne radne površine (na
  primjer radna površina 2).
* Prilikom povlačenja i ispuštanja stavki kao što je raspoređivanje
  prikvačenih unosa (pločice u Windows 10) u izborniku Start ili brze radnje
  za Action Center s Alt+Šift+tipke sa strelicama, NVDA će najaviti efekte
  „povlačenja” i/ili povlačenja i ispuštanja prije i tijekom povlačenja
  stavki. Ovo je sada dio NVDA čitača 2022.4.
* Najave kao što su promjene glasnoće/svjetline/isključivanje mikrofona
  (Windows 11 22H2 i novije verzije) u File Explorereru i obavijesti
  aktualiziranja programa s Microsoft Store stranica, mogu se potisnuti
  isključivanjem opcije „Izvijesti o obavijestima” u NVDA postavkama prikaza
  objekata.
* In Windows 11, NVDA will announce search highlights in Start menu when it
  opens. This is now part of NVDA 2023.1.

## Cortana

* Tekstualni odgovori Cortane najavljuju se u većini slučajeva.
* NVDA neće govoriti kad pričaš sa Cortanom.

## Karte

* NVDA svira zvuk za lokacije za lokacije na karti.

## Moderna tipkovnica

To uključuje ploču s emojijima, povijest međuspremnika,
diktatiranje/tipkanje govorom, prijedloge unosa hardvera i moderne uređivače
načina unosa za određene jezike u Windows verzijama 10 i 11. Kad pregledavaš
emojije, aktiviraj postavku Unicode Consortium u NVDA postavkama govora i
postavi razinu simbola na „neki” ili višu. Prilikom umetanja iz povijesti
međuspremnika u sustavu Windows 10, pritisni tipku za razmak umjesto tipke
Enter za umetanje odabranog elementa.

* U ploči emojija sustava Windows 10, kad je jedna grupa emojija odabrana
  (uključujući kaomoji i grupa simbola), NVDA više neće pomicati
  navigacijski objekt na određene emojije.
* In Windows 11 clipboard history, browse mode will be turned off by
  default, designed to let NVDA announce clipboard history entry menu items.
* In Windows 11 22H2 Moment 1 and later, NVDA will announce suggested
  actions when compatible data such as phone numbers is copied to the
  clipboard.

## Osobe

* Prilikom pretraživanja kontakata najavit će se prvi prijedlog.

## Postavke

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

## Pristup glasu

Ovo se odnosi na značajku za pristup glasu koja je predstavljena u sustavu
Windows 11 22H2.

* NVDA će najaviti stanje mikrofona kad se mikrofon uključi ili isključi iz
  sučelja za pristup glasu.

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
