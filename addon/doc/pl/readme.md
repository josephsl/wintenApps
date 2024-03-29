# Windows App Essentials #

* Autorzy: Joseph Lee, Derek Riemer i inni

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
* Ustawienia (Windows+I)

Notatki:

* This add-on requires 64-bit Windows 10 22H2 (build 19045), 11 22H2 (build
  22621), or later releases.
* Czas trwania pomocy technicznej dotyczącej aktualizacji funkcji jest
  powiązany z czasem trwania pomocy technicznej dla klientów (wersje Home,
  Pro, Pro Education, Pro dla stacji roboczych), a dodatek może zakończyć
  świadczenie pomocy technicznej dla aktualizacji funkcji przed zakończeniem
  świadczenia pomocy technicznej dla klientów indywidualnych. Zobacz
  <https://aka.ms/WindowsTargetVersioninfo>, aby uzyskać więcej informacji i
  daty pomocy technicznej.
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
znajduje się w dokumencie [changelogs for add-on releases][1].

## Ogólne

* In Windows 11 24H2 Insider Preview builds, quick settings (shellhost.exe)
  interface elements can be navigated using mouse and/or touch interaction.

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

## Ustawienia (Windows+I)

* NVDA will report updates to Windows Update status as download and install
  progresses. In Windows 10, this may result in speech interruption when
  navigating Settings app while updates are being downloaded and
  installed. In Windows 11, object navigation can be used in updates list to
  review update status for individual entries.

[[!tag dev stable]]

[1]: https://github.com/josephsl/wintenapps/wiki/w10changelog
