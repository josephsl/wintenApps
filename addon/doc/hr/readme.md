# Osnovni dodaci za Windows 10 aplikacije #

* Autori: Joseph Lee, Derek Riemer u drugi korisnici Windows 10
* Preuzmi [stabilnu verziju][1]
* Preuzmi [razvojnu verziju][2]
* NVDA compatibility: 2019.3 and beyond

Ovaj NVDA dodatak je zbirka aplikacijskih modula za razne Windows 10
aplikacije, kao i poboljšanja i ispravci određenih windows 10 kontrola.

Uključeni su sljedeći moduli (za svaku aplikaciju postoji odlomak, gdje piše
što je uključeno):

* Kalkulator (moderan).
* Kalendar
* Cortana (Conversations)
* Pošta
* Karte
* Microsoft Store
* Modern keyboard (emoji panel/dictation/hardware input suggestions/cloud
  clipboard history/modern input method editors)
* Osobe
* Postavke (postavke sustava, Windows+I)
* Prognoza
* Dodatni moduli za kontrole kao što su pločice izbornika Start.

Napomene:

* This add-on requires Windows 10 Version 1903 (build 18362) or later. For
  best results, use the add-on with latest Windows 10 stable release (build
  18363).
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
  pratiti. Za UIA događaj obavijesti, čut će se ton za uklanjanje grešaka,
  ako obavijesti dolaze odnekud drugdje od trenutačno aktivne aplikacije.
* Moguće je pratiti samo određene događaje i-ili događaje koji dolaze iz
  određenih aplikacija.
* Prilikom otvaranja, zatvaranja ili prebacivanja između virtualnih radnih
  površina, NVDA će najaviti trenutačno ime radne površine (na primjer,
  desktop 2).
* NVDA više neće najaviti veličinu teksta izbornika Start, kad se mijenja
  rezolucija ili položaj ekrana.
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

Most items are no longer applicable on Version 1903 and later unless Cortana
Conversations (Version 2004 and later) is in use.

* Textual responses from Cortana are announced in most situations.
* NVDA neće govoriti kad pričaš sa Cortanom.
* In Version 1909 (November 2019 Update) and later, modern search experience
  in File Explorer powered by Windows Search user interface is supported.

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

## Microsoft Store

* Nakon provjere nadogradnji aplikacija, aplikacije na popisu koje se
  trebaju nadograditi su pravilno označene.
* Prilikom preuzimanja sadržaja kao što su aplikacije i filmovi, NVDA će
  najaviti naziv proizvoda i traku napredovanja preuzimanja.

## Moderna tipkovnica

This includes emoji panel, clipboard history, dictation, hardware input
suggestions, and modern input method editors for certain languages. When
viewing emojis, for best experience, enable Unicode Consortium setting from
NVDA's speech settings and set symbol level to "Some" or higher.

* When opening clipboard history, NVDA will no longer announce "clipboard"
  when there are items in the clipboard under some circumstances.
* Na nekim sustavima koji imaju verziju 1903 (nadogradnja svibnja 2019.) i
  noviju, NVDA više neće izgledati kao da ništa ne radi kad se otvori ploča
  s emojijima.
* Added support for modern Chinese, Japanese, and Korean (CJK) IME
  candidates interface introduced in Version 2004 (build 18965 and later).

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
