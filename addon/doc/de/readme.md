# Windows 10 App Essentials #

* Authors: Joseph Lee, Derek Riemer and other Windows 10 users
* [Stabile Version][1] herunterladen
* [Entwicklerversion][2] herunterladen

Diese Erweiterung ist ein Paket von App-Modulen für diverse Windows 10 Apps
sowie Korrekturen in einigen Windows 10 Steuerung.

Die folgenden App-Module oder unterstützte Module für einige Apps sind
inbegriffen (siehen Sie in jeden App-Bereich für Details, um zu sehen,
welche inbegriffen sind):

* Wecker und Uhr.
* Bank of America
* Calendar
* Rechner (modern).
* Cortana
* Mail
* Maps
* Microsoft Edge
* Einstellungen (System-Einstellungen mit Win+I).
* Skype Preview
* Store
* Twitter.
* TeamViewer Touch.
* Weather.
* Diverse Steuermodule wie beispielsweise die Startmenübereiche

Note: this add-on requires Windows 10 Version 1507 (build 10240) or later
and NVDA 2016.3 or later.

## Allgemein

* Im Kontextmenü von Kacheln werden untermenüs korrekt erkannt
* Beim Minimieren aller Anwendungen mit Windows+m wird nicht mehr "Feld"
  angezeigt (betrifft die Insider-Versionen)
* Certain dialogs are now recognized as proper dialogs. This include Insider
  Preview dialog (settings app) and new-style UAC dialog in build 14328 and
  later for NvDA 2016.2.1 or earlier.
* Appearance/close of suggestions for certain search fields (notably
  Settings app) is announced via sounds and/or brailled.
* In certain context menus (such as in Edge), position information (e.g. 1
  of 2) is no longer announced.

## Wecker und Uhr

* Das Steuerelement zum Einstellen der Weckzeit wird nun erkannt. Dies
  betrifft auch das Steuerelement zum Einstellen des geplanten Zeitpunkts
  für einen neustart des Systems nach der Installation von Aktualisierungen
  für Windows.

## Calendar and Mail

* NVDA no longer announces "read-only" for appointment subject in Calendar
  and message content in Mail.

## Rechner

* Wenn Sie die Eingabetaste drücken, wird das Ergebnis der Berechnung
  angesagt.

## Cortana

* Textuelle Antworten von Cortana werden in den meisten Fällen angezeigt
  (falls nicht, öffnen Sie das StartMenü und starten Sie die Suche erneut).
* NVDA will be silent when you talk to Cortana via voice.
* NVDA will now announce reminder confirmation after you set one.

## Mail and calendar

* NVDA no longer announces "edit" or "read-only" in message body and other
  fields.

## Maps

* NVDA plays location beep for map locations.

## Microsoft Edge

* Notifications such as file downloads are now announced.
* Note that overall support is experimental at this point (you should not
  use Edge as your primary browser for a while).

## Einstellungen

* Bestimmte Informationen wie der Fortschritt bei Windows Updates werden nun
  automatisch angesagt.
* Progress bar values and other information are no longer announced twice.
* If it takes a while to search for settings, NVDA will announce "searching"
  and search result status such as if a setting cannot be found.

## Skype Preview

* Typing indicator text is announced just like Skype for Desktop client.
* Partial return of Control+NvDA+number row commands to read recent chat
  history and to move navigator object to chat entries just like Skype for
  Desktop.

## Store

* After checking for app updates, app names in list of apps to be updated
  are correctly labeled.

## TeamViewer Touch

* Beschriftungen für Auswahlschalter werden nun angesagt.
* Lables for buttons are announced.

## Bank of America/Twitter

* Schalterbeschriftungen werden nun angesagt.

## Weather

* Tabs such as "forecast" and "maps" are recognized as proper tabs (patch by
  Derek Riemer).
* when reading a forecast, use the left and right arrows to move between
  items. Use the up and down arrows to read the individual items. For
  example, pressing the right arrow might report "Monday: 79 degrees, partly
  cloudy, ..." pressing the down arrow will say "Monday" Then pressing it
  again will read the next item (Like the temperature). This currently works
  for daily and hourly forecasts.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=w10

[2]: http://addons.nvda-project.org/files/get.php?file=w10-dev
