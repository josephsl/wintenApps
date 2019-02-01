# Windows 10 App Essentials #

* Autori: Joseph Lee, Derek Riemer și alți utilizatori Windows 10
* Descărcați [versiunea stabilă][1]
* Descărcați [versiunea în dezvoltare][2]
* Compatibilitate NVDA: 2018.3 - 2019.1

Acest supliment cuprinde o colecție de module pentru diverse aplicații din
Windows 10, dar și rezolvări și îmbunătățiri pentru anumite controale din
Windows 10.

Următoarele module de aplicații sau module de suport pentru unele aplicații
sunt incluse (verificați fiecare secțiune a aplicației pentru detalii cu
privire la ceea ce este inclus):

* Centru de acțiuni
* Alarme și Ceas.
* Calendar
* Calculator (modern).
* Cortana
* Centrul de Feedback
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

* This add-on requires Windows 10 Version 1803 (build 17134) or later and
  NVDA 2018.3 or later. For best results, use the add-on with latest Windows
  10 stable release (build 17763) and latest stable version of NVDA.
* Unele caracteristici ale suplimentului fac sau vor face parte din
  cititorul de ecran NVDA.
* For entries not listed below, you can assume that features are part of
  NVDA, no longer applicable as the add-on does not support old Windows 10
  releases, or changes were made to Windows 10 and apps that makes entries
  no longer applicable.
* Standalone update check from this add-on has been removed. For future
  add-on updates, please use Add-on Updater add-on.

Pentru o listă a modificărilor efectuate la fiecare versiune a
suplimentului, consultați documentul [jurnalelor de modificări pentru
versiunile suplimentului][3].

## General

* Au fost făcute modificări interne care să facă acest supliment compatibil
  cu viitoarele versiuni de NVDA.
* Mici modificări la modul în care unele mesaje sunt prezentate în alte
  limbi decât engleză.
* Elementele de submeniu sunt recunoscute corespunzător în diverse
  aplicații, incluzând meniul context pentru comenzile din meniul Start și
  meniul de aplicație al Microsoft Edge (Redstone 5).
* Anumite dialoguri sunt acum recunoscute ca dialoguri corespunzătoare și
  sunt raportate ca atare. Acestea includ dialogul Insider Preview
  (aplicația setări). Aceasta face parte acum din NVDA 2018.3.
* NVDA poate anunța numărul de sugestii la efectuarea unei căutări în
  majoritatea cazurilor. Această opțiune este controlată de „informația
  poziției obiectului în dialogul prezentării obiectului.
* În anumite meniuri contextuale (cum ar fi în Edge), informația poziției
  (e.x. 1 din 2) nu mai este anunțată.
* Următoarele evenimente UIA sunt recunoscute: schimbarea poziției textului
  activ, controler pentru, început de tragere, tragere finalizată, element
  selectat, stare element, schimbare regiune activă, notificare, alertă de
  sistem, indiciu deschis, fereastră deschisă. Cu NVDA-ul setat să ruleze cu
  diagnosticarea activată, aceste evenimente vor fi urmărite, iar pentru
  evenimentul de tip notificare UIA, se va auzi un ton de diagnosticare dacă
  notificările nu vin din aplicația curentă, ci de altundeva.
* Indiciile din Edge și alte aplicații universale sunt recunoscute și vor fi
  anunțate.
* La deschiderea, închiderea sau comutarea între spațiile de lucru virtuale,
  NVDA va anunța ID-ul spațiului de lucru curent (spațiu de lucru 2).
* NVDA nu mai anunță „dimensiune text start meniu” la schimbarea rezoluției
  ecranului sau a orientării.

## Centru de acțiuni

* Brightness quick action is now a button instead of a toggle button. This
  will be part of NVDA 2019.1.
* Various status changes such as Focus Assist and Brightness will be
  reported. This will be part of NVDA 2019.1.

## Alarme și ceas

* Time picker values are now announced, noticeable when moving focus to
  picker controls. This also affects the control used to select when to
  restart to finish installing Windows updates. This will be part of NVDA
  2019.1.

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

## Mail

* Când examinați elemente dinn lista de mesaje, puteți să folosiți comenzile
  de navigare ale tabelului pentru a examina antetele mesajelor. Rețineți că
  navigarea printre rânduri (mesaje) nu este suportată.
* La scrierea unui mesaj, aspectele sugestiilor de menționare a arondului
  sunt indicate de sunete.

## Hărți

* NVDA redă bipul locației pentru locațiile hărții.
* Atunci când se utilizează vedere din stradă laterală și în cazul în care
  opțiunea "utilizare tastatură" este activată, NVDA va anunța adrese pe
  măsură ce utilizați tastele săgeată pentru a naviga pe hartă.

## Microsoft Edge

* Autocompletarea textului va fi urmărită și anunțată în omnibara de adrese.
* NVDA will no longer play suggestion sound when pressing F11 to toggle full
  screen.

## Tastatură modernă

Notă: majoritatea caracteristicilor de mai jos nu fac parte din NVDA 2018.3.

* Suport pentru panoul de intrare floating Emoji în versiunea 1709 (Fall
  Creators Update) și pentru panoul nou din compilarea 17661 sau mai nouă,
  și modificările făcute 19H1 (compilarea 18262). Dacă folosiți versiuni mai
  vechi decât 2018.4, pentru cea mai bună experiență la citirea
  emoji-urilor, folosiți sintetizatorul Windows OneCore. Dacă versiunea
  2018.4 sau mai nouă este în uz, activați setarea Unicode Consortium din
  setările de vorbire ale NVDA și setați nivelul simbolurilor la „unele” sau
  la „fără”.
* Suport pentru sugestiile de intrare a tastaturii hardware în compilarea
  1803 sau mai nouă.
* În compilările post-1709, NVDA va anunța primul emoji selectat când se
  deschide panoul emoji. Aceasta este mai observabilă în compilarea 18262 și
  mai nouă, în care panoul emoji se poate deschide la ultima categorie în
  care s-a navigat, cum ar fi redarea modificatoarelor tonurilor de sunat la
  deschiderea categoriei Persoane.
* Suport pentru anunțarea elementelor planșetei cloud în versiunea 1809
  (compilarea 17666 și mai nouă.
* S-a redus verbozitatea inutilă la lucrul cu tastatura modernă și
  caracteristicile sale. Acestea includ neanunțarea "Microsoft Candidate UI"
  la deschiderea sugestiilor de introducere a tastaturii hardware și starea
  în modul silențios atunci când anumite taste ale tastaturii tactile
  generează un eveniment de schimbare a numelui pe unele sisteme.
* NVDA nu va mai reda tonuri de eroare sau nu va mai face nimic la
  închiderea panoului emoji în compilări mai recente Insider Preview 19H1.
* În versiunea 1809 (October 2018 Update) și mai nouă, NVDA va anunța
  rezultatele căutării pentru emoji-uri dacă este posibil.

## Persoane

* La căutarea de contacte, va fi anunțată prima sugestie, în particular dacă
  se folosesc versiuni recente ale aplicației.

## Setări

* Anumite informații, cum ar fi progresul Windows Update, sunt acum
  raportate automat, incluzând stocarea sensului sau widget-ul curățare
  disc.
* Valorile barei de progres și alte informații nu mai sunt anunțate de două
  ori.
* Pentru unele casete combinate și butoane rotative, NVDA nu va mai eșua la
  recunoașterea etichetelor și/sau anunțarea schimbărilor valorii.
* Bipurile barei de progres a volumului audio nu mai sunt auzite în
  compilarea 1803 sau mai nouă.
* Sunt anunțate mai multe mesaje în legătură cu stadiul actualizărilor
  Windows, mai exact atunci când Windows Update întâmpină erori.
* NVDA nu va mai fi nevoit să nu facă nimic sau să redea tonuri de eroare
  dacă se utilizează comenzile de navigare ale obiectului în anumite
  circumstanțe.
* Dialogul de tip memento al Windows Update este recunoscut așa cum trebuie.

## Skype

Notă: intrările de mai jos nu vor funcționa așa cum trebuie în aplicația
universală Skype 14.

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
