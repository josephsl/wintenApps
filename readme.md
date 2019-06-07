# Windows 10 App Essentials

* Authors: Joseph Lee, Derek Riemer and other Windows 10 users
* Download [stable version][1]
* Download [development version][2]
* NVDA compatibility: 2018.4 to 2019.1

This add-on is a collection of app modules for various Windows 10 apps, as well as enhancements and fixes for certain windows 10 controls.

The following app modules or support modules for some apps are included (see each app section for details on what is included):

* Action center
* Alarms and Clock.
* Calendar
* Calculator (modern).
* Cortana
* Feedback Hub
* Mail
* Maps
* Microsoft Edge
* Modern keyboard (emoji panel/dictation/hardware input suggestions/cloud clipboard items in Version 1709 and later)
* People
* Settings (system settings, Windows+I)
* Store
* Weather.
* Miscellaneous modules for controls such as Start Menu tiles.

Notes:

* This add-on requires Windows 10 Version 1803 (build 17134) or later and NVDA 2018.4 or later. For best results, use the add-on with latest Windows 10 stable release (build 18362) and latest stable version of NVDA.
* Some add-on features are or will be part of NVDA screen reader.
* For entries not listed below, you can assume that features are part of NVDA, no longer applicable as the add-on does not support old Windows 10 releases, or changes were made to Windows 10 and apps that makes entries no longer applicable.

For a list of changes made between each add-on releases, refer to [changelogs for add-on releases][3] document.

## General

* NVDA will no longer play error tones or do nothing if this add-on becomes active from Windows 7, Windows 8.1, and unsupported releases of Windows 10.
* Submenu items are properly recognized in various apps, including context menu for Start menu tiles and microsoft Edge's app menu (Redstone 5).
* In addition to dialogs recognized by NVDA, more dialogs are now recognized as proper dialogs and reported as such, including Insider Preview dialog (settings app).
* NVDA can announce suggestion count when performing a search in majority of cases. This option is controlled by "Report object position information" in Object presentation panel found in NVDA settings.
* In certain context menus (such as in Edge), position information (e.g. 1 of 2) is no longer announced.
* The following UIA events are recognized: active text position change, controller for, drag start, drag cancel, drag complete, element selected, item status, live region change, notification, system alert, text change, tooltip opened, window opened. With NVDA set to run with debug logging enabled, these events will be tracked, and for UIA notification event, a debug tone will be heard if notifications come from somewhere other than the currently active app.
* Tooltips from Edge and universal apps are recognized and will be announced.
* When opening, closing, or switching between virtual desktops, NVDA will announce current desktop name (desktop 2, for example).
* NVDA will no longer announce Start menu size text when changing screen resolutions or orientation.
* In Version 1903 (May 2019 Update), NVDA will announce volume and brightness changes immediately.

## Action center

* Brightness quick action is now a button instead of a toggle button. This is now part of NVDA 2019.1.
* Various status changes such as Focus Assist and Brightness will be reported. This is now part of NVDA 2019.1.

## Alarms and clock

* Time picker values are now announced, noticeable when moving focus to picker controls. This also affects the control used to select when to restart to finish installing Windows updates. This is now part of NVDA 2019.1.

## Calculator

* When ENTER or Escape is pressed, NVDA announces calculation results.
* For calculations such as unit converter and currency converter, NVDA will announce results as soon as calculations are entered.
* NVDA will no longer announce "heading level" for calculator results.
* NVDA will notify if maximum digit count has been reached while entering expressions.

## calendar

* NVDA no longer announces "edit" or "read-only" in message body and other fields.

## Cortana

* Textual responses from Cortana are announced in most situations (if it doesn't, reopen Start menu and try searching again).
* NVDA will be silent when talking to Cortana via voice.
* NVDA will now announce reminder confirmation after you set one.

## Feedback Hub

* For newer app releases, NVDA will no longer announce feedback categories twice.

## Mail

* When reviewing items in messages list, you can now use table navigation commands to review message headers. Note that navigating between rows (messages) is not supported.
* When writing a message, appearance of at mention suggestions are indicated by sounds.
* NVDA will no longer do anything or play error tones after closing this app. This is now part of NVDA 2019.1.

## Maps

* NVDA plays location beep for map locations.
* When using street side view and if "use keyboard" option is enabled, NVDA will announce street addresses as you use arrow keys to navigate the map.

## Microsoft Edge

* Text auto-complete will be tracked and announced in address omnibar.
* NVDA will no longer play suggestion sound when pressing F11 to toggle full screen.

## Modern keyboard

Note: most features below are now part of NVDA 2018.3 or later.

* Support for Emoji input panel in Version 1709 (Fall Creators Update) and later, including the redesigned panel in Version 1809 (build 17661 and later) and changes made in 19H1 (build 18262 and later, including kaomoji and symbols categories in build 18305). If using NVDA releases earlier than 2018.4, for best experience when reading emojis, use Windows OneCore speech synthesizer. If 2018.4 or later is in use, enable Unicode Consortium setting from NvDA's speech settings and set symbol level to "some" or higher.
* Support for hardware keyboard input suggestions in Version 1803 (April 2018 Update) and later.
* In post-1709 builds, NVDA will announce the first selected emoji when emoji panel opens. This is more noticeable in build 18262 and later where emoji panel may open to last browsed category, such as displaying skin tone modifiers when opened to People category.
* Support for announcing cloud clipboard items in Version 1809 (build 17666 and later).
* Reduced unnecessary verbosity when working with modern keyboard and its features. These include no longer announcing "Microsoft Candidate UI" when opening hardware keyboard input suggestions and staying silent when certain touch keyboard keys raise name change event on some systems.
* NVDA will no longer play error tones or do nothing when closing emoji panel in more recent 19H1 Insider Preview builds. This is now part of NVDA 2019.1.
* In Version 1809 (October 2018 Update) and later, NVDA will announce search results for emojis if possible. This is now part of NVDA 2019.1.
* NVDA will no longer announce "clipboard" when there are items in the clipboard under some circumstances.
* On some systems running Version 1903 (May 2019 Update), NVDA will no longer appear to do nothing when emoji panel opens.

## People

* When searching for contacts, first suggestion will be announced, particularly if using recent app releases.

## Settings

* Certain information such as Windows Update progress is reported automatically, including Storage sense/disk cleanup widget and errors from Windows Update.
* Progress bar values and other information are no longer announced twice.
* For some combo boxes and radio buttons, NVDA will no longer fail to recognize labels and/or announce value changes.
* Audio Volume progress bar beeps are no longer heard in Version 1803 and later.
* NVDA will no longer appear to do nothing or play error tones if using object navigation commands under some circumstances.
* Windows Update reminder dialog is recognized as a proper dialog.
* Odd control labels seen in certain Windows 10 installations has been corrected.
* In more recent revisions of Version 1803 and later, due to changes to Windows Update procedure for feature updates, a "download and instlal now" link has been added. NVDA will now announce the title for the new update if present.

## Store

* After checking for app updates, app names in list of apps to be updated are correctly labeled.
* When downloading content such as apps and movies, NVDA will announce product name and download progress.

## Weather

* Tabs such as "forecast" and "maps" are recognized as proper tabs (patch by Derek Riemer).
* when reading a forecast, use the left and right arrows to move between items. Use the up and down arrows to read the individual items. For example, pressing the right arrow might report "Monday: 79 degrees, partly cloudy, ..." pressing the down arrow will say "Monday" Then pressing it again will read the next item (Like the temperature). This currently works for daily and hourly forecasts.

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
