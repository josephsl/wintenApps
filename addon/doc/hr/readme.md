# Osnovni moduli za Windows aplikacije (Windows App Essentials) #

* Autori: Joseph Lee, Derek Riemer i drugi
* Preuzmi [stabilnu verziju][1]
* Preuzmi [beta verziju][2]
* Preuzmi [razvojnu verziju][3]
* NVDA kompatibilnost: 2023.2 i novije verzije

Napomena: Izvorno ime „Osnovni moduli za Windows 10 aplikacije”, preimenovan
je 2021. godine u „Osnovni moduli za Windows aplikacije” kako bi podržao
Windows 10 i buduća izdanja poput Windows 11. Dijelovi ovog dodatka će se i
nadalje odnositi na izvorno ime dodatka.

Ovaj NVDA dodatak je zbirka modula za razne moderne Windows aplikacije, kao
i poboljšanja i ispravci određenih kontrola u sustavu Windows 10 i novijim.

Uključeni su sljedeći moduli (za svaku aplikaciju postoji odlomak, gdje piše
što je uključeno):

* Moderna tipkovnica (ploča emojija, diktatiranje, tipkanje glasom,
  prijedlozi za unos hardverom, povijest međuspremnika, predložene radnje,
  moderni uređivači za unos)
* Postavke (postavke sustava, Windows+I)

Napomene:

* Ovaj dodatak zahtijeva Windows 10 22H2 (gradnja 19045), 11 22H2 (gradnja
  22621) ili novija izdanja.
* Trajanje podrške za aktualiziranje značajki povezano je s trajanjem
  korisničke podrške (izdanja Home, Pro, Pro Education, Pro for
  Workstations) i dodatak može prekinuti podršku za aktualiziranje značajki
  prije završetka korisničke podrške. Pogledaj
  aka.ms/WindowsTargetVersioninfo za više informacija i datume podrške.
* Mada je instalacija moguća, ovaj dodatak ne podržava izdanja Windows
  Enterprise LTSC (Long-Term Servicing Channel) i Windows Server.
* Windows Insider Preview gradnje neće podržati sve značajke, pogotovo
  značajke koje su predstavljene u podskupu „Windows Insiders” u kanalima
  canary i razvoja.
* The add-on may emulate changes included in Insider Preview builds which
  are subsequently removed, and for these changes, the add-on may remove
  them in future releases.
* Kanal dodataka u razvoju uključivat će promjene uključujući
  eksperimentalni sadržaj koji može, ali ne mora biti uključen u beta i
  stabilnim izdanjima, a beta kanal će sadržati promjene koje su planirane
  za buduća stabilna izdanja.
* Neke funkcije dodatka već jesu ili će postati dio NVDA čitača ekrana.
* Za najbolje iskustvo s aplikacijama koje ugrađuju web tehnologije i
  sadržaj kao što je izbornik Start i njegov kontekstni izbornik, aktiviraj
  postavku „Automatski modus fokusa za promjene fokusa” u ploči postavki
  modusa čitanja NVDA čitača.

Za popis promjena između izdanja dodatka, pogledaj dokument [s izmjenama
izdanja dodatka][4].

## Moderna tipkovnica

To uključuje ploču s emojijima, povijest međuspremnika,
diktatiranje/tipkanje govorom, prijedloge unosa hardvera i moderne uređivače
načina unosa za određene jezike u Windows verzijama 10 i 11. Kad pregledavaš
emojije, aktiviraj postavku Unicode Consortium u NVDA postavkama govora i
postavi razinu simbola na „neki” ili višu. Prilikom umetanja iz povijesti
međuspremnika u sustavu Windows 10, za umetanje odabranog elementa pritisni
tipku za razmak umjesto tipke Enter.

* U sustavu Windows 11 22H2 i novijim verzijama, NVDA će najaviti predložene
  radnje kad se kompatibilni podaci poput telefonskih brojeva kopiraju u
  međuspremnik.

## Postavke

* NVDA will report updates to Windows Update status as download and install
  progresses. This may result in speech interruption when navigating
  Settings app while updates are being downloaded and installed. If using
  Windows 11 and UIA event registration is set to selective from NVDA
  advanced settings panel, you must move focus to updates list as soon as
  they appear so NVDA can announce update progress.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps

[2]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-dev

[4]: https://github.com/josephsl/wintenapps/wiki/w10changelog
