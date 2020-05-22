# Windows 10 App Essentials #

* Autori: Joseph Lee, Derek Riemer e altri utenti Windows 10.
* Scarica la [versione stabile][1]
* Scarica la [versione in sviluppo][2]
* NVDA compatibility: 2019.3 to 2020.1

Questo componente aggiuntivo è un insieme di app module per numerose app di
Windows10, che consente anche di risolvere anomalie con alcuni controlli.

Di seguito l'elenco di tutti gli appmodule contenuti nel componente
aggiuntivo, si veda la relativa sezione per ulteriori informazioni:

* Calcolatrice (moderna).
* Calendario
* Cortana (Conversations)
* Posta
* Mappe
* Microsoft Solitaire Collection
* Microsoft Store
* Modern keyboard (emoji panel/dictation/hardware input suggestions/cloud
  clipboard history/modern input method editors)
* Persone
* Impostazioni (Impostazioni Windows, Windows+i)
* Meteo
* Vari moduli per controlli come le mattonelle del menu avvio.

Note:

* This add-on requires Windows 10 Version 1903 (build 18362) or later. For
  best results, use the add-on with latest Windows 10 stable release (build
  18363).
* Alcune caratteristiche di questo componente aggiuntivo sono o diventeranno
  parte di NVDA
* Per le voci non elencate di seguito, si può supporre che son
  caratteristiche già incluse in NVDA, che non sono applicabili dal
  componente in quanto non supporta precedenti versioni di Windows, o che le
  applicazioni son state modificate in modo che le caratteristiche del
  componente non son più applicabili.

Per un elenco delle modifiche riguardo le versioni rilasciate, fare
riferimento al documento [changelogs for add-on releases][3].

## Generale

* NVDA will no longer play error tones or do nothing if this add-on becomes
  active from Windows 7, Windows 8.1, and unsupported releases of Windows
  10.
* In addition to dialogs recognized by NVDA, more dialogs are now recognized
  as proper dialogs and reported as such, including Insider Preview dialog
  (settings app).
* NVDA can announce suggestion count when performing a search in majority of
  cases. This option is controlled by "Report object position information"
  in Object presentation panel found in NVDA settings.
* When searching in Start menu or File Explorer in Version 1909 (November
  2019 Update) and later, instances of NVDA announcing search results twice
  when reviewing results are less noticeable, which also makes braille
  output more consistent when reviewing items.
* The following UIA events are recognized: controller for, drag start, drag
  cancel, drag complete, drag target enter, drag target leave, drag target
  dropped, element selected, item status, live region change, notification,
  system alert, text change, tooltip opened, window opened. With NVDA set to
  run with debug logging enabled, these events will be tracked, and for UIA
  notification event, a debug tone will be heard if notifications come from
  somewhere other than the currently active app.
* It is possible to tracke only specific events and/or events coming from
  specific apps.
* When opening, closing, or switching between virtual desktops, NVDA will
  announce current desktop name (desktop 2, for example).
* NVDA non leggerà più le dimensioni del testo del menu avvio quando si
  cambia la risoluzione dello schermo o orientamento.
* When arranging Start menu tiles or Action Center quick actions with
  Alt+Shift+arrow keys, NVDA will announce information on dragged items or
  new position of the dragged item.
* IN recent releases of Word 365, NVDA will no longer announce "delete back
  word" when pressing Control+Backspace.
* Announcements such as volume/brightness changes in File Explorer and app
  update notifications from Microsoft Store can be suppressed by turning off
  Report Notifications in NVDA's object presentation settings.

## Calcolatrice

* When ENTER or Escape is pressed, NVDA will announce calculation results.
* Per i calcoli quali conversioni di unità di misura o valuta, NVDA leggerà
  il risultato non appena verranno inseriti i dati
* NVDA non annuncerà più il livello di intestazione per i risultati dei
  calcoli.
* NVDA will notify if maximum digit count has been reached while entering
  expressions.
* Added support for always on mode in Calculator version 10.1908 and later.

## Calendario

* Non verrà più letta la dicitura "Modificabile" e  "sola lettura" nel corpo
  del messaggio o in altri campi editazione.

## Cortana

Most items are no longer applicable on Version 1903 and later unless Cortana
Conversations (Version 2004 and later) is in use.

* Textual responses from Cortana are announced in most situations.
* NVDA rimarrà in silenzio mentre si parla a Cortana  con la voce.
* In Version 1909 (November 2019 Update) and later, modern search experience
  in File Explorer powered by Windows Search user interface is supported.

## Posta

* Quando si scorrono le voci nell'elenco messaggi, è possibile utilizzare i
  comandi di navigazione tabella per controllare le intestazioni. Notare che
  la navigazione tra le righe (messaggi) non è supportato.
* Durante la composizione di un messaggio, verranno emessi segnali acustici
  nel caso ci siano dei suggerimenti per menzioni dopo la chiocciola

## Mappe

* NVDA emette dei segnali acustici per le posizioni presenti nella mappa.
* Quando si usa la visualizzazione per strade e l'opzione "utilizza
  tastiera" è attiva, NVDA annuncerà gli indirizzi delle vie mentre si
  scorre la mappa con le frecce.

## Microsoft Solitaire Collection

* NVDA will announce names of cards and card decks.

## Microsoft Store

* Dopo aver controllato la presenza di aggiornamenti di app, i nomi delle
  app nell'elenco degli aggiornamenti viene correttamente etichettato.
* Mentre si scaricano contenuti quali app o film, NVDA ne leggerà il nome e
  l'avanzamento del download.

## Tastiera moderna

This includes emoji panel, clipboard history, dictation, hardware input
suggestions, and modern input method editors for certain languages. When
viewing emojis, for best experience, enable Unicode Consortium setting from
NvDA's speech settings and set symbol level to "some" or higher.

* When opening clipboard history, NVDA will no longer announce "clipboard"
  when there are items in the clipboard under some circumstances.
* On some systems running Version 1903 (May 2019 Update) and later, NVDA
  will no longer appear to do nothing when emoji panel opens.
* Added support for modern Chinese, Japanese, and Korean (CJK) IME
  candidates interface introduced in Version 2004 (build 18965 and later).

## Persone

* Durante la ricerca di contatti, verrà letto il primo suggerimento, in
  particolare se si utilizza le ultime versioni delle app.

## Impostazioni

* Certain information such as Windows Update progress is reported
  automatically, including Storage sense/disk cleanup widget and errors from
  Windows Update.
* Le informazioni delle barre di avanzamento non vengono più lette due
  volte.
* Per alcune caselle combinate o pulsanti radio, NVDA non commetterà più
  errori nel riconoscere le etichette o nell'annunciare i cambiamenti dei
  valori.
* NVDA non riporterà più errori quando si usa  il navigatore ad oggetti in
  alcune situazioni.
* la finestra di notifica per nuovi aggiornamenti windows verrà ora
  visualizzata  correttamente.
* Odd control labels seen in certain Windows 10 installations has been
  corrected.
* In more recent revisions of Version 1803 and later, due to changes to
  Windows Update procedure for feature updates, a "download and install now"
  link has been added. NVDA will now announce the title for the new update
  if present.

## Meteo

* Schede come "previsioni" e "mappe" vengono riconosciute correttamente
  (patch da Derek Riemer). 
* When reading a forecast, use the left and right arrows to move between
  items. Use the up and down arrows to read the individual items. For
  example, pressing the right arrow might report "Monday: 79 degrees, partly
  cloudy, ..." pressing the down arrow will say "Monday" Then pressing it
  again will read the next item (Like the temperature). This currently works
  for daily and hourly forecasts.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
