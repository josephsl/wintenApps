# Windows 10 App Essentials #

* Авторы: Joseph Lee, Derek Riemer и другие пользователи Windows 10
* Загрузить [стабильную версию][1]
* Загрузить [разрабатываемую версию][2]
* NVDA compatibility: 2019.1 to 2019.2

Это дополнение представляет собой сборник модулей для различных приложений
Windows 10, а также исправлений для некоторых типов управления Windows 10.

Включены следующие модули поддержки или модули для некоторых приложений
(смотрите каждый раздел приложения для подробной информации):

* Калькулятор (modern).
* Календарь
* Cortana
* Feedback Hub
* Почта
* Карты
* Microsoft Edge
* Modern keyboard (emoji panel/dictation/hardware input suggestions/cloud
  clipboard items in Version 1709 and later)
* Люди
* Настройки (настройки системы, Windows+I)
* Магазин
* Погода.
* Разные модули для типов управления, таких, как плитки главного меню.

Notes:

* This add-on requires Windows 10 Version 1809 (build 17763) or later and
  NVDA 2019.1 or later. For best results, use the add-on with latest Windows
  10 stable release (build 18362) and latest stable version of NVDA.
* Some add-on features are or will be part of NVDA screen reader.
* For entries not listed below, you can assume that features are part of
  NVDA, no longer applicable as the add-on does not support old Windows 10
  releases, or changes were made to Windows 10 and apps that makes entries
  no longer applicable.

For a list of changes made between each add-on releases, refer to
[changelogs for add-on releases][3] document.

## Общие

* NVDA will no longer play error tones or do nothing if this add-on becomes
  active from Windows 7, Windows 8.1, and unsupported releases of Windows
  10.
* Submenu items are properly recognized in various apps, including context
  menu for Start menu tiles and microsoft Edge's app menu (Redstone 5).
* In addition to dialogs recognized by NVDA, more dialogs are now recognized
  as proper dialogs and reported as such, including Insider Preview dialog
  (settings app).
* NVDA can announce suggestion count when performing a search in majority of
  cases. This option is controlled by "Report object position information"
  in Object presentation panel found in NVDA settings.
* In certain context menus (such as in Edge), position information (e.g. 1
  of 2) is no longer announced.
* The following UIA events are recognized: controller for, drag start, drag
  cancel, drag complete, element selected, item status, live region change,
  notification, system alert, text change, tooltip opened, window
  opened. With NVDA set to run with debug logging enabled, these events will
  be tracked, and for UIA notification event, a debug tone will be heard if
  notifications come from somewhere other than the currently active app.
* It is possible to tracke only specific events and/or events coming from
  specific apps.
* Tooltips from Edge and universal apps are recognized and will be
  announced. This will be part of NVDA 2019.3.
* When opening, closing, or switching between virtual desktops, NVDA will
  announce current desktop name (desktop 2, for example).
* NVDA will no longer announce Start menu size text when changing screen
  resolutions or orientation.
* In Version 1903 (May 2019 Update), NVDA will announce volume and
  brightness changes immediately if focused on File Explorer. This is now
  part of NVDA 2019.2.

## Калькулятор

* Когда нажмёте ENTER или Escape, NVDA сообщает результаты расчёта.
* For calculations such as unit converter and currency converter, NVDA will
  announce results as soon as calculations are entered.
* NVDA will no longer announce "heading level" for calculator results.
* NVDA will notify if maximum digit count has been reached while entering
  expressions.

## календарь

* NVDA no longer announces "edit" or "read-only" in message body and other
  fields.

## Cortana

* Textual responses from Cortana are announced in most situations (if it
  doesn't, reopen Start menu and try searching again).
* NVDA will be silent when talking to Cortana via voice.
* NVDA will now announce reminder confirmation after you set one.
* In build 18945 and later, modern search experience in File Explorer
  powered by Cortana user interface is supported.

## Feedback Hub

* For newer app releases, NVDA will no longer announce feedback categories
  twice.

## Почта

* When reviewing items in messages list, you can now use table navigation
  commands to review message headers. Note that navigating between rows
  (messages) is not supported.
* When writing a message, appearance of at mention suggestions are indicated
  by sounds.
* NVDA will no longer do anything or play error tones after closing this
  app. This is now part of NVDA 2019.2.

## Карты

* NVDA проигрывает сигнал расположения для положения на карте.
* When using street side view and if "use keyboard" option is enabled, NVDA
  will announce street addresses as you use arrow keys to navigate the map.

## Microsoft Edge

* Text auto-complete will be tracked and announced in address omnibar.
* NVDA will no longer play suggestion sound when pressing F11 to toggle full
  screen.

## Modern keyboard

Note: most features below are now part of NVDA 2018.3 or later.

* Support for Emoji input panel in Version 1709 (Fall Creators Update) and
  later, including the redesigned panel in Version 1809 (build 17661 and
  later) and changes made in 19H1 (build 18262 and later, including kaomoji
  and symbols categories in build 18305). If using NVDA releases earlier
  than 2018.4, for best experience when reading emojis, use Windows OneCore
  speech synthesizer. If 2018.4 or later is in use, enable Unicode
  Consortium setting from NvDA's speech settings and set symbol level to
  "some" or higher.
* NVDA will no longer announce "clipboard" when there are items in the
  clipboard under some circumstances.
* On some systems running Version 1903 (May 2019 Update), NVDA will no
  longer appear to do nothing when emoji panel opens.

## Люди

* When searching for contacts, first suggestion will be announced,
  particularly if using recent app releases.

## Настройки

* Certain information such as Windows Update progress is reported
  automatically, including Storage sense/disk cleanup widget and errors from
  Windows Update.
* Значения индикатора выполнения и другая информация теперь не объявляются
  дважды.
* For some combo boxes and radio buttons, NVDA will no longer fail to
  recognize labels and/or announce value changes.
* Audio Volume progress bar beeps are no longer heard in Version 1803 and
  later.
* NVDA will no longer appear to do nothing or play error tones if using
  object navigation commands under some circumstances.
* Windows Update reminder dialog is recognized as a proper dialog.
* Odd control labels seen in certain Windows 10 installations has been
  corrected.
* In more recent revisions of Version 1803 and later, due to changes to
  Windows Update procedure for feature updates, a "download and install now"
  link has been added. NVDA will now announce the title for the new update
  if present.

## Магазин

* После проверки обновлений для приложений, обновлённые названия приложений
  в списке приложений будут правильно помечены.
* При загрузке содержимого, такого как приложения и фильмы, NVDA будет
  сообщать Наименование продукта и прогресс загрузки.

## Погода

* Вкладки, такие как "прогноз" и "карты" расспознаются надлежащим образом
  (патч Derek Riemer).
* when reading a forecast, use the left and right arrows to move between
  items. Use the up and down arrows to read the individual items. For
  example, pressing the right arrow might report "Monday: 79 degrees, partly
  cloudy, ..." pressing the down arrow will say "Monday" Then pressing it
  again will read the next item (Like the temperature). This currently works
  for daily and hourly forecasts.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
