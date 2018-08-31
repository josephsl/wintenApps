# Windows 10 App Essentials #

* Autori: Joseph Lee, Derek Riemer e altri utenti Windows 10.
* Download [versione stabile][1]
* Download [versione in sviluppo][2]

Questo componente aggiuntivo è un insieme di app module per numerose app
Windows10, e consente anche di risolvere anomalie con alcuni controlli.

Segue l'elenco di tutti gli appmodule contenuti nel componente aggiuntivo,
si veda la relativa sezione per ulteriori informazioni:

* Allarmi e sveglia.
* Calendario
* Calcolatrice (moderna).
* Cortana
* Centro Feedback
* Barra dei giochi
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

* This add-on requires Windows 10 Version 1709 (build 16299) or later and
  NVDA 2018.2 or later. For best results, use the add-on with latest Windows
  10 stable release (build 17134) and latest stable version of NVDA.
* Alcune caratteristiche di questo componente aggiuntivo sono o diventeranno
  parte di NVDA
* For entries not listed below, you can assume that features are part of
  NVDA, no longer applicable as the add-on does not support old Windows 10
  releases, or changes were made to apps that makes entries no longer
  applicable.

For a list of changes made between each add-on releases, refer to
[changelogs for add-on releases][3] document.

## Generale

* Submenu items are properly recognized in various apps, including context
  menu for Start menu tiles and microsoft Edge's app menu (Redstone 5).
* Certain dialogs are now recognized as proper dialogs and reported as such,
  including Insider Preview dialog (settings app). This will be part of NVDA
  2018.3.
* NVDA può annunciare il numero dei suggerimenti quando si esegue una
  ricerca. Questa funzione è controllata dall'opzione "leggi le informazioni
  sulla posizione dell'oggetto" nella finestra presentazioni oggetti di
  NVDA.
* In alcuni menu di contesto, come in Edge, le informazioni sulla posizione
  come 1 su 2 non vengono più annunciate.
* The following UIA events are recognized: active text position change,
  controller for, drag start, drag cancel, drag complete, element selected,
  live region change, notification, system alert, tooltip opened, window
  opened. With NVDA set to run with debug logging enabled, these events will
  be tracked, and for UIA notification event, a debug tone will be heard if
  notifications come from somewhere other than the currently active app.
* Aggiunta la possibilità di controllare automaticamente o manualmente la
  presenza di aggiornamenti di questo componente aggiuntivo mediante la
  finestra di dialogo Windows10 Essentials presente al menu preferenze di
  NVDA. Di default le versioni stabili eseguiranno un controllo settimanale,
  mentre quelle in sviluppo giornaliero.
* In some apps, live region text is announced. This includes alerts in Edge
  (including elements marked with aria-role=alert), results in Calculator
  and others. Note that this may result in double-speaking in some
  cases. This is now part of NVDA 2017.3 or later.
* Notifications from newer app releases on Windows 10 Version 1709 (build
  16299) and later are announced. NVDA 2018.2 and later supports this, with
  2018.3 adding support for more notifications.
* Vengono riconosciuti e annunciati i suggerimenti di Microsoft Edge e app
  universali.
* With Sets turned on (builds 17627 through 17692 for some insiders), when
  opening a new Sets tab (Control+Windows+T), NVDA will announce search
  results when searching for items in the embedded Cortana window.
* With Sets turned on, when switching between Sets tabs, NvDA will announce
  name and position of the tab you are switching to.
* Quando si passa ad un desktop virtuale successivo, o viene chiuso o ne
  viene aperto uno, NVDA annuncerà il numero del desktop, ad esempio
  Desktop2, Desktop3, etc.
* NVDA non leggerà più le dimensioni del testo del menu avvio quando si
  cambia la risoluzione dello schermo o orientamento.

## Allarmi e sveglia

* I valori per selezionare l'ora adesso vengono annunciati. Questo comprende
  anche la sezione inerente la scelta dell'orario sul quando riavviare per
  terminare gli aggiornamenti di Windows Update

## Calcolatrice

* Quando viene premuto invio o Esc, NVDA annuncia il risultato del calcolo.
* Per i calcoli quali conversioni di unità di misura o valuta, NVDA leggerà
  il risultato non appena verranno inseriti i dati
* NVDA non annuncerà più il livello di intestazione per i risultati dei
  calcoli.

## calendario

* Insider Hub (centro di supporto in Anniversary Update): solo per quegli
  utenti che usano una versione Insider di Windows, servendosi del centro
  Feedback Insider per aggiornamenti.

## Cortana

* Le risposte di tipo testuale di Cortana vengono lette nella maggior parte
  dei casi, se non dovesse funzionare riaprire il menu avvio e ripetere la
  ricerca.
* NVDA rimarrà in silenzio mentre si parla a Cortana  con la voce.
* NVDA annuncerà la conferma di un promemoria quando ne viene inserito uno.

## Centro Feedback

* Per le release di nuove app, NVDA non annuncerà più due volte la categoria
  feedback.

## Barra dei giochi

* NVDA annuncerà la comparsa della barra dei giochi. Purtroppo a causa di
  limitazioni tecniche, l'interazione con la GameBar non è possibile in
  maniera completa fino alla versione 17723.

## Posta

* Quando si scorrono gli elementi in un elenco messaggi, è possibile
  utilizzare i comandi di navigazione tabella per controllare le
  intestazioni.
* Durante la composizione di un messaggio, verranno emessi segnali acustici
  nel caso ci siano dei suggerimenti per menzioni dopo la chiocciola

## Mappe

* NVDA emette dei segnali acustici per le posizioni presenti nella mappa.
* Quando si usa la visualizzazione per strade e l'opzione "utilizza
  tastiera" è attiva, NVDA annuncerà gli indirizzi delle vie mentre si
  scorre la mappa con le frecce.

## Microsoft Edge

* Vengono annunciate correttamente le notifiche dei download dei file, degli
  avvisi delle pagine web e se è disponibile la modalità lettura (dalla
  versione 1709 in poi)

## Tastiera moderna

* Supporto per l'immissione di emoji animate (Fall creators Update in su,
  comprese build 17661 e successive aventi pannelli con nuovi design). Per
  ottenere i migliori risultati si consiglia di servirsi delle voci OneCore,
  ossia quelle già presenti in Windows10.
* Supporto per i suggerimenti di immissione in tastiere hardware nella
  Versione 1803 (aggiornamento Aprile 2018) e successive
* Nelle build successive alla 1709, NVDA leggerà la prima emoji selezionata
  quando si apre il pannello Emoji.
* Supporto per la lettura di appunti cloud nella build 17666 (Redstone 5) e
  successive.
* Reduced unnecessary verbosity when working with modern keyboard and its
  features. These include no longer announcing "Microsoft Candidate UI" when
  opening hardware keyboard input suggestions and staying silent when
  certain touch keyboard keys raise name change event on some systems.

## Persone

* Durante la ricerca di contatti, verrà letto il primo suggerimento, in
  particolare se si utilizza le ultime versioni delle app.

## Impostazioni

* Vengono annunciate automaticamente le informazioni di avanzamento delle
  operazioni di Windows Update.
* Le informazioni delle barre di avanzamento non vengono più lette due
  volte.
* Il gruppo impostazioni viene riconosciuto quando ci si sposta tra i
  controlli usando la navigazione ad oggetti.
* Per alcune caselle combinate, NVDA non commetterà più errori nel
  riconoscere le etichette o annunciare i cambiamenti dei valori.
* Non vengono più riprodotti beep per le barre di avanzamento del controllo
  volume dalla versioni 1803 e successive.
* More messages about Windows Update status are announced, especially if
  Windows Update encounters errors.

## Skype

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
