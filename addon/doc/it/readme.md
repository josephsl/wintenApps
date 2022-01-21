# Windows App Essentials #

* Authors: Joseph Lee, Derek Riemer and others
* Scarica la [versione stabile][1]
* Scarica la [versione in sviluppo][2]
* NVDA compatibility: 2021.2 and later

Note: Originally called Windows 10 App Essentials, it was renamed to Windows
App Essentials in 2021 to support Windows 10 and future releases such as
Windows 11. Parts of this add-on will still refer to the original add-on
name.

This add-on is a collection of app modules for various modern Windows apps,
as well as enhancements and fixes for certain controls found in Windows 10
and later.

Di seguito l'elenco di tutti gli appmodule contenuti nel componente
aggiuntivo, si veda la relativa sezione per ulteriori informazioni:

* Calcolatrice
* Cortana
* Posta
* Mappe
* Microsoft Solitaire Collection
* Modern keyboard (emoji panel/dictation/voice typing/hardware input
  suggestions/clipboard history/modern input method editors)
* Notepad (Windows 11)
* Persone
* Impostazioni (Impostazioni di Windows, Windows+i)
* Meteo
* Miscellaneous modules for controls such as Start Menu tiles

Note:

* This add-on requires Windows 10 21H1 (build 19043) or later and is
  compatible with Windows 11.
* Although installation is possible, this add-on does not support Windows
  Enterprise LTSC (Long-Term Servicing Channel) and Windows Server releases.
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
  is now part of NVDA 2021.3.
* In addition to UIA event handlers provided by NVDA, the following UIA
  events are recognized: drag complete, drop target dropped, layout
  invalidated. With NVDA's log level set to debug, these events will be
  tracked, and for UIA notification event, a debug tone will be heard if
  notifications come from somewhere other than the currently active
  app. Events built into NVDA such as name change and controller for events
  are tracked from an add-on called Event Tracker.
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
* In Windows 10, history and memory list items are properly labeled.

## Cortana

* Le risposte testuali di Cortana sono vocalizzate nella maggior parte dei
  casi.
* NVDA rimarrà in silenzio mentre si parla a Cortana  con la voce.

## Posta

* Quando si scorrono le voci nell'elenco messaggi, è possibile utilizzare i
  comandi di navigazione tabella per controllarne le intestazioni. Notare
  che la navigazione tra le righe (messaggi) non è supportata.

## Mappe

* NVDA emette dei segnali acustici per le posizioni presenti nella mappa.
* Quando si usa la visualizzazione per strade e l'opzione "utilizza
  tastiera" è attiva, NVDA annuncerà gli indirizzi delle vie mentre si
  scorre la mappa con le frecce.

## Microsoft Solitaire Collection

* NVDA vocalizzerà i nomi delle carte e dei mazzi di carte.

## Tastiera moderna

This includes emoji panel, clipboard history, dictation/voice typing,
hardware input suggestions, and modern input method editors for certain
languages. When viewing emojis, for best experience, enable Unicode
Consortium setting from NVDA's speech settings and set symbol level to
"some" or higher. When pasting from clipboard history in Windows 10, press
Space key instead of Enter key to paste the selected item. NVDA also
supports updated input experience panel in Windows 11.

* In Windows 10, when an emoji group (including kaomoji and symbols group)
  is selected, NVDA will no longer move navigator object to certain emojis.
* Added support for updated input experience panel (combined emoji panel and
  clipboard history) in Windows 11.
* In Windows 11, it is again possible to use the arrow keys to review emojis
  when emoji panel opens.

## Notepad

This refers to Windows 11 Notepad version 11 or later.

* NVDA will announce status items such as line and column information when
  report status bar command (NVDA+End in desktop layout, NvDA+Shift+End in
  laptop layout) is performed.
* NVDA will no longer announce entered text when pressing Enter key from the
  document.

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
* NVDA will announce the name of the optional quality update control if
  present (download and install now link in Windows 10, download button in
  Windows 11).
* In Windows 11, breadcrumb bar items are properly recognized.

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
