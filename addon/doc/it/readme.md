# Windows 10 App Essentials #

* Autori: Joseph Lee, Derek Riemer e altri utenti Windows 10.
* Download [versione stabile][1]
* Download [versione in sviluppo][2]

Questo componente aggiuntivo è un insieme di app module per numerose app
Windows10, e consente anche di risolvere anomalie con alcuni controlli.

Segue l'elenco di tutti gli appmodule contenuti nel componente aggiuntivo,
si veda la relativa sezione per ulteriori informazioni:

* Allarmi e sveglia.
* Bank of America
* Calendario
* Calcolatrice (moderna).
* Cortana
* Groove Music
* Posta
* Mappe
* Microsoft Edge
* Impostazioni (Impostazioni Windows, Windows+i)
* Anteprima Skype
* Store
* Twitter.
* TeamViewer Touch.
* Meteo
* Windows Defender Security Center (Creators Update and later)
* Vari moduli per controlli come le mattonelle del menu avvio.

Nota: questo add-on richiede  Windows 10 Versione 1511 (build 10586) o
successive e NVDA 2016.3 o successive. Per avere le prestazioni migliori,
utilizzare il componente aggiuntivo con l'ultima build stabile (build
14393).

## Generale

* Nei menu di contesto per le mattonelle del menu avvio, vengono
  riconosciuti in maniera corretta i sottomenu.
* Quando vengono ridotte a icona tutte le finestre (Windows+M), non verrà
  più annunciata la parola "riquadro".
* Certain dialogs are now recognized as proper dialogs. This include Insider
  Preview dialog (settings app) and new-style UAC dialog in build 14328 and
  later for NvDA 2016.2.1 or earlier.
* Appearance/close of suggestions for certain search fields (notably
  Settings and Store apps) is announced via sounds and/or brailled.
* In certain context menus (such as in Edge), position information (e.g. 1
  of 2) is no longer announced.
* The following UIA events are recognized: Controller for, live region
  changed (handled by name change event).

## Allarmi e sveglia

* I valori per selezionare l'ora adesso vengono annunciati. Questo comprende
  anche la sezione inerente la scelta dell'orario sul quando riavviare per
  terminare gli aggiornamenti di Windows Update

## Calcolatrice

* Quando viene premuto invio, NVDA annuncia il risultato del calcolo.

## Cortana

* Le risposte di tipo testuale di Cortana vengono lette nella maggior parte
  dei casi, se non dovesse funzionare riaprire il menu avvio e ripetere la
  ricerca.
* NVDA will be silent when you talk to Cortana via voice.
* NVDA will now announce reminder confirmation after you set one.

## Groove Music

* Appearance of suggestions when searching for tracks is now detected.

## Mail and calendar

* Insider Hub (centro di supporto in Anniversary Update): solo per quegli
  utenti che usano una versione Insider di Windows, servendosi del centro
  Feedback Insider per aggiornamenti.

## Mappe

* NVDA plays location beep for map locations.

## Microsoft Edge

* Vengono annunciate correttamente le notifiche dei download dei file.
* Edge support is a work in progress.

## Impostazioni

* Vengono annunciate automaticamente le informazioni di avanzamento delle
  operazioni di Windows Update.
* Le informazioni delle barre di avanzamento non vengono più lette due
  volte.
* If it takes a while to search for settings, NVDA will announce "searching"
  and search result status such as if a setting cannot be found.
* Settings groups are recognized when using object navigation to navigate
  between controls.

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
* Appearance of search suggestions are now announced.

## TeamViewer Touch

* Vengono lette le etichette dei pulsanti radio.
* Vengono lette le etichette dei pulsanti.

## Bank of America/Twitter/Windows Defender Security Center

* Vengono annunciate correttamente le etichette dei pulsanti.
* Windows Defender Security Center (universal app) is included in build
  14986 and later and support for this app from this add-on is subject to
  change.

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
