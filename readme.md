# Windows 10 App Essentials

* Authors: Joseph Lee, Derek Riemer and other Windows 10 users
* Download [stable version][1]
* Download [development version][2]

This add-on is a collection of app modules for various Windows 10 apps, as well as fixes for certain windows 10 controls.

The following app modules or support modules for some apps are included (see each app section for details on what is included):

* Alarms and Clock.
* Calendar
* Calculator (modern).
* Cortana
* Game Bar
* Groove Music
* Mail
* Maps
* Microsoft Edge
* People
* Settings (system settings, Windows+I)
* Skype (universal app)
* Store
* Weather.
* Miscellaneous modules for controls such as Start Menu tiles.

Note: this add-on requires Windows 10 Version 1607 (build 14393) or later and NVDA 2017.1 or later. For best results, use the add-on with latest stable build (build 15063) and latest stable version of NVDA. Also, after changing update settings for the add-on, be sure to save NVDA settings.

## General

* In context menus for Start Menu tiles, submenus are properly recognized.
* Certain dialogs are now recognized as proper dialogs. These include Insider Preview dialog (settings app) and new-style UAC dialog in build 14328 and later for NvDA 2016.2.1 or earlier.
* Appearance/close of suggestions for certain search fields (notably Settings and Store apps) is announced via sounds and braille. This also includes Start menu search box. This is scheduled to be included in NVDA 2017.3.
* NVDA can announce suggestion count when performing a search in majority of cases. This option is controlled by "Report object position information" in Object presentation dialog.
* In certain context menus (such as in Edge), position information (e.g. 1 of 2) is no longer announced.
* The following UIA events are recognized: Controller for, live region change, system alert, element selected, window opened. With NVDA set to run with debug logging enabled, these events will be tracked.
* Added ability to check for add-on updates (automatic or manual) via the new Windows 10 App Essentials dialog found in NvDA Preferences menu. By default, stable and development versions will check for new updates automatically on a weekly or daily basis, respectively.
* Initial support for floating Emoji input panel in build 16215 or later (for best experience when reading emojis, use Windows OneCore speech synthesizer).
* In some apps, live region text is announced. This includes alerts in Edge, results in Calculator and others. Note that this may result in double-speaking in some cases.
* Toasts are no longer announced multiple times in Creators Update and later. This fix is included in NVDA 2017.3.

## Alarms and clock

* Time picker values are now announced, noticeable when moving focus to picker controls. This also affects the control used to select when to restart to finish installing Windows updates.

## Calculator

* When ENTER or Escape is pressed, NVDA announces calculation results.
* For calculations such as unit converter and currency converter, NVDA will announce results as soon as calculations are entered.

## calendar

* NVDA no longer announces "edit" or "read-only" in message body and other fields.

## Cortana

* Textual responses from Cortana are announced in most situations (if it doesn't, reopen Start menu and try searching again).
* NVDA will be silent when you talk to Cortana via voice.
* NVDA will now announce reminder confirmation after you set one.

## Game Bar

* NVDA will announce appearance of Game Bar window. Due to technical limitations, NVDA cannot interact fully with Game Bar.

## Groove Music

* Appearance of suggestions when searching for tracks is now detected.

## Mail

* When reviewing items in messages list, you can now use table navigation commands to review message headers.
* When writing a message, appearance of at mention suggestions are indicated by sounds.

## Maps

* NVDA plays location beep for map locations.
* When using street side view and if "use keyboard" option is enabled, NVDA will announce street addresses as you use arrow keys to navigate the map.

## Microsoft Edge

* Notifications such as file downloads and various webpage alerts are now announced.
* In Creators Update, NVDA will no longer announce "WebRuntime Content View" when going to another site.

## People

* When searching for contacts, a sound will play if there are search results.

## Settings

* Certain information such as Windows Update progress is now reported automatically.
* Progress bar values and other information are no longer announced twice.
* If it takes a while to search for settings, NVDA will announce "searching" and search result status such as if a setting cannot be found.
* Settings groups are recognized when using object navigation to navigate between controls.
* For some combo boxes, NVDA will no longer fail to recognize labels and/or announce value changes.

## Skype

* Typing indicator text is announced just like Skype for Desktop client.
* Partial return of Control+NvDA+number row commands to read recent chat history and to move navigator object to chat entries just like Skype for Desktop.
* You can now press Alt+number row to locate and move to conversations (1), contacts list (2), bots (3) and chat edit field if visible (4). Note that these commands will work properly if Skype update released in March 2017 is installed.
* Combo box labels for Skype preview app released in November 2016 are announced.
* NVDA will no longer announce "Skype Message" when reviewing messages for majority of cases.
* Various issues when using Skype with braille displays fixed, including inability to review message history items in braille.
* From message history list, pressing NVDA+D on a message item will now allow NVDA to announce detailed information about a message such as channel type, sent date and time and so on.

## Store

* After checking for app updates, app names in list of apps to be updated are correctly labeled.
* Appearance of search suggestions are now announced.
* When downloading content such as apps and movies, NVDA will announce product name and download progress.

## Weather

* Tabs such as "forecast" and "maps" are recognized as proper tabs (patch by Derek Riemer).
* when reading a forecast, use the left and right arrows to move between items. Use the up and down arrows to read the individual items. For example, pressing the right arrow might report "Monday: 79 degrees, partly cloudy, ..." pressing the down arrow will say "Monday" Then pressing it again will read the next item (Like the temperature). This currently works for daily and hourly forecasts.

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev
