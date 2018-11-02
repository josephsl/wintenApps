# Windows 10 App dodaci #

* Autori: Joseph Lee, Derek Riemer u drugi korisnici Windows 10
* Preuzmi [stabilnu inačicu][1]
* Preuzmi [razvojnu inačicu][2]

This add-on is a collection of app modules for various Windows 10 apps, as
well as enhancements and fixes for certain windows 10 controls.

Slijedeće skripte su uključene (pogledajte svaku aplikaciju da biste vidjeli
što je uključeno):

* Action center
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
  NVDA 2018.3 or later. For best results, use the add-on with latest Windows
  10 stable release (build 17134) and latest stable version of NVDA. Note
  that until further notice, Version 1809 (build 17763) is not available
  from Microsoft.
* Some add-on features are or will be part of NVDA screen reader.
* For entries not listed below, you can assume that features are part of
  NVDA, no longer applicable as the add-on does not support old Windows 10
  releases, or changes were made to apps that makes entries no longer
  applicable.

For a list of changes made between each add-on releases, refer to
[changelogs for add-on releases][3] document.

## Općenito

* If Add-on Updater add-on is installed, that add-on will check for Windows
  10 App Essentials updates.
* Default update check interval has changed to weekly checks for both stable
  and development releases. This is applicable if the add-on itself checks
  for updates.
* Submenu items are properly recognized in various apps, including context
  menu for Start menu tiles and microsoft Edge's app menu (Redstone 5).
* Certain dialogs are now recognized as proper dialogs and reported as such,
  including Insider Preview dialog (settings app). This is now part of NVDA
  2018.3.
* NVDA can announce suggestion count when performing a search in majority of
  cases. This option is controlled by "Report object position information"
  in Object presentation dialog/panel.
* U većini kontekstnih izbornika (kao što je to u Edgeu), informacije o
  poziciji (NPR. 1 od 2) se više ne izgovara.
* The following UIA events are recognized: active text position change,
  controller for, drag start, drag cancel, drag complete, element selected,
  item status, live region change, notification, system alert, tooltip
  opened, window opened. With NVDA set to run with debug logging enabled,
  these events will be tracked, and for UIA notification event, a debug tone
  will be heard if notifications come from somewhere other than the
  currently active app.
* Notifications from newer app releases on Windows 10 Version 1709 (build
  16299) and later are announced. NVDA 2018.2 and later supports this, with
  2018.3 adding support for more notifications.
* Tooltips from Edge and universal apps are recognized and will be
  announced.
* When opening, closing, or switching between virtual desktops, NVDA will
  announce current desktop ID (desktop 2, for example).
* NVDA will no longer announce Start menu size text when changing screen
  resolutions or orientation.

## Action center

* Brightness quick action is now a button instead of a toggle button.
* Various status changes such as Focus Assist and Brightness will be
  reported.

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

* When reviewing items in messages list, you can now use table navigation
  commands to review message headers. Note that navigating between rows
  (messages) is not supported.
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
* Text auto-complete will be tracked and announced in address omnibar.

## Modern keyboard

Note: most features below are now part of NVDA 2018.3.

* Support for Emoji input panel in Version 1709 (Fall Creators Update) and
  later, including the redesigned panel in Version 1809 (build 17661 and
  later) and changes made in 19H1 (build 18262). For best experience when
  reading emojis, use Windows OneCore speech synthesizer.
* Support for hardware keyboard input suggestions in Version 1803 (April
  2018 Update) and later.
* In post-1709 builds, NVDA will announce the first selected emoji when
  emoji panel opens. This is more noticeable in build 18262 and later where
  emoji panel may open to last browsed category, such as displaying skin
  tone modifier when opened to People category.
* Support for announcing cloud clipboard items in Version 1809 (build 17666
  and later).
* Reduced unnecessary verbosity when working with modern keyboard and its
  features. These include no longer announcing "Microsoft Candidate UI" when
  opening hardware keyboard input suggestions and staying silent when
  certain touch keyboard keys raise name change event on some systems.
* NVDA will no longer play error tones or do nothing when closing emoji
  panel in more recent Insider Preview builds.

## Osobe

* When searching for contacts, first suggestion will be announced,
  particularly if using recent app releases.

## Postavke

* Certain information such as Windows Update progress is reported
  automatically, including Storage sense/disk cleanup widget.
* Vrijednosti trake napredovanja i druge informacije više se ne izgovaraju
  duplo.
* Prupe postavaka se prepoznaju prilikom korištenja objektne navigacije za
  kretanje po elementima.
* For some combo boxes and radio buttons, NVDA will no longer fail to
  recognize labels and/or announce value changes.
* Audio Volume progress bar beeps are no longer heard in Version 1803 and
  later.
* More messages about Windows Update status are announced, especially if
  Windows Update encounters errors.

## Skype

Note: the below entries won't work properly in Skype 14 universal app.

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
