# Windows 10 App Essentials #

* Autorzy: Joseph Lee, Derek Riemer i Inni użytkownicy windowsa 10.
* Pobierz [wersja stabilna][1]
* Pobierz [Wersja rozwojowa][2]

Ten dodatek jest kolekcją różnych modułów aplikacji dla Windows 10, a też i
poprawek dla niektórych kontrolek w Windowsie 10.

Następujące moduły wspierające aplikacji są dołączone (sprawdź rozdział
każdej aplikacji co jest wspierane):

* Alarmy i zegar.
* Kalendarz
* Kalkulator (nowoczesny).
* Cortana
* Centrum opinii
* Pasek gry
* Poczta
* Mapy
* Microsoft Edge
* Nowoczesna klawiatura (panel emoji/podpowiedzi klawiatury
  sprzętowej/elementy schowka w chmurze w wersji 1709 i nowszych)
* Osoby
* Ustawienia (Ustawienia systemowe, Windows+I)
* Skype (aplikacja uniwersalna)
* Sklep
* Pogoda.
* Różne moduły dla takich kontrolek, jak kafelki menu start.

Uwagi:

* Uwaga: Ten dodatek wymaga Windows 10 Wersję 1703 (kompilację 15063) lub
  nowszą i NVDA 2017.3 lub nowszą. Dla lepszych wyników, trzeba będzie
  używać dodatek z najnowszą stabilną kompilacją (kompilacja 16299) lub
  17134 i ostatnią stabilną wersję NVDA. Także, po zmianie ustawień
  aktualizacji dodatku, trzeba się upewnić, czy konfiguracja jest zachowana.
* Niektóre funkcję dodatku są, lub staną się częścią czytnika ekranu NVDA.

## Ogólne

* W meni kontekstowym kafelek meni start, meni rozwijane są prawidłowo
  rozpoznawane.
* Większość okien dialogowych teraz są rozpoznawalne jako prawdziwe okna
  dialogowe, włączając w to okna dialogowe w wersjach testowych (settings
  app).
* NVDA może ogłaszać liczbę wypowiedzi przy wyszukiwaniu w wielu
  przypadkach. Ta opcja jest kontrolowana przez opcję "odczytuj położenie
  obiektu" w panelu "prezentacja obiektu".
* W większości meni kontekstowych (tak jak w Microsoft Edge), informacja o
  położeniu (NP. 1 z 2) więcej nie jest odczytywana.
* Następujące zdarzenia UIA są rospoznawalne: Controller for, drag start,
  drag cancel, drag complete, element selected, live region change,
  notification, system alert, tooltip opened, window opened. Te zdarzenia
  będą śledzone, gdy NVDA jest włączone w trybie debugowania.
* Dodana możliwość sprawdzania aktualizacji dodatku (automatycznie lub
  ręcznie) poprzez nowe okno dialogowe Windows 10 App Essentials, które
  można znaleźć w meni NvDA meni ustawienia. Domyślnie, wersje stabilne i
  rozwojowe będą sprawdzane pod kątem nowych aktualizacji codziennie lub
  tygodniowo.
* W niektórych aplikacjach, tekst żywego regionu jest wypowiadany. W tym są
  włączone powiadomienia w Microsoft Edge i innych. Proszę mieć na uwadze,
  że to może skutkować podwójne wymawianie w niektórych przypadkach.
* Powiadomienia z nowych wersji aplikacji w Windows 10 wersji 1709
  (kompilacja 16299) i nowszych są wymawiane. Z powodu ograniczen
  technicznych, ta funkcja działa poprawnie w wersji NVDA 2018.1 i nowszych.
* Opisy obiektów w Edge i innych aplikacjach UWP są rozpoznawane  i będą
  czytane automatycznie.
* NVDA już nie będzie wymawiać "nieznane" gdy jtwierany jest meni szybkiego
  łącza (Windows+X). ta poprawka jest częścią NVDA 2018.2.
* w kompilacji 17627 i nowszych, gdy nowa karta sets jest otwierana
  (Control+Windows+T), NVDA będzie oznajmiało wyniki cortany.
* Przy przełączaniu pomiędzy kartami właściwości sets, NVDA będzie wymawiało
  nazwę i pozycję karty właściwości.
* otwierając, zamykając lub przełączając się między wirtualnymi pulpitami,
  NVDA będzie oznajmiało aktualny identyfikator (na przykład pulpit 2).
* NVDA nie będzie wypowiadało wielkość tekstu w meni start, gdy zmienia się
  rozdzielczość ekranu lub orientacja ekranu.

## Alarmy i zegar

* Teraz są wypowiadane kontrolki wypowiadania czasu, zauważalne przy
  poruszaniu się po nich. To także dotyczy kontrolki wyboru czasu ponownego
  uruchomienia po instalacji aktualizacji.

## Kalkulator

* Kiedy enter albo escape jest wciśnięty, NVDA wymawia wynik obliczenia.
* Dla wyliczeń, takich jak przetwarzanie jednostek lub waluty, NVDA
  automatycznie będzie wymawiało wyniki obliczenia

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

## Pasek gry

* NVDA będzie powiadamiał o istnieniu paska do gier w danym momencie,
  interakcja z przyczyn technicznych z tą kontrolą nie jest możliwa.

## Poczta

* Przy wyświetlaniu elementów w liście wiadomości, teraz można użyć skrótów
  dla nawigacji po tabelach, aby przeczytać nagłówki wiadomości.
* Przy pisaniu wiadomości, istnienie podpowiedzi o wzmiankach teraz jest
  oznajmiane dzwiękami.

## Mapy

* NVDA ottwarza sygnały dźwiękowe położenia dla położenia na mapie.
* Przy użyciu trybu ulicy i jeśli opcja "użyj klawiatury" jest włączona,
  NVDA będzie wymawiać adresy ulic przy nawigacji strzałkami po mapie.

## Microsoft Edge

* Powiadomienia, takie jak pobierania plików i różne ostrzeżenia na stronach
  webowychsą oznajmiane.

## Klawiatura nowoczesna

* Wsparcie dla pływającego panelu wprowadzania Emoji w kompilacji 16215 lub
  nowszej, włączając w to 17661 i nowszych (dla lepszych wyników trzeba
  używać syntezatora mowy OneCore, czyli Microsoft sapi mobile).
* wsparcie dla podpowiedzi sprzętowych w wersji 1803 (kwietniowa
  aktualizacja) i nowszych.
* W kompilacjach po kompilacji 1709, NVDA będzie oznajmiać pierwszy wybrany
  emoji, przy oznajmianiu panelu emoji.
* Wsparcie dla oznajmiania elementów schowka w chmurze w kompilacji 17666
  (Redstone 5) i nowszych.

## Osoby

* Przy wyszukiwaniu kontaktów, dźwięk będzie ottwarzany, jeżeli istnieją
  wyniki wyszukiwania.

## Ustawienia

* Większość informacji, takich jak pasek stanu w Windows update, będzie
  wypowiadany automatycznie.
* Wartości paska postępu i inne informacje, nie są wypowiadane
  automatycznie.
* Grupy ustawień są rpspoznawane przy użyciu nawigacji obiektowej aby było
  można poruszać się pomięcy kontrolkami.
* Dla niektórych pól kombi, NVDA będzie wykrywał nazwę oraz wypowiadał
  zmiany wartości. Poprawka zmiany wartości jest wprowadzona w wersji NVDA
  2017.3.
* Dzwięki paska postępu głośności nie są więcej słyszane w kompilacji 1803 i
  nowszych.

## Skype

* Powiadomienie o pisaniu będzie wypowiadane, tak jak i w Skype dla pulpitu.
* Połowicznie przywróciły komendy Ctrl+NvDA+komendy na rzędzie cyfrowym aby
  móc przeczytać ostatnią historię czatu, a także  aby móc przemieśczać
  obiekt nawigatora do poszczególnej wiadomości jak i w skype dla pulpitu.
* Teraz można nacisnąć Alt+rząd cyfrowy aby móc znaleźć i przemieszczać się
  między  czatami (1), kontaktami (2), botami (3) i polem do wpisywania
  wiadomości jeżeli jest widoczne (4). Uwaga, te skróty będą poprawnie
  działać, jeżeli aktualizacja skypea wydana w marcu 2017 jest
  zainstalowana.
* Oznaczenia pól kombi dla aplikacji Skype preview wydanej w listopadzie
  2016 są wypowiadane.
* NVDA dla większości sytuacji nie będzie wypowiadał "Skype Message" przy
  przeglądaniu wiadomości.
* Różne błędy przy używaniu Skype za pomocą linijek brajlowskich są teraz
  poprawione, włączając w to niemożliwość czytania wiadomości za pomocą
  brajla.
* Z listy historii wiadomości, wciskając NVDA+D teraz wypowiada typ kanału,
  datę wiadomości i tak dalej.

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
