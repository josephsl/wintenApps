# Windows 10 App Essentials #

* Autori: Joseph Lee, Derek Riemer e altri utenti Windows 10.
* Scarica la [versione stabile][1]
* Scarica la [versione in sviluppo][2]
* Compatibilità con NVDA: dalla 2018.3 alla  2019.1

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
* Skype (universal app)
* Store
* Meteo
* Vari moduli per controlli come le mattonelle del menu avvio.

Note:

* Nota: questo addon richiede Windows 10 Versione 1803 (build 17134) o
  successive, e NVDA 2018.3 o successive. Per migliori prestazioni,
  utilizzare il componente con l'ultima versione stabile di Windows10 (build
  17763) e l'ultima versione stabile di NVDA. 
* Alcune caratteristiche di questo componente aggiuntivo sono o diventeranno
  parte di NVDA
* Per le voci non elencate di seguito, si può supporre che son
  caratteristiche già incluse in NVDA, che non sono applicabili dal
  componente in quanto non supporta precedenti versioni di Windows, o che le
  applicazioni son state modificate in modo che le caratteristiche del
  componente non son più applicabili.
* Il controllo dell'aggiornamento automatico direttamente dal componente è
  stato rimosso. Per i futuri aggiornamenti automatici si potrà usare il
  componente aggiuntivo addonsUpdate.

Per un elenco delle modifiche riguardo le versioni rilasciate, fare
riferimento al documento [changelogs for add-on releases][3].

## Generale

* Modifiche interne per rendere il componente aggiuntivo  compatibile con le
  future versioni di NVDA. 
* Modifiche minori per i messaggi presentati in altre lingue diverse
  dall'inglese. 
* le Voci di sottomenu vengono correttamente riconosciute in varie
  applicazioni, incluso il menu contestuale per la griglia del menu Start e
  delle apps di Microsoft Edge (Redstone 5).
* Molte finestre di dialogo vengono gestite correttamente, soprattutto
  quelle inerenti il feedback su Windows Insider. Questo è stato incluso in
  NVDA 2018.3.
* NVDA può annunciare il numero dei suggerimenti quando si esegue una
  ricerca. Questa funzione è controllata dall'opzione "leggi le informazioni
  sulla posizione dell'oggetto" nella finestra presentazioni oggetti di
  NVDA.
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

## Centro attività:

* Il pulsante per la Luminositàora funziona come un pulsante attivabile e
  non come un pulsante ciclico. Questa caratteristica verrà inclusa in NVDA
  2019.1.
* Vari cambiamenti di stato come assistenza in primo piano e Luminosità
  verranno segnalati. Queste caratteristiche verranno incluse in NVDA 2019.1

## Allarmi e sveglia

* I valori per selezionare l'ora adesso vengono annunciati. Questo comprende
  anche la sezione inerente la scelta dell'orario sul quando riavviare per
  terminare gli aggiornamenti di Windows Update. Queste caratteristiche
  verranno incluse in NVDA 2019.1.

## Calcolatrice

* Quando viene premuto invio o Esc, NVDA annuncia il risultato del calcolo.
* Per i calcoli quali conversioni di unità di misura o valuta, NVDA leggerà
  il risultato non appena verranno inseriti i dati
* NVDA non annuncerà più il livello di intestazione per i risultati dei
  calcoli.

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

Nota: la maggior parte delle caratteristiche di seguito sono state incluse
in NVDA 2018.3. 

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
* NVDA non avviserà più con un suono di errore o altri messaggi quando si
  chiude il pannello delle emoji nelle nuove anteprime Insider.
* Nella  Versione 1809 (aggiornamento Windows di ottobre 2018 ) e
  successive, NVDA annuncerà i risultati di ricerca per emojis quando
  possibile.

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

## Skype

Nota: le voci di seguito non funzionano correttamente in Skype 14
Universal-app.

* Viene annunciato quando un utente sta scrivendo, così come accade in Skype
  per desktop.
* Control+NVDA+fila dei numeri, utilizzato per leggere la cronologia delle
  chat recenti e per spostare il navigatore ad oggetti nelle varie voci
  della chat in Skype per Desktop, ora è anche disponibile in Skype UWP.
* è possibile premere il tasto alt in combinazione con i numeri per
  spostarsi tra conversazioni (1), elenco contatti  (2), bots (3) e campo
  editazione della chat se visibile (4). Si noti che questi comandi
  funzioneranno a dovere se è stato installato l'aggiornamento di Skype di
  marzo 2017.
* Nella maggior parte dei casi, NVDA non leggerà più i messaggi Skype di
  continuo quando se ne sta controllando uno
* Dall'elenco cronologia messaggi, è possibile premere NVDA+d in un
  qualsiasi elemento per fare in modo che NVDA legga alcuni dettagli del
  messaggio, come il tipo di canale, ora e data di invio, etc.

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
