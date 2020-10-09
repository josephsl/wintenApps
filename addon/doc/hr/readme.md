# Osnovni dodaci za Windows 10 aplikacije #

* Autori: Joseph Lee, Derek Riemer u drugi korisnici Windows 10
* Preuzmi [stabilnu verziju][1]
* Preuzmi [razvojnu verziju][2]
* NVDA kompatibilnost: 2020.1 do 2020.3

Ovaj NVDA dodatak je zbirka aplikacijskih modula za razne Windows 10
aplikacije, kao i poboljšanja i ispravci određenih windows 10 kontrola.

Uključeni su sljedeći moduli (za svaku aplikaciju postoji odlomak, gdje piše
što je uključeno):

* Kalkulator (moderan).
* Kalendar
* Cortana (Conversations)
* Pošta
* Karte
* Microsoft Solitaire Collection
* Microsoft Store
* Moderna tipkovnica (ploča emojija, diktatiranje, prijedlozi za ulazni
  hardver, povijest međuspremnika oblaka, moderni uređivači za unos)
* Osobe
* Postavke (postavke sustava, Windows+I)
* Vremenska prognoza.
* Dodatni moduli za kontrole kao što su pločice izbornika Start.

Napomene:

* Za ovaj dodatak potrebna je Windows 10 verzija 1909 (gradnja 18363) ili
  novija. Za najbolje rezultate, koristi dodatak s najnovijim stabilnim
  izdanjem sustava Windows 10 (gradnja 19041).
* Neke funkcije dodatka već jesu ili će postati dio NVDA čitača ekrana.
* Za unose koji niže dolje nisu navedeni, može se pretpostaviti da su te
  funkcije dio NVDA čitača. Više nisu primjenjive jer dodatak ne podržava
  stara izdanja sustava Windows 10 ili su napravljene promjene u sustavu
  Windows 10 i aplikacijama, zbog čega unosi više nisu primjenjivi.

Za popis promjena izvršenih između svakog izdanja dodatka, pogledaj
[dokument s izmjenama izdanja dodatka][3].

## Opće

* NVDA više neće svirati tonove grešaka ili neće raditi ništa, ako se ovaj
  dodatak aktivira u sustavima Windows 7, Windows 8.1 i nepodržanim
  izdanjima sustava Windows 10.
* Većina dijaloških okvira se sada prepoznaju kao pravi dijaloški okviri i o
  njima se izvještava kao takvima, uključujući dijaloški okvir za Insider
  Preview (aplikacija za postavke).
* U većini slučajeva NVDA može najaviti broj prijedloga prilikom
  pretrage. Ova opcija se kontrolira u „Izvijesti o informaciji o položaju
  objekta” u ploči „Prezentacija objekta”.
* Prilikom pretraživanja u izborniku Start ili Exploreru datoteka u verziji
  1909 (nadogradnja studenog 2019.) i novijim, slučajevi gdje NVDA dvaput
  najavljuje rezultate pretrage prilikom pregledavanja rezultata su manje
  uočljivi, čime i izlazna brajica postaje dosljednija prilikom
  pregledavanja stavki.
* Prepoznaju se sljedeći UIA događaji: kontroler za, početak povlačenja,
  prekid povlačenja, povlačenje dovršeno, povlačenje u cilj, povlačenje
  izvan cilja, povlačenje i ispuštanje u cilj, element odabran, stanje
  stavke, promjena regije uživo, obavijest, upozorenje sustava, promjena
  teksta, alatni savjet otvoren, prozor otvoren. Kad se NVDA postavi, tako
  da se pokrene s aktiviranim zapisivanjem grešaka, ti će se događaji
  pratiti. Za UIA događaj obavijesti, ćut će se ton za uklanjanje grešaka,
  ako obavijesti dolaze odnekud drugdje od trenutačno aktivne
  aplikacije. Neki će događaji pružati dodatne informacije kao što su broj
  elemenata u kontroleru za događaj, stanje elementa za događaj promjene
  stanja i tekst stavke za događaj stanja stavke.
* Moguće je pratiti samo određene događaje i-ili događaje koji dolaze iz
  određenih aplikacija.
* NVDA više neće izgledati kao da ništa ne radi ili svirati tonove za
  greške, ako se UIA Id automatizacije za element ne može zabilježiti
  prilikom praćenja događaja.
* Prilikom otvaranja, zatvaranja ili prebacivanja između virtualnih radnih
  površina, NVDA će najaviti trenutačno ime radne površine (na primjer,
  desktop 2).
* NVDA više neće najaviti veličinu teksta izbornika Start, kad se mijenja
  rezolucija ili položaj ekrana.
* Kad se pločice izbornika Start ili brze radnje za Action Center
  raspoređuju s tipkama Alt+šift+strelice, NVDA će najaviti podatke o
  povučenim stavkama ili o novom položaju povučene stavke.
* U nedavnim izdanjima Worda 365, NVDA više neće objavljivati „izbriši
  riječi ispred” pritiskom na kontrol+backspace.
* Najave kao što su promjena glasnoće/svjetline u File Explorereru i
  obavijesti aktualiziranja programa s Microsoft Store stranica, mogu se
  potisnuti isključivanjem opcije „Izvijesti o obavijestima” u NVDA
  postavkama prikaza objekata.
* U verziji 2004. (aktualizirano u svibnju 2020.) i kasnijim verzijama,
  dijalog „Otvori s” najavljuje se kad se otvori.

## Kalkulator

* Kad su tipke enter ili escape pritisnute, NVDA izgovara rezultate
  izračuna.
* Za izračune kao što su pretvaranje jedinica i pretvaranje valuta, NVDA će
  objaviti rezultate čim se pojave.
* NVDA više neće javljati tekst za razinu naslova pri rezultatima izračuna.
* NVDA će obavijestiti kad se dostigne maksimalni broj znamenki tijekom
  unosa izraza.
* Dodana je podrška za modus „uvijek uključen” u Kalkulatoru 10.1908 i
  novijim verzijama.

## Kalendar

* NVDA više ne izgovara „uređivanje” ili „samo za čitanje” u tijelu poruke i
  drugim poljima.

## Cortana

Većina stavki više nije primjenjiva u verzijama 1903 i novijim, ukoliko se
ne koristi Cortana Conversations (verzija 2004 i novije).

* Tekstualni odgovori Cortane najavljuju se u većini slučajeva.
* NVDA neće govoriti kad pričaš sa Cortanom.
* U verziji 1909 (studeni 2019.) i novijim verzijama, podržano je moderno
  pretraživanja u Exploreru datoteka koje pokreće korisničko sučelje Windows
  Search.

## Pošta

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
NVDA postavkama govora i postavi razinu simbola na „neki” ili višu.

* Prilikom otvaranja povijesti međuspremnika, pod nekim okolnostima, NVDA
  više neće objavljivati „međuspremnik” kad se u međuspremniku nalaze
  stavke.
* Na nekim sustavima koji imaju verziju 1903 (nadogradnja svibnja 2019.) i
  noviju, NVDA više neće izgledati kao da ništa ne radi kad se otvori ploča
  s emojijima.
* Dodana je podrška za sučelja suvremenih IME kandidata za kineski, japanski
  i korejski (CJK), uvedena u verziji 2004 (gradnja 18965 i novije).
* Kad se odabere grupa emojija (uključujući kaomoji i skupinu simbola u
  verziji 1903 ili novijoj), NVDA više neće pomicati navigacijski objekt na
  određene emojije.
* NVDA će najaviti odabrane emojije, ako se ploča emojija otvori više puta u
  gradnji 20226.

## Osobe

* Prilikom pretraživanja kontakata najavit će se prvi prijedlog, posebice,
  ako se koriste nedavna izdanja aplikacija.

## Postavke

* O većini informacija, poput trake napredovanja za ažuriranje Windowsa, se
  izvještava automatski.
* Vrijednosti trake napredovanja i druge informacije više se ne najavljuju
  dvaput.
* Za većinu odabirnih okvira i izbornih gumba, NVDA će uspjeti prepoznati
  oznaku i-ili najaviti promjene vrijednosti.
* NVDA više neće izgledati kao da ništa ne radi ili svirati tonove za
  greške, ako se koriste naredbe navigacijskog objekta pod nekim
  okolnostima.
* Dijaloški okvir podsjetnika za ažuriranje Windowsa će se prepoznati kao
  pravi dijaloški okvir.
* Čudne kontrolne oznake viđene u određenim instalacijama sustava Windows 10
  su ispravljene.
* U novijim revizijama verzije 1803 i novije, zbog promjena u postupku
  Windows ažuriranja za ažuriranje funkcija, dodana je poveznica „preuzmi i
  instaliraj sada”. NVDA će sad objaviti naslov nove nadogradnje, ako
  postoji.

## Vremenska prognoza

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
