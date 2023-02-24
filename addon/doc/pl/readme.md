# Windows App Essentials #

* Autorzy: Joseph Lee, Derek Riemer i inni
* Pobierz [wersja stabilna][1]
* Pobierz [wersja rozwojowa][2]
* Zgodność z NVDA: 2022.4 i nowsze

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
* Mapy
* Nowoczesna klawiatura (panel emoji/klawiatura dotykowa/dyktowanie/pisanie
  głosowe/sugestie dotyczące wprowadzania sprzętu/historia
  schowka/sugerowane akcje/nowoczesne edytory metod wprowadzania)
* Ustawienia (ustawienia systemowe, Windows+I)
* Dostęp głosowy (Windows 11 22H2)
* Pogoda
* Różne moduły sterowania i funkcji, takich jak ogłoszenia wirtualnych
  pulpitów

Notatki:

* Ten dodatek wymaga systemu Windows 10 21H2 (kompilacja 19044), 11 21H2
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
* Not all features from Windows Insider Preview builds will be supported,
  more so for features introduced to a subset of Windows Insiders in dev
  channel.
* Niektóre funkcje dodatkowe są lub będą częścią czytnika ekranu NVDA.
* Niektóre aplikacje obsługują tryb kompaktowej nakładki (na przykład zawsze
  na wierzchu w Kalkulatorze), a ten tryb nie będzie działał poprawnie z
  przenośną wersją NVDA.
* Aby uzyskać najlepsze wrażenia z aplikacji, które osadzają technologie
  internetowe i zawartość, taką jak menu Start i jego menu kontekstowe,
  włącz ustawienie "Automatyczny tryb ustawiania ostrości dla zmian
  ostrości" w panelu ustawień trybu przeglądania NVDA.

Listę zmian wprowadzonych między poszczególnymi wersjami dodatków można
znaleźć w dokumencie [dzienniki zmian dla wydań dodatków][3].

## Ogólne

* Podczas otwierania, zamykania lub przełączania się między wirtualnymi
  pulpitami, NVDA ogłosi nazwę aktywnego wirtualnego pulpitu (na przykład
  desktop 2).
* W systemie Windows 11 NVDA ogłosi najważniejsze elementy wyszukiwania w
  menu Start po jego otwarciu. Jest to teraz część NVDA 2023.1.
* In Windows 11 22H2 and later, mouse and/or touch interaction can be used
  to interact with redesigned system tray overflow window and Open With
  dialog. This is now part of NVDA 2023.1.
* NVDA zapisze architekturę procesora dla bieżącej instalacji systemu
  Windows (x86/32-bit, AMD64, ARM64) po jej uruchomieniu. Jest to teraz
  część NVDA 2023.1.
* Improved Windows 10 and 11 taskbar experience, including announcing
  results of rearranging icons when pressing Alt+Shift+left/right arrow keys
  (Windows 11 prior to build 25267) and reporting item position when moving
  through taskbar icons (Windows 10 and 11 prior to build 25281).
* NVDA ogłosi komunikat o pustym folderze wewnątrz pustego folderu w
  Eksploratorze plików.
* In aps such as File Explorer and Notepad where tabbed windows are
  supported, NVDA will announce the name and the position of tabs when
  switching between them.

## Cortana

* Odpowiedzi tekstowe z Cortany są ogłaszane w większości sytuacji.
* NVDA będzie milczeć podczas rozmowy z Cortaną za pomocą głosu.

## Mapy

* NVDA odtwarza sygnał dźwiękowy lokalizacji dla lokalizacji na mapie.
* W niektórych przypadkach NVDA nie będzie już przerywać mowy, gdy skupi się
  na elementach innych niż sterowanie mapą.

## Klawiatura nowoczesna

Obejmuje to panel emoji, historię schowka, klawiaturę dotykową, dyktowanie /
pisanie głosowe, sugestie dotyczące wprowadzania sprzętu, sugerowane
działania i nowoczesne edytory metod wprowadzania dla niektórych języków w
systemach Windows 10 i 11. Aby wyświetlić emotikony, aby uzyskać najlepsze
wyniki, włącz ustawienie Unicode Consortium z ustawień mowy NVDA i ustaw
poziom symbolu na "niektóre" lub wyższe. Podczas wklejania z historii
schowka w systemie Windows 10 naciśnij spacji zamiast Enter, aby wkleić
wybrany element.

* W panelu emoji systemu Windows 10, gdy wybrana jest grupa emoji (w tym
  grupa kaomoji i symbole), NVDA nie będzie już przenosić obiektu nawigatora
  do niektórych emotikonów.
* W historii schowka systemu Windows 11 tryb przeglądania będzie domyślnie
  wyłączony, zaprojektowany tak, aby umożliwić NVDA ogłaszanie elementów
  menu wprowadzania historii schowka. Jest to teraz część NVDA 2023.1.
* W systemie Windows 11 22H2 i nowszych NVDA poinformuje o sugerowanych
  działaniach, gdy kompatybilne dane, takie jak numery telefonów, zostaną
  skopiowane do schowka.

## Ustawienia

* NVDA ogłosi nazwę opcjonalnej kontroli jakości aktualizacji, jeśli jest
  obecna (pobierz i zainstaluj teraz link w systemie Windows 10, przycisk
  pobierania w systemie Windows 11).
* W systemie Windows 11 elementy paska okruszków nawigacyjnych są prawidłowo
  rozpoznawane.
* W systemach Windows 10 i 11 22H2 i nowszych NVDA będzie zakłócać mowę i
  zgłaszać aktualizacje stanu usługi Windows Update w miarę postępu
  pobierania i instalacji. Może to spowodować przerwanie mowy podczas
  nawigowania po aplikacji Ustawienia podczas pobierania i instalowania
  aktualizacji. Jeśli używasz systemu Windows 11 22H2 i nowszych, jeśli
  selektywna rejestracja zdarzeń UIA jest włączona, musisz przenieść fokus
  na listę aktualizacji, gdy tylko się pojawią, aby NVDA mogła ogłosić
  postęp aktualizacji.

## Dostęp głosowy

Odnosi się to do funkcji dostępu głosowego wprowadzonej w systemie Windows
11 22H2.

* NVDA ogłosi stan mikrofonu podczas przełączania mikrofonu z interfejsu
  dostępu głosowego.

## Pogoda

* Karty właściwości, takie jak "prognoza" i "mapy" są rospoznane jak
  prawidłowe karty właściwości (poprawił Derek Riemer).
* Przy czytaniu pogody, użyj strzałek w lewo i w prawo aby się przemieszczać
  pomiędzy elementami. Użyj strzałki w górę lub w dół, aby przeczytać
  pojedynczy element. Na przykład, wciskając strzałke w prawo może wymówić
  "Poniedziałek: 79 stopni, częściowo pochmurno, ..." wciskając strzałkę w
  dół powie "Poniedziałek" wciskając ję jeszcze raz wypowie następujący
  element (jak temperaturę). Teraz to działą dla prognozy pogody dzienniej i
  godzinnej.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
