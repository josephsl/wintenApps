# Windows 10 App Essentials #

* Autori: Joseph Lee, Derek Riemer și alți utilizatori Windows 10
* Descărcați [versiunea stabilă][1]
* Descărcați [versiunea în dezvoltare][2]
* NVDA compatibility: 2019.1 to 2019.2

Acest supliment cuprinde o colecție de module pentru diverse aplicații din
Windows 10, dar și rezolvări și îmbunătățiri pentru anumite controale din
Windows 10.

Următoarele module de aplicații sau module de suport pentru unele aplicații
sunt incluse (verificați fiecare secțiune a aplicației pentru detalii cu
privire la ceea ce este inclus):

* Calculator (modern).
* Calendar
* Cortana (Classic and Conversations)
* Centrul de Feedback
* Mail
* Hărți
* Microsoft Edge
* Microsoft Store
* Modern keyboard (emoji panel/dictation/hardware input suggestions/cloud
  clipboard items in Version 1709 and later)
* Persoane
* Setări (setări de sistem, Windows+I)
* Meteo.
* Diverse module de control precum comenzile din meniul start.

Note:

* This add-on requires Windows 10 Version 1809 (build 17763) or later and
  NVDA 2019.1 or later. For best results, use the add-on with latest Windows
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
* The following UIA events are recognized: controller for, drag start, drag
  cancel, drag complete, element selected, item status, live region change,
  notification, system alert, text change, tooltip opened, window
  opened. With NVDA set to run with debug logging enabled, these events will
  be tracked, and for UIA notification event, a debug tone will be heard if
  notifications come from somewhere other than the currently active app.
* It is possible to tracke only specific events and/or events coming from
  specific apps.
* Tooltips from Edge and universal apps are recognized and will be
  announced. This will be part of NVDA 2019.3.
* When opening, closing, or switching between virtual desktops, NVDA will
  announce current desktop name (desktop 2, for example).
* NVDA nu mai anunță „dimensiune text start meniu” la schimbarea rezoluției
  ecranului sau a orientării.
* In Version 1903 (May 2019 Update), NVDA will announce volume and
  brightness changes immediately if focused on File Explorer. This is now
  part of NVDA 2019.2.
* App name and version for various Microsoft Store apps are now shown
  correctly. This will be part of NVDA 2019.3.

## Calculator

* When ENTER or Escape is pressed, NVDA will announce calculation results.
* Pentru calcule precum convertorul de unitate și convertorul valutar, NVDA
  va anunța rezultatele de îndată ce vor fi introduse calculele.
* NVDA nu va mai anunța „rubrică nivel” pentru rezultatele calculatorului.
* NVDA will notify if maximum digit count has been reached while entering
  expressions.
* Added support for always on mode in future Calculator releases.

## calendar

* NVDA nu mai anunță „Editare” sau „doar citire” în corpul mesajului sau în
  alte câmpuri.

## Cortana

Most items are no longer applicable on Version 1903 and later. Classic
Cortana refers to older Cortana interface which was part of Start menu.

* Textual responses from Cortana (both Classic and Conversations UI) are
  announced in most situations (if using Classic Cortana, reopen Start menu
  and try searching again if responses are not announced).
* NVDA va fi silențios atunci când vorbiți cu Cortana prin voce.
* In Classic Cortana, NVDA will announce reminder confirmation after you set
  one.
* In build 18945 and later, modern search experience in File Explorer
  powered by Cortana user interface is supported.

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
  app. This is now part of NVDA 2019.2.

## Hărți

* NVDA redă bipul locației pentru locațiile hărții.
* Atunci când se utilizează vedere din stradă laterală și în cazul în care
  opțiunea "utilizare tastatură" este activată, NVDA va anunța adrese pe
  măsură ce utilizați tastele săgeată pentru a naviga pe hartă.

## Microsoft Edge

This refers to classic EdgeHTML-based Microsoft Edge.

* Text auto-complete will be tracked and announced in address omnibar. This
  will be part of NVDA 2019.3.
* NVDA will no longer play suggestion sound when pressing F11 to toggle full
  screen. This will be part of NVDA 2019.3.
* Removed suggestions sound playback for address omnibar. This will be part
  of NVDA 2019.3.

## Microsoft Store

* După căutarea actualizărilor aplicației, nume de aplicații în lista
  aplicațiilor care urmează să fie actualizate sunt etichetate corect.
* La descărcarea conținutului, cum ar fi aplicații și filme, NVDA va anunța
  numele produsului și progresul descărcării.

## Tastatură modernă

Most features below are now part of NVDA 2018.3 or later.

* Support for Emoji input panel in Version 1709 (Fall Creators Update) and
  later, including the redesigned panel in Version 1809 (build 17661 and
  later) and changes made in 19H1 (build 18262 and later, including kaomoji
  and symbols categories in build 18305). This is also applicable in build
  18963 and later as the app has been renamed. If using NVDA releases
  earlier than 2018.4, for best experience when reading emojis, use Windows
  OneCore speech synthesizer. If 2018.4 or later is in use, enable Unicode
  Consortium setting from NvDA's speech settings and set symbol level to
  "some" or higher.
* NVDA will no longer announce "clipboard" when there are items in the
  clipboard under some circumstances.
* On some systems running Version 1903 (May 2019 Update), NVDA will no
  longer appear to do nothing when emoji panel opens.
* Added support for modern Chinese, Japanese, and Korean (CJK) IME
  candidates interface introduced in 20H1 build 18965 and later.

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
* In more recent revisions of Version 1803 and later, due to changes to
  Windows Update procedure for feature updates, a "download and install now"
  link has been added. NVDA will now announce the title for the new update
  if present.

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
