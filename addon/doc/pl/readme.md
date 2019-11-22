# Windows 10 App Essentials #

* Autorzy: Joseph Lee, Derek Riemer i Inni użytkownicy windowsa 10.
* Pobierz [wersja stabilna][1]
* Pobierz [Wersja rozwojowa][2]
* Zgodność z wersjami NVDA: 2019.2 do 2019.3

Ten dodatek jest kolekcją różnych modułów aplikacji dla Windows 10, jak
również ulepszeń i poprawek dla niektórych kontrolek w tym systemie.

Dołączone są następujące moduły wspierające aplikacje (sprawdź rozdział
każdej aplikacji, aby dokładnie sprawdzić co jest wspierane):

* Kalkulator (nowoczesny).
* Kalendarz
* Cortana (klasyczna i konwersacje)
* Centrum opinii
* Poczta
* Mapy
* Microsoft Edge
* Microsoft Store
* Nowoczesna klawiatura (panel emoji/dyktowanie/podpowiedzi wpisywania
  sprzętowego/elementy chmurowego schowka w wersji 1709  nowszych)
* Osoby
* Ustawienia (Ustawienia systemowe, Windows+I)
* Pogoda.
* Różne moduły dla takich kontrolek, jak kafelki meni start.

Uwagi:

* Uwaga! Ten dodatek wymaga Windowsa 10 Wersji 1809 (kompilacji 17763) lub
  nowszej i NVDA 2019.2 lub nowszej. Aby uzyskać najlepsze wyniki, należy
  używać dodatku z najnowszą stabilną kompilacją systemu (kompilacja 18363)
  i najnowszą stabilną wersją NVDA. 
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
* Elementy meni rozwijanego są prawidłowo rozpoznawane w różnych
  aplikacjach, takich jak menu kontekstowe dla kafelków meni start, a także
  menu aplikacji dla Microsoft Edge (aktualizacja 1809).
* Niektóre okna dialogowe są od teraz prawidłowo rozpoznawane i wymawiane
  jako okna dialogowe. Są to np. okna dialogowe w wersjach testowych
  (settings app). Jest to już wbudowane w sam czytnik ekranu.
* W większości przypadków, NVDA może ogłaszać liczbę sugestii
  wyszukiwania. Ta funkcja jest kontrolowana przez opcję "odczytuj położenie
  obiektu" dostępną w ustawieniach NVDA, w panelu "prezentacja obiektu".
* NVDA już nie będzie wymawiała "pusto" podczas naciskania strzałek w góre i
  w dół do otwierania przeglądu wszystkich aplikacji w meni start. Będzie to
  część NVDA 2019.3.
* Gdy jest uruchomione wyszukiwanie w wersji 1909 (aktualizacja listopadowa
  2019) i nowszych, podwójnie wymawianie wyników wyszukiwania jest mniej
  zauważalne, co idzie za tym, że to co jest wyświetlane na monitorze
  brajlowskim jest bardziej spójne przy przeglądaniu elementy.
* W większości meni kontekstowych (tak jak w Microsoft Edge), informacja o
  położeniu (NP. 1 z 2) nie jest już odczytywana.
* Następujące zdarzenia UIA są rozpoznawane: controller for, drag start,
  drag cancel, drag complete, drag target enter, drag target leave, drag
  target dropped, element selected, item status, live region change,
  notification, system alert, text change, tooltip opened, window
  opened. Gdy NVDA jest uruchomiony z zapisywaniem debugowania, te zdarzenia
  będą śledzone, i dla UIA zdarzenia powiadomień, a dźwięk debugowania
  będzie odtwarzany jeżeli powiadomienia przychodzą z innej niż aktualnie
  aktywnej aplikacji.
* Teraz jest możliwe śledzenie zdarzeń z określonych oraz specyficznych
  aplikacji.
* Opisy obiektów w Edge i innych aplikacjach UWP są rozpoznawane  i będą
  czytane automatycznie. To będzie częścią NVDA 2019.3.
* Podczas otwierania, zamykając lub przełączając się między wirtualnymi
  pulpitami, NVDA będzie oznajmiała aktualny identyfikator (na przykład
  pulpit 2).
* NVDA nie będzie wypowiadało wielkość tekstu w meni start, gdy zmienia się
  rozdzielczość ekranu lub orientacja ekranu.
* Wersja i nazwa aplikacji teraz są wyświetlane poprawnie dla różnych
  aplikacji współczesnych. Będzie to częscią NVDA 2019.3.
* Przy ułożeniu kafelków meni start lub szybkich akcji w centrum akcji za
  pomocą Alt+Shift+strzałek, NVDA będzie wymawiała informację o
  upuszczonyche elementach lub o ich nowych pozycjach.

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

Niektóre elementy już nie są zastosowalne dla wersji 1903 i
nowszych. Kortana klasyczna była częścią meni start.

* Tekstualne odpowiedzi Cortany (zarówno klasycznej jak i interfejsu
  konwersacji) są wypowiadane w większości sytuacji (Jeśli jest używana
  klasyczna Cortana, ponownie otwórz Cortanę klasyczną jeśli odpowiedzi nie
  są wypowiadane).
* NVDA będzie przyciszony, gdy mówisz do Cortany.
* W Cortany klasycznej, NVDA będzie wypowiadała powiadomienia cortany kiedy
  jedne będzie ustawione.
* W wersji 1909 (aktualizacja dla listopada) i kompilacji 20H1 18945 i
  nowszych, współczesne wyszukiwanie jest wspierane.

## Centrum opinii

* Dla nowych wyda aplikacji, NVDA więcej nie będzie oznajmiało kategorię
  informacji zwrotnych dwukrotnie.

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

## Microsoft Edge

Jest to odwołanie do klasycznego Microsoft edge.

* Autouzupełnienie tekstu będzie śledzone i wymawiane w omnibarze. Będzie ot
  częścią NVDA 2019.3.
* NVDA nie będzie już odtwarzać dźwięku podpowiedzi po naciśnięciu F11 aby
  przełączyć pełny ekran. Będzie to częścią NVDA 2019.3.
* Wyłączono odtwarzanie dźwięku dla pasku adresowego omnibar. Będzie to
  częscią NVDA 2019.3.

## Microsoft Store

* Po sprawdzaniu aktualizacji aplikacji, nazyw aplikacji w liście aplikacji
  do zaktualizowania są poprawnie oznaczone.
* Przy pobieraniu zawartości, takiej jak aplikacje i muzyka, NVDA wymówi
  nazwę produktu i pasek postępu.

## Klawiatura nowoczesna

Uwaga: Większość funkcji tego dodatku jest teraz częścią NVDA 2018.3 lub
nowszej wersji.

* Wsparcie dla panelu wprwadzania emij w wersji 1709 (zimowa aktualizacja
  dla twórców) i nowsze, włączając to przeprojektowany panel w wersji 1809
  (kompilacja 17661 i nowsze) i zmiany w 19H1 (kompilacja 18262 i nowsze,
  włączając w to kaomoji i kategorie symboli w kompilacji 18305). jest to
  także zastosowalne dla kompilacji 18963 i nowszych bo aplikacja zmieniła
  nazwę. Używając NVDA wydania wcześniejsze niż 2018.4, dla lepszego
  wrażenia czytania emoji, prosimy używać Windows OneCore syntezatora
  mowy. Jeżeli jest używane wydanie 2018,4 lub nowsze, prosimy włączyć dane
  konsorcjum unicode i ustaw poziom symboli na "niektóre" lub większe.
* NVDA już nie będzie wymawiała "showek" gdy istnieją w nim elementy.
* Na niektórych komputerach na których jest uruchomiony Windows 10  1903
  (Aktualizacja z maju 2019), NVDA nie będzie wydawała efekt robienia nic
  gdy panel emoji się otwiera.
* Dodane wsparcie dla interfejsu współczesnego IME dla języków chińskiego,
  japońskiego, i koreańskiego (CJK) wprowadzonego w 20H1 wersji 18965 i
  nowszych.

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
* Dzwięki paska postępu głośności nie są więcej słyszane w kompilacji 1803 i
  nowszych. Będzie to częścią NVDA 2019.3
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
