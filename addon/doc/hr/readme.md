# Osnovni moduli za Windows aplikacije (Windows App Essentials) #

* Autori: Joseph Lee, Derek Riemer i drugi
* Preuzmi [stabilnu verziju][1]
* Preuzmi [beta verziju][2]
* Preuzmi [razvojnu verziju][3]
* NVDA kompatibilnost: 2022.4 i novije verzije

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
* Windows Insider Preview gradnje neće podržati sve značajke, pogotovo
  značajke koje su predstavljene u podskupu „Windows Insiders” u kanalima
  canary i razvoja.
* Kanal dodataka u razvoju uključivat će promjene uključujući
  eksperimentalni sadržaj koji može, ali ne mora biti uključen u beta i
  stabilnim izdanjima, a beta kanal će sadržati promjene koje su planirane
  za buduća stabilna izdanja.
* Neke funkcije dodatka već jesu ili će postati dio NVDA čitača ekrana.
* Za najbolje iskustvo s aplikacijama koje ugrađuju web tehnologije i
  sadržaj kao što je izbornik Start i njegov kontekstni izbornik, aktiviraj
  postavku „Automatski modus fokusa za promjene fokusa” u ploči postavki
  modusa čitanja NVDA čitača.

Za popis promjena između izdanja dodatka, pogledaj dokument [s izmjenama
izdanja dodatka][4].

## Opće

* Prilikom otvaranja, zatvaranja ili prebacivanja između virtualnih radnih
  površina, NVDA će najaviti ime aktivne virtualne radne površine (na
  primjer radna površina 2).
* U sustavu Windows 11, NVDA će najaviti istaknute stavke pretraživanja u
  izborniku Start kada se otvori. Ovo je sada dio u NVDA čitača 2023.1.
* U sustavu Windows 11 22H2 i daljnjim izdanjima, interakcija mišem i/ili
  dodirom može se koristiti za interakciju s redizajniranim prozorom trake
  sustava i dijaloškim okvirom „Otvori pomoću”. Ovo je sada dio NVDA verzije
  2023.1.
* NVDA će zabilježiti arhitekturu procesora za trenutačnu Windows
  instalaciju (x86/32-bit, AMD64, ARM64) kad se pokrene. Ovo je sada dio
  NVDA čitača 2023.1.
* Poboljšana programska traka sustava Windows 10 i 11, uključujući
  najavljivanje rezultata premještanja ikona kada se pritisne Alt+Šift+tipke
  strelica lijevo/desno (Windows 11 prije izgradnje 25267) i izvještavanje o
  položaju stavke prilikom kretanja kroz ikone programske trake (Windows 10
  i 11 prije izgradnje 25281).
* NVDA će najaviti tekst prazne mape unutar prazne mape u File Exploreru.
* U aplikacijama kao što su File Explorer i Notepad gdje su podržani prozori
  s karticama, NVDA će najaviti ime i položaj kartica prilikom prebacivanja
  između njih. Ovo je sada dio NVDA verzije 2023.2.

## Cortana

* Tekstualni odgovori Cortane najavljuju se u većini slučajeva.

## Karte

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
* U povijesti međuspremnika sustava Windows 11, način pregledavanja bit će
  standardno isključen, kako bi NVDA najavio stavke izbornika unosa
  povijesti međuspremnika. Ovo je sada dio NVDA čitača 2023.1.
* U sustavu Windows 11 22H2 i novijim verzijama, NVDA će najaviti predložene
  radnje kad se kompatibilni podaci poput telefonskih brojeva kopiraju u
  međuspremnik.

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

[1]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps

[2]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-dev

[4]: https://github.com/josephsl/wintenapps/wiki/w10changelog
