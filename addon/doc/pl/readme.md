# Windows App Essentials #

* Autorzy: Joseph Lee, Derek Riemer i inni
* Pobierz [wersja stabilna][1]
* Pobierz [wersja rozwojowa][2]
* Zgodność z wersjami NVDA: 2021.2 i nowsze

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

* Kalkulator (nowoczesny)
* Cortana (konwersacje)
* Mail
* Mapy
* Microsoft Solitaire Collection
* Microsoft Store
* Nowoczesna klawiatura (panel emoji / dyktowanie / pisanie głosowe /
  podpowiedzi do pisania na klawiaturze sprzętowej / historia schowka /
  nowoczesne edytory metod wprowadzania)
* Osoby
* Ustawienia (ustawienia systemowe, Windows+I)
* Pogoda
* Różne moduły dla kontrolek, takie jak kafelki menu Start

uwagi: 

* Ten dodatek wymaga systemu Windows 10 20H2 (kompilacja 19042) lub nowszego
  i jest zgodny z systemem Windows 11.
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

* NVDA może ogłosić liczbę sugestii podczas wyszukiwania w większości
  przypadków, w tym gdy sugestie liczą zmiany w miarę postępu
  wyszukiwania. Ta opcja jest kontrolowana przez "Raport informacji o
  położenia obiektu" w panelu Prezentacja obiektu znajdującym się w
  ustawieniach NVDA.
* Oprócz programów obsługi zdarzeń UIA dostarczanych przez NVDA rozpoznawane
  są następujące zdarzenia UIA: przeciągnij start, przeciągnij anuluj,
  przeciągnij complete, upuść docelowy przeciągnij enter, upuść docelowy
  przeciągnij w udziel, upuść cel upuszczony, układ unieważniony. Po
  ustawieniu poziomu dziennika NVDA na debugowanie zdarzenia te będą
  śledzone, a w przypadku zdarzenia powiadomienia UIA dźwięk debugowania
  będzie słyszalny, jeśli powiadomienia pochodzą z innego miejsca niż
  aktualnie aktywna aplikacja. Zdarzenia wbudowane w NVDA, takie jak zmiana
  nazwy i kontroler zdarzeń, będą śledzone z dodatku o nazwie Event Tracker.
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

## Cortana

Większość elementów ma zastosowanie podczas korzystania z konwersacji
Cortany (Windows 10 2004 i nowsze).

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

## Microsoft Store

* Po sprawdzeniu dostępności aktualizacji aplikacji nazwy aplikacji na
  liście aplikacji do zaktualizowania są poprawnie oznaczone etykietami.
* Przy pobieraniu zawartości, takiej jak aplikacje i filmy, NVDA wymówi
  nazwę produktu i pasek postępu.

## Klawiatura nowoczesna

Obejmuje to panel emoji, historię schowka, dyktowanie / pisanie głosowe,
sugestie wprowadzania sprzętu i nowoczesne edytory metod wprowadzania dla
niektórych języków. Podczas przeglądania emotikonów, aby uzyskać najlepsze
wrażenia, włącz ustawienie Unicode Consortium w ustawieniach mowy NVDA i
ustaw poziom symbolu na "niektóre" lub wyższe. Podczas wklejania z historii
schowka w systemie Windows 10 naciśnij spacji zamiast wchodzić, aby wkleić
wybrany element. NVDA obsługuje również zaktualizowany panel doświadczenia
wejściowego w systemie Windows 11.

* Po wybraniu grupy emotikonów (w tym grupy kaomoji i symboli w systemie
  Windows 10 1903 lub nowszym) NVDA nie będzie już przenosić obiektu
  nawigatora do określonych emotikonów.
* Dodano obsługę zaktualizowanego panelu doświadczenia wprowadzania
  (połączony panel emoji i historia schowka) w systemie Windows 11.

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
* NVDA będzie wymawiała nazwę linku do pobieraniado opcjonalnej aktualizacji
  jakości, jeśli jest obecny, zwykle o nazwie "pobierz i zainstaluj teraz".

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
