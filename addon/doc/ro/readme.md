# Windows 10 App Essentials #

* Autori: Joseph Lee, Derek Riemer și alți utilizatori Windows 10
* Descărcați [versiunea stabilă][1]
* Descărcați [versiunea în dezvoltare][2]

Acest supliment cuprinde o colecție de module pentru diverse aplicații din
Windows 10, dar și rezolvări și îmbunătățiri pentru anumite controale din
Windows 10.

Următoarele module de aplicații sau module de suport pentru unele aplicații
sunt incluse (verificați fiecare secțiune a aplicației pentru detalii cu
privire la ceea ce este inclus):

* Action center
* Alarme și ceas.
* Calendar
* Calculator (modern).
* Cortana
* Centrul de Feedback
* Bară de jocuri
* Mail
* Hărți
* Microsoft Edge
* Tastatură modernă (sugestii de intrare a panoului/hardware emoji/elemente
  ale planșetei cloud în versiunea 1709 și mai nouă)
* Persoane
* Setări (setări de sistem, Windows+I)
* Skype (aplicație universală)
* Magazin
* Meteo.
* Diverse module de control precum comenzile din meniul start.

Note:

* This add-on requires Windows 10 Version 1709 (build 16299) or later and
  NVDA 2018.3 or later. For best results, use the add-on with latest Windows
  10 stable release (build 17134) and latest stable version of NVDA. Note
  that until further notice, Version 1809 (build 17763) is not available
  from Microsoft.
* Unele caracteristici ale suplimentului fac sau vor face parte din
  cititorul de ecran NVDA.
* Pentru intrările care nu sunt listate mai jos, puteți presupune că
  funcționalitățile fac parte din NVDA și nu mai sunt aplicabile, întrucât
  suplimentul nu mai suportă versiunile vechi de Windows 10, sau că au fost
  efectuate modificări la aplicații, care fac ca intrările să nu mai fie
  aplicabile.

Pentru o listă a modificărilor efectuate la fiecare versiune a
suplimentului, consultați documentul [jurnalelor de modificări pentru
versiunile suplimentului][3].

## General

* If Add-on Updater add-on is installed, that add-on will check for Windows
  10 App Essentials updates.
* Default update check interval has changed to weekly checks for both stable
  and development releases. This is applicable if the add-on itself checks
  for updates.
* Elementele de submeniu sunt recunoscute corespunzător în diverse
  aplicații, incluzând meniul context pentru comenzile din meniul Start și
  meniul de aplicație al Microsoft Edge (Redstone 5).
* Certain dialogs are now recognized as proper dialogs and reported as such,
  including Insider Preview dialog (settings app). This is now part of NVDA
  2018.3.
* NVDA poate anunța numărul de sugestii la efectuarea unei căutări în
  majoritatea cazurilor. Această opțiune este controlată de „informația
  poziției obiectului în dialogul prezentării obiectului.
* În anumite meniuri contextuale (cum ar fi în Edge), informația poziției
  (e.x. 1 din 2) nu mai este anunțată.
* The following UIA events are recognized: active text position change,
  controller for, drag start, drag cancel, drag complete, element selected,
  item status, live region change, notification, system alert, tooltip
  opened, window opened. With NVDA set to run with debug logging enabled,
  these events will be tracked, and for UIA notification event, a debug tone
  will be heard if notifications come from somewhere other than the
  currently active app.
* Sunt anunțate Notificările versiunilor mai noi ale aplicațiilor din
  Windows 10 versiunea 1709 (compilare 16299) și mai nouă. NVDA 2018.2
  suportă asta, iar 2018.3 vine cu suport pentru mai multe notificări.
* Indiciile din Edge și alte aplicații universale sunt recunoscute și vor fi
  anunțate.
* La deschiderea, închiderea sau comutarea între spațiile de lucru virtuale,
  NVDA va anunța ID-ul spațiului de lucru curent (spațiu de lucru 2).
* NVDA nu mai anunță „dimensiune text start meniu” la schimbarea rezoluției
  ecranului sau a orientării.

## Action center

* Brightness quick action is now a button instead of a toggle button.
* Various status changes such as Focus Assist and Brightness will be
  reported.

## Alarme și ceas

* Valorile selectorului de dată sunt acum anunțate, de observat atunci când
  focalizarea se deplasează la selectorul de comenzi. De asemenea, aceasta
  afectează comanda utilizată pentru a selecta când să repornească pentru
  finalizarea actualizărilor Windows.

## Calculator

* Când se apasă Enter sau Escape, NVDA anunță rezultatele calculului.
* Pentru calcule precum convertorul de unitate și convertorul valutar, NVDA
  va anunța rezultatele de îndată ce vor fi introduse calculele.
* NVDA nu va mai anunța „rubrică nivel” pentru rezultatele calculatorului.

## calendar

* NVDA nu mai anunță „Editare” sau „doar citire” în corpul mesajului sau în
  alte câmpuri.

## Cortana

* Răspunsurile textuale de la Cortana sunt anunțate în cele mai multe
  situații (dacă nu, redeschideți meniul start și încercați căutarea din
  nou).
* NVDA va fi silențios atunci când vorbiți cu Cortana prin voce.
* NVDA va anunța o confirmare memento după ce ați setat unul.

## Centrul de Feedback

* Pentru versiunile mai noi de aplicații, NVDA nu va mai anunța categoriile
  de feedback de două ori.

## Bară de jocuri

* NVDA va anunța aspectul barei de jocuri. Datorită limitărilor tehnice,
  NVDA nu poate interacționa pe deplin cu bara de jocuri într-o compilare
  mai veche decât 17723.

## Mail

* When reviewing items in messages list, you can now use table navigation
  commands to review message headers. Note that navigating between rows
  (messages) is not supported.
* La scrierea unui mesaj, aspectele sugestiilor de menționare a arondului
  sunt indicate de sunete.

## Hărți

* NVDA redă bipul locației pentru locațiile hărții.
* Atunci când se utilizează vedere din stradă laterală și în cazul în care
  opțiunea "utilizare tastatură" este activată, NVDA va anunța adrese pe
  măsură ce utilizați tastele săgeată pentru a naviga pe hartă.

## Microsoft Edge

* Notificările precum descărcări de fișiere și diverse alerte de pe paginile
  web, dar și disponibilitatea funcției Reading view (dacă se utilizează
  versiunea 1709 și mai nouă) sunt anunțate.
* Text auto-complete will be tracked and announced in address omnibar.

## Tastatură modernă

Note: most features below are now part of NVDA 2018.3.

* Support for Emoji input panel in Version 1709 (Fall Creators Update) and
  later, including the redesigned panel in Version 1809 (build 17661 and
  later) and changes made in 19H1 (build 18262). For best experience when
  reading emojis, use Windows OneCore speech synthesizer.
* Suport pentru sugestiile de intrare a tastaturii hardware în compilarea
  1803 sau mai nouă.
* In post-1709 builds, NVDA will announce the first selected emoji when
  emoji panel opens. This is more noticeable in build 18262 and later where
  emoji panel may open to last browsed category, such as displaying skin
  tone modifier when opened to People category.
* Support for announcing cloud clipboard items in Version 1809 (build 17666
  and later).
* S-a redus verbozitatea inutilă la lucrul cu tastatura modernă și
  caracteristicile sale. Acestea includ neanunțarea "Microsoft Candidate UI"
  la deschiderea sugestiilor de introducere a tastaturii hardware și starea
  în modul silențios atunci când anumite taste ale tastaturii tactile
  generează un eveniment de schimbare a numelui pe unele sisteme.
* NVDA will no longer play error tones or do nothing when closing emoji
  panel in more recent Insider Preview builds.

## Persoane

* La căutarea de contacte, va fi anunțată prima sugestie, în particular dacă
  se folosesc versiuni recente ale aplicației.

## Setări

* Certain information such as Windows Update progress is reported
  automatically, including Storage sense/disk cleanup widget.
* Valorile barei de progres și alte informații nu mai sunt anunțate de două
  ori.
* Grupurile de setări sunt recunoscute la utilizarea navigării obiectului
  pentru a naviga printre controale.
* For some combo boxes and radio buttons, NVDA will no longer fail to
  recognize labels and/or announce value changes.
* Bipurile barei de progres a volumului audio nu mai sunt auzite în
  compilarea 1803 sau mai nouă.
* Sunt anunțate mai multe mesaje în legătură cu stadiul actualizărilor
  Windows, mai exact atunci când Windows Update întâmpină erori.

## Skype

Note: the below entries won't work properly in Skype 14 universal app.

* Textul indicatorului de scriere este anunțat la fel ca Skype pentru
  Desktop.
* Comenzile Control+NvDA+1, 2, 3, 4, 5, 6, 7, 8, 9 și 0, utilizate în Skype
  pentru Desktop la citirea istoricului conversației recente și pentru
  deplasarea obiectului navigator la intrările conversației, sunt
  disponibile și în Skype UWP.
* Puteți apăsa Alt+rândul cu numere pentru a localiza și a vă deplasa la
  conversații (1), lista de contacte (2), boți (3) și câmpul de editare al
  chatului dacă e vizibil (4). Rețineți că aceste comenzi vor funcționa
  corespunzător dacă actualizarea Skype-ului lansată în martie 2017 este
  instalată.
* NVDA nu mai anunță „Mesaj Skype” la examinarea mesajelor pentru
  majoritatea cazurilor.
* Din lista istoricului mesajelor, apăsarea NVDA+D pe un element de mesaj îi
  va permite NVDA-ului să anunțe informații detaliate despre un mesaj, cum
  ar fi tip de canal, data și ora trimiterii și așa mai departe.

## Magazin

* După căutarea actualizărilor aplicației, nume de aplicații în lista
  aplicațiilor care urmează să fie actualizate sunt etichetate corect.
* La descărcarea conținutului, cum ar fi aplicații și filme, NVDA va anunța
  numele produsului și progresul descărcării.

## Meteo

* Etichete precum „vremea” și „hărțile” sunt recunoscute ca etichete
  adegvate (patch de Derek Riemer).
* atunci când citiți o prognoză, utilizați săgețile stânga și  dreapta
  pentru a vă deplasa între elemente. Utilizați săgețile sus și jos pentru a
  citi articolele individuale. De exemplu, apăsând pe săgeata din dreapta
  poate raporta un "luni: 79 de grade, parțial noros, ...", apăsând săgeata
  în jos va spune "luni" Apoi, apăsând din nou va citi elementul următor (La
  fel ca temperatura). Acest lucru funcționează în prezent pentru
  previziunile zilnice și orare.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
