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
* Pasek gry
* Poczta
* Mapy
* Microsoft Edge
* Osoby
* Ustawienia (Ustawienia systemowe, Windows+I)
* Skype (aplikacja uniwersalna)
* Sklep
* Pogoda.
* Różne moduły dla takich kontrolek, jak kafelki menu start.

Uwaga: Ten dodatek wymaga Windows 10 Wersję 1607 (kompilację 14393) lub
nowszą i NVDA 2017.3 lub nowszą. Dla lepszych wyników, trzeba będzie używać
dodatek z najnowszą stabilną kompilacją (kompilacja 16299) i ostatnią
stabilną wersję NVDA. Także, po zmianie ustawień aktualizacji dodatku,
trzeba się upewnić, czy konfiguracja jest zachowana.

Ważna informacja dotycząca NVDA 2017.3: ze względu wstecznie niezgodnych
zmian  w NVDA 2017.3, wersja dodatku 17.09 i nowsze, nie będą działały z
wersjami starszymi niż 2017.3.

## Ogólne

* W meni kontekstowym kafelek meni start, meni rozwijane są prawidłowo
  rozpoznawane.
* Większość okien dialogowych teraz jest rospoznawana jako właściwie
  dialogi. Te dialogi stanowią na przykład: okno dialogowe insider preview
  (aplikacja ustawienia) i nowe stylizowane okno dialogowe kontroli kont
  użytkownika w kompilacji i nowszych dla NvDA 2016.2.1 i starsze.
* pojawianie się/zamykanie podpowiedzi dla niektórych pól wyszukiwania
  (zauważalne w aplikacjach Ustawienia i Sklep) są wymawiane i wyświetlane
  na monitorze brajlowskim. To również dotyczy pola edycyjnego w meni
  start. To usprawnienie jest częścią NVDA 2017.3.
* NVDA może ogłaszać liczbę wypowiedzi przy wyszukiwaniu w wielu
  przypadkach. Ta opcja jest kontrolowana przez opcję "odczytuj położenie
  obiektu" w oknie dialogowym "prezentacja obiektu".
* W większości meni kontekstowych (tak jak w Microsoft Edge), informacja o
  położeniu (NP. 1 z 2) więcej nie jest odczytywana.
* Następujące zdarzenia UIA są rospoznane: Controller for, live region
  change, system alert, element selected, window opened. Z NVDA ustawioną na
  tryb debugowania, te zdarzenia będą śledzone.
* Dodana możliwość sprawdzania aktualizacji dodatku (automatycznie lub
  ręcznie) poprzez nowe okno dialogowe Windows 10 App Essentials, które
  można znaleźć w meni NvDA meni ustawienia. Domyślnie, wersje stabilne i
  rozwojowe będą sprawdzane pod kątem nowych aktualizacji codziennie lub
  tygodniowo.
* Możliwość śledzenia zdarzeń z aplikacji ujednoliconej platformy Windows
  (UWP) jeżeli NVDA jest uruchomione w trybie debugowania (2017.1 lub
  nowsze).
* Wsparcie dla pływającego panelu wprowadzania Emoji w kompilacji 16215 lub
  nowszej (dla lepszych wyników trzeba używać syntezatora mowy OneCore,
  czyli Microsoft sapi mobile).
* W niektórych aplikacjach, tekst żywego regionu jest wypowiadany. W tym są
  włączone powiadomienia w Microsoft Edge i innych. Proszę mieć na uwadze,
  że to może skutkować podwójne wymawianie w niektórych
  przypadkach. Niektóre takie zdarzenia są imvlementowane w NVDa 20ag.c.
* Powiadomienia nie są wymawiane wiele razy w aktualizacji dla twórców i
  nowszych aktualizacjach. To usprawnienie jest teraz częścią NVDA 2017.3. 

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
  webowychsą oznajmiane. Niektóre takie scenariusze są częścią NVDA 2017.3.

## Osoby

* Przy wyszukiwaniu kontaktów, dźwięk będzie ottwarzany, jeżeli istnieją
  wyniki wyszukiwania.

## Ustawienia

* Większość informacji, tak jak pasek stanu w Windows update, będzie
  wypowiadany automatycznie. Większość tych informacji będzie wypowiadana
  przez NVDA 2017.3
* Wartości paska postępu i inne informacje, nie są wypowiadane
  automatycznie.
* Jeżeli wyszukiwanie ustawień trwa dłużej niż zwykle, NVDA będzie wymawiał
  "wyszukiwanie", oraz wynik wyszukiwania, jeżeli istnieje. To usprawnienie
  jest teraz częścią NVDA 2017.3.
* Grupy ustawień są rpspoznawane przy użyciu nawigacji obiektowej aby było
  można poruszać się pomięcy kontrolkami.
* Dla niektórych pól kombi, NVDA będzie wykrywał nazwę oraz wypowiadał
  zmiany wartości. Poprawka zmiany wartości jest wprowadzona w wersji NVDA
  2017.3.

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
* Istnienie podpowiedzi wyszukiwania teraz jest oznajmiane. To usprawnienie
  jest teraz częścią NVDA 2017.3
* Przy pobieraniu zawartości, takiej jak apliakacje i muzyka, NVDA wymówi
  nazwę produktu i pasek postępu. Podstawowa poprawka jest teraz częscią
  NVDA 2017.3.

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
