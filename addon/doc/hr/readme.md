# Osnovne Windows aplikacije (Windows App Essentials) #

* Autori: Joseph Lee, Derek Riemer i drugi
* Preuzmi [stabilnu verziju][1]
* Preuzmi [razvojnu verziju][2]
* NVDA compatibility: 2021.3 and later

Napomena: Izvorno ime „Osnovni moduli za Windows 10 aplikacije”, preimenovan
je 2021. godine u „Osnovni moduli za Windows aplikacije” kako bi podržao
Windows 10 i buduća izdanja poput Windows 11. Dijelovi ovog dodatka će se i
nadalje odnositi na izvorno ime dodatka.

Ovaj NVDA dodatak je zbirka aplikacijskih modula za razne Windows
aplikacije, kao i poboljšanja i ispravci određenih kontrola u sustavu
Windows 10 i novijim.

Uključeni su sljedeći moduli (za svaku aplikaciju postoji odlomak, gdje piše
što je uključeno):

* Kalkulator
* Cortana
* Mail
* Karte
* Microsoft Solitaire zbirka
* Moderna tipkovnica (ploča emojija, diktatiranje, tipkanje glasom,
  prijedlozi hardvera unosa, povijest međuspremnika, moderni uređivači za
  unos)
* Notepad (Windows 11)
* Osobe
* Postavke (postavke sustava, Windows+I)
* Vrijeme
* Dodatni moduli za kontrole kao što su pločice izbornika Start

Napomene:

* Ovaj dodatak zahtijeva Windows 10 21H1 (gradnja 19043) ili noviju verziju
  i kompatibilan je sa sustavom Windows 11.
* Mada je instalacija moguća, ovaj dodatak ne podržava izdanja Windows
  Enterprise LTSC (Long-Term Servicing Channel) i Windows Server.
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
* When arranging pinned entries (tiles in Windows 10) in Start menu or
  Action Center quick actions with Alt+Shift+arrow keys, NVDA will announce
  information on dragged items or new position of the dragged item.
* Najave kao što su promjena glasnoće/svjetline u File Explorereru i
  obavijesti aktualiziranja programa s Microsoft Store stranica, mogu se
  potisnuti isključivanjem opcije „Izvijesti o obavijestima” u NVDA
  postavkama prikaza objekata.
* In Windows 11 Insider Preview builds, microphone mute toggle status
  (Windows+Alt+K) is announced from everywhere.

## Kalkulator

* NVDA više neće dvaputa najaviti poruku ekrana grafičkog kalkulatora.
* In Windows 10, history and memory list items are properly labeled. This is
  now part of NVDA 2022.1.
* NVDA will now announce calculator display content when performing
  scientific mode commands such as trigonometry operations.

## Cortana

* Tekstualni odgovori Cortane najavljuju se u većini slučajeva.
* NVDA neće govoriti kad pričaš sa Cortanom.

## Mail

* Prilikom pregleda stavaka u popisu poruka, sada možete koristiti prečace
  za navigaciju po tablicama kako biste pregledali zaglavlja poruke.

## Karte

* NVDA svira zvuk za lokacije za lokacije na karti.

## Microsoft Solitaire zbirka

* NVDA će najaviti imenta karata i setove karata.

## Moderna tipkovnica

To uključuje ploču s emojijima, povijest međuspremnika,
diktatiranje/tipkanje govorom, prijedloge unosa hardvera i moderne uređivače
načina unosa za određene jezike. Kad pregledavaš emojije, aktiviraj postavku
Unicode Consortium u NVDA postavkama govora i postavi razinu simbola na
„neki” ili višu. Prilikom umetanja iz povijesti međuspremnika u sustavu
Windows 10, pritisni tipku za razmak umjesto tipke Enter za umetanje
odabranog elementa. Također, NVDA podržava aktualiziranu ploču unosa u
Windows 11.

* U sustavu Windows 10, kad je odabrana grupa emojija (uključujući kaomoji i
  grupu simbola), NVDA više neće pomicati navigacijski objekt na određene
  emojije.
* Dodana je podrška za aktualiziranu ploču unosa (kombinacija ploče emojija
  i povijesti međuspremnika) u Windows 11.
* In Windows 11, it is again possible to use the arrow keys to review emojis
  when emoji panel opens. This is now part of NVDA 2022.1.
* In Windows 11 clipboard history, browse mode will be turned off by
  default, designed to let NVDA announce clipboard history entry menu items.

## Notepad

Ovo se odnosi na Windows 11 Notepad verziju 11 ili noviju.

* NVDA će najaviti elemente stanja kao što su informacije o retku i stupcu
  kad se izvrši naredba statusne trake izvještaja (NVDA+Kraj u izgledu radne
  površine, NvDA+Shift+Kraj u izgledu prijenosnog računala).
* NVDA više neće najaviti upisani tekst, kad se pritisne tipka Enter u
  dokumentu.

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
