# Windows 10 App Essentials #

* Autori: Joseph Lee, Derek Riemer e altri utenti Windows 10.
* Scarica la [versione stabile][1]
* Scarica la [versione in sviluppo][2]
* NVDA compatibility: 2019.1 to 2019.2

Questo componente aggiuntivo è un insieme di app module per numerose app di
Windows10, che consente anche di risolvere anomalie con alcuni controlli.

Di seguito l'elenco di tutti gli appmodule contenuti nel componente
aggiuntivo, si veda la relativa sezione per ulteriori informazioni:

* Calcolatrice (moderna).
* Calendario
* Cortana
* Centro Feedback
* Posta
* Mappe
* Microsoft Edge
* Modern keyboard (emoji panel/dictation/hardware input suggestions/cloud
  clipboard items in Version 1709 and later)
* Persone
* Impostazioni (Impostazioni Windows, Windows+i)
* Store
* Meteo
* Vari moduli per controlli come le mattonelle del menu avvio.

Note:

* This add-on requires Windows 10 Version 1809 (build 17763) or later and
  NVDA 2019.1 or later. For best results, use the add-on with latest Windows
  10 stable release (build 18362) and latest stable version of NVDA.
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
* le Voci di sottomenu vengono correttamente riconosciute in varie
  applicazioni, incluso il menu contestuale per la griglia del menu Start e
  delle apps di Microsoft Edge (Redstone 5).
* In addition to dialogs recognized by NVDA, more dialogs are now recognized
  as proper dialogs and reported as such, including Insider Preview dialog
  (settings app).
* NVDA can announce suggestion count when performing a search in majority of
  cases. This option is controlled by "Report object position information"
  in Object presentation panel found in NVDA settings.
* In alcuni menu di contesto, come in Edge, le informazioni sulla posizione
  come 1 su 2 non vengono più annunciate.
* The following UIA events are recognized: controller for, drag start, drag
  cancel, drag complete, element selected, item status, live region change,
  notification, system alert, text change, tooltip opened, window
  opened. With NVDA set to run with debug logging enabled, these events will
  be tracked, and for UIA notification event, a debug tone will be heard if
  notifications come from somewhere other than the currently active app.
* It is possible to tracke only specific events and/or events coming from
  specific apps.
* Tooltips from Edge and universal apps are recognized and will be
  announced. This will be part of NVDA 2019.3.
* When opening, closing, or switching between virtual desktops, NVDA will
  announce current desktop name (desktop 2, for example).
* NVDA non leggerà più le dimensioni del testo del menu avvio quando si
  cambia la risoluzione dello schermo o orientamento.
* In Version 1903 (May 2019 Update), NVDA will announce volume and
  brightness changes immediately if focused on File Explorer. This is now
  part of NVDA 2019.2.
* App name and version for various universal apps are now shown correctly.

## Calcolatrice

* Quando viene premuto invio o Esc, NVDA annuncia il risultato del calcolo.
* Per i calcoli quali conversioni di unità di misura o valuta, NVDA leggerà
  il risultato non appena verranno inseriti i dati
* NVDA non annuncerà più il livello di intestazione per i risultati dei
  calcoli.
* NVDA will notify if maximum digit count has been reached while entering
  expressions.
* Added support for always on mode in future Calculator releases.

## calendario

* Non verrà più letta la dicitura "Modificabile" e  "sola lettura" nel corpo
  del messaggio o in altri campi editazione.

## Cortana

* Le risposte di tipo testuale di Cortana vengono lette nella maggior parte
  dei casi, se non dovesse funzionare riaprire il menu avvio e ripetere la
  ricerca.
* NVDA rimarrà in silenzio mentre si parla a Cortana  con la voce.
* NVDA annuncerà la conferma di un promemoria quando ne viene inserito uno.
* In build 18945 and later, modern search experience in File Explorer
  powered by Cortana user interface is supported.

## Centro Feedback

* Per le release di nuove app, NVDA non annuncerà più due volte la categoria
  feedback.

## Posta

* Quando si scorrono le voci nell'elenco messaggi, è possibile utilizzare i
  comandi di navigazione tabella per controllare le intestazioni. Notare che
  la navigazione tra le righe (messaggi) non è supportato.
* Durante la composizione di un messaggio, verranno emessi segnali acustici
  nel caso ci siano dei suggerimenti per menzioni dopo la chiocciola
* NVDA will no longer do anything or play error tones after closing this
  app. This is now part of NVDA 2019.2.

## Mappe

* NVDA emette dei segnali acustici per le posizioni presenti nella mappa.
* Quando si usa la visualizzazione per strade e l'opzione "utilizza
  tastiera" è attiva, NVDA annuncerà gli indirizzi delle vie mentre si
  scorre la mappa con le frecce.

## Microsoft Edge

* Monitoraggio e lettura del completamento automatico del testo nelle barre
  degli indirizzi.
* NVDA non riprodurrà più un suono di avviso quando si attiva o disattiva lo
  schermo intero con F11.
* Removed suggestions sound playback for address omnibar.

## Tastiera moderna

Note: most features below are now part of NVDA 2018.3 or later.

* Supporto per l'immissione di emoji nella versione 1709 (Fall creators
  Update) e successive, compreso la nuova interfaccia  del pannello emoji
  nella build 1809 (build 17661 e successive), con aggiornamenti per la 19h1
  (build 18262 e successive, che includono i kaomoji e categorie per i
  simboli nella build 18305).Se si usa una versione precedente a NVDA
  2018.4, per una migliore lettura degli emoji è consigliato usare come
  sintetizzatore vocale le OneCore. Se si usa NVDA 2018.4 o successive,
  attivare la casella di controllo "Includi dati del consorzio Unicode"
  dalle Impostazioni Voce di NVDA, ed impostare il livello di lettura
  simboli/punteggiatura su "Cualcosa" o superiore.
* NVDA will no longer announce "clipboard" when there are items in the
  clipboard under some circumstances.
* On some systems running Version 1903 (May 2019 Update), NVDA will no
  longer appear to do nothing when emoji panel opens.

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
* Non vengono più riprodotti beep per le barre di avanzamento del controllo
  volume dalla versioni 1803 e successive.
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

## Store

* Dopo aver controllato la presenza di aggiornamenti di app, i nomi delle
  app nell'elenco degli aggiornamenti viene correttamente etichettato.
* Mentre si scaricano contenuti quali app o film, NVDA ne leggerà il nome e
  l'avanzamento del download.

## Meteo

* Schede come "previsioni" e "mappe" vengono riconosciute correttamente
  (patch da Derek Riemer). 
* durante la lettura di una previsione, utilizzare le frecce sinistra e
  destra per spostarsi tra gli elementi. Utilizzare le frecce su e giù per
  leggere i singoli elementi. Per esempio, premendo la freccia destra
  potrebbe venir annunciato "lunedì: 29 gradi, parzialmente nuvoloso, ..."
  premendo la freccia giù dirà "lunedì", Quindi premerla di nuovo per
  leggere il prossimo elemento (ad esempio la temperatura). Ciò funziona per
  previsioni orarie e giornaliere.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
