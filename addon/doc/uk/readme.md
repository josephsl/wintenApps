# Windows App Essentials (Поліпшення для застосунків Windows) #

* Автори: Joseph Lee, Derek Riemer та інші
* Завантажити [стабільну версію][1]
* Завантажити [бета версію][2]
* Завантажити [версію в розробці][3]
* Сумісність з NVDA: 2023.1 і новіші

Примітка: спочатку додаток називався Windows 10 App Essentials, у 2021 році
його було перейменовано на Windows App Essentials для підтримки Windows 10 і
майбутніх випусків, таких як Windows 11. Частини цього додатка все ще
посилатимуться на оригінальну назву додатка.

Цей додаток є набором модулів програм для різноманітних сучасних програм
Windows, а також удосконаленням та виправленням певних елементів керування,
доступних у Windows 10 і вище.

Включено наведені нижче модулі додатків або модулі підтримки для деяких
додатків (перегляньте розділ кожного додатка, щоб дізнатися, що включено):

* Cortana
* Сучасна клавіатура (панель емодзі/сенсорна клавіатура/диктування/голосове
  введення/пропозиції введення з апаратної клавіатури/історія буфера
  обміну/пропоновані дії/сучасні редактори методів вводу)
* Настройки (параметри системи, Windows+I)
* Голосовий доступ (Windows 11 22H2)
* Погода
* Різноманітні модулі для елементів керування й функцій, таких як оголошення
  віртуальних робочих столів

Примітки:

* Для цього додатка потрібна Windows 10 22H2 (збірка 19045), 11 21H2 (збірка
  22000) або вище.
* Тривалість підтримки оновлень функцій прив'язана до тривалості підтримки
  користувачів (версії Home, Pro, Pro Education, Pro для робочих станцій), і
  додаток може припинити підтримку оновлення функцій до закінчення підтримки
  користувачів. Додаткову інформацію й дати підтримки див. на
  aka.ms/WindowsTargetVersioninfo.
* Цей додаток не підтримує версії Windows Enterprise LTSC (Long-Term
  Servicing Channel) і Windows Server, Хоча встановлення на ці версії
  можливе.
* Якщо встановлено Оновлювач додатків та увімкнено фонове оновлення
  додатків, Windows App Essentials взагалі не встановлюватиметься у версіях
  Windows, які не підтримуються.
* Не всі функції зі збірок Windows Insider Preview підтримуватимуться,
  особливо функції, представлені для підгруп Windows Insiders у каналах
  canary і dev.
* The add-on may emulate fixes included in Insider Preview builds which are
  subsequently removed, and for these changes, the add-on may remove them in
  future releases.
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
змін випусків додатка][4].

## Загальне

* При відкритті, закритті або перемиканні між віртуальними робочими столами
  NVDA називатиме ім'я активного віртуального робочого столу (наприклад,
  робочий стіл 2). Тепер це є частиною NVDA 2023.2.
* Improved Windows 10 and 11 taskbar experience, including announcing
  results of rearranging icons when pressing Alt+Shift+left/right arrow keys
  (Windows 11) and reporting item position when moving through taskbar icons
  (Windows 10 and 11). Note that these are emulated workarounds for features
  introduced and then subsequently removed in Insider Preview builds and may
  be removed from the add-on in the future.
* In aps such as Windows 11 22H2 File Explorer and Notepad where tabbed
  windows are supported, NVDA will announce the name and the position of
  tabs when switching between them. This is now part of NVDA 2023.2.

## Cortana

* Текстові відповіді від Cortana оголошуються в більшості випадків.

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

* У Windows 11 22H2 і пізніших версіях NVDA оголошуватиме запропоновані дії,
  коли сумісні дані, такі як телефонні номери, копіюватимуться до буфера
  обміну.

## Настройки

* NVDA оголосить назву додаткового контролю якості оновлення, якщо він буде
  присутній (посилання «Завантажити та встановити зараз» у Windows 10,
  кнопка «Завантажити» у Windows 11).
* У Windows 11 елементи панелі навігації розпізнаються належним чином.
* NVDA will report updates to Windows Update status as download and install
  progresses. This may result in speech interruption when navigating
  Settings app while updates are being downloaded and installed. If using
  Windows 11 and UIA event registration is set to selective from NVDA
  advanced settings panel, you must move focus to updates list as soon as
  they appear so NVDA can announce update progress.

## Голосовий доступ

Це стосується функції голосового доступу, що представлена в Windows 11 22H2.

* NVDA сповістить про стан мікрофона під час перемикання мікрофона з
  інтерфейсу голосового доступу.

## Погода

* Такі вкладки, як «погода» і «карти», розпізнаються як правильні вкладки
  (патч від Дерека Рімера).

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps

[2]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-dev

[4]: https://github.com/josephsl/wintenapps/wiki/w10changelog
