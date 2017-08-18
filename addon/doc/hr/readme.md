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
* Traka za igrice
* Groove Music
* Pošta
* Karte
* Microsoft Edge
* Osobe
* Postavke (postavke sustava, Windows+I)
* Skype (univerzalna aplikacija)
* Trgovina
* Prognoza
* Dodatni moduli za dijelove sustava kao što su to izbornik start i
  pripadajuće mu ikonice

Upozorenje: ovaj dodatak zahtjeva Windows 10 Verziju 1511 (podverziju 10586)
ili noviju i NVDA 2016.4 ili noviji. Za najbolje rezultate, koristite
dodatak sa zadnjom stabilnom inačicom (podverzija 15063) i zadnju stabilnu
inačicu nvda. Također, prilikom spremanja postavki za nadogradnju dodatka,
budite sigurni da ste spremili postavke za NVDA.

Important note about NVDA 2017.3: due to backwards incompatible changes in
NVDA 2017.3, add-on version 17.09 and later will not work on NVDA versions
earlier than 2017.3.

## Općenito

* U kontekstnim izbornicima za pločice početnog izbornika, Podizbornici se
  prepoznaju ispravno.
* Certain dialogs are now recognized as proper dialogs. These include
  Insider Preview dialog (settings app) and new-style UAC dialog in build
  14328 and later for NvDA 2016.2.1 or earlier.
* Appearance/close of suggestions for certain search fields (notably
  Settings and Store apps) is announced via sounds and braille. This also
  includes Start menu search box. This is now part of NVDA as of 2017.3.
* NVDA može čitati broj prijedloga prilikom pretrage u većini slučajeva. Ova
  opcija se kontrolira u "izgovori poziciju objekta" u dijaloškom okviru
  prezentacija objekt.
* U većini kontekstnih izbornika (kao što je to u Edgeu), informacije o
  poziciji (NPR. 1 od 2) se više ne izgovara.
* Slijedeći UIA događaji se izgovaraju: Controller for, live region changed
  (handled by name change event).
* Dodana mogućnost provjere nadogradnje dodatka (ručno ili automatski) preko
  novog win 10 app Essentials u izborniku postavki. Podrazumijevano,
  stabilne i razvojne inačice se provjeravaju na danjoj ili tjednoj bazi.
* Mogućnost praćenja događaja koji dolaze iz  Univerzalnih Windows Platform
  (UWP) aplikacija ako je NVDA sa postavljenim načinom zapisa na debug
  (2017.1 ili noviji).
* Support for floating Emoji input panel in Fall Creators Update (for best
  experience when reading emojis, use Windows OneCore speech synthesizer).
* In some apps, live region text is announced. This includes alerts in Edge,
  results in Calculator and others. Note that this may result in
  double-speaking in some cases. Most of the scenarios are now part of NVDA
  2017.3.
* Toasts are no longer announced multiple times in Creators Update and
  later. This fix is included in NVDA 2017.3.

## Alarm i sat

* Odabirnici vremena se sada izgovaraju, vidljivo prilikom odabira kontrole
  odabirnika. Ovo se također primjenjuje na kontrolu koja utjeće nana odabir
  vremena instalacije Windows nadogradnji.

## Kalkulator

* Kada je pritisnuta tipka enter, NVDA izgovara rezultate izračuna.
* Za izračune kao što su pretvaranje jedinica i pretvaranje valuta, NVDA će
  izvijestiti o rezultatima čim se isti pojave. 

## Kalendar

* NVDA više ne izgovara "uređivanje" ili "samo za čitanje" u tijelu poruke i
  drugim poljima.

## Cortana

* U većini slučajeva tekstualni odgovori Cortane se čitaju, ako to nije
  slučaj, ponovno otvorite izbornik start.
* NVDA će biti tih kada pričate sa Cortanom.
* NVDA će izgovarati potvrdu termina ako ga postavite.

## Traka za igrice

* NVDA će opisati izgled prozora trake za igrice. Zbog tehničkih
  nedostataka, NVDA ne može u potpunosti komunicirati s trakom za igrice.

## Groove Music

* Prisutstvo prijedloga se izgovara prilikom traženja muzičkih numera.

## Pošta

* Prilikom pregleda stavaka u popisu poruka, sada možete koristiti prečice
  za navigaciju po tablicama kako biste pregledali zaglavlja poruke.
* Tijekom pisanja poruke, ako spominjete neku osobu, pojavljene sugestije
  bit će popraćene zvukovima. 

## Karte

* NVDA reproducira zvuk lokacije za lokacije na mapi.
* Prilikom korištenja prikaza ulice te ako je opcija "korištenje tipkovnice"
  omogućena, NVDA će izgovarati adrese i kućne brojeve prilikom kretanja
  strelicama po mapi.

## Microsoft Edge

* Notifications such as file downloads and various webpage alerts are now
  announced. Most of these scenarios are now part of NVDA 2017.3.

## Osobe

* Tijekom pretraživanja kontakata, začut ćete zvuk ako postoje rezultati
  pretrage. 

## Postavke

* Certain information such as Windows Update progress is now reported
  automatically. NVDA itself will handle majority of cases in 2017.3.
* Vrijednosti trake napredovanja i druge informacije više se ne izgovaraju
  duplo.
* If it takes a while to search for settings, NVDA will announce "searching"
  and search result status such as if a setting cannot be found. This is now
  done from NVDA in 2017.3.
* Prupe postavaka se prepoznaju prilikom korištenja objektne navigacije za
  kretanje po elementima.
* For some combo boxes, NVDA will no longer fail to recognize labels and/or
  announce value changes. Value change fix is included in NVDA 2017.3.

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
* Riješeni su različiti problemi pri korištenju Skypea sa brajičnim recima,
  uključujući nemogućnost pregledavanja povijesti poruka na brajici. 
* Ako pritisnete NVDA + D na određenoj poruci u povijesti razgovora, NVDA će
  pročitati detaljne informacije o poruci, kao što su datum I vrijeme slanja
  poruke itd. 

## Trgovina

* poslije provjere nadogradnji aplikacija, aplikacije na popisu koje se
  trebaju nadograditi su pravilno označene.
* Appearance of search suggestions are now announced. This is now part of
  NVDA 2017.3.
* When downloading content such as apps and movies, NVDA will announce
  product name and download progress. A basic fix is now part of NVDA
  2017.3.

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
