# Windows App Essentials #

* Autoren: Joseph Lee, Derek Riemer und weitere
* [Stabile Version herunterladen][1]
* [Beta-Version herunterladen][2]
* [Entwicklerversion herunterladen][3]
* NVDA-Kompatibilität: 2023.1 und neuer

Hinweis: Ursprünglich als Windows 10 App Essentials bezeichnet, wurde es
2021 in Windows App Essentials umbenannt, um Windows 10 und zukünftige
Versionen wie Windows 11 zu unterstützen. Teile dieser Erweiterung beziehen
sich weiterhin auf den ursprünglichen Namen der Erweiterung.

Diese Erweiterung ist eine Sammlung von App-Modulen für verschiedene moderne
Windows-Apps sowie Verbesserungen und Korrekturen für bestimmte
Steuerelemente in Windows 10 und neuer.

Nachfolgend die beinhalteten App Module oder Unterstützungen für Module von
Windows-10-Apps (dazu weiter unten Deteils für jeden App Bereich)

* Cortana
* Moderne Tastatur
  (Emoji-Panel/Touch-Tastatur/Diktat/Sprachsteuerung/Hardware-Eingabevorschläge/Zwischenablage-Verlauf/Vorgeschlagene
  Aktionen/Editoren für moderne Eingabemethoden)
* Einstellungen (System-Einstellungen, Windows+I)
* Sprachzugang (Windows 11 Version 22H2)
* Wetter
* Verschiedene Module für Steuerungen und Funktionen wie die Mitteilung
  virtueller Desktops

Hinweise:

* Diese NVDA-Erweiterung benötigt Windows 10 Version 22H2 (Build 19045),
  Windows 11 Version 21H2 (Build 22000) oder neuere Versionen.
* Die Dauer der Unterstützung für Feature-Updates ist an die Dauer des
  Consumer-Supports (Home, Pro, Pro Education, Pro for Workstations
  Editionen) gebunden und die Erweiterung kann den Support für ein
  Feature-Update vor dem Ende des Consumer-Supports beenden. Unter
  aka.ms/WindowsTargetVersioninfo finden Sie weitere Informationen und
  Support-Informationen dazu.
* Obwohl eine Installation möglich ist, unterstützt diese Erweiterung keine
  Versionen von Windows Enterprise LTSC (Long-Term Servicing Channel) und
  Windows Server.
* Wenn der Updater für NVDA-Erweiterungen installiert ist und Add-on-Updates
  im Hintergrund aktiviert sind, wird Windows App Essentials auf nicht
  unterstützten Windows-Versionen überhaupt nicht installiert.
* Nicht alle Funktionen von Windows Insider Preview-Builds werden
  unterstützt. Dies gilt vor allem für Funktionen, die einer Untergruppe von
  Windows Insidern im Canary- und Dev-Channel vorgestellt werden.
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

## Allgemein

* Beim Öffnen, Schließen oder Umschalten zwischen virtuellen Desktops teilt
  NVDA nun den Namen des aktiven virtuellen Desktops mit (z. B. Desktop
  2). Dies ist nun fester Bestandteil in NVDA 2023.2.
* Die Taskleiste von Windows 10 und 11 wurde verbessert, u. a. durch die
  Anzeige der Ergebnisse der Neuanordnung von Symbolen beim Drücken von
  Alt+Umschalt+Pfeiltasten links/rechts (Windows 11) und durch die Anzeige
  der Position von Elementen beim Bewegen durch die Taskleistensymbole
  (Windows 10 und 11).
* In Apps wie der Datei-Explorer oder Notepad (Editor) in Windows 11 Version
  22H2, in denen Fenster mit Registerkarten unterstützt werden, zeigt NVDA
  den Namen und die Position der Registerkarten an, wenn zwischen ihnen
  gewechselt wird. Dies ist nun fester Bestandteil in NVDA 2023.2.

## Cortana

* Rückmeldungstexte von Cortana werden in den meisten Situationen
  angekündigt.

## Moderne virtuelle Tastaturen

Dazu gehören das Emoji-Bedienfeld, der Verlauf der Zwischenablage, die
Touch-Tastatur, Diktat-/Spracheingabe, Hardware-Eingabevorschläge,
vorgeschlagene Aktionen und moderne Eingabemethoden-Editoren für bestimmte
Sprachen in Windows 10 und 11. Aktivieren Sie bei der Anzeige von Emojis die
Unicode-Konsortium-Einstellung in den NVDA-Spracheinstellungen und setzen
Sie die Symbolebene auf "Einige" oder höher. Drücken Sie beim Einfügen aus
dem Verlauf der Zwischenablage in Windows 10 die Leertaste anstelle der
Eingabetaste, um das ausgewählte Element einzufügen.

* In Windows 11 Version 22H2 und neuer zeigt NVDA vorgeschlagene Aktionen
  an, wenn kompatible Daten wie Telefonnummern in die Zwischenablage kopiert
  werden.

## Einstellungen

* NVDA teilt den Namen optionaler Qualitätsupdates mit, falls vorhanden
  (Link zum Download und Jetzt installieren in Windows 10,
  Download-Schaltfläche in Windows 11).
* In Windows 11 werden die Breadcrumb-Leisten richtig erkannt.
* NVDA teilt Updates an den Windows Update-Status mit, während der Download
  und die Installation fortschreiten. Dies kann zu Sprachunterbrechungen
  führen, wenn Sie in den Einstellungen navigieren, während die Updates
  heruntergeladen und installiert werden. Wenn Sie Windows 11 verwenden und
  die UIA-Ereignisregistrierung in den erweiterten Einstellungen von NVDA
  auf Selektiv eingestellt ist, müssen Sie die Update-Liste fokussieren,
  sobald diese erscheint, damit NVDA den Update-Fortschritt mitteilen kann.

## Sprachzugang

Dies bezieht sich auf die in Windows 11 Version 22H2 eingeführte Funktion
für den Sprachzugang.

* NVDA teilt den Mikrofon-Status mit, wenn das Mikrofon über die
  Sprachzugriffsoberfläche umgeschaltet wird.

## Wetter

* Registerkarten wie"Prognose" und"Karten" werden als richtige
  Registerkarten erkannt (Patch von Derek Riemer).

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps

[2]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-dev

[4]: https://github.com/josephsl/wintenapps/wiki/w10changelog
