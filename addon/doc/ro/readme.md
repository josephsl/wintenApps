# Windows 10 App Essentials #

* Autori: Joseph Lee, Derek Riemer și alți utilizatori Windows 10
* Descărcați [versiunea stabilă][1]
* Descărcați [versiunea în dezvoltare][2]
* NVDA compatibility: 2018.4 to 2019.1

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
* Modern keyboard (emoji panel/dictation/hardware input suggestions/cloud
  clipboard items in Version 1709 and later)
* Persoane
* Setări (setări de sistem, Windows+I)
* Magazin
* Meteo.
* Diverse module de control precum comenzile din meniul start.

Note:

* This add-on requires Windows 10 Version 1803 (build 17134) or later and
  NVDA 2018.4 or later. For best results, use the add-on with latest Windows
  10 stable release (build 18362) and latest stable version of NVDA.
* Unele caracteristici ale suplimentului fac sau vor face parte din
  cititorul de ecran NVDA.
* Pentru intrările care nu sunt listate mai jos, puteți presupune că
  funcționalitățile fac parte din NVDA, nu mai sunt aplicabile, întrucât
  suplimentul nu mai suportă versiunile vechi de Windows 10, sau că au fost
  efectuate modificări la Windows 10 și la aplicații, care fac ca intrările
  să nu mai fie aplicabile.

Pentru o listă a modificărilor efectuate la fiecare versiune a
suplimentului, consultați documentul [jurnalelor de modificări pentru
versiunile suplimentului][3].

## General

* NVDA will no longer play error tones or do nothing if this add-on becomes
  active from Windows 7, Windows 8.1, and unsupported releases of Windows
  10.
* Elementele de submeniu sunt recunoscute corespunzător în diverse
  aplicații, incluzând meniul context pentru comenzile din meniul Start și
  meniul de aplicație al Microsoft Edge (Redstone 5).
* Anumite dialoguri sunt acum recunoscute ca dialoguri corespunzătoare și
  sunt raportate ca atare. Acestea includ dialogul Insider Preview
  (aplicația setări).
* NVDA poate anunța numărul de sugestii la efectuarea unei căutări în
  majoritatea cazurilor. Această opțiune este controlată de „informația
  poziției obiectului din dialogul prezentării obiectului, găsit în panoul
  de setări NVDA.
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
* When opening, closing, or switching between virtual desktops, NVDA will
  announce current desktop name (desktop 2, for example).
* NVDA nu mai anunță „dimensiune text start meniu” la schimbarea rezoluției
  ecranului sau a orientării.
* In Version 1903 (May 2019 Update), NVDA will announce volume and
  brightness changes immediately.

## Centru de acțiuni

* Brightness quick action is now a button instead of a toggle button. This
  is now part of NVDA 2019.1.
* Various status changes such as Focus Assist and Brightness will be
  reported. This is now part of NVDA 2019.1.

## Alarme și ceas

* Time picker values are now announced, noticeable when moving focus to
  picker controls. This also affects the control used to select when to
  restart to finish installing Windows updates. This is now part of NVDA
  2019.1.

## Calculator

* Când se apasă Enter sau Escape, NVDA anunță rezultatele calculului.
* Pentru calcule precum convertorul de unitate și convertorul valutar, NVDA
  va anunța rezultatele de îndată ce vor fi introduse calculele.
* NVDA nu va mai anunța „rubrică nivel” pentru rezultatele calculatorului.
* NVDA will notify if maximum digit count has been reached while entering
  expressions.

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
* NVDA will no longer do anything or play error tones after closing this
  app. This is now part of NVDA 2019.1.

## Hărți

* NVDA redă bipul locației pentru locațiile hărții.
* Atunci când se utilizează vedere din stradă laterală și în cazul în care
  opțiunea "utilizare tastatură" este activată, NVDA va anunța adrese pe
  măsură ce utilizați tastele săgeată pentru a naviga pe hartă.

## Microsoft Edge

* Autocompletarea textului va fi urmărită și anunțată în omnibara de adrese.
* NVDA nu va mai reda sunete de sugestie la apăsarea tastei F11 pentru
  activarea/dezactivarea ecranului complet.

## Tastatură modernă

Notă: majoritatea caracteristicilor de mai jos fac parte din NVDA 2018.3.

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
* NVDA will no longer play error tones or do nothing when closing emoji
  panel in more recent 19H1 Insider Preview builds. This is now part of NVDA
  2019.1.
* In Version 1809 (October 2018 Update) and later, NVDA will announce search
  results for emojis if possible. This is now part of NVDA 2019.1.
* NVDA will no longer announce "clipboard" when there are items in the
  clipboard under some circumstances.
* On some systems running Version 1903 (May 2019 Update), NVDA will no
  longer appear to do nothing when emoji panel opens.

## Persoane

* La căutarea de contacte, va fi anunțată prima sugestie, în particular dacă
  se folosesc versiuni recente ale aplicației.

## Setări

* Certain information such as Windows Update progress is reported
  automatically, including Storage sense/disk cleanup widget and errors from
  Windows Update.
* Valorile barei de progres și alte informații nu mai sunt anunțate de două
  ori.
* Pentru unele casete combinate și butoane rotative, NVDA nu va mai eșua la
  recunoașterea etichetelor și/sau anunțarea schimbărilor valorii.
* Bipurile barei de progres a volumului audio nu mai sunt auzite în
  compilarea 1803 sau mai nouă.
* NVDA nu va mai fi nevoit să nu facă nimic sau să redea tonuri de eroare
  dacă se utilizează comenzile de navigare ale obiectului în anumite
  circumstanțe.
* Dialogul de tip memento al Windows Update este recunoscut așa cum trebuie.
* Odd control labels seen in certain Windows 10 installations has been
  corrected.

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
