# Windows 10 App Essentials #

* Autori: Joseph Lee, Derek Riemer e altri utenti Windows 10.
* Scarica la [versione stabile][1]
* Scarica la [versione in sviluppo][2]
* NVDA compatibility: 2018.4 to 2019.1

Questo componente aggiuntivo è un insieme di app module per numerose app di
Windows10, che consente anche di risolvere anomalie con alcuni controlli.

Di seguito l'elenco di tutti gli appmodule contenuti nel componente
aggiuntivo, si veda la relativa sezione per ulteriori informazioni:

* Centro attività:
* Allarmi e sveglia.
* Calendario
* Calcolatrice (moderna).
* Cortana
* Centro Feedback
* Posta
* Mappe
* Microsoft Edge
* Tastiera moderna (suggerimenti di immissione per tastiere
  hardware/pannello emoji in Versione 1709 e successive)
* Persone
* Impostazioni (Impostazioni Windows, Windows+i)
* Store
* Meteo
* Vari moduli per controlli come le mattonelle del menu avvio.

Note:

* This add-on requires Windows 10 Version 1803 (build 17134) or later and
  NVDA 2018.4 or later. For best results, use the add-on with latest Windows
  10 stable release (build 17763) and latest stable version of NVDA.
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
* Sono riconosciuti i seguenti eventi UIA: modulo di controllo, inizio
  trascinamento, trascinamento annullato, trascinamento completato, elemento
  selezionato, modifica regione live, notifica, avviso di sistema,
  suggerimento aperto, finestra aperta. Quando NVDA è avviato con il log
  impostato su debug, questi eventi saranno tracciati, e per gli eventi di
  notifiche UIA, verrà emesso un segnale acustico.
* Vengono riconosciuti e annunciati i suggerimenti di Microsoft Edge e
  universal-app.
* Quando si passa ad un desktop virtuale successivo, o viene chiuso o ne
  viene aperto uno, NVDA annuncerà il numero del desktop, ad esempio
  Desktop2, Desktop3, etc.
* NVDA non leggerà più le dimensioni del testo del menu avvio quando si
  cambia la risoluzione dello schermo o orientamento.
* In Version 1903, NVDA will announce volume and brightness changes
  immediately.

## Centro attività:

* Brightness quick action is now a button instead of a toggle button. This
  is now part of NVDA 2019.1.
* Various status changes such as Focus Assist and Brightness will be
  reported. This is now part of NVDA 2019.1.

## Allarmi e sveglia

* Time picker values are now announced, noticeable when moving focus to
  picker controls. This also affects the control used to select when to
  restart to finish installing Windows updates. This is now part of NVDA
  2019.1.

## Calcolatrice

* Quando viene premuto invio o Esc, NVDA annuncia il risultato del calcolo.
* Per i calcoli quali conversioni di unità di misura o valuta, NVDA leggerà
  il risultato non appena verranno inseriti i dati
* NVDA non annuncerà più il livello di intestazione per i risultati dei
  calcoli.
* NVDA will notify if maximum digit count has been reached while entering
  expressions.

## calendario

* Non verrà più letta la dicitura "Modificabile" e  "sola lettura" nel corpo
  del messaggio o in altri campi editazione.

## Cortana

* Le risposte di tipo testuale di Cortana vengono lette nella maggior parte
  dei casi, se non dovesse funzionare riaprire il menu avvio e ripetere la
  ricerca.
* NVDA rimarrà in silenzio mentre si parla a Cortana  con la voce.
* NVDA annuncerà la conferma di un promemoria quando ne viene inserito uno.

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
  app. This is now part of NVDA 2019.1.

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
* Supporto per i suggerimenti di immissione in tastiere hardware nella
  Versione 1803 (aggiornamento Aprile 2018) e successive
* Nella build di windows 10 1709, quando si apre il pannello degli emoji
  verrà letto correttamente il primo emoji selezionato.Questo è più evidente
  nella build 18262 e successive, dove il pannello degli emoji può aprirsi
  sull'ultima categoria usata, come per esempio nella categoria Persone
  verranno visualizzate le espressioni di umore.
* Supporto per la lettura di appunti cloud nella versione 1809 (build 17666
  e successive).
* Ridotto la verbosità quando si utilizzano tastiere moderne con diverse
  caratteristiche. Sono inclusi i lunghi annunci delle nuove interfaccie
  Microsoft all'apertura dei suggerimenti dell'input delle tastiere, e in
  alcuni sistemi non vengono più annunciati i cambiamenti del nome degli
  eventi quando si preme un tasto nella tastiera.
* NVDA will no longer play error tones or do nothing when closing emoji
  panel in more recent 19H1 Insider Preview builds. This will be part of
  NVDA 2019.1.
* In Version 1809 (October 2018 Update) and later, NVDA will announce search
  results for emojis if possible. This will be part of NVDA 2019.1.

## Persone

* Durante la ricerca di contatti, verrà letto il primo suggerimento, in
  particolare se si utilizza le ultime versioni delle app.

## Impostazioni

* Vengono annunciate automaticamente le informazioni di avanzamento delle
  operazioni di Windows Update, incluse informazioni di archiviazione e
  rimozione dal disco di widget.
* Le informazioni delle barre di avanzamento non vengono più lette due
  volte.
* Per alcune caselle combinate o pulsanti radio, NVDA non commetterà più
  errori nel riconoscere le etichette o nell'annunciare i cambiamenti dei
  valori.
* Non vengono più riprodotti beep per le barre di avanzamento del controllo
  volume dalla versioni 1803 e successive.
* Verranno annunciati diversi messaggi sull'aggiornamento di Windows 10, in
  particolare quando Windows Update rileva errori. 
* NVDA non riporterà più errori quando si usa  il navigatore ad oggetti in
  alcune situazioni.
* la finestra di notifica per nuovi aggiornamenti windows verrà ora
  visualizzata  correttamente.
* Odd control labels seen in certain Windows 10 installations has been
  corrected.

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
