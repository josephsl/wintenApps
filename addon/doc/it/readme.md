# Windows 10 App Essentials #

* Autori: Joseph Lee, Derek Riemer e altri utenti Windows 10.
* Download [versione stabile][1]
* Download [versione in sviluppo][2]

Questo componente aggiuntivo è un insieme di app module per numerose app
Windows10, e consente anche di risolvere anomalie con alcuni controlli.

Segue l'elenco di tutti gli appmodule contenuti nel componente aggiuntivo,
si veda la relativa sezione per ulteriori informazioni:

* Allarmi e sveglia.
* Bank of America
* Calendario
* Calcolatrice (moderna).
* Cortana
* Groove Music
* Posta
* Mappe
* Microsoft Edge
* Impostazioni (Impostazioni Windows, Windows+i)
* Anteprima Skype
* Store
* Twitter.
* TeamViewer Touch.
* Meteo
* Windows Defender Security Center (Creators Update and later)
* Vari moduli per controlli come le mattonelle del menu avvio.

Nota: questo add-on richiede  Windows 10 Versione 1511 (build 10586) o
successive e NVDA 2016.4 o successive. Per avere le prestazioni migliori,
utilizzare il componente aggiuntivo con l'ultima build stabile (build
14393).

## Generale

* Nei menu di contesto per le mattonelle del menu avvio, vengono
  riconosciuti in maniera corretta i sottomenu.
* Quando vengono ridotte a icona tutte le finestre (Windows+M), non verrà
  più annunciata la parola "riquadro".
* Molte finestre di dialogo vengono gestite correttamente, soprattutto
  quelle inerenti il feedback su Windows Insider e le impostazioni, nonché i
  nuovi controlli UAC presenti dalla build 14328 e successive per NVDA
  2016.2.1 in poi
* Viene annunciata la comparsa di suggerimenti nei risultati di ricerca,
  soprattutto nelle impostazioni e nello store, attraverso sia suoni che
  braille. In questo è compresa anche la finestra di ricerca del menu avvio.
* NVDA può annunciare il numero dei suggerimenti quando si esegue una
  ricerca, almeno nella maggior parte dei casi. Questa funzione è
  controllata dall'opzione "leggi le informazioni sulla posizione
  dell'oggetto" nella finestra presentazioni oggetti di NVDA.
* In alcuni menu di contesto, come in Edge, le informazioni sulla posizione
  come 1 su 2 non vengono più annunciate.
* Vengono riconosciuti e gestiti i seguenti eventi UIA: Controller for, live
  region changed (handled by name change event).
* Aggiunta la possibilità di controllare automaticamente o manualmente la
  presenza di aggiornamenti di questo componente aggiuntivo mediante la
  finestra di dialogo Windows10 Essentials presente al menu preferenze di
  NVDA. Di default le versioni stabili eseguiranno un controllo settimanale,
  mentre quelle in sviluppo giornaliero.

## Allarmi e sveglia

* I valori per selezionare l'ora adesso vengono annunciati. Questo comprende
  anche la sezione inerente la scelta dell'orario sul quando riavviare per
  terminare gli aggiornamenti di Windows Update

## Calcolatrice

* Quando viene premuto invio, NVDA annuncia il risultato del calcolo.

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

## Groove Music

* Viene annunciata la comparsa di suggerimenti mentre si stanno cercando
  elementi all'interno delle tracce

## Posta

* Quando si scorrono gli elementi in un elenco messaggi, è possibile
  utilizzare i comandi di navigazione tabella per controllare le
  intestazioni.

## Mappe

* NVDA emette dei segnali acustici per le posizioni presenti nella mappa.

## Microsoft Edge

* Vengono annunciate correttamente le notifiche dei download dei file.
* Il Supporto per Microsoft Edge è in continuo sviluppo.

## Impostazioni

* Vengono annunciate automaticamente le informazioni di avanzamento delle
  operazioni di Windows Update.
* Le informazioni delle barre di avanzamento non vengono più lette due
  volte.
* Se la ricerca di un'impostazione richiede troppo tempo, NVDA si comporterà
  come se non ci siano risultati da visualizzare.
* Il gruppo impostazioni viene riconosciuto quando ci si sposta tra i
  controlli usando la navigazione ad oggetti.

## Anteprima Skype

* Viene annunciato quando un utente sta scrivendo, così come accade in Skype
  per desktop.
* Implementazione parziale della funzionalità di lettura rapida delle chat
  con ctrl+NVDA+numeri da 1 a 9, come accade in Skype Desktop.
* è possibile premere il tasto alt in combinazione con i numeri per attivare
  le schede, ossia alt-1 contatti, alt-2 elenco conversazioni, alt-3 va nel
  campo editazione della chat. Le schede devono essere attivate per
  potercisi spostare.
* Vengono lette le etichette delle caselle combinate in anteprima Skype
  novembre 2016
* Nella maggior parte dei casi, NVDA non leggerà più i messaggi Skype di
  continuo quando se ne sta controllando uno

## Store

* Dopo aver controllato la presenza di aggiornamenti di app, i nomi delle
  app nell'elenco degli aggiornamenti viene correttamente etichettato.
* viene annunciata la comparsa  dei suggerimenti di ricerca
* Mentre si scaricano contenuti quali app o film, NVDA ne leggerà il nome e
  l'avanzamento del download.

## TeamViewer Touch

* Vengono lette le etichette dei pulsanti radio.
* Vengono lette le etichette dei pulsanti.

## Bank of America/Twitter/Windows Defender Security Center

* Vengono annunciate correttamente le etichette dei pulsanti.
* Potrebbero esserci modifiche al supporto da parte di questo componente
  aggiuntivo per Windows Defender Security Center, in quanto viene inclusa
  come app universale dalla build 14986 

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

[1]: http://addons.nvda-project.org/files/get.php?file=w10

[2]: http://addons.nvda-project.org/files/get.php?file=w10-dev
