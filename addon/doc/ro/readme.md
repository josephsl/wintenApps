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

* Acest supliment necesită Windows 10 versiunea 1709 )compilarea 16299) sau
  mai nouă și NVDA 2018.3 sau mai nou. Pentru cele mai bune rezultate,
  folosiți-l cu ultima compilare stabilă ( compilarea 17763) și cea mai
  recentă versiune stabilă a NVDA-ului.
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

* Au fost făcute modificări interne care să facă acest supliment compatibil
  cu viitoarele versiuni de NVDA.
* Dacă suplimentul Add-on Updater este instalat, va căuta actualizări pentru
  Windows 10 App Essentials.
* Intervalul implicit de căutare a actualizărilor a fost modificat la
  căutări săptămânale atât pentru versiunile stabile, cât și pentru cele în
  dezvoltare. Acesta este aplicabil dacă suplimentul însuși caută
  actualizări.
* Dacă suplimentul este setat să caute actualizări, la actualizare, dacă
  versiunea nouă necesită o versiune mai nouă de NVDA, va apărea un mesaj de
  eroare.
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
* Sunt anunțate Notificările versiunilor mai noi ale aplicațiilor din
  Windows 10 versiunea 1709 (compilare 16299) și mai nouă. NVDA 2018.2
  suportă asta, iar 2018.3 vine cu suport pentru mai multe notificări.
* Indiciile din Edge și alte aplicații universale sunt recunoscute și vor fi
  anunțate.
* La deschiderea, închiderea sau comutarea între spațiile de lucru virtuale,
  NVDA va anunța ID-ul spațiului de lucru curent (spațiu de lucru 2).
* NVDA nu mai anunță „dimensiune text start meniu” la schimbarea rezoluției
  ecranului sau a orientării.

## Centru de acțiuni

* Acțiunea rapidă a luminozității este acum un buton, nu un buton de
  activare.
* Diverse modificări de stare precum asistarea focalizării și luminozitatea,
  vor fi raportate.

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

* Notificările precum descărcări de fișiere și diverse alerte de pe paginile
  web, dar și disponibilitatea funcției Reading view (dacă se utilizează
  versiunea 1709 și mai nouă) sunt anunțate.
* Autocompletarea textului va fi urmărită și anunțată în omnibara de adrese.

## Tastatură modernă

Notă: majoritatea caracteristicilor de mai jos nu fac parte din NVDA 2018.3.

* Suport pentru panoul de intrare floating Emoji în versiunea 1709 (Fall
  Creators Update) și pentru panoul nou din compilarea 17661 sau mai nouă,
  și modificările făcute 19H1 (compilarea 18262). Pentru cea mai bună
  experiență la citirea moji-urilor, folosiți sintetizatorul Windows
  OneCore.
* Suport pentru sugestiile de intrare a tastaturii hardware în compilarea
  1803 sau mai nouă.
* În compilările post-1709, NVDA va anunța primul emoji selectat când se
  deschide panoul emoji. Aceasta este mai observabilă în compilarea 18262 și
  mai nouă, în care panoul emoji se poate deschide la ultima categorie în
  care s-a navigat.
* Suport pentru anunțarea elementelor planșetei cloud în versiunea 1809
  (compilarea 17666 și mai nouă.
* S-a redus verbozitatea inutilă la lucrul cu tastatura modernă și
  caracteristicile sale. Acestea includ neanunțarea "Microsoft Candidate UI"
  la deschiderea sugestiilor de introducere a tastaturii hardware și starea
  în modul silențios atunci când anumite taste ale tastaturii tactile
  generează un eveniment de schimbare a numelui pe unele sisteme.
* NVDA nu va mai reda tonuri de eroare sau nu va mai face nimic la
  închiderea panoului emoji în compilări mai recente Insider Preview.
* NVDA va anunța rezultatele căutării pentru emoji-uri dacă este posibil.

## Persoane

* La căutarea de contacte, va fi anunțată prima sugestie, în particular dacă
  se folosesc versiuni recente ale aplicației.

## Setări

* Anumite informații, cum ar fi progresul Windows Update, sunt acum
  raportate automat, incluzând stocarea sensului sau widget-ul curățare
  disc.
* Valorile barei de progres și alte informații nu mai sunt anunțate de două
  ori.
* Grupurile de setări sunt recunoscute la utilizarea navigării obiectului
  pentru a naviga printre controale.
* Pentru unele casete combinate și butoane rotative, NVDA nu va mai eșua la
  recunoașterea etichetelor și/sau anunțarea schimbărilor valorii.
* Bipurile barei de progres a volumului audio nu mai sunt auzite în
  compilarea 1803 sau mai nouă.
* Sunt anunțate mai multe mesaje în legătură cu stadiul actualizărilor
  Windows, mai exact atunci când Windows Update întâmpină erori.
* NVDA nu va mai fi nevoit să nu facă nimic sau să redea tonuri de eroare
  dacă se utilizează comenzile de navigare ale obiectului în anumite
  circumstanțe.
* Au fost adăugate diverse link-uri în compilarea 18282 fără vreo etichetă.
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
