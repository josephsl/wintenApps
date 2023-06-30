# Windows App Essentials #

* Autorzy: Joseph Lee, Derek Riemer i inni
* Pobierz [wersja stabilna][1]
* Pobierz [wersja beta][2]
* Pobierz [wersja rozwojowa][3]
* Zgodność z NVDA: 2023.1 i nowsze

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

* Cortana
* Nowoczesna klawiatura (panel emoji/klawiatura dotykowa/dyktowanie/pisanie
  głosowe/sugestie dotyczące wprowadzania sprzętu/historia
  schowka/sugerowane akcje/nowoczesne edytory metod wprowadzania)
* Ustawienia (ustawienia systemowe, Windows+I)
* Dostęp głosowy (Windows 11 22H2)
* Różne moduły sterowania i funkcji, takich jak ogłoszenia wirtualnych
  pulpitów

Notatki:

* Ten dodatek wymaga systemu Windows 10 22H2 (kompilacja 19045), 11 21H2
  (kompilacja 22000) lub nowszych wersji.
* Czas trwania pomocy technicznej dotyczącej aktualizacji funkcji jest
  powiązany z czasem trwania pomocy technicznej dla klientów (wersje Home,
  Pro, Pro Education, Pro dla stacji roboczych), a dodatek może zakończyć
  świadczenie pomocy technicznej dla aktualizacji funkcji przed zakończeniem
  świadczenia pomocy technicznej dla klientów indywidualnych. Zobacz
  aka.ms/WindowsTargetVersioninfo, aby uzyskać więcej informacji i daty
  pomocy technicznej.
* Chociaż instalacja jest możliwa, ten dodatek nie obsługuje wersji Windows
  Enterprise LTSC (Long-Term Servicing Channel) i Windows Server.
* Jeśli jest zainstalowany program Add-on Updater i włączone są aktualizacje
  dodatków w tle, program Windows App Essentials nie zostanie w ogóle
  zainstalowany w nieobsługiwanych wersjach systemu Windows.
* Nie wszystkie funkcje kompilacji Windows Insider Preview będą obsługiwane,
  tym bardziej w przypadku funkcji wprowadzonych do podzbioru niejawnych
  testerów systemu Windows w kanałach kanarkowych i deweloperskich.
* The add-on may emulate fixes included in Insider Preview builds which are
  subsequently removed, and for these changes, the add-on may remove them in
  future releases.
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

## Ogólne

* When opening, closing, or switching between virtual desktops, NVDA will
  announce active virtual desktop name (desktop 2, for example). This is now
  part of NVDA 2023.2.
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

* Odpowiedzi tekstowe z Cortany są ogłaszane w większości sytuacji.

## Klawiatura nowoczesna

Obejmuje to panel emoji, historię schowka, klawiaturę dotykową, dyktowanie /
pisanie głosowe, sugestie dotyczące wprowadzania sprzętu, sugerowane
działania i nowoczesne edytory metod wprowadzania dla niektórych języków w
systemach Windows 10 i 11. Aby wyświetlić emotikony, aby uzyskać najlepsze
wyniki, włącz ustawienie Unicode Consortium z ustawień mowy NVDA i ustaw
poziom symbolu na "niektóre" lub wyższe. Podczas wklejania z historii
schowka w systemie Windows 10 naciśnij spacji zamiast Enter, aby wkleić
wybrany element.

* W systemie Windows 11 22H2 i nowszych NVDA poinformuje o sugerowanych
  działaniach, gdy kompatybilne dane, takie jak numery telefonów, zostaną
  skopiowane do schowka.

## Ustawienia

* NVDA ogłosi nazwę opcjonalnej kontroli jakości aktualizacji, jeśli jest
  obecna (pobierz i zainstaluj teraz link w systemie Windows 10, przycisk
  pobierania w systemie Windows 11).
* W systemie Windows 11 elementy paska okruszków nawigacyjnych są prawidłowo
  rozpoznawane.
* NVDA will report updates to Windows Update status as download and install
  progresses. This may result in speech interruption when navigating
  Settings app while updates are being downloaded and installed. If using
  Windows 11 and UIA event registration is set to selective from NVDA
  advanced settings panel, you must move focus to updates list as soon as
  they appear so NVDA can announce update progress.

## Dostęp głosowy

Odnosi się to do funkcji dostępu głosowego wprowadzonej w systemie Windows
11 22H2.

* NVDA ogłosi stan mikrofonu podczas przełączania mikrofonu z interfejsu
  dostępu głosowego.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps

[2]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-dev

[4]: https://github.com/josephsl/wintenapps/wiki/w10changelog
