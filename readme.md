# Windows App Essentials

* Authors: Joseph Lee, Derek Riemer and others

Note: Originally called Windows 10 App Essentials, it was renamed to Windows App Essentials in 2021 to support Windows 10 and future releases such as Windows 11. Parts of this add-on will still refer to the original add-on name.

This add-on is a collection of app modules for various modern Windows apps, as well as enhancements and fixes for certain controls found in Windows 10 and later.

The following app modules or support modules for some apps are included (see each app section for details on what is included):

* Modern keyboard
* Settings (Windows+I)

Notes:

* This add-on requires 64-bit Windows 10 22H2 (build 19045), 11 22H2 (build 22621), or later releases.
* Feature update support duration is tied to consumer support duration (Home, Pro, Pro Education, Pro for Workstations editions) and the add-on may end support for a feature update prior to end of consumer support. See <https://aka.ms/WindowsTargetVersioninfo> for more information and support dates.
* Although installation is possible, this add-on does not support Windows Enterprise LTSC (Long-Term Servicing Channel) and Windows Server releases.
* Not all features from Windows Insider Preview builds will be supported, more so for features introduced to a subset of Windows Insiders in canary and dev channels.
* The add-on may emulate changes included in Insider Preview builds which are subsequently removed, and for these changes, the add-on may remove them in future releases.
* Add-on dev channel will include changes including experimental content that may or may not be included in beta and stable releases, and beta channel will come with changes planned for future stable releases.
* Some add-on features are or will be part of NVDA screen reader.
* For best experience with apps that embed web technologies and content such as Start menu and its context menu, enable "Automatic focus mode for focus changes" setting from NVDA's browse mode settings panel.

For a list of changes made between each add-on releases, refer to [changelogs for add-on releases][1] document.

## General

* In Windows 11 24H2 Insider Preview builds, quick settings (shellhost.exe) interface elements can be navigated using mouse and/or touch interaction.

## Modern keyboard

This includes emoji panel, clipboard history, touch keyboard, dictation/voice typing, hardware input suggestions, suggested actions, and modern input method editors for certain languages across Windows 10 and 11. When viewing emojis, for best experience, enable Unicode Consortium setting from NVDA's speech settings and set symbol level to "some" or higher. When pasting from clipboard history in Windows 10, press Space key instead of Enter key to paste the selected item.

* In Windows 11, NVDA will announce suggested actions when compatible data such as phone numbers is copied to the clipboard. This is now part of NVDA 2024.2.

## Settings (Windows+I)

* NVDA will report updates to Windows Update status as download and install progresses. In Windows 10, this may result in speech interruption when navigating Settings app while updates are being downloaded and installed. In Windows 11, object navigation can be used in updates list to review update status for individual entries.

[1]: https://github.com/josephsl/wintenapps/wiki/w10changelog
