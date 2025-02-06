# Windows App Essentials Changelog

This document lists release changelogs for Windows App Essentials add-on.

Note: originally called Windows 10 App Essentials, this add-on was renamed to Windows App Essentials in 2021 to reflect support for future Windows releases such as Windows 11. Internally, it is still called WinTenApps to reflect the ad-on's origins and to denote actual Windows system version in use (10.0).

For each add-on version entry, minor versions (such as 18.06.1) are included under major release (18.06, for example).

## Version preview

This section lists changes planned for future add-on releases. Items in this section are not tied to specific releases and may or may not appear in stable add-on releases. See below sections for items included in past or upcoming stable releases.

## Version 25.04

* NVDA 2025.1 or later is required.
* Removed app module for modern keyboard.
* Modern keyboard: Removed Windows 11 clipboard history content announcements workaround as it is part of NVDA 2025.1.

## Version 25.02

* Settings: The workaround to announce Windows Update status for individual updates with speech interruption in Windows 10 is deprecated and will be removed in a future add-on release as live region change is no longer announced as of 22H2 build 19045.5440 (KB5050081).

## Version 25.01 (Windows 10 end of support countdown)

Starting from this release, only critical changes will be applied to Windows 10 support features.

* NVDA 2024.4.1 or later is required.
* Windows 10: Add-on dev channel releases no longer support Windows 10.
* Reformatted add-on modules using Ruff to better align with NVDA coding standards.
* Moved ad-on wiki documents such as add-on changelog to the main code repository.
* Added support for Copilot WebView2 app.
* Copilot: Textual responses from Copilot are announced.

## Version 24.10

* NVDA 2024.3.1 or later is required.
* Various features and fixes that were included with the add-on are now part of NVDA. These include NVDA no longer moving focus to somewhere else when opening different parts of the emoji panel, no longer announcing "clipboard history" twice when navigating through categories, and speech no longer getting cut off when reviewing kaomojis and symbols.
* Modern keyboard: In Windows 11 clipboard history, NVDA will no longer announce history contents when the panel is closed while entries are present.

## Version 24.09

* Add-on beta channel is discontinued.
* Windows 10: 32-bit systems are no longer supported.
* Windows 11: Requires Version 23H2 or later.
* Removed WinAppObjs global plugin from the add-on install package (the global plugin module remains in the add-on source code repository).

## Version 24.08 (Goodbye, 32-bit Windows 10)

This is the last version to support 32-bit (x86) Windows 10 systems. Although it is possible to install future add-on releases on 32-bit Windows 10, support for this configuration will not be provided.

* NVDA 2024.2 or later is required.
* Various features and fixes that were included with the add-on are now part of NVDA. These include mouse and touch interaction in Windows 11 24H2 quick settings interface and announcing top suggestions in Windows 11 Suggested Actions, hardware keyboard input, and the modern IME interface.
* Removed app module for Shell Host (Windows 11 24H2 action center/quick settings).
* Switched linting tool from Flake8 to Ruff.

## Version 24.06

* Add-on beta channel is deprecated to simplify add-on development releases.
* Modern keyboard: Several Windows 11 emoji panel fixes, including NVDA no longer moving focus to somewhere else when opening different parts of the emoji panel, no longer announcing "clipboard history" twice when navigating through categories, and speech no longer getting cut off when reviewing kaomojis and symbols.
* Settings: In Windows 10, NVDA will announce Windows Update live region changes regardless of appearance of action buttons such as restarting the computer. This will result in speech getting interrupted whenever live region changes occur.

## Version 24.05

* NVDA 2024.1 is required due to massive internal changes including Python 3.11 upgrade that affect this add-on.
* Removed the ability to detect additional UIA dialogs as it is resolved in NVDA 2024.1.
* Settings: Removed the ability to announce Windows Update status for individual updates in Windows 11 if selective UIA event registration is active and focus moves to updates list. Object navigation can be used to navigate to and obtain update status for individual updates.

## Version 24.04

* Initial support for Windows 11 Version 24H2 (2024 Update) and Server 2025.
* Support for 32-bit Windows 10 systems is deprecated.
* Download links for add-on releases are no longer included in add-on documentation. You can download the add-on from NV Access add-on store.
* Removed Calculator app module again.
* Modern keyboard: Restructured Windows 11 modern keyboard support with changes and fixes, including announcing the top hardware keyboard input suggestion instead of announcing suggestions as they change and reporting visible IME candidates when modern IME window opens.
* Settings: The ability to announce Windows Update status for individual updates in Windows 11 is deprecated and will be removed in a future add-on release (applicable if UIA selective event registration is active and focus moves to updates list).

## Version 24.03

* NVDA 2023.3.4 or later is required due to security fixes.
* NVDA will present the supported release above the current build instead of list of supported releases if trying to install the add-on on unsupported Windows releases.
* Action center: Redesigned action center in Insider Preview build 26000 series can be navigated using mouse and/or touch interaction.
* Modern keyboard/voice typing (Windows 11): NVDA will no longer announce "listening" when pressing Windows+H.

## Version 24.02

* NVDA 2023.3.3 or later is required due to security fixes.
* Modern keyboard/voice typing (Windows 11): NVDA will announce voice typing alert regardless of UIA event registration setting (selective or global). As a result, the ability to announce "listening" when pressing Windows+H is deprecated and will be removed in a future add-on release.
* Modern keyboard/suggested actions: NVDA will announce the top suggestion instead of all suggested actions.

## Version 24.01

As of this release, Windows 10 support features are frozen.

* Reintroduced Calculator app module.
* Optimized add-on code to use NVDA 2024.1 features and work better with selective UIA event registration.
* Calculator: NVDA will announce results when pressing Enter with calculations involving identical single digit operands between an operator (for example, 2+2).
* Settings: NVDA will announce Windows Update progress in Windows Insider canary build 26010 and later.

## Version 23.12

* NVDA 2023.3 or later is required.
* Removed app module for Voice Access.
* Settings: Removed update history label workaround and update announcement caching (Windows 10), optional Windows Update label announcement (Windows 10 and 11), and breadcrumb bar item recognition (Windows 11).
* Voice Access: Removed microphone button toggle as announcement can be inaccurate at times and cannot be toggled using object navigation and touch gestures.

## Version 23.11

* Modern keyboard: NVDA will no longer announce focused control twice in some apps after closing Windows 11 clipboard history.
* Settings: Workarounds related to Windows Update and Windows 11 breadcrumb bar item recognition are deprecated and will be removed in a future add-on release.
* Voice Access: Microphone button toggle announcement is deprecated and will be removed in a future add-on release.

## Version 23.10

* NVDA 2023.2 or later is required.
* Various features and fixes that were included with the add-on are now part of NVDA. These include virtual desktop switch announcements, announcing tab switches in Notepad (Windows 11) and File Explorer (Windows 11 22H2), Windows 11 IME interface support in modern keyboard, and anouncing expressions in Calculator compact overlay mode when using portable NVDA.
* Removed support for automatic add-on updates feature from Add-on Updater add-on with its impending end of life.
* Changed add-on home page shown on add-on store from community add-ons (addons.nvda-project.org) website to GitHub (github.com/josephsl/wintenapps) repository.

## Version 23.09 (From Cortana to Copilot)

* Removed app module for Cortana.
* Cortana:  Deprecated and replaced by Windows Copilot with the interface powered by Microsoft Edge. As a result, textual responses from Cortana will no longer be announced.
* Modern keyboard/Voice Access (Windows 11 22H2 and later): When "correct that" voice command is issued, NVDA will announce appearance of dictation suggestions instead of just announcing the selected text.

## Version 23.08 (Scaling up and down)

* Windows 11: Requires Version 22H2 or later.
* Removed app modules for CSRSS and MSN Weather.
* Removed Windows 10 and 11 taskbar item enhancements such as announcing position information when reviewing (Windows 10 and 11) and rearranging items (Windows 11). These were emulated changes for features introduced and then removed in Insider Preview builds.
* CSRSS: Transferred virtual desktop switch announcement from CSRSS app module to WinApObjs global plugin to align with recent NVDA source code changes.
* MSN Weather: Removed tab control role reclassification.

## Version 23.07

* Initial support for Windows 11 Version 23H2 (2023 Update).
* Removed app module for Maps.
* Taskbar enhancements such as position announcements when reviewing (Windows 10 and 11) and rearranging items (Windows 11) are deprecated and will be removed in a future add-on release. This is an emulated bug fix from Windows Insider builds which was subsequently removed in later builds.
* NVDA will once again present list of supported Windows releases if attempting to install the add-on on unsupported Windows releases.
* Cortana: To be replaced by Windows Copilot with the interface powered by Microsoft Edge. As a result, announcing Cortana responses is deprecated and will be removed in a future add-on release.
* Maps: Removed focus announcement workaround seen when reviewing app menu items.
* MSN Weather: Tab control role reclassification is deprecated and will be removed in a future add-on release.
* Settings: Removed early progress and message announcements workaround in Settings/Update and Security (System in Windows 11)/Recovery/Reset as NVDA can announce these messages regardless of selective UIA event registration setting.

## Version 23.06

* NVDA 2023.1 or later is required.
* Windows 10: Requires Version 22H2, end of support for Server 2022 from the add-on. Version 22H2 is the final feature update.
* Various features and fixes that were included with the add-on are now part of NVDA. These include announcing search highlights in Windows 11 Start menu, recognizing search fields and suggestions in more apps such as People, mouse and touch interaction in Windows 11 22H2 Open With dialog and Moment 2 system tray overflow window, and disabling browse mode in Windows 11 clipboard history.
* NVDA will announce virtual desktop names before announcing focus changes, notably when opening and switching between virtual desktops.
* When attempting to install the add-on on unsupported Windows builds, NVDA will present supported releases with higher build numbers.
* Modern keyboard: Removed Windows 10 emoji panel navigator object workaround after selecting emoji/kaomoji/symbols categories.
* MSN Weather: Due to app changes, dedicated commands to review forecast item content using up and down arrow keys are removed. Use browse mode commands to read forecast content in app version 4.53.51095 and later.
* Settings: Removed developer mode label workaround in Windows 10.

## Version 23.05

* File Explorer: Removed empty folder announcement feature due to a critical bug that cannot be resolved easily.
* Maps: Removed map location beeps feature in favor of Object Location Tones add-on.
* Settings: NVDA will announce Windows Update status changes in Windows 11 21H2.

## Version 23.04

* Split add-on dev channel into dev and beta channels, the former designed to test features that are experimental and may not come to stable releases, the latter designed to test changes destined for stable add-on releases.
* Calculator: Portable NVDA will no longer appear to do nothing or play error tones when using calculator in compact overlay mode (Alt+up arrow from standard calculator mode).
* Maps: Map location beeps feature is deprecated and will be removed in a future add-on release in favor of Object Location Tones add-on.

## Version 23.03

* Added type information to more areas of the add-on source code.
* Windows 11: NVDA will no longer appear to do nothing or play error tones when using the mouse to review taskbar items at the cost of not announcing position information sometimes.
* Windows 11: NVDA will no longer record information on 22H2 beta builds.
* MSN Weather: Removed "no more weather data" message when arrowing up and down from weather items list.
* Notepad (Windows 11): NVDA will no longer say "back" when retrieving status bar contents in Notepad 11.2301 and later, particularly after opening and closing Notepad settings (Alt+S).

## Version 23.02

* NVDA 2022.4 or later is required.
* Various features and fixes that were included with the add-on are now part of NVDA. These include announcing "dragging" when an item is about to be dragged and announcing drag and drop target effects.
* Removed additional UIA event tracking facility as the last set of additional events (drag and drop) are included in NVDA 2022.4.
* Improved Windows 10 and 11 taskbar experience, including announcing results of rearranging icons when pressing Alt+Shift+left/right arrow keys (Windows 11 prior to build 25267) and reporting item position when moving through taskbar icons (Windows 10 and 11 prior to build 25281).
* In Windows 11 22H2, Open With dialog can be navigated using mouse and/or touch interaction.
* NVDA will announce empty folder text inside an empty folder in File Explorer.
* In aps such as File Explorer and Notepad where tabbed windows are supported, NVDA will announce the name and the position of tabs when switching between them.
* Notepad (Windows 11): NVDA will once again announce status bar contents in version 11.2212 or later, particularly when multiple tabs are open.

## Version 23.01

* NVDA 2022.3 or later is required.
* Removed app module for People app.
* Removed the ability to toggle UIA notification announcements from apps such as Calculator via "Report notifications" setting found in NVDA's object presentation settings panel.
* In Windows 11 22H2 Moment 2, redesigned system tray overflow area can be detected properly when using mouse and/or touch interaction.
* NVDA will record processor architecture for the current Windows installation (x86/32-bit, AMD64, ARM64) in the log when the add-on starts.
* Maps: NVDA will no longer interrupt speech when focused on items other than the map control in some cases.

## Version 22.12

* Supported releases and builds across Windows 10 and 11 will be displayed if attempting to install the add-on on unsupported Windows releases including releases earlier than 10 and unsupported feature updates.
* Removed most Windows version detection code from WinAppObjs global plugin as it was ineffective in preventing the add-on from running in unsupported Windows releases.
* Windows 11: If running on 22H2 beta builds (22622/22623), NVDA will recognize this fact and record this information in the log.
* Windows 11 22H2 beta: Requires build 22623.
* Transferred virtual desktop switch announcement from WinAppObjs global plugin to CSRSS (client/server runtime subsystem) ap module as announcements come from CSRSS.
* Voice access: Microphone toggle state is announced once again in Insider Preview build 25200 series.

## Version 22.11

* Transferred Word 365 formatting announcement fix to Office Desk add-on.
* The ability to toggle UIA notification announcements from apps such as Calculator via "Report notifications" setting found in NVDA's object presentation settings panel is deprecated and will be removed in a future add-on release.
* Removed microphone toggle announcement from everywhere except File Explorer in Windows 11 22H2 and later. As a workaround, minimize all apps and then press Alt+Windows+K to toggle microphone status.
* In Windows 11, NVDA will announce search highlights in Start menu when it opens.
* Modern keyboard: Suggested Actions is now part of Windows 11 22H2 Moment 1 (enabled in build 22621).
* People: Recognizing contacts search field and suggestions are deprecated and will be removed in a future add-on release as NVDA 2023.1 will provide a more generic support for search suggestions in more apps such as People app.

## Version 22.10

* The following UIA property changes are recognized: drag is grabbed (recognized as a distinct state), drop target effect.
* UIA drag start/cancel/complete events are recognized once again, this time as a state change events.
* NVDA will announce "dragging" when dragging certain items such as when arranging Windows 10 Start menu tiles by pressing Alt+Shift+arrow keys.
* Drop target dropped UIA event is removed. As a result, NVDA will no longer announce position of the newly dragged item by faking focus events once drag and drop operation completes, replaced by announcing drag drop and drop target effects while drag and drop is in progress.
* Debug logging for drag and drop events is now handled by Event Tracker add-on, more so if using NVDA 2022.4.
* Due to verbosity issues, item status change announcements in more apps has been removed.

## Version 22.09

* NVDA 2022.2 or later is required, more so for security (2022.2.2 or later is recommended).
* Windows 10: Requires Version 21H2 or later.
* Various features and fixes that were included with the add-on are now part of NVDA. NVDA 2022.1 include support for Windows 11 Calculator, announcing history and memory items in Windows 10 Calculator, fixing inability to use arrow keys to review emojis in Windows 11 emoji panel, and resolving text output repetition in Windows Terminal 1.12.10733 and later. NVDA 2022.2 include announcing more results including scientific mode command results in Calculator, announcing search result details in Start menu again, detecting Windows 11 UI elements when interacting with mouse and/or touch, and announcing status bar in Windows 11 Notepad if shown.
* Removed app modules for Windows 10 and 11 Calculator, Mail, Microsoft Solitaire Collection, and Windows 11 Notepad. NVDA includes Calculator and Notepad app modules, removed table navigation commands for mail items from Mail app module, and cards are labeled in Solitaire Collection.
* The list of supported releases is also shown on Windows 11 systems when attempting to install the add-on on unsupported releases. Currently supported releases are 21H2 (22000), 22H2 (22621/22622 beta), and Windows Insider builds above 25000.
* Item status changes are announced in more apps including Visual Studio Community 2022.

## Version 22.08 (Crossroads)

* Initial support for Windows 10 Version 22H2 (2022 Update), not to be confused with Windows 11 Version 22H2. This is the final Windows 10 feature update.
* Added support for automatic add-on updates feature from Add-on Updater add-on. In particular, the add-on will not install if using unsupported Windows releases.
* Event debug log for events added by this add-on (drag complete, drag drop effect, drop target dropped) are logged from event handlers themselves rather than  through a dedicated method. This makes debug log for events more concise.
* Microsoft Solitaire Collection: In version 4.13 and later, NVDA will announce card (suit and rank) labels provided by the app itself. As a result, support for Solitaire Collection is deprecated and will be removed in a future add-on release.
* Modern keyboard: Added support for Suggested Actions backported to build 22622 (Windows 11 22H2 beta).
* Settings: In Windows 11 22H2 and later, NVDA will announce the name of the update being downloaded from Windows Update. This works best with selective UIA event registration off, but if this setting is enabled, move to updates list as soon as it appears so NVDA can detect and announce update progress.
* Settings: In newer Windows 11 21H2 releases, optional update title will be announced if shown.

## Version 22.07

* Initial support for Windows 11 Version 22H2 (2022 Update), including beta build 22622.
* In Windows 10, NVDA will present a list of supported releases when attempting to install the add-on on unsupported Windows 10 releases. Currently supported releases are Windows 10 21H1 (19043), 21H2 (19044), and Server 2022 (20348). Consequently, installing and using the add-on on Windows Insider Preview builds earlier than 20348 is no longer supported unless Windows 10 feature updates are released from these builds.
* Mail: Table navigation commands for mail items is deprecated and will be removed in a future add-on release.

## Version 22.06

* Added support for Voice access (Windows 11 Version 22H2 preview).
* Initial support for Suggested Actions presented by modern keyboard (Windows 11 Insider Preview).
* Modern keyboard: In Insider Preview build 25115, NVDA will announce suggested actions when compatible data such as phone numbers is copied to the clipboard.
* Notepad (Windows 11): Removed text repetition fix as it is resolved in Notepad 11.2203.
* Notepad (Windows 11): Fixed a regression introduced in add-on 22.05 where NVDA did nothing or played error tones when trying to read status bar text.
* Voice access: NVDA will announce microphone toggle status when pressing Space or Enter keys while focused on microphone button.

## Version 22.05

* NVDA will once again announce search result details in Start menu.
* In Windows 11, Taskbar items and other user interface controls can be detected properly when using mouse and/or touch interaction.
* Settings: In Windows 10, NVDA will interupt speech and report updates to Windows Update status as download and install progresses. This may result in speech interruption when navigating Settings app while updates are being downloaded and installed.

## Version 22.03

* NVDA 2021.3 or later is required, more so for security (NVDA 2021.3.3 is advised).
* Various features and fixes that were included with the add-on are now part of NVDA. These include announcing search suggestion count in apps such as Settings and Microsoft Store and "pane" no longer being announced when switching between apps in Windows 11.
* Installing and using the add-on on Windows Insider Preview builds between 20348 (Server 2022) and 22000 (Windows 11) is no longer supported.
* Removed the warning message when installing the add-on on Windows Server systems as the add-on is better optimized for Windows 10/11 client systems.
* Removed deprecated XAML heading detection feature.
* Removed the debug tone heard when UIA notification events come from background apps when debug log is on. Use Event Tracker add-on to debug UIA notification events.
* Removed Start menu size announcement workaround as it is no longer heard in recent Windows 10 releases.
* UIA drag drop effect property event is now tracked.
* More information is announced when arranging Start menu tiles or Action center quick actions with Alt+Shift+arrow keys such as potential location of the dragged tile and placement of Action center quick action.
* NVDA will no longer repeat text output in Windows Terminal 1.12.10733 and later.
* Calculator: NVDA will announce results when more commands are performed such as pressing equals (=) key and performing operations in scientific calculator mode such as trigonometric operations.
* Maps: Removed street side view workaround as it is no longer applicable in recent app releases.
* Modern keyboard: In Windows 11 clipboard history, browse mode will be turned off by default, designed to let NVDA announce clipboard history entry menu items.
* Settings: In Windows 10, update history items no longer include installation status to align with Windows 11.

## Version 22.02

* Windows 10: Requires Version 21H1 or later.
* In Windows 11 Insider Preview builds, microphone mute status is announced from anywhere when Windows+Alt+K is pressed.
* Notepad (Windows 11): Provided that status bar is checked from View menu, NVDA will no longer announce status bar information such as line number from places other than document edit window.
* Notepad (Windows 11): added support for Notepad version 11.2112. In particular, status bar content is announced in the new release.

## Version 22.01

* Transferred layout invalidated event tracking and logging to Event Tracker add-on.
* The following UIA events are no longer tracked and logged due to lack of useful information: drag start, drag cancel, drop target enter, drop target leave.
* XAML heading recognition is deprecated and will be removed in a future release as it caused problems in apps such as Calculator and Settings.
* Removed app modules for File Explorer and Microsoft Store as Store version 2 (Windows 10/11) provides better support for download progress announcements without using the app module.
* Added support for Windows 11 Notepad.
* File Explorer: Due to compatibility issues with other add-ons, File Explorer app module was removed which may cause increased verbosity when switching between apps in Windows 11. The fix for "pane" announcement issue when switching apps is not affected.
* Notepad (Windows 11 preview): NVDA will announce status items such as line and column information when report status bar command (NVDA+End in desktop layout, NVDA+Shift+End in laptop layout) is performed.
* Notepad (Windows 11 preview): NVDA will no longer announce entered text when pressing Enter key from the document.
* Settings: In Windows 11, breadcrumb bar items are properly recognized.

## Version 21.11

* Partially removed the ability to recognize additional dialogs as recent Windows and app updates improve NVDA's ability to detect dialogs without help from the add-on. Dialogs with UIA class names included in NVDA will still be detected.
* The debug log prefix was changed from "W10" to "winapps" to reflect the renamed add-on.
* It is no longer required to enable report object position information option from NVDA's object presentation settings to be notified about suggestion count when searching in various apps.
* Roles for headings found in apps such as Settings app are properly marked as headings when displaying developer info for navigator object (NVDA+F1).
* Microsoft Store: Removed download list item label workaround in Windows 10 Store as the item label includes download status.
* Modern keyboard: In Windows 11, IME and hardware input suggestion candidate items are no longer announced twice.

## Version 21.10

* NVDA 2021.2 is required due to massive internal changes including control types refactor that affect this add-on.
* Initial support for Windows 11 Version 21H2 (RTM), not to be confused with Windows 10 Version 21H2 and Server 2022.
* Various features that were included with the add-on are now part of NVDA. These include braille announcements when entering expressions in Calculator, announcing suggestion count in File Explorer, improved item detection when emoji panel and clipboard history opens in recent Windows 10 releases, among others.
* Removed app modules for Calendar and Windows 10/11 search app (NVDA includes Windows 10 and 11 search app modules).
* Removed support for pre-refactor control types module contents in NVDA 2021.1 or earlier. Consequently, roles and states from refactored control types package are used.
* The Windows 11 support notice dialog for stable add-on releases and a startup message for detecting Windows 11 are removed.
* With event tracking for most events transferred to Event Tracker add-on, only events added by this add-on such as layout invalidated event will be tracked and logged, as well as removed the ability to track specific events and/or events coming from specific apps.
* The ability to recognize additional dialogs is deprecated and will be removed in a future release as Windows and apps were updated to let NVDA detect dialogs properly.
* Mail: Removed suggestions sound playback functionality for at address suggestions.
* Windows Search: Removed the Windows 10 search app module as it does not provide improved experience for braille users.

## Version 21.09

* On systems running Windows Server releases such as Server 2022, a warning dialog will be presented when installing the add-on as most modern apps such as Microsoft Store are not present in server systems, thereby limiting add-on features.
* When using Add-on Updater to update this add-on on unsupported Windows releases, the warning dialog will resemble the one shown when installing the add-on manually by being specific about minimum supported Windows release.
* Removed dedicated search field support and transferred suggestions count announcement to a dedicated suggestions list view object.
* Calculator: Added support for redesigned Calculator (version 10.2109) included in Windows 11.
* Calculator: Removed memory and history item workaround in Calculator 10.2109 as these items have labels.
* Modern keyboard: In Windows 11, it is no longer required to press the Escape key twice to close combined emoji panel and clipboard history.

## Version 21.08 (Windows 10 in transition)

Renamed to Windows App Essentials but things remain the same.

* Initial support for Windows 10 Version 21H2 (November 2021 Update) and Server 2022. These two releases have different build numbers.
* Requires Windows 10 Version 20H2 or later.
* Experimental support for Windows 11 Version 21H2 (RTM), not to be confused with Windows 10 Version 21H2.
* In Windows 11, NVDA will no longer announce "pane" when switching between programs.
* Windows Search (formerly classic Cortana) and modern keyboard app modules were renamed to reflect executable names for these apps in Version 2004 and later.
* Removed app module for combined Mail and Calendar (experimental version) as separate apps were reinstated in late 2020.
* The ability to track and log events for most events is handled by a new add-on named Event Tracker. Consequently, tracking events such as name change and controler for events is deprecated and will be removed in a future release.
* In search fields, NVDA can announce suggestions count whenever suggestions list changes as opposed to only when suggestions are first shown.
* Added support for layout invalidated UIA event, used to announce suggestions count changes as search terms are entered.
* When tracking events, information specific to certain events such as suggestion count for layout invalidated event will be logged separately from general information such as UIA element and Automation Id.
* Removed additional dialog class names as the only place where it was applicable (Windows Insider Program sign up screen) is no longer a dialog.
* Modern keyboard: In Windows 11, it is again possible to use the arrow keys to review emojis when emoji panel opens.
* Settings: In Settings/Update and Security/Recovery/Reset, initial progress messages and content changes are announced even when selective UIA event registration is active.
* Windows Search/File Explorer: In Windows 11, NVDA will no longer fail to announce suggestion count, caused by the Windows Search executable being renamed.

## Version 21.06

* NVDA 2020.4 or later is required.
* Various features that were included with the add-on are now part of NVDA. These include IME support in modern keyboard and silencing speech when entering expressions in Calculator.
* The following UIA events were renamed to make them consistent with actual UI Automation event names: drag target enter to drop target enter, drag target leave to drop target leave, drag target dropped to drop target dropped.
* If running on Windows 11 builds, NVDA will recognize this fact and record this information in the log, along with presenting a warning message when trying to install it on Windows 11.
* Modern keyboard: In build 21300 and later, with focus mode active from places such as web browsers, NVDA will no longer announce blank when using the arrow keys to navigate among emojis.
* Modern keyboard: When pressing Escape key to close emoji panel or clipboard history in build 21300 and later, focus will move back to the control you were working on before modern keyboard interface was opened. In some cases, Escape key should be pressed twice.

## Version 21.04

* Resolved additional issues via Flake8.
* Calculator: Calculation results from standard and scientific calculator modes will be announced in braille in addition to speech announcements.
* Calculator: Calculation expressions will be announced in braille.
* Calculator: NVDA will announce calculator results when Delete key is pressed to clear results.

## Version 21.03

* Initial support for Windows 10 Version 21H1 (May 2021 Update).
* Parts of the add-on source code now includes type annotations.
* When attempting to install the add-on on an unsupported Windows 10 release, an error dialog instead of a confirmation question will be presented and add-on installation will be blocked.
* Modern keyboard: Removed support for emoji panel changes introduced in Windows server 2022 Preview build 20200 series. This does not affect emoji panel support in other Windows 10 builds, including dev channel build 21300 series.
* Settings: If two or more optional updates are available and one of them happens to be a preview cumulative update, NVDA will no longer include extraneous text for "View optional updates" link.

## Version 21.02

* Requires Windows 10 Version 2004 or later.
* Modern keyboard: Added support for updated input experience panel (combined emoji panel and clipboard history) in build 21296 and later.

## Version 21.01

* NVDA 2020.3 or later is required.
* Various workarounds that were included with the add-on are now part of NVDA. These include reading Open With dialog content and better recognition of progressive web apps (PWA's) hosted by WWA Host process.
* Removed app modules for Open With dialog and WWA Host process.
* UIA help text (description change) property event is now tracked.
* Calculator: NVDA will once again announce calculator history and memory entries in version 10.2009 and later.

## Version 20.11

* NVDA 2020.2 or later is required.
* Resolved more coding style issues and potential bugs with Flake8.

## Version 20.10

* It is no longer necessary to restart NVDA with debug logging mode to read debug messages from log viewer. You can view debug messages if log level is set to "debug" from NVDA's general settings panel.
* Cortana: NVDA will no longer appear to do nothing or play error tones when Cortana version 2 window loses focus.
* Cortana: NVDA will announce Cortana's responses in version 2.20102 or later.
* Modern keyboard: Improved support for modern IME such as Microsoft Quick Input for Chinese. In particular, when modern Chinese, Japanese, and Korean IME opens, the first few candidates will be announced similar to older IME candidate window.
* Modern keyboard: Hardware keyboard input suggestions are once again announced in Version 1909. If using NVDA 2020.3 or later, disable selective UIA event registration from NVDA's Advanced settings panel.
* Modern keyboard: NVDA will announce selected emoji if emoji panel is opened more than once in build 20226.
* Modern keyboard: NVDA will no longer announce first people emoji when people category is selected in emoji panel.

## Version 20.08 (Another anniversary, another release)

* NVDA 2020.1 or later is required.
* Initial support for Windows 10 Version 20H2 (October 2020 Update).
* Open With dialog fix has been extended to Version 1909.
* Calculator: NVDA will announce more notices such as memory operations.
* Cortana: Text responses from app version 2.2007.24 or later are announced.
* Modern keyboard: Added workarounds to support selective UIA event registration flag introduced in recent NVDA alpha snapshots.
* Modern keyboard: Various usability improvements, especially for braille users when reviewing emoji groups.
* Windows Store: Product update announcements are once again announced in version 12007 or later.

## Version 20.07

* Requires Windows 10 Version 1909 or later.
* Open With dialog in Version 2004 (May 2020 Update) and later is announced when opened.
* Cortana: Text responses from non-English Cortana in May 2020 Update are now announced.

## Version 20.06

* Resolved many coding style issues and potential bugs with Flake8.
* Announcements such as volume/brightness changes in File Explorer and app update notifications from Microsoft Store can be suppressed by turning off Report Notifications in NVDA's object presentation settings.

## Version 20.05

* Added support for Microsoft Solitaire Collection.
* Microsoft Solitaire Collection: NVDA will announce names of cards and card decks.

## Version 20.03

* IN recent releases of Word 365, NVDA will no longer announce "delete back word" when pressing Control+Backspace.
* Cortana: Text responses from Cortana in version 2 is now announced.
* Mail and Calendar: Added support for upcoming Calendar app.

## Version 20.02

* Initial support for Windows 10 Version 2004 (May 2020 Update).
* Requires Windows 10 Version 1903 or later, end of support for Server 2019 from the add-on.
* Removed app modules for Feedback Hub, File Explorer, Microsoft Edge (EdgeHTML and emergency Chromium based), Search App in 20H1, Shell Experience Host, and Text Input Host/Modern keyboard in 20H1. For 20H1 apps, NVDA itself includes them.
* Removed submenu detection and position announcement workaround for various apps for consistency with recent Windows 10 and app changes.

## Version 20.01

* NVDA 2019.3 is required due to massive internal changes that affect this add-on.
* Various workarounds that were included with the add-on are now part of NVDA. These include silence bug in Mail, suggestion sound bug fix for EdgeHTML based Microsoft Edge, recognizing tool tips from universal apps, among others.
* Settings: Developer mode label for Version 2004 has been corrected.

## Version 19.11

* NVDA 2019.2 is required.
* The following UIA events are recognized: drag target enter, drag target leave, drag target dropped.
* When arranging Start menu tiles or Action center quick actions with Alt+Shift+arrow keys, NVDA will announce information on dragged items or new position of the dragged item.
* Microsoft Edge (Chromium-based): Added emergency support for Edge 79 or later for NVDA 2019.2.1.

## Version 19.10

* Removed Version 1909 detection message from the log.
* NVDA will no longer announce "blank" when pressing up or down arrow to open all apps views in Start menu.
* Cortana: Added support for conversation UI introduced in build 18922 and later, including announcing textual responses from Cortana.
* Modern keyboard: Added support for modern Chinese, Japanese, and Korean (CJK) IME candidates interface introduced in 20H1 build 18965 and later.
* Settings: Storage Sense combo box announcement fix has been added for Version 1909 support.
* Windows Search/File Explorer: NVDA will no longer announce search results twice when reviewing results, which also makes braille output more consistent when reviewing items. This is applicable in Version 1909 (November 2019 Update) and later.

## Version 19.09

* App name and version for various Microsoft Store apps are now shown correctly.
* Calculator: Added support for always on mode in Calculator version 10.1908 and later.
* Microsoft Edge: Removed suggestions sound playback for address omnibar.

## Version 19.08 (Windows 10 turns four years old)

* NVDA 2019.1 is required.
* Initial support for Windows 10 Version 1909 (November 2019 Update).
* Requires Windows 10 Version 1809 or later.
* If running on 1909 builds, NVDA will recognize this fact and record this information in the log.
* Cortana/File Explorer: In build 18945 and later, modern search experience in File Explorer powered by Cortana user interface is supported, which was backported to Version 1909 later.

## Version 19.07

* Added tracking for text change event, and removed active text position change event from being tracked.
* It is possible to tracke only specific events and/or events coming from specific apps.
* In Version 1903 (May 2019 Update), NVDA will announce volume and brightness changes immediately if focused on File Explorer. This is now part of NVDA 2019.2.
* Settings: More information is announced that weren't announced before.

## Version 19.06

* Modern keyboard: NVDA will no longer announce "clipboard" when there are items in the clipboard under some circumstances.
* Modern keyboard: On some systems running Version 1903 (May 2019 Update), NVDA will no longer appear to do nothing when emoji panel opens.
* Settings: In more recent revisions of Version 1803 and later, due to changes to Windows Update procedure for feature updates, a "download and install now" link has been added. NVDA will now announce the title for the new update if present.

## Version 19.05

* In Version 1903, NVDA will announce volume and brightness changes immediately.
* Calculator: NVDA will notify if maximum digit count has been reached while entering expressions.

## Version 19.04

* NVDA 2018.4 is required.
* NVDA will no longer play error tones or do nothing if this add-on becomes active from unsupported releases of Windows 10.
* Removed support for Skype universal app.
* Settings: Odd control labels for certain controls have been corrected.

## Version 19.03

* Initial support for Windows 10 Version 1903 (May 2019 Update).
* NVDA will no longer play error tones or do nothing if this add-on becomes active from Windows 7 and 8.1.
* In build 18323 and later, NVDA will now announce audio volume and brightness changes.
* Mail: NVDA will no longer do anything or play error tones after closing this app.
* Settings: Disk cleanup progress will be announced in System/storage/Storage Sense.
* Settings: In Version 1903, NVDA will correctly recognize options in Storage Sense combo boxes.

## Version 19.02

* Requires Windows 10 Version 1803 or later.
* Standalone add-on update feature has been removed.
* Action center: Item status announcement and brightness button handler is now part of NVDA 2019.1.
* Alarms and clock: Time picker fix is now part of NVDA 2019.1.

## Version 19.01

* Standalone add-on update feature has been marked for deprecation. For future add-on updates, Add-on Updater add-on should be used.
* Microsoft Edge: NVDA will no longer play suggestion sound when pressing F11 to toggle full screen.
* Modern keyboard: In build 18305 and later, NVDA will no longer do nothing when opening emoji panel or cloud clipboard paste screen.
* Settings: No label workaround for various links and radio buttons have been removed, as Settings app ships with proper labels.

## Version 18.12

* Added compatibility flags for use by future NVDA releases.
* When updating the add-on, if the new add-on release requires a newer version of NVDA, an error message will be presented.
* Small changes to how some messages are presented in languages other than English.
* In build 18282 and later, NVDA will no longer announce Start menu size text.
* Modern keyboard: NVDA will announce search results for emojis if possible.
* Settings: Various links added in build 18282 with no labels now have labels.
* Settings: Windows Update reminder dialog is recognized as a proper dialog.

## Version 18.11

* Backported UIA performance enhancement fix from NVDA 2018.4 for users using earlier NVDA releases, removed in 18.11.1 due to an issue with Google Chrome.
* UIA item status property event is now tracked.
* Action center: Brightness quick action is now a button instead of a toggle button.
* Action center: Various status changes such as Focus Assist and Brightness will be reported.
* Mail: Because using table navigation keys to navigate between message rows is not supported, NVDA will advise users of this limitation.
* Microsoft Edge: Text auto-complete will be tracked and announced in address omnibar.
* Modern keyboard: When opening clipboard history (Windows+V in Version 1809) for the first time, NVDA will now announce current clipboard status.
* Modern keyboard: NVDA will no longer play error tones or do nothing when closing emoji panel in more recent Insider Preview builds.
* Modern keyboard: In build 18262 and later (19H1), when emoji panel opens to People category, NVDA will announce first selected emoji instead of selected skin tone modifier to reduce verbosity.
* Settings: In build 18267 and later (19H1), added labels for radio buttons for Search Indexer found in Cortana (Search)/Search Windows page.
* Settings: Progress of Disk Cleanup widget found in Settings/System/Storage/Storage sense/Free up space now page will be announced.
* Settings: NVDA will no longer appear to do nothing or play error tones if using object navigation commands under some circumstances.

## Version 18.10

* NVDA 2018.3 is required.
* If Add-on Updater add-on is installed, that add-on will check for Windows 10 App Essentials updates.
* Default update check interval has changed to weekly checks for both stable and development releases. This is applicable if the add-on itself checks for updates.
* NVDA no longer plays a beep when encountering dialogs.
* Skype: NVDA-specific commands have been removed in Skype 14 due to various UIA issues.

## Version 18.09

* Initial support for Windows 10 Version 1809 (October 2018 Update) and Server 2019.
* Add-on update channel selection is no longer possible in preparation for allowing Add-on Updater (proof of concept) and NVDA to check for add-on updates in the future. To switch channels, visit NVDA Community Add-ons website, go to "Windows 10 App Essentials", and download appropriate version.

## Version 18.08 (Happy Third Birthday, Windows 10)

* Added support for IUIAutomation6 interface (works properly with NVDA 2018.3 or later).
* IN Windows 10 Redstone 5, improved NVDA's responsiveness in some situations by using features introduced in IUIAutomation6, particularly when switching apps while a long-running task is running in the background.
* Updated various add-on source code parts to reflect 2018 changes.
* When tracking events, the sender itself (object where the event came from) is also logged.
* When tracking UIA notification events, debug tone will be heard if notifications came from somewhere other than the active app.
* Expanded submenu handling beyond Shell experience Host, as Microsoft Edge's app menu (Alt+X) contains submenus since Redstone 5.
* Custom handler for looping selector items (not the list) found in Alarms and Clock and Settings apps are no longer included due to improved accessibility of this control in recent Windows 10 releases.
* Added support for recent releases of People (modern Outlook/Contacts) app (via a dedicated app module).
* Modern keyboard: When opening clipboard items list in redstone 5, NVDA will no longer announce "Clipboard" (the label for the list itself) when this panel is opened.
* People: In recent app releases, NVDA will once again announce top suggestions when searching for contacts.

## Version 18.07

* Requires Windows 10 Version 1709 or later.
* Added UIA active text position change event (Redstone 5) to list of events to be tracked in debug mode.
* NVDA will play a tone and log a message when encountering a dialog (through use of IsDialog property (Redstone 5) or after consulting a list of known dialog class names).
* NVDA will recognize alert text in various apps and announce them via live region changed event. This includes aria-role=alert element in Microsoft Edge and other apps.
* Calculator: Calculation results are no longer treated as headings.
* Modern keyboard: Reduced unnecessary verbosity when working with modern keyboard and its features. These include no longer announcing "Microsoft Candidate UI" when opening hardware keyboard input suggestions and staying silent when certain touch keyboard keys raise name change event on some systems.
* Modern keyboard: In build 17704 and later, reduced verbosity when browsing emojis.
* Settings: More messages about Windows Update status are announced, especially if Windows Update encounters errors.
* Settings: In Version 1803 and later, headings are announced when using object navigation to review screen content.
* Settings: In Settings/Update and Security/Recovery/Reset, initial progress messages and content changes are announced.

## Version 18.06

* Requires NVDA 2018.2.
* Various fixes included in this add-on are now part of NVDA. These include no more announcement of "unknown" when opening quick link menu (Windows+X), announcing notifications from newer apps releases and so on.
* In Windows 10 Redstone 5 builds with Sets enabled, when switching between Sets tabs, NVDA will announce name and position of the tab you are switching to.
* NVDA will no longer announce Start menu size text when changing screen resolutions or orientation.
* NVDA will announce various dialogs as "dialog".
* Calculator: NVDA will announce unit conversion values in recent Calculator releases.
* Microsoft Edge: NVDA will announce more notifications, including Reading View availability.

## Version 18.05

* When opening, closing, or switching between virtual desktops, NVDA will announce current desktop ID (desktop 2, for example).
* When opening a new Sets tab (Redstone 5) and search for items in the embedded Cortana search box, NVDA will announce suggestions and let you navigate context menus for certain items.
* Modern keyboard: In Windows 10 Version 1803, with hardware keyboard input suggestion turned on and if NVDA is set to announce all candidates via input composition settings dialog/panel, NVDA will announce the first suggestion as you type.
* Modern keyboard: Resolved a major problem where NVDA may play error sounds when trying to start dictating text (Windows+H) on recent Windows 10 releases.
* Modern keyboard: Added support for redesigned emoji panel and announcing paste candidates for cloud clipboard in Redstone 5.

## Version 18.04 (Spring Creators/April 2018 Update)

* Added tracking support for UIA drag events, including drag start, drag cancel, and drag complete, as well as tooltip opened UIA event.
* Tooltips from Edge and universal apps will be recognized and announced.
* NVDA will not announce notifications (powered by UIA notification event) from background apps.
* NVDA will no longer announce "unknown" when opening quick link menu (Windows+X).
* On build 17627 and later, when opening a new Sets tab (Control+Windows+T), NVDA will announce search results when searching for things in the embedded Cortana window.
* Feedback hub: In recent app releases, if running NVDA 2018.1 or later, NVDA will no longer announce feedback categories twice.
* Settings: Resolves more issues with audio volume progress beep in Settings/System/Sound in Version 1803.
* Windows Store: Product update announcements on recent releases (11801 and later) are more reliable.

## Version 18.03 (Thunderbolt)

* Initial support for Windows 10 Version 1803 (April 2018 Update).
* Restored compatibility with NVDA 2017.4.
* NVDA will now track UIA notification event introduced in Version 1709 (Fall Creators Update). This allows NVDA to announce notifications in apps such as Microsoft Edge, Microsoft Store, Calculator, Alarms and Clock and others. With debug logging enabled, NVDA will output debug information about this event to the log.
* Added support for IUIAutomation4 and IUIAutomation5 interfaces (works properly with NVDA 2018.1 or later).
* Calculator: Resolved double-speaking issue when announcing calculation results in some areas.

## Version 18.02

* Resolved a critical issue with add-on update feature with NVDA next snapshots running.
* UIA notification event (introduced in Version 1709) is tracked and a debug tone will be heard if NVDA is restarted with debug logging enabled.
* Added a workaround in recent versions of Calculator and Skype where new information isn't announced (such as calculation results or new chat messages).
* Modern keyboard: In post-1709 builds (past 16299), when emoji panel opens, NVDA will announce first selected emoji.
* Settings: More status messages are announced.

## Version 18.01

* Requires Windows 10 Version 1703 or later, end of support for Server 2016 from the add-on.
* Calculator: In various parts of Calculator (such as unit converter), NVDA will now announce results as soon as values are entered.
* Modern keyboard: Fixed double speaking of hardware input suggestions in build 17063.
* Settings: More information (especially information pertaining to updates in build 17063) are announced.

## Version 17.12

* Modern keyboard: Added support for announcing hardware keyboard input suggestions in build 17040 and later.
* Settings: In build 17035 and later, volume progress bar beeps are no longer heard.

## Version 17.11

* Fixed conflict with accelerator key for Windows 10 App Essentials dialog with that of Windows 10 OCR dialog introduced in NVDA 2017.4 snapshots.
* Skype: Improved message announcements.

## Version 17.10 (Fall Creators Update)

* Modern keyboard: When looking up emojis via emoji panel, NVDA will announce emoji categories when moving to different emoji categories.
* Settings: In more recent Windows Insider Preview builds, feature update entries are properly recognized in Update and Security/Windows Update/update history.

## Version 17.09 (Second Anniversary)

* Requires NVDA 2017.3.
* Action center: The workaround in place for tab key issue in recent Fall Creators Update releases is gone, as Windows itself provides a fix.
* Windows Store: In latest update (version 11708), content download progress is once again reported.

## Version 17.08 (Windows 10 Birthday Edition)

* Initial support for Windows 10 Version 1709 (Fall Creators Update).
* In Windows 10 App Essentials dialog, when changing update channels, if the previous channel was stable and then switched to development branch, a warning message will be presented when closing the dialog. Be sure to read the message and choose carefully, as development builds sometimes include features that could break on some systems.
* Action center: In recent Fall Creators Update preview builds, when Action center has no notifications and if you press Tab to move between items, you'll find that it won't work. A temporary workaround is now part of this add-on to restore this functionality until Microsoft comes up with a fix.
* Calculator: NVDA will announce live region changes when appropriate. This is done when the app is in converter mode, especially unit and currency conversion.
* Settings: In Windows 10 Fall Creators Update preview build 16251 and later, NVDA will no longer play error tones or appear to do nothing when pressing Tab from Wi-Fi network connections window.
* Skype: In recent releases, NVDA may not announce chat messages or play error tones when you press Control+NVDA+number row. This has been corrected.

## Version 17.07

* Requires Windows 10 Version 1607 or later.
* When tracking live region change events, the debug information will say "liveRegionChange" to align with work being done by NV Access to support live region change event everywhere.
* Added tracking information for element selected and window opened events, the latter used to help NV Access troubleshoot toast announcement problem.
* Alerts in Edge and other applications that use live region change event is announced. In some cases, this may result in double-speaking.
* A new "development pilot" channel (hidden) is introduced, designed for people using NVDA and Windows 10 App Essentials development snapshots. The code in this channel removes legacy code and is designed to respond to changes made in NVDA master or next snapshots.
* In Version 1703 and later, toasts will no longer be announced multiple times.
* When pressing Windows+G to open Game Bar, NVDA will announce appearance of this window. Due to technical limitations, NVDA cannot interact with Game Bar.
* Refinements to emoji panel support in Fall Creators Update. Specifically, emoji panel support is now contained in an app module instead of being part of the WinTenObjects global plugin.

## Version 17.06

* Requires NVDA 2017.2.
* Certain workarounds are deprecated as NVDA itself will include them. These include announcing value changes for some combo boxes in Settings app. The workarounds that were part of the add-on will be removed once a stable version of NVDA that includes them is released.
* UIA system alert events are now tracked.
* Various tweaks to search field detection and handling in more apps.
* In Settings and other apps where search suggestions are viewable, when you move through search suggestions, braille will show suggestions themselves instead of showing the edit field content. Note that this does not work on Start menu at the moment.
* Initial support for floating Emoji input panel in Windows 10 build 16215 or later (for best results, use Windows OneCore speech synthesizer).
* In People app or when looking up contacts in My People (Redstone 3), NVDA will play suggestion sounds when contact suggestions appear.
* Calculator: When Escape is pressed to clear the results window, NVDA will announce "display is 0".
* Mail: Added support for recent versions of Mail app due to executable file being renamed.
* Mail: In Mail app, when writing a message, using at mentions (@) results in a list of contact suggestions appearing. NVDA will detect this and play suggestions sounds.
* Microsoft Edge: Alerts on websites such as YouTube are now announced.
* Settings: Windows Update download status is now announced in Windows 10 build 16215 or later.
* Skype: Various issues when using Skype with braille displays fixed, including inability to read items in message history.
* Skype: You can now press NVDA+D from message history to read details about a message such as channel, sent date and time and so on.
* Skype: You can now use Skype commands while using My People.

## Version 17.05

* A new set of suggestion sounds were added, replacing the previous sounds set.
* Laid the foundation to support wxPython 4.
* Windows store: Fixed errors seen in Windows Store app where download progress wasn't announced.
* Settings: In Version 1607 (build 14393) and later, update titles in Settings/Update and Security/Windows Update/Update history is now announced.

## Version 17.04 (Creativity Edition)

* Skype: Keyboard shortcuts has changed in order to avoid conflicts with commands introduced in March 2017 update. The new commands are: Alt+1 for conversations, Alt+2 for contacts, Alt+3 for bots, and Alt+4 to go to chat edit field if visible (the last command works if the add-on is installed).

## Version 17.03

* Initial support for Windows 10 Version 1703 (Creators Update).
* Improved add-on update download and installation experience: no longer need to respond to a browser window, and no more installation prompts.
* Improved support for newer style time picker controls found in Creators Update and February 2017 update to Alarms and Clock app.
* When viewing results from Start search box, NVDA will no longer announce items twice.
* Removed app modules for Bank of America, TeamViewer Touch, Twitter, and Windows Defender Security Center.
* Thanks to work from Microsoft, Windows Defender Security Center workaround is no longer required. Consequently, the app module for this app has been removed.
* Maps: When street view is active and "use keyboard" option is enabled, NVDA will announce street addresses as you use arrow keys to navigate a map.
* Microsoft Edge: In Version 1703, NVDA will no longer announce "WebRuntime Content View" when moving to another site.
* Settings: Added labels for certain combo boxes, Bluetooth passcode field in Devices/Bluetooth (Devices/Bluetooth and other devices in Creators Update) and Game Bar key assignment grid (Gaming/Game Bar in Creators Update).
* Settings: New values are now announced for certain combo boxes.

## Version 17.02

* Requires NVDA 2016.4 or later.
* Added ability to check for add-on updates (automatic or manual) via the new Windows 10 App Essentials dialog found in NVDA Preferences menu. By default, stable and development versions will check for new updates automatically on a weekly or daily basis, respectively.
* NVDA can announce suggestion count when performing a search in majority of cases. This option is controlled by "Report object position information" in Object presentation dialog.
* Added support for Windows Defender Security Center in build 15007 or later. Windows Defender in build 14986 is also supported.
* Mail: When reviewing items in messages list, you can now use table navigation commands to review message headers.
* Skype Preview: NVDA will no longer announce "Skype Message" when reviewing messages for majority of cases.
* Windows Store: When downloading content such as apps and movies, NVDA will announce product name and download progress.

## Version 17.01

* Settings: Settings groups are recognized when using object navigation to navigate between controls.
* Windows Store: Appearance of search suggestions are announced.

## Version 16.12

* Requires Windows 10 Version 1511 or later.
* In time pickers in Alarms and Clock and similar controls, control labels and values are announced when moving focus to them.
* Added support for Groove Music and Windows Defender (Redstone 2).
* Groove Music: Appearance of suggestions while searching for tracks is now recognized.
* Windows Defender (UWP for Insiders): Button labels will be announced.

## Version 16.11

* Settings: NVDA will no longer play error tones or not say things when announcing certain information from Settings/Update and Security/Windows Update.
* Skype Preview: You can use Alt+number row keys to locate (and move to) contacts list (1), conversations (2) or chat edit field (3). NVDA will warn you if it cannot find these elements, and you need to select the correct tab (radio button) in order to move to the desired part of Skype Preview.
* Skype Preview: Settings combo box labels are now announced (seen in November 2016 release).
* Windows Store: Support for November 2016 version of Windows Store.

## Version 16.10

* NVDA can now recognize UIA live region changed event as name change events.
* In Start menu, top search suggestion is brailled.
* Position information in context menus is no longer announced.
* Cortana: NVDA will announce reminder confirmation.
* Mail and calendar: "edit" and "read-only" are no longer announced.
* Microsoft Edge: Address bar suggestions are now recognized.
* Settings: Search status such as announcement of when no results are available are announced.

## Version 16.09

* Requires NVDA 2016.3 for optimal experience, and will not run on Windows releases earlier than 7 Service Pack 1 in consideration for users who would like to upgrade to Windows 10.
* In certain search fields, suggestions will appear as you enter search terms. NVDA will notify you via sound when suggestions appear. You can also use up and down arrow keys to move through suggestions. Examples of this enhancement include search field in Settings app.
* Added support for Mail and Calendar, Maps, MSN Weather, and Windows Store.
* Cortana: Fixed a long standing issue where NVDA kept announcing gibberish while talking to Cortana.
* Mail and Calendar: NVDA no longer announces "read-only" for Calendar's appointment name field and Mail's message content.
* Maps: Fixed an issue where one could not use TAB key to move between controls.
* MSN Weather: Recognition of tabs and ability to use up and down arrow keys to read forecast for each day (contributed by Derek Riemer).
* Settings: When checking for updates in Settings/Update and security/Windows Update, update progress messages such as "downloading" are announced once instead of repeated as percentage changes.
* Skype Preview: Reduced verbosity of chat messages, as well as ability to move navigator object to a chat item when Control+NVDA+number row is pressed just like Skype for Desktop.
* Skype Preview: Fixed an issue when pressing Control+NVDA+number row where it did nothing or played error tones.
* Windows Store: After checking for app updates, app names in list of apps to be updated are labeled correctly.

## Version 16.08 (Anniversary Celebratory Edition)

* Introduced localizations.
* Basic support for Skype Preview (UWP) app.
* Cortana: Added support for new Cortana command Windows+Shift+C).
* Settings: When combo box items are changed, NVDA will no longer announce items multiple times.
* Skype Preview: NVDA will announce who is typing while chatting, and partial return of Control+NVDA+number row commands to read chat history.

## Version 16.07

* Initial support for Windows 10 Version 1607 (Anniversary Update) and Server 2016.
* Laid the foundation for localization into other languages.
* Microsoft Edge: Newer version of Microsoft Edge (part of Anniversary Update) is supported.
* Cortana: Cortana listening mode command has changed in Insider build 14383 (it is now Windows+Shift+C).

## Version 16.06

* Code repository and releases moved to GitHub.
* Uninstall dialog for UWP apps is recognized as a proper dialog.
* Added support for Bank of America UWP app, Redstone 1 version of Calculator, and improved support for microsoft Edge.
* Bank of America: Button labels are now announced.
* Microsoft Edge: Notifications from Edge are now announced.

## Version 16.05

* Certain dialogs are now recognized as proper dialogs. These include Insider Preview dialog (settings app) and new-style UAC dialog in build 14328 and later.

## Version 16.04

* Insider Hub has been renamed to Feedback Hub in Redstone 1.
* Added support for looping selectors in Redstone 1.

## Version 16.03

* When minimizing windows (Windows+M), "pane" is no longer announced (noticeable if using Insider Preview builds) for Redstone 1/Version 1607.
* Added support for Cortana.
* Cortana: Textual responses from Cortana are announced in most situations.
* Cortana: NVDA will try to stay silent when voice interaction command (Windows+C) is pressed.

## Version 16.02

* In context menus for Start Menu tiles, submenus are properly recognized.
* Added support for Settings app.
* Settings: Certain information such as Windows Update progress is now reported automatically.

## Version 15.12

This is the first stable version of Windows 10 App Essentials add-on.

* Initial support for Windows 10 Version 1511 (November Update).
* Fixed an issue where certain combo box items, notably some combo boxes in Settings app were not announced.

## Version 15.11

* Added Windows 10 Controls global plugin.
* Added support for looping selectors for selecting time in Windows Update, Alarms and Clock and others.
* Added a patch in app module handler to allow loading app modules for executables with a dot in the middle of the name.
* Added support for Alarms and Clock, TeamViewer Touch, universal app version of Twitter.
* Alarms and clock: Time picker values are announced. This also affects the control used to select when to restart to finish installing Windows updates.
* Calculator: Pressing Numpad Enter will let NVDA announce calculation results.
* TeamViewer Touch: Lables for buttons are announced.
* Twitter: Button labels are announced.

## Version 15.09

This is the first testing release of Windows 10 App Essentials add-on. Although version text is shown as "15.9", it is named "15.09" in this document for consistency with future releases.

* Initial public release on Windows 10 Version 1507 (RTM).
* Added support for modern Calculator and Insider Hub (Windows insiders only).
* Calculator: When ENTER is pressed, NVDA announces calculation results.
* Insider Hub: Meant to be used by Windows Insiders running an Insider build.
* Insider Hub: Labels for radio buttons are announced.

## Insider Hub (prerelease/Version 15.08)

Originally known as "Insider Hub" and meant to provide support for Insider Hub app, used by Windows Insiders.
