# Windows App Essentials #

* Autori: Joseph Lee, Derek Riemer e altri utenti di Windows 10
* Scarica la [versione stabile][1]
* Scarica la [versione in sviluppo][2]
* NVDA compatibility: 2020.4 and beyond

Note: Originally called Windows 10 App Essentials, it was renamed to Windows
App Essentials in 2021 to support Windows 10 and future releases such as
Windows 11. Parts of this add-on will still refer to the original add-on
name.

This add-on is a collection of app modules for various modern Windows apps,
as well as enhancements and fixes for certain controls found in Windows 10
and later.

Di seguito l'elenco di tutti gli appmodule contenuti nel componente
aggiuntivo, si veda la relativa sezione per ulteriori informazioni:

* Calculator (modern)
* Calendario
* Cortana (Conversazioni)
* Posta
* Mappe
* Microsoft Solitaire Collection
* Microsoft Store
* Modern keyboard (emoji panel/dictation/voice typing/hardware input
  suggestions/clipboard history/modern input method editors)
* Persone
* Impostazioni (Impostazioni di Windows, Windows+i)
* Meteo
* Miscellaneous modules for controls such as Start Menu tiles

Note:

* This add-on requires Windows 10 20H2 (build 19042) or later. For best
  results, use the add-on with latest Windows release (Windows 10 21H1/build
  19043).
* Although installation is possible, this add-on does not support Windows
  Enterprise LTSC (Long-Term Servicing Channel) and Windows Server releases.
* Support for Windows 11 is experimental, and some features will not work
  (see relevant entries for details). A warning dialog will be shown if
  trying to install stable versions of this add-on on Windows 11 prior to
  general availability.
* Alcune caratteristiche di questo componente aggiuntivo sono o diventeranno
  parte di NVDA.
* For entries not listed below, you can assume that features are part of
  NVDA, no longer applicable as the add-on does not support unsupported
  Windows releases such as old Windows 10 versions, or changes were made to
  Windows and apps that makes entries no longer applicable.
* Some apps support compact overlay mode (always on top in Calculator, for
  example), and this mode will not work properly with portable version of
  NVDA.

Per un elenco delle modifiche presenti in ogni versione dell'add-on, fare
riferimento al documento [changelogs for add-on releases][3].

## Generale

* NVDA can announce suggestion count when performing a search in majority of
  cases, including when suggestion count changes as search progresses. This
  option is controlled by "Report object position information" in Object
  presentation panel found in NVDA settings.
* When searching in Start menu or File Explorer in Windows 10 1909 (November
  2019 Update) and later, instances of NVDA announcing search results twice
  when reviewing results are less noticeable, which also makes braille
  output more consistent when reviewing items.
* In addition to UIA event handlers provided by NVDA, the following UIA
  events are recognized: drag start, drag cancel, drag complete, drop target
  drag enter, drop target drag leave, drop target dropped, layout
  invalidated. With NVDA's log level set to debug, these events will be
  tracked, and for UIA notification event, a debug tone will be heard if
  notifications come from somewhere other than the currently active
  app. Events built into NVDA such as name change and controller for events
  will be tracked from an add-on called Event Tracker.
* E' possibile tracciare solo specifici eventi e/o eventi provenienti solo
  da applicazioni specifiche.
* When opening, closing, reordering (Windows 11), or switching between
  virtual desktops, NVDA will announce active virtual desktop name (desktop
  2, for example).
* NVDA non leggerà più le dimensioni del testo del menu avvio quando si
  cambia la risoluzione o l'orientamento dello schermo.
* Quando si riposizionano le mattonelle del menu Avvio o le azioni rapide
  del centro azioni con Alt+Shift+frecce, NVDA fornirà informazioni sugli
  elementi trascinati e sulle loro nuove posizioni.
* Messaggi come le modifiche al volume e alla luminosità in Esplora File o
  le notifiche di aggiornamento delle app in Microsoft Store possono essere
  soppressi disattivando l'opzione Annuncia Notifiche nelle impostazioni di
  NVDA, categoria presentazione oggetti.

## Calcolatrice

* NVDA will no longer announce graphing calculator screen message twice.

## Calendario

* Non verrà più letta la dicitura "Modificabile" e  "sola lettura" nel corpo
  del messaggio o in altri campi editazione.

## Cortana

Most items are applicable when using Cortana Conversations (Windows 10 2004
and later).

* Le risposte testuali di Cortana sono vocalizzate nella maggior parte dei
  casi.
* NVDA rimarrà in silenzio mentre si parla a Cortana  con la voce.
* In Windows 10 1909 (November 2019 Update) and later, modern search
  experience in File Explorer powered by Windows Search user interface is
  supported.

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
* When downloading content such as apps and movies, NVDA will announce
  product name and download progress (does not work properly in updated
  Microsoft Store in Windows 11).

## Tastiera moderna

This includes emoji panel, clipboard history, dictation/voice typing,
hardware input suggestions, and modern input method editors for certain
languages. When viewing emojis, for best experience, enable Unicode
Consortium setting from NVDA's speech settings and set symbol level to
"some" or higher. When pasting from clipboard history in Windows 10, press
Space key instead of Enter key to paste the selected item. NVDA also
supports updated input experience panel in Windows 11.

* In alcune circostanze, quando si apre lo storico degli appunti, NVDA non
  dirà più "appunti" se vi sono elementi negli appunti.
* On some systems running Windows 10 1903 (May 2019 Update) and later, NVDA
  will no longer appear to do nothing when emoji panel opens.
* When an emoji group (including kaomoji and symbols group in Windows 10
  1903 or later) is selected, NVDA will no longer move navigator object to
  certain emojis.
* Added support for updated input experience panel (combined emoji panel and
  clipboard history) in Windows 11.

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
* Odd control labels seen in certain Windows installations has been
  corrected.
* NVDA will announce the name of the optional quality update link if
  present, typically named "download and install now".

## Meteo

* Schede come "previsioni" e "mappe" vengono riconosciute correttamente
  (patch da Derek Riemer).
* Durante la lettura di una previsione, utilizzare le frecce sinistra e
  destra per spostarsi tra gli elementi. Utilizzare le frecce su e giù per
  leggere i dettagli di un elemento. Per esempio, premendo la freccia destra
  potrebbe venir annunciato "lunedì: 29 gradi, parzialmente nuvoloso, ..."
  premendo la freccia giù dirà "lunedì", Quindi premerla di nuovo per
  leggere il prossimo elemento (ad esempio la temperatura). Ciò funziona per
  previsioni orarie e giornaliere.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
