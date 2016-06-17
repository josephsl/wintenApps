# Windows 10 App Essentials

* Author: Joseph Lee
* Download [stable version][1]
* Download [development version][2]

This add-on is a collection of app modules for various Windows 10 apps, as well as fixes for certain windows 10 controls.

The following app modules or support modules for some apps are included (see each app section for details on what is included):

* Alarms and Clock.
* Bank of America
* Calculator (modern).
* Cortana
* Insider Hub/Feedback Hub (Windows Insiders only).
* Microsoft Edge
* Settings (system settings, Windows+I).
* Twitter.
* TeamViewer Touch.
* Miscellaneous modules for controls such as Start Menu tiles.

## General

* In context menus for Start Menu tiles, submenus are properly recognized.
* When minimizing windows (Windows+M), "pane" is no longer announced (noticeable if using Insider Preview builds).
* Certain dialogs are now recognized as proper dialogs. This include Insider Preview dialog (settings app) and new-style UAC dialog in build 14328 and later.
* Time picker announcement works in non-English locales.

## Alarms and clock

* Time picker values are now announced. This also affects the control used to select when to restart to finish installing Windows updates.

## Calculator

* When ENTER is pressed, NVDA announces calculation results.

## Cortana

* Textual responses from Cortana are announced in most situations (if it doesn't, reopen Start menu and try searching again).

## Insider/Feedback Hub and TeamViewer Touch

* Insider Hub (Feedback Hub in Anniversary Update) only: Meant to be used by Windows Insiders running an Insider build.
* Labels for radio buttons are announced.
* TeamViewer Touch: Lables for buttons are announced.

## Microsoft Edge

* Notifications such as file downloads are now announced.
* Note that overall support is experimental at this point (you should not use Edge as your primary browser for a while).

## Settings

* Certain information such as Windows Update progress is now reported automatically.
* Progress bar values are no longer announced twice.

## Bank of America/Twitter

* Button labels are now announced.

[1]: http://addons.nvda-project.org/files/get.php?file=w10

[2]: http://addons.nvda-project.org/files/get.php?file=w10-dev
