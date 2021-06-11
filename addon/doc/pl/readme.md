# Windows 10 App Essentials #

* Autorzy: Joseph Lee, Derek Riemer i Inni użytkownicy windowsa 10.
* Pobierz [wersja stabilna][1]
* Pobierz [Wersja rozwojowa][2]
* Zgodność z wersjami NVDA: 2020.3 do 2020.4

Ten dodatek jest kolekcją różnych modułów aplikacji dla Windows 10, jak
również ulepszeń i poprawek dla niektórych kontrolek w tym systemie.

Dołączone są następujące moduły wspierające aplikacje (sprawdź rozdział
każdej aplikacji, aby dokładnie sprawdzić co jest wspierane):

* Kalkulator (nowoczesny)
* Kalendarz
* Cortana (konwersacje)
* Poczta
* Mapy
* Microsoft Solitaire Collection
* Microsoft Store
* Nowoczesna klawiatura (panel emoji / dyktowanie / sugestie wejścia
  sprzętowego / historia schowka / nowoczesne edytory metod wprowadzania)
* Osoby
* Ustawienia (Ustawienia systemowe, Windows+I)
* Pogoda
* Różne moduły dla kontrolek, takie jak kafelki menu Start

Uwagi:

* Ten dodatek wymaga systemu Windows 10 w wersji 2004 (kompilacja 19041) lub
  nowszej. Aby uzyskać najlepsze wyniki, użyj dodatku z najnowszą wersją
  stabilną systemu Windows 10 (21H1/kompilacja 19043).
* Although installation is possible, this add-on does not support Windows 10
  Enterprise LTSC (Long-Term Servicing Channel) and Windows Server releases.
* Niektóre funkcję dodatku są, lub staną się częścią czytnika ekranu NVDA.
* Dla wpisów nie podanych poniżej, można wnioskować, że zostały one
  wprowadzone do NVDA. Nie można ich już zastosować, ponieważ dodatek nie
  wspiera starszych wydań systemu, lub aplikacje są zmienione w taki sposób,
  że te wpisy są unieważnione.
* Niektóre aplikacje obsługują tryb kompaktowej nakładki (zawsze na górze w
  kalkulatorze, na przykład), a ten tryb nie będzie działać poprawnie z
  przenośną wersją NVDA.

Aby zobaczyć listę zmian pomiędzy kolejnymi wersjami, prosimy przeczytać
[listę zmian dla wersji dodatku][3].

## Ogólne

* W większości przypadków, NVDA może ogłaszać liczbę sugestii
  wyszukiwania. Ta funkcja jest kontrolowana przez opcję "odczytuj położenie
  obiektu" dostępną w ustawieniach NVDA, w panelu "prezentacja obiektu".
* Gdy jest uruchomione wyszukiwanie w wersji 1909 (aktualizacja listopadowa
  2019) i nowszych, podwójnie wymawianie wyników wyszukiwania jest mniej
  zauważalne, co idzie za tym, że to co jest wyświetlane na monitorze
  brajlowskim jest bardziej spójne przy przeglądaniu elementy.
* Oprócz programów obsługi zdarzeń UIA dostarczonych przez NVDA rozpoznawane
  są następujące zdarzenia UIA: drag start, drag cancel, drag complete, drop
  target drag enter, drop target drag leave, drop target dropped. Z poziomu
  dziennika NVDA ustawiony na debugowanie, te zdarzenia będą śledzone, a dla
  zdarzenia powiadomień UIA dźwięk debugowania będą słyszane, jeśli
  powiadomienia pochodzą z innego miejsca niż aktualnie aktywna
  aplikacja. Niektóre zdarzenia zapewni dodatkowe informacje, takie jak
  liczba elementów w kontrolerze dla zdarzenia, stan elementu dla zdarzenia
  zmiany stanu i tekst elementu dla zdarzenia stanu elementu.
* Teraz jest możliwe śledzenie zdarzeń z określonych oraz specyficznych
  aplikacji.
* Podczas otwierania, zamykając lub przełączając się między wirtualnymi
  pulpitami, NVDA będzie oznajmiała aktualny identyfikator (na przykład
  pulpit 2). Działa w kompilacji 21337 lub nowszej.
* NVDA nie będzie już ogłaszać tekstu o rozmiarze menu Start podczas zmiany
  rozdzielczości ekranu lub orientacji.
* Przy ułożeniu kafelków meni start lub szybkich akcji w centrum akcji za
  pomocą Alt+Shift+strzałek, NVDA będzie wymawiała informację o
  upuszczonyche elementach lub o ich nowych pozycjach.
* Powiadomienia takie jak zmiany głośności oraz jasności w eksploratorze
  plików i aktualizacji aplikacji powiadomienia o aktualizacjach w Microsoft
  store można wyłączyć, wyłączając opcje odczytuj powiadomienia w
  ustawieniach prezentacji obiektów NVDA.

## Kalkulator

* NVDA nie będzie już dwukrotnie ogłaszać komunikatu ekranu kalkulatora
  wykresów.

## Kalendarz

* NVDA nie wymawia więcej "pole edycji" lub "tylko do odczytu" w ciele
  wiadomości i innych polach.

## Cortana

Większość elementów ma zastosowanie podczas korzystania z konwersacji
Cortany (wersja 2004 lub nowsza).

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

Obejmuje to panel emoji, historię schowka, dyktowanie, sugestie dotyczące
wprowadzania sprzętu i nowoczesne edytory metod wprowadzania dla niektórych
języków. Podczas przeglądania emotikonów, aby uzyskać najlepsze wrażenia,
włącz ustawienie Konsorcjum Unicode z ustawień mowy NVDA i ustaw poziom
symbolu na "niektóre" lub wyższe. Ponadto NVDA obsługuje zaktualizowany
panel środowiska wejściowego w kompilacji 21296 i nowszych.

* Gdy historia schowka jest wypowiadana, NVDA już nie będzie wymawiała
  "schowek" w niektórych przypadkach, gdy istnieje treść.
* Na niektórych komputerach na których jest uruchomiony Windows 10  1903
  (Aktualizacja z maju 2019), NVDA nie będzie wydawała efekt robienia nic
  gdy panel emoji się otwiera.
* Gdy zaznaczona jest grupa emoji, włączając w to kaomoji i grupę symboli w
  wersji Windowsa 10 1903 lub nowszej) NVDA nie będzie przemieszczał obiekt
  nawigatora do poszczególnych emoji.
* Dodano obsługę zaktualizowanego panelu wejścia (połączony panel emoji i
  historię schowka) w kompilacji 21296 i nowszych.

## Osoby

* Przy wyszukiwaniu kontaktów, dźwięk będzie ottwarzany, jeżeli istnieją
  wyniki wyszukiwania.

## Ustawienia

* Większość informacji, takich jak pasek stanu w Windows update, będzie
  wypowiadany automatycznie, włączając w to widget czujnika pamięci i błędy
  z Windows update.
* Wartości paska postępu i inne informacje, nie są wypowiadane
  automatycznie.
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
