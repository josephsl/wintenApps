# Osnovni dodaci za Windows 10 aplikacije #

* Autori: Joseph Lee, Derek Riemer u drugi korisnici Windows 10
* Preuzmi [stabilnu verziju][1]
* Preuzmi [razvojnu verziju][2]
* NVDA kompatibilnost: 2019.2 do 2019.3

Ovaj NVDA dodatak je zbirka aplikacijskih modula za razne Windows 10
aplikacije, kao i poboljšanja i ispravci određenih windows 10 kontrola.

Uključeni su sljedeći moduli (za svaku aplikaciju postoji odlomak, gdje piše
što je uključeno):

* Kalkulator (moderan).
* Kalendar
* Cortana (Classic i Conversations)
* Feedback Hub
* Pošta
* Karte
* Microsoft Edge
* Microsoft Store
* Moderna tipkovnica (emoji ploča, diktat, prijedlozi za ulazni hardver,
  stavke međuspremnika u oblaku u verziji 1709 i novijoj)
* Osobe
* Postavke (postavke sustava, Windows+I)
* Prognoza
* Dodatni moduli za kontrole kao što su pločice izbornika Start.

Napomene:

* Ovaj dodatak zahtjeva Windows 10 verziju 1809 (gradnja 17763) ili noviju i
  NVDA 2019.2 ili noviju. Najbolje rezultate daje dodatak sa zadnjom
  stabilnom verzijom Windows 10 (gradnja 18363) i zadnjom stabilnom verzijom
  NVDA čitača.
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
* Stavke podizbornika se pravilno prepoznaju u raznim aplikacijama,
  uključujući kontekstni izbornik za pločice izbornika Start i izbornik
  aplikacije Microsoft Edge verzije 1809 (nadogradnja u listopadu 2018.).
* Većina dijaloških okvira se sada prepoznaju kao pravi dijaloški okviri i o
  njima se izvještava kao takvima, uključujući dijaloški okvir za Insider
  Preview (aplikacija za postavke).
* U većini slučajeva NVDA može najaviti broj prijedloga prilikom
  pretrage. Ova opcija se kontrolira u „Izvijesti o informaciji o položaju
  objekta” u ploči „Prezentacija objekta”.
* NVDA više neće najaviti „prazno” kad se pritisne strelica gore ili dolje,
  kojima se otvaraju svi prikazi aplikacija u izborniku Start. Ovo će biti
  ugrađeno u NVDA 2019.3.
* Prilikom pretraživanja u izborniku Start ili Exploreru datoteka u verziji
  1909 (nadogradnja studenog 2019.) i novijim, slučajevi gdje NVDA dvaput
  najavljuje rezultate pretrage prilikom pregledavanja rezultata su manje
  uočljivi, čime i izlazna brajica postaje dosljednija prilikom
  pregledavanja stavki.
* U većini kontekstnih izbornika (kao što je to u Edgeu), informacije o
  poziciji (npr. 1 od 2) se više ne najavljuje.
* Prepoznaju se sljedeći UIA događaji: kontroler za, početak povlačenja,
  prekid povlačenja, povlačenje dovršeno, povlačenje u cilj, povlačenje
  izvan cilja, povlačenje i ispuštanje u cilj, element odabran, stanje
  stavke, promjena regije uživo, obavijest, upozorenje sustava, promjena
  teksta, alatni savjet otvoren, prozor otvoren. Kad se NVDA postavi, tako
  da se pokrene s aktiviranim zapisivanjem grešaka, ti će se događaji
  pratiti. Za UIA događaj obavijesti, čut će se ton za uklanjanje grešaka,
  ako obavijesti dolaze odnekud drugdje od trenutačno aktivne aplikacije.
* Moguće je pratiti samo određene događaje i-ili događaje koji dolaze iz
  određenih aplikacija.
* Alatni savjeti za Edge i univerzalne aplikacije prepoznaju se i bit će
  najavljene. To će biti dio NVDA 2019.3.
* Prilikom otvaranja, zatvaranja ili prebacivanja između virtualnih radnih
  površina, NVDA će najaviti trenutačno ime radne površine (na primjer,
  desktop 2).
* NVDA više neće najaviti veličinu teksta izbornika Start, kad se mijenja
  rezolucija ili položaj ekrana.
* Naziv i verzija za razne Microsoft Store aplikacije se sada ispravno
  prikazuju. Ovo će biti dio NVDA 2019.3.
* Kad se pločice izbornika Start ili brze radnje za Action Center
  raspoređuju s tipkama Alt+Shift+strelice, NVDA će najaviti podatke o
  povučenim stavkama ili o novom položaju povučene stavke.

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

Većina stavki više nije primjenjiva u verzijama 1903 i novijim. Classic
Cortana se odnosi na starije Cortanovo sučelje, koje je bilo dio izbornika
Start.

* U većini slučajeva se tekstualni odgovori Cortane najavljuju (za oba
  sučelja). Ako to nije slučaj, ponovo otvori izbornik Start i ponovi
  pretragu.
* NVDA neće govoriti kad pričaš sa Cortanom.
* U Classic Cortana će NVDA najaviti potvrdu termina, ako je postavljen.
* U verziji 1909 (studeni 2019.) i verziji 20H1 gradnja 18945 i novijim
  verzijama, podržano je moderno pretraživanja u Exploreru datoteka koje
  pokreće korisničko sučelje Windows Search.

## Feedback Hub

* Za novija izdanja aplikacija, NVDA više neće dvaput najaviti kategorije
  povratnih informacija.

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

## Microsoft Edge

Ovo se odnosi na klasični Microsoft Edge, baziran na EdgeHTML-u.

* Automatsko dovršavanje teksta pratit će se i najaviti u višenamjenskoj
  adresnoj traci. To će biti dio NVDA 2019.3.
* NVDA više neće svirati zvuk za prijedloge kad se pritisne F11 za
  uključivanje prikaza preko cijelog ekrana. To će biti dio NVDA 2019.3.
* Uklonjeno je sviranje zvuka za prijedloge za višenamjensku adresnu
  traku. To će biti dio NVDA 2019.3.

## Microsoft Store

* Nakon provjere nadogradnji aplikacija, aplikacije na popisu koje se
  trebaju nadograditi su pravilno označene.
* Prilikom preuzimanja sadržaja kao što su aplikacije i filmovi, NVDA će
  najaviti naziv proizvoda i traku napredovanja preuzimanja.

## Moderna tipkovnica

Većina dolje navedenih funkcija su dio NVDA 2018.3 ili novije verzije.

* Podrška za ploču za unos Emojia u verziji 1709 (Fall Creators nadogradnja)
  i novijoj verziji, uključujući redizajniranu ploču u verziji 1809 (gradnja
  17661 i novije) i promjene izvršene u 19H1 (gradnja 18262 i novije
  verzije, uključujući kategorije kaomoji i simboli u gradnji 18305). Ovo se
  također primjenjuje u gradnji 18963. i novijima, jer je aplikacija
  preimenovana. Ako se koriste NVDA izdanja ranija od 2018.4, za najbolje
  čitanje emojija koristi govornu jedinicu Windows OneCore. Ako se koristi
  2018.4 ili novija, uključi postavku Unicode konzorcija u NVDA postavkama i
  postavi razinu simbola na „poneke” ili višu.
* NVDA više neće objavljivati „međuspremnik” kad se u međuspremniku nalaze
  stavke pod nekim okolnostima.
* Na nekim sustavima koji imaju verziju 1903 (nadogradnja svibnja 2019.) i
  noviju, NVDA više neće izgledati kao da ništa ne radi kad se otvori ploča
  s emojijima.
* Dodana je podrška za sučelja suvremenih IME kandidata za kineski, japanski
  i korejski (CJK), uvedena u 20H1 gradnji 18965 i novijim.

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
* Zvučni signali trake napretka glasnoće zvuka se više ne čuju u verziji
  1803 i novijom. To će biti dio NVDA 2019.3.
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
