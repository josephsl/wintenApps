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

* Сучасна клавіатура
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
* Додаток може імітувати виправлення, включені до збірок Insider Preview,
  які згодом видаляються, і для цих змін додаток може видаляти їх у
  майбутніх випусках.
* Канал розробників доповнень міститиме зміни, включаючи експериментальний
  контент, який може бути включений або не включений до бета- та стабільних
  випусків, а канал бета-версій міститиме зміни, заплановані для майбутніх
  стабільних випусків.
* Деякі функції додатка є або будуть частиною NVDA.
* Для найкращого досвіду роботи з програмами, які включають веб-технології
  та вміст, наприклад меню «Пуск» і його контекстне меню, увімкніть параметр
  «Автоматичний перехід в режим фокуса при зміні фокуса» у розділі "Режим
  огляду" налаштувань NVDA.

Перелік змін, внесених між випусками додатка, наведено у документі [журнал
змін випусків додатка][1].

## Загальне

* In Windows 11 24H2 Insider Preview builds, quick settings (shellhost.exe)
  interface elements can be navigated using mouse and/or touch interaction.

## Сучасна клавіатура

Це включає панель емодзі, історію буфера обміну, сенсорну клавіатуру,
диктування/голосовий ввід, пропозиції при апаратному введенні, пропоновані
дії та сучасні редактори методів введення для певних мов у Windows 10 і
11. Для найкращого перегляду емодзі увімкніть опцію «Включити дані
Консорціуму Юнікоду (включно з емодзі) при обробці знаків та символів» у
розділі «Мовлення» налаштувань NVDA і встановіть рівень символів і знаків
пунктуації на «деякі» або вище. Під час вставлення з історії буфера обміну в
Windows 10 натисніть клавішу пробілу замість клавіші Enter, щоб вставити
вибраний елемент.

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
