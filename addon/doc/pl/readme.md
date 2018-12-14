# Windows 10 App Essentials #

* Autorzy: Joseph Lee, Derek Riemer i Inni użytkownicy windowsa 10.
* Pobierz [wersja stabilna][1]
* Pobierz [Wersja rozwojowa][2]
* Zgodność z wersjami NVDA: 2018.3 do 2019.1

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
* Różne moduły dla takich kontrolek, jak kafelki meni start.

Uwagi:

* This add-on requires Windows 10 Version 1709 (build 16299) or later and
  NVDA 2018.3 or later. For best results, use the add-on with latest Windows
  10 stable release (build 17763) and latest stable version of NVDA.
* Niektóre funkcję dodatku są, lub staną się częścią czytnika ekranu NVDA.
* Dla wpisów nie podanych poniżej, można wnioskować, że zostały one
  wprowadzone do NVDA. Nie można ich już zastosować, ponieważ dodatek nie
  wspiera starszych wydań systemu, lub aplikacje są zmienione w taki sposób,
  że te wpisy są unieważnione.

Aby zobaczyć listę zmian pomiędzy kolejnymi wersjami, prosimy przeczytać
[listę zmian dla wersji dodatku][3].

## Ogólne

* Zmiany wewnętrzne czyniące dodatek zgodnym z przyszłymi wersjami NVDA.
* Jeśli dodatek "Add-on Updater" jest zainstalowany, ten dodatek będzie
  sprawdzał aktualizacje dadatku Win 10 app essentials.
* Domyślny czas sprawdzania aktualizacji został zmieniony na aktualizacje
  tygodniowe dla wersji stabilnych i rozwojowych. To jest stosowane, gdy
  dodatek sam sprawdza aktualizacje.
* Jeżeli dodatek jest ustawiony tak, aby sprawdzał aktualizacje, przy
  aktualizacji, jeżeli dodatek wymaga nowszej wersji NVDA, komunikat o
  błędzie będzie pokazany.
* Drobne zmiany w pokazywanych wiadomościach w innych językach niż
  angielski.
* Elementy meni rozwijanego są prawidłowo rozpoznawane w różnych
  aplikacjach, takich jak menu kontekstowe dla kafelków meni start, a także
  menu aplikacji dla Microsoft Edge (Redstone 5).
* Certain dialogs are now recognized as proper dialogs and reported as such,
  including Insider Preview dialog (settings app). This is now part of NVDA
  2018.3.
* W wielu przypadkach, NVDA może ogłaszać liczbę sugestii wyszukiwania. Ta
  opcja jest kontrolowana przez opcję "odczytuj położenie obiektu" w panelu
  "prezentacja obiektu".
* W większości meni kontekstowych (tak jak w Microsoft Edge), informacja o
  położeniu (NP. 1 z 2) nie jest już odczytywana.
* The following UIA events are recognized: active text position change,
  controller for, drag start, drag cancel, drag complete, element selected,
  item status, live region change, notification, system alert, tooltip
  opened, window opened. With NVDA set to run with debug logging enabled,
  these events will be tracked, and for UIA notification event, a debug tone
  will be heard if notifications come from somewhere other than the
  currently active app.
* Powiadomienia z nowych wersji aplikacji w Windows 10 wersji 1709
  (kompilacja 16299) i nowszych są wymawiane. NVDA wspiera to od wersji
  2018.2. Ponadto, NVDA 2018.3 wspiera jeszcze więcej powiadomień.
* Opisy obiektów w Edge i innych aplikacjach UWP są rozpoznawane  i będą
  czytane automatycznie.
* Podczas otwierania, zamykając lub przełączając się między wirtualnymi
  pulpitami, NVDA będzie oznajmiało aktualny identyfikator (na przykład
  pulpit 2).
* NVDA nie będzie wypowiadało wielkość tekstu w meni start, gdy zmienia się
  rozdzielczość ekranu lub orientacja ekranu.

## Centrum powiadomień

* Szybka akcja jasności została zmieniona z przycisku przełączającego na
  przycisk zwykły.
* Róźne zmiany stanu, takie jak asysta punktu uwagi i jasność będą
  wymawiane.

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

* Powiadomienia, takie jak pobierania plików i różne ostrzeżenia na stronach
  webowych są oznajmiane. także oznajmiane jest dostępność trybu czytania (
  wersja 1709
* Autouzupełnienie tekstu będzie śledzone i wymawiane w omnibarze.

## Klawiatura nowoczesna

Uwaga: Większość funkcji tego dodatku jest teraz częścią NVDA 2018.3.

* Support for Emoji input panel in Version 1709 (Fall Creators Update) and
  later, including the redesigned panel in Version 1809 (build 17661 and
  later) and changes made in 19H1 (build 18262). For best experience when
  reading emojis, use Windows OneCore speech synthesizer.
* wsparcie dla podpowiedzi sprzętowych w wersji 1803 (kwietniowa
  aktualizacja) i nowszych.
* In post-1709 builds, NVDA will announce the first selected emoji when
  emoji panel opens. This is more noticeable in build 18262 and later where
  emoji panel may open to last browsed category, such as Wyświetlanie
  modyfikatoru karnacji skóry gdy kategoria ludzie jest otwarta.
* Wsparcie oznajmiania chmurowego schowka w wersji 1809 (kompilacja 17666 i
  nowszych).
* Zmniejszona niechciana gadatliwośc przy działaniach związanych z
  współczesną klawiaturą i jej funkcjami. W tym jest włączone bezpodstawne
  wymawianie "Microsoft Candidate UI" gdy otwiera się klawiatura sprzętowa
  podpowiedzi wpisywania i pozostawianie cichym przy tym, jak niektóre
  klawisze na klawiaturze wywołują zdarzenie zmiany nazwy na niektórych
  systemach.
* NVDA już nie będzie odtwarzało dźwięk błędu lub nie robiło nic w bardziej
  aktualnych kompilacjach insider preview.
* NVDA będzie oznajmiało wyniki wyszukiwania emoji jeżeli to możliwe.

## Osoby

* Przy wyszukiwaniu kontaktów, dźwięk będzie ottwarzany, jeżeli istnieją
  wyniki wyszukiwania.

## Ustawienia

* Większość informacji, takich jak pasek stanu w Windows update, będzie
  wypowiadany automatycznie, włączając w to widget czujnika pamięci.
* Wartości paska postępu i inne informacje, nie są wypowiadane
  automatycznie.
* Grupy ustawień są rpspoznawane przy użyciu nawigacji obiektowej aby było
  można poruszać się pomięcy kontrolkami.
* Dla niektórych list rozwijanych i przycisków opcji, NVDA będzie wykrywał
  nazwę oraz wypowiadał zmiany wartości. 
* Dzwięki paska postępu głośności nie są więcej słyszane w kompilacji 1803 i
  nowszych.
* Więcej komunikatów o stanie Windows Update są wypowiadane, najważniejsze,
  gdy Windows update zobaczy błąd.
* NVDA will no longer appear to do nothing or play error tones if using
  object navigation commands under some circumstances.
* Various links added in build 18282 with no labels now have labels.
* Windows Update reminder dialog is recognized as a proper dialog.

## Skype

Note: the below entries won't work properly in Skype 14 universal app.

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
