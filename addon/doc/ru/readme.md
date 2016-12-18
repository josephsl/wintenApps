# Windows 10 App Essentials #

* Авторы: Joseph Lee, Derek Riemer и другие пользователи Windows 10
* Загрузить [стабильную версию][1]
* Загрузить [разрабатываемую версию][2]

Это дополнение представляет собой сборник модулей для различных приложений
Windows 10, а также исправлений для некоторых типов управления Windows 10.

Включены следующие модули поддержки или модули для некоторых приложений
(смотрите каждый раздел приложения для подробной информации):

* Будильники и часы.
* Bank of America
* Календарь
* Калькулятор (modern).
* Cortana
* Groove Music
* Почта
* Карты
* Microsoft Edge
* Настройки (настройки системы, Windows+I).
* Skype Preview
* Store
* Twitter.
* Сенсорный экран TeamViewer.
* Погода.
* Разные модули для типов управления, таких, как плитки главного меню.

Note: this add-on requires Windows 10 Version 1511 (build 10586) or later
and NVDA 2016.3 or later. For best results, use the add-on with latest
stable build (build 14393).

## Общие

* В контекстных меню для плиток главного меню, правильно распознаются
  подменю.
* When minimizing windows (Windows+M), "pane" is no longer announced
  (noticeable if using Insider Preview builds).
* Certain dialogs are now recognized as proper dialogs. This include Insider
  Preview dialog (settings app) and new-style UAC dialog in build 14328 and
  later for NvDA 2016.2.1 or earlier.
* Appearance/close of suggestions for certain search fields (notably
  Settings app) is announced via sounds and/or brailled.
* In certain context menus (such as in Edge), position information (e.g. 1
  of 2) is no longer announced.
* The following UIA events are recognized: Controller for, live region
  changed (handled by name change event).

## Будильники и часы

* Time picker values are now announced. This also affects the control used
  to select when to restart to finish installing Windows updates.

## Календарь и Почта

* NVDA no longer announces "read-only" for appointment subject in Calendar
  and message content in Mail.

## Калькулятор

* Когда нажимаете ENTER, NVDA сообщает результаты расчёта.

## Cortana

* Textual responses from Cortana are announced in most situations (if it
  doesn't, reopen Start menu and try searching again).
* NVDA will be silent when you talk to Cortana via voice.
* NVDA will now announce reminder confirmation after you set one.

## Groove Music

* Appearance of suggestions when searching for tracks is now detected.

## Mail and calendar

* NVDA no longer announces "edit" or "read-only" in message body and other
  fields.

## Карты

* NVDA plays location beep for map locations.

## Microsoft Edge

* Теперь объявляются уведомления, такие как загрузка файлов.
* Отметим, что на данный момент поддержка экспериментальна (Вы не должны
  использовать EDGE в качестве браузера по умолчанию ещё некоторое время).

## Настройки

* Теперь автоматически сообщается определённая информация, такая, как
  индикатор обновления Windows.
* Значения индикатора выполнения и другая информация теперь не объявляются
  дважды.
* If it takes a while to search for settings, NVDA will announce "searching"
  and search result status such as if a setting cannot be found.

## Skype Preview

* Typing indicator text is announced just like Skype for Desktop client.
* Partial return of Control+NvDA+number row commands to read recent chat
  history and to move navigator object to chat entries just like Skype for
  Desktop.
* You can now press Alt+number row to locate and move to contacts list (1),
  conversations (2) and chat edit field (3). Note that one must activate
  these tabs to move to the desired part.
* Combo box labels for Skype preview app released in November 2016 are
  announced.

## Store

* After checking for app updates, app names in list of apps to be updated
  are correctly labeled.

## TeamViewer Touch

* Метки радиокнопок теперь объявляются.
* Lables for buttons are announced.

## Bank of America/Twitter

* Теперь объявляются метки кнопок.

## Погода

* Tabs such as "forecast" and "maps" are recognized as proper tabs (patch by
  Derek Riemer).
* when reading a forecast, use the left and right arrows to move between
  items. Use the up and down arrows to read the individual items. For
  example, pressing the right arrow might report "Monday: 79 degrees, partly
  cloudy, ..." pressing the down arrow will say "Monday" Then pressing it
  again will read the next item (Like the temperature). This currently works
  for daily and hourly forecasts.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=w10

[2]: http://addons.nvda-project.org/files/get.php?file=w10-dev
