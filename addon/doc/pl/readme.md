# Windows App Essentials #

* Autorzy: Joseph Lee, Derek Riemer i inni
* Pobierz [wersja stabilna][1]
* Pobierz [wersja beta][2]
* Pobierz [wersja rozwojowa][3]
* Zgodność z NVDA: 2023.3.4 i nowsze

Uwaga: Pierwotniea nazwa tego dodatku była Windows 10 App Essentials, a
potem została zmieniona na Windows App Essentials w 2021 roku, aby
obsługiwać Windows 10 i przyszłe wersje, takie jak Windows 11. Części tego
dodatku nadal będą odnosić się do oryginalnej nazwy dodatku.

Ten dodatek to zbiór modułów aplikacji dla różnych nowoczesnych aplikacji
systemu Windows, a także ulepszeń i poprawek dla niektórych kontrolek
znajdujących się w systemie Windows 10 i nowszych.

Dołączone są następujące moduły aplikacji lub moduły pomocy technicznej dla
niektórych aplikacji (szczegółowe informacje na temat tego, co jest
dołączone, zobacz każdą sekcję aplikacji):

* Klawiatura nowoczesna
* Ustawienia (ustawienia systemowe, Windows+I)

Notatki:

* Ten dodatek wymaga systemu Windows 10 22H2 (kompilacja 19045), 11 22H2
  (kompilacja 22621) lub nowszych wersji.
* Feature update support duration is tied to consumer support duration
  (Home, Pro, Pro Education, Pro for Workstations editions) and the add-on
  may end support for a feature update prior to end of consumer support. See
  <https://aka.ms/WindowsTargetVersioninfo> for more information and support
  dates.
* Chociaż instalacja jest możliwa, ten dodatek nie obsługuje wersji Windows
  Enterprise LTSC (Long-Term Servicing Channel) i Windows Server.
* Nie wszystkie funkcje kompilacji Windows Insider Preview będą obsługiwane,
  tym bardziej w przypadku funkcji wprowadzonych do podzbioru niejawnych
  testerów systemu Windows w kanałach kanarkowych i deweloperskich.
* The add-on may emulate changes included in Insider Preview builds which
  are subsequently removed, and for these changes, the add-on may remove
  them in future releases.
* Kanał deweloperski dodatków będzie zawierał zmiany, w tym zawartość
  eksperymentalną, która może, ale nie musi być zawarta w wersjach beta i
  stabilnych, a kanał beta będzie zawierał zmiany planowane dla przyszłych
  stabilnych wydań.
* Niektóre funkcje dodatkowe są lub będą częścią czytnika ekranu NVDA.
* Aby uzyskać najlepsze wrażenia z aplikacji, które osadzają technologie
  internetowe i zawartość, taką jak menu Start i jego menu kontekstowe,
  włącz ustawienie "Automatyczny tryb ustawiania ostrości dla zmian
  ostrości" w panelu ustawień trybu przeglądania NVDA.

Lista zmian wprowadzonych pomiędzy poszczególnymi wydaniami dodatków
znajduje się w dokumencie [changelogs for add-on releases][4].

## Klawiatura nowoczesna

Obejmuje to panel emoji, historię schowka, klawiaturę dotykową, dyktowanie /
pisanie głosowe, sugestie dotyczące wprowadzania sprzętu, sugerowane
działania i nowoczesne edytory metod wprowadzania dla niektórych języków w
systemach Windows 10 i 11. Aby wyświetlić emotikony, aby uzyskać najlepsze
wyniki, włącz ustawienie Unicode Consortium z ustawień mowy NVDA i ustaw
poziom symbolu na "niektóre" lub wyższe. Podczas wklejania z historii
schowka w systemie Windows 10 naciśnij spacji zamiast Enter, aby wkleić
wybrany element.

* In Windows 11, NVDA will announce suggested actions when compatible data
  such as phone numbers is copied to the clipboard. This is now part of NVDA
  2024.2.

## Ustawienia

* NVDA will report updates to Windows Update status as download and install
  progresses. This may result in speech interruption when navigating
  Settings app while updates are being downloaded and installed. If using
  Windows 11 and UIA event registration is set to selective from NVDA
  advanced settings panel, you must move focus to updates list as soon as
  they appear so NVDA can announce update progress.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps

[2]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-dev

[4]: https://github.com/josephsl/wintenapps/wiki/w10changelog
