# Windows App Essentials #

* Autorzy: Joseph Lee, Derek Riemer i inni
* Pobierz [wersja stabilna][1]
* Pobierz [wersja rozwojowa][2]
* NVDA compatibility: 2021.2 and later

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
* Nowoczesna klawiatura (panel emoji / dyktowanie / pisanie głosowe /
  podpowiedzi do pisania na klawiaturze sprzętowej / historia schowka /
  nowoczesne edytory metod wprowadzania)
* Notepad (Windows 11)
* Osoby
* Ustawienia (ustawienia systemowe, Windows+I)
* Pogoda
* Różne moduły dla kontrolek, takie jak kafelki menu Start

uwagi: 

* This add-on requires Windows 10 21H1 (build 19043) or later and is
  compatible with Windows 11.
* Chociaż instalacja jest możliwa, ten dodatek nie obsługuje wersji Windows
  Enterprise LTSC (Long-Term Servicing Channel) i Windows Server.
* Niektóre funkcje dodatkowe są lub będą częścią czytnika ekranu NVDA.
* W przypadku wpisów niewymienionych poniżej można założyć, że funkcje są
  częścią NVDA, nie mają już zastosowania, ponieważ dodatek nie obsługuje
  przestarzałe wersji systemu Windows, takich jak stare wersje systemu
  Windows 10, lub wprowadzono zmiany w systemie Windows i aplikacjach, które
  sprawiają, że wpisy nie mają już zastosowania.
* Niektóre aplikacje obsługują tryb kompaktowej nakładki (na przykład zawsze
  na górze w kalkulatorze), a ten tryb nie będzie działał poprawnie z
  przenośną wersją NVDA.

Listę zmian wprowadzonych między poszczególnymi wersjami dodatków można
znaleźć w dokumencie [dzienniki zmian dla wydań dodatków][3].

## Ogólne

* NVDA can announce suggestion count when performing a search in majority of
  cases, including when suggestion count changes as search progresses. This
  is now part of NVDA 2021.3.
* In addition to UIA event handlers provided by NVDA, the following UIA
  events are recognized: drag complete, drop target dropped, layout
  invalidated. With NVDA's log level set to debug, these events will be
  tracked, and for UIA notification event, a debug tone will be heard if
  notifications come from somewhere other than the currently active
  app. Events built into NVDA such as name change and controller for events
  are tracked from an add-on called Event Tracker.
* Podczas otwierania, zamykania, zmiany kolejności (Windows 11) lub
  przełączania się między pulpitami wirtualnymi NVDA ogłosi nazwę aktywnego
  pulpitu wirtualnego (na przykład pulpit 2).
* NVDA nie będzie już ogłaszać tekstu rozmiaru menu Start podczas zmiany
  rozdzielczości lub orientacji ekranu.
* Podczas rozmieszczania kafelków menu Start lub szybkich akcji Centrum
  akcji za pomocą Alt+ Shift + strzałek, NVDA ogłosi informacje o
  przeciągniętych elementach lub nowym położeniu przeciągniętego elementu.
* Anonsy, takie jak zmiany głośności/jasności w Eksploratorze plików i
  powiadomienia o aktualizacjach aplikacji ze sklepu Microsoft Store, można
  pominąć, wyłączając opcję Powiadomienia o raportach w ustawieniach
  prezentacji obiektów NVDA.

## Kalkulator

* NVDA nie będzie już dwukrotnie ogłaszać komunikatu na ekranie kalkulatora
  graficznego.
* In Windows 10, history and memory list items are properly labeled.

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
* Podczas korzystania z widoku ulicy i jeśli opcja użyj klawiatury jest
  włączona, NVDA ogłosi adresy ulic, gdy używasz strzałek do poruszania się
  po mapie.

## Microsoft Solitaire Collection

* NVDA ogłosi nazwy kart i talii kart.

## Klawiatura nowoczesna

Obejmuje to panel emoji, historię schowka, dyktowanie / pisanie głosowe,
sugestie wprowadzania sprzętu i nowoczesne edytory metod wprowadzania dla
niektórych języków. Podczas przeglądania emotikonów, aby uzyskać najlepsze
wrażenia, włącz ustawienie Unicode Consortium w ustawieniach mowy NVDA i
ustaw poziom symbolu na "niektóre" lub wyższe. Podczas wklejania z historii
schowka w systemie Windows 10 naciśnij spacji zamiast wchodzić, aby wkleić
wybrany element. NVDA obsługuje również zaktualizowany panel doświadczenia
wejściowego w systemie Windows 11.

* In Windows 10, when an emoji group (including kaomoji and symbols group)
  is selected, NVDA will no longer move navigator object to certain emojis.
* Dodano obsługę zaktualizowanego panelu doświadczenia wprowadzania
  (połączony panel emoji i historia schowka) w systemie Windows 11.

## Notepad

This refers to Windows 11 Notepad version 11 or later.

* NVDA will announce status items such as line and column information when
  report status bar command (NVDA+End in desktop layout, NvDA+Shift+End in
  laptop layout) is performed.
* NVDA will no longer announce entered text when pressing Enter key from the
  document.

## Osoby

* Przy wyszukiwaniu kontaktów, dźwięk będzie ottwarzany, jeżeli istnieją
  wyniki wyszukiwania.

## Ustawienia

* Większość informacji, takich jak pasek stanu w Windows update, będzie
  wypowiadany automatycznie, włączając w to widget czujnika pamięci i błędy
  z Windows update.
* Wartości paska postępu i inne informacje, nie są wypowiadane
  automatycznie.
* Niezrozumiałe nazwy kontrolek obecne w niektórych oknach instalacji
  Windows 10 zostały poprawione.
* NVDA will announce the name of the optional quality update control if
  present (download and install now link in Windows 10, download button in
  Windows 11).
* In Windows 11, breadcrumb bar items are properly recognized.

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
