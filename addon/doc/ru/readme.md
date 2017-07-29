# Windows 10 App Essentials #

* Авторы: Joseph Lee, Derek Riemer и другие пользователи Windows 10
* Загрузить [стабильную версию][1]
* Загрузить [разрабатываемую версию][2]

Это дополнение представляет собой сборник модулей для различных приложений
Windows 10, а также исправлений для некоторых типов управления Windows 10.

Включены следующие модули поддержки или модули для некоторых приложений
(смотрите каждый раздел приложения для подробной информации):

* Будильники и часы.
* Календарь
* Калькулятор (modern).
* Cortana
* Game Bar
* Музыка Groove
* Почта
* Карты
* Microsoft Edge
* Люди
* Настройки (настройки системы, Windows+I)
* Skype (universal app)
* Магазин
* Погода.
* Разные модули для типов управления, таких, как плитки главного меню.

Примечание: Это дополнение требует Windows 10 Версии 1607 (сборки 14393) или
позднее и NVDA 2017.1 или позднее. Для наилучших результатов используйте
дополнение с последней стабильной сборкой (сборка 15063) и последней
стабильной версией NVDA. Кроме того, после изменения настроек обновления для
дополнения, обязательно сохраните настройки программы NVDA.

## Общие

* В контекстных меню для плиток главного меню, правильно распознаются
  подменю.
* Certain dialogs are now recognized as proper dialogs. This include Insider
  Preview dialog (settings app) and new-style UAC dialog in build 14328 and
  later for NvDA 2016.2.1 or earlier.
* Appearance/close of suggestions for certain search fields (notably
  Settings and Store apps) is announced via sounds and braille. This also
  includes Start menu search box.
* NVDA can announce suggestion count when performing a search in majority of
  cases. This option is controlled by "Report object position information"
  in Object presentation dialog.
* In certain context menus (such as in Edge), position information (e.g. 1
  of 2) is no longer announced.
* The following UIA events are recognized: Controller for, live region
  change, system alert, element selected, window opened.
* Added ability to check for add-on updates (automatic or manual) via the
  new Windows 10 App Essentials dialog found in NvDA Preferences menu. By
  default, stable and development versions will check for new updates
  automatically on a weekly or daily basis, respectively.
* Ability to track events coming from Universal Windows Platform (UWP) apps
  if NVDA is run with debug logging enabled.
* Initial support for floating Emoji input panel in build 16215 or later
  (for best experience when reading emojis, use Windows OneCore speech
  synthesizer).
* In some apps, live region text is announced. This includes alerts in Edge
  and others. Note that this may result in double-speaking in some cases.
* Toasts are no longer announced multiple times in Creators Update and
  later.

## Будильники и часы

* Time picker values are now announced, noticeable when moving focus to
  picker controls. This also affects the control used to select when to
  restart to finish installing Windows updates.

## Калькулятор

* Когда нажмёте ENTER или Escape, NVDA сообщает результаты расчёта.

## календарь

* NVDA no longer announces "edit" or "read-only" in message body and other
  fields.

## Cortana

* Textual responses from Cortana are announced in most situations (if it
  doesn't, reopen Start menu and try searching again).
* NVDA will be silent when you talk to Cortana via voice.
* NVDA will now announce reminder confirmation after you set one.

## Game Bar

* NVDA will announce appearance of Game Bar window. Due to technical
  limitations, NVDA cannot interact fully with Game Bar.

## Музыка Groove

* Appearance of suggestions when searching for tracks is now detected.

## Почта

* When reviewing items in messages list, you can now use table navigation
  commands to review message headers.
* When writing a message, appearance of at mention suggestions are indicated
  by sounds.

## Карты

* NVDA plays location beep for map locations.
* When using street side view and if "use keyboard" option is enabled, NVDA
  will announce street addresses as you use arrow keys to navigate the map.

## Microsoft Edge

* Теперь объявляются уведомления, такие как загрузка файлов и различные
  предупреждения веб-страниц.
* In Creators Update, NVDA will no longer announce "WebRuntime Content View"
  when going to another site.

## Люди

* When searching for contacts, a sound will play if there are search
  results.

## Настройки

* Теперь автоматически сообщается определённая информация, такая, как
  индикатор обновления Windows.
* Значения индикатора выполнения и другая информация теперь не объявляются
  дважды.
* If it takes a while to search for settings, NVDA will announce "searching"
  and search result status such as if a setting cannot be found.
* Settings groups are recognized when using object navigation to navigate
  between controls.
* For some combo boxes, NVDA will no longer fail to recognize labels and/or
  announce value changes.

## Skype

* Typing indicator text is announced just like Skype for Desktop client.
* Partial return of Control+NvDA+number row commands to read recent chat
  history and to move navigator object to chat entries just like Skype for
  Desktop.
* You can now press Alt+number row to locate and move to conversations (1),
  contacts list (2), bots (3) and chat edit field if visible (4). Note that
  these commands will work properly if Skype update released in March 2017
  is installed.
* Combo box labels for Skype preview app released in November 2016 are
  announced.
* NVDA will no longer announce "Skype Message" when reviewing messages for
  majority of cases.
* Various issues when using Skype with braille displays fixed, including
  inability to review message history items in braille.
* From message history list, pressing NVDA+D on a message item will now
  allow NVDA to announce detailed information about a message such as
  channel type, sent date and time and so on.

## Магазин

* После проверки обновлений для приложений, обновлённые названия приложений
  в списке приложений будут правильно помечены.
* Объявляются Появление поисковых подсказок.
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
