# Windows 10 App Essentials #

* Autorzy: Joseph Lee, Derek Riemer i Inni użytkownicy windowsa 10.
* Pobierz [wersja stabilna][1]
* Pobierz [Wersja rozwojowa][2]
* Zgodność z wersjami NVDA: 2019.3 i nowsze
* Pobierz [Wersję starszą][4] zgodna z NVDA 2019.2.1 i starszymi

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
* Modern keyboard (emoji panel/dictation/hardware input suggestions/cloud
  clipboard history/modern input method editors)
* Osoby
* Ustawienia (Ustawienia systemowe, Windows+I)
* Pogoda.
* Różne moduły dla takich kontrolek, jak kafelki meni start.

Uwagi:

* This add-on requires Windows 10 Version 1809 (build 17763) or later and
  NVDA 2019.3 or later. For best results, use the add-on with latest Windows
  10 stable release (build 18363) and latest stable version of NVDA.
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
* NVDA will no longer announce "blank" when pressing up or down arrow to
  open all apps views in Start menu. This is now part of NVDA 2019.3.
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
* Tooltips from Edge and universal apps are recognized and will be
  announced. This is now part of NVDA 2019.3.
* Podczas otwierania, zamykając lub przełączając się między wirtualnymi
  pulpitami, NVDA będzie oznajmiała aktualny identyfikator (na przykład
  pulpit 2).
* NVDA nie będzie wypowiadało wielkość tekstu w meni start, gdy zmienia się
  rozdzielczość ekranu lub orientacja ekranu.
* App name and version for various Microsoft Store apps are now shown
  correctly. This is now part of NVDA 2019.3.
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
* In Version 1909 (November 2019 Update) and later, modern search experience
  in File Explorer powered by Windows Search user interface is supported.

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

* Text auto-complete will be tracked and announced in address omnibar. This
  is now part of NVDA 2019.3.
* NVDA will no longer play suggestion sound when pressing F11 to toggle full
  screen. This is now part of NVDA 2019.3.
* Removed suggestions sound playback for address omnibar. This is now part
  of NVDA 2019.3.

## Microsoft Store

* Po sprawdzaniu aktualizacji aplikacji, nazyw aplikacji w liście aplikacji
  do zaktualizowania są poprawnie oznaczone.
* Przy pobieraniu zawartości, takiej jak aplikacje i muzyka, NVDA wymówi
  nazwę produktu i pasek postępu.

## Klawiatura nowoczesna

This includes emoji panel, clipboard history, dictation, hardware input
suggestions, and modern input method editors for certain languages. When
viewing emojis, for best experience, enable Unicode Consortium setting from
NvDA's speech settings and set symbol level to "some" or higher.

* Support for Emoji input panel in Version 1709 (Fall Creators Update) and
  later, including redesigned panel in Version 1809 (build 17661 and later)
  and changes made in Version 1903 (build 18262 and later, including kaomoji
  and symbols categories in build 18305). This is also applicable in Version
  2004 (build 18963 and later) as the app has been renamed. All of these
  changes are now part of NVDA 2019.3.
* When opening clipboard history, NVDA will no longer announce "clipboard"
  when there are items in the clipboard under some circumstances.
* Na niektórych komputerach na których jest uruchomiony Windows 10  1903
  (Aktualizacja z maju 2019), NVDA nie będzie wydawała efekt robienia nic
  gdy panel emoji się otwiera.
* Added support for modern Chinese, Japanese, and Korean (CJK) IME
  candidates interface introduced in Version 2004 (build 18965 and later).

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
* Audio Volume progress bar beeps are no longer heard in Version 1803 and
  later. This is now part of NVDA 2019.3.
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

[4]: https://addons.nvda-project.org/files/get.php?file=w10-2019
