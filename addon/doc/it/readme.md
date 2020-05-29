# Windows 10 App Essentials #

* Autori: Joseph Lee, Derek Riemer e altri utenti Windows 10
* Scarica la [versione stabile][1]
* Scarica la [versione in sviluppo][2]
* Compatibilità con NVDA: dalla versione 2019.3 alla 2020.1

Questo componente aggiuntivo è un insieme di app module per numerose app di
Windows 10, che inoltre risolve anomalie e migliora alcuni controlli.

Di seguito l'elenco di tutti gli appmodule contenuti nel componente
aggiuntivo, si veda la relativa sezione per ulteriori informazioni:

* Calcolatrice (moderna).
* Calendario
* Cortana (Conversazioni)
* Posta
* Mappe
* Microsoft Solitaire Collection
* Microsoft Store
* Tastiera moderna (pannello emoji/dettatura/suggerimenti per l'input da
  tastiere hardware/storico degli appunti nel cloud/editor per i metodi di
  input moderni)
* Persone
* Impostazioni (Impostazioni Windows, Windows+i)
* Meteo.
* Vari moduli per controlli come le mattonelle del menu avvio.

Note:

* Questo addon richiede Windows 10 Versione 1903 (build 18362) o
  successive. Per migliori prestazioni, utilizzare il componente con
  l'ultima versione stabile di Windows10 (build 18363).
* Alcune caratteristiche di questo componente aggiuntivo sono o diventeranno
  parte di NVDA.
* Per le voci non elencate di seguito, si può supporre che esse siano
  caratteristiche incluse in NVDA, non più applicabili dal componente in
  quanto non supporta precedenti versioni di Windows 10, o che le
  applicazioni siano state modificate in modo che le caratteristiche del
  componente non sono più applicabili.

Per un elenco delle modifiche presenti in ogni versione dell'add-on, fare
riferimento al documento [changelogs for add-on releases][3].

## Generale

* NVDA non avviserà più con un suono di errore se questo add-on viene
  attivato con Windows 7, Windows 8.1 e versioni non supportate di Windows
  10.
* Oltre alle finestre di dialogo riconosciute da NVDA, ora ne vengono
  gestite correttamente altre, comprese quelle delle Insider Preview (app
  impostazioni)
* Nella maggior parte dei casi, NVDA può annunciare il numero dei
  suggerimenti quando si esegue una ricerca. Questa funzione è controllata
  dall'opzione "leggi le informazioni sulla posizione dell'oggetto" nella
  finestra presentazioni oggetti di NVDA.
* Quando si cerca nel menu Avvio o in Esplora File nella Versione 1909
  (aggiornamento di novembre 2019) e successive,  le doppie ripetizioni da
  parte di NVDA quando si leggono i risultati con il cursore di controllo
  sono meno frequenti, il che migliora anche l'output Braille nella stessa
  situazione.
* Sono riconosciuti i seguenti eventi UIA: modulo di controllo, inizio
  trascinamento, trascinamento annullato, trascinamento completato,
  destinazione del trascinamento inserita, abbandono della destinazione del
  trascinamento, destinazione del trascinamento rilasciata, elemento
  selezionato, stato dell'elemento, modifica regione live, notifica, avviso
  di sistema, modifica testo, suggerimento aperto, finestra aperta. Quando
  NVDA è avviato con il log impostato su debug, questi eventi saranno
  tracciati, e, per gli eventi di notifiche UIA, verrà emesso un segnale
  acustico se le notifiche provengono da applicazioni diverse da quella
  attiva.
* E' possibile tracciare solo specifici eventi e/o eventi provenienti solo
  da applicazioni specifiche.
* Quando si passa ad un desktop virtuale successivo, o ne viene chiuso o
  aperto uno, NVDA annuncerà il numero del desktop, ad esempio Desktop2.
* NVDA non leggerà più le dimensioni del testo del menu avvio quando si
  cambia la risoluzione o l'orientamento dello schermo.
* Quando si riposizionano le mattonelle del menu Avvio o le azioni rapide
  del centro azioni con Alt+Shift+frecce, NVDA fornirà informazioni sugli
  elementi trascinati e sulle loro nuove posizioni.
* Nelle versioni nuove di Word 365, NVDA non dirà più "parola cancellata
  all'indietro" quando si preme Control+Backspace.
* Messaggi come le modifiche al volume e alla luminosità in Esplora File o
  le notifiche di aggiornamento delle app in Microsoft Store possono essere
  soppressi disattivando l'opzione Annuncia Notifiche nelle impostazioni di
  NVDA, categoria presentazione oggetti.

## Calcolatrice

* Quando viene premuto invio o Esc, NVDA annuncia il risultato del calcolo.
* Per i calcoli quali conversioni di unità di misura o valuta, NVDA leggerà
  il risultato non appena verranno inseriti i dati.
* NVDA non annuncerà più il livello di intestazione per i risultati dei
  calcoli.
* NVDA segnalerà che è stato raggiunto il numero massimo di cifre
  nell'inserimento di espressioni.
* Aggiunto il supporto per la modalità "sempre attiva" nelle versioni della
  calcolatrice dalla 10.1908 in poi.

## Calendario

* Non verrà più letta la dicitura "Modificabile" e  "sola lettura" nel corpo
  del messaggio o in altri campi editazione.

## Cortana

La maggior parte delle funzionalità non sono più applicabili nelle versioni
1903 e successive, a meno che non si utilizzi Cortana Conversations versione
2004 o superiore.

* Le risposte testuali di Cortana sono vocalizzate nella magior parte dei
  casi.
* NVDA rimarrà in silenzio mentre si parla a Cortana  con la voce.
* Nella versione 1909 (aggiornamento di novembre 2019) e nelle successive, è
  supportata l'esperienza di ricerca moderna in Esplora File fornita
  dall'interfaccia utente di Windows Search.

## Posta

* Quando si scorrono le voci nell'elenco messaggi, è possibile utilizzare i
  comandi di navigazione tabella per controllarne le intestazioni. Notare
  che la navigazione tra le righe (messaggi) non è supportata.
* Durante la composizione di un messaggio, verranno emessi segnali acustici
  nel caso ci siano dei suggerimenti per menzioni dopo la chiocciola.

## Mappe

* NVDA emette dei segnali acustici per le posizioni presenti nella mappa.
* Quando si usa la visualizzazione per strade e l'opzione "utilizza
  tastiera" è attiva, NVDA annuncerà gli indirizzi delle vie mentre si
  scorre la mappa con le frecce.

## Microsoft Solitaire Collection

* NVDA vocalizzerà i nomi delle carte e dei mazzi di carte.

## Microsoft Store

* Dopo aver controllato la presenza di aggiornamenti di app, il nome delle
  app nell'elenco degli aggiornamenti viene correttamente etichettato.
* Mentre si scaricano contenuti quali app o film, NVDA ne leggerà il nome e
  l'avanzamento del download.

## Tastiera moderna

Questa funzionalità comprende il pannello emoji, lo storico degli appunti,
la dettatura, i suggerimenti per l'input da tastiere hardware e l'editor di
metodi di input moderni per alcune lingue.

* In alcune circostanze, quando si apre lo storico degli appunti, NVDA non
  dirà più "appunti" se vi sono elementi negli appunti.
* In alcuni sistemi che eseguono la versione 1903 (aggiornamento di maggio
  2019) o superiore, NVDA non resterà più muto quando si apre il pannello
  emoji.
* Aggiunto il supporto per le IME candidates interface in cinese moderno,
  Giapponese e coreano (CJK), introdotte nella versione 2004 (build 18965 e
  successive).

## Persone

* Durante la ricerca di contatti, verrà letto il primo suggerimento, in
  particolare se si utilizzano le ultime versioni delle app.

## Impostazioni

* Vengono annunciate automaticamente alcune informazioni come l'avanzamento
  di Windows Update, comprese le informazioni fornite dalle utility di
  manutenzione unità e pulizia disco e i messaggi di errore di Windows
  Update.
* I valori delle barre di avanzamento ed altre informazioni non vengono più
  letti due volte.
* Per alcune caselle combinate o pulsanti radio, NVDA non commetterà più
  errori nel riconoscere le etichette o nell'annunciare i cambiamenti dei
  valori.
* NVDA non resterà più muto né riporterà errori quando si usa  il navigatore
  ad oggetti in alcune situazioni.
* La finestra di notifica per nuovi aggiornamenti windows verrà ora
  visualizzata  correttamente.
* Le strane etichette dei controlli viste in alcune installazioni di Windows
  10 sono state corrette.
* Nelle revisioni più recenti della versione 1803 e nelle successive, a
  causa di modifiche alla procedura di Windows Update dovuta ad
  aggiornamenti di alcune funzionalità, è stato aggiunto un link "scarica e
  installa adesso". Ora NVDA vocalizzerà il titolo del nuovo aggiornamento
  se presente.

## Meteo

* Schede come "previsioni" e "mappe" vengono riconosciute correttamente
  (patch da Derek Riemer).
* Durante la lettura di una previsione, utilizzare le frecce sinistra e
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
