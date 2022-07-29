# Windows App Essentials #

* Autorzy: Joseph Lee, Derek Riemer i inni
* Pobierz [wersja stabilna][1]
* Pobierz [wersja rozwojowa][2]
* Zgodność z NVDA: 2021.3 i nowsze

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
* Mapy
* Nowoczesna klawiatura (panel emoji/dyktowanie/pisanie głosowe/sugestie
  wprowadzania sprzętowego/historia schowka/Sugerowane działania
  (podgląd)/nowoczesne edytory metod wprowadzania)
* Notatnik (Windows 11)
* Osoby
* Ustawienia (ustawienia systemowe, Windows+I)
* Voice access (Windows 11 22H2)
* Pogoda
* Różne moduły dla kontrolek, takie jak kafelki menu Start

Notatki:

* This add-on requires Windows 10 21H1 (build 19043), Windows 11 21H2 (build
  22000), or later releases.
* Chociaż instalacja jest możliwa, ten dodatek nie obsługuje wersji Windows
  Enterprise LTSC (Long-Term Servicing Channel) i Windows Server.
* Nie wszystkie funkcje kompilacji systemu Windows Insider Preview będą
  obsługiwane.
* Niektóre funkcje dodatkowe są lub będą częścią czytnika ekranu NVDA.
* W przypadku wpisów niewymienionych poniżej można założyć, że funkcje są
  częścią NVDA, nie mają już zastosowania, ponieważ dodatek nie obsługuje
  przestarzałe wersji systemu Windows, takich jak stare wersje systemu
  Windows 10, lub wprowadzono zmiany w systemie Windows i aplikacjach, które
  sprawiają, że wpisy nie mają już zastosowania.
* Niektóre aplikacje obsługują tryb kompaktowej nakładki (na przykład zawsze
  na górze w kalkulatorze), a ten tryb nie będzie działał poprawnie z
  przenośną wersją NVDA.
* Aby uzyskać najlepsze wrażenia z aplikacji, które osadzają technologie
  internetowe i zawartość, taką jak menu Start i jego menu kontekstowe,
  włącz ustawienie "Automatyczny tryb ustawiania ostrości dla zmian
  ostrości" w panelu ustawień trybu przeglądania NVDA.

Listę zmian wprowadzonych między poszczególnymi wersjami dodatków można
znaleźć w dokumencie [dzienniki zmian dla wydań dodatków][3].

## Ogólne

* Oprócz programów obsługi zdarzeń UIA dostarczanych przez NVDA rozpoznawane
  są następujące zdarzenia i właściwości UIA: przeciągnij zakończone, efekt
  przeciągania, upuść cel upuszczony. Po ustawieniu poziomu dziennika NVDA
  na debugowanie zdarzenia te będą śledzone i rejestrowane.
* Podczas otwierania, zamykania, zmiany kolejności (Windows 11) lub
  przełączania się między pulpitami wirtualnymi NVDA ogłosi nazwę aktywnego
  pulpitu wirtualnego (na przykład pulpit 2).
* Podczas rozmieszczania przypiętych wpisów (kafelków w systemie Windows 10)
  w menu Start lub szybkich akcji Centrum akcji za pomocą Alt + Shift +
  strzałek, NVDA ogłosi informacje o przeciągniętych elementach lub nowej
  pozycji przeciągniętego elementu.
* Anonsy, takie jak zmiany głośności/jasności w Eksploratorze plików i
  powiadomienia o aktualizacjach aplikacji ze sklepu Microsoft Store, można
  pominąć, wyłączając opcję Powiadomienia o raportach w ustawieniach
  prezentacji obiektów NVDA.
* In Windows 11 22H2 and later, microphone mute toggle status
  (Windows+Alt+K) is announced from everywhere.
* NVDA nie będzie już powtarzać tekstu wyjściowego w Terminalu Windows
  1.12.10733 i nowszych. Jest to teraz część NVDA 2022.1.
* NVDA po raz kolejny ogłosi szczegóły wyników wyszukiwania w menu
  Start. Jest to teraz część NVDA 2022.2.
* W systemie Windows 11 elementy paska zadań i inne elementy interfejsu
  użytkownika powłoki można wykryć poprawnie podczas korzystania z myszy i /
  lub interakcji dotykowej. Jest to teraz część NVDA 2022.2.

## Kalkulator

* W systemie Windows 10 elementy listy historii i pamięci są prawidłowo
  oznaczone. Jest to teraz część NVDA 2022.1.
* NVDA ogłosi wyświetlanie zawartości kalkulatora podczas wykonywania
  poleceń trybu naukowego, takich jak operacje trygonometrii. Jest to teraz
  część NVDA 2022.2.

## Cortana

* Odpowiedzi tekstowe z Cortany są ogłaszane w większości sytuacji.
* NVDA będzie milczeć podczas rozmowy z Cortaną za pomocą głosu.

## Mapy

* NVDA odtwarza sygnał dźwiękowy lokalizacji dla lokalizacji na mapie.

## Klawiatura nowoczesna

Obejmuje to panel emoji, historię schowka, dyktowanie / pisanie głosowe,
sugestie wprowadzania sprzętu, sugerowane działania (podgląd) i nowoczesne
edytory metod wprowadzania dla niektórych języków w systemach Windows 10 i
11. Podczas przeglądania emotikonów, aby uzyskać najlepsze wrażenia, włącz
ustawienie Unicode Consortium w ustawieniach mowy NVDA i ustaw poziom
symbolu na "niektóre" lub wyższe. Podczas wklejania z historii schowka w
systemie Windows 10 naciśnij spacji zamiast wchodzić, aby wkleić wybrany
element.

* W systemie Windows 10 po wybraniu grupy emoji (w tym grupy kaomoji i
  symboli), NVDA nie będzie już przenosić obiektu nawigatora do określonych
  emotikonów.
* W systemie Windows 11 ponownie można używać strzałek do przeglądania
  emotikonów po otwarciu panelu emoji. Jest to teraz część NVDA 2022.1.
* W historii schowka systemu Windows 11 tryb przeglądania zostanie domyślnie
  wyłączony, zaprojektowany tak, aby NVDA ogłaszała elementy menu
  wprowadzania historii schowka.
* In Insider Preview build 25115 and later (backported to Windows 11 beta
  build 22622), NVDA will announce suggested actions when compatible data
  such as phone numbers is copied to the clipboard.

## Notatnik

Odnosi się to do Notatnika systemu Windows 11 w wersji 11 lub nowszej.

* NVDA ogłosi elementy stanu, takie jak informacje o wierszu i kolumnie, gdy
  zostanie wykonane polecenie paska stanu raportu (NVDA + End w układzie
  pulpitu, NvDA + Shift + End w układzie laptopa). Jest to teraz część NVDA
  2022.2.

## Osoby

* Przy wyszukiwaniu kontaktów, dźwięk będzie ottwarzany, jeżeli istnieją
  wyniki wyszukiwania.

## Ustawienia

* Niezrozumiałe nazwy kontrolek obecne w niektórych oknach instalacji
  Windows 10 zostały poprawione.
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
