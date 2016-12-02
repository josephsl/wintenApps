# Windows 10 App Essentials #

* Authors: Joseph Lee, Derek Riemer and other Windows 10 users
* Download [versione stabile][1]
* Download [versione in sviluppo][2]

Questo componente aggiuntivo è un insieme di app module per numerose app
Windows10, e consente anche di risolvere anomalie con alcuni controlli.

Segue l'elenco di tutti gli appmodule contenuti nel componente aggiuntivo,
si veda la relativa sezione per ulteriori informazioni:

* Allarmi e sveglia.
* Bank of America
* Calendar
* Calcolatrice (moderna).
* Cortana
* Mail
* Maps
* Microsoft Edge
* Impostazioni (Impostazioni Windows, Windows+i)
* Anteprima Skype
* Store
* Twitter.
* TeamViewer Touch.
* Weather.
* Vari moduli per controlli come le mattonelle del menu avvio.

Note: this add-on requires Windows 10 Version 1511 (build 10586) or later
and NVDA 2016.3 or later. For best results, use the add-on with latest
stable build (build 14393).

## Generale

* Nei menu di contesto per le mattonelle del menu avvio, vengono
  riconosciuti in maniera corretta i sottomenu.
* Quando vengono ridotte a icona tutte le finestre (Windows+M), non verrà
  più annunciata la parola "riquadro".
* Certain dialogs are now recognized as proper dialogs. This include Insider
  Preview dialog (settings app) and new-style UAC dialog in build 14328 and
  later for NvDA 2016.2.1 or earlier.
* Appearance/close of suggestions for certain search fields (notably
  Settings app) is announced via sounds and/or brailled.
* In certain context menus (such as in Edge), position information (e.g. 1
  of 2) is no longer announced.
* The following UIA events are recognized: Controller for, live region
  changed (handled by name change event).

## Allarmi e sveglia

* I valori per selezionare l'ora adesso vengono annunciati. Questo comprende
  anche la sezione inerente la scelta dell'orario sul quando eseguire
  Windows Update e quando debbano essere installati gli aggiornamenti.

## Calendar and Mail

* NVDA no longer announces "read-only" for appointment subject in Calendar
  and message content in Mail.

## Calcolatrice

* Quando viene premuto invio, NVDA annuncia il risultato del calcolo.

## Cortana

* Le risposte di tipo testuale di Cortana vengono lette nella maggior parte
  dei casi, se non dovesse funzionare riaprire il menu avvio e ripetere la
  ricerca.
* NVDA will be silent when you talk to Cortana via voice.
* NVDA will now announce reminder confirmation after you set one.

## Mail and calendar

* NVDA no longer announces "edit" or "read-only" in message body and other
  fields.

## Maps

* NVDA plays location beep for map locations.

## Microsoft Edge

* Vengono annunciate correttamente le notifiche dei download dei file.
* Si noti che il supporto per il momento è sperimentale, non usare Edge come
  browser predefinito.

## Impostazioni

* Vengono annunciate automaticamente le informazioni di avanzamento delle
  operazioni di Windows Update.
* Le informazioni delle barre di avanzamento non vengono più lette due
  volte.
* If it takes a while to search for settings, NVDA will announce "searching"
  and search result status such as if a setting cannot be found.

## Anteprima Skype

* Viene annunciato quando un utente sta scrivendo, così come accade in Skype
  per desktop.
* Partial return of Control+NvDA+number row commands to read recent chat
  history and to move navigator object to chat entries just like Skype for
  Desktop.
* You can now press Alt+number row to locate and move to contacts list (1),
  conversations (2) and chat edit field (3). Note that one must activate
  these tabs to move to the desired part.
* Combo box labels for Skype preview app released in November 2016 are
  announced.

## Store

* After checking for app updates, app names in list of apps to be updated
  are correctly labeled.

## TeamViewer Touch

* Vengono lette le etichette dei pulsanti radio.
* Lables for buttons are announced.

## Bank of America/Twitter

* Vengono annunciate correttamente le etichette dei pulsanti.

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
