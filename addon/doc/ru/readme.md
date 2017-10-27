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
* Почта
* Карты
* Microsoft Edge
* Люди
* Настройки (настройки системы, Windows+I)
* Skype (универсальное приложение)
* Магазин
* Погода.
* Разные модули для типов управления, таких, как плитки главного меню.

Note: this add-on requires Windows 10 Version 1607 (build 14393) or later
and NVDA 2017.3 or later. For best results, use the add-on with latest
Windows 10 stable build (build 16299) and latest stable version of
NVDA. Also, after changing update settings for the add-on, be sure to save
NVDA settings.

Важное Примечание о NVDA 2017.3: из-за обратно несовместимых изменений в
NVDA 2017.3, дополнение версии 17.09 и младше не будет работать в версиях
NVDA старше 2017.3.

## Общие

* В контекстных меню для плиток главного меню, правильно распознаются
  подменю.
* Certain dialogs are now recognized as proper dialogs. These include
  Insider Preview dialog (settings app) and new-style UAC dialog in build
  14328 and later for NvDA 2016.2.1 or earlier.
* Appearance/close of suggestions for certain search fields (notably
  Settings and Store apps) is announced via sounds and braille. This also
  includes Start menu search box. This is now part of NVDA as of 2017.3.
* NVDA can announce suggestion count when performing a search in majority of
  cases. This option is controlled by "Report object position information"
  in Object presentation dialog.
* In certain context menus (such as in Edge), position information (e.g. 1
  of 2) is no longer announced.
* The following UIA events are recognized: Controller for, live region
  change, system alert, element selected, window opened. With NVDA set to
  run with debug logging enabled, these events will be tracked.
* Добавлена возможность  проверки обновления дополнения (автоматически или
  вручную) при помощи диалога Windows 10 App Essentials, который находится в
  меню параметров NVDA. По умолчанию, стабильная и разрабатываемая версии
  будут автоматически проверять наличие новых обновлений на еженедельной или
  ежедневной основе, соответственно.
* Ability to track events coming from Universal Windows Platform (UWP) apps
  if NVDA is run with debug logging enabled.
* Support for floating Emoji input panel in Version 1709 (Fall Creators
  Update). For best experience when reading emojis, use Windows OneCore
  speech synthesizer.
* In some apps, live region text is announced. This includes alerts in Edge,
  results in Calculator and others. Note that this may result in
  double-speaking in some cases. Most of the scenarios are now part of NVDA
  2017.3.
* Toasts are no longer announced multiple times in Creators Update and
  later. This fix is included in NVDA 2017.3.

## Будильники и часы

* Time picker values are now announced, noticeable when moving focus to
  picker controls. This also affects the control used to select when to
  restart to finish installing Windows updates.

## Калькулятор

* Когда нажмёте ENTER или Escape, NVDA сообщает результаты расчёта.
* For calculations such as unit converter and currency converter, NVDA will
  announce results as soon as calculations are entered.

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

## Почта

* При просмотре элементов в списке Сообщений, теперь вы можете использовать
  команды табличной навигации для просмотра заголовков Сообщений.
* When writing a message, appearance of at mention suggestions are indicated
  by sounds.

## Карты

* NVDA проигрывает сигнал расположения для положения на карте.
* When using street side view and if "use keyboard" option is enabled, NVDA
  will announce street addresses as you use arrow keys to navigate the map.

## Microsoft Edge

* Теперь объявляются уведомления, такие как загрузка файлов и различные
  предупреждения веб-страниц. Большинство этих сценариев сейчас входит в
  nvda 2017.3.

## Люди

* При поиске контактов, будет воспроизводиться звук при наличии результатов
  поиска.

## Настройки

* Теперь автоматически сообщается определённая информация, такая, как
  индикатор обновления Windows. Большинство случаев будет обрабатывать NVDA
  2017.3.
* Значения индикатора выполнения и другая информация теперь не объявляются
  дважды.
* If it takes a while to search for settings, NVDA will announce "searching"
  and search result status such as if a setting cannot be found. This is now
  done from NVDA in 2017.3.
* Группы настроек распознаются при использовании навигации объектов для
  перемещения между элементами управления.
* Для некоторых полей комбинированных списков, NVDA больше не будет
  оставлять нераспознанными метки и/или уведомления об изменении
  значения. Исправление изменения значения включено в NVDA 2017.3.

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
* Исправлены различные проблемы при использовании Skype с брайлем, в том
  числе невозможность просмотра элементов истории сообщений шрифтом брайля.
* From message history list, pressing NVDA+D on a message item will now
  allow NVDA to announce detailed information about a message such as
  channel type, sent date and time and so on.

## Магазин

* После проверки обновлений для приложений, обновлённые названия приложений
  в списке приложений будут правильно помечены.
* Объявляются Появление поисковых подсказок. Теперь это часть NVDA 2017.3.
* При загрузке содержимого, такого как приложения и фильмы, NVDA будет
  сообщать Наименование продукта и прогресс загрузки. Основа этого
  исправления теперь является частью NVDA 2017.3.

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
