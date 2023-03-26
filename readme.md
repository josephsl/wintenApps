# Windows App Essentials

* Authors: Joseph Lee, Derek Riemer and others
* Download [stable version][1]
* Download [development version][3]
* NVDA compatibility: 2022.4 and later

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

* This add-on requires Windows 10 21H2 (build 19044), 11 21H2 (build 22000), or later releases.
* Feature update support duration is tied to consumer support duration (Home, Pro, Pro Education, Pro for Workstations editions) and the add-on may end support for a feature update prior to end of consumer support. See aka.ms/WindowsTargetVersioninfo for more information and support dates.
* Although installation is possible, this add-on does not support Windows Enterprise LTSC (Long-Term Servicing Channel) and Windows Server releases.
* If Add-on Updater is installed and background add-on updates is enabled, Windows App Essentials will not install at all on unsupported Windows releases.
* Not all features from Windows Insider Preview builds will be supported, more so for features introduced to a subset of Windows Insiders in canary and dev channels.
* Some add-on features are or will be part of NVDA screen reader.
* Some apps support compact overlay mode (always on top in Calculator, for example), and this mode will not work properly with the portable version of NVDA.
* For best experience with apps that embed web technologies and content such as Start menu and its context menu, enable "Automatic focus mode for focus changes" setting from NVDA's browse mode settings panel.

For a list of changes made between each add-on releases, refer to [changelogs for add-on releases][4] document.

## General

* When opening, closing, or switching between virtual desktops, NVDA will announce active virtual desktop name (desktop 2, for example).
* In Windows 11, NVDA will announce search highlights in Start menu when it opens. This is now part of NVDA 2023.1.
* In Windows 11 22H2 and later, mouse and/or touch interaction can be used to interact with redesigned system tray overflow window and Open With dialog. This is now part of NVDA 2023.1.
* NVDA will record processor architecture for the current Windows installation (x86/32-bit, AMD64, ARM64) when it starts. This is now part of NVDA 2023.1.
* Improved Windows 10 and 11 taskbar experience, including announcing results of rearranging icons when pressing Alt+Shift+left/right arrow keys (Windows 11 prior to build 25267) and reporting item position when moving through taskbar icons (Windows 10 and 11 prior to build 25281).
* NVDA will announce empty folder text inside an empty folder in File Explorer.
* In aps such as File Explorer and Notepad where tabbed windows are supported, NVDA will announce the name and the position of tabs when switching between them.

## Cortana

* Textual responses from Cortana are announced in most situations.

## Maps

* NVDA will no longer interrupt speech when focused on items other than the map control in some cases.

## Modern keyboard

This includes emoji panel, clipboard history, touch keyboard, dictation/voice typing, hardware input suggestions, suggested actions, and modern input method editors for certain languages across Windows 10 and 11. When viewing emojis, for best experience, enable Unicode Consortium setting from NVDA's speech settings and set symbol level to "some" or higher. When pasting from clipboard history in Windows 10, press Space key instead of Enter key to paste the selected item.

* In Windows 10 emoji panel, when an emoji group (including kaomoji and symbols group) is selected, NVDA will no longer move navigator object to certain emojis.
* In Windows 11 clipboard history, browse mode will be turned off by default, designed to let NVDA announce clipboard history entry menu items. This is now part of NVDA 2023.1.
* In Windows 11 22H2 and later, NVDA will announce suggested actions when compatible data such as phone numbers is copied to the clipboard.

## Settings

* NVDA will announce the name of the optional quality update control if present (download and install now link in Windows 10, download button in Windows 11).
* In Windows 11, breadcrumb bar items are properly recognized.
* In Windows 10 and 11 22H2 and later, NVDA will interupt speech and report updates to Windows Update status as download and install progresses. This may result in speech interruption when navigating Settings app while updates are being downloaded and installed. If using Windows 11 22H2 and later, if selective UIA event registration is on, you must move focus to updates list as soon as they appear so NVDA can announce update progress.

## Voice access

This refers to Voice access feature introduced in Windows 11 22H2.

* NVDA will announce microphone status when toggling microphone from Voice access interface.

## Weather

* Tabs such as "forecast" and "maps" are recognized as proper tabs (patch by Derek Riemer).
* When reading a forecast, use the left and right arrows to move between items. Use the up and down arrows to read the individual items. For example, pressing the right arrow might report "Monday: 79 degrees, partly cloudy, ..." pressing the down arrow will say "Monday" Then pressing it again will read the next item (Like the temperature). This currently works for daily and hourly forecasts.

[1]: https://addons.nvda-project.org/files/get.php?file=wintenApps

[2]: https://addons.nvda-project.org/files/get.php?file=wintenApps-beta

[3]: https://addons.nvda-project.org/files/get.php?file=wintenApps-dev

[4]: https://github.com/josephsl/wintenapps/wiki/w10changelog
