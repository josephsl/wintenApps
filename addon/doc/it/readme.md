# Windows 10 App Essentials #

* Autori: Joseph Lee, Derek Riemer e altri utenti Windows 10.
* Download [versione stabile][1]
* Download [versione in sviluppo][2]

Questo componente aggiuntivo è un insieme di app module per numerose app
Windows10, e consente anche di risolvere anomalie con alcuni controlli.

Segue l'elenco di tutti gli appmodule contenuti nel componente aggiuntivo,
si veda la relativa sezione per ulteriori informazioni:

* Action center
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
  NVDA 2018.3 or later. For best results, use the add-on with latest Windows
  10 stable release (build 17763) and latest stable version of NVDA.
* Alcune caratteristiche di questo componente aggiuntivo sono o diventeranno
  parte di NVDA
* For entries not listed below, you can assume that features are part of
  NVDA, no longer applicable as the add-on does not support old Windows 10
  releases, or changes were made to apps that makes entries no longer
  applicable.

For a list of changes made between each add-on releases, refer to
[changelogs for add-on releases][3] document.

## Generale

* Internal changes to make the add-on compatible with future NVDA releases.
* If Add-on Updater add-on is installed, that add-on will check for Windows
  10 App Essentials updates.
* Default update check interval has changed to weekly checks for both stable
  and development releases. This is applicable if the add-on itself checks
  for updates.
* If the add-on is set up to check for updates, when updating the add-on, if
  the new add-on release requires a newer version of NVDA, an error message
  will be presented.
* Small changes to how some messages are presented in languages other than
  English.
* Submenu items are properly recognized in various apps, including context
  menu for Start menu tiles and microsoft Edge's app menu (Redstone 5).
* Certain dialogs are now recognized as proper dialogs and reported as such,
  including Insider Preview dialog (settings app). This is now part of NVDA
  2018.3.
* NVDA può annunciare il numero dei suggerimenti quando si esegue una
  ricerca. Questa funzione è controllata dall'opzione "leggi le informazioni
  sulla posizione dell'oggetto" nella finestra presentazioni oggetti di
  NVDA.
* In alcuni menu di contesto, come in Edge, le informazioni sulla posizione
  come 1 su 2 non vengono più annunciate.
* The following UIA events are recognized: active text position change,
  controller for, drag start, drag cancel, drag complete, element selected,
  item status, live region change, notification, system alert, tooltip
  opened, window opened. With NVDA set to run with debug logging enabled,
  these events will be tracked, and for UIA notification event, a debug tone
  will be heard if notifications come from somewhere other than the
  currently active app.
* Notifications from newer app releases on Windows 10 Version 1709 (build
  16299) and later are announced. NVDA 2018.2 and later supports this, with
  2018.3 adding support for more notifications.
* Vengono riconosciuti e annunciati i suggerimenti di Microsoft Edge e app
  universali.
* Quando si passa ad un desktop virtuale successivo, o viene chiuso o ne
  viene aperto uno, NVDA annuncerà il numero del desktop, ad esempio
  Desktop2, Desktop3, etc.
* NVDA non leggerà più le dimensioni del testo del menu avvio quando si
  cambia la risoluzione dello schermo o orientamento.

## Action center

* Brightness quick action is now a button instead of a toggle button.
* Various status changes such as Focus Assist and Brightness will be
  reported.

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

* When reviewing items in messages list, you can now use table navigation
  commands to review message headers. Note that navigating between rows
  (messages) is not supported.
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
* Text auto-complete will be tracked and announced in address omnibar.

## Tastiera moderna

Note: most features below are now part of NVDA 2018.3.

* Support for Emoji input panel in Version 1709 (Fall Creators Update) and
  later, including the redesigned panel in Version 1809 (build 17661 and
  later) and changes made in 19H1 (build 18262). For best experience when
  reading emojis, use Windows OneCore speech synthesizer.
* Supporto per i suggerimenti di immissione in tastiere hardware nella
  Versione 1803 (aggiornamento Aprile 2018) e successive
* In post-1709 builds, NVDA will announce the first selected emoji when
  emoji panel opens. This is more noticeable in build 18262 and later where
  emoji panel may open to last browsed category, such as displaying skin
  tone modifier when opened to People category.
* Support for announcing cloud clipboard items in Version 1809 (build 17666
  and later).
* Reduced unnecessary verbosity when working with modern keyboard and its
  features. These include no longer announcing "Microsoft Candidate UI" when
  opening hardware keyboard input suggestions and staying silent when
  certain touch keyboard keys raise name change event on some systems.
* NVDA will no longer play error tones or do nothing when closing emoji
  panel in more recent Insider Preview builds.
* NVDA will announce search results for emojis if possible.

## Persone

* Durante la ricerca di contatti, verrà letto il primo suggerimento, in
  particolare se si utilizza le ultime versioni delle app.

## Impostazioni

* Certain information such as Windows Update progress is reported
  automatically, including Storage sense/disk cleanup widget.
* Le informazioni delle barre di avanzamento non vengono più lette due
  volte.
* Il gruppo impostazioni viene riconosciuto quando ci si sposta tra i
  controlli usando la navigazione ad oggetti.
* For some combo boxes and radio buttons, NVDA will no longer fail to
  recognize labels and/or announce value changes.
* Non vengono più riprodotti beep per le barre di avanzamento del controllo
  volume dalla versioni 1803 e successive.
* More messages about Windows Update status are announced, especially if
  Windows Update encounters errors.
* NVDA will no longer appear to do nothing or play error tones if using
  object navigation commands under some circumstances.
* Various links added in build 18282 with no labels now have labels.
* Windows Update reminder dialog is recognized as a proper dialog.

## Skype

Note: the below entries won't work properly in Skype 14 universal app.

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
