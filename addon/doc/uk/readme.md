# Windows App Essentials (Поліпшення для застосунків Windows) #

* Автори: Joseph Lee, Derek Riemer та інші

Примітка: спочатку додаток називався Windows 10 App Essentials, у 2021 році
його було перейменовано на Windows App Essentials для підтримки Windows 10 і
майбутніх випусків, таких як Windows 11. Частини цього додатка все ще
посилатимуться на оригінальну назву додатка.

Цей додаток є набором модулів програм для різноманітних сучасних програм
Windows, а також удосконаленням та виправленням певних елементів керування,
доступних у Windows 10 і вище.

Включено наведені нижче модулі додатків або модулі підтримки для деяких
додатків (перегляньте розділ кожного додатка, щоб дізнатися, що включено):

* Settings (Windows+I)

Примітки:

* This add-on requires 64-bit Windows 10 22H2 (build 19045), 11 22H2 (build
  22621), or later releases.
* Тривалість підтримки оновлень функцій прив'язана до тривалості підтримки
  користувачів (версії Home, Pro, Pro Education, Pro для робочих станцій), і
  додаток може припинити підтримку оновлення функцій до закінчення підтримки
  користувачів. Додаткову інформацію й дати підтримки див. на
  <https://aka.ms/WindowsTargetVersioninfo>.
* Цей додаток не підтримує версії Windows Enterprise LTSC (Long-Term
  Servicing Channel) і Windows Server, Хоча встановлення на ці версії
  можливе.
* Не всі функції зі збірок Windows Insider Preview підтримуватимуться,
  особливо функції, представлені для підгруп Windows Insiders у каналах
  canary і dev.

Перелік змін, внесених між випусками додатка, наведено у документі [журнал
змін випусків додатка][1].

## Загальне

* In Windows 11 24H2, quick settings (shellhost.exe) interface elements can
  be navigated using mouse and/or touch interaction. This is now part of
  NVDA 2024.2.
* In Windows 11, NVDA will announce suggested actions when compatible data
  such as phone numbers is copied to the clipboard. This is now part of NVDA
  2024.2.

## Settings (Windows+I)

* NVDA will report updates to Windows Update status as download and install
  progresses. In Windows 10, this may result in speech interruption when
  navigating Settings app while updates are being downloaded and
  installed. In Windows 11, object navigation can be used in updates list to
  review update status for individual entries.

[[!tag dev stable]]

[1]: https://github.com/josephsl/wintenapps/wiki/w10changelog
