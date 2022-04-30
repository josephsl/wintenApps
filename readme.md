# Windows App Essentials

* Authors: Joseph Lee, Derek Riemer and others
* Download [stable version][1]
* Download [development version][2]
* NVDA compatibility: 2021.3 and later

Note: Originally called Windows 10 App Essentials, it was renamed to Windows App Essentials in 2021 to support Windows 10 and future releases such as Windows 11. Parts of this add-on will still refer to the original add-on name.

This add-on is a collection of app modules for various modern Windows apps, as well as enhancements and fixes for certain controls found in Windows 10 and later.

The following app modules or support modules for some apps are included (see each app section for details on what is included):

* Calculator
* Cortana
* Mail
* Maps
* Microsoft Solitaire Collection
* Modern keyboard (emoji panel/dictation/voice typing/hardware input suggestions/clipboard history/modern input method editors)
* Notepad (Windows 11)
* People
* Settings (system settings, Windows+I)
* Weather
* Miscellaneous modules for controls such as Start Menu tiles

Notes:

* This add-on requires Windows 10 21H1 (build 19043) or later and is compatible with Windows 11.
* Although installation is possible, this add-on does not support Windows Enterprise LTSC (Long-Term Servicing Channel) and Windows Server releases.
* Not all features from Windows Insider Preview builds will be supported.
* Some add-on features are or will be part of NVDA screen reader.
* For entries not listed below, you can assume that features are part of NVDA, no longer applicable as the add-on does not support unsupported Windows releases such as old Windows 10 versions, or changes were made to Windows and apps that makes entries no longer applicable.
* Some apps support compact overlay mode (always on top in Calculator, for example), and this mode will not work properly with portable version of NVDA.
* For best experience with apps that embed web technologies and content such as Start menu and its context menu, enable "Automatic focus mode for focus changes" setting from NVDA's browse mode settings panel.

For a list of changes made between each add-on releases, refer to [changelogs for add-on releases][3] document.

## General

* In addition to UIA event handlers provided by NVDA, the following UIA events and properties are recognized: drag complete, drag drop effect, drop target dropped. With NVDA's log level set to debug, these events will be tracked and logged.
* When opening, closing, reordering (Windows 11), or switching between virtual desktops, NVDA will announce active virtual desktop name (desktop 2, for example).
* When arranging pinned entries (tiles in Windows 10) in Start menu or Action Center quick actions with Alt+Shift+arrow keys, NVDA will announce information on dragged items or new position of the dragged item.
* Announcements such as volume/brightness changes in File Explorer and app update notifications from Microsoft Store can be suppressed by turning off Report Notifications in NVDA's object presentation settings.
* In Windows 11 Insider Preview builds, microphone mute toggle status (Windows+Alt+K) is announced from everywhere.
* NVDA will no longer repeat text output in Windows Terminal 1.12.10733 and later. This is now part of NVDA 2022.1.
* NVDA will once again announce search result details in Start menu. This is now part of NVDA 2022.2.
* In Windows 11, Taskbar items and other user interface controls can be detected properly when using mouse and/or touch interaction.

## Calculator

* NVDA will no longer announce graphing calculator screen message twice.
* In Windows 10, history and memory list items are properly labeled. This is now part of NVDA 2022.1.
* NVDA will announce calculator display content when performing scientific mode commands such as trigonometry operations. This is now part of NVDA 2022.2.

## Cortana

* Textual responses from Cortana are announced in most situations.
* NVDA will be silent when talking to Cortana via voice.

## Mail

* When reviewing items in messages list, you can now use table navigation commands to review message headers. Note that navigating between rows (messages) is not supported.

## Maps

* NVDA plays location beep for map locations.

## Microsoft Solitaire Collection

* NVDA will announce names of cards and card decks.

## Modern keyboard

This includes emoji panel, clipboard history, dictation/voice typing, hardware input suggestions, and modern input method editors for certain languages. When viewing emojis, for best experience, enable Unicode Consortium setting from NVDA's speech settings and set symbol level to "some" or higher. When pasting from clipboard history in Windows 10, press Space key instead of Enter key to paste the selected item. NVDA also supports updated input experience panel in Windows 11.

* In Windows 10, when an emoji group (including kaomoji and symbols group) is selected, NVDA will no longer move navigator object to certain emojis.
* Added support for updated input experience panel (combined emoji panel and clipboard history) in Windows 11.
* In Windows 11, it is again possible to use the arrow keys to review emojis when emoji panel opens. This is now part of NVDA 2022.1.
* In Windows 11 clipboard history, browse mode will be turned off by default, designed to let NVDA announce clipboard history entry menu items.

## Notepad

This refers to Windows 11 Notepad version 11 or later.

* NVDA will announce status items such as line and column information when report status bar command (NVDA+End in desktop layout, NvDA+Shift+End in laptop layout) is performed.
* NVDA will no longer announce entered text when pressing Enter key from the document.

## People

* When searching for contacts, first suggestion will be announced, particularly if using recent app releases.

## Settings

* Odd control labels seen in certain Windows installations has been corrected.
* NVDA will announce the name of the optional quality update control if present (download and install now link in Windows 10, download button in Windows 11).
* In Windows 11, breadcrumb bar items are properly recognized.
* In Windows 10, NVDA will interupt speech and report updates to Windows Update status as download and install progresses. This may result in speech interruption when navigating Settings app while updates are being downloaded and installed.

## Weather

* Tabs such as "forecast" and "maps" are recognized as proper tabs (patch by Derek Riemer).
* When reading a forecast, use the left and right arrows to move between items. Use the up and down arrows to read the individual items. For example, pressing the right arrow might report "Monday: 79 degrees, partly cloudy, ..." pressing the down arrow will say "Monday" Then pressing it again will read the next item (Like the temperature). This currently works for daily and hourly forecasts.

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
