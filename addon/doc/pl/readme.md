# Windows 10 App Essentials #

* Autorzy: Joseph Lee, Derek Riemer i Inni użytkownicy windowsa 10.
* Pobierz [wersja stabilna][1]
* Pobierz [Wersja rozwojowa][2]

Ten dodatek jest kolekcją różnych modułów aplikacji dla Windows 10, jak
również ulepszeń i poprawek dla niektórych kontrolek w tym systemie.

Dołączone są następujące moduły wspierające aplikacje (sprawdź rozdział
każdej aplikacji, aby dokładnie sprawdzić co jest wspierane):

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

* Uwaga! Ten dodatek wymaga Windowsa 10 Wersji 1709 (kompilacji 16299) lub
  nowszej i NVDA 2018.2 lub nowszej. Aby uzyskiwać najlepsze wyniki, należy
  używać dodatku z najnowszą stabilną kompilacją systemu (kompilacja 17134)
  i najnowszą stabilną wersją NVDA. 
* Niektóre funkcję dodatku są, lub staną się częścią czytnika ekranu NVDA.
* Dla wpisów nie podanych poniżej, można wnioskować, że zostały one
  wprowadzone do NVDA. Nie można ich już zastosować, ponieważ dodatek nie
  wspiera starszych wydań systemu, lub aplikacje są zmienione w taki sposób,
  że te wpisy są unieważnione.

Dla listy zmian pomiędzy kolejnymi wersjami, prosimy przeczytać [listę zmian
dla wersji dodatku][3].

## Ogólne

* Elementy menu rozwijanego są prawidłowo rozpoznawane w różnych
  aplikacjach, włączając w to menu kontekstowe dla kafelków meni start, a
  także menu aplikacji dla Microsoft Edge (Redstone 5).
* Niektóre okna dialogowe są od teraz prawidłowo rozpoznawane i wymawiane
  jako okna dialogowe. Są to np. okna dialogowe w wersjach testowych
  (settings app). W NVDA 2018.3, będzie to już wbudowane w sam czytnik
  ekranu.
* W wielu przypadkach, NVDA może ogłaszać liczbę sugestii wyszukiwania. Ta
  opcja jest kontrolowana przez opcję "odczytuj położenie obiektu" w panelu
  "prezentacja obiektu".
* W większości menu kontekstowych (tak jak w Microsoft Edge), informacja o
  położeniu (NP. 1 z 2) nie jest już odczytywana.
* Następujące zdarzenia UIA są rozpoznawane: active text position change,
  controller for, drag start, drag cancel, drag complete, element selected,
  live region change, notification, system alert, tooltip opened, window
  opened. Gdy w NVDA jest włączony tryb debugowania, te zdarzenia będą
  śledzone, natomiast, dla UIA zdarzenia UIA notification event, dźwięk
  debugowania będzie odtwarzany jeżeli powiadomienie przykodzi z innej
  aplikacji niż ta aktywna.
* Dodana możliwość sprawdzania aktualizacji dodatku (automatycznie lub
  ręcznie) poprzez nowe okno dialogowe Windows 10 App Essentials, które
  można znaleźć w meni NvDA meni ustawienia. Domyślnie, wersje stabilne i
  rozwojowe będą sprawdzane pod kątem nowych aktualizacji codziennie lub
  tygodniowo.
* W niektórych aplikacjach, tekst żywego regionu jest wypowiadany. Są to
  m.in. powiadomienia w Microsoft Edge (włącznie z elementami oznaczonymi
  aria-role=aler), czy wyniki w kalkulatorze. Proszę mieć na uwadze, że w
  niektórych przypadkach może to skutkować podwójnym wymawianiem. Jest to
  wbudowane w NVDA 2017.3 i nowsze.
* Powiadomienia z nowych wersji aplikacji w Windows 10 wersji 1709
  (kompilacja 16299) i nowszych są wymawiane. NVDA wspiera to od wersji
  2018.2. Ponadto, NVDA 2018.3 wspiera jeszcze więcej powiadomień.
* Opisy obiektów w Edge i innych aplikacjach UWP są rozpoznawane  i będą
  czytane automatycznie.
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
* NVDA nie będzie więcej wymawiało "nagłówek" dla wyników kalkulatora.

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

* NVDA będzie powiadamiał o istnieniu paska do gier Z przyczyn technicznych,
  interakcja z tą kontrolką możliw jest tylko aczynając od wersji 17723.

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
  webowych są oznajmiane. także oznajmiane jest dostępność trybu czytania (
  wersja 1709

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
* Zmniejszona niechciana gadatliwośc przy działaniach związanych z
  współczesną klawiaturą i jej funkcjami. W tym jest włączone bezpodstawne
  wymawianie "Microsoft Candidate UI" gdy otwiera się klawiatura sprzętowa
  podpowiedzi wpisywania i pozostawianie cichym przy tym, jak niektóre
  klawisze na klawiaturze wywołują zdarzenie zmiany nazwy na niektórych
  systemach.

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
* Więcej komunikatów o stanie Windows Update są wypowiadane, najważniejsze,
  gdy Windows update zobaczy błąd.

## Skype

* Powiadomienie o pisaniu będzie wypowiadane, tak jak i w Skype dla pulpitu.
* Control+NvDA+komendy rzędu cyfr, używane do odczytywania wiadomości w
  czacie skypea a także do przemieszczania obiektu nawitaora do nich są
  także dostępne w skype dla UWP.
* Teraz można nacisnąć Alt+rząd cyfrowy aby móc znaleźć i przemieszczać się
  między  czatami (1), kontaktami (2), botami (3) i polem do wpisywania
  wiadomości jeżeli jest widoczne (4). Uwaga, te skróty będą poprawnie
  działać, jeżeli aktualizacja skypea wydana w marcu 2017 jest
  zainstalowana.
* NVDA dla większości sytuacji nie będzie wypowiadał "Skype Message" przy
  przeglądaniu wiadomości.
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

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
