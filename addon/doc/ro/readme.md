# Windows App Essentials #

* Authors: Joseph Lee, Derek Riemer and others
* Descărcați [versiunea stabilă][1]
* Descărcați [versiunea în dezvoltare][2]
* NVDA compatibility: 2021.2 and beyond

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

* Calculator
* Cortana
* Mail
* Hărți
* Microsoft Solitaire Collection
* Microsoft Store
* Modern keyboard (emoji panel/dictation/voice typing/hardware input
  suggestions/clipboard history/modern input method editors)
* Persoane
* Setări (setări de sistem, Windows+I)
* Meteo
* Miscellaneous modules for controls such as Start Menu tiles

Note:

* This add-on requires Windows 10 20H2 (build 19042) or later and is
  compatible with Windows 11.
* Although installation is possible, this add-on does not support Windows
  Enterprise LTSC (Long-Term Servicing Channel) and Windows Server releases.
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

* NVDA can announce suggestion count when performing a search in majority of
  cases, including when suggestion count changes as search progresses. This
  is now part of NVDA 2021.3.
* In addition to UIA event handlers provided by NVDA, the following UIA
  events are recognized: drag start, drag cancel, drag complete, drop target
  drag enter, drop target drag leave, drop target dropped, layout
  invalidated. With NVDA's log level set to debug, these events will be
  tracked, and for UIA notification event, a debug tone will be heard if
  notifications come from somewhere other than the currently active
  app. Events built into NVDA such as name change and controller for events
  will be tracked from an add-on called Event Tracker.
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

## Cortana

* Textual responses from Cortana are announced in most situations.
* NVDA va fi silențios atunci când vorbiți cu Cortana prin voce.

## Mail

* Când examinați elemente dinn lista de mesaje, puteți să folosiți comenzile
  de navigare ale tabelului pentru a examina antetele mesajelor. Rețineți că
  navigarea printre rânduri (mesaje) nu este suportată.

## Hărți

* NVDA redă bipul locației pentru locațiile hărții.
* Atunci când se utilizează vedere din stradă laterală și în cazul în care
  opțiunea "utilizare tastatură" este activată, NVDA va anunța adrese pe
  măsură ce utilizați tastele săgeată pentru a naviga pe hartă.

## Microsoft Solitaire Collection

* NVDA will announce names of cards and card decks.

## Microsoft Store

* When downloading content such as apps and movies, NVDA will announce
  product name and download progress.

## Tastatură modernă

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

## Persoane

* La căutarea de contacte, va fi anunțată prima sugestie, în particular dacă
  se folosesc versiuni recente ale aplicației.

## Setări

* Certain information such as Windows Update progress is reported
  automatically, including Storage sense/disk cleanup widget and errors from
  Windows Update.
* Valorile barei de progres și alte informații nu mai sunt anunțate de două
  ori.
* Odd control labels seen in certain Windows installations has been
  corrected.
* NVDA will announce the name of the optional quality update control if
  present (download and install now link in Windows 10, download button in
  Windows 11).

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
