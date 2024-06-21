# Osnovni moduli za Windows aplikacije (Windows App Essentials) #

* Autori: Joseph Lee, Derek Riemer i drugi

Napomena: Izvorno ime „Osnovni moduli za Windows 10 aplikacije”, preimenovan
je 2021. godine u „Osnovni moduli za Windows aplikacije” kako bi podržao
Windows 10 i buduća izdanja poput Windows 11. Dijelovi ovog dodatka će se i
nadalje odnositi na izvorno ime dodatka.

Ovaj NVDA dodatak je zbirka modula za razne moderne Windows aplikacije, kao
i poboljšanja i ispravci određenih kontrola u sustavu Windows 10 i novijim.

Uključeni su sljedeći moduli (za svaku aplikaciju postoji odlomak, gdje piše
što je uključeno):

* Postavke (Windows+I)

Napomene:

* Ovaj dodatak zahtijeva 64-bitni Windows 10 22H2 (gradnja 19045), 11 22H2
  (gradnja 22621) ili novija izdanja.
* Trajanje podrške za aktualiziranje značajki povezano je s trajanjem
  korisničke podrške (izdanja Home, Pro, Pro Education, Pro for
  Workstations) i dodatak može prekinuti podršku za aktualiziranje značajki
  prije završetka korisničke podrške. Pogledaj
  <https://aka.ms/WindowsTargetVersioninfo> za više informacija i datume
  podrške.
* Mada je instalacija moguća, ovaj dodatak ne podržava izdanja Windows
  Enterprise LTSC (Long-Term Servicing Channel) i Windows Server.
* Windows Insider Preview gradnje neće podržati sve značajke, pogotovo
  značajke koje su predstavljene u podskupu „Windows Insiders” u kanalima
  canary i razvoja.

Za popis promjena između izdanja dodatka, pogledaj dokument [s izmjenama
izdanja dodatka][1].

## Postavke (Windows+I)

* NVDA će izvjestiti o napretku preuzimanja i instalacije nove Windows
  verzije. U sustavu Windows 10 to može rezultirati prekidom govora tijekom
  kretanja u aplikaciji Postavke tijekom aktualiziranja preuzimanja i
  instaliranja novih verzija. U sustavu Windows 11, kretanje po objektima se
  može koristiti u popisu novih verzija za pregled stanja aktualiziranja za
  pojedinačne unose.

[[!tag dev stable]]

[1]: https://github.com/josephsl/wintenapps/wiki/w10changelog
