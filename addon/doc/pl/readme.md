# Windows 10 App Essentials #

* Autorzy: Joseph Lee, Derek Riemer i Inni użytkownicy windowsa 10.
* Pobierz [wersja stabilna][1]
* Pobierz [Wersja rozwojowa][2]
* NVDA compatibility: 2020.1 to 2020.2

Ten dodatek jest kolekcją różnych modułów aplikacji dla Windows 10, jak
również ulepszeń i poprawek dla niektórych kontrolek w tym systemie.

Dołączone są następujące moduły wspierające aplikacje (sprawdź rozdział
każdej aplikacji, aby dokładnie sprawdzić co jest wspierane):

* Kalkulator (nowoczesny).
* Kalendarz
* Cortana (konwersacje)
* Poczta
* Mapy
* Microsoft Solitaire Collection
* Microsoft Store
* Klawiatura współczesna (panel emoji/dyktowanie/podpowiedzie wpisywania na
  klawiaturze sprzętowej/historia schowka w chmurze/współczesne edytory
  wprowadzania wschodnioazjatyckiego)
* Osoby
* Ustawienia (Ustawienia systemowe, Windows+I)
* Pogoda.
* Różne moduły dla takich kontrolek, jak kafelki meni start.

Uwagi:

* Ten dodatek wymaga wersji systemu operacyjnego Windows 10 1909 (kompilacja
  18362) lub nowsza . Dla lepszych wyników, trzeba używać dodatku z ostatnią
  stabilną wersją systemu operacyjnego windows 10 (kompilacja 19041).
* Niektóre funkcję dodatku są, lub staną się częścią czytnika ekranu NVDA.
* Dla wpisów nie podanych poniżej, można wnioskować, że zostały one
  wprowadzone do NVDA. Nie można ich już zastosować, ponieważ dodatek nie
  wspiera starszych wydań systemu, lub aplikacje są zmienione w taki sposób,
  że te wpisy są unieważnione.

Aby zobaczyć listę zmian pomiędzy kolejnymi wersjami, prosimy przeczytać
[listę zmian dla wersji dodatku][3].

## Ogólne

* NVDA już nie będzie odtwarzało dźwięki błędu oraz robiło nic jeżeli ten
  dodatek zostanie aktywowany w Windowsie 7, Windowsie 8.1, i niewspieranych
  wersjach Windowsa 10.
* Niektóre okna dialogowe są od teraz prawidłowo rozpoznawane i wymawiane
  jako okna dialogowe. Są to np. okna dialogowe w wersjach testowych
  (settings app). Jest to już wbudowane w sam czytnik ekranu.
* W większości przypadków, NVDA może ogłaszać liczbę sugestii
  wyszukiwania. Ta funkcja jest kontrolowana przez opcję "odczytuj położenie
  obiektu" dostępną w ustawieniach NVDA, w panelu "prezentacja obiektu".
* Gdy jest uruchomione wyszukiwanie w wersji 1909 (aktualizacja listopadowa
  2019) i nowszych, podwójnie wymawianie wyników wyszukiwania jest mniej
  zauważalne, co idzie za tym, że to co jest wyświetlane na monitorze
  brajlowskim jest bardziej spójne przy przeglądaniu elementy.
* The following UIA events are recognized: controller for, drag start, drag
  cancel, drag complete, drag target enter, drag target leave, drag target
  dropped, element selected, item status, live region change, notification,
  system alert, text change, tooltip opened, window opened. With NVDA set to
  run with debug logging enabled, these events will be tracked, and for UIA
  notification event, a debug tone will be heard if notifications come from
  somewhere other than the currently active app. Some events will provide
  additional information such as element count in controller for event,
  state of the element for state change event, and item text for item status
  event.
* Teraz jest możliwe śledzenie zdarzeń z określonych oraz specyficznych
  aplikacji.
* NVDA will no longer appear to do nothing or play error tones if UIA
  Automation Id for an element could not be recorded when tracking events.
* Podczas otwierania, zamykając lub przełączając się między wirtualnymi
  pulpitami, NVDA będzie oznajmiała aktualny identyfikator (na przykład
  pulpit 2).
* NVDA nie będzie wypowiadało wielkość tekstu w meni start, gdy zmienia się
  rozdzielczość ekranu lub orientacja ekranu.
* Przy ułożeniu kafelków meni start lub szybkich akcji w centrum akcji za
  pomocą Alt+Shift+strzałek, NVDA będzie wymawiała informację o
  upuszczonyche elementach lub o ich nowych pozycjach.
* W ostatnich wersjach programu Word 365, NVDA już nie będzie wypowiadała
  "usuniętą słowo wstecz" gdy jest naciśnięta kombinacja klawiszy
  Control+Backspace.
* Powiadomienia takie jak zmiany głośności oraz jasności w eksploratorze
  plików i aktualizacji aplikacji powiadomienia o aktualizacjach w Microsoft
  store można wyłączyć, wyłączając opcje odczytuj powiadomienia w
  ustawieniach prezentacji obiektów NVDA.
* Okno dialogowe otwórz za pomocą w wersji 2004 (majowa aktualizacja 2020)
  and later jest odpowiednio wymawian gdy jest otwarte.

## Kalkulator

* Kiedy enter albo escape jest wciśnięty, NVDA będzie wymawiał wynik
  obliczenia.
* Dla wyliczeń, takich jak przetwarzanie jednostek lub waluty, NVDA
  automatycznie będzie wymawiało wyniki obliczenia
* NVDA nie będzie więcej wymawiało "nagłówek" dla wyników kalkulatora.
* NVDA powiadomi, jeżeli ilość liczb osiągnie maksymalną wartość przy
  wpisywaniu wyrażenia.
* Dodano wsparcie trybu  "zawsze włączony", wersja 10.1908 i nowsza.

## Kalendarz

* NVDA nie wymawia więcej "pole edycji" lub "tylko do odczytu" w ciele
  wiadomości i innych polach.

## Cortana

Większość elementów nie jest już zastosowalna dla wersji 1903 i nowszych
wyjątkiem są konwersacje Cortana (wersja 2004 and later) .

* Odpowiedzi tekstowe kortany są wymawiane w większości sytuacjach.
* NVDA będzie przyciszony, gdy mówisz do Cortany.
* W wersji 1909 (aktualizacja dla listopada 2019) i nowszych, współczesne
  wyszukiwanie używane przez interfejs wyszukiwania windows od teraz jest
  wymawiane prawidłowo.

## Poczta

* Przy wyświetlaniu elementów w listy wiadomości, teraz można użyć skrótów
  dla nawigacji po tabelach, aby przeczytać nagłówki wiadomości. Miejcie na
  uwadze, że nawigacja po kolumnach (wiadomościach) jest niewspierana.
* Przy pisaniu wiadomości, istnienie podpowiedzi o wzmiankach teraz jest
  oznajmiane dzwiękami.

## Mapy

* NVDA ottwarza sygnały dźwiękowe położenia dla położenia na mapie.
* Przy użyciu trybu ulicy i jeśli opcja "użyj klawiatury" jest włączona,
  NVDA będzie wymawiać adresy ulic przy nawigacji strzałkami po mapie.

## Microsoft Solitaire Collection

* NVDA będzie wymawiała nazwy kart i talij.

## Microsoft Store

* Po sprawdzaniu aktualizacji aplikacji, nazyw aplikacji w liście aplikacji
  do zaktualizowania są poprawnie oznaczone.
* Przy pobieraniu zawartości, takiej jak aplikacje i muzyka, NVDA wymówi
  nazwę produktu i pasek postępu.

## Klawiatura nowoczesna

Włączony jest w to panel emoji, historia schowka, dyktowanie, podpowiedzi
klawiatury sprzętowej, i współczesne metody wprowadzania dla niektórych
języków. Przy czytaniu emoji, dla lepszej doświadczenia, włącz ustawienie
odczytywania emoji w ustawieniach mowy NVDA, a poziom interpunkcji na
"niektóre" lub wyższy.

* Gdy historia schowka jest wypowiadana, NVDA już nie będzie wymawiała
  "schowek" w niektórych przypadkach, gdy istnieje treść.
* Na niektórych komputerach na których jest uruchomiony Windows 10  1903
  (Aktualizacja z maju 2019), NVDA nie będzie wydawała efekt robienia nic
  gdy panel emoji się otwiera.
* Dodano wsparcie dla współczesnego interfejsu kandydatów dla chińskiego,
  japońskiego, i koreańskiego (CJK) wprowadzonego w wersji 2004 (kompilacja
  18965 i nowsze).
* When an emoji group (including kaomoji and symbols group in Version 1903
  or later) is selected, NVDA will no longer move navigator object to
  certain emojis.

## Osoby

* Przy wyszukiwaniu kontaktów, dźwięk będzie ottwarzany, jeżeli istnieją
  wyniki wyszukiwania.

## Ustawienia

* Większość informacji, takich jak pasek stanu w Windows update, będzie
  wypowiadany automatycznie, włączając w to widget czujnika pamięci i błędy
  z Windows update.
* Wartości paska postępu i inne informacje, nie są wypowiadane
  automatycznie.
* Dla niektórych list rozwijanych i przycisków opcji, NVDA będzie wykrywał
  nazwę oraz wypowiadał zmiany wartości. 
* W niektórych przypadkach, gdy używana jest nawigacja obiektowa, NVDA nie
  będzie się zachowywał  sposób nijaki, albo nie będzie odtwarzał dźwięku
  błedu.
* Okno dialogowe przypomnienia o aktualizacjach Windows, teraz jest
  rozpoznawane jako poprawne okno dialogowe.
* Nieparzyste kontrolki obecne w niektórych oknach instalacji Windows 10
  zostały poprawione.
* Wbardziej ostatnich aktualizacjach Windowsa  1803 i nowszych, z powodu
  zmian procederów windows update dla aktualizacji funkcji, dodano przycisk
  "pobierz i zainstaluj teraz". Jeżeli znaleziono aktualizację, NVDA będzie
  oznajmiałą jej tytuł.

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
