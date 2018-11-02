# Windows 10 App Essentials #

* Авторы: Joseph Lee, Derek Riemer и другие пользователи Windows 10
* Загрузить [стабильную версию][1]
* Загрузить [разрабатываемую версию][2]

Это дополнение представляет собой сборник модулей для различных приложений
Windows 10, а также исправлений для некоторых типов управления Windows 10.

Включены следующие модули поддержки или модули для некоторых приложений
(смотрите каждый раздел приложения для подробной информации):

* Action center
* Будильники и часы.
* Календарь
* Калькулятор (modern).
* Cortana
* Feedback Hub
* Game Bar
* Почта
* Карты
* Microsoft Edge
* Modern keyboard (emoji panel/hardware input suggestions/cloud clipboard
  items in Version 1709 and later)
* Люди
* Настройки (настройки системы, Windows+I)
* Skype (универсальное приложение)
* Магазин
* Погода.
* Разные модули для типов управления, таких, как плитки главного меню.

Notes:

* This add-on requires Windows 10 Version 1709 (build 16299) or later and
  NVDA 2018.3 or later. For best results, use the add-on with latest Windows
  10 stable release (build 17134) and latest stable version of NVDA. Note
  that until further notice, Version 1809 (build 17763) is not available
  from Microsoft.
* Some add-on features are or will be part of NVDA screen reader.
* For entries not listed below, you can assume that features are part of
  NVDA, no longer applicable as the add-on does not support old Windows 10
  releases, or changes were made to apps that makes entries no longer
  applicable.

For a list of changes made between each add-on releases, refer to
[changelogs for add-on releases][3] document.

## Общие

* If Add-on Updater add-on is installed, that add-on will check for Windows
  10 App Essentials updates.
* Default update check interval has changed to weekly checks for both stable
  and development releases. This is applicable if the add-on itself checks
  for updates.
* Submenu items are properly recognized in various apps, including context
  menu for Start menu tiles and microsoft Edge's app menu (Redstone 5).
* Certain dialogs are now recognized as proper dialogs and reported as such,
  including Insider Preview dialog (settings app). This is now part of NVDA
  2018.3.
* NVDA can announce suggestion count when performing a search in majority of
  cases. This option is controlled by "Report object position information"
  in Object presentation dialog/panel.
* In certain context menus (such as in Edge), position information (e.g. 1
  of 2) is no longer announced.
* The following UIA events are recognized: active text position change,
  controller for, drag start, drag cancel, drag complete, element selected,
  item status, live region change, notification, system alert, tooltip
  opened, window opened. With NVDA set to run with debug logging enabled,
  these events will be tracked, and for UIA notification event, a debug tone
  will be heard if notifications come from somewhere other than the
  currently active app.
* Notifications from newer app releases on Windows 10 Version 1709 (build
  16299) and later are announced. NVDA 2018.2 and later supports this, with
  2018.3 adding support for more notifications.
* Tooltips from Edge and universal apps are recognized and will be
  announced.
* When opening, closing, or switching between virtual desktops, NVDA will
  announce current desktop ID (desktop 2, for example).
* NVDA will no longer announce Start menu size text when changing screen
  resolutions or orientation.

## Action center

* Brightness quick action is now a button instead of a toggle button.
* Various status changes such as Focus Assist and Brightness will be
  reported.

## Будильники и часы

* Time picker values are now announced, noticeable when moving focus to
  picker controls. This also affects the control used to select when to
  restart to finish installing Windows updates.

## Калькулятор

* Когда нажмёте ENTER или Escape, NVDA сообщает результаты расчёта.
* For calculations such as unit converter and currency converter, NVDA will
  announce results as soon as calculations are entered.
* NVDA will no longer announce "heading level" for calculator results.

## календарь

* NVDA no longer announces "edit" or "read-only" in message body and other
  fields.

## Cortana

* Textual responses from Cortana are announced in most situations (if it
  doesn't, reopen Start menu and try searching again).
* NVDA will be silent when talking to Cortana via voice.
* NVDA will now announce reminder confirmation after you set one.

## Feedback Hub

* For newer app releases, NVDA will no longer announce feedback categories
  twice.

## Game Bar

* NVDA will announce appearance of Game Bar window. Due to technical
  limitations, NVDA cannot interact fully with Game Bar prior to build
  17723.

## Почта

* When reviewing items in messages list, you can now use table navigation
  commands to review message headers. Note that navigating between rows
  (messages) is not supported.
* When writing a message, appearance of at mention suggestions are indicated
  by sounds.

## Карты

* NVDA проигрывает сигнал расположения для положения на карте.
* When using street side view and if "use keyboard" option is enabled, NVDA
  will announce street addresses as you use arrow keys to navigate the map.

## Microsoft Edge

* Notifications such as file downloads and various webpage alerts, as well
  as availability of Reading View (if using Version 1709 and later) are
  announced.
* Text auto-complete will be tracked and announced in address omnibar.

## Modern keyboard

Note: most features below are now part of NVDA 2018.3.

* Support for Emoji input panel in Version 1709 (Fall Creators Update) and
  later, including the redesigned panel in Version 1809 (build 17661 and
  later) and changes made in 19H1 (build 18262). For best experience when
  reading emojis, use Windows OneCore speech synthesizer.
* Support for hardware keyboard input suggestions in Version 1803 (April
  2018 Update) and later.
* In post-1709 builds, NVDA will announce the first selected emoji when
  emoji panel opens. This is more noticeable in build 18262 and later where
  emoji panel may open to last browsed category, such as displaying skin
  tone modifier when opened to People category.
* Support for announcing cloud clipboard items in Version 1809 (build 17666
  and later).
* Reduced unnecessary verbosity when working with modern keyboard and its
  features. These include no longer announcing "Microsoft Candidate UI" when
  opening hardware keyboard input suggestions and staying silent when
  certain touch keyboard keys raise name change event on some systems.
* NVDA will no longer play error tones or do nothing when closing emoji
  panel in more recent Insider Preview builds.

## Люди

* When searching for contacts, first suggestion will be announced,
  particularly if using recent app releases.

## Настройки

* Certain information such as Windows Update progress is reported
  automatically, including Storage sense/disk cleanup widget.
* Значения индикатора выполнения и другая информация теперь не объявляются
  дважды.
* Группы настроек распознаются при использовании навигации объектов для
  перемещения между элементами управления.
* For some combo boxes and radio buttons, NVDA will no longer fail to
  recognize labels and/or announce value changes.
* Audio Volume progress bar beeps are no longer heard in Version 1803 and
  later.
* More messages about Windows Update status are announced, especially if
  Windows Update encounters errors.

## Skype

Note: the below entries won't work properly in Skype 14 universal app.

* Typing indicator text is announced just like Skype for Desktop client.
* Control+NvDA+number row commands, used to read recent chat history and to
  move navigator object to chat entries in Skype for Desktop, is also
  available in Skype UWP.
* You can press Alt+number row to locate and move to conversations (1),
  contacts list (2), bots (3) and chat edit field if visible (4). Note that
  these commands will work properly if Skype update released in March 2017
  is installed.
* NVDA will no longer announce "Skype Message" when reviewing messages for
  majority of cases.
* From message history list, pressing NVDA+D on a message item will allow
  NVDA to announce detailed information about a message such as channel
  type, sent date and time and so on.

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
