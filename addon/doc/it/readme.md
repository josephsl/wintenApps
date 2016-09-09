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
* Insider Hub/Feedback Hub (solo per utenti Windows Insiders).
* Mail
* Maps
* Microsoft Edge
* Impostazioni (Impostazioni Windows, Windows+i)
* Anteprima Skype
* Twitter.
* TeamViewer Touch.
* Weather.
* Vari moduli per controlli come le mattonelle del menu avvio.

Note: this add-on requires Windows 10 Version 1507 (build 10240) or later
and NVDA 2015.4 or later.

## Generale

* Nei menu di contesto per le mattonelle del menu avvio, vengono
  riconosciuti in maniera corretta i sottomenu.
* Quando vengono ridotte a icona tutte le finestre (Windows+M), non verrà
  più annunciata la parola "riquadro".
* Certain dialogs are now recognized as proper dialogs. This include Insider
  Preview dialog (settings app) and new-style UAC dialog in build 14328 and
  later for NvDA 2016.2.1 or earlier.
* La selezione dei valori dell'orario funziona anche nei sistemi con lingua
  diversa dall'inglese.
* Appearance/close of suggestions for certain search fields (notably
  Settings app) is announced via sounds and/or brailled.

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
* For better experience when talking to Cortana, press Cortana listening
  mode hotkey (Windows+C on Versions 1507 and 1511, Windows+Shift+C in
  version 1607).

## Insider/Feedback Hub e TeamViewer Touch

* Insider Hub (Feedback Hub in Anniversary Update) only: Meant to be used by
  Windows Insiders running an Insider build.
* Vengono lette le etichette dei pulsanti radio.
* TeamViewer Touch: vengono riconosciute le etichette dei pulsanti.

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

## Anteprima Skype

* Viene annunciato quando un utente sta scrivendo, così come accade in Skype
  per desktop.
* Partial return of Control+NvDA+number row commands to read recent chat
  history and to move navigator object to chat entries just like Skype for
  Desktop.

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
