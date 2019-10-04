# Windows 10 App Essentials #

* Autorzy: Joseph Lee, Derek Riemer i Inni użytkownicy windowsa 10.
* Pobierz [wersja stabilna][1]
* Pobierz [Wersja rozwojowa][2]
* Zgodność z wersjami NVDA: 2019.1 do 2019.2

Ten dodatek jest kolekcją różnych modułów aplikacji dla Windows 10, jak
również ulepszeń i poprawek dla niektórych kontrolek w tym systemie.

Dołączone są następujące moduły wspierające aplikacje (sprawdź rozdział
każdej aplikacji, aby dokładnie sprawdzić co jest wspierane):

* Kalkulator (nowoczesny).
* Kalendarz
* Cortana (Classic and Conversations)
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
  nowszej i NVDA 2019.1 lub nowszej. Aby uzyskać najlepsze wyniki, należy
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
* Teraz jest możliwe śledzenie zdarzeń z określonych oraz specyficznych
  aplikacji.
* Opisy obiektów w Edge i innych aplikacjach UWP są rozpoznawane  i będą
  czytane automatycznie. To będzie częścią NVDA 2019.3.
* Podczas otwierania, zamykając lub przełączając się między wirtualnymi
  pulpitami, NVDA będzie oznajmiała aktualny identyfikator (na przykład
  pulpit 2).
* NVDA nie będzie wypowiadało wielkość tekstu w meni start, gdy zmienia się
  rozdzielczość ekranu lub orientacja ekranu.
* W wersji 1903 (aktualizacji majowej 2019), NVDA będzie oznajmiał zmiany
  głośności i jasności od razu, gdy jest się fokusowanyw na oknie
  eksploratora windows. Jest to teraz część NVDA 2019.2.
* App name and version for various Microsoft Store apps are now shown
  correctly. This will be part of NVDA 2019.3.

## Kalkulator

* When ENTER or Escape is pressed, NVDA will announce calculation results.
* Dla wyliczeń, takich jak przetwarzanie jednostek lub waluty, NVDA
  automatycznie będzie wymawiało wyniki obliczenia
* NVDA nie będzie więcej wymawiało "nagłówek" dla wyników kalkulatora.
* NVDA powiadomi, jeżeli ilość liczb osiągnie maksymalną wartość przy
  wpisywaniu wyrażenia.
* Dodano wsparcie trybu  "zawsze włączony", dla przyszłych wersji
  kalkulatora.

## Kalendarz

* NVDA nie wymawia więcej "pole edycji" lub "tylko do odczytu" w ciele
  wiadomości i innych polach.

## Cortana

Most items are no longer applicable on Version 1903 and later. Classic
Cortana refers to older Cortana interface which was part of Start menu.

* Textual responses from Cortana (both Classic and Conversations UI) are
  announced in most situations (if using Classic Cortana, reopen Start menu
  and try searching again if responses are not announced).
* NVDA będzie przyciszony, gdy mówisz do Cortany.
* In Classic Cortana, NVDA will announce reminder confirmation after you set
  one.
* w kompilacji 18945 i nowszych, wspierany jest nowy interfejs wyszukiwania
  cortana w eksploratorze plików.

## Centrum opinii

* Dla nowych wyda aplikacji, NVDA więcej nie będzie oznajmiało kategorię
  informacji zwrotnych dwukrotnie.

## Poczta

* Przy wyświetlaniu elementów w listy wiadomości, teraz można użyć skrótów
  dla nawigacji po tabelach, aby przeczytać nagłówki wiadomości. Miejcie na
  uwadze, że nawigacja po kolumnach (wiadomościach) jest niewspierana.
* Przy pisaniu wiadomości, istnienie podpowiedzi o wzmiankach teraz jest
  oznajmiane dzwiękami.
* NVDA nie będzie robiło nic, lub odtwarzało dźwięk błędu, gdyy ta aplikacja
  jest zamknięta. Ta funkcja jest teraz częścią NVDA 2019.2.

## Mapy

* NVDA ottwarza sygnały dźwiękowe położenia dla położenia na mapie.
* Przy użyciu trybu ulicy i jeśli opcja "użyj klawiatury" jest włączona,
  NVDA będzie wymawiać adresy ulic przy nawigacji strzałkami po mapie.

## Microsoft Edge

This refers to classic EdgeHTML-based Microsoft Edge.

* Text auto-complete will be tracked and announced in address omnibar. This
  will be part of NVDA 2019.3.
* NVDA will no longer play suggestion sound when pressing F11 to toggle full
  screen. This will be part of NVDA 2019.3.
* Removed suggestions sound playback for address omnibar. This will be part
  of NVDA 2019.3.

## Microsoft Store

* Po sprawdzaniu aktualizacji aplikacji, nazyw aplikacji w liście aplikacji
  do zaktualizowania są poprawnie oznaczone.
* Przy pobieraniu zawartości, takiej jak aplikacje i muzyka, NVDA wymówi
  nazwę produktu i pasek postępu.

## Klawiatura nowoczesna

Most features below are now part of NVDA 2018.3 or later.

* Support for Emoji input panel in Version 1709 (Fall Creators Update) and
  later, including the redesigned panel in Version 1809 (build 17661 and
  later) and changes made in 19H1 (build 18262 and later, including kaomoji
  and symbols categories in build 18305). This is also applicable in build
  18963 and later as the app has been renamed. If using NVDA releases
  earlier than 2018.4, for best experience when reading emojis, use Windows
  OneCore speech synthesizer. If 2018.4 or later is in use, enable Unicode
  Consortium setting from NvDA's speech settings and set symbol level to
  "some" or higher.
* NVDA już nie będzie wymawiała "showek" gdy istnieją w nim elementy.
* Na niektórych komputerach na których jest uruchomiony Windows 10  1903
  (Atualizacja z maju 2019), NVDA nie będzie wydawała efekt robienia nic gdy
  panel emoji się otwiera.
* Added support for modern Chinese, Japanese, and Korean (CJK) IME
  candidates interface introduced in 20H1 build 18965 and later.

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
