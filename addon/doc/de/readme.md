# Windows App Essentials #

* Autoren: Joseph Lee, Derek Riemer und weitere

Hinweis: Ursprünglich als Windows 10 App Essentials bezeichnet, wurde es
2021 in Windows App Essentials umbenannt, um Windows 10 und zukünftige
Versionen wie Windows 11 zu unterstützen. Teile dieser Erweiterung beziehen
sich weiterhin auf den ursprünglichen Namen der Erweiterung.

Diese Erweiterung ist eine Sammlung von App-Modulen für verschiedene moderne
Windows-Apps sowie Verbesserungen und Korrekturen für bestimmte
Steuerelemente in Windows 10 und neuer.

Nachfolgend die beinhalteten App Module oder Unterstützungen für Module von
Windows-10-Apps (dazu weiter unten Deteils für jeden App Bereich)

* Moderne virtuelle Tastaturen
* Einstellungen (Windows+I)

Hinweise:

* This add-on requires 64-bit Windows 10 22H2 (build 19045), 11 22H2 (build
  22621), or later releases.
* Die Dauer der Unterstützung für Feature-Updates ist an die Dauer des
  Consumer-Supports (Home, Pro, Pro Education, Pro for Workstations
  Editionen) gebunden und die Erweiterung kann den Support für ein
  Feature-Update vor dem Ende des Consumer-Supports beenden. Unter
  <https://aka.ms/WindowsTargetVersioninfo> finden Sie weitere Informationen
  und Support-Informationen dazu.
* Obwohl eine Installation möglich ist, unterstützt diese Erweiterung keine
  Versionen von Windows Enterprise LTSC (Long-Term Servicing Channel) und
  Windows Server.
* Nicht alle Funktionen von Windows Insider Preview-Builds werden
  unterstützt. Dies gilt vor allem für Funktionen, die einer Untergruppe von
  Windows Insidern im Canary- und Dev-Channel vorgestellt werden.
* Die NVDA-Erweiterung kann Änderungen emulieren, die in
  Insider-Preview-Builds enthalten sind, die später entfernt werden, und für
  diese Änderungen kann die NVDA-Erweiterung sie in zukünftigen Versionen
  entfernen.
* Der Dev-Kanal der NVDA-Erweiterung wird Änderungen enthalten,
  einschließlich experimenteller Inhalte, die in den Beta- und
  Stable-Releases enthalten sein können oder auch nicht, und der Beta-Kanal
  wird Änderungen enthalten, die für zukünftige Stable-Releases geplant
  sind.
* Einige Zusatzfunktionen sind oder werden Teil von NVDA sein.
* Für eine optimale Nutzung von Anwendungen, die Webtechnologien und
  -inhalte einbetten, wie z. B. das Startmenü und sein Kontextmenü,
  aktivieren Sie die Einstellung "Automatischer Fokusmodus bei
  Fokusänderungen" im NVDA-Einstellungsdialogfeld für den Suchmodus.

Eine Liste der Änderungen, die zwischen den einzelnen Versionen der
NVDA-Erweiterung vorgenommen wurden, finden Sie im Dokument
[Änderungsprotokolle für Versionen der NVDA-Erweiterung][1].

## Allgemein

* In Windows 11 24H2 Insider Preview builds, quick settings (shellhost.exe)
  interface elements can be navigated using mouse and/or touch interaction.

## Moderne virtuelle Tastaturen

Dazu gehören das Emoji-Bedienfeld, der Verlauf der Zwischenablage, die
Touch-Tastatur, Diktat-/Spracheingabe, Hardware-Eingabevorschläge,
vorgeschlagene Aktionen und moderne Eingabemethoden-Editoren für bestimmte
Sprachen in Windows 10 und 11. Aktivieren Sie bei der Anzeige von Emojis die
Unicode-Konsortium-Einstellung in den NVDA-Spracheinstellungen und setzen
Sie die Symbolebene auf "Einige" oder höher. Drücken Sie beim Einfügen aus
dem Verlauf der Zwischenablage in Windows 10 die Leertaste anstelle der
Eingabetaste, um das ausgewählte Element einzufügen.

* In Windows 11, NVDA will announce suggested actions when compatible data
  such as phone numbers is copied to the clipboard. This is now part of NVDA
  2024.2.

## Einstellungen (Windows+I)

* NVDA will report updates to Windows Update status as download and install
  progresses. In Windows 10, this may result in speech interruption when
  navigating Settings app while updates are being downloaded and
  installed. In Windows 11, object navigation can be used in updates list to
  review update status for individual entries.

[[!tag dev stable]]

[1]: https://github.com/josephsl/wintenapps/wiki/w10changelog
