# Windows App Essentials #

* Autorzy: Joseph Lee, Derek Riemer i inni
* Pobierz [wersja stabilna][1]
* Pobierz [wersja rozwojowa][2]
* NVDA compatibility: 2022.2 and later

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
* Modern keyboard (emoji panel/dictation/voice typing/hardware input
  suggestions/clipboard history/Suggested Actions/modern input method
  editors)
* Osoby
* Ustawienia (ustawienia systemowe, Windows+I)
* Voice access (Windows 11 22H2)
* Pogoda
* Różne moduły dla kontrolek, takie jak kafelki menu Start

Notatki:

* This add-on requires Windows 10 21H2 (build 19044), 11 21H2 (build 22000),
  or later releases.
* Feature update support duration is tied to consumer support duration
  (Home, Pro, Pro Education, Pro for Workstations editions) and the add-on
  may end support for a feature update prior to end of consumer support. See
  aka.ms/WindowsTargetVersioninfo for more information and support dates.
* Chociaż instalacja jest możliwa, ten dodatek nie obsługuje wersji Windows
  Enterprise LTSC (Long-Term Servicing Channel) i Windows Server.
* If Add-on Updater is installed and background add-on updates is enabled,
  Windows App Essentials will not install at all on unsupported Windows
  releases.
* Not all features from Windows Insider Preview builds will be supported,
  more so for features introduced to a subset of Windows Insiders in dev
  channel.
* Niektóre funkcje dodatkowe są lub będą częścią czytnika ekranu NVDA.
* Some apps support compact overlay mode (always on top in Calculator, for
  example), and this mode will not work properly with the portable version
  of NVDA.
* Aby uzyskać najlepsze wrażenia z aplikacji, które osadzają technologie
  internetowe i zawartość, taką jak menu Start i jego menu kontekstowe,
  włącz ustawienie "Automatyczny tryb ustawiania ostrości dla zmian
  ostrości" w panelu ustawień trybu przeglądania NVDA.

Listę zmian wprowadzonych między poszczególnymi wersjami dodatków można
znaleźć w dokumencie [dzienniki zmian dla wydań dodatków][3].

## Ogólne

* In addition to UIA event handlers provided by NVDA, the following UIA
  events and properties are recognized: drag start/cancel/complete
  (recognized as state change event), drag drop effect, drag item is
  grabbed, drop target effect.
* When opening, closing, or switching between virtual desktops, NVDA will
  announce active virtual desktop name (desktop 2, for example).
* When dragging and dropping items such as arranging pinned entries (tiles
  in Windows 10) in Start menu or Action Center quick actions with
  Alt+Shift+arrow keys, NVDA will announce "dragging" and/or drag and drop
  effects before and while dragging items, respectively. This is now part of
  NVDA 2022.4.
* Announcements such as volume/brightness/microphone mute (Windows 11 22H2
  and later) changes in File Explorer and app update notifications from
  Microsoft Store can be suppressed by turning off Report Notifications in
  NVDA's object presentation settings.
* In Windows 11, NVDA will announce search highlights in Start menu when it
  opens. This is now part of NVDA 2023.1.

## Cortana

* Odpowiedzi tekstowe z Cortany są ogłaszane w większości sytuacji.
* NVDA będzie milczeć podczas rozmowy z Cortaną za pomocą głosu.

## Mapy

* NVDA odtwarza sygnał dźwiękowy lokalizacji dla lokalizacji na mapie.

## Klawiatura nowoczesna

This includes emoji panel, clipboard history, dictation/voice typing,
hardware input suggestions, suggested actions, and modern input method
editors for certain languages across Windows 10 and 11. When viewing emojis,
for best experience, enable Unicode Consortium setting from NVDA's speech
settings and set symbol level to "some" or higher. When pasting from
clipboard history in Windows 10, press Space key instead of Enter key to
paste the selected item.

* In Windows 10 emoji panel, when an emoji group (including kaomoji and
  symbols group) is selected, NVDA will no longer move navigator object to
  certain emojis.
* W historii schowka systemu Windows 11 tryb przeglądania zostanie domyślnie
  wyłączony, zaprojektowany tak, aby NVDA ogłaszała elementy menu
  wprowadzania historii schowka.
* In Windows 11 22H2 Moment 1 and later, NVDA will announce suggested
  actions when compatible data such as phone numbers is copied to the
  clipboard.

## Osoby

* When searching for contacts, first suggestion will be announced.

## Ustawienia

* NVDA ogłosi nazwę opcjonalnej kontroli jakości aktualizacji, jeśli jest
  obecna (pobierz i zainstaluj teraz link w systemie Windows 10, przycisk
  pobierania w systemie Windows 11).
* W systemie Windows 11 elementy paska okruszków nawigacyjnych są prawidłowo
  rozpoznawane.
* In Windows 10 and 11 22H2 and later, NVDA will interupt speech and report
  updates to Windows Update status as download and install progresses. This
  may result in speech interruption when navigating Settings app while
  updates are being downloaded and installed. If using Windows 11 22H2 and
  later, if selective UIA event registration is on, you must move focus to
  updates list as soon as they appear so NVDA can announce update progress.

## Dostęp głosowy

This refers to Voice access feature introduced in Windows 11 22H2.

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
