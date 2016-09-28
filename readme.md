# Windows 10 App Essentials

* Authors: Joseph Lee, Derek Riemer and other Windows 10 users
* Download [stable version][1]
* Download [development version][2]

This add-on is a collection of app modules for various Windows 10 apps, as well as fixes for certain windows 10 controls.

The following app modules or support modules for some apps are included (see each app section for details on what is included):

* Alarms and Clock.
* Bank of America
* Calendar
* Calculator (modern).
* Cortana
* Mail
* Maps
* Microsoft Edge
* Settings (system settings, Windows+I).
* Skype Preview
* Store
* Twitter.
* TeamViewer Touch.
* Weather.
* Miscellaneous modules for controls such as Start Menu tiles.

Note: this add-on requires Windows 10 Version 1507 (build 10240) or later and NVDA 2016.3 or later.

## General

* In context menus for Start Menu tiles, submenus are properly recognized.
* When minimizing windows (Windows+M), "pane" is no longer announced (noticeable if using Insider Preview builds).
* Certain dialogs are now recognized as proper dialogs. This include Insider Preview dialog (settings app) and new-style UAC dialog in build 14328 and later for NvDA 2016.2.1 or earlier.
* Appearance/close of suggestions for certain search fields (notably Settings app) is announced via sounds and/or brailled.
* In certain context menus (such as in Edge), position information (e.g. 1 of 2) is no longer announced.

## Alarms and clock

* Time picker values are now announced. This also affects the control used to select when to restart to finish installing Windows updates.

## Calendar and Mail

* NVDA no longer announces "read-only" for appointment subject in Calendar and message content in Mail.

## Calculator

* When ENTER is pressed, NVDA announces calculation results.

## Cortana

* Textual responses from Cortana are announced in most situations (if it doesn't, reopen Start menu and try searching again).
* NVDA will be silent when you talk to Cortana via voice.
* NVDA will now announce reminder confirmation after you set one.

## Mail and calendar

* NVDA no longer announces "edit" or "read-only" in message body and other fields.

## Maps

* NVDA plays location beep for map locations.

## Microsoft Edge

* Notifications such as file downloads are now announced.
* Note that overall support is experimental at this point (you should not use Edge as your primary browser for a while).

## Settings

* Certain information such as Windows Update progress is now reported automatically.
* Progress bar values and other information are no longer announced twice.

## Skype Preview

* Typing indicator text is announced just like Skype for Desktop client.
* Partial return of Control+NvDA+number row commands to read recent chat history and to move navigator object to chat entries just like Skype for Desktop.

## Store

* After checking for app updates, app names in list of apps to be updated are correctly labeled.

## TeamViewer Touch

* Labels for radio buttons are announced.
* Lables for buttons are announced.

## Bank of America/Twitter

* Button labels are now announced.

## Weather

* Tabs such as "forecast" and "maps" are recognized as proper tabs (patch by Derek Riemer).
* when reading a forecast, use the left and right arrows to move between items. Use the up and down arrows to read the individual items. For example, pressing the right arrow might report "Monday: 79 degrees, partly cloudy, ..." pressing the down arrow will say "Monday" Then pressing it again will read the next item (Like the temperature). This currently works for daily and hourly forecasts.

[1]: http://addons.nvda-project.org/files/get.php?file=w10

[2]: http://addons.nvda-project.org/files/get.php?file=w10-dev
