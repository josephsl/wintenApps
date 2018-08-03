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
* Feedback Hub
* Traka za igrice
* Pošta
* Karte
* Microsoft Edge
* Modern keyboard (emoji panel/hardware input suggestions/cloud clipboard
  items in Version 1709 and later)
* Osobe
* Postavke (postavke sustava, Windows+I)
* Skype (univerzalna aplikacija)
* Trgovina
* Prognoza
* Dodatni moduli za dijelove sustava kao što su to izbornik start i
  pripadajuće mu ikonice

Notes:

* This add-on requires Windows 10 Version 1709 (build 16299) or later and
  NVDA 2018.2 or later. For best results, use the add-on with latest Windows
  10 stable release (build 17134) and latest stable version of NVDA.
* Some add-on features are or will be part of NVDA screen reader.
* For entries not listed below, you can assume that features are part of
  NVDA, no longer applicable as the add-on does not support old Windows 10
  releases, or changes were made to apps that makes entries no longer
  applicable.

For a list of changes made between each add-on releases, refer to
[changelogs for add-on releases][3] document.

## Općenito

* Submenu items are properly recognized in various apps, including context
  menu for Start menu tiles and microsoft Edge's app menu (Redstone 5).
* Certain dialogs are now recognized as proper dialogs and reported as such,
  including Insider Preview dialog (settings app).
* NVDA can announce suggestion count when performing a search in majority of
  cases. This option is controlled by "Report object position information"
  in Object presentation dialog/panel.
* U većini kontekstnih izbornika (kao što je to u Edgeu), informacije o
  poziciji (NPR. 1 od 2) se više ne izgovara.
* The following UIA events are recognized: active text position change,
  controller for, drag start, drag cancel, drag complete, element selected,
  live region change, notification, system alert, tooltip opened, window
  opened. With NVDA set to run with debug logging enabled, these events will
  be tracked, and for UIA notification event, a debug tone will be heard if
  notifications come from somewhere other than the currently active app.
* Added ability to check for add-on updates (automatic or manual) via
  Windows 10 App Essentials dialog found in NvDA Preferences menu. By
  default, stable and development versions will check for new updates
  automatically on a weekly or daily basis, respectively.
* In some apps, live region text is announced. This includes alerts in Edge
  (including elements marked with aria-role=alert), results in Calculator
  and others. Note that this may result in double-speaking in some cases.
* Notifications from newer app releases on Windows 10 Version 1709 (build
  16299) and later are announced.
* Tooltips from Edge and universal apps are recognized and will be
  announced.
* With Sets turned on (builds 17627 through 17692 for some insiders), when
  opening a new Sets tab (Control+Windows+T), NVDA will announce search
  results when searching for items in the embedded Cortana window.
* With Sets turned on, when switching between Sets tabs, NvDA will announce
  name and position of the tab you are switching to.
* When opening, closing, or switching between virtual desktops, NVDA will
  announce current desktop ID (desktop 2, for example).
* NVDA will no longer announce Start menu size text when changing screen
  resolutions or orientation.

## Alarm i sat

* Odabirnici vremena se sada izgovaraju, vidljivo prilikom odabira kontrole
  odabirnika. Ovo se također primjenjuje na kontrolu koja utjeće nana odabir
  vremena instalacije Windows nadogradnji.

## Kalkulator

* Kada je pritisnuta tipka enter, NVDA izgovara rezultate izračuna.
* Za izračune kao što su pretvaranje jedinica i pretvaranje valuta, NVDA će
  izvijestiti o rezultatima čim se isti pojave. 
* NVDA will no longer announce "heading level" for calculator results.

## Kalendar

* NVDA više ne izgovara "uređivanje" ili "samo za čitanje" u tijelu poruke i
  drugim poljima.

## Cortana

* U većini slučajeva tekstualni odgovori Cortane se čitaju, ako to nije
  slučaj, ponovno otvorite izbornik start.
* NVDA will be silent when talking to Cortana via voice.
* NVDA će izgovarati potvrdu termina ako ga postavite.

## Feedback Hub

* For newer app releases, NVDA will no longer announce feedback categories
  twice.

## Traka za igrice

* NVDA will announce appearance of Game Bar window. Due to technical
  limitations, NVDA cannot interact fully with Game Bar prior to build
  17723.

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

* Notifications such as file downloads and various webpage alerts, as well
  as availability of Reading View (if using Version 1709 and later) are
  announced.

## Modern keyboard

* Support for Emoji input panel in Version 1709 (Fall Creators Update) and
  later, including the redesigned panel in build 17661 and later. For best
  experience when reading emojis, use Windows OneCore speech synthesizer.
* Support for hardware keyboard input suggestions in Version 1803 (April
  2018 Update) and later.
* In post-1709 builds, NVDA will announce the first selected emoji when
  emoji panel opens.
* Support for announcing cloud clipboard items in build 17666 (Redstone 5)
  and later.
* Reduced unnecessary verbosity when working with modern keyboard and its
  features. These include no longer announcing "Microsoft Candidate UI" when
  opening hardware keyboard input suggestions and staying silent when
  certain touch keyboard keys raise name change event on some systems.

## Osobe

* When searching for contacts, first suggestion will be announced,
  particularly if using recent app releases.

## Postavke

* Certain information such as Windows Update progress is reported
  automatically.
* Vrijednosti trake napredovanja i druge informacije više se ne izgovaraju
  duplo.
* Prupe postavaka se prepoznaju prilikom korištenja objektne navigacije za
  kretanje po elementima.
* For some combo boxes, NVDA will no longer fail to recognize labels and/or
  announce value changes.
* Audio Volume progress bar beeps are no longer heard in Version 1803 and
  later.
* More messages about Windows Update status are announced, especially if
  Windows Update encounters errors.

## Skype

* Obavijest prilikom pisanja teksta je je izgovarana kao u skzpeu za radnu
  površinu.
* Control+NvDA+number row commands, used to read recent chat history and to
  move navigator object to chat entries in Skype for Desktop, is also
  available in Skype UWP.
* You can press Alt+number row to locate and move to conversations (1),
  contacts list (2), bots (3) and chat edit field if visible (4). Note that
  these commands will work properly if Skype update released in March 2017
  is installed.
* NVDA više neće izgovarati "skype message" prilikom pregleda poruka u
  većini slučajeva.
* From message history list, pressing NVDA+D on a message item will allow
  NVDA to announce detailed information about a message such as channel
  type, sent date and time and so on.

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

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
