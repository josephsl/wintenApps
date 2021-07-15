# Windows App Essentials #

* Autori: Joseph Lee, Derek Riemer și alți utilizatori Windows 10
* Descărcați [versiunea stabilă][1]
* Descărcați [versiunea în dezvoltare][2]
* NVDA compatibility: 2020.4 and beyond

Note: Originally called Windows 10 App Essentials, it was renamed to Windows
App Essentials in 2021 to support Windows 10 and future releases such as
Windows 11. Parts of this add-on will still refer to the original add-on
name.

This add-on is a collection of app modules for various modern Windows apps,
as well as enhancements and fixes for certain controls found in Windows 10
and later.

Următoarele module de aplicații sau module de suport pentru unele aplicații
sunt incluse (verificați fiecare secțiune a aplicației pentru detalii cu
privire la ceea ce este inclus):

* Calculator (modern)
* Calendar
* Cortana (Conversations)
* Mail
* Hărți
* Microsoft Solitaire Collection
* Microsoft Store
* Modern keyboard (emoji panel/dictation/hardware input
  suggestions/clipboard history/modern input method editors)
* Persoane
* Setări (setări de sistem, Windows+I)
* Meteo
* Miscellaneous modules for controls such as Start Menu tiles

Note:

* This add-on requires Windows 10 20H2 (build 19042) or later. For best
  results, use the add-on with latest Windows release (Windows 10 21H1/build
  19043).
* Although installation is possible, this add-on does not support Windows
  Enterprise LTSC (Long-Term Servicing Channel) and Windows Server releases.
* Support for Windows 11 is experimental, and some features will not work
  (see relevant entries for details).
* Unele caracteristici ale suplimentului fac sau vor face parte din
  cititorul de ecran NVDA.
* For entries not listed below, you can assume that features are part of
  NVDA, no longer applicable as the add-on does not support unsupported
  Windows releases such as old Windows 10 versions, or changes were made to
  Windows and apps that makes entries no longer applicable.
* Some apps support compact overlay mode (always on top in Calculator, for
  example), and this mode will not work properly with portable version of
  NVDA.

Pentru o listă a modificărilor efectuate la fiecare versiune a
suplimentului, consultați documentul [jurnalelor de modificări pentru
versiunile suplimentului][3].

## General

* NVDA poate anunța numărul de sugestii la efectuarea unei căutări în
  majoritatea cazurilor. Această opțiune este controlată de „informația
  poziției obiectului din dialogul prezentării obiectului, găsit în panoul
  de setări NVDA.
* When searching in Start menu or File Explorer in Windows 10 1909 (November
  2019 Update) and later, instances of NVDA announcing search results twice
  when reviewing results are less noticeable, which also makes braille
  output more consistent when reviewing items.
* In addition to UIA event handlers provided by NVDA, the following UIA
  events are recognized: drag start, drag cancel, drag complete, drop target
  drag enter, drop target drag leave, drop target dropped. With NVDA's log
  level set to debug, these events will be tracked, and for UIA notification
  event, a debug tone will be heard if notifications come from somewhere
  other than the currently active app. Some events will provide additional
  information such as element count in controller for event, state of the
  element for state change event, and item text for item status event.
* It is possible to tracke only specific events and/or events coming from
  specific apps.
* When opening, closing, reordering (Windows 11), or switching between
  virtual desktops, NVDA will announce active virtual desktop name (desktop
  2, for example).
* NVDA will no longer announce Start menu size text when changing screen
  resolutions or orientation.
* When arranging Start menu tiles or Action Center quick actions with
  Alt+Shift+arrow keys, NVDA will announce information on dragged items or
  new position of the dragged item.
* Announcements such as volume/brightness changes in File Explorer and app
  update notifications from Microsoft Store can be suppressed by turning off
  Report Notifications in NVDA's object presentation settings.

## Calculator

* NVDA will no longer announce graphing calculator screen message twice.

## Calendar

* NVDA nu mai anunță „Editare” sau „doar citire” în corpul mesajului sau în
  alte câmpuri.

## Cortana

Most items are applicable when using Cortana Conversations (Windows 10 2004
and later).

* Textual responses from Cortana are announced in most situations.
* NVDA va fi silențios atunci când vorbiți cu Cortana prin voce.
* In Windows 10 1909 (November 2019 Update) and later, modern search
  experience in File Explorer powered by Windows Search user interface is
  supported.

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

## Microsoft Solitaire Collection

* NVDA will announce names of cards and card decks.

## Microsoft Store

* După căutarea actualizărilor aplicației, nume de aplicații în lista
  aplicațiilor care urmează să fie actualizate sunt etichetate corect.
* When downloading content such as apps and movies, NVDA will announce
  product name and download progress (does not work properly in updated
  Microsoft Store in Windows 11).

## Tastatură modernă

This includes emoji panel, clipboard history, dictation, hardware input
suggestions, and modern input method editors for certain languages. When
viewing emojis, for best experience, enable Unicode Consortium setting from
NVDA's speech settings and set symbol level to "some" or higher. Also, NVDA
supports updated input experience panel in Windows 11.

* When opening clipboard history, NVDA will no longer announce "clipboard"
  when there are items in the clipboard under some circumstances.
* On some systems running Windows 10 1903 (May 2019 Update) and later, NVDA
  will no longer appear to do nothing when emoji panel opens.
* When an emoji group (including kaomoji and symbols group in Windows 10
  1903 or later) is selected, NVDA will no longer move navigator object to
  certain emojis.
* Added support for updated input experience panel (combined emoji panel and
  clipboard history) in Windows 11.

## Persoane

* La căutarea de contacte, va fi anunțată prima sugestie, în particular dacă
  se folosesc versiuni recente ale aplicației.

## Setări

* Certain information such as Windows Update progress is reported
  automatically, including Storage sense/disk cleanup widget and errors from
  Windows Update.
* Valorile barei de progres și alte informații nu mai sunt anunțate de două
  ori.
* Dialogul de tip memento al Windows Update este recunoscut așa cum trebuie.
* Odd control labels seen in certain Windows installations has been
  corrected.
* NVDA will announce the name of the optional quality update link if
  present, typically named "download and install now".

## Meteo

* Etichete precum „vremea” și „hărțile” sunt recunoscute ca etichete
  adegvate (patch de Derek Riemer).
* When reading a forecast, use the left and right arrows to move between
  items. Use the up and down arrows to read the individual items. For
  example, pressing the right arrow might report "Monday: 79 degrees, partly
  cloudy, ..." pressing the down arrow will say "Monday" Then pressing it
  again will read the next item (Like the temperature). This currently works
  for daily and hourly forecasts.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
