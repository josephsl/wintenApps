# Windows 10 App dodaci #

* Autori: Joseph Lee, Derek Riemer u drugi korisnici Windows 10
* Preuzmi [stabilnu inačicu][1]
* Preuzmi [razvojnu inačicu][2]

Ovaj NVDA dodatak je kolekcija različitih skripti za razne Windows 10
aplikacije.

Slijedeće skripte su uključene (pogledajte svaku aplikaciju da biste vidjeli
što je uključeno):

* Alarmi i Sat
* Kalendar
* kalkulator (moderan).
* Cortana
* Groove Music
* Pošta
* Karte
* Microsoft Edge
* People
* Postavke (postavke sustava, Windows+I)
* Skype (univerzalna aplikacija)
* Trgovina
* Prognoza
* Dodatni moduli za dijelove sustava kao što su to izbornik start i
  pripadajuće mu ikonice

Note: this add-on requires Windows 10 Version 1511 (build 10586) or later
and NVDA 2017.1 or later. For best results, use the add-on with latest
stable build (build 15063) and latest stable version of NVDA. Also, after
changing update settings for the add-on, be sure to save NVDA settings.

## Općenito

* U kontekstnim izbornicima za pločice početnog izbornika, Podizbornici se
  prepoznaju ispravno.
* Većina dijaloških okvir sada se prepoznaje kao pravi dijaloški okviri. Ovo
  ukljućuje dijaloški okvir insider preview (aplikacija postavke) to
  ukljućuje i novi dijaloški okvir kontrole korisničkog računa u buildu
  14328 i noviji za NVDA 2016.2.1 i ranije.
* Izgled/zatvaranje prijedloga za većinu uređivačkih polja (vidljivo u
  Postavkama i Trgovini) se izgovara putem zvuka i brajice.. to također
  ukljućuje polje pretrage u izborniku start.
* NVDA može čitati broj prijedloga prilikom pretrage u većini slučajeva. Ova
  opcija se kontrolira u "izgovori poziciju objekta" u dijaloškom okviru
  prezentacija objekt.
* U većini kontekstnih izbornika (kao što je to u Edgeu), informacije o
  poziciji (NPR. 1 od 2) se više ne izgovara.
* The following UIA events are recognized: Controller for, live region
  changed, system alert.
* Dodana mogućnost provjere nadogradnje dodatka (ručno ili automatski) preko
  novog win 10 app Essentials u izborniku postavki. Podrazumijevano,
  stabilne i razvojne inačice se provjeravaju na danjoj ili tjednoj bazi.
* Ability to track events coming from Universal Windows Platform (UWP) apps
  if NVDA is run with debug logging enabled.
* Initial support for floating Emoji input panel in build 16215 or later
  (for best results, use Windows OneCore speech synthesizer).

## Alarm i sat

* Odabirnici vremena se sada izgovaraju, vidljivo prilikom odabira kontrole
  odabirnika. Ovo se također primjenjuje na kontrolu koja utjeće nana odabir
  vremena instalacije Windows nadogradnji.

## Kalkulator

* When ENTER or Escape is pressed, NVDA announces calculation results.

## Kalendar

* NVDA više ne izgovara "uređivanje" ili "samo za čitanje" u tijelu poruke i
  drugim poljima.

## Cortana

* U većini slučajeva tekstualni odgovori Cortane se čitaju, ako to nije
  slučaj, ponovno otvorite izbornik start.
* NVDA će biti tih kada pričate sa Cortanom.
* NVDA će izgovarati potvrdu termina ako ga postavite.

## Groove Music

* Prisutstvo prijedloga se izgovara prilikom traženja muzičkih numera.

## Pošta

* Prilikom pregleda stavaka u popisu poruka, sada možete koristiti prečice
  za navigaciju po tablicama kako biste pregledali zaglavlja poruke.
* When writing a message, appearance of at mention suggestions are indicated
  by sounds.

## Karte

* NVDA reproducira zvuk lokacije za lokacije na mapi.
* Prilikom korištenja prikaza ulice te ako je opcija "korištenje tipkovnice"
  omogućena, NVDA će izgovarati adrese i kućne brojeve prilikom kretanja
  strelicama po mapi.

## Microsoft Edge

* Notifications such as file downloads and various webpage alerts are now
  announced.
* U nadogradnji za tvorce, NVDA više neće izgovarati "WebRuntime Content
  View" prilikom prebacivanja na drugi prikaz.

## People

* When searching for contacts, a sound will play if there are search
  results.

## Postavke

* Većina informacija poput Windows Update trake napredovanja  izgovaraju se
  automatski.
* Vrijednosti trake napredovanja i druge informacije više se ne izgovaraju
  duplo.
* Ako je potrebno duže vremena traženja postavki, NVDA će izgovoriti
  "traženje" i stanje rezultata pretrage kao što je to na primjer
  nemogučnost pronalaska dane opcije.
* Prupe postavaka se prepoznaju prilikom korištenja objektne navigacije za
  kretanje po elementima.
* Za većinu odabirnih okvira, NVDA više neće neuspjevati prepoznavati lznaku
  i-ili promjenu vrijednosti.

## Skype

* Obavijest prilikom pisanja teksta je je izgovarana kao u skzpeu za radnu
  površinu.
* Djelomičan povratak prečaca  Control+NvDA+gornji numerički red za čitanje
  zadnje povijesti poruka i za premještanje objekta navigatora na popis
  poruka kao i u skypeu za radnu površinu.
* Sada možete pritisnuti Alt+brojčani red kako biste locirali i prebacivali
  se između razgovora (1), popis kontakata (2), botova (3) i i polja za upis
  poruke u čavrljanju, ako je vidljivo (4). Imajte na umu, da će ovi prečaci
  raditi samo sa instaliranim ažuriranjem izdanom u ožujku 2017.
* oznake odabirnih okvira za Skype preview app objavljenu u studenom 2016 se
  izgovaraju.
* NVDA više neće izgovarati "skype message" prilikom pregleda poruka u
  većini slučajeva.
* Various issues when using Skype with braille displays fixed, including
  inability to review message history items in braille.
* From message history list, pressing NVDA+D on a message item will now
  allow NVDA to announce detailed information about a message such as
  channel type, sent date and time and so on.

## Trgovina

* poslije provjere nadogradnji aplikacija, aplikacije na popisu koje se
  trebaju nadograditi su pravilno označene.
* Sada se izgovaraju prijedlozi pretrage.
* Prilikom preuzimanja sadržaja kao što su to aplikacije i filmovi, NVDA će
  izgovarati naziv proizvoda i traku napredovanja.

## Prognoza

* Kartice svojstava poput "prognoza" i "karte" prepoznaju se kao ispravne
  kartice svojstava (patch napravio Derek Riemer).
* Prilikom čitanja prognoze, pritišćite strelice kako biste se kretali
  između stavaka. pritišćite gornju ili dolnju strelicu kako biste se
  premještali između individualnih stavaka. Na primjer, pritisak desne
  strelice može izgovorit "Ponedjeljak: 79 stupnjeva, djelomično oblačno,
  ..." pritiskom na strelicu dolje će izgovoriti "Ponedjeljak" potom
  pritišćući još jedamput pročitati će slijedeću stavku (poput
  temperature). Ovo trenutno radi za dnevnu i svakosatnu vremensku prognozu.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev
