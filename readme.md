# Windows App Essentials

* Authors: Joseph Lee, Derek Riemer and others
* Download [stable version][1]
* Download [beta version][2]
* Download [development version][3]
* NVDA compatibility: 2023.1 and later

Note: Originally called Windows 10 App Essentials, it was renamed to Windows App Essentials in 2021 to support Windows 10 and future releases such as Windows 11. Parts of this add-on will still refer to the original add-on name.

This add-on is a collection of app modules for various modern Windows apps, as well as enhancements and fixes for certain controls found in Windows 10 and later.

The following app modules or support modules for some apps are included (see each app section for details on what is included):

* Cortana
* Maps
* Modern keyboard (emoji panel/touch keyboard/dictation/voice typing/hardware input suggestions/clipboard history/Suggested Actions/modern input method editors)
* Settings (system settings, Windows+I)
* Voice access (Windows 11 22H2)
* Weather
* Miscellaneous modules for controls and features such as virtual desktops announcements

Notes:

* This add-on requires Windows 10 22H2 (build 19045), 11 21H2 (build 22000), or later releases.
* Feature update support duration is tied to consumer support duration (Home, Pro, Pro Education, Pro for Workstations editions) and the add-on may end support for a feature update prior to end of consumer support. See aka.ms/WindowsTargetVersioninfo for more information and support dates.
* Although installation is possible, this add-on does not support Windows Enterprise LTSC (Long-Term Servicing Channel) and Windows Server releases.
* If Add-on Updater is installed and background add-on updates is enabled, Windows App Essentials will not install at all on unsupported Windows releases.
* Not all features from Windows Insider Preview builds will be supported, more so for features introduced to a subset of Windows Insiders in canary and dev channels.
* Add-on dev channel will include changes including experimental content that may or may not be included in beta and stable releases, and beta channel will come with changes planned for future stable releases.
* Some add-on features are or will be part of NVDA screen reader.
* For best experience with apps that embed web technologies and content such as Start menu and its context menu, enable "Automatic focus mode for focus changes" setting from NVDA's browse mode settings panel.

For a list of changes made between each add-on releases, refer to [changelogs for add-on releases][4] document.

## General

* When opening, closing, or switching between virtual desktops, NVDA will announce active virtual desktop name (desktop 2, for example).
* Improved Windows 10 and 11 taskbar experience, including announcing results of rearranging icons when pressing Alt+Shift+left/right arrow keys (Windows 11) and reporting item position when moving through taskbar icons (Windows 10 and 11).
* In aps such as File Explorer and Notepad where tabbed windows are supported, NVDA will announce the name and the position of tabs when switching between them. This is now part of NVDA 2023.2.

## Cortana

* Textual responses from Cortana are announced in most situations.

## Maps

* NVDA will no longer interrupt speech when focused on items other than the map control in some cases.

## Modern keyboard

This includes emoji panel, clipboard history, touch keyboard, dictation/voice typing, hardware input suggestions, suggested actions, and modern input method editors for certain languages across Windows 10 and 11. When viewing emojis, for best experience, enable Unicode Consortium setting from NVDA's speech settings and set symbol level to "some" or higher. When pasting from clipboard history in Windows 10, press Space key instead of Enter key to paste the selected item.

* In Windows 11 22H2 and later, NVDA will announce suggested actions when compatible data such as phone numbers is copied to the clipboard.

## Settings

* NVDA will announce the name of the optional quality update control if present (download and install now link in Windows 10, download button in Windows 11).
* In Windows 11, breadcrumb bar items are properly recognized.
* NVDA will report updates to Windows Update status as download and install progresses. This may result in speech interruption when navigating Settings app while updates are being downloaded and installed. If using Windows 11 and selective UIA event registration is on or set to selective, you must move focus to updates list as soon as they appear so NVDA can announce update progress.

## Voice access

This refers to Voice access feature introduced in Windows 11 22H2.

* NVDA will announce microphone status when toggling microphone from Voice access interface.

## Weather

* Tabs such as "forecast" and "maps" are recognized as proper tabs (patch by Derek Riemer).
* When reading a forecast, use the left and right arrows to move between items. Use the up and down arrows to read the individual items. For example, pressing the right arrow might report "Monday: 79 degrees, partly cloudy, ..." pressing the down arrow will say "Monday" Then pressing it again will read the next item (Like the temperature). This currently works for daily and hourly forecasts.

[1]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps

[2]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-dev

[4]: https://github.com/josephsl/wintenapps/wiki/w10changelog
