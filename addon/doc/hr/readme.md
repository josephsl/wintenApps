# Osnovni moduli za Windows aplikacije (Windows App Essentials) #

* Autori: Joseph Lee, Derek Riemer i drugi
* Preuzmi [stabilnu verziju][1]
* Preuzmi [razvojnu verziju][2]
* NVDA kompatibilnost: 2022.3 i novije verzije

Napomena: Izvorno ime „Osnovni moduli za Windows 10 aplikacije”, preimenovan
je 2021. godine u „Osnovni moduli za Windows aplikacije” kako bi podržao
Windows 10 i buduća izdanja poput Windows 11. Dijelovi ovog dodatka će se i
nadalje odnositi na izvorno ime dodatka.

Ovaj NVDA dodatak je zbirka modula za razne moderne Windows aplikacije, kao
i poboljšanja i ispravci određenih kontrola u sustavu Windows 10 i novijim.

Uključeni su sljedeći moduli (za svaku aplikaciju postoji odlomak, gdje piše
što je uključeno):

* Cortana
* Karte
* Moderna tipkovnica (ploča emojija, diktatiranje, tipkanje glasom,
  prijedlozi za unos hardverom, povijest međuspremnika, predložene radnje,
  moderni uređivači za unos)
* Postavke (postavke sustava, Windows+I)
* Pristup glasu (Windows 11 22H2)
* Vrijeme
* Razni moduli za kontrole i značajke kao što su najave virtualnih radnih
  površina

Napomene:

* Ovaj dodatak zahtijeva Windows 10 21H2 (gradnja 19044), 11 21H2 (gradnja
  22000) ili novija izdanja.
* Trajanje podrške za aktualiziranje značajki povezano je s trajanjem
  korisničke podrške (izdanja Home, Pro, Pro Education, Pro for
  Workstations) i dodatak može prekinuti podršku za aktualiziranje značajki
  prije završetka korisničke podrške. Pogledaj
  aka.ms/WindowsTargetVersioninfo za više informacija i datume podrške.
* Mada je instalacija moguća, ovaj dodatak ne podržava izdanja Windows
  Enterprise LTSC (Long-Term Servicing Channel) i Windows Server.
* Ako je dodatak „Ažuriranje dodataka” instaliran i pozadinsko ažuriranje
  dodataka aktivirano, dodatak „Osnovni moduli za Windows aplikacije” se
  uopće neće instalirati na nepodržana izdanja sustava Windows.
* Sve značajke iz Windows Insider Preview gradnji neće biti podržane,
  pogotovo značajke koje su predstavljene u podskupu „Windows Insiders” u
  kanalu razvoja. Za beta kanal, podržava se samo najnovija gradnja (22623).
* Neke funkcije dodatka već jesu ili će postati dio NVDA čitača ekrana.
* Neke aplikacije podržavaju način kompaktnog preklapanja (na primjer,
  uvijek na vrhu u Kalkulatoru) i ovaj modus neće ispravno raditi s
  prijenosnom verzijom NVDA čitača.
* Za najbolje iskustvo s aplikacijama koje ugrađuju web tehnologije i
  sadržaj kao što je izbornik Start i njegov kontekstni izbornik, aktiviraj
  postavku „Automatski modus fokusa za promjene fokusa” u ploči postavki
  modusa čitanja NVDA čitača.

Za popis promjena izvršenih između svakog izdanja dodatka, pogledaj
[dokument s izmjenama izdanja dodatka][3].

## Opće

* Pored UIA rukovateljima događajima koje nudi NVDA, prepoznaju se sljedeći
  UIA događaji i svojstva: početak povlačenja/odustani/dovršeno (prepoznati
  kao događaji promjene stanja), efekt povuci-i-ispusti, povlačenje prvog
  odabranog elementa, efekt ispuštanja na cilj. Ovi događaji su sada dio
  NVDA verzije 2022.4.
* Prilikom otvaranja, zatvaranja ili prebacivanja između virtualnih radnih
  površina, NVDA će najaviti ime aktivne virtualne radne površine (na
  primjer radna površina 2).
* Prilikom povlačenja i ispuštanja stavki kao što je raspoređivanje
  prikvačenih unosa (pločice u Windows 10) u izborniku Start ili brze radnje
  za Action Center s Alt+Šift+tipke sa strelicama, NVDA će najaviti efekte
  „povlačenja” i/ili povlačenja i ispuštanja prije i tijekom povlačenja
  stavki. Ovo je sada dio NVDA čitača 2022.4.
* U sustavu Windows 11, NVDA će najaviti istaknute stavke pretraživanja u
  izborniku Start kada se otvori. Ovo je sada dio u NVDA čitača 2023.1.
* U sustavu Windows 10, povijest i elementi popisa memorije ispravno su
  označeni.
  
U Windows 11 22H2 Moment 2, redizajnirano područje prelijevanje trake
  sustava može se pravilno otkriti kad se koristi interakcija miša i/ili
  dodira.
* NVDA će zabilježiti arhitekturu procesora za trenutačnu Windows
  instalaciju (x86/32-bit, AMD64, ARM64) kad se pokrene. Ovo je sada dio
  NVDA čitača 2023.1.
* In Windows 11 builds prior to Insider Preview build 25267, NVDA will
  announce results of rearranging taskbar icons when pressing
  Alt+Shift+left/right arrow keys.

## Cortana

* Tekstualni odgovori Cortane najavljuju se u većini slučajeva.
* NVDA neće govoriti kad pričaš sa Cortanom.

## Karte

* NVDA svira zvuk za lokacije za lokacije na karti.
* NVDA više neće prekidati govor kada je fokusiran na stavke koje nisu
  kontrole karte u nekim slučajevima.

## Moderna tipkovnica

To uključuje ploču s emojijima, povijest međuspremnika,
diktatiranje/tipkanje govorom, prijedloge unosa hardvera i moderne uređivače
načina unosa za određene jezike u Windows verzijama 10 i 11. Kad pregledavaš
emojije, aktiviraj postavku Unicode Consortium u NVDA postavkama govora i
postavi razinu simbola na „neki” ili višu. Prilikom umetanja iz povijesti
međuspremnika u sustavu Windows 10, za umetanje odabranog elementa pritisni
tipku za razmak umjesto tipke Enter.

* U ploči emojija sustava Windows 10, kad je jedna grupa emojija odabrana
  (uključujući kaomoji i grupa simbola), NVDA više neće pomicati
  navigacijski objekt na određene emojije.
* In Windows 11 clipboard history, browse mode will be turned off by
  default, designed to let NVDA announce clipboard history entry menu
  items. This is now part of NVDA 2023.1.
* U sustavu Windows 11 22H2 Moment 1 i novijim verzijama, NVDA će najaviti
  predložene radnje kad se kompatibilni podaci poput telefonskih brojeva
  kopiraju u međuspremnik.

## Postavke

* NVDA će najaviti naziv opcionalne kontrole kvalitete aktualiziranja ako
  postoji (preuzimi i instaliraj poveznicu sada u Windows 10, gumb za
  preuzimanje u Windows 11).
* U sustavu Windows 11 elementi trake navigacije se ispravno prepoznaju.
* U sustavu Windows 10 i 11 22H2 i novijim verzijama, NVDA će prekinuti
  govor i prijaviti ažuriranja stanja Windows Update kao preuzimanje i
  napredovanje instaliranja. To može prouzročiti prekid govora prilikom
  kretanja po aplikaciji „Postavke” dok se ažuriranja preuzimaju i
  instaliraju. Ako koristiš Windows 11 22H2 i noviju verziju, ako je
  selektivna registracija UIA događaja uključena, morađ premjestiti fokus na
  popis ažuriranja čim se pojave kako bi NVDA mogao najaviti napredovanje
  ažuriranja.

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
