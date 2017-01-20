# Windows 10 App dodaci #

* Autori: Joseph Lee, Derek Riemer u drugi korisnici Windows 10
* Preuzmi [stabilnu inačicu][1]
* Preuzmi [razvojnu inačicu][2]

Ovaj NVDA dodatak je kolekcija različitih skripti za razne Windows 10
aplikacije.

Slijedeće skripte su uključene (pogledajte svaku aplikaciju da biste vidjeli
što je uključeno):

* Alarmi i Sat
* Bank of America
* Kalendar
* kalkulator (moderan).
* Cortana
* Groove Music
* Pošta
* Karte
* Microsoft Edge
* Postavke (Postavke sustava, Windows+I).
* Preview inačica skypea
* Trgovina
* Twitter
* Team viewer za zaslone osjetljive na dodir
* Prognoza
* Windows Defender Security Center (Creators Update and later)
* Dodatni moduli za dijelove sustava kao što su to izbornik start i
  pripadajuće mu ikonice

Napomena: Ovaj dodatak zahtijeva Windows 10 Inačicu 1511 (podverziju 10586)
ili noviju i NVDA 2016.3 ili noviji. Za najbolje rezultate, koristite
dodatak sa posljednjom stabilnom podverzijom (podverzija 14393).

## Općenito

* In context menus for Start Menu tiles, submenus are properly recognized.
* When minimizing windows (Windows+M), "pane" is no longer announced
  (noticeable if using Insider Preview builds).
* Certain dialogs are now recognized as proper dialogs. This include Insider
  Preview dialog (settings app) and new-style UAC dialog in build 14328 and
  later for NvDA 2016.2.1 or earlier.
* Appearance/close of suggestions for certain search fields (notably
  Settings and Store apps) is announced via sounds and/or brailled.
* In certain context menus (such as in Edge), position information (e.g. 1
  of 2) is no longer announced.
* The following UIA events are recognized: Controller for, live region
  changed (handled by name change event).

## Alarms and clock

* Time picker values are now announced, noticeable when moving focus to
  picker controls. This also affects the control used to select when to
  restart to finish installing Windows updates.

## Kalkulator

* Kada je pritisnuta tipka enter, NVDA izgovara rezultate izračuna.

## Cortana

* Textual responses from Cortana are announced in most situations (if it
  doesn't, reopen Start menu and try searching again).
* NVDA will be silent when you talk to Cortana via voice.
* NVDA will now announce reminder confirmation after you set one.

## Groove Music

* Appearance of suggestions when searching for tracks is now detected.

## Mail and calendar

* NVDA no longer announces "edit" or "read-only" in message body and other
  fields.

## Karte

* NVDA plays location beep for map locations.

## Microsoft Edge

* Notifications such as file downloads are now announced.
* Edge support is a work in progress.

## Settings

* Certain information such as Windows Update progress is now reported
  automatically.
* Progress bar values and other information are no longer announced twice.
* If it takes a while to search for settings, NVDA will announce "searching"
  and search result status such as if a setting cannot be found.
* Settings groups are recognized when using object navigation to navigate
  between controls.

## Preview inačica skypea

* Typing indicator text is announced just like Skype for Desktop client.
* Partial return of Control+NvDA+number row commands to read recent chat
  history and to move navigator object to chat entries just like Skype for
  Desktop.
* You can now press Alt+number row to locate and move to contacts list (1),
  conversations (2) and chat edit field (3). Note that one must activate
  these tabs to move to the desired part.
* Combo box labels for Skype preview app released in November 2016 are
  announced.

## Trgovina

* After checking for app updates, app names in list of apps to be updated
  are correctly labeled.
* Appearance of search suggestions are now announced.

## TeamViewer za ekrane osjetljive na dodir

* Natpisi na izbornim gumbima se izgovaraju.
* Oznake na gumbima se izgovaraju.

## Bank of America/Twitter/Windows Defender Security Center

* Oznake na gumbima se sada izgovaraju.
* Windows Defender Security Center (universal app) is included in build
  14986 and later and support for this app from this add-on is subject to
  change.

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

[1]: http://addons.nvda-project.org/files/get.php?file=w10

[2]: http://addons.nvda-project.org/files/get.php?file=w10-dev
