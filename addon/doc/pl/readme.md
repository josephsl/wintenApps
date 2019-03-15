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

* This add-on requires Windows 10 Version 1803 (build 17134) or later and
  NVDA 2018.3 or later. For best results, use the add-on with latest Windows
  10 stable release (build 17763) and latest stable version of NVDA.
* Niektóre funkcję dodatku są, lub staną się częścią czytnika ekranu NVDA.
* For entries not listed below, you can assume that features are part of
  NVDA, no longer applicable as the add-on does not support old Windows 10
  releases, or changes were made to Windows 10 and apps that makes entries
  no longer applicable.

Aby zobaczyć listę zmian pomiędzy kolejnymi wersjami, prosimy przeczytać
[listę zmian dla wersji dodatku][3].

## Ogólne

* NVDA will no longer play error tones or do nothing if this add-on becomes
  active from Windows 7 and 8.1.
* Elementy meni rozwijanego są prawidłowo rozpoznawane w różnych
  aplikacjach, takich jak menu kontekstowe dla kafelków meni start, a także
  menu aplikacji dla Microsoft Edge (Redstone 5).
* In addition to dialogs recognized by NVDA, more dialogs are now recognized
  as proper dialogs and reported as such, including Insider Preview dialog
  (settings app).
* NVDA can announce suggestion count when performing a search in majority of
  cases. This option is controlled by "Report object position information"
  in Object presentation panel found in NVDA settings.
* W większości meni kontekstowych (tak jak w Microsoft Edge), informacja o
  położeniu (NP. 1 z 2) nie jest już odczytywana.
* Następujące zdarzenia UIA są rozpoznawane: active text position change,
  controller for, drag start, drag cancel, drag complete, element selected,
  item status, live region change, notification, system alert, tooltip
  opened, window opened. Gdy w NVDA jest włączony tryb debugowania, te
  zdarzenia będą śledzone. Natomiast dla UIA, zdarzenia UIA notification
  event, dźwięk debugowania będzie odtwarzany jeżeli powiadomienie
  przychodzi z innej aplikacji niż ta aktywna.
* Opisy obiektów w Edge i innych aplikacjach UWP są rozpoznawane  i będą
  czytane automatycznie.
* Podczas otwierania, zamykając lub przełączając się między wirtualnymi
  pulpitami, NVDA będzie oznajmiało aktualny identyfikator (na przykład
  pulpit 2).
* NVDA nie będzie wypowiadało wielkość tekstu w meni start, gdy zmienia się
  rozdzielczość ekranu lub orientacja ekranu.
* In build 18323 and later, NVDA will now announce audio volume and
  brightness changes.

## Centrum powiadomień

* Brightness quick action is now a button instead of a toggle button. This
  will be part of NVDA 2019.1.
* Various status changes such as Focus Assist and Brightness will be
  reported. This will be part of NVDA 2019.1.

## Alarmy i zegar

* Time picker values are now announced, noticeable when moving focus to
  picker controls. This also affects the control used to select when to
  restart to finish installing Windows updates. This will be part of NVDA
  2019.1.

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

## Poczta

* Przy wyświetlaniu elementów w listy wiadomości, teraz można użyć skrótów
  dla nawigacji po tabelach, aby przeczytać nagłówki wiadomości. Miejcie na
  uwadze, że nawigacja po kolumnach (wiadomościach) jest niewspierana.
* Przy pisaniu wiadomości, istnienie podpowiedzi o wzmiankach teraz jest
  oznajmiane dzwiękami.
* NVDA will no longer do anything or play error tones after closing this
  app.

## Mapy

* NVDA ottwarza sygnały dźwiękowe położenia dla położenia na mapie.
* Przy użyciu trybu ulicy i jeśli opcja "użyj klawiatury" jest włączona,
  NVDA będzie wymawiać adresy ulic przy nawigacji strzałkami po mapie.

## Microsoft Edge

* Autouzupełnienie tekstu będzie śledzone i wymawiane w omnibarze.
* NVDA will no longer play suggestion sound when pressing F11 to toggle full
  screen.

## Klawiatura nowoczesna

Note: most features below are now part of NVDA 2018.3 or later.

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
* NVDA will no longer play error tones or do nothing when closing emoji
  panel in more recent 19H1 Insider Preview builds. This will be part of
  NVDA 2019.1.
* In Version 1809 (October 2018 Update) and later, NVDA will announce search
  results for emojis if possible. This will be part of NVDA 2019.1.

## Osoby

* Przy wyszukiwaniu kontaktów, dźwięk będzie ottwarzany, jeżeli istnieją
  wyniki wyszukiwania.

## Ustawienia

* Większość informacji, takich jak pasek stanu w Windows update, będzie
  wypowiadany automatycznie, włączając w to widget czujnika pamięci.
* Wartości paska postępu i inne informacje, nie są wypowiadane
  automatycznie.
* Dla niektórych list rozwijanych i przycisków opcji, NVDA będzie wykrywał
  nazwę oraz wypowiadał zmiany wartości. 
* Dzwięki paska postępu głośności nie są więcej słyszane w kompilacji 1803 i
  nowszych.
* Więcej komunikatów o stanie Windows Update są wypowiadane, najważniejsze,
  gdy Windows update zobaczy błąd.
* W niektórych przypadkach, gdy używana jest nawigacja obiektowa, NVDA nie
  będzie się zachowywał  sposób nijaki, albo nie będzie odtwarzał dźwięku
  błedu.
* Okno dialogowe przypomnienia o aktualizacjach Windows, teraz jest
  rozpoznawane jako poprawne okno dialogowe.

## Skype

Uwaga: Niektóre funkcje nie będą działać w Skype 14 aplikacji uniwersalnej.

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
