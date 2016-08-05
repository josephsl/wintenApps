# Windows 10 App Essentials #

* Autore: Joseph Lee
* Download [versione stabile][1]
* Download [versione in sviluppo][2]

Questo componente aggiuntivo è un insieme di app module per numerose app
Windows10, e consente anche di risolvere anomalie con alcuni controlli.

Segue l'elenco di tutti gli appmodule contenuti nel componente aggiuntivo,
si veda la relativa sezione per ulteriori informazioni:

* Allarmi e sveglia.
* Bank of America
* Calcolatrice (moderna).
* Cortana
* Insider Hub/Feedback Hub (solo per utenti Windows Insiders).
* Microsoft Edge
* Impostazioni (Impostazioni Windows, Windows+i)
* Anteprima Skype
* Twitter.
* TeamViewer Touch.
* Vari moduli per controlli come le mattonelle del menu avvio.

## Generale

* Nei menu di contesto per le mattonelle del menu avvio, vengono
  riconosciuti in maniera corretta i sottomenu.
* Quando vengono ridotte a icona tutte le finestre (Windows+M), non verrà
  più annunciata la parola "riquadro".
* Molte finestre di dialogo vengono gestite correttamente, soprattutto
  quelle inerenti il feedback su Windows Insider e le impostazioni, nonché i
  nuovi controlli UAC presenti dalla build 14328 e successive.
* La selezione dei valori dell'orario funziona anche nei sistemi con lingua
  diversa dall'inglese.

## Allarmi e sveglia

* I valori per selezionare l'ora adesso vengono annunciati. Questo comprende
  anche la sezione inerente la scelta dell'orario sul quando eseguire
  Windows Update e quando debbano essere installati gli aggiornamenti.

## Calcolatrice

* Quando viene premuto invio, NVDA annuncia il risultato del calcolo.

## Cortana

* Le risposte di tipo testuale di Cortana vengono lette nella maggior parte
  dei casi, se non dovesse funzionare riaprire il menu avvio e ripetere la
  ricerca.

## Insider/Feedback Hub e TeamViewer Touch

* Insider Hub (Feedback Hub in Anniversary Update) only: Meant to be used by
  Windows Insiders running an Insider build.
* Vengono lette le etichette dei pulsanti radio.
* TeamViewer Touch: vengono riconosciute le etichette dei pulsanti.

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

## Bank of America/Twitter

* Vengono annunciate correttamente le etichette dei pulsanti.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=w10

[2]: http://addons.nvda-project.org/files/get.php?file=w10-dev
