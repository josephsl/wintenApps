# Windows App Essentials #

* Авторы: Joseph Lee, Derek Riemer и другие

Примечание: Первоначально дополнение называлось Windows 10 App Essentials,
но в 2021 году было переименовано в Windows App Essentials для поддержки
Windows 10 и будущих версий, таких как Windows 11. Некоторые части этого
дополнения по-прежнему будут содержать оригинальное название.

Это дополнение представляет собой сборник модулей для различных приложений
Windows, а также улучшения и исправления для некоторых элементов управления,
найденных в Windows 10 и более поздних версиях.

Включены следующие модули поддержки или модули для некоторых приложений
(смотрите каждый раздел приложения для подробной информации):

* Настройки системы (Windows+I)

Примечания:

* Для этого дополнения требуется 64-разрядная версия Windows 10 22H2 (сборка
  19045), 11 22H2 (сборка 22621) или более поздние версии.
* Feature update support duration is tied to consumer support duration
  (Home, Pro, Pro Education, Pro for Workstations editions) and the add-on
  may end support for a feature update prior to end of consumer support. See
  <https://aka.ms/WindowsTargetVersioninfo> for more information and support
  dates.
* Although installation is possible, this add-on does not support Windows
  Enterprise LTSC (Long-Term Servicing Channel) and Windows Server releases.
* Not all features from Windows Insider Preview builds will be supported,
  more so for features introduced to a subset of Windows Insiders in canary
  and dev channels.
* Add-on dev channel will include changes including experimental content
  that may or may not be included in beta and stable releases, and beta
  channel will come with changes planned for future stable releases.
* Некоторые функции дополнения являются или будут частью программы NVDA.

Список изменений, внесённых между выпусками каждого дополнения, приведён в
документе [списки изменений для выпусков дополнения][1].

## Общие

* В Windows 11 24H2 для быстрой настройки элементов интерфейса
  (shellhost.exe) можно управлять с помощью мыши и/или касания. Теперь это
  часть NVDA 2024.2.
* В Windows 11 NVDA сообщит о предлагаемых действиях при копировании
  совместимых данных, таких как номера телефонов, в буфер обмена. Теперь это
  часть NVDA 2024.2.

## Настройки системы (Windows+I)

* NVDA будет сообщать о состоянии обновлений в центре обновлений Windows по
  мере их загрузки и установки. В Windows 10 это может привести к прерыванию
  речи при навигации по приложению "Параметры" во время загрузки и установки
  обновлений. В Windows 11 навигация по объектам может использоваться в
  списке обновлений для просмотра статуса обновления отдельных записей.

[[!tag dev stable]]

[1]: https://github.com/josephsl/wintenapps/wiki/w10changelog
