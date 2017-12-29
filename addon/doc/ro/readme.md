# Windows 10 App Essentials #

* Autori: Joseph Lee, Derek Riemer și alți utilizatori Windows 10 
* Descărcați [versiunea stabilă][1]
* Descărcați [versiunea în dezvoltare][2]

This add-on is a collection of app modules for various Windows 10 apps, as
well as enhancements and fixes for certain windows 10 controls.

Următoarele module de aplicații sau module de suport pentru unele aplicații
sunt incluse (verificați fiecare secțiune a aplicației pentru detalii cu
privire la ceea ce este inclus):

* Alarme și ceas.
* Calendar
* Calculator (modern).
* Cortana
* Bară de jocuri
* Mail
* Hărți
* Microsoft Edge
* Tastatură modernă (sugestii de intrare a panoului/hardware emoji în
  versiunea 1709 și mai nouă)
* Persoane
* Setări (setări de sistem, Windows+I)
* Skype (aplicație universală)
* Magazin
* Meteo.
* Diverse module de control precum tile-urile din meniul start.

Note: this add-on requires Windows 10 Version 1703 (build 15063) or later
and NVDA 2017.3 or later. For best results, use the add-on with latest
Windows 10 stable build (build 16299) and latest stable version of
NVDA. Also, after changing update settings for the add-on, be sure to save
NVDA settings.

## General

* În meniurile contextuale ale tile-urilor din cadrul Start Meniu,
  submeniurile sunt recunoscute corect.
* Certain dialogs are now recognized as proper dialogs, including Insider
  Preview dialog (settings app).
* NVDA poate anunța numărul de sugestii la efectuarea unei căutări în
  majoritatea cazurilor. Această opțiune este controlată de „informația
  poziției obiectului în dialogul prezentării obiectului.
* În anumite meniuri contextuale (cum ar fi în Edge), informația poziției
  (e.x. 1 din 2) nu mai este anunțată.
* Următoarele evenimente UIA sunt recunoscute: Controler pentru, schimbarea
  regiunii live, alertă de sistem, element selectat, fereastră deschisă. Cu
  NVDA-ul setat să ruleze cu diagnosticarea activată, aceste evenimente vor
  fi urmărite.
* Added ability to check for add-on updates (automatic or manual) via
  Windows 10 App Essentials dialog found in NvDA Preferences menu. By
  default, stable and development versions will check for new updates
  automatically on a weekly or daily basis, respectively.
* In some apps, live region text is announced. This includes alerts in Edge,
  results in Calculator and others. Note that this may result in
  double-speaking in some cases.

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
* NVDA will be silent when talking to Cortana via voice.
* NVDA va anunța o confirmare memento după ce ați setat unul.

## Bară de jocuri

* NVDA va anunța aspectul barei de jocuri. Datorită limitărilor tehnice,
  NVDA nu poate interacționa pe deplin cu bara de jocuri.

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

* Notifications such as file downloads and various webpage alerts are
  announced.

## Tastatură modernă

* Suport pentru panoul de intrare floating Emoji în versiunea 1709 (Fall
  Creators Update). Pentru cea mai bună experiență la citirea moji-urilor,
  folosiți sintetizatorul Windows OneCore.
* Suport pentru sugestiile de intrare a tastaturii hardware în compilarea
  17040 sau mai nouă.

## Persoane

* La căutarea contactelor, un sunet se va reda dacă există rezultate de
  căutare.

## Setări

* Certain information such as Windows Update progress is reported
  automatically.
* Valorile barei de progres și alte informații nu mai sunt anunțate de două
  ori.
* Grupurile de setări sunt recunoscute la utilizarea navigării obiectului
  pentru a naviga printre controale.
* For some combo boxes, NVDA will no longer fail to recognize labels and/or
  announce value changes.
* Bipurile barei de progres a volumului audio nu mai sunt auzite în
  compilarea 17035 sau mai nouă.

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
* When downloading content such as apps and movies, NVDA will announce
  product name and download progress.

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
