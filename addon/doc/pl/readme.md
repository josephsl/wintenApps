# Windows 10 App Essentials #

* Autorzy: Joseph Lee, Derek Riemer i Inni użytkownicy windowsa 10.
* Pobierz [wersja stabilna][1]
* Pobierz [Wersja rozwojowa][2]
* Zgodność z wersjami NVDA: 2018.4 do 2019.2

Ten dodatek jest kolekcją różnych modułów aplikacji dla Windows 10, jak
również ulepszeń i poprawek dla niektórych kontrolek w tym systemie.

Dołączone są następujące moduły wspierające aplikacje (sprawdź rozdział
każdej aplikacji, aby dokładnie sprawdzić co jest wspierane):

* Centrum powiadomień
* Alarmy i zegar.
* Kalendarz
* Kalkulator (nowoczesny).
* Cortana
* Centrum opinii
* Poczta
* Mapy
* Microsoft Edge
* Nowoczesna klawiatura (panel emoji/dyktowanie/podpowiedzi wpisywania
  sprzętowego/elementy chmurowego schowka w wersji 1709  nowszych)
* Osoby
* Ustawienia (Ustawienia systemowe, Windows+I)
* Sklep
* Pogoda.
* Różne moduły dla takich kontrolek, jak kafelki meni start.

Uwagi:

* Uwaga! Ten dodatek wymaga Windowsa 10 Wersji 1803 (kompilacji 17134) lub
  nowszej i NVDA 2018.4 lub nowszej. Aby uzyskać najlepsze wyniki, należy
  używać dodatku z najnowszą stabilną kompilacją systemu (kompilacja 18362)
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
  menu aplikacji dla Microsoft Edge (Redstone 5).
* Niektóre okna dialogowe są od teraz prawidłowo rozpoznawane i wymawiane
  jako okna dialogowe. Są to np. okna dialogowe w wersjach testowych
  (settings app). Jest to już wbudowane w sam czytnik ekranu.
* W większości przypadków, NVDA może ogłaszać liczbę sugestii
  wyszukiwania. Ta funkcja jest kontrolowana przez opcję "odczytuj położenie
  obiektu" dostępną w ustawieniach NVDA, w panelu "prezentacja obiektu".
* W większości meni kontekstowych (tak jak w Microsoft Edge), informacja o
  położeniu (NP. 1 z 2) nie jest już odczytywana.
* Następujące zdarzenia UIA są rozpoznawane: active text position change,
  controller for, drag start, drag cancel, drag complete, element selected,
  item status, live region change, notification, system alert, text change,
  tooltip opened, window opened. Gdy NVDA jest uruchomiony z zapisywaniem
  debugowania, te zdarzenia będą śledzone, i dla UIA notification event, a
  dźwięk debugowania będzie odtwarzany jeżeli powiadomienia przychodzą z
  innej niż aktualnie aktywnej aplikacji.
* Opisy obiektów w Edge i innych aplikacjach UWP są rozpoznawane  i będą
  czytane automatycznie.
* Podczas otwierania, zamykając lub przełączając się między wirtualnymi
  pulpitami, NVDA będzie oznajmiała aktualny identyfikator (na przykład
  pulpit 2).
* NVDA nie będzie wypowiadało wielkość tekstu w meni start, gdy zmienia się
  rozdzielczość ekranu lub orientacja ekranu.
* W wersji 1903 (aktualizacji dla maja 2019), NVDA będzie ogłaszać zmiany
  głośności dźwięku i jasności ekranu.

## Centrum powiadomień

* Szybka akcja jasności została zmieniona z przycisku przełączającego na
  przycisk zwykły. Jest to teraz część NVDA 2019.1.
* Róźne zmiany stanu, takie jak asysta punktu uwagi i jasność będą
  wymawiane. Jest to teraz część  NVDA 2019.1.

## Alarmy i zegar

* Teraz są wypowiadane kontrolki wypowiadania czasu, zauważalne przy
  poruszaniu się po nich. To także dotyczy kontrolki wyboru czasu ponownego
  uruchomienia po instalacji aktualizacji. To jest teraz część NVDA 2019.1.

## Kalkulator

* Kiedy enter albo escape jest wciśnięty, NVDA wymawia wynik obliczenia.
* Dla wyliczeń, takich jak przetwarzanie jednostek lub waluty, NVDA
  automatycznie będzie wymawiało wyniki obliczenia
* NVDA nie będzie więcej wymawiało "nagłówek" dla wyników kalkulatora.
* NVDA powiadomi, jeżeli ilość liczb osiągnie maksymalną wartość przy
  wpisywaniu wyrażenia.

## Kalendarz

* NVDA nie wymawia więcej "pole edycji" lub "tylko do odczytu" w ciele
  wiadomości i innych polach.

## Cortana

* Zwroty tekstowe Cortany są wypowiadane w większości sytuacjach (jeżeli nie
  są, ponownie otwórz meni start, i spróbuj ponownie).
* NVDA będzie przyciszony, gdy mówisz do Cortany.
* NVDA teraz wymawia potwierdzenie przypomnienia po jego ustawieniu.

## Centrum opinii

* Dla nowych wyda aplikacji, NVDA więcej nie będzie oznajmiało kategorię
  informacji zwrotnych dwukrotnie.

## Poczta

* Przy wyświetlaniu elementów w listy wiadomości, teraz można użyć skrótów
  dla nawigacji po tabelach, aby przeczytać nagłówki wiadomości. Miejcie na
  uwadze, że nawigacja po kolumnach (wiadomościach) jest niewspierana.
* Przy pisaniu wiadomości, istnienie podpowiedzi o wzmiankach teraz jest
  oznajmiane dzwiękami.
* W niektórych przypadkach, gdy używana jest nawigacja obiektowa, NVDA nie
  będzie się zachowywał  w sposób nijaki, albo nie będzie odtwarzał dźwięku
  błedu. Jest to teraz część NVDA 2019.1.

## Mapy

* NVDA ottwarza sygnały dźwiękowe położenia dla położenia na mapie.
* Przy użyciu trybu ulicy i jeśli opcja "użyj klawiatury" jest włączona,
  NVDA będzie wymawiać adresy ulic przy nawigacji strzałkami po mapie.

## Microsoft Edge

* Autouzupełnienie tekstu będzie śledzone i wymawiane w omnibarze.
* NVDA nie będzie już odtwarzać dźwięku podpowiedzi po naciśnięciu F11 aby
  przełączyć pełny ekran.

## Klawiatura nowoczesna

Uwaga: Większość funkcji tego dodatku jest teraz częścią NVDA 2018.3 lub
nowszej wersji.

* Wsparcie dla panelu wprowadzania emoji w wersji 1709 (zimowa aktualizacja
  dla twórców) i nowsze, włączając w to przeprojektowany panel w wersji 1809
  (kompilacja 17661 i nowsze) a także zmiany wprowadzone w wersji 19H1
  (kompilacja 18262 i nowsze, włączając w to kaomoji i kategorie znaków w
  kompilacji 18305). gdy wersja NVDA starsza niż 2018.4 jest używana, dla
  lepszych wyników, trzeba będzie używać syntezator One core. Jeżeli jest
  używana wersja NVDA 2018.4 lub nowsza,, włącz słownik danych unicode z
  dialogu ustawień mowy i ustaw wymawianie symboli na "niektóre" lub wyższy
  poziom.
* wsparcie dla podpowiedzi sprzętowych w wersji 1803 (kwietniowa
  aktualizacja) i nowszych.
* W kompilacjach po kompilacji 1709 ,  NVDA będzie wymawiało pierwszy
  wybrany emoji na liście. To jest bardziej zauważalne w kompilacji 18262 i
  nowszych gdzie panel może być otwarty w ostatniej kategorii, takiej jak
  wyświetlanie karnacji skóry, gdy kategoria ludzie jest otwarta.
* Wsparcie oznajmiania chmurowego schowka w wersji 1809 (kompilacja 17666 i
  nowszych).
* Zmniejszona niechciana gadatliwośc przy działaniach związanych z
  współczesną klawiaturą i jej funkcjami. W tym jest włączone bezpodstawne
  wymawianie "Microsoft Candidate UI" gdy otwiera się klawiatura sprzętowa
  podpowiedzi wpisywania i pozostawianie cichym przy tym, jak niektóre
  klawisze na klawiaturze wywołują zdarzenie zmiany nazwy na niektórych
  systemach.
* NVDA już nie będzie odtwarzało dźwięk błędu lub robiło nic, gdy panel
  emoji jest zamykany w bardziej ostatnich kompilacjach 19H1. To jest część
  NVDA 2019.1
* W wersji 1809 (październikowa aktualizacja 2018), NVDA będzie oznajmiało
  wyniki wyszukiwania emoji jeżeli to możliwe. To jest część NVDA 2019.1
* NVDA już nie będzie wymawiała "showek" gdy istnieją w nim elementy.
* Na niektórych komputerach na których jest uruchomiony Windows 10  1903
  (Atualizacja z maju 2019), NVDA nie będzie wydawała efekt robienia nic gdy
  panel emoji się otwiera.

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
  nowszych.
* W niektórych przypadkach, gdy używana jest nawigacja obiektowa, NVDA nie
  będzie się zachowywał  sposób nijaki, albo nie będzie odtwarzał dźwięku
  błedu.
* Okno dialogowe przypomnienia o aktualizacjach Windows, teraz jest
  rozpoznawane jako poprawne okno dialogowe.
* Nieparzyste kontrolki obecne w niektórych oknach instalacji Windows 10
  zostały poprawione.

## Sklep

* Po sprawdzaniu aktualizacji aplikacji, nazyw aplikacji w liście aplikacji
  do zaktualizowania są poprawnie oznaczone.
* Przy pobieraniu zawartości, takiej jak aplikacje i muzyka, NVDA wymówi
  nazwę produktu i pasek postępu.

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
