# Windows 10 Aplicații Esențiale #

* Autori: Joseph Lee, Derek Riemer și alți utilizatori Windows 10 
* Descărcați [versiunea stabilă][1]
* Descărcați [versiunea în dezvoltare][2]

Acest supliment cuprinde o colecție de module pentru diverse aplicații din
Windows 10 și soluții pentru anumite comenzi din Windows 10.

Următoarele module de aplicații sau module de suport pentru unele aplicații
sunt incluse (verificați fiecare secțiune a aplicației pentru detalii cu
privire la ceea ce este inclus):

* Alarme și ceas.
* Calendar
* Calculator (modern).
* Cortana
* Bară de jocuri
* Muzică Groove
* Mail
* Hărți
* Microsoft Edge
* Persoane
* Setări (setări de sistem, Windows+I)
* Skype (aplicație universală)
* Magazin
* Meteo.
* Diverse module de control precum tile-urile din meniul start.

Notă: acest supliment necesită Windows 10 versiunea 1607 (build 14393) sau
mai nou și NVDA 2017.1 sau mai nou. Pentru rezultate foarte bune, folosiți-l
cu ultimul build stabil (build 15063) și cea mai recentă versiune stabilă a
NVDA-ului. De asemenea, după modificarea setărilor de actualizare pentru
supliment, asigurați-vă că salvați setările NVDA-ului.

## General

* În meniurile contextuale ale tile-urilor din cadrul Start Meniu,
  submeniurile sunt recunoscute corect.
* Anumite dialoguri sunt acum recunoscute ca dialoguri
  corespunzătoare. Aceasta include dialogul Insider Preview (în aplicația
  Setări) și un nou stil în dialogul UAC în build 14328 și mai nou pentru
  NvDA 2016.2.1 sau mai vechi.
* Aspectul/aproape de sugestii pentru anumite câmpuri de căutare (în special
  în aplicațiile Setări și Magazin) este anunțat prin sunete și braille. De
  asemenea, acesta include caseta de căutare a meniului Start.
* NVDA poate anunța numărul de sugestii la efectuarea unei căutări în
  majoritatea cazurilor. Această opțiune este controlată de „informația
  poziției obiectului în dialogul prezentării obiectului.
* În anumite meniuri contextuale (cum ar fi în Edge), informația poziției
  (e.g. 1 din 2) nu mai este anunțată.
* Următoarele evenimente UIA sunt recunoscute: Controler pentru, schimbarea
  regiunii în care locuiți, alertă de sistem, element selectat, fereastră
  deschisă.
* A fost adăugată abilitatea pentru căutarea actualizărilor add-on-ului
  (automat sau manual) printr-un  nou dialog Windows 10 App Essentials găsit
  în meniul NVDA, submeniul Preferințe. În mod implicit, versiunea stabilă
  și cea în dezvoltare vor căuta noi actualizări automat săptămânal sau
  zilnic.
* Abilitatea de a urmări evenimentele care provin din platforma universală
  Windows (UWP) și din aplicații, în cazul în care NVDA rulează cu
  diagnosticarea activată.
* Suport inițial pentru panoul de intrare floating moji în build-ul 16215
  sau mai nou (pentru o experiență foarte bună în citirea mojiurilor,
  utilizați sintetizatorul Windows OneCore).
* În unele aplicații, textul regiunii în care locuiți este anunțat. Aceasta
  include alertele din Edge, rezultatele din Calculator și altele. Rețineți
  faptul că asta poate rezulta o dublă vorbire în unele cazuri.
* Toast-urile nu mai sunt anunțate de multe ori în Creators Update și mai
  nou.

## Alarme și ceas

* valorile selectorului de dată sunt acum anunțate, de observat atunci când
  focalizarea se deplasează la selectorul de comenzi. De asemenea, aceasta
  afectează comanda utilizată pentru a selecta când să repornească pentru
  finalizarea actualizărilor Windows.

## Calculator

* Când se apasă Enter sau Escape, NVDA anunță rezultatele calculului.
* Pentru calcule precum convertorul de unitate și convertorul valutar, NVDA
  va anunța rezultatele de îndată ce vor fi introduse calculele.

## calendar

* NVDA nu mai anunță „Editare” sau „doar citire” în corpul mesajului sau în
  alte câmpuri.

## Cortana

* Răspunsurile textuale de la Cortana sunt anunțate în cele mai multe
  situații (dacă nu, redeschideți meniul start și încercați căutarea din
  nou).
* NVDA va fi silențios atunci când vorbiți cu Cortana prin voce.
* NVDA va anunța o confirmare memento după ce ați setat unul.

## Bară de jocuri

* NVDA va anunța aspectul barei de jocuri. Datorită limitărilor tehnice,
  NVDA nu poate interacționa pe deplin cu bara de jocuri.

## Muzică Groove

* Aspectul sugestiilor la căutarea pieselor este acum detectat.

## Mail

* Când examinați elemente în lista de mesaje, puteți să folosiți comenzile
  de navigare ale tabelului pentru a examina antetele mesajelor.
* La scrierea unui mesaj, aspectele sugestiilor de menționare a arondului
  sunt indicate de sunete.

## Hărți

* NVDA redă bipul locației pentru locațiile hărții.
* Atunci când se utilizează vedere din stradă laterală și în cazul în care
  opțiunea "utilizare tastatură" este activată, NVDA va anunța adrese pe
  măsură ce utilizați tastele săgeată pentru a naviga pe hartă.

## Microsoft Edge

* Notificările, cum ar fi descărcări de fișiere și diferite alerte ale
  paginilor web sunt acum anunțate.
* În Creators Update, NVDA nu va mai anunța "WebRuntime Content View" atunci
  când se merge pe un alt site.

## Persoane

* La căutarea contactelor, un sunet se va reda dacă există rezultate de
  căutare.

## Setări

* Anumite informații, cum ar fi o actualizare Windows în curs de descărcare
  și/sau instalare esunt raportate automat.
* Valorile barei de progres și alte informații nu mai sunt anunțate de două
  ori.
* Dacă durează ceva timp să căutați în setări, NVDA va anunța „se caută” și
  starea rezultatului căutării, cum ar fi dacă o setare nu poate fi găsită.
* Grupurile de setări sunt recunoscute la utilizarea navigării obiectului
  pentru a naviga printre controale.
* Pentru unele casete combinate, NVDA nu va mai eșua la recunoașterea
  etichetelor și/sau anunțarea schimbărilor valorii.

## Skype

* Textul indicatorului de scriere este anunțat la fel ca Skype pentru
  Desktop.
* Revenire parțială a comenzii Control+NvDA+1 până la 0 pentru citirea
  istoricului chatului recent și pentru deplasarea obiectului navigator la
  intrările chatului (la fel ca Skype pentru Desktop).
* Puteți apăsa Alt+rândul cu numere pentru a localiza și a vă deplasa la
  conversații (1), lista de contacte (2), boți (3) și câmpul de editare al
  chatului dacă e vizibil (4). Rețineți că aceste comenzi vor funcționa
  corespunzător dacă actualizarea Skype-ului lansată în martie 2017 este
  instalată.
* Etichetele Casetelor combinate pentru aplicația Skype preview, lansată în
  noiembrie 2016, sunt anunțate.
* NVDA nu mai anunță „Mesaj Skype” la examinarea mesajelor pentru
  majoritatea cazurilor.
* Diferite probleme la utilizarea Skype-ului cu afișaje braille au fost
  rezolvate, incluzând incapacitatea de a examina elementele istoricului
  mesajelor în braille.
* Din lista istoricului mesajelor, apăsarea NVDA+D pe un element de mesaj
  nu-i va permite NVDA-ului să anunțe informații detaliate despre un mesaj,
  cum ar fi tip de canal, data și ora trimiterii și așa mai departe.

## Magazin

* După căutarea actualizărilor aplicației, nume de aplicații în lista
  aplicațiilor care urmează să fie actualizate sunt etichetate corect.
* Aspectele sugestiilor de căutare sunt acum anunțate.
* La descărcarea conținutului, cum ar fi aplicații și filme, NVDA va anunța
  numele produsului și descărcarea în curs.

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
