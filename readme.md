# Windows App Essentials

* Authors: Joseph Lee, Derek Riemer and others
* Download [stable version][1]
* Download [development version][2]
* NVDA compatibility: 2021.2 and later

Note: Originally called Windows 10 App Essentials, it was renamed to Windows App Essentials in 2021 to support Windows 10 and future releases such as Windows 11. Parts of this add-on will still refer to the original add-on name.

This add-on is a collection of app modules for various modern Windows apps, as well as enhancements and fixes for certain controls found in Windows 10 and later.

The following app modules or support modules for some apps are included (see each app section for details on what is included):

* Calculator
* Cortana
* Mail
* Maps
* Microsoft Solitaire Collection
* Modern keyboard (emoji panel/dictation/voice typing/hardware input suggestions/clipboard history/modern input method editors)
* People
* Settings (system settings, Windows+I)
* Weather
* Miscellaneous modules for controls such as Start Menu tiles

Notes:

* This add-on requires Windows 10 20H2 (build 19042) or later and is compatible with Windows 11.
* Although installation is possible, this add-on does not support Windows Enterprise LTSC (Long-Term Servicing Channel) and Windows Server releases.
* Some add-on features are or will be part of NVDA screen reader.
* For entries not listed below, you can assume that features are part of NVDA, no longer applicable as the add-on does not support unsupported Windows releases such as old Windows 10 versions, or changes were made to Windows and apps that makes entries no longer applicable.
* Some apps support compact overlay mode (always on top in Calculator, for example), and this mode will not work properly with portable version of NVDA.

For a list of changes made between each add-on releases, refer to [changelogs for add-on releases][3] document.

## General

* NVDA can announce suggestion count when performing a search in majority of cases, including when suggestion count changes as search progresses. This is now part of NVDA 2021.3.
* In addition to UIA event handlers provided by NVDA, the following UIA events are recognized: drag complete, drop target dropped, layout invalidated. With NVDA's log level set to debug, these events will be tracked, and for UIA notification event, a debug tone will be heard if notifications come from somewhere other than the currently active app. Events built into NVDA such as name change and controller for events are tracked from an add-on called Event Tracker.
* When opening, closing, reordering (Windows 11), or switching between virtual desktops, NVDA will announce active virtual desktop name (desktop 2, for example).
* NVDA will no longer announce Start menu size text when changing screen resolutions or orientation.
* When arranging Start menu tiles or Action Center quick actions with Alt+Shift+arrow keys, NVDA will announce information on dragged items or new position of the dragged item.
* Announcements such as volume/brightness changes in File Explorer and app update notifications from Microsoft Store can be suppressed by turning off Report Notifications in NVDA's object presentation settings.

## Calculator

* NVDA will no longer announce graphing calculator screen message twice.

## Cortana

* Textual responses from Cortana are announced in most situations.
* NVDA will be silent when talking to Cortana via voice.

## Mail

* When reviewing items in messages list, you can now use table navigation commands to review message headers. Note that navigating between rows (messages) is not supported.

## Maps

* NVDA plays location beep for map locations.
* When using street side view and if "use keyboard" option is enabled, NVDA will announce street addresses as you use arrow keys to navigate the map.

## Microsoft Solitaire Collection

* NVDA will announce names of cards and card decks.

## Modern keyboard

This includes emoji panel, clipboard history, dictation/voice typing, hardware input suggestions, and modern input method editors for certain languages. When viewing emojis, for best experience, enable Unicode Consortium setting from NVDA's speech settings and set symbol level to "some" or higher. When pasting from clipboard history in Windows 10, press Space key instead of Enter key to paste the selected item. NVDA also supports updated input experience panel in Windows 11.

* In Windows 10, when an emoji group (including kaomoji and symbols group) is selected, NVDA will no longer move navigator object to certain emojis.
* Added support for updated input experience panel (combined emoji panel and clipboard history) in Windows 11.

## People

* When searching for contacts, first suggestion will be announced, particularly if using recent app releases.

## Settings

* Certain information such as Windows Update progress is reported automatically, including Storage sense/disk cleanup widget and errors from Windows Update.
* Progress bar values and other information are no longer announced twice.
* Odd control labels seen in certain Windows installations has been corrected.
* NVDA will announce the name of the optional quality update control if present (download and install now link in Windows 10, download button in Windows 11).
* In Windows 11, breadcrumb bar items are properly recognized.

## Weather

* Tabs such as "forecast" and "maps" are recognized as proper tabs (patch by Derek Riemer).
* When reading a forecast, use the left and right arrows to move between items. Use the up and down arrows to read the individual items. For example, pressing the right arrow might report "Monday: 79 degrees, partly cloudy, ..." pressing the down arrow will say "Monday" Then pressing it again will read the next item (Like the temperature). This currently works for daily and hourly forecasts.

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
