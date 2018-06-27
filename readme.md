# Windows 10 App Essentials

* Authors: Joseph Lee, Derek Riemer and other Windows 10 users
* Download [stable version][1]
* Download [development version][2]

This add-on is a collection of app modules for various Windows 10 apps, as well as enhancements and fixes for certain windows 10 controls.

The following app modules or support modules for some apps are included (see each app section for details on what is included):

* Alarms and Clock.
* Calendar
* Calculator (modern).
* Cortana
* Feedback Hub
* Game Bar
* Mail
* Maps
* Microsoft Edge
* Modern keyboard (emoji panel/hardware input suggestions/cloud clipboard items in Version 1709 and later)
* People
* Settings (system settings, Windows+I)
* Skype (universal app)
* Store
* Weather.
* Miscellaneous modules for controls such as Start Menu tiles.

Notes:

* This add-on requires Windows 10 Version 1709 (build 16299) or later and NVDA 2018.2 or later. For best results, use the add-on with latest Windows 10 stable release (build 17134) and latest stable version of NVDA.
* Some add-on features are or will be part of NVDA screen reader.
* For entries not listed below, you can assume that features are part of NVDA, no longer applicable as the add-on does not support old Windows 10 releases, or changes were made to apps that makes entries no longer applicable.

For a list of changes made between each add-on releases, refer to [changelogs for add-on releases][3] document.

## General

* In context menus for Start Menu tiles, submenus are properly recognized.
* Certain dialogs are now recognized as proper dialogs and reported as such, including Insider Preview dialog (settings app).
* NVDA can announce suggestion count when performing a search in majority of cases. This option is controlled by "Report object position information" in Object presentation dialog/panel.
* In certain context menus (such as in Edge), position information (e.g. 1 of 2) is no longer announced.
* The following UIA events are recognized: active text position change, controller for, drag start, drag cancel, drag complete, element selected, live region change, notification, system alert, tooltip opened, window opened. With NVDA set to run with debug logging enabled, these events will be tracked, and for UIA notification event, a debug tone will be heard.
* Added ability to check for add-on updates (automatic or manual) via Windows 10 App Essentials dialog found in NvDA Preferences menu. By default, stable and development versions will check for new updates automatically on a weekly or daily basis, respectively.
* In some apps, live region text is announced. This includes alerts in Edge, results in Calculator and others. Note that this may result in double-speaking in some cases.
* Notifications from newer app releases on Windows 10 Version 1709 (build 16299) and later are announced.
* Tooltips from Edge and universal apps are recognized and will be announced.
* With Sets turned on (builds 17627 through 17692 for some insiders), when opening a new Sets tab (Control+Windows+T), NVDA will announce search results when searching for items in the embedded Cortana window.
* With Sets turned on, when switching between Sets tabs, NvDA will announce name and position of the tab you are switching to.
* When opening, closing, or switching between virtual desktops, NVDA will announce current desktop ID (desktop 2, for example).
* NVDA will no longer announce Start menu size text when changing screen resolutions or orientation.

## Alarms and clock

* Time picker values are now announced, noticeable when moving focus to picker controls. This also affects the control used to select when to restart to finish installing Windows updates.

## Calculator

* When ENTER or Escape is pressed, NVDA announces calculation results.
* For calculations such as unit converter and currency converter, NVDA will announce results as soon as calculations are entered.

## calendar

* NVDA no longer announces "edit" or "read-only" in message body and other fields.

## Cortana

* Textual responses from Cortana are announced in most situations (if it doesn't, reopen Start menu and try searching again).
* NVDA will be silent when talking to Cortana via voice.
* NVDA will now announce reminder confirmation after you set one.

## Feedback Hub

* For newer app releases, NVDA will no longer announce feedback categories twice.

## Game Bar

* NVDA will announce appearance of Game Bar window. Due to technical limitations, NVDA cannot interact fully with Game Bar.

## Mail

* When reviewing items in messages list, you can now use table navigation commands to review message headers.
* When writing a message, appearance of at mention suggestions are indicated by sounds.

## Maps

* NVDA plays location beep for map locations.
* When using street side view and if "use keyboard" option is enabled, NVDA will announce street addresses as you use arrow keys to navigate the map.

## Microsoft Edge

* Notifications such as file downloads and various webpage alerts, as well as availability of Reading View (if using Version 1709 and later) are announced.

## Modern keyboard

* Support for Emoji input panel in Version 1709 (Fall Creators Update) and later, including the redesigned panel in build 17661 and later. For best experience when reading emojis, use Windows OneCore speech synthesizer.
* Support for hardware keyboard input suggestions in Version 1803 (April 2018 Update) and later.
* In post-1709 builds, NVDA will announce the first selected emoji when emoji panel opens.
* Support for announcing cloud clipboard items in build 17666 (Redstone 5) and later.
* Reduced unnecessary verbosity when working with modern keyboard and its features. These include no longer announcing "Microsoft Candidate UI" when opening hardware keyboard input suggestions and staying silent when certain touch keyboard keys raise name change event on some systems.

## People

* When searching for contacts, a sound will play if there are search results.

## Settings

* Certain information such as Windows Update progress is reported automatically.
* Progress bar values and other information are no longer announced twice.
* Settings groups are recognized when using object navigation to navigate between controls.
* For some combo boxes, NVDA will no longer fail to recognize labels and/or announce value changes.
* Audio Volume progress bar beeps are no longer heard in Version 1803 and later.
* More messages about Windows Update status are announced, especially if Windows Update encounters errors.

## Skype

* Typing indicator text is announced just like Skype for Desktop client.
* Control+NvDA+number row commands, used to read recent chat history and to move navigator object to chat entries in Skype for Desktop, is also available in Skype UWP.
* You can press Alt+number row to locate and move to conversations (1), contacts list (2), bots (3) and chat edit field if visible (4). Note that these commands will work properly if Skype update released in March 2017 is installed.
* NVDA will no longer announce "Skype Message" when reviewing messages for majority of cases.
* From message history list, pressing NVDA+D on a message item will allow NVDA to announce detailed information about a message such as channel type, sent date and time and so on.

## Store

* After checking for app updates, app names in list of apps to be updated are correctly labeled.
* When downloading content such as apps and movies, NVDA will announce product name and download progress.

## Weather

* Tabs such as "forecast" and "maps" are recognized as proper tabs (patch by Derek Riemer).
* when reading a forecast, use the left and right arrows to move between items. Use the up and down arrows to read the individual items. For example, pressing the right arrow might report "Monday: 79 degrees, partly cloudy, ..." pressing the down arrow will say "Monday" Then pressing it again will read the next item (Like the temperature). This currently works for daily and hourly forecasts.

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
