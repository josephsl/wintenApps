# Windows 10 App Essentials #

* Auteurs: Joseph Lee, Derek Riemer en andere Windows 10 gebruikers
* Download [stabiele versie][1]
* Download [ontwikkelversie][2]
* NVDA compatibility: 2020.3 to 2020.4

This add-on is a collection of app modules for various Windows 10 apps, as
well as enhancements and fixes for certain windows 10 controls.

De volgende app-modules of ondersteuningsmodules voor sommige apps zijn
inbegrepen (zie elke app-sectie voor details over wat is inbegrepen):

* Rekenmachine (modern).
* Agenda
* Cortana (Gesprekken)
* Mail
* Kaarten
* Microsoft Solitaire Collection
* Microsoft Store
* Modern toetsenbord (emoji-paneel / dicteren / hardware-invoersuggesties /
  cloudklembordgeschiedenis / moderne invoermethode-editors)
* Personen
* Instellingen (systeeminstellingen, Windows+I)
* Weer
* Diverse modules voor bedieningselementen zoals Start Menu-tegels.

Opmerkingen:

* This add-on requires Windows 10 Version 1909 (build 18363) or later. For
  best results, use the add-on with latest Windows 10 stable release
  (20H2/build 19042).
* Sommige add-on-functies zijn of zullen deel gaan uitmaken van de
  NVDA-schermlezer.
* Voor items die hieronder niet worden vermeld, kunt u ervan uitgaan dat
  functies deel uitmaken van NVDA, niet langer van toepassing zijn omdat de
  add-on geen ondersteuning biedt voor oude Windows 10 versies, of er
  wijzigingen zijn aangebracht in Windows 10 en apps waardoor items niet
  langer van toepassing zijn.

Voor een lijst met wijzigingen die zijn aangebracht in elke nieuwe versie
van deze add-on, zie het document [changelogs for add-on releases][3].

## Algemeen

* NVDA will no longer play error tones or do nothing if this add-on becomes
  active from Windows 7, Windows 8.1, and unsupported releases of Windows
  10.
* In addition to dialogs recognized by NVDA, more dialogs are now recognized
  as proper dialogs and reported as such, including Insider Preview dialog
  (settings app).
* NVDA can announce suggestion count when performing a search in majority of
  cases. This option is controlled by "Report object position information"
  in Object presentation panel found in NVDA settings.
* When searching in Start menu or File Explorer in Version 1909 (November
  2019 Update) and later, instances of NVDA announcing search results twice
  when reviewing results are less noticeable, which also makes braille
  output more consistent when reviewing items.
* In addition to UIA event handlers provided by NVDA, the following UIA
  events are recognized: drag start, drag cancel, drag complete, drag target
  enter, drag target leave, drag target dropped. With NVDA's log level set
  to debug, these events will be tracked, and for UIA notification event, a
  debug tone will be heard if notifications come from somewhere other than
  the currently active app. Some events will provide additional information
  such as element count in controller for event, state of the element for
  state change event, and item text for item status event.
* It is possible to tracke only specific events and/or events coming from
  specific apps.
* When opening, closing, or switching between virtual desktops, NVDA will
  announce current desktop name (desktop 2, for example).
* NVDA will no longer announce Start menu size text when changing screen
  resolutions or orientation.
* When arranging Start menu tiles or Action Center quick actions with
  Alt+Shift+arrow keys, NVDA will announce information on dragged items or
  new position of the dragged item.
* Announcements such as volume/brightness changes in File Explorer and app
  update notifications from Microsoft Store can be suppressed by turning off
  Report Notifications in NVDA's object presentation settings.

## Rekenmachine

* When ENTER or Escape is pressed, NVDA will announce calculation results.
* For calculations such as unit converter and currency converter, NVDA will
  announce results as soon as calculations are entered.
* NVDA will notify if maximum digit count has been reached while entering
  expressions.

## Agenda

* NVDA no longer announces "edit" or "read-only" in message body and other
  fields.

## Cortana

Most items are no longer applicable on Version 1903 and later unless Cortana
Conversations (Version 2004 and later) is in use.

* Textual responses from Cortana are announced in most situations.
* NVDA will be silent when talking to Cortana via voice.
* In Version 1909 (November 2019 Update) and later, modern search experience
  in File Explorer powered by Windows Search user interface is supported.

## Mail

* When reviewing items in messages list, you can now use table navigation
  commands to review message headers. Note that navigating between rows
  (messages) is not supported.
* When writing a message, appearance of at mention suggestions are indicated
  by sounds.

## Kaarten

* NVDA plays location beep for map locations.
* When using street side view and if "use keyboard" option is enabled, NVDA
  will announce street addresses as you use arrow keys to navigate the map.

## Microsoft Solitaire Collection

* NVDA will announce names of cards and card decks.

## Microsoft Store

* After checking for app updates, app names in list of apps to be updated
  are correctly labeled.
* When downloading content such as apps and movies, NVDA will announce
  product name and download progress.

## Modern keyboard

This includes emoji panel, clipboard history, dictation, hardware input
suggestions, and modern input method editors for certain languages. When
viewing emojis, for best experience, enable Unicode Consortium setting from
NVDA's speech settings and set symbol level to "some" or higher.

* When opening clipboard history, NVDA will no longer announce "clipboard"
  when there are items in the clipboard under some circumstances.
* On some systems running Version 1903 (May 2019 Update) and later, NVDA
  will no longer appear to do nothing when emoji panel opens.
* Added support for modern Chinese, Japanese, and Korean (CJK) IME
  candidates interface introduced in Version 2004 (build 18965 and later).
* When an emoji group (including kaomoji and symbols group in Version 1903
  or later) is selected, NVDA will no longer move navigator object to
  certain emojis.

## Personen

* When searching for contacts, first suggestion will be announced,
  particularly if using recent app releases.

## Instellingen

* Certain information such as Windows Update progress is reported
  automatically, including Storage sense/disk cleanup widget and errors from
  Windows Update.
* Progress bar values and other information are no longer announced twice.
* Windows Update reminder dialog is recognized as a proper dialog.
* Odd control labels seen in certain Windows 10 installations has been
  corrected.
* In more recent revisions of Version 1803 and later, due to changes to
  Windows Update procedure for feature updates, a "download and install now"
  link has been added. NVDA will now announce the title for the new update
  if present.

## Weer

* Tabs such as "forecast" and "maps" are recognized as proper tabs (patch by
  Derek Riemer).
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
