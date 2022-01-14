# Osnovne Windows aplikacije (Windows App Essentials) #

* Autori: Joseph Lee, Derek Riemer i drugi
* Preuzmi [stabilnu verziju][1]
* Preuzmi [razvojnu verziju][2]
* NVDA compatibility: 2021.2 and later

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

* This add-on requires Windows 10 21H1 (build 19043) or later and is
  compatible with Windows 11.
* Mada je instalacija moguća, ovaj dodatak ne podržava izdanja Windows
  Enterprise LTSC (Long-Term Servicing Channel) i Windows Server.
* Neke funkcije dodatka već jesu ili će postati dio NVDA čitača ekrana.
* Za unose koji niže dolje nisu navedeni, može se pretpostaviti da su te
  funkcije dio NVDA čitača. Više nisu primjenjive jer dodatak ne podržava
  stara izdanja sustava poput stare Windows 10 verzije ili su napravljene
  promjene u Windows sustavu i aplikacijama, zbog čega unosi više nisu
  primjenjivi.
* Neke aplikacije podržavaju način kompaktnog preklapanja (na primjer,
  uvijek na vrhu u Kalkulatoru) i ovaj modus neće ispravno raditi s
  prijenosnom verzijom NVDA čitača.

Za popis promjena izvršenih između svakog izdanja dodatka, pogledaj
[dokument s izmjenama izdanja dodatka][3].

## Opće

* U većini slučajeva NVDA može najaviti broj prijedloga prilikom pretrage,
  uključujući kad se broj prijedloga mijenja kako pretraživanje
  napreduje. Ovo je sada dio NVDA 2021.
* Prepoznaju se sljedeći UIA događaji: drag complete, drop target dropped,
  layout invalidated. Kad je razina NVDA dnevnika postavljena na otklanjanje
  grešaka, ti će se događaji pratiti, a za događaj UAIA obavijesti, ton za
  uklanjanje grešaka će se čuti ako obavijesti dolaze s nekog drugog
  trenutačno aktivnog programa. Događaji koji su ugrađeni u NVDA kao što su
  promjena imena i kontroler za događaje prate se iz dodatka nazvanog
  „Praćenje događaja”.
* Prilikom otvaranja, zatvaranja, preraspoređivanja (Windows 11) ili
  prebacivanja između virtualnih radnih površina, NVDA će najaviti
  trenutačno ime radne površine (na primjer, desktop 2).
* NVDA više neće najaviti veličinu teksta izbornika Start, kad se mijenjaju
  rezolucije ili položaj ekrana.
* Kad se pločice izbornika Start ili brze radnje za Action Center
  raspoređuju s tipkama Alt+šift+strelice, NVDA će najaviti podatke o
  povučenim stavkama ili o novom položaju povučene stavke.
* Najave kao što su promjena glasnoće/svjetline u File Explorereru i
  obavijesti aktualiziranja programa s Microsoft Store stranica, mogu se
  potisnuti isključivanjem opcije „Izvijesti o obavijestima” u NVDA
  postavkama prikaza objekata.

## Kalkulator

* NVDA više neće dvaputa najaviti poruku ekrana grafičkog kalkulatora.
* In Windows 10, history and memory list items are properly labeled.

## Cortana

* Tekstualni odgovori Cortane najavljuju se u većini slučajeva.
* NVDA neće govoriti kad pričaš sa Cortanom.

## Mail

* Prilikom pregleda stavaka u popisu poruka, sada možete koristiti prečace
  za navigaciju po tablicama kako biste pregledali zaglavlja poruke.

## Karte

* NVDA svira zvuk za lokacije za lokacije na karti.
* Prilikom korištenja prikaza ulice te ako je opcija „korištenje tipkovnice”
  omogućena, NVDA će izgovarati adrese i kućne brojeve prilikom kretanja
  strelicama po karti.

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

## Notepad

This refers to Windows 11 Notepad version 11 or later.

* NVDA will announce status items such as line and column information when
  report status bar command (NVDA+End in desktop layout, NvDA+Shift+End in
  laptop layout) is performed.
* NVDA will no longer announce entered text when pressing Enter key from the
  document.

## Osobe

* Prilikom pretraživanja kontakata najavit će se prvi prijedlog, posebice,
  ako se koriste nedavna izdanja aplikacija.

## Postavke

* O većini informacija, poput trake napredovanja za ažuriranje Windowsa, se
  izvještava automatski.
* Vrijednosti trake napredovanja i druge informacije više se ne najavljuju
  dvaput.
* Čudne kontrolne oznake viđene u određenim Windows instalacijama su
  ispravljene.
* NVDA će najaviti naziv opcionalne kontrole kvalitete aktualiziranja ako
  postoji (preuzimi i instaliraj poveznicu sada u Windows 10, gumb za
  preuzimanje u Windows 11).
* In Windows 11, breadcrumb bar items are properly recognized.

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
