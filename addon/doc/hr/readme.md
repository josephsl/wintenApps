# Osnovni moduli za Windows aplikacije #

* Authors: Joseph Lee, Derek Riemer and others
* Preuzmi [stabilnu verziju][1]
* Preuzmi [razvojnu verziju][2]
* NVDA compatibility: 2021.2 and beyond

Napomena: Izvorno ime „Osnovni moduli za Windows 10 aplikacije”, preimenovan
je 2021. godine u „Osnovni moduli za Windows aplikacije” kako bi podržao
Windows 10 i buduća izdanja poput Windows 11. Dijelovi ovog dodatka će se i
nadalje odnositi na izvorno ime dodatka.

Ovaj NVDA dodatak je zbirka aplikacijskih modula za razne Windows
aplikacije, kao i poboljšanja i ispravci određenih kontrola u sustavu
Windows 10 i novijim.

Uključeni su sljedeći moduli (za svaku aplikaciju postoji odlomak, gdje piše
što je uključeno):

* Kalkulator (moderan)
* Cortana (konverzacije)
* Mail
* Karte
* Microsoft Solitaire Collection
* Microsoft Store
* Modern keyboard (emoji panel/dictation/voice typing/hardware input
  suggestions/clipboard history/modern input method editors)
* Osobe
* Postavke (postavke sustava, Windows+I)
* Vrijeme
* Dodatni moduli za kontrole kao što su pločice izbornika Start

Napomene:

* This add-on requires Windows 10 20H2 (build 19042) or later and is
  compatible with Windows 11.
* Although installation is possible, this add-on does not support Windows
  Enterprise LTSC (Long-Term Servicing Channel) and Windows Server releases.
* Neke funkcije dodatka već jesu ili će postati dio NVDA čitača ekrana.
* For entries not listed below, you can assume that features are part of
  NVDA, no longer applicable as the add-on does not support unsupported
  Windows releases such as old Windows 10 versions, or changes were made to
  Windows and apps that makes entries no longer applicable.
* Neke aplikacije podržavaju način kompaktnog preklapanja (na primjer,
  uvijek na vrhu u Kalkulatoru) i ovaj modus neće ispravno raditi s
  prijenosnom verzijom NVDA čitača.

Za popis promjena izvršenih između svakog izdanja dodatka, pogledaj
[dokument s izmjenama izdanja dodatka][3].

## Opće

* NVDA can announce suggestion count when performing a search in majority of
  cases, including when suggestion count changes as search progresses.
* In addition to UIA event handlers provided by NVDA, the following UIA
  events are recognized: drag start, drag cancel, drag complete, drop target
  drag enter, drop target drag leave, drop target dropped, layout
  invalidated. With NVDA's log level set to debug, these events will be
  tracked, and for UIA notification event, a debug tone will be heard if
  notifications come from somewhere other than the currently active
  app. Events built into NVDA such as name change and controller for events
  will be tracked from an add-on called Event Tracker.
* When opening, closing, reordering (Windows 11), or switching between
  virtual desktops, NVDA will announce active virtual desktop name (desktop
  2, for example).
* NVDA više neće najaviti veličinu teksta izbornika Start, kad se mijenjaju
  rezolucije ili položaj ekrana.
* Kad se pločice izbornika Start ili brze radnje za Action Center
  raspoređuju s tipkama Alt+šift+strelice, NVDA će najaviti podatke o
  povučenim stavkama ili o novom položaju povučene stavke.
* Najave kao što su promjena glasnoće/svjetline u File Explorereru i
  obavijesti aktualiziranja programa s Microsoft Store stranica, mogu se
  potisnuti isključivanjem opcije „Izvijesti o obavijestima” u NVDA
  postavkama prikaza objekata.

## Kalkulator

* NVDA više neće dvaputa najaviti poruku ekrana grafičkog kalkulatora.

## Cortana

Most items are applicable when using Cortana Conversations (Windows 10 2004
and later).

* Tekstualni odgovori Cortane najavljuju se u većini slučajeva.
* NVDA neće govoriti kad pričaš sa Cortanom.

## Mail

* Prilikom pregleda stavaka u popisu poruka, sada možete koristiti prečace
  za navigaciju po tablicama kako biste pregledali zaglavlja poruke.

## Karte

* NVDA svira zvuk za lokacije za lokacije na karti.
* Prilikom korištenja prikaza ulice te ako je opcija „korištenje tipkovnice”
  omogućena, NVDA će izgovarati adrese i kućne brojeve prilikom kretanja
  strelicama po karti.

## Microsoft Solitaire Collection

* NVDA će najaviti imenta karata i setove karata.

## Microsoft Store

* Nakon provjere nadogradnji aplikacija, aplikacije na popisu koje se
  trebaju nadograditi su pravilno označene.
* When downloading content such as apps and movies, NVDA will announce
  product name and download progress.

## Moderna tipkovnica

This includes emoji panel, clipboard history, dictation/voice typing,
hardware input suggestions, and modern input method editors for certain
languages. When viewing emojis, for best experience, enable Unicode
Consortium setting from NVDA's speech settings and set symbol level to
"some" or higher. When pasting from clipboard history in Windows 10, press
Space key instead of Enter key to paste the selected item. NVDA also
supports updated input experience panel in Windows 11.

* When an emoji group (including kaomoji and symbols group in Windows 10
  1903 or later) is selected, NVDA will no longer move navigator object to
  certain emojis.
* Added support for updated input experience panel (combined emoji panel and
  clipboard history) in Windows 11.

## Osobe

* Prilikom pretraživanja kontakata najavit će se prvi prijedlog, posebice,
  ako se koriste nedavna izdanja aplikacija.

## Postavke

* O većini informacija, poput trake napredovanja za ažuriranje Windowsa, se
  izvještava automatski.
* Vrijednosti trake napredovanja i druge informacije više se ne najavljuju
  dvaput.
* Odd control labels seen in certain Windows installations has been
  corrected.
* NVDA will announce the name of the optional quality update link if
  present, typically named "download and install now".

## Vrijeme

* Kartice poput „prognoza” i „karte” prepoznaju se kao ispravne kartice
  (zakrpu je napravio Derek Riemer).
* Prilikom čitanja prognoze, pritišćite strelice kako biste se kretali
  između stavaka. Pritišćite gornju ili donju strelicu kako biste se
  premještali između individualnih stavaka. Na primjer, pritiskom desne
  strelice čitač izgovara „Ponedjeljak: 79 stupnjeva, djelomično oblačno,
  …”, pritiskom na strelicu dolje izgovara „Ponedjeljak”. Ponovnim pritiskom
  čita sljedeću stavku (poput temperature). Ovo trenutačno radi za dnevnu i
  svakosatnu vremensku prognozu.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
