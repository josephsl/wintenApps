# Windows 10 App Essentials #

* Autors: Joseph Lee, Derek Riemer und mehrere Benutzer von Windows 10
* [Stabile Version][1] herunterladen
* [Entwicklerversion][2] herunterladen

Diese Erweiterung ist ein Paket von App-Modulen für diverse Windows 10 Apps
sowie Korrekturen in einigen Windows 10 Steuerung.

Die folgenden App-Module oder unterstützte Module für einige Apps sind
inbegriffen (siehen Sie in jeden App-Bereich für Details, um zu sehen,
welche inbegriffen sind):

* Wecker und Uhr
* Kalender
* Rechner (modern)
* Cortana
* Game Bar
* Mail
* Maps
* Microsoft Edge
* Kontakte
* Settings (system settings, Windows+I)
* Skype (universal app)
* Store
* Wetter
* Diverse Steuermodule wie beispielsweise die Startmenübereiche

Note: this add-on requires Windows 10 Version 1607 (build 14393) or later
and NVDA 2017.3 or later. For best results, use the add-on with latest
Windows 10 stable build (build 16299) and latest stable version of
NVDA. Also, after changing update settings for the add-on, be sure to save
NVDA settings.

Important note about NVDA 2017.3: due to backwards incompatible changes in
NVDA 2017.3, add-on version 17.09 and later will not work on NVDA versions
earlier than 2017.3.

## Allgemein

* Im Kontextmenü von Kacheln werden untermenüs korrekt erkannt
* Certain dialogs are now recognized as proper dialogs. These include
  Insider Preview dialog (settings app) and new-style UAC dialog in build
  14328 and later for NvDA 2016.2.1 or earlier.
* Appearance/close of suggestions for certain search fields (notably
  Settings and Store apps) is announced via sounds and braille. This also
  includes Start menu search box. This is now part of NVDA as of 2017.3.
* NVDA can announce suggestion count when performing a search in majority of
  cases. This option is controlled by "Report object position information"
  in Object presentation dialog.
* In certain context menus (such as in Edge), position information (e.g. 1
  of 2) is no longer announced.
* The following UIA events are recognized: Controller for, live region
  change, system alert, element selected, window opened. With NVDA set to
  run with debug logging enabled, these events will be tracked.
* Added ability to check for add-on updates (automatic or manual) via the
  new Windows 10 App Essentials dialog found in NvDA Preferences menu. By
  default, stable and development versions will check for new updates
  automatically on a weekly or daily basis, respectively.
* Ability to track events coming from Universal Windows Platform (UWP) apps
  if NVDA is run with debug logging enabled.
* Support for floating Emoji input panel in Version 1709 (Fall Creators
  Update). For best experience when reading emojis, use Windows OneCore
  speech synthesizer.
* In some apps, live region text is announced. This includes alerts in Edge,
  results in Calculator and others. Note that this may result in
  double-speaking in some cases. Most of the scenarios are now part of NVDA
  2017.3.
* Toasts are no longer announced multiple times in Creators Update and
  later. This fix is included in NVDA 2017.3.

## Wecker und Uhr

* Time picker values are now announced, noticeable when moving focus to
  picker controls. This also affects the control used to select when to
  restart to finish installing Windows updates.

## Rechner

* When ENTER or Escape is pressed, NVDA announces calculation results.
* For calculations such as unit converter and currency converter, NVDA will
  announce results as soon as calculations are entered.

## calendar

* NVDA no longer announces "edit" or "read-only" in message body and other
  fields.

## Cortana

* Textuelle Antworten von Cortana werden in den meisten Fällen angezeigt
  (falls nicht, öffnen Sie das StartMenü und starten Sie die Suche erneut).
* NVDA verstummt bei der Verwendung von Cortana, so dass die Stimmen nicht
  mehr sich in die Quere kommen.
* NVDA will now announce reminder confirmation after you set one.

## Game Bar

* NVDA will announce appearance of Game Bar window. Due to technical
  limitations, NVDA cannot interact fully with Game Bar.

## Mail

* When reviewing items in messages list, you can now use table navigation
  commands to review message headers.
* When writing a message, appearance of at mention suggestions are indicated
  by sounds.

## Maps

* NVDA plays location beep for map locations.
* When using street side view and if "use keyboard" option is enabled, NVDA
  will announce street addresses as you use arrow keys to navigate the map.

## Microsoft Edge

* Notifications such as file downloads and various webpage alerts are now
  announced. Most of these scenarios are now part of NVDA 2017.3.

## Kontakte

* Wenn nach Kontakten gesucht wird, ertönt bei Erfolg ein Signalton.

## Einstellungen

* Certain information such as Windows Update progress is now reported
  automatically. NVDA itself will handle majority of cases in 2017.3.
* Progress bar values and other information are no longer announced twice.
* If it takes a while to search for settings, NVDA will announce "searching"
  and search result status such as if a setting cannot be found. This is now
  done from NVDA in 2017.3.
* Settings groups are recognized when using object navigation to navigate
  between controls.
* For some combo boxes, NVDA will no longer fail to recognize labels and/or
  announce value changes. Value change fix is included in NVDA 2017.3.

## Skype

* Typing indicator text is announced just like Skype for Desktop client.
* Partial return of Control+NvDA+number row commands to read recent chat
  history and to move navigator object to chat entries just like Skype for
  Desktop.
* You can now press Alt+number row to locate and move to conversations (1),
  contacts list (2), bots (3) and chat edit field if visible (4). Note that
  these commands will work properly if Skype update released in March 2017
  is installed.
* Combo box labels for Skype preview app released in November 2016 are
  announced.
* NVDA will no longer announce "Skype Message" when reviewing messages for
  majority of cases.
* Various issues when using Skype with braille displays fixed, including
  inability to review message history items in braille.
* From message history list, pressing NVDA+D on a message item will now
  allow NVDA to announce detailed information about a message such as
  channel type, sent date and time and so on.

## Store

* After checking for app updates, app names in list of apps to be updated
  are correctly labeled.
* Appearance of search suggestions are now announced. This is now part of
  NVDA 2017.3.
* When downloading content such as apps and movies, NVDA will announce
  product name and download progress. A basic fix is now part of NVDA
  2017.3.

## Wetter

* Tabs such as "forecast" and "maps" are recognized as proper tabs (patch by
  Derek Riemer).
* when reading a forecast, use the left and right arrows to move between
  items. Use the up and down arrows to read the individual items. For
  example, pressing the right arrow might report "Monday: 79 degrees, partly
  cloudy, ..." pressing the down arrow will say "Monday" Then pressing it
  again will read the next item (Like the temperature). This currently works
  for daily and hourly forecasts.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev
