# Windows App Essentials #

* Autoren: Joseph Lee, Derek Riemer und weitere
* [Stabile Version herunterladen][1]
* [Beta-Version herunterladen][2]
* [Entwicklerversion herunterladen][3]
* NVDA-Kompatibilität: 2023.3.3 und neuer

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
* Einstellungen (System-Einstellungen, Windows+I)

Hinweise:

* Diese NVDA-Erweiterung benötigt Windows 10 Version 22H2 (Build 19045),
  Windows 11 Version 22H2 (Build 22621) oder neuere Versionen.
* Feature update support duration is tied to consumer support duration
  (Home, Pro, Pro Education, Pro for Workstations editions) and the add-on
  may end support for a feature update prior to end of consumer support. See
  <https://aka.ms/WindowsTargetVersioninfo> for more information and support
  dates.
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
[Änderungsprotokolle für Versionen der NVDA-Erweiterung][4].

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

## Einstellungen

* NVDA teilt Updates an den Windows Update-Status mit, während der Download
  und die Installation fortschreiten. Dies kann zu Sprachunterbrechungen
  führen, wenn Sie in den Einstellungen navigieren, während die Updates
  heruntergeladen und installiert werden. Wenn Sie Windows 11 verwenden und
  die UIA-Ereignisregistrierung in den erweiterten Einstellungen von NVDA
  auf Selektiv eingestellt ist, müssen Sie die Update-Liste fokussieren,
  sobald diese erscheint, damit NVDA den Update-Fortschritt mitteilen kann.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps

[2]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-dev

[4]: https://github.com/josephsl/wintenapps/wiki/w10changelog
