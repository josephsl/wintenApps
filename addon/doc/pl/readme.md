# Windows App Essentials #

* Autorzy: Joseph Lee, Derek Riemer i inni
* Pobierz [wersja stabilna][1]
* Pobierz [wersja rozwojowa][2]
* NVDA compatibility: 2021.3 and later

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

* Kalkulator
* Cortana
* Mail
* Mapy
* Microsoft Solitaire Collection
* Modern keyboard (emoji panel/dictation/voice typing/hardware input
  suggestions/clipboard history/Suggested Actions (preview)/modern input
  method editors)
* Notepad (Windows 11)
* Osoby
* Ustawienia (ustawienia systemowe, Windows+I)
* Voice access (Windows 11)
* Pogoda
* Różne moduły dla kontrolek, takie jak kafelki menu Start

uwagi: 

* This add-on requires Windows 10 21H1 (build 19043), Windows 11 21H2 (build
  22000) or later.
* Chociaż instalacja jest możliwa, ten dodatek nie obsługuje wersji Windows
  Enterprise LTSC (Long-Term Servicing Channel) i Windows Server.
* Not all features from Windows Insider Preview builds will be supported.
* Niektóre funkcje dodatkowe są lub będą częścią czytnika ekranu NVDA.
* W przypadku wpisów niewymienionych poniżej można założyć, że funkcje są
  częścią NVDA, nie mają już zastosowania, ponieważ dodatek nie obsługuje
  przestarzałe wersji systemu Windows, takich jak stare wersje systemu
  Windows 10, lub wprowadzono zmiany w systemie Windows i aplikacjach, które
  sprawiają, że wpisy nie mają już zastosowania.
* Niektóre aplikacje obsługują tryb kompaktowej nakładki (na przykład zawsze
  na górze w kalkulatorze), a ten tryb nie będzie działał poprawnie z
  przenośną wersją NVDA.
* For best experience with apps that embed web technologies and content such
  as Start menu and its context menu, enable "Automatic focus mode for focus
  changes" setting from NVDA's browse mode settings panel.

Listę zmian wprowadzonych między poszczególnymi wersjami dodatków można
znaleźć w dokumencie [dzienniki zmian dla wydań dodatków][3].

## Ogólne

* In addition to UIA event handlers provided by NVDA, the following UIA
  events and properties are recognized: drag complete, drag drop effect,
  drop target dropped. With NVDA's log level set to debug, these events will
  be tracked and logged.
* Podczas otwierania, zamykania, zmiany kolejności (Windows 11) lub
  przełączania się między pulpitami wirtualnymi NVDA ogłosi nazwę aktywnego
  pulpitu wirtualnego (na przykład pulpit 2).
* When arranging pinned entries (tiles in Windows 10) in Start menu or
  Action Center quick actions with Alt+Shift+arrow keys, NVDA will announce
  information on dragged items or new position of the dragged item.
* Anonsy, takie jak zmiany głośności/jasności w Eksploratorze plików i
  powiadomienia o aktualizacjach aplikacji ze sklepu Microsoft Store, można
  pominąć, wyłączając opcję Powiadomienia o raportach w ustawieniach
  prezentacji obiektów NVDA.
* In Windows 11 Insider Preview builds, microphone mute toggle status
  (Windows+Alt+K) is announced from everywhere.
* NVDA will no longer repeat text output in Windows Terminal 1.12.10733 and
  later. This is now part of NVDA 2022.1.
* NVDA will once again announce search result details in Start menu. This is
  now part of NVDA 2022.2.
* In Windows 11, Taskbar items and other shell user interface elements can
  be detected properly when using mouse and/or touch interaction. This is
  now part of NVDA 2022.2.

## Kalkulator

* In Windows 10, history and memory list items are properly labeled. This is
  now part of NVDA 2022.1.
* NVDA will announce calculator display content when performing scientific
  mode commands such as trigonometry operations. This is now part of NVDA
  2022.2.

## Cortana

* Odpowiedzi tekstowe z Cortany są ogłaszane w większości sytuacji.
* NVDA będzie milczeć podczas rozmowy z Cortaną za pomocą głosu.

## Mail

* Podczas przeglądania elementów na liście wiadomości można teraz używać
  poleceń nawigacji po tabeli do przeglądania nagłówków
  wiadomości. Pamiętaj, że nawigacja między wierszami (wiadomościami) nie
  jest obsługiwana.

## Mapy

* NVDA odtwarza sygnał dźwiękowy lokalizacji dla lokalizacji na mapie.

## Microsoft Solitaire Collection

* NVDA ogłosi nazwy kart i talii kart.

## Klawiatura nowoczesna

This includes emoji panel, clipboard history, dictation/voice typing,
hardware input suggestions, suggested actions (preview), and modern input
method editors for certain languages across Windows 10 and 11. When viewing
emojis, for best experience, enable Unicode Consortium setting from NVDA's
speech settings and set symbol level to "some" or higher. When pasting from
clipboard history in Windows 10, press Space key instead of Enter key to
paste the selected item.

* In Windows 10, when an emoji group (including kaomoji and symbols group)
  is selected, NVDA will no longer move navigator object to certain emojis.
* In Windows 11, it is again possible to use the arrow keys to review emojis
  when emoji panel opens. This is now part of NVDA 2022.1.
* In Windows 11 clipboard history, browse mode will be turned off by
  default, designed to let NVDA announce clipboard history entry menu items.
* In Insider Preview build 25115, NVDA will announce suggested actions when
  compatible data such as phone numbers is copied to the clipboard.

## Notepad

This refers to Windows 11 Notepad version 11 or later.

* NVDA will announce status items such as line and column information when
  report status bar command (NVDA+End in desktop layout, NvDA+Shift+End in
  laptop layout) is performed. This is now part of NVDA 2022.2.

## Osoby

* Przy wyszukiwaniu kontaktów, dźwięk będzie ottwarzany, jeżeli istnieją
  wyniki wyszukiwania.

## Ustawienia

* Niezrozumiałe nazwy kontrolek obecne w niektórych oknach instalacji
  Windows 10 zostały poprawione.
* NVDA will announce the name of the optional quality update control if
  present (download and install now link in Windows 10, download button in
  Windows 11).
* In Windows 11, breadcrumb bar items are properly recognized.
* In Windows 10, NVDA will interupt speech and report updates to Windows
  Update status as download and install progresses. This may result in
  speech interruption when navigating Settings app while updates are being
  downloaded and installed.

## Voice access

This refers to Voice access feature introduced in Windows 11 22H2 preview.

* NVDA will announce microphone status when toggling microphone from Voice
  access interface.

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
