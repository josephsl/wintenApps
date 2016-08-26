# Windows 10 App Essentials #

* Автор: Joseph Lee
* Загрузить [стабильную версию][1]
* Загрузить [разрабатываемую версию][2]

Это дополнение представляет собой сборник модулей для различных приложений
Windows 10, а также исправлений для некоторых типов управления Windows 10.

Включены следующие модули поддержки или модули для некоторых приложений
(смотрите каждый раздел приложения для подробной информации):

* Будильники и часы.
* Bank of America
* Калькулятор (modern).
* Cortana
* Insider Hub/Feedback Hub (Windows Insiders only).
* Microsoft Edge
* Настройки (настройки системы, Windows+I).
* Skype Preview
* Twitter.
* Сенсорный экран TeamViewer.
* Разные модули для типов управления, таких, как плитки главного меню.

## Общие

* В контекстных меню для плиток главного меню, правильно распознаются
  подменю.
* When minimizing windows (Windows+M), "pane" is no longer announced
  (noticeable if using Insider Preview builds).
* Certain dialogs are now recognized as proper dialogs. This include Insider
  Preview dialog (settings app) and new-style UAC dialog in build 14328 and
  later.
* Time picker announcement works in non-English locales.

## Будильники и часы

* Time picker values are now announced. This also affects the control used
  to select when to restart to finish installing Windows updates.

## Калькулятор

* Когда нажимаете ENTER, NVDA сообщает результаты расчёта.

## Cortana

* Textual responses from Cortana are announced in most situations (if it
  doesn't, reopen Start menu and try searching again).

## Insider/Feedback Hub and TeamViewer Touch

* Insider Hub (Feedback Hub in Anniversary Update) only: Meant to be used by
  Windows Insiders running an Insider build.
* Метки радиокнопок теперь объявляются.
* Сенсорный экран TeamViewer: Теперь объявляются метки кнопок.

## Microsoft Edge

* Теперь объявляются уведомления, такие как загрузка файлов.
* Отметим, что на данный момент поддержка экспериментальна (Вы не должны
  использовать EDGE в качестве браузера по умолчанию ещё некоторое время).

## Настройки

* Теперь автоматически сообщается определённая информация, такая, как
  индикатор обновления Windows.
* Значения индикатора выполнения и другая информация теперь не объявляются
  дважды.

## Skype Preview

* Typing indicator text is announced just like Skype for Desktop client.
* Partial return of Control+NvDA+number row commands to read recent chat
  history.

## Bank of America/Twitter

* Теперь объявляются метки кнопок.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=w10

[2]: http://addons.nvda-project.org/files/get.php?file=w10-dev
