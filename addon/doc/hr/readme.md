# Windows 10 App dodaci #

* Autori: Joseph Lee, Derek Riemer u drugi korisnici Windows 10
* Preuzmi [stabilnu inačicu][1]
* Preuzmi [razvojnu inačicu][2]

This add-on is a collection of app modules for various Windows 10 apps, as
well as enhancements and fixes for certain windows 10 controls.

Slijedeće skripte su uključene (pogledajte svaku aplikaciju da biste vidjeli
što je uključeno):

* Alarmi i Sat
* Kalendar
* kalkulator (moderan).
* Cortana
* Traka za igrice
* Pošta
* Karte
* Microsoft Edge
* Modern keyboard (emoji panel/hardware input suggestions in Version 1709
  and later)
* Osobe
* Postavke (postavke sustava, Windows+I)
* Skype (univerzalna aplikacija)
* Trgovina
* Prognoza
* Dodatni moduli za dijelove sustava kao što su to izbornik start i
  pripadajuće mu ikonice

Note: this add-on requires Windows 10 Version 1703 (build 15063) or later
and NVDA 2017.3 or later. For best results, use the add-on with latest
Windows 10 stable build (build 16299) and latest stable version of
NVDA. Also, after changing update settings for the add-on, be sure to save
NVDA settings.

## Općenito

* U kontekstnim izbornicima za pločice početnog izbornika, Podizbornici se
  prepoznaju ispravno.
* Certain dialogs are now recognized as proper dialogs, including Insider
  Preview dialog (settings app).
* NVDA može čitati broj prijedloga prilikom pretrage u većini slučajeva. Ova
  opcija se kontrolira u "izgovori poziciju objekta" u dijaloškom okviru
  prezentacija objekt.
* U većini kontekstnih izbornika (kao što je to u Edgeu), informacije o
  poziciji (NPR. 1 od 2) se više ne izgovara.
* The following UIA events are recognized: Controller for, live region
  change, system alert, element selected, window opened. With NVDA set to
  run with debug logging enabled, these events will be tracked.
* Added ability to check for add-on updates (automatic or manual) via
  Windows 10 App Essentials dialog found in NvDA Preferences menu. By
  default, stable and development versions will check for new updates
  automatically on a weekly or daily basis, respectively.
* In some apps, live region text is announced. This includes alerts in Edge,
  results in Calculator and others. Note that this may result in
  double-speaking in some cases.

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
* NVDA will be silent when talking to Cortana via voice.
* NVDA će izgovarati potvrdu termina ako ga postavite.

## Traka za igrice

* NVDA će opisati izgled prozora trake za igrice. Zbog tehničkih
  nedostataka, NVDA ne može u potpunosti komunicirati s trakom za igrice.

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

* Notifications such as file downloads and various webpage alerts are
  announced.

## Modern keyboard

* Support for floating Emoji input panel in Version 1709 (Fall Creators
  Update). For best experience when reading emojis, use Windows OneCore
  speech synthesizer.
* Support for hardware keyboard input suggestions in build 17040 and later.

## Osobe

* Tijekom pretraživanja kontakata, začut ćete zvuk ako postoje rezultati
  pretrage. 

## Postavke

* Certain information such as Windows Update progress is reported
  automatically.
* Vrijednosti trake napredovanja i druge informacije više se ne izgovaraju
  duplo.
* Prupe postavaka se prepoznaju prilikom korištenja objektne navigacije za
  kretanje po elementima.
* For some combo boxes, NVDA will no longer fail to recognize labels and/or
  announce value changes.
* Audio Volume progress bar beeps are no longer heard in build 17035 and
  later.

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
* When downloading content such as apps and movies, NVDA will announce
  product name and download progress.

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
