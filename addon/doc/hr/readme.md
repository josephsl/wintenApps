# Windows 10 App dodaci #

* Autori: Joseph Lee, Derek Riemer u drugi korisnici Windows 10
* Preuzmi [stabilnu inačicu][1]
* Preuzmi [razvojnu inačicu][2]
* NVDA compatibility: 2018.4 to 2019.2

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
* Pošta
* Karte
* Microsoft Edge
* Modern keyboard (emoji panel/dictation/hardware input suggestions/cloud
  clipboard items in Version 1709 and later)
* Osobe
* Postavke (postavke sustava, Windows+I)
* Trgovina
* Prognoza
* Dodatni moduli za dijelove sustava kao što su to izbornik start i
  pripadajuće mu ikonice

Notes:

* This add-on requires Windows 10 Version 1803 (build 17134) or later and
  NVDA 2018.4 or later. For best results, use the add-on with latest Windows
  10 stable release (build 18362) and latest stable version of NVDA.
* Some add-on features are or will be part of NVDA screen reader.
* For entries not listed below, you can assume that features are part of
  NVDA, no longer applicable as the add-on does not support old Windows 10
  releases, or changes were made to Windows 10 and apps that makes entries
  no longer applicable.

For a list of changes made between each add-on releases, refer to
[changelogs for add-on releases][3] document.

## Općenito

* NVDA will no longer play error tones or do nothing if this add-on becomes
  active from Windows 7, Windows 8.1, and unsupported releases of Windows
  10.
* Submenu items are properly recognized in various apps, including context
  menu for Start menu tiles and microsoft Edge's app menu (Redstone 5).
* In addition to dialogs recognized by NVDA, more dialogs are now recognized
  as proper dialogs and reported as such, including Insider Preview dialog
  (settings app).
* NVDA can announce suggestion count when performing a search in majority of
  cases. This option is controlled by "Report object position information"
  in Object presentation panel found in NVDA settings.
* U većini kontekstnih izbornika (kao što je to u Edgeu), informacije o
  poziciji (NPR. 1 od 2) se više ne izgovara.
* The following UIA events are recognized: active text position change,
  controller for, drag start, drag cancel, drag complete, element selected,
  item status, live region change, notification, system alert, text change,
  tooltip opened, window opened. With NVDA set to run with debug logging
  enabled, these events will be tracked, and for UIA notification event, a
  debug tone will be heard if notifications come from somewhere other than
  the currently active app.
* Tooltips from Edge and universal apps are recognized and will be
  announced.
* When opening, closing, or switching between virtual desktops, NVDA will
  announce current desktop name (desktop 2, for example).
* NVDA will no longer announce Start menu size text when changing screen
  resolutions or orientation.
* In Version 1903 (May 2019 Update), NVDA will announce volume and
  brightness changes immediately.

## Action center

* Brightness quick action is now a button instead of a toggle button. This
  is now part of NVDA 2019.1.
* Various status changes such as Focus Assist and Brightness will be
  reported. This is now part of NVDA 2019.1.

## Alarm i sat

* Time picker values are now announced, noticeable when moving focus to
  picker controls. This also affects the control used to select when to
  restart to finish installing Windows updates. This is now part of NVDA
  2019.1.

## Kalkulator

* Kada je pritisnuta tipka enter, NVDA izgovara rezultate izračuna.
* Za izračune kao što su pretvaranje jedinica i pretvaranje valuta, NVDA će
  izvijestiti o rezultatima čim se isti pojave. 
* NVDA will no longer announce "heading level" for calculator results.
* NVDA will notify if maximum digit count has been reached while entering
  expressions.

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

## Pošta

* When reviewing items in messages list, you can now use table navigation
  commands to review message headers. Note that navigating between rows
  (messages) is not supported.
* Tijekom pisanja poruke, ako spominjete neku osobu, pojavljene sugestije
  bit će popraćene zvukovima. 
* NVDA will no longer do anything or play error tones after closing this
  app. This is now part of NVDA 2019.1.

## Karte

* NVDA reproducira zvuk lokacije za lokacije na mapi.
* Prilikom korištenja prikaza ulice te ako je opcija "korištenje tipkovnice"
  omogućena, NVDA će izgovarati adrese i kućne brojeve prilikom kretanja
  strelicama po mapi.

## Microsoft Edge

* Text auto-complete will be tracked and announced in address omnibar.
* NVDA will no longer play suggestion sound when pressing F11 to toggle full
  screen.

## Modern keyboard

Note: most features below are now part of NVDA 2018.3 or later.

* Support for Emoji input panel in Version 1709 (Fall Creators Update) and
  later, including the redesigned panel in Version 1809 (build 17661 and
  later) and changes made in 19H1 (build 18262 and later, including kaomoji
  and symbols categories in build 18305). If using NVDA releases earlier
  than 2018.4, for best experience when reading emojis, use Windows OneCore
  speech synthesizer. If 2018.4 or later is in use, enable Unicode
  Consortium setting from NvDA's speech settings and set symbol level to
  "some" or higher.
* Support for hardware keyboard input suggestions in Version 1803 (April
  2018 Update) and later.
* In post-1709 builds, NVDA will announce the first selected emoji when
  emoji panel opens. This is more noticeable in build 18262 and later where
  emoji panel may open to last browsed category, such as displaying skin
  tone modifiers when opened to People category.
* Support for announcing cloud clipboard items in Version 1809 (build 17666
  and later).
* Reduced unnecessary verbosity when working with modern keyboard and its
  features. These include no longer announcing "Microsoft Candidate UI" when
  opening hardware keyboard input suggestions and staying silent when
  certain touch keyboard keys raise name change event on some systems.
* NVDA will no longer play error tones or do nothing when closing emoji
  panel in more recent 19H1 Insider Preview builds. This is now part of NVDA
  2019.1.
* In Version 1809 (October 2018 Update) and later, NVDA will announce search
  results for emojis if possible. This is now part of NVDA 2019.1.
* NVDA will no longer announce "clipboard" when there are items in the
  clipboard under some circumstances.
* On some systems running Version 1903 (May 2019 Update), NVDA will no
  longer appear to do nothing when emoji panel opens.

## Osobe

* When searching for contacts, first suggestion will be announced,
  particularly if using recent app releases.

## Postavke

* Certain information such as Windows Update progress is reported
  automatically, including Storage sense/disk cleanup widget and errors from
  Windows Update.
* Vrijednosti trake napredovanja i druge informacije više se ne izgovaraju
  duplo.
* For some combo boxes and radio buttons, NVDA will no longer fail to
  recognize labels and/or announce value changes.
* Audio Volume progress bar beeps are no longer heard in Version 1803 and
  later.
* NVDA will no longer appear to do nothing or play error tones if using
  object navigation commands under some circumstances.
* Windows Update reminder dialog is recognized as a proper dialog.
* Odd control labels seen in certain Windows 10 installations has been
  corrected.

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
