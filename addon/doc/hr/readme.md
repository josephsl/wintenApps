# Osnovni moduli za Windows 10 aplikacije #

* Autori: Joseph Lee, Derek Riemer u drugi korisnici Windows 10
* Preuzmi [stabilnu verziju][1]
* Preuzmi [razvojnu verziju][2]
* NVDA kompatibilnost: 2020.4 i novije

Ovaj NVDA dodatak je zbirka aplikacijskih modula za razne Windows 10
aplikacije, kao i poboljšanja i ispravci određenih windows 10 kontrola.

Uključeni su sljedeći moduli (za svaku aplikaciju postoji odlomak, gdje piše
što je uključeno):

* Kalkulator (moderan)
* Kalendar
* Cortana (konverzacije)
* Mail
* Karte
* Microsoft Solitaire Collection
* Microsoft Store
* Moderna tipkovnica (ploča emojija, diktatiranje, prijedlozi za ulazni
  hardver, povijest međuspremnika, moderni uređivači za unos)
* Osobe
* Postavke (postavke sustava, Windows+I)
* Vrijeme
* Dodatni moduli za kontrole kao što su pločice izbornika Start

Napomene:

* This add-on requires Windows 10 Version 2004 (build 19041) or later. For
  best results, use the add-on with latest Windows release (Windows 10
  Version 21H1/build 19043).
* Although installation is possible, this add-on does not support Windows
  Enterprise LTSC (Long-Term Servicing Channel) and Windows Server releases.
* Neke funkcije dodatka već jesu ili će postati dio NVDA čitača ekrana.
* For entries not listed below, you can assume that features are part of
  NVDA, no longer applicable as the add-on does not support older Windows
  releases, or changes were made to Windows and apps that makes entries no
  longer applicable.
* Neke aplikacije podržavaju način kompaktnog preklapanja (na primjer,
  uvijek na vrhu u Kalkulatoru) i ovaj modus neće ispravno raditi s
  prijenosnom verzijom NVDA čitača.

Za popis promjena izvršenih između svakog izdanja dodatka, pogledaj
[dokument s izmjenama izdanja dodatka][3].

## Opće

* U većini slučajeva NVDA može najaviti broj prijedloga prilikom
  pretrage. Ova opcija se kontrolira u „Izvijesti o informaciji o položaju
  objekta” u ploči „Prezentacija objekta”.
* Prilikom pretraživanja u izborniku Start ili Exploreru datoteka u verziji
  1909 (nadogradnja studenog 2019.) i novijim, slučajevi gdje NVDA dvaput
  najavljuje rezultate pretrage prilikom pregledavanja rezultata su manje
  uočljivi, čime i izlazna brajica postaje dosljednija prilikom
  pregledavanja stavki.
* Prepoznaju se sljedeći UIA događaji: drag start, drag cancel, drag
  complete, drop target drag enter, drop target drag leave, drop target
  dropped. Kad je razina NVDA dnevnika postavljena na otklanjanje grešaka,
  ti će se događaji pratiti. Za obavijesti UIA događaja, ćut će se ton za
  otklanjanje grešaka, ako obavijesti dolaze odnekud drugdje od trenutačno
  aktivne aplikacije. Neki će događaji pružati dodatne informacije kao što
  su broj elemenata u kontroleru za događaj, stanje elementa za događaj
  promjene stanja i tekst stavke za događaj stanja stavke.
* Moguće je pratiti samo određene događaje i-ili događaje koji dolaze iz
  određenih aplikacija.
* Prilikom otvaranja, zatvaranja, preraspoređivanja (gradnja 21337 ili
  novija) ili prebacivanja između virtualnih radnih površina, NVDA će
  najaviti trenutačno ime radne površine (na primjer, desktop 2).
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

## Kalendar

* NVDA više ne najavljuje „uređivanje” ili „samo za čitanje” u sadržaju
  poruke i drugim poljima.

## Cortana

Većina stavki je primjenjiva kad se koristi Cortana konverzacije (verzija
2004 i novija).

* Tekstualni odgovori Cortane najavljuju se u većini slučajeva.
* NVDA neće govoriti kad pričaš sa Cortanom.
* U verziji 1909 (studeni 2019.) i novijim verzijama, podržano je moderno
  pretraživanja u Exploreru datoteka koje pokreće korisničko sučelje Windows
  Search.

## Mail

* Prilikom pregleda stavaka u popisu poruka, sada možete koristiti prečace
  za navigaciju po tablicama kako biste pregledali zaglavlja poruke.
* Tijekom pisanja poruke, ako spominjete neku osobu, pojavljeni prijedlozi
  bit će naznačeni zvukovima.

## Karte

* NVDA svira zvuk za lokacije za lokacije na karti.
* Prilikom korištenja prikaza ulice te ako je opcija „korištenje tipkovnice”
  omogućena, NVDA će izgovarati adrese i kućne brojeve prilikom kretanja
  strelicama po karti.

## Microsoft Solitaire Collection

* NVDA će najaviti imenta karata i setove karata.

## Microsoft Store

* Nakon provjere nadogradnji aplikacija, aplikacije na popisu koje se
  trebaju nadograditi su pravilno označene.
* Prilikom preuzimanja sadržaja kao što su aplikacije i filmovi, NVDA će
  najaviti naziv proizvoda i traku napredovanja preuzimanja.

## Moderna tipkovnica

To uključuje ploču s emojijima, povijest međuspremnika, diktatiranje,
prijedloge unosa hardvera i moderne uređivače načina unosa za određene
jezike. Kad pregledavaš emojije, aktiviraj postavku Unicode Consortium u
NVDA postavkama govora i postavi razinu simbola na „neki” ili višu. Također,
NVDA podržava aktualiziranu ploču unosa u gradnji 21296 i novijoj.

* Prilikom otvaranja povijesti međuspremnika, pod nekim okolnostima, NVDA
  više neće objavljivati „međuspremnik” kad se u međuspremniku nalaze
  stavke.
* Na nekim sustavima koji imaju verziju 1903 (nadogradnja svibnja 2019.) i
  noviju, NVDA više neće izgledati kao da ništa ne radi kad se otvori ploča
  s emojijima.
* Kad se odabere grupa emojija (uključujući kaomoji i skupinu simbola u
  verziji 1903 ili novijoj), NVDA više neće pomicati navigacijski objekt na
  određene emojije.
* Dodana je podrška za aktualiziranu ploču unosa (kombinacija ploče emojija
  i povijesti međuspremnika) u gradnji 21296 i novijoj.

## Osobe

* Prilikom pretraživanja kontakata najavit će se prvi prijedlog, posebice,
  ako se koriste nedavna izdanja aplikacija.

## Postavke

* O većini informacija, poput trake napredovanja za ažuriranje Windowsa, se
  izvještava automatski.
* Vrijednosti trake napredovanja i druge informacije više se ne najavljuju
  dvaput.
* Dijaloški okvir podsjetnika za ažuriranje Windowsa će se prepoznati kao
  pravi dijaloški okvir.
* Odd control labels seen in certain Windows installations has been
  corrected.
* U novijim revizijama verzije 1803 i novije, zbog promjena u postupku
  Windows ažuriranja za ažuriranje funkcija, dodana je poveznica „preuzmi i
  instaliraj sada”. NVDA će sad objaviti naslov nove nadogradnje, ako
  postoji.

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
